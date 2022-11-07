import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import numpy as np
import numpy.polynomial.polynomial as poly
from matplotlib.offsetbox import AnchoredText

data = pd.read_csv("combat_data.csv", header = 0)
columns = data["0"]
data = data.drop(columns = "0", axis =1)
print(data.head)
volume = data.iloc[13]
print(columns)
print(type(columns))
#square=3
for index, feature in columns.items():
    print("plotting",index,"......")

    #plot scatter graph
    plt.figure()
    fig, axis = plt.subplots(1, 1)
    axis.scatter(volume, data.iloc[index], s=2, c='b')
    x = np.linspace(min(volume), max(volume), 1000)
    #find best fit line
    coefs=poly.polyfit(volume,data.iloc[index], 1)
    ffit = poly.Polynomial(coefs)    # instead of np.poly1d
    axis.plot(x, ffit(x), "red", linewidth=1)
    corr_matrix = np.corrcoef(volume, data.iloc[index])
    corr = corr_matrix[0,1]
    R_sq = corr**2
    at = AnchoredText(
    "R2:{:.4f}".format(R_sq), prop=dict(size=15), frameon=True, loc='upper left')
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")


    #find best fit polynomial
    coefs=poly.polyfit(volume,data.iloc[index], 4)
    ffit = poly.Polynomial(coefs)    # instead of np.poly1d
    axis.plot(x, ffit(x), "b", linewidth=1, alpha = 0.5)


    axis.add_artist(at)
    axis.set_title(feature, fontsize=12)
    axis.legend(["ITV"],loc='upper right')
    plt.savefig("/media/sf_research/krishni/output/221030both_line/"+str(index)+str(feature)+".png")
    print("graph plotted:",index)
