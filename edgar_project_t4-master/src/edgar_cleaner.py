import os
from bs4 import BeautifulSoup

def clean_html_text(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    text = soup.get_text()
    return text


def write_clean_html_text_files(input_folder, dest_folder):
    for filename in os.listdir(input_folder):
        with open(os.path.join(input_folder, filename), 'r',encoding='windows-1252') as f: 
            file = f.read()
            text = clean_html_text(file)
            f.close()
            new_file = dest_folder+'/'+filename.replace('html','')+'.txt'
            f = open(new_file,'w')
            f.write(text)