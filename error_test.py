# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 12:24:24 2019

@author: gela
"""
import pandas 
import numpy as np

def addtoexcel(X, Y, delta_X, delta_Y, deltau, sheetname = 'Error of Single Hyperbola'):
       
        
    delta_tau = [deltau]*len(X)
    dataframe = pandas.DataFrame({'X ': X,
                                  'Y ': Y,
                                  'Delta Tau': delta_tau,
                                  'Delta X': delta_X,
                                  'Delta Y': delta_Y
                                  })
    
    
    writer_obj = pandas.ExcelWriter(sheetname+'.xlsx', engine='xlsxwriter')
    
    dataframe.to_excel(writer_obj, sheet_name = sheetname)
    writer_obj.save()
    writer_obj.close()






def delta_x(x,y,delta_tau, f = 1):
    mic1 = -1
    mic2 = 1
    f = 1
    d1 = np.sqrt((x-mic1)**2 + y**2)
    d2 = np.sqrt((x-mic2)**2 + y**2)
    tau = np.abs(d1- d2)/2
    
    nomish = 2*tau*(y)**2/(f**2 - tau**2)
    demoninator = 2*np.sqrt((tau**2/(f**2 - tau**2))*(y**2)+2*tau**3)
    del_x = (nomish + nomish*tau**2 +6*tau)/demoninator
    del_x = del_x*delta_tau
    delta_y = (f**2 - tau**2)*x/(tau**2)
    delta_y = delta_y/np.sqrt((f**2 - tau**2)*(x**2)/tau**2 - 2*(tau**5)*(f**2 - tau**2))
    delta_y = delta_y*del_x
    return del_x, delta_y

def element_wise(array_of_coords, delta_tau):
    delta_xs = []
    delta_ys = []
    for term in array_of_coords:
        x, y = term
        del_x, delta_y = delta_x(x,y,delta_tau)
        delta_xs.append(del_x)
        delta_ys.append(delta_y)
        
    return delta_xs, delta_ys


X_and_Y = np.abs(10*np.random.normal(5.0, 5, size =(5,2)))
X_and_Y = np.vstack((X_and_Y, 20*np.abs(np.random.normal(5.0, 5, size =(5,2)))))
X_and_Y = np.vstack((X_and_Y, 50*np.abs(np.random.normal(5.0, 5, size =(5,2)))))

X = X_and_Y[:,0]
Y = X_and_Y[:,1]
delta_xs, delta_y = element_wise(X_and_Y, 0.001)
addtoexcel(X,Y,delta_xs, delta_y, 0.001)
print('done')