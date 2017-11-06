# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:03:48 2017

@author: Federico Biondi
"""


if 0:
    # lettura file in generale
    if 0:
        f = open('tabella_ascii.txt', 'r')
        lines = f.read()
        f.close()
        print (lines)
        print ('')   


    if 0:
        f = open('tabella_ascii.txt', 'r')
        for line in f:
            print (line, type(line))
        f.close()
        print ('')    



    if 0:
        f = open('tabella_ascii.txt', 'r')
        for line in f:
            riga = line.strip()  # scrosta gli spazi bianchi e o caratteri a piacere all'inizio o alla fine della stringa
            colo = riga.split()  # divide le stringhe separate da spazi bianchi o da un separatore arbitrario
            print (colo[0], colo[1])
        f.close()
        print ('')    

    
    
    if 0:    
        f = open('tabella_ascii.txt', 'r')
        '''
        for i in range(3):
            print f.readline()
        '''
        print ('')
    
        lines = f.readlines()
        f.close()
        print (lines)    

        for line in lines:
            colo = line.strip().split()
            print (colo[0], colo[1])
    
    # Scrittura file in generale
    if 0:
        a = [1,2,3,4,5]
        b = ['a','b','c','d','e']
        file_out = open('out_standard.txt', 'w')
        for x,y in zip(a,b):
            file_out.write(str(x) + '\t' + y + '\n')            
        file_out.close()
        
###############################################################################

if False:
    # asciidata   (https://www.stecf.org/software/PYTHONtools/astroasciidata/)
    # dopo averlo estratto: python setup.py install
    import asciidata
    
    
    # scrivo
    if 0:
        x = [0,1,2,3,4,5,6,7,8,9]
        y = [pippo*2 for pippo in x]
        
        
        tabella = asciidata.create(2,10, null=None, delimiter=None)
        #print tabella
        for i in range(tabella.nrows):
            tabella[0][i] = x[i]
            tabella[1][i] = y[i]
        
        tabella.writeto('tabella_ascii.txt')
    

    # leggo: 
    if 0:   
        tab = asciidata.open('tabella_ascii.txt')
        col1 = tab[0]
        col2 = tab[1]
        
        '''
        col1 = [x_ for x_ in col1]
        col2 = [x_ for x_ in col2]
        '''

###############################################################################

if False:  
    # pickle
    import pickle
    a = {'a':2, 'b':3}
    b = [1,2,3,4,5]
    
    # scrivo
    f_out = open('output.pkl','w')
    pickle.dump(a,f_out)
    pickle.dump(b,f_out)
    f_out.close()
    
    # leggo
    with open('output.pkl') as f_in:
        aa = pickle.load(f_in)
        bb = pickle.load(f_in)
        
###############################################################################

if 0:
    import numpy as np
    # leggo
    d1,d2 = np.loadtxt('tabella_ascii.txt', usecols=(0,1), unpack=True)
    #c1,c2 = np.load('output.pkl')

    # scrivo
    k1 = np.array([1,2,3,4,5])
    k2 = np.array([10,20,30,40,50])
    np.savetxt('out___.dat', np.c_[k1,k2])


if False:
    import pandas as pd
    tabella = pd.read_csv('tabella_ascii.txt')
    tabella.to_csv('ffff.dat', index_label=False, header=False, index=False)
    
###############################################################################

if 0:
    from astropy.io import ascii
    from astropy.table import Table
    
    data = ascii.read('tabella_ascii.txt')  
    print(data)                       

    k1 = np.array([1,2,3,4,5])
    k2 = np.array([10,20,30,40,50])

    data_da_scrivere = Table([k1, k2], names=['k1', 'k2'])
    data_da_scrivere.write('tabella_astropy.dat', format='latex')
    
    