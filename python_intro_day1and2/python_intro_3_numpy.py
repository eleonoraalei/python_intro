# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 16:05:40 2017

@author: Federico Biondi
"""

###################################
#
#       NUMPY
#
###################################

# Elementi dello stesso tipo
# Efficiente se di grandi dimensioni (vediamo alla fine un confronto con le liste)

import numpy as np

# Creo array vuoto
v = np.empty(2)
w = np.empty((3,2), dtype=float)
y = np.empty((2,2,2))

# Creo array con dei valori
z = np.array([0,1,2,3,4,5,6,7,8,9])

#Accesso, slicing, modifica
x1 = z[2]
z[0]=-1
x2 = z[2:-4:2]
x3 = z[::-1]
x4 = z[::-3]

mat = np.array([[1,2,3,4,5],[0,0,0,0,0]], float)

# Valori in sequenza
s = np.arange(5,19)
ss = np.linspace(0,99,99)
dim_ss = len(ss)

# Zeri e uni
zeri = np.zeros((5,2))
uni  = np.ones(20)

# Identità
iden1 = np.identity(3)
iden2 = np.eye(5,3,k=1)

# Forma di un array
lunghezza_zeri = len(zeri)
forma_zeri = np.shape(zeri)


# La copia
copia1 = np.array([1,2,3,4,5])
copia2 = copia1
copia3 = np.copy(copia1)
if 1:
    copia1[0]=-1

# Valore in array
bool1 = 1 in zeri

# matrice trasposta
transp1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
transp2 = transp1.transpose()

# flatten
flat = transp1.flatten()

# concatenazione
con1 = np.array([[1, 2], [3, 4]])
con2 = np.array([[5, 6], [7, 8]])
con3 = np.concatenate((con1,con2))
con4 = np.concatenate((con1,con2), axis=1)

# 
cost1 = np.pi
cost2 = np.e
cost3 = np.NaN
cost4 = np.Inf

# arrotondamenti
arr1 = np.array([1.1, 1.5, 1.930999])
arr2 = np.floor(arr1)
arr3 = np.ceil(arr1)
arr4 = np.rint(arr1)
arr5 = np.round(arr1,2)

# funzioni standard
fun1 = np.array([2, 4, 3])
fun2 = fun1.sum()
fun3 = fun1.prod()
fun4 = np.sum(fun1)
fun5 = np.prod(fun1)

stat = np.array([2, 1, 9])
media = stat.mean()
media1 = np.mean(stat)
varia = stat.var()
varia1 = np.var(stat)
sig = stat.std()
sig1 = np.std(stat)

minimo = np.amin(stat)
massimo = np.amax(stat)

ami = stat.argmin()
ama = stat.argmax()

stat2d = np.array([[0, 2], [3, -1], [3, 5]])
media2d = np.mean(stat2d, axis=0)
pippo = np.mean(stat2d, axis=1)

# confronti
conf1 = np.array([1, 3, 0])
conf2 = np.array([0, 3, 2])
conf3 = conf1 > conf2
conf4 = np.any(conf1<2)
conf5 = np.all(conf1<2)

conf6 = np.where(conf1>1, conf1*2, conf2)
conf1111 = np.where(conf1<2)


conf7 = np.logical_and(conf1<2, conf1>0)
conf8 = np.logical_or(conf1<2, conf1>0)

conf9 = np.array([10, np.NaN, np.Inf])
conf10 = np.isnan(conf9)
conf11 = np.isfinite(conf9)

conf12 = len(conf1[conf1<2])
conf13 = [0,0,1]
conf14 = conf1[conf13]

if False:
    # fit polinomiale
    #    
    ascissa       = np.array([-5, -3, 0, 1, 6, 9], float)
    ordinata      = np.array([28., 9., -3., 1., 33., 75.])
    poli_retta    = np.polyfit(ascissa, ordinata, 1)
    poli_parabola = np.polyfit(ascissa, ordinata, 2)
    
    fpoli_retta    = np.poly1d(poli_retta)    
    fpoli_parabola = np.poly1d(poli_parabola)    
    
    xfit          = np.linspace(-10,10,100)    
    yfit_retta    = fpoli_retta(xfit)
    yfit_parabola = fpoli_parabola(xfit)

     
    # plot
    import matplotlib.pyplot as plt
    plt.close()
    plt.figure()
    plt.plot(ascissa, ordinata, 'bo')
    plt.plot(xfit, yfit_retta, 'g:')
    plt.plot(xfit, yfit_parabola, 'r:')
    plt.show(block=False)





if True:
    # list comprehention
    import time
    n = 100   # cambiare n da 4 a 7
    l = range(n)
    ll = np.arange(n)
    print ('')

    t0 = time.time()
    b = [x*1000 for x in l]
    print ('list comprehention:                              ', time.time() - t0)
 
   
    c = []
    t0 = time.time()
    for i in range(n):
        c.append(i*1000)
    print ('ciclo for tradizionale                           ', time.time() - t0)
    
    

    d = []
    t0 = time.time()    
    for i in l:
        d.append(i*1000)     
    print ('ciclo for sugli items                            ', time.time() - t0)





    if 0:
        e = np.array([])
        t0 = time.time()    
        for i in l:
            e = np.append(e, i*1000)     
        print ('append a numpy array vuoto                       ', time.time() - t0)




    
    f = np.empty(n)
    t0 = time.time()    
    for i in l:
        f[i] = i*1000     
    print ('append a numpy array già allocato                ', time.time() - t0)


    if 0:
        t0 = time.time()    
        g = l*1000
        print ('operazione su numpy array partendo da lista      ', time.time() - t0)
    
    t0 = time.time()    
    h = ll*1000
    print ('operazione su numpy array partendo da numpy array', time.time() - t0)
    
