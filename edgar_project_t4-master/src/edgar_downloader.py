import requests
from bs4 import BeautifulSoup

def write_page(url, file_path):
    r = requests.get(url) # requests data from url stores it as html doc
    soup = BeautifulSoup(r.content,'html.parser') # creates parse tree object 
    soup = str(soup.prettify()) # enables us to see how tags are nested
    soup = "".join([x for x in soup if ord(x) < 128]) # unicode??
    f = open(file_path,'w',encoding='utf-8')
    f.write(soup) # writes to text file
    

def download_files_10k(ticker, dest_folder,date):
    d = {}
    r = requests.get('https://www.sec.gov/include/ticker.txt') # info on all tickers and CIKs
    text = r.text #speculative encoding
    text_lines = text.splitlines() # splits string into list where each line is an item 
    for line in text_lines:
        (key,val) = line.split('\t') # (splits where \n or \t (tab))
        d[key] = val
    try:
        CIK = d.get(ticker.lower())
    except:
        print('Invalid ticker entered')
        exit()


    endpoint = r"https://www.sec.gov/cgi-bin/browse-edgar" # browse all filings

    params ={'action':'getcompany', #action = getcompany
            'CIK':CIK,
            'type':'10-k',
            'owner':'exclude',
            'start':'',
            'output':'atom',
            'count':'100'}

    response = requests.get(url = endpoint,params=params)
    soup = BeautifulSoup(response.content,'lxml')

    list_dates = soup.findAll('filing-date')
    list_dates = [i.string for i in list_dates]
    list_doc_idx = soup.findAll('filing-href')
    list_doc_idx = [i.string for i in list_doc_idx]
    i=0
    for url in list_doc_idx:
        filing_date=list_dates[i]
        filing_year = filing_date[0:4]
        if filing_year>=date: # user inputs filter by date
            response = requests.get(url)
            soup = BeautifulSoup(response.content,'html.parser')

            table = soup.find("table", { "summary" : "Document Format Files" }) # Looks in <table summary = "Document Format Files">

            for row in table.findAll("tr")[1]: # Looks in table row for Document Link 
                cells = row.find('a')
                if cells !=-1 and cells is not None:
                    link = cells['href'].replace('/ix?doc=','') # removes /ix?doc=
                
            url = "https://www.sec.gov"+link
            file_path = dest_folder+ticker.upper()+'_10-k_'+filing_date+'.html'
            r = requests.get(url)
            write_page(url,file_path)
        i+=1

download_files_10k('aapl', r'\Users\chris\OneDrive\Documents\Kubrick Training\Week 7- Python\Edgar Project\HTMLTest', '2017')





