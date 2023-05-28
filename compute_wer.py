# Code to compute WER + SER

import worderrorrate
import pandas as pd
from tqdm import tqdm

punctuation = ["'",'!','(',')','-','[',']','{','}',';',':','"',',','<','>','.','/','?','@','#','$','%','^','&','*','_','~']

# Remove punctuation
def remove_punctuation(sentence):
    return ''.join([c for c in sentence if c not in punctuation])

# Remove capitalization
def remove_capitalization(sentence):
    return sentence.lower()

# Word Error Rate
def compute_wer(df, ref_name, hyp_name, preprocess=lambda x: x):
    num, den = 0, 0
    for _, row in df.iterrows():
        wer = worderrorrate.WER(preprocess(row[ref_name]).split(' '), preprocess(row[hyp_name]).split(' '))
        num += wer.nerr
        den += len(wer.ref)
    return num/den

lans = ['Catalan', 'Dutch', 'French', 'Italian', 'Lithuanian',
        'Polish', 'Romanian', 'Spanish', 'Croatian', 'English',
        'German', 'Latvian', 'Norwegian', 'Portuguese', 'Russian',
        'Ukranian']

for l in lans:
    filename = "results/wer_ser_{}.txt".format(l)
    print(l)
    with open(filename, 'w') as fp:
        for lp in tqdm(lans):
            input_path = "output_validate/{}/predictions_{}_post.csv".format(l,lp)

            df = pd.read_csv(input_path)

            wer_generated = compute_wer(df, 'Actual Text', 'Post Generated Text')
            wer_generated_nopunc = compute_wer(df, 'Actual Text', 'Post Generated Text', remove_punctuation)
            wer_generated_nocap = compute_wer(df, 'Actual Text', 'Post Generated Text', remove_capitalization)
            wer_source = compute_wer(df, 'Actual Text', 'Source Text')
            wer_source_nopunc = compute_wer(df, 'Actual Text', 'Source Text', remove_punctuation)
            wer_source_nocap = compute_wer(df, 'Actual Text', 'Source Text', remove_capitalization)

            fp.write(f'{lp}: \n')
            fp.write(f'Word Error Rate - Generated Text = {wer_generated} \n')
            fp.write(f'Word Error Rate - Generated Text (punc) = {wer_generated_nocap} \n')
            fp.write(f'Word Error Rate - Generated Text (cap) = {wer_generated_nopunc} \n')
            fp.write(f'Word Error Rate - Source Text = {wer_source} \n')
            fp.write(f'Word Error Rate - Source Text (punc) = {wer_source_nocap} \n')
            fp.write(f'Word Error Rate - Source Text (cap) = {wer_source_nopunc} \n')
            fp.write("\n")
