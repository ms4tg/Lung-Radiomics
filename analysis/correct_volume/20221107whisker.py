import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import numpy as np
import numpy.polynomial.polynomial as poly
from matplotlib.offsetbox import AnchoredText

blacklist = ["0","BEPre","BJPre", "DCPreN1", "HAPreN1", "HWPreN7","LKPreN6", "SBPre","SJPreN2","SWPre", "SWPreN1"]
batch_number= [5,5,5,1,6,6,6,12,5,5,9,9,9,9,9,8,2,3,5,4,1,1,4,10,5,5,3,5,12,13,13,5,4,11,5,5,2,5,2,2,2,4,8,7,2,8,2,2,4,5,12,12,3,11,3,3,3,2,3,2,2,2,4,2,12,12,5,12,6,5,7,2,2,13,12,12,1,1,6,2,5,2,12,12,5,1,1,2,14,12,12,5,5,5,2,2,4,2,2,2,2,10,4,2,2,2,2,5,12,14,2,2,2,2,2,5,12,12,12,5,5,1,1,1,6,6,5,6,11,2,4,4,4,4,3,4,3,7,2,2,2,2,2,2]

batch_count = np.arange(min(batch_number),max(batch_number)+1,1)
print(batch_count)
data = pd.read_csv("combat_data.csv", header = 0)
columns = data["0"] #save the header for plotting
data = data.drop(columns = "0", axis =1)
data.set_index(columns)
data = data.T
data["Batch"] = batch_number #add batch as one column

batch = {}
for i in batch_count:
    batch[i] = data[(data["Batch"] == i)]

p_data = pd.read_csv("original.csv", header = 0)
p_data = p_data.drop(columns = "0", axis =1)
p_data = p_data.T
p_data["Batch"] = batch_number #add batch as one column
p_data = p_data.astype(float)

p_batch = {}
for i in batch_count:
    p_batch[i] = p_data[(p_data["Batch"] == i)]
print(p_batch)


#p_data = p_data.reset_index(drop = True)
#p_data = p_data.astype(float)

#print(data.head)
#print(p_data.head)

volume = data.iloc[13].div(1000)
p_volume = p_data.iloc[13].div(1000)

#print(columns)
#print(type(columns))
#square=3
for index, feature in columns.items():
    print("plotting",index,"......")

    def set_box_color(bp, color):
        plt.setp(bp['boxes'], color=color)
        plt.setp(bp['whiskers'], color=color)
        plt.setp(bp['caps'], color=color)
        plt.setp(bp['medians'], color=color)

    #plot scatter graph
    plt.figure()
    fig, axis = plt.subplots(1, 1)
    for i in batch_count:
        red = axis.boxplot(batch[i][index],positions = [i-0.1],showfliers=False)
        blue = axis.boxplot(p_batch[i][index],positions = [i+0.1],showfliers=False)
        set_box_color(red, 'r') # colors are from http://colorbrewer2.org/
        set_box_color(blue, 'b')
    #axis.hist(data.iloc[index], density=True,color ='r', alpha = 0.5,bins=30, label = "ComBat")
    #axis.hist(p_data.iloc[index], density=True,color ='b', alpha = 0.5,bins=30, label = "Original")

    axis.plot([], c='r', label='ComBat')
    axis.plot([], c='b', label='Original')
    axis.set_xticks(batch_count,batch_count)
    axis.set_title(feature, fontsize=12)
    axis.legend(loc='upper right')
    plt.savefig("/media/sf_research/krishni/code/output/221107whisker/"+str(index)+str(feature)+".png")
    #print("graph plotted:",index)
