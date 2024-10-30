from nltk import ngrams
import os
from configure import *
import numpy as np
from tqdm import tqdm


def get_ngrams(text, n):
    n_grams = ngrams(text, n)
    return [' '.join(grams) for grams in n_grams]


total_n_grams = []
# file_dir = f'../{file_dir}'
file_dir = input_txt_dir
for file_title in tqdm(os.listdir(file_dir)):
    if file_title.endswith(".txt"):
        file_path = os.path.join(file_dir, file_title)
        f = open(file_path, "r")
        text = f.read()
        for re_str in re_strs:
            text = text.replace(re_str, ' ')
        total_n_grams.append(get_ngrams(text.split(), n))
        f.close()

np.save(gram_file, total_n_grams)