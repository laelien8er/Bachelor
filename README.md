# Bachelorarbeit: KI-basiert versus klassisch - File Carving in der digitalen Fahrzeugforensik [AI-based versus Classical - File Carving in Digital Vehicle Forensics]

This repository holds the dataset, tooling and Docker environments used for a bachelor
thesis comparing machine-learning-based file carving against traditional file-carving
tools, applied to vehicle forensic artifacts:

- **CDR files** – Crash Data Retrieval / event data recorder exports
- **GPS logs** – vehicle location/track data (csv, gpx, xlsx)
- **DBC files** – CAN-bus signal database definitions

The core comparison is between [`sceadan`](https://github.com/UTSA-cyber/sceadan), an
ML content-type classifier, and established carving tools (Autopsy/Sleuthkit, foremost,
scalpel, bulk_extractor).

## Repository layout

```
Dataset/            Raw and generated test data
  original_Dataset/   Source files as downloaded (CDR, GPS, DBC)
  created_Dataset/    Derived files split/converted for carving experiments
                       (cdr, csv, gpx, xlsx, dbc)
  test_data_small/    Small hand-picked sample set for quick tests
  *.ipynb              Notebooks used to convert/split GPS and DBC data
  Dataset_documentation.txt  File counts per category
  Dataset_update.txt         Dataset sources and a running changelog

KI_Carver/          Docker environment for the ML-based carver (sceadan)
  Dockerfile


FileCarver/          Docker environment for traditional carving tools
  Dockerfile           Autopsy, Sleuthkit, foremost, scalpel, bulk_extractor

Test/                Ad-hoc scripts for building/converting test data
  Create_gps_files.py   Convert GPS csv data to gpx/xlsx/csv variants
  dbc_generate.py       Count/inspect DBC files
  get_files.py          Bulk-rename/move helper for GPS files
  gpx_files/, xls_files/  Small sample outputs
```

## Dataset sources

- GPS data: [Kaggle PVS dataset](https://www.kaggle.com/datasets/jefmenegazzo/pvs-passive-vehicular-sensors-datasets), [IO-VNBD](https://github.com/onyekpeu/IO-VNBD) ([paper](https://www.sciencedirect.com/science/article/pii/S2352340921001694)), [IEEE DataPort road vehicle localization dataset](https://ieee-dataport.org/open-access/road-vehicle-localization-dataset)
- CDR files: [NHTSA CISS CDR file downloads](https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/CISS/CDR%20Files/)
- DBC files: [commaai/opendbc](https://github.com/commaai/opendbc)

See [Dataset/Dataset_update.txt](Dataset/Dataset_update.txt) for the detailed
processing log and [Dataset/Dataset_documentation.txt](Dataset/Dataset_documentation.txt)
for per-category file counts.

## Running the environments

### ML carver (sceadan)

```
docker build -t ki_carver KI_Carver/
docker run -d -it -v /c/Bachelorarbeit/KI_Carver/case:/case ki_carver
docker exec -it <containerid> /bin/bash

# inside the container
cd tools && python3 sceadan_train.py --validate --data=/case/DATA --exp=<outputfolder>
cd tools && python3 sceadan_train.py --data=/case/DATA --exp=<outputfolder>
```

### Traditional carving tools (Autopsy et al.)

```
docker build -t file_carver FileCarver/
docker run -d -p 80:80 file_carver
docker cp <dataset-image> <containerid>:/usr/share
docker exec -it <containerid> /bin/bash
```

Autopsy itself is started inside the container with `bin/autopsy`.

## Notes

- `Dataset` and `Test` are not tracked with Git LFS; the repository is large (multiple
  GB) because it contains the full forensic test corpus rather than pointers to it.
- `KI_Carver/case/DATA` intentionally mirrors `Dataset/created_Dataset` — it's the
  volume that gets mounted into the sceadan container for training/validation.
