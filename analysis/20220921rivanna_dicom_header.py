import os
import re
import pandas as pd
import numpy as np
import pydicom
import csv
import itertools
import sys

#patients_dir="/media/sf_research/krishni/dataset/CT/"
patients_dir="/nv/vol141/phys_nrf/Menglin/dataset_new/"

#patients = ["SW"]
patients = ['BE', 'BJ', 'BM', 'BS', 'CT', 'DC', 'DJ', 'FH', 'FJ', 'GD', 'HA', 'HD', 'HG', 'HW', 'KE', 'LD', 'LK', 'LL', 'LT', 'MB', 'MC', 'MK', 'MS', 'NJ', 'OW', 'RS', 'SB', 'SE', 'SJ', 'SL', 'SW', 'TB', 'TC', 'TH', 'WE', 'WM']

headers = ["Manufacturer","ManufacturerModelName","SliceThickness","KVP","DataCollectionDiameter","FilterType","FocalSpots","ConvolutionKernel","ExposureTime","XRayTubeCurrent","Exposure", "PixelSpacing"]


headerinfo = {}
for p in patients:
    try:
        timesteps = sorted(next(os.walk(patients_dir+p))[1])
    except:
        print("Couldn't find patient directory at",patients_dir+p)
        exit(1)
    for timestep in timesteps:
        ct_info = {}
        print("Reading CT from",p+"/"+timestep)
        try:
            for file in os.listdir(patients_dir+p+"/"+timestep):
                if file.startswith("CT"):
                    ct_path = os.path.join(patients_dir+p+"/"+timestep, file)
                    break
        #print(ct_path)
        except:
            printf(patients_dir+p+"/"+timestep+"is not a directory")
            exit(1)
        ct_img = pydicom.dcmread(ct_path)
        for header in headers:
            key = header
            value = ct_img[header].value
            ct_info[key] = value
        headerinfo[p+timestep] = ct_info
        #header_info = {header:ct_img[header] for header in headers}
        #print(header_info)
headers.insert(0,"Timestep")

with open("patients_headerinfo.csv", "w") as f:
    w = csv.DictWriter(f, headers)
    w.writeheader()
    for key,val in sorted(headerinfo.items()):
        row = {'Timestep': key}
        row.update(val)
        w.writerow(row)
