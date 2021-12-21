import csv;import os
import glob
import re
import string
import ref_data as rd

def write_document_sentiments(input_folder, output_file):
    column_headers = ['Symbol', 'Report Type', 'Filing Date', 'Positive', 'Negative',
                 'Uncertainty', 'Litigious', 'Constraining', 'Superfluous',
                 'Interesting','Modal']

    f_out = open(output_file, 'w')
    wr = csv.writer(f_out, lineterminator='\n')
    wr.writerow(column_headers)
    file_list = glob.glob(input_folder)

    file_path = "./LoughranMcDonald_MasterDictionary_2018.csv"
    _,lm_dictionary = rd.get_sentiment_word_dict(file_path)

    file_list = glob.glob(input_folder+'/*.*')

    for file in file_list:
        with open(file, 'r', encoding='UTF-8') as f_in:
            doc = f_in.read()
        # doc = re.sub('(May|MAY)', ' ', doc)  # drop all May month references
        doc = doc.upper()  # for this parse caps aren't informative so shift

        output_data = get_data(doc,lm_dictionary)
        output_data[0] = os.path.basename(file).split('_')[0]
        output_data[1] = '10-k'
        output_data[2] = os.path.basename(file).split('_')[-1].replace('..txt','')
        wr.writerow(output_data)
    

def get_data(doc,lm_dictionary):

    vdictionary = {}
    odata = [0] * 11
    
    tokens = re.findall('\w+', doc)
    for token in tokens:
        if not token.isdigit() and len(token) > 1 and token in lm_dictionary:
            if token not in vdictionary:
                vdictionary[token] = 1
            if lm_dictionary[token].positive: odata[3] += 1
            if lm_dictionary[token].negative: odata[4] += 1
            if lm_dictionary[token].uncertainty: odata[5] += 1
            if lm_dictionary[token].litigious: odata[6] += 1
            if lm_dictionary[token].constraining: odata[7] += 1
            if lm_dictionary[token].superfluous: odata[8] += 1
            if lm_dictionary[token].interesting: odata[9] += 1
            if lm_dictionary[token].modal: odata[10] += 1 
    return odata

write_document_sentiments('/Users/alexanderrobertson/Documents/Cleaned', '/Users/alexanderrobertson/Documents/Output/sentiment_factors.csv')