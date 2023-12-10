import os

# get every gps file from MagLand
startdir = "D:\Bachelorarbeit\Dataset\original_files\GPS_Data\kaggle"
movedir = "D:\Bachelorarbeit\Dataset\original_files\GPS_Data\MagLand_GPS"


for path, subdirs, files in os.walk(startdir):

    for file in files:
        os.rename(os.path.join(path, file), startdir + path.split("\\")[-1].replace(" ","") + file)

