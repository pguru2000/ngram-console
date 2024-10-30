import nltk
from tqdm import tqdm
import numpy as np
import argparse
from configure import *
import os
import pathlib
import time

# Get the number of files in input folder
file_count = 0
for path in pathlib.Path(input_txt_dir).iterdir():
    if path.is_file():
        file_count += 1

total_n_grams = list(np.load(gram_file, allow_pickle=True))

# start_idx = args.idx * step
# end_idx = (args.idx+1) * step

pro_arr = []

for i in range(file_count):    
    pro_arr.append(i)

pbar = tqdm(total=file_count)
# result = np.zeros((101, file_count), np.uint8)
result = np.zeros((101, file_count, file_count), np.uint8)
# print(result)
# time.sleep(50)
spec_files = ''
#for i in range(start_idx, end_idx):
# print(pro_arr)
k5 = []
s5 = []
for i in pro_arr:
    f1_gram = total_n_grams[i]
    print("1gram", len(f1_gram))
    his = []
    for j in range(i + 1, file_count):
        f2_gram = total_n_grams[j]
        distance = nltk.jaccard_distance(set(f1_gram), set(f2_gram))
        
        distance = 100 - int(distance * 100)        
        for k in range(distance, 101):
            if k == 5:
                if (str(i) + "-" + str(j)) not in k5:
                    k5.append(str(i) + "-" + str(j))
                    print(str(i) + "-" + str(j))
                if i not in s5:
                    s5.append(i)
                if j not in s5:
                    s5.append(j)
                break
            
    pbar.update(1)
pbar.close()

print(len(k5))
print(len(s5))