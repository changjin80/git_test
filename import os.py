import os
# tkinter
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory
from nptdms import TdmsFile, TdmsWriter, ChannelObject
import soundfile as sf
import numpy as np

def read_tdms(fname,ch):
    tdms_file = TdmsFile.read(fname)
    group = tdms_file[np.array(tdms_file)[0]]
    channel = group[list(group._channels.keys())[ch]]
    data = channel[:]
    return data

root = Tk(  )

path= askdirectory()
root.destroy()

print(path)
sr=25000
ch=4

file_list = os.listdir(path)
file_list_tdms = [file for file in file_list if file.endswith(".tdms")]

for i in file_list_tdms:
    print(i)
    file_path=path+'\\'+i
    sig=read_tdms(file_path,ch)
    fname='.\\wav\\'+i.split('.')[0]
    sf.write(fname, sig, sr,subtype='float')