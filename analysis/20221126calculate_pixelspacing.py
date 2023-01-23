import os
import re
import pandas as pd
import numpy as np
import pydicom
import csv
import itertools
import sys

#patients_dir="/nv/vol141/phys_nrf/Menglin/dataset_new/"
patients_dir="/Users/menglin/Dropbox/uva/research/krishni/code/dataset/CT/"

patients = ["SW"]
#patients = ['BE', 'BJ', 'BM', 'BS', 'CT', 'DC', 'DJ', 'FH', 'FJ', 'GD', 'HA', 'HD', 'HG', 'HW', 'KE', 'LD', 'LK', 'LL', 'LT', 'MB', 'MC', 'MK', 'MS', 'NJ', 'OW', 'RS', 'SB', 'SE', 'SJ', 'SL', 'SW', 'TB', 'TC', 'TH', 'WE', 'WM']

headers = ["SliceThickness", "PixelSpacing"]

headerinfo = {}
for p in patients:
    try:
        timesteps = sorted(next(os.walk(patients_dir+p))[1])
    except:
        print("Couldn't find patient directory at",patients_dir+p)
        exit(1)
    for timestep in timesteps:
        #ct_info = {}
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
        #for header in headers:
            #key = header
            #value = ct_img[header].value
        spacing = re.findall("\d+\.\d+",str(ct_img["PixelSpacing"].value))
        spacing = [float(a) for a in spacing]
        spacing.append(float(ct_img["SliceThickness"].value))
        print(spacing)
        spacingvalue = np.prod(spacing)
        #ct_info["Spacing"] = spacingvalue
        #headerinfo[p+timestep] = ct_info
        headerinfo[p+timestep] = spacingvalue
        #print(ct_info)
        #header_info = {header:ct_img[header] for header in headers}
        #print(header_info)
headers.insert(0,"Timestep")

with open('pixelspacing.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Timestep","Spacing"])
    for key, value in headerinfo.items():
       writer.writerow([key, value])
