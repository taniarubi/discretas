def propOr(p, q, r):
    return p or q

def propAnd(p, q, r):
    return p and q

def propNot(p, q, r):
    return not p

def propImplies(p, q, r):
    return propOr(propNot(p, q, r),q, r)

def propIfAndOnlyIf(p, q, r):
    pImplicaQ = propImplies(p, q, r)
    qImplicaP = propImplies(q, p, r)
    return propAnd(pImplicaQ,qImplicaP, r)  

def opImplies1(p, q):
    return not p or q    

def propNot2(p, q):
    return not p

def op1(p, q):
    return not ((opImplies1(p,q)) and (opImplies1(not p,q))) or q    

def op2(p, q):
    return opImplies1((opImplies1(p,propNot2(p,q)) and q),propNot2(p,q))   

def op3(p, q, r):
    return not((opImplies1(p,q) and opImplies1(q,r)) and (not r)) or (not p)

def op4(p, q):
    return opImplies1 (not p, q)     

def op6(p, q, r):
    return not(p or q) or (r and p)    

def op7(p, q, r):
    return (not(not p or not q) or r) and (not r or (not p or not q))

def op8(p, q, r):
    return not((not p or q) and (not q or p)) or r

def op9(p, q, r):
    return ((p and q) or ((not q) and r)) 

def op10(p, q, r):
    return (((not p) or (q and r)) and ((not(q and r)) or p)) or ((not r) or ((not p) and q))

def tablaDeVerdad1(proposicion, cadena):
    print ("_____________")
    print (' p      ' + cadena)
    print ('True    ' + str(proposicion(True,True,True)))
    print ('False   ' + str(proposicion(False,True,True)))

def tablaDeVerdad2(proposicion, cadena):
    print ("________________________")
    print (' p        q      ' + cadena)
    print ('True    True     ' + str(proposicion(True,True,True)))
    print ('True    False    ' + str(proposicion(True,False,True)))
    print ('False   True     ' + str(proposicion(False,True,True)))
    print ('False   False    ' + str(proposicion(False,False,True)))

def tablaDeVerdad3(proposicion, cadena):
    print ("__________________________________")
    print (' p        q        r     ' + cadena)
    print ('True    True     True              ' + str(proposicion(True,True,True)))
    print ('True    True     False             ' + str(proposicion(True,True,False)))
    print ('True    False    True              ' + str(proposicion(True,False,True)))
    print ('True    False    False             ' + str(proposicion(True,False,False)))
    print ('False   True     True              ' + str(proposicion(False,True,True)))
    print ('False   True     False             ' + str(proposicion(False,True,False)))
    print ('False   False    True              ' + str(proposicion(False,False,True)))
    print ('False   False    False             ' + str(proposicion(False,False,False)))

def tablaDeVerdad4(proposicion, cadena): 
    print ("___________________________________")
    print ('p          q     ' + cadena)
    print ('True     True       ' + str(proposicion(True, True)))
    print ('True     False      ' + str(proposicion(True, False)))
    print ('False    True       ' + str(proposicion(False, True)))
    print ('False    False      ' + str(proposicion(False, False)))

tablaDeVerdad1(propNot, 'not p')
tablaDeVerdad2(propOr, 'p or q')
tablaDeVerdad2(propAnd, 'p and q')
tablaDeVerdad2(propImplies, 'p => q')
tablaDeVerdad2(propIfAndOnlyIf, 'p <=> q')

# Ejercicio 1.
tablaDeVerdad4(op1, '((p => q) ^ (¬p => q)) => q')
tablaDeVerdad4(op2, '((p => ¬q) ^ q) => ¬p')
tablaDeVerdad3(op3, '((p => q) ^(q => r) ^ ¬r) => ¬p')
tablaDeVerdad4(op4, '(¬p => q)')
tablaDeVerdad2(propImplies, 'p => q')

# Ejercicio 2.
tablaDeVerdad3(op6, '(p V s) => (r ^p)')
tablaDeVerdad3(op7, '(p => ¬q) <=> r')
tablaDeVerdad3(op8, '(p <=> q) => r')
tablaDeVerdad3(op9, '(p ^ q) V (¬q ^ r)') 
tablaDeVerdad3(op10, '(p <=> q ^ r) V (r => ¬p ^ q)')