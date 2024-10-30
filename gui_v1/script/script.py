import nltk
from tqdm import tqdm
import numpy as np
import argparse
from configure import *
import os
import pathlib

# Get the number of files in input folder
file_count = 0
for path in pathlib.Path(input_txt_dir).iterdir():
    if path.is_file():
        file_count += 1

parser = argparse.ArgumentParser()
parser.add_argument("--idx", type=int, help="the index of the script")
parser.add_argument("--count", type=int, help="the cont of the scripts")
args = parser.parse_args()
total_n_grams = list(np.load(gram_file, allow_pickle=True))
step = int(file_count / args.count)
# start_idx = args.idx * step
# end_idx = (args.idx+1) * step

pro_arr = []

for i in range(file_count):
    if args.idx == i % args.count:
        pro_arr.append(i)

pbar = tqdm(total=step)
result = np.zeros((101, file_count), np.uint8)
spec_files = ''
#for i in range(start_idx, end_idx):
# print(pro_arr)

for i in pro_arr:
    f1_gram = total_n_grams[i]
    his = []
    for j in range(i + 1, file_count):
        f2_gram = total_n_grams[j]
        distance = nltk.jaccard_distance(set(f1_gram), set(f2_gram))
        distance = 100 - int(distance * 100)        
        for k in range(distance, 101):
            result[k][i] += 1
            result[k][j] += 1
    pbar.update(1)
pbar.close()

file_path = 'result/{:02d}.npy'.format(args.idx)
np.save(file_path, result)
if args.idx == 10:
    hist = np.zeros((101, file_count), np.uint8)
    for file_title in os.listdir(result_path):
        if file_title.endswith('.npy'):
            file_path = os.path.join(result_path, file_title)
            his = np.load(file_path)
            hist |= his
            os.remove(file_path)
    os.remove(gram_file)
    hist_sum = np.sum(hist, axis=1, dtype=np.uint32)
    with open('somefile.txt', 'w') as the_file:
        for i, h in enumerate(hist_sum):
            result = str(i + 1) + ' | ' + str(h) + '\n'
            the_file.write(result)