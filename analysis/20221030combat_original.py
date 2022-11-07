import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import numpy as np
import numpy.polynomial.polynomial as poly
from matplotlib.offsetbox import AnchoredText

blacklist = ["0","BEPre","BJPre", "DCPreN1", "HAPreN1", "HWPreN7","LKPreN6", "SBPre","SJPreN2","SWPre", "SWPreN1"]

data = pd.read_csv("combat_data.csv", header = 0)
columns = data["0"] #save the header for plotting
data = data.drop(columns = "0", axis =1)

p_data = pd.read_csv("patients_data.csv", header = 0)
p_data = p_data.drop(columns = blacklist, axis =1) #removed extra patients and features
keys=[]
for i in p_data.index:
    try:
        val=float(p_data.iloc[:,0][i])

    except:
        keys.append(i)
        continue
p_data = p_data.drop(keys, axis =0)
p_data = p_data.reset_index(drop = True)
p_data = p_data.astype(float)

print(data.head)
print(p_data.head)

volume = data.iloc[13].div(1000)
p_volume = p_data.iloc[13].div(1000)

#print(columns)
#print(type(columns))
#square=3
for index, feature in columns.items():
    print("plotting",index,"......")

    #plot scatter graph
    plt.figure()
    fig, axis = plt.subplots(1, 1)
    axis.scatter(volume, data.iloc[index], s=2, c='r',label = "ComBat")
    axis.scatter(p_volume, p_data.iloc[index], s=2, c='b', label = "Original")

    x = np.linspace(min(volume), max(volume), 1000)
    #find best fit line
    coefs=poly.polyfit(volume,data.iloc[index], 1)
    ffit = poly.Polynomial(coefs)
    axis.plot(x, ffit(x), c = "r", linewidth=1)
    axis.text(0.5,0.9, 'y = ' + '{:.2f}'.format(coefs[0]) + ' + {:.2f}'.format(coefs[1]) + 'x', c = "r", fontsize=15, transform=axis.transAxes)
    corr_matrix = np.corrcoef(volume, data.iloc[index])
    corr = corr_matrix[0,1]
    R_sq = corr**2
    axis.text(0.1,0.9, r'$R^2=${:.4f}'.format(R_sq), c = "r", fontsize=15, transform=axis.transAxes)

    coefs=poly.polyfit(p_volume,p_data.iloc[index], 1)
    ffit = poly.Polynomial(coefs)    # instead of np.poly1d
    axis.plot(x, ffit(x), c = "b", linewidth=1)
    axis.text(0.5,0.8, 'y = ' + '{:.2f}'.format(coefs[0]) + ' + {:.2f}'.format(coefs[1]) + 'x', c = "b", fontsize=15, transform=axis.transAxes)
    corr_matrix = np.corrcoef(p_volume, p_data.iloc[index])
    corr = corr_matrix[0,1]
    R_sq = corr**2
    axis.text(0.1,0.8, r'$R^2=${:.4f}'.format(R_sq), c = 'b', fontsize=15, transform=axis.transAxes)

    axis.plot(x, x, c = "grey", label = "slope = 1")

    #at = AnchoredText(
    #"R2:{:.4f}".format(R_sq), prop=dict(size=15), frameon=True, loc='upper left')
    #at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")


    #find best fit polynomial
    #coefs=poly.polyfit(volume,data.iloc[index], 4)
    #ffit = poly.Polynomial(coefs)    # instead of np.poly1d
    #axis.plot(x, ffit(x), "b", linewidth=1, alpha = 0.5)

    axis.set_title(feature, fontsize=12)
    axis.legend(loc='upper right')
    plt.savefig("/Users/menglin/Dropbox/uva/research/krishni/output/221030both_line/"+str(index)+str(feature)+".png")
    print("graph plotted:",index)
