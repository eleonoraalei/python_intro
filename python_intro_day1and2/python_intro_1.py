# -*- coding: utf-8 -*-
"""
Created on Fri Feb 03 18:31:28 2017

@author: Blond
"""

###############################
#
#
#     MINI CORSO PYTHON
#
#
###############################

# Notazione utilizzata
'''Ho voluto scrivere un unico documento (questo) i cui vari "pezzi" vengono
attivati da "blocchi if". Se l' if è seguito da un boolean = True allora vengono
eseguite le istruzioni all'interno del blocco, altrimenti il blocco viene ignorato.'''


a = 1
b = 1
if a == b:
    print
    print ('Ok')
    print

if False:
    print ('Ok')

###############################################################################

if 0:
    
    # Sintassi / Tipi / Generalità
    
    print (type('pausa caffe'))
    print (type(2147483647))
    print (type(4.5))
    print (type(2147483648))
    print (type(4j))
    
    print 
    
    print
    print ('____________________')
    print
    
    a = 'pausa caffe'
    b = 45
    c = 4.5
    
    ta = type(a)
    tb = type(b) 
    tc = type(c) 
    
    # il tipo di una variabile è il tipo del valore a cui essa si riferisce
    
    
    # print variable printa il contenuto della variabile, 
    #evaluate (<-- non è un comando) variable usa lo stesso formato che si utilizza per scriverla

    # case sensitive
    d = 5
    #print D
    
    # parole riservate  
    #mostrarla
    '''
    and       del       for       is        raise    
    assert    elif      from      lambda    return   
    break     else      global    not       try      
    class     except    if        or        while    
    continue  exec      import    pass      yield    
    def       finally   in        print
    '''
    
    # ordine di precedenza operatori
    # ()
    # **
    # * /
    # + -
    # da sx a dx    
    
    # vedere la precedenza degli operatori logici

###############################################################################

if 1:
    # operazioni sulle stringhe
    a = 'py'
    b = 'corso di ' + a + 'thon' + ' oggi ----- '
    b = b * 10
    print ('Ecco cosa esce: ',b)
    
    print ('')
    print ('------------')
    print ('')
    print("si puo' evitare di andare a capo",end="") # non mette 'newline' alla fine
    print("... sono sulla stessa riga")
    
    # altre operazioni (split ecc)

###############################################################################

if 0: 
    num = 100
    den = 3
    frazio = num / den
    print (frazio)
    # questo non funziona in py2.7 attenzione ai passaggi python3 --> 2
    
    num = 100
    den = 3
    frazio = 100 / 3. # forzatura di tipo
    print (frazio)
    
    
    num = 100
    den = 3
    frazio = float(num) / den # conversione di tipo
    print (frazio)
    
    num = 100.
    den = 3
    frazio = int(num) / den
    print (frazio)
    
    num = str(num)
    print (num*3)

if False:
    print (10. // 3)
    print (10. % 3)
    

if 0:
    import math as mt
    a = mt.log10(4)

# exp sin cos tan asin acos atan pi e 
# altre operazioni abs % // incrementi(i += 1)

###############################################################################

if 0:
    # booleane:
    r = 2 == 2
    print (r)
    
    r = 2 != 2
    print (r)
    
    r = 2 != 3
    print (r)
    
    r = 2 > 2
    print (r)
    
    r = 2 >= 2
    print (r)
    
    r = 2 < 2
    print (r)
    
    r = 2 <= 2
    print (r)
  
###############################################################################

if False:
#esecuzione condizionale
    a = 3
    b = 4
    if a < 9:
        print ('')
        print ('20Feb')
    elif a > 10 and a < 30:
        if b == 4 or b == 6:
            print ('sssss')
        else:
            print ('ttttt')
    else:
        print ('bbbbb')
    
    
    
    
    if 0:
        print ('corso base')
    if 1:
        print ('corso avanzato')    
    
    if False:
        print ('corso base')
    if True:
        print ('corso avanzato')    

###############################################################################

if 0:
    # funzioni
    
    def Funzione1():
        # non fa nulla
        pass
    
    def Funzione2():
        # prina una riga
        print ('scrivo')
    
    def Funzione3(x,y=-5,z=-4):
        import math
        # return e input parametro
        if x+y <=0:
            return
        else:
            try:
                print (math.log10(z))        
            except:
                print ('no log for your number')
    
    def Funzione4(a,b):
        # parametri input e output
        return a+b, a-b
    
    def Funzione5(n):
        #
        if not type(n) is int:                   # alternativa if type(n) != type(1)
            print ('Voglio un intero positivo!')
            return
        else:
            if n == 0 or n == 1:
                return 1
            else:
                return Funzione5(n-1) + Funzione5(n-2)
        
if 1:
    if 0:
        # liste (serie ordinata di valori)
        lista1 = [1, 5, 5, 10]
        lista2 = [1, 5., 5, 10]
        lista3 = [9, 'parola', ['wow', 5]]
        
        print (lista1[0])
        lista1[1] = -999
        print (lista1) 
        
        lista111 = lista1 * 3
        print (lista111)
        
        print (lista2[:])
        print (lista2[:3])
        print (lista1[-1])
        
        del lista1[-1]
        print (lista1)
        
        #interessante #1
        appartiene = 1 in lista1
        print (appartiene)
    
    if 0:    
        # ATTENZIONE
        lista10 = [1,2,3,4,5]
        lista20 = lista10
        print (lista10)
        print (lista20)
        del lista10[0]
        print ('dopo aver cancellato il primo elemento')
        print (lista10)
        print (lista20)   # b è un alias di a e punta allo stesso valore  # la stringa non ha questo problema
        
        # per clonare
        lista30 = lista10[:]
        # oppure
        import copy
        lista40 = copy.copy(lista10)


if 0:
    # for
    # ciclo "tradizionale"
    if 0:
        for i in range(4,10):
            print (i)
        print ('')    
        for i in range(10):
            print (i)
        
    if 0:
        # ciclo sugli items:
        settimana = ['lune', 'marte', 'mercole', 'giove',
                     'venere', 'sabato', 'domenica']
        for giorno in settimana:
            print (giorno)
        
        print ('')
        for i in range(len(settimana)):
            print (settimana[i])
        
    if 0:    
        # interessante  #1
        a = [1, 2, 3]
        b = ['a', 'b', 'c']
        for x,y in zip(a,b):
            print (y + str(x))
         
        print ('') 
        # interessante #2
        a = [1, 2, 3]
        b = ['a', 'b', 'c']
        import itertools
        for x in itertools.product(b,a):
            print (x)
            
    if 0:        
        # interessante #3
        a = [1, 2, 3]
        b = ['a', 'b', 'c']
        for i, x in enumerate(b):
            print (x + str(a[i]))
    

    if 0:    
        # alterazioni ciclo
        if 0:
            # break (esce dal ciclo)
            for i in range(100):
                if i>13:
                    break
                print (i)
             
            print ('')
            print ('------------------------') 
            print ('')
        
        if 0:
            # continue (cicla all'indice successivo ignorando il resto del contenuto)  
            for i in range(100):
                if i != 10 and i != 20:
                    continue
                    print ('Questo non lo scrivo')
                print (i)
            print ('-----------')

        if 0:
        # pass (non fa nulla) 
            for i in range(100):
                if i != 10 and i != 20:
                    pass                         
                    print ('Questo lo scrivo')
                print (i)
            

if 0:
    # list comprehention
    import time
    n = 1000  # cambiare n
    l = range(n)
    
    t0 = time.time()
    b = [x*1000 for x in l]
    print (time.time() - t0)
    
    c = []
    t0 = time.time()
    for i in range(n):
        c.append(i*1000)
    print (time.time() - t0)
    
    d = []
    t0 = time.time()    
    for i in l:
        d.append(i*1000)     
    print (time.time() - t0)


if False:
    # while
    i = 0
    while True:
        i += 1
        print (i)
        if i >20:
            break
    
    while 0:
        print ('@@@@@@@')


if False:
    # tupla
    a = (1,)
    b = (8, 9, 10)
    c = ('a', 'b', 'c')
    d = ('a', 'b', 4.0)
    
    try:
        d[0] = 0
    except:
        print ('non posso cambiare gli elementi di una tupla')
    
    e = list(d)
    
    # figata con la tupla
    tx = 10
    ty = 20
    tx, ty = ty, tx


if False:
    # dizionari
    dizio1 = {}
    dizio2 = {'chiave1':'a', 'chiave2':1, 'chiave3':[1,2,3,4], 10:(5,6,7)}

    chiavi = dizio2.keys()
    print (chiavi)
    print ()
    valori = dizio2.values()
    print (valori)
    print ()
    elementi = dizio2.items()
    print (10 in dizio2)
    print ()
    print('---------------')
    
    dizio2['nuova_chiave'] = 1000
    
    print (dizio2.pop('chiave1'))   # restituisce il valore e poi cancella
    dizio2.pop('chiave1', None)     # il valore non esiste piu, quindi restituisce none
    del dizio2['chiave2']           # cancella senza restituire nulla
    
    # come per le liste (fare delle prove)
    dizio3 = {'a':1, 'b':2}
    dizio4 = dizio3.copy()
    dizio5 = dizio4
    
    # Fibonacci
    precedenti = {0:1, 1:1}
    def fibo(n):
        if precedenti.has_key(n):
            return(precedenti[n])
        else:
            nuovo = fibo(n-1) + fibo(n-2)
            precedenti[n] = nuovo
            return nuovo

    # Altri esempi: salvare dati con commento / esempio del monitoraggio di una cartella
    
############################################### no    
if False:
    # lambda: funzioni anonime a runtime
    funz1 = lambda x: x*x
    print (funz1(10))
    
    l1 = [1,2,3,4]
    out1 = map(funz1,l1)
    print (list(out1))
    
    
    funz2 = lambda x: x < 0
    l2 = [-2, -1, 0, 1, 2]
    out2 = filter(funz2, l2)
################################################

if 0:
    # sortare liste
    ordinare = [5,4,6,7,-1]
    
    out_ordinato1 = sorted(ordinare)
    
    o1 = ['b', 'a', 'd', 'c']
    o2 = [1,2,3,4]
    o3 = [1,2,1,2]
    
    oo1, oo2, oo3 = zip(*sorted(zip(o1, o2, o3))) # *lista spacchetta la lista ** spacchetta i dizionari
    
    
    
    def somma(a,b):
        print (a+b)
    
    somma(3,4)    
    a = [3,4]
    somma(*a)


if 0:
    import time
    # formattazione
    a = -3.44445
    b = 'qwerty'
    c = 400

    print ('a', '\t', 'b')
    print ('c', '\n') 
    print ('c')

    print ('primo numero: {0:14.2F} secondo numero {0:.2e} password {1:20s}'.format(a,b))


    def beep():
        print ("\a")
    for i in range (0,3):	
        time.sleep(4)
        beep()



