from edgar_cleaner import write_clean_html_text_files as clean_files
from edgar_downloader import download_files_10k as df10k
from edgar_sentiment_wordcount import write_document_sentiments as write_sent
from ref_data import get_sp100
import os,shutil
from tkinter import *
from tkinter import filedialog,messagebox,ttk

def edgar_process(ticker_input,file_path,date,popup):
    popup.title('Working...')
    Label(popup,text=f'Scraping Edgar Filings after {date}').pack()
    progress_var = IntVar()
    progress = 0
    progressbar = ttk.Progressbar(popup,orient=HORIZONTAL, variable=progress_var, maximum=500)
    progressbar.pack(side="bottom")

    os.chdir(file_path)
    cwd = file_path

    # Download SEC filings to Output folder
    try:
        shutil.rmtree(ticker_input.upper()+'_Output')
        os.mkdir(ticker_input.upper()+'_Output')
    except:
        os.mkdir(ticker_input.upper()+'_Output')
    popup.update()
    progress += 100
    progress_var.set(progress)
    dl_file_path = cwd+'/'+ticker_input.upper()+'_Output/'
    df10k(ticker_input,dl_file_path,date)

    popup.update()
    progress += 100
    progress_var.set(progress)
    # Clean files to cleaned folder
    try:
        shutil.rmtree(ticker_input.upper()+'_Cleaned/')
        os.mkdir(ticker_input.upper()+'_Cleaned')
    except:
        os.mkdir(ticker_input.upper()+'_Cleaned')
    popup.update()
    progress += 100
    progress_var.set(progress)

    clean_file_path = cwd+'/'+ticker_input.upper()+'_Cleaned/'
    clean_files(dl_file_path[:-1],clean_file_path)

    popup.update()
    progress += 100
    progress_var.set(progress)


    # Write document sentiments to file
    sentiment_path = cwd+'/'+ticker_input.upper()+'_sentiments.csv'
    write_sent(clean_file_path, sentiment_path)
    popup.update()
    progress += 100
    progress_var.set(progress)
    popup.update()
