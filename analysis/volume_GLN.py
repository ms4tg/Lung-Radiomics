import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import numpy as np

FilePath="/Users/menglinshi/Dropbox/uva/research/emery_data/"
#I had written that CT has some missing data, not sure if that was fixed but they look alright now
#BJ data appears to be bad, I'm including them for now to avoid cherry-picking patients
#MK is missing some data
blacklist=["DA","MJ","BB","HR","HI"]
dates=pd.read_csv(FilePath+"Dates.csv")
patients=list(dates.columns)
for i in blacklist:
    if i in patients:
        patients.remove(i)


#d={p:[dt.datetime.strptime(i,"%m/%d/%y") for i in dates[p]
      #if type(i)==type("")] for p in patients}
#d={p:[(d[p][0]-i).days for i in d[p]] for p in d}


ITV={p:pd.read_csv(FilePath+p+"/ITV.csv") for p in patients}
#PTV={p:pd.read_csv(FilePath+p+"/PTV.csv") for p in patients}
Random_ITV={p:pd.read_csv(FilePath+p+"/R_ITV.csv") for p in patients}
#Random_PTV={p:pd.read_csv(FilePath+p+"/R_PTV.csv") for p in patients}

keys=[]
for i in ITV[patients[0]].index:
    try:
        val=float(ITV[patients[0]]["Pre"][i])
        keys.append(i)
    except:
        continue
print(patients)

ITVdata={}
RITVdata={}
for k in keys:
    X,y=[],[]
    for p in patients:
        #print (ITV[p].head())
        #X+=d[p]
        ITV[p]=ITV[p].set_index("Unnamed: 0").T
        #ITV = ITV[p]
        #ITV.iloc[30,1:]=ITV.iloc[30,1:].astype(float)
        #print(ITV.head())
        #ITV = ITV[ITV.iloc[30,1:]>1000]
        ITV[p]['original_shape_MeshVolume'] = ITV[p]['original_shape_MeshVolume'].astype(float)
        #print(ITV["original_shape_MeshVolume"]>1000)
        ITV[p]=ITV[p][(ITV[p]['original_shape_MeshVolume'])>1000]
        #print(ITV[p].head())
        #ITV[p]=ITV[p].T
        #volume = list(ITV.iloc[30])[1:]
        volume = list(ITV[p]["original_shape_MeshVolume"])
        volume = [float(i) for i in volume]
        X+=volume
        #Normalize to Pre, might want to change this
        ITV[p]=ITV[p].T.reset_index()
        add=list(ITV[p].iloc[k])[1:]
        #add=[float(i)/float(1) for i in add] #/float(add[0]) not normalized
        y+=add
        #print (ITV[p].head())
    if not len(X)==len(y):
        print(p,"X and y different lengths")
        continue
    ITVdata[k]=(X,y)

    #X,y=[],[]
    #for p in patients:
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
    axis.set_title(ITV[patients[0]]["Unnamed: 0"][i], fontsize=12)
    axis.legend(["ITV"],loc='upper right')
    plt.savefig("/Users/menglinshi/Dropbox/uva/research/test/"+str(i)+".png")
    print("graph plotted:",i)
