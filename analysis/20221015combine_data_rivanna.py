import pandas as pd
import numpy as np
import pydicom

patients_dir="/nv/vol141/phys_nrf/Menglin/dataset_new/"
#patients = ['BE', 'BJ', 'BM', 'BS', 'CT', 'DC', 'DJ', 'FH', 'FJ', 'GD', 'HA', 'HD', 'HG', 'HW', 'KE', 'LD', 'LK', 'LL', 'LT', 'MB', 'MC', 'MK', 'MS', 'NJ', 'OW', 'RS', 'SB', 'SE', 'SJ', 'SL', 'SW', 'TB', 'TC', 'TH', 'WE', 'WM']
patients = ['BE','BJ','CT','FJ','LK','HD','MB','MK','SB','SW']
blacklist = ["BEPre","BJPre", "DCPreN1", "HAPreN1", "HWPreN7","LKPreN6", "SBPre","SJPreN2","SWPre", "SWPreN1"]

ITV={p:pd.read_csv(patients_dir+p+"/Aorta.csv", header = None, index_col=0) for p in patients}

data_list = []
for p in patients:
    header=[]
    timesteps = ITV[p].iloc[0]
    for timestep in timesteps:
        header.append (p+timestep)
    ITV[p].iloc[0,:] = header
    data_list.append(ITV[p])
data_merged = pd.concat(data_list, axis = 1)
new_header = data_merged.iloc[0]
data_merged = data_merged[1:]
data_merged.columns = new_header

data_merged = data_merged.drop(columns = blacklist，axis=1)
    #print(ITV)
    #data.index = list(ITV.index)
    #output = pd.merge(data, ITV,how = "left")
print(data_merged)
data_merged.to_csv("Aorta_data.csv")
