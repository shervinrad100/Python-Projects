from tkinter import *
from tkinter import filedialog,messagebox,ttk
import edgar,pandas as pd
from ref_data import get_sp100
import datetime
from PIL import Image,ImageTk
from ref_data import get_yahoo_data
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

def select_file():
    global file_dir
    file_path= filedialog.askdirectory()
    file_dir.set(file_path)

def perform_edgar():
    global file_dir
    global ticker_var
    global date_var
    file_path = file_dir.get()
    if file_path=='':
        messagebox.showerror(title='Folder Select Error', message='No folder selected!')
    else:
        ticker = ticker_var.get()
        date = date_var.get()
        popup = Toplevel()
        edgar.edgar_process(ticker,file_path,date,popup)
        popup.destroy()
        messagebox.showinfo(title='Process Info', message=f'Edgar Process Complete in path {file_path}')

def get_yahoo():
    global file_dir
    global ticker_var
    global date_var
    file_path = file_dir.get()
    if file_path=='':
        messagebox.showerror(title='Folder Select Error', message='No folder selected!')
    else:
        ticker = ticker_var.get()
        date = date_var.get()
        today = str(datetime.datetime.today().date())
        start_date = date+'-01-01'
        prices = get_yahoo_data(start_date,today,ticker)
        file_path = file_path+'/'+date+'_'+ticker+'.csv'
        prices.to_csv(path_or_buf=file_path)
        messagebox.showinfo(title='Process Info', message=f'Yahoo financials scraped into {file_path}')

def plot_yahoo(root):
    global file_dir
    global ticker_var
    global date_var
    ticker = ticker_var.get()
    file_path = file_dir.get()
    date = date_var.get()
    try:
        prices = pd.read_csv(file_path+'/'+date+'_'+ticker+'.csv')
        prices['formatted_date']=pd.to_datetime(prices['formatted_date'])
        prices.set_index('formatted_date', inplace=True)
        sentiments = pd.read_csv(file_path+'/'+ticker+'_sentiments.csv')
    except:
        messagebox.showerror(title='File Select Error', message='No file present!')
        return
    sentiments['Filing Date'] = pd.to_datetime(sentiments['Filing Date'])

    sentiments.sort_values(by=['Filing Date'], inplace=True, ascending=True)

    info = pd.merge(prices,sentiments,left_index=True,right_on='Filing Date')
    info.set_index('Filing Date', inplace=True)
    info = info.drop(columns=['high','low','open','close','volume','1d returns','2d returns','3d returns','5d returns','10d returns','Symbol_x','Symbol_y','Report Type'])
    info['Total Words'] = info['Positive']+info['Negative']+info['Uncertainty']+info['Litigious']+info['Constraining']+info['Superfluous']+info['Interesting']+info['Modal']
    info[['Positive','Negative','Uncertainty','Litigious','Constraining','Superfluous','Interesting','Modal']]=info[['Positive','Negative','Uncertainty','Litigious','Constraining','Superfluous','Interesting','Modal']].div(info['Total Words'], axis=0)

    normalised_prices=(info['adjclose']-info['adjclose'].min())/(info['adjclose'].max()-info['adjclose'].min())
    normalised_Positive=(info['Positive']-info['Positive'].min())/(info['Positive'].max()-info['Positive'].min())
    normalised_Negative=(info['Negative']-info['Negative'].min())/(info['Negative'].max()-info['Negative'].min())
    normalised_Uncertainty=(info['Uncertainty']-info['Uncertainty'].min())/(info['Uncertainty'].max()-info['Uncertainty'].min())
    normalised_Litigious=(info['Litigious']-info['Litigious'].min())/(info['Litigious'].max()-info['Litigious'].min())
    normalised_Constraining=(info['Constraining']-info['Constraining'].min())/(info['Constraining'].max()-info['Constraining'].min())
    normalised_Superfluous=(info['Superfluous']-info['Superfluous'].min())/(info['Superfluous'].max()-info['Superfluous'].min())
    normalised_Interesting=(info['Interesting']-info['Interesting'].min())/(info['Interesting'].max()-info['Interesting'].min())
    normalised_Modal=(info['Modal']-info['Modal'].min())/(info['Modal'].max()-info['Modal'].min())
    info = info.drop(columns='Total Words')

    dates=info.index
    fig = Figure(figsize=(5, 4), dpi=100)
    a = fig.add_subplot(111)
    a.plot(dates,normalised_prices,label='Price')
    a.plot(dates,normalised_Positive,label='Positive')
    a.plot(dates,normalised_Negative,label='Negative')
    a.plot(dates,normalised_Uncertainty,label='Uncertainty')
    a.plot(dates,normalised_Litigious,label='Litigious')
    a.plot(dates,normalised_Constraining,label='Constraining')
    a.plot(dates,normalised_Superfluous,label='Superfluous')
    a.plot(dates,normalised_Interesting,label='Interesting')
    a.plot(dates,normalised_Modal,label='Modal')
    fig.legend()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=2,columnspan=4,sticky=N+S+W+E)

def splash_screen():
    root = Tk()
    root.title('Load Screen')
    canvas = Canvas(root)
    image = Image.open('./Team4SEC.png')
    image = ImageTk.PhotoImage(image)
    Label(root, image=image).pack()
    progressbar = ttk.Progressbar(orient=HORIZONTAL, length=720, mode='determinate')
    progressbar.pack(side="bottom")
    progressbar.start()
    root.after(5250, root.destroy)
    root.mainloop()

def main_gui():
    global file_dir
    global ticker_var
    global date_var
    tickers = get_sp100()
    year = datetime.datetime.today().year
    years = list(range(year, year - 11, -1))
    root = Tk()
    root.geometry('800x500')
    root.grid_columnconfigure(0,weight=1)
    root.grid_columnconfigure(1,weight=1)
    root.grid_columnconfigure(2,weight=1)
    root.grid_columnconfigure(3,weight=1)
    root.grid_rowconfigure(0,weight=1)
    root.grid_rowconfigure(1,weight=1)
    root.grid_rowconfigure(2,weight=1)
    root.grid_rowconfigure(3,weight=1)
    root.title('Edgar Project Team 4')
    Label(root, text="Desired Ticker").grid(row=0,sticky=N+S+E+W)
    Label(root, text="From which year?").grid(row=0,column=2,sticky=N+S+E+W)

    file_dir = StringVar()
    ticker_var = StringVar(root)
    ticker_var.set(tickers[0])
    date_var = StringVar(root)
    date_var.set(years[0])

    e1 = OptionMenu(root,ticker_var,*tickers)
    e2 = OptionMenu(root,date_var,*years)

    e1.grid(row=0, column=1,sticky=N+S+E+W,padx=5)
    e2.grid(row=0, column=3,sticky=N+S+E+W,padx=5)

    filebut = Button(root, text="Select Destination Folder", command=select_file)
    filebut.grid(row=1, column=0,sticky=W+E,padx=5)

    edgbut = Button(root, text="Run Edgar", command=perform_edgar)
    edgbut.grid(row=1, column=1,sticky=W+E,padx=5)

    yahoobut = Button(root, text="Get Yahoo Finance data", command=get_yahoo)
    yahoobut.grid(row=1, column=2,sticky=W+E,padx=5)

    plotbut = Button(root, text="Plot data", command=lambda: plot_yahoo(root))
    plotbut.grid(row=1, column=3,sticky=W+E,padx=5)

    root.mainloop()

splash_screen()
main_gui()