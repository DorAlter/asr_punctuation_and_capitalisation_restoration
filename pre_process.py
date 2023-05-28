# Code to remove punctuation + further pre-processing

import os
import pandas as pd

MIN_SENTENCE_LENGTH = 15
MAX_SENTENCE_LENGTH = 512

def removePunctuation(textInput):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    result = ""

    for i in textInput:
        i = i.lower()
        if i not in punctuations:
            result += i
    return result

def remove_single_quote(sentence):
    num_quotes = len([c for c in sentence if c == '"'])
    if num_quotes == 1:
        return ''.join([c for c in sentence if c != '"'])
    return sentence

def preprocess(inputText):
    inputText = inputText.replace('\n\n', ' ').replace('\n',' ')
    inputText = inputText.replace('   ', ' ').replace('  ', ' ')
    end_symbols = ['!', '?', '.']
    start_index = 0
    sentences = []
    for i, c in enumerate(inputText):
        for e_s in end_symbols:
            if c == e_s:
                sentences.append(inputText[start_index:i+1])
                start_index = i+2   
    return [remove_single_quote(s) for s in sentences if len(s) > MIN_SENTENCE_LENGTH and len(s) < MAX_SENTENCE_LENGTH][10000:25000]

def remove_before_dash(line):
    pattern = '  —   '
    pattern_index = line.find(pattern)
    if pattern_index != -1:
        return line[pattern_index+len(pattern):]
    else:
        return line

def readlines(filename):
    lines = []
    with open(filename, 'r') as fp:
        lines = fp.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    return lines


def read_data(file_location):
    data_dict = {'source' : [], 'target' : []}
    data = ''.join(readlines(file_location))
    preprocessedData = preprocess(data)
    noPunctuationData = [removePunctuation(p) for p in preprocessedData]
    data_dict['target'] = preprocessedData
    data_dict['source'] = noPunctuationData
    return data_dict


lans = ['Catalan', 'Dutch', 'French', 'Italian', 'Lithuanian',
        'Polish', 'Romanian', 'Spanish', 'Croatian', 'English',
        'German', 'Latvian', 'Norwegian', 'Portuguese', 'Russian',
        'Ukranian']

for lan in lans:
   file_location = "articles/{}_pre.txt".format(lan)
   data_dict = read_data(file_location)
   df = pd.DataFrame.from_dict(data_dict)
   print(len(df))
   file_out = "training_data/data_{}.csv".format(lan)
   df.to_csv(file_out, index=False)
