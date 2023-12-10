# generate new dbc files from commaai dbc dataset (https://github.com/commaai/opendbc)

import os
import pandas

startdir = r"D:\Bachelorarbeit\Dataset\original_files\DBC_Files"

for path, subdirs, files in os.walk(startdir):
    i = 0
    for file in files:

        i += 1

    print(i)
