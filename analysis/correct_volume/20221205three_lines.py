import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import numpy as np
import numpy.polynomial.polynomial as poly
from matplotlib.offsetbox import AnchoredText

#blacklist = ["0","BEPre","BJPre", "DCPreN1", "HAPreN1", "HWPreN7","LKPreN6", "SBPre","SJPreN2","SWPre", "SWPreN1"]
volume_cc = [0.543989,0.307469,0.270602,0.294556,0.113893,0.105675,0.086302,2.793354,3.754931,3.464973,2.885628,2.407288,0.955745,0.515751,0.587344,0.760665,0.317817,0.336014,0.026839,0.840198,24.80681,24.81538,1.214741,0.069002,1.330683,0.865402,6.217733,8.838524,22.29957,13.45396,5.293841,11.31172,1.287479,0.517282,0.134989,0.298215,0.281392,0.25157,0.254139,0.826999,0.376701,0.364232,14.58643,10.30087,11.88325,12.84121,16.79919,15.44599,12.89173,0.934294,0.430711,0.318178,0.470876,0.337972,0.318074,1.900194,1.828563,17.52965,11.12782,10.58354,9.555532,9.410438,12.20094,1.509109,1.098115,1.31549,1.204187,1.077141,1.208082,1.279293,1.21951,0.65565,0.901221,2.186296,1.130676,0.804662,0.729812,0.669171,0.707358,1.391828,0.6368,0.876609,0.60598,0.656037,0.750328,0.166734,0.059049,56.04538,4.793916,3.970056,3.765012,3.471913,2.981021,2.623494,12.80783,7.25507,7.851116,10.72525,4.96983,4.794593,5.309189,6.638619,0.790063,0.173439,0.012722,0.007643,0.009741,0.026178,0.021006,0.848025,1.655571,0.698129,1.212755,1.084803,0.84129,0.720527,0.927787,1.936296,0.80734,2.070896,1.769047,4.054928,0.640349,0.621673,0.38552,0.233815,0.194337,0.334552,16.10505,12.8423,2.543108,2.50403,2.170324,5.501503,4.873517,1.400708,3.372005,2.84035,2.397581,2.604199,2.546663,2.266599,1.747864,1.588563]

pixelspacing = [1.126271,0.87349,0.688554,0.732727,0.869412,0.617981,0.684933,0.774426,0.551223,0.881672,0.961876,0.839361,1.067871,0.971283,1.179405,0.833148,0.821233,0.688554,0.516133,1.126271,0.927357,0.923157,1.192092,1.301931,0.84114,1.09406,1.039929,1.053334,0.494403,0.656323,0.751539,0.531941,0.8532,0.976004,0.69582,0.952764,0.728994,0.597553,0.670552,0.952764,1.192092,0.778274,1.192092,1.126271,0.974196,1.192092,0.617981,0.845152,1.03548,0.649266,0.635267,0.681324,1.192092,1.379477,1.000232,1.192092,0.789876,0.617981,0.670552,0.617981,0.740222,0.666981,0.621419,0.617981,0.782133,0.531941,0.476151,0.617981,0.786,0.706792,1.192092,1.192092,1.192092,1.192092,0.762939,1.192092,1.062317,1.048857,1.017781,0.81728,0.829167,0.987172,0.869412,0.485234,0.87349,0.952764,1.135559,0.952764,0.59082,0.885778,0.688554,1.004604,0.944258,0.927357,1.192092,1.192092,1.192092,1.192092,1.192092,1.192092,1.117018,1.009369,0.8532,0.894017,0.706792,0.849171,0.69582,0.429154,0.368519,0.476151,0.617981,0.631791,1.071338,1.192092,0.952764,0.611134,0.770587,0.587468,0.944258,1.071338,0.931568,1.075863,0.914784,1.144885,1.053334,0.677724,0.75913,0.774426,1.087738,0.952764,1.084944,1.112408,1.126271,1.192092,1.071338,1.192092,1.084944,0.931568,0.918966,1.008989,0.944258,0.995869,0.793762,0.927357]


data = pd.read_csv("combat_data.csv", header = 0)
columns = data["0"] #save the header for plotting
data = data.drop(columns = "0", axis =1)

p_data = pd.read_csv("patients_144.csv", header = 0)
p_data = p_data.drop(columns = "0", axis =1) #removed extra patients and features

a_data = pd.read_csv("aorta_combat_data.csv", header = 0)
a_data = a_data.drop(columns = "0", axis =1) #removed extra patients and features

#volume = p_data.iloc[18]
volume = pixelspacing
p_volume = data.iloc[18]
a_volume = a_data.iloc[18]

r_value = []
#print(columns)
#print(type(columns))
#square=3
for index, feature in columns.items():
    print("plotting",index,"......")

    #plot scatter graph
    plt.figure()
    fig, axis = plt.subplots(1, 2,figsize=(15, 7))
    axis[0].scatter(volume, data.iloc[index], s=2, c='r',label = "ComBat")
    axis[0].scatter(volume, a_data.iloc[index], s=2, c='b', label = "Aorta Combat")
    axis[0].scatter(volume, p_data.iloc[index], s=2, c='grey', label = "Original")

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


    #x = np.linspace(min(p_volume), max(p_volume), 1000)
    coefs=poly.polyfit(volume,p_data.iloc[index], 1)
    ffit = poly.Polynomial(coefs)    # instead of np.poly1d
    axis[0].plot(x, ffit(x), c = "grey", linewidth=1)
    #axis.text(0.5,0.8, 'y = ' + '{:.2f}'.format(coefs[0]) + ' + {:.2f}'.format(coefs[1]) + 'x', c = "b", fontsize=15, transform=axis.transAxes)
    corr_matrix = np.corrcoef(volume, p_data.iloc[index])
    corr = corr_matrix[0,1]
    R_sq2 = corr**2
    t =axis[0].text(0.1,0.7, r'$R^2=${:.4f}'.format(R_sq2), c = 'grey', fontsize=10, transform=axis[0].transAxes)
    t.set_bbox(dict(facecolor='white', alpha=0.7, edgecolor='white'))


    #x = np.linspace(min(a_volume), max(a_volume), 1000)
    coefs=poly.polyfit(volume,a_data.iloc[index], 1)
    ffit = poly.Polynomial(coefs)    # instead of np.poly1d
    axis[0].plot(x, ffit(x), c = "b", linewidth=1)
    #axis.text(0.5,0.8, 'y = ' + '{:.2f}'.format(coefs[0]) + ' + {:.2f}'.format(coefs[1]) + 'x', c = "b", fontsize=15, transform=axis.transAxes)
    corr_matrix = np.corrcoef(volume, a_data.iloc[index])
    corr = corr_matrix[0,1]
    R_sq3 = corr**2
    t=axis[0].text(0.1,0.8, r'$R^2=${:.4f}'.format(R_sq3), c = 'b', fontsize=10, transform=axis[0].transAxes)
    t.set_bbox(dict(facecolor='white', alpha=0.7, edgecolor='white'))


    axis[1].scatter(volume_cc, data.iloc[index], s=2, c='r',label = "ComBat")
    axis[1].scatter(volume_cc, a_data.iloc[index], s=2, c='b', label = "Aorta Combat")
    axis[1].scatter(volume_cc, p_data.iloc[index], s=2, c='grey', label = "Original")

    x = np.linspace(min(volume_cc), max(volume_cc), 1000)
    #find best fit line
    coefs=poly.polyfit(volume_cc,data.iloc[index], 1)
    ffit = poly.Polynomial(coefs)
    axis[1].plot(x, ffit(x), c = "r", linewidth=1)
    #axis.text(0.5,0.9, 'y = ' + '{:.2f}'.format(coefs[0]) + ' + {:.2f}'.format(coefs[1]) + 'x', c = "r", fontsize=15, transform=axis.transAxes)
    corr_matrix = np.corrcoef(volume_cc, data.iloc[index])
    corr = corr_matrix[0,1]
    R_sq1 = corr**2
    t =axis[1].text(0.1,0.9, r'$R^2=${:.4f}'.format(R_sq1), c = "r", fontsize=10, transform=axis[1].transAxes)
    t.set_bbox(dict(facecolor='white', alpha=0.7, edgecolor='white'))


    #x = np.linspace(min(p_volume), max(p_volume), 1000)
    coefs=poly.polyfit(volume_cc,p_data.iloc[index], 1)
    ffit = poly.Polynomial(coefs)    # instead of np.poly1d
    axis[1].plot(x, ffit(x), c = "grey", linewidth=1)
    #axis.text(0.5,0.8, 'y = ' + '{:.2f}'.format(coefs[0]) + ' + {:.2f}'.format(coefs[1]) + 'x', c = "b", fontsize=15, transform=axis.transAxes)
    corr_matrix = np.corrcoef(volume_cc, p_data.iloc[index])
    corr = corr_matrix[0,1]
    R_sq2 = corr**2
    t =axis[1].text(0.1,0.7, r'$R^2=${:.4f}'.format(R_sq2), c = 'grey', fontsize=10, transform=axis[1].transAxes)
    t.set_bbox(dict(facecolor='white', alpha=0.7, edgecolor='white'))


    #x = np.linspace(min(a_volume), max(a_volume), 1000)
    coefs=poly.polyfit(volume_cc,a_data.iloc[index], 1)
    ffit = poly.Polynomial(coefs)    # instead of np.poly1d
    axis[1].plot(x, ffit(x), c = "b", linewidth=1)
    #axis.text(0.5,0.8, 'y = ' + '{:.2f}'.format(coefs[0]) + ' + {:.2f}'.format(coefs[1]) + 'x', c = "b", fontsize=15, transform=axis.transAxes)
    corr_matrix = np.corrcoef(volume_cc, a_data.iloc[index])
    corr = corr_matrix[0,1]
    R_sq3 = corr**2
    t=axis[1].text(0.1,0.8, r'$R^2=${:.4f}'.format(R_sq3), c = 'b', fontsize=10, transform=axis[1].transAxes)
    t.set_bbox(dict(facecolor='white', alpha=0.7, edgecolor='white'))
    #r_value.append((R_sq1,R_sq3,R_sq2))

    axis[0].set_title(feature, fontsize=12)
    axis[0].legend(loc='upper right')
    axis[0].set_xlabel("Pixel Spacing")

    axis[1].set_title(feature, fontsize=12)
    axis[1].legend(loc='upper right')
    axis[1].set_xlabel("Volume(cc)")

    plt.savefig("/media/sf_research/krishni/code/output/20221205pixelspacing/"+str(index)+str(feature)+".png")
    print("graph plotted:",index)

#df = pd.DataFrame(r_value, columns =['Combat',"Aorta_Combat","Original"],index = columns)
#df.to_csv('r_value.csv', index=True, header=True, sep=',')
