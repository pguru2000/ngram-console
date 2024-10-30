import string
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import table

import tkinter as tk
from tkinter import filedialog

from tkinter import messagebox
import os

def png_save_dialog():
    f = filedialog.asksaveasfilename(initialfile = "test", filetypes=[("Png files", "*.png")])
    if f != '':    
        if f.endswith('.png') is False:
            f += '.png'
        file_save_action(f)

def pdf_save_dialog():
    f = filedialog.asksaveasfilename(initialfile = "test", filetypes=[("Pdf files", "*.pdf")])
    
    if f != '':
        if f.endswith('.pdf') is False:
            f += '.pdf'
        file_save_action(f)

def close_window():
    root.destroy()

def file_save_action(file_name):
    ax = plt.subplot(111, frame_on=False)
    ax.figure.set_size_inches(5, 20)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

    rows, cols = 5, 10
    labels = ['Taux de similitude','Nombre de textes']

    result_arr = []
    result_txt = '../result.txt'
    with open(result_txt, 'r') as rows:
        for i, row in enumerate(rows):
            result_arr.append([row.split(' | ')[0], row.split(' | ')[1].strip('\n')])

    # df = pd.DataFrame(np.random.randint(0, 100, size=(100, 2)), columns=labels)
    df = pd.DataFrame(result_arr, columns=labels)
    
    table(ax, df, loc='center')  # where df is your data frame
    # plt.tight_layout()
    plt.savefig(file_name)
    messagebox.showinfo(title=None, message=f" File saved in {file_name}")

root = tk.Tk(className='Save result')
root.geometry("500x200")
btn_png_save = tk.Button(root, text='Save result as a PNG', command=png_save_dialog)
btn_png_save.grid(row=0, column=0, padx=200, pady=10)

btn_pdf_save = tk.Button(root, text='Save result as a PDF', command=pdf_save_dialog)
btn_pdf_save.grid(row=1, column=0, padx=200, pady=10)

btn_close = tk.Button(root, text='Close', command=close_window)
btn_close.grid(row=2, column=0, padx=200, pady=10)
# btn_png_save.pack()
# btn_pdf_save.pack()
# btn_close.pack()
root.mainloop()