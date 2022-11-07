import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import numpy as np
from matplotlib.offsetbox import AnchoredText

FilePath="/Users/menglinshi/Dropbox/uva/research/rider_data/"
#I had written that CT has some missing data, not sure if that was fixed but they look alright now
#BJ data appears to be bad, I'm including them for now to avoid cherry-picking patients
#MK is missing some data

#blacklist=["DA","MJ","BB","HR","HI"]
#dates=pd.read_csv(FilePath+"Dates.csv")
#patients=list(dates.columns)
#for i in blacklist:
    #if i in patients:
        #patients.remove(i)

patients = list(range(1,25))
#d={p:[dt.datetime.strptime(i,"%m/%d/%y") for i in dates[p]
      #if type(i)==type("")] for p in patients}
#d={p:[(d[p][0]-i).days for i in d[p]] for p in d}


ITV={p:pd.read_csv(FilePath+str(p)+"/GTVp_test_auto.csv") for p in patients}
#PTV={p:pd.read_csv(FilePath+p+"/PTV.csv") for p in patients}
#Random_ITV={p:pd.read_csv(FilePath+p+"/R_ITV.csv") for p in patients}
#Random_PTV={p:pd.read_csv(FilePath+p+"/R_PTV.csv") for p in patients}

keys=[]
for i in ITV[patients[0]].index:
    try:
        val=float(ITV[patients[0]]["Test"][i])
        keys.append(i)
    except:
        continue

ITVdata={}
#RITVdata={}
for k in keys:
    X,y=[],[]
    for p in patients:
        #X+=d[p]
        volume = list(ITV[p].iloc[35])[1:]
        volume = [float(i) for i in volume]
        X+=volume
        #Normalize to Pre, might want to change this
        add=list(ITV[p].iloc[k])[1:]
        add=[float(i)/float(1) for i in add] #/float(add[0])
        y+=add
    if not len(X)==len(y):
        print(p,"X and y different lengths")
        continue
    ITVdata[k]=(X,y)

#    X,y=[],[]
#    for p in patients:
        #X+=d[p]
    #    volume = list(Random_ITV[p].iloc[32])[1:]
    #    volume = [float(i) for i in volume]
    #    X+=volume
        #Normalize to Pre, might want to change this
    #    add=list(Random_ITV[p].iloc[k])[1:]
    #    add=[float(i)/float(1) for i in add] #/float(add[0])
    #    y+=add
#    RITVdata[k]=(X,y)

#square=3
for i in keys:
    print("plotting",i,"......")
    plt.figure()
    fig, axis = plt.subplots(1, 1)
    axis.scatter(ITVdata[i][0],ITVdata[i][1], s=2, c='b')
    fit=np.polyfit(ITVdata[i][0], ITVdata[i][1], 1)
    p=np.poly1d(fit)
    axis.plot(ITVdata[i][0], p(ITVdata[i][0]), "b", linewidth=1)
            #axis.scatter(RITVdata[i][0],RITVdata[i][1], s=2, c='r')
            #fit=np.polyfit(RITVdata[i][0], RITVdata[i][1], 1)
            #p=np.poly1d(fit)
            #axis.plot(RITVdata[i][0], p(RITVdata[i][0]), "r", linewidth=1)
    corr_matrix = np.corrcoef(ITVdata[i][0], ITVdata[i][1])
    corr = corr_matrix[0,1]
    R_sq = corr**2
    at = AnchoredText(
    ("R2:"+str(R_sq)), prop=dict(size=15), frameon=True, loc='upper left')
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    axis.add_artist(at)
    axis.set_title(ITV[patients[0]]["Unnamed: 0"][i], fontsize=12)
    axis.legend(["ITV"],loc='upper right')
    plt.savefig("/Users/menglinshi/Dropbox/uva/research/220729rider/"+str(i)+".png")
    print("graph plotted:",i)
