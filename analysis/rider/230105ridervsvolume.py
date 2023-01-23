import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import numpy as np
import numpy.polynomial.polynomial as poly
from matplotlib.offsetbox import AnchoredText

#blacklist = ["0","BEPre","BJPre", "DCPreN1", "HAPreN1", "HWPreN7","LKPreN6", "SBPre","SJPreN2","SWPre", "SWPreN1"]

data = pd.read_csv("rider_144.csv", header = 0)
columns = data["0"] #save the header for plotting
data = data.drop(columns = "0", axis =1)

p_data = pd.read_csv("original.csv", header = 0)
p_data = p_data.drop(columns = "0", axis =1) #removed extra patients and features

rider_postcombat = pd.read_csv("rider_postcombat.csv", header = 0)
rider_postcombat = rider_postcombat.drop(columns = "0", axis =1)

contrast_postcombat = pd.read_csv("contrast_postcombat.csv", header = 0)
contrast_postcombat = contrast_postcombat.drop (columns = "0", axis =1)

#a_data = pd.read_csv("aorta_combat_data.csv", header = 0)
#a_data = a_data.drop(columns = "0", axis =1) #removed extra patients and features

#volume = p_data.iloc[18]
volume = data.iloc[-1]
p_volume = p_data.iloc[-1]

#a_volume = a_data.iloc[18]

rider_volume = rider_postcombat.iloc[-1]
contrast_volume = contrast_postcombat.iloc[-1]

r_value = []
#print(columns)
#print(type(columns))
#square=3
for index, feature in columns.items():
    print("plotting",index,"......")

    #plot scatter graph
    plt.figure()
    fig, axis = plt.subplots(1, 2,figsize=(15, 7))
    axis[0].scatter(volume, data.iloc[index], s=2, c='r',label = "RIDER without contrast pre Combat")
    axis[0].scatter(p_volume, p_data.iloc[index], s=2, c='b', label = "With contrast pre Combat")

    x = np.linspace(min(volume), max(volume), 1000)
    #find best fit line
    coefs=poly.polyfit(volume,data.iloc[index], 1)
    ffit = poly.Polynomial(coefs)
    axis[0].plot(x, ffit(x), c = "r", linewidth=1)
    #axis.text(0.5,0.9, 'y = ' + '{:.2f}'.format(coefs[0]) + ' + {:.2f}'.format(coefs[1]) + 'x', c = "r", fontsize=15, transform=axis.transAxes)
    corr_matrix = np.corrcoef(volume, data.iloc[index])
    corr = corr_matrix[0,1]
    R_sq1 = corr**2
    t =axis[0].text(0.1,0.9, r'$R^2=${:.4f}'.format(R_sq1), c = "r", fontsize=10, transform=axis[0].transAxes)
    t.set_bbox(dict(facecolor='white', alpha=0.7, edgecolor='white'))


    x = np.linspace(min(p_volume), max(p_volume), 1000)
    coefs=poly.polyfit(p_volume, p_data.iloc[index], 1)
    ffit = poly.Polynomial(coefs)    # instead of np.poly1d
    axis[0].plot(x, ffit(x), c = "b", linewidth=1)
    #axis.text(0.5,0.8, 'y = ' + '{:.2f}'.format(coefs[0]) + ' + {:.2f}'.format(coefs[1]) + 'x', c = "b", fontsize=15, transform=axis.transAxes)
    corr_matrix = np.corrcoef(p_volume, p_data.iloc[index])
    corr = corr_matrix[0,1]
    R_sq2 = corr**2
    t =axis[0].text(0.1,0.85, r'$R^2=${:.4f}'.format(R_sq2), c = 'b', fontsize=10, transform=axis[0].transAxes)
    t.set_bbox(dict(facecolor='white', alpha=0.7, edgecolor='white'))


    axis[1].scatter(rider_volume, rider_postcombat.iloc[index], s=2, c='r',label = "RIDER without contrast post ComBat")
    #axis[1].scatter(volume_cc_aorta, a_data.iloc[index], s=2, c='b', label = "Aorta Combat")
    axis[1].scatter(contrast_volume, contrast_postcombat.iloc[index], s=2, c='b', label = "With contrast post Combat")

    x = np.linspace(min(rider_volume), max(rider_volume), 1000)
    #find best fit line
    coefs=poly.polyfit(rider_volume,rider_postcombat.iloc[index], 1)
    ffit = poly.Polynomial(coefs)
    axis[1].plot(x, ffit(x), c = "r", linewidth=1)
    #axis.text(0.5,0.9, 'y = ' + '{:.2f}'.format(coefs[0]) + ' + {:.2f}'.format(coefs[1]) + 'x', c = "r", fontsize=15, transform=axis.transAxes)
    corr_matrix = np.corrcoef(rider_volume, rider_postcombat.iloc[index])
    corr = corr_matrix[0,1]
    R_sq1 = corr**2
    t =axis[1].text(0.1,0.9, r'$R^2=${:.4f}'.format(R_sq1), c = "r", fontsize=10, transform=axis[1].transAxes)
    t.set_bbox(dict(facecolor='white', alpha=0.7, edgecolor='white'))


    x = np.linspace(min(contrast_volume), max(contrast_volume), 1000)
    coefs=poly.polyfit(contrast_volume,contrast_postcombat.iloc[index], 1)
    ffit = poly.Polynomial(coefs)    # instead of np.poly1d
    axis[1].plot(x, ffit(x), c = "b", linewidth=1)
    #axis.text(0.5,0.8, 'y = ' + '{:.2f}'.format(coefs[0]) + ' + {:.2f}'.format(coefs[1]) + 'x', c = "b", fontsize=15, transform=axis.transAxes)
    corr_matrix = np.corrcoef(contrast_volume, contrast_postcombat.iloc[index])
    corr = corr_matrix[0,1]
    R_sq2 = corr**2
    t =axis[1].text(0.1,0.85, r'$R^2=${:.4f}'.format(R_sq2), c = 'b', fontsize=10, transform=axis[1].transAxes)
    t.set_bbox(dict(facecolor='white', alpha=0.7, edgecolor='white'))



    axis[0].set_title(feature, fontsize=12)
    axis[0].legend(loc='upper right')
    axis[0].set_xlabel("Volume (cc)")

    axis[1].set_title(feature, fontsize=12)
    axis[1].legend(loc='upper right')
    axis[1].set_xlabel("Volume (cc)")

    plt.savefig("/Users/menglin/Dropbox/uva/research/krishni/code/output/230105ridervscontrast/"+str(index)+str(feature)+".png")
    print("graph plotted:",index)

#df = pd.DataFrame(r_value, columns =['Combat',"Aorta_Combat","Original"],index = columns)
#df.to_csv('r_value.csv', index=True, header=True, sep=',')
