# create different filetypes with GPS data
# https://gpx-converter.readthedocs.io/en/latest/usage.html file -> gpx
# https://docs.pyexcel.org/en/latest/ csv -> xls

from gpx_converter import Converter
import os
import csv
import pandas
import chardet


def get_files(startdir):
    """

    :param startdir: Path to directory
    :return: list of contained files
    """

    file_list = []

    for path, subdirs, files in os.walk(startdir):
        for file in files:
            file_list.append(os.path.join(path, file))
    return file_list


def convert_file_to_gpx(file_list, encoding="utf-8", sep=",",
                        outputdir=None):  # parallelisieren wenn möglich sonst no no
    for file in file_list:
        # create dataframe
        df = pandas.read_csv(file, encoding=encoding, sep=sep)

        # get filepath for output
        if outputdir:
            outf = outputdir + "\\" + file.split("\\")[-1].split(".")[0] + ".gpx"
        else:
            outf = file.split(".")[0] + ".gpx"

        # check if needed columns there (latitude, longitude)
        lat = ""
        long = ""
        for name in list(df.columns.values):
            if "latitude" in name: lat = name
            if "longitude" in name: long = name

        if lat and long:
            Converter.dataframe_to_gpx(df, lats_colname=lat, longs_colname=long, output_file=outf)
        else:
            print(file + " is not a gps file")


def get_encoding(filepath):
    with open(filepath, "rb") as f:
        content = f.read()
    return chardet.detect(content)['encoding']


def get_separator(filepath):
    with open(filepath, 'r') as csvfile:
        delimiter = str(csv.Sniffer().sniff(csvfile.read()).delimiter)
        return delimiter


def convert_file_to_xlsx(filelist, encoding="utf-8", sep=",", outputdir=None):
    for file in filelist:
        df = pandas.read_csv(file, encoding=encoding, sep=sep)

        if outputdir:
            outf = outputdir + file.split("\\")[-1].split(".")[0] + ".xlsx"
        else:
            outf = file.split(".")[0] + ".xlsx"
        with pandas.ExcelWriter(outf) as writer:
            df.to_excel(writer)


def convert_file_to_csv(filelist, outputdir=None):
    for file in filelist:
        df = pandas.read_csv(file, encoding='utf8')
        print(df)
        if outputdir:
            outf = outputdir + "\\" + file.split("\\")[-1].split(".")[0] + ".csv"
            df.to_csv(outf)

        break


def split_files(file_list, encoding="utf-8", sep=",", outputdir=None):
    for file in file_list:
        df = pandas.read_csv(file, encoding=encoding, sep=sep)
        part_1 = df.sample(frac=0.5)
        part_2 = df.drop(part_1.index)

        if outputdir:
            outp1 = outputdir + file.split("\\")[-1].split(".")[-1] + "1.csv"
            outp2 = outputdir + file.split("\\")[-1].split(".")[-1] + "2.csv"

            part_1.to_csv(outp1)
            part_2.to_csv(outp2)


files = get_files("D:\Bachelorarbeit\Dataset\original_files\GPS_Data\MagLand_GPS")
convert_file_to_csv(files, outputdir="D:\Bachelorarbeit\Dataset\_ds\csv")
