import pandas as pd
import datetime as dt
import numpy as np
import numpy.polynomial.polynomial as poly
from matplotlib.offsetbox import AnchoredText

#blacklist = ["0","BEPre","BJPre", "DCPreN1", "HAPreN1", "HWPreN7","LKPreN6", "SBPre","SJPreN2","SWPre", "SWPreN1"]
blacklist = ["0"]

p_data = pd.read_csv("rider_ITV.csv", header = 0)
columns = p_data["0"]
p_data = p_data.drop(columns = blacklist, axis =1) #removed extra patients and features
keys=[]
for i in p_data.index:
    try:
        val=float(p_data.iloc[:,0][i])

    except:
        keys.append(i)
        continue
p_data = p_data.drop(keys, axis =0)
#p_data = p_data.reset_index(drop = True)
columns = columns.drop(keys)
p_data.index = columns

p_data.to_csv('rider_144.csv', index=True, header=True, sep=',')
