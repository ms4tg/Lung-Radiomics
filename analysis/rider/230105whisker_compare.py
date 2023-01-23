import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import numpy as np
import numpy.polynomial.polynomial as poly
from matplotlib.offsetbox import AnchoredText

rider = pd.read_csv("rider_144.csv", header = 0)
columns = rider["0"] #save the header for plotting
#delete the last radimoics features since it gives very large standard deviation (~144)

contrast = pd.read_csv("original.csv", header = 0)

rider_postcombat = pd.read_csv("rider_postcombat.csv", header = 0)

contrast_postcombat = pd.read_csv("contrast_postcombat.csv", header = 0)


data = [rider, contrast, rider_postcombat, contrast_postcombat]
data_new =[]
for df in data:
    df = df.drop(columns = "0", axis =1)
    df = df.T.reset_index(drop = True)
    #print(df.head)
    summary = df.describe()
    print(summary)
    for i in range(112):
        # Grab the mean and std of attribute i
        mean = summary.iloc[1, i]
        std = summary.iloc[2, i]
        df.iloc[:,i:(i + 1)] = (df.iloc[:,i:(i + 1)] - mean) / std
    summary = df.describe()
    print(summary)
    df = df.T.iloc[:112]
    data_new.append(df)

print(data_new[0].iloc[0])

plt.figure()
fig, axis = plt.subplots(1, 2, figsize = (60, 130),sharey =True)

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

def set_violin_color(parts, color):
    for pc in parts['bodies']:
        pc.set_facecolor(color)
        pc.set_edgecolor(color)
        pc.set_alpha(1)

#for index, feature in columns.items():
for index in range(112):
    print("plotting",index,"......")

    #red = axis[0].boxplot(data_new[0].iloc[index],positions = [index-0.1],showfliers=True, flierprops={'marker': '+', 'markersize': 2,'markerfacecolor': 'r'},vert = 0)
    #blue = axis[0].boxplot(data_new[1].iloc[index],positions = [index+0.1],showfliers=True, flierprops={'marker': '+', 'markersize': 2,'markerfacecolor': 'b'},vert = 0)
    red = axis[0].violinplot(data_new[0].iloc[index],positions = [3*index-0.5], showmeans=False, showmedians=True, vert =0,
        showextrema=True)#,showfliers=True, flierprops={'marker': '+', 'markersize': 2,'markerfacecolor': 'r'},vert = 0)
    blue = axis[0].violinplot(data_new[1].iloc[index],positions = [3*index+0.5], showmeans=False, showmedians=True, vert=0,
        showextrema=True)#,showfliers=True, flierprops={'marker': '+', 'markersize': 2,'markerfacecolor': 'b'},vert = 0)


    set_violin_color(red, 'r') # colors are from http://colorbrewer2.org/
    set_violin_color(blue, 'b')

    red = axis[1].violinplot(data_new[2].iloc[index],positions = [3*index-0.5], showmeans=False, showmedians=True, vert =0,
        showextrema=True)#,showfliers=True, flierprops={'marker': '+', 'markersize': 2,'markerfacecolor': 'r'},vert = 0)
    blue = axis[1].violinplot(data_new[3].iloc[index],positions = [3*index+0.5], showmeans=False, showmedians=True, vert=0,
        showextrema=True)#,showfliers=True, flierprops={'marker': '+', 'markersize': 2,'markerfacecolor': 'b'},vert = 0)


    set_violin_color(red, 'r') # colors are from http://colorbrewer2.org/
    set_violin_color(blue, 'b')
    #axis.hist(data.iloc[index], density=True,color ='r', alpha = 0.5,bins=30, label = "ComBat")
    #axis.hist(p_data.iloc[index], density=True,color ='b', alpha = 0.5,bins=30, label = "Original")

    #red = axis[1].boxplot(data_new[2].iloc[index],positions = [index-0.1],showfliers=True, flierprops={'marker': '+', 'markersize': 2,'markerfacecolor': 'r'},vert = 0)
    #blue = axis[1].boxplot(data_new[3].iloc[index],positions = [index+0.1],showfliers=True, flierprops={'marker': '+', 'markersize': 2,'markerfacecolor': 'b'},vert = 0)
    #set_box_color(red, 'r') # colors are from http://colorbrewer2.org/
    #set_box_color(blue, 'b')

axis[0].plot([], c='r', label='Pre-Combat: without contrast')
axis[0].plot([], c='b', label='Pre-Combat: with contrast')

axis[1].plot([], c='r', label='Post-Combat: without contrast')
axis[1].plot([], c='b', label='Post-Combat: with contrast')

axis[0].set_title("Pre-Combat", fontsize=30)
axis[1].set_title("Post-Combat", fontsize = 30)

axis[0].legend(loc='upper right')
axis[1].legend(loc='upper right')

axis[0].set_yticks(np.arange(0,336,3), columns[:-1], rotation=20, ha='right', fontsize=20)
#axis[1].set_yticks(visible = False)

plt.savefig("/Users/menglin/Dropbox/uva/research/krishni/code/output/230105whisker_compare/"+"violin_compare.png")
    #print("graph plotted:",index)
