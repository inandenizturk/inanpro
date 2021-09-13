#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 08:04:29 2021

@author: inandenizturk
"""

import numpy as np
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib as plt



data =np.array([[56,45,68,77]]).T

x = data[:,0]
data1 = pd.DataFrame({'i':np.arange(1,5), 'inanverilenveriler':[56,45,68,77]})
data1.set_index('i',inplace = True )
data1
#y = data[:,1]
print(data1)
data1.mean

filtre1 =  (data1.iloc[:,0] >= 67)
filtre2 = (data1.iloc[:,0]< 67)
filtre2
filtre1,filtre2


filtre1 =  (data1.iloc[:,0] >= 67)
verilerdesecilimbuyuk = data1[filtre1]
verilerdesecilimbuyuk
filtre2 = (data1.iloc[:,0]< 67)
verilerdesecilimkucuk = data1[filtre2]
verilerdesecilimkucuk,verilerdesecilimbuyuk

x =verilerdesecilimkucuk.iloc[:,0]
y =verilerdesecilimbuyuk.iloc[:,0]

z = y*y
z

yz = np.array(z[0:,])
total = np.sum(yz)
mutlak = np.sqrt(total)
mutlak,yz,total
print("mutlak: {:7.4f}\ntotal: {:7d}\n".format(mutlak,total,z))
print("mutlak approximately: {:6.2f}\ntotal: {:7d}\n".format(mutlak,total,z))
print("67 den büyük:  ", yz)

xz = np.array(x[0:,])
eksiltme = 67 -xz
eksiltme 
eksiltme_toplam_67 =np.sum(eksiltme)
print("eksiltme_toplam_67:      {:3.0f}\n".format(eksiltme_toplam_67))
print( "67 den çıkarma :  ",  eksiltme   )
print( "67 den küçük :  "  ,   xz)
