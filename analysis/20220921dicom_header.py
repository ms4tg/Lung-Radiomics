import os
import re
import pandas as pd
import numpy as np
import pydicom

patients_dir="/media/sf_research/krishni/dataset/CT/"

patients = ["SW"]
extracted_info = ["ManufacturerModelName"]

def find_prefixed_file(directory, prefix):
    for i in os.listdir(directory):
        if re.search('^'+prefix, directory) is not None:
            return os.path.join(directory, i)
        return []

for p in patients:
    try:
        timesteps = sorted(os.listdir(patients_dir+p))
    except:
        print("Couldn't find patient directory at",patients_dir+p)
        exit(1)
    for timestep in timesteps:
        print("Reading CT from",p+"/"+timestep)
        for file in os.listdir(patients_dir+p+"/"+timestep):
            if file.startswith("CT"):
                ct_path = os.path.join(patients_dir+p+"/"+timestep, file)
                break
        #print(ct_path)
        ct_img = pydicom.dcmread(ct_path)
        print(ct_img.ManufacturerModelName)
