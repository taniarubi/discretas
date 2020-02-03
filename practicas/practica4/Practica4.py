'''Ejercicios'''   
def nHojas(tree):
    if (tree is None):
        return 0
    if (tree[0] is None and tree[2] is None):
        return 1
    else:
         return nHojas (tree[0]) + nHojas(tree[2]) 
        
def suma(tree):
    if (tree is None):
        return 0
    else:
        return tree[1] + suma (tree[0]) + suma (tree[2])

def poda(tree):
    if (tree is None):
        return None
    if (tree[0] is None and tree[2] is None):
        return None
    else:
        return poda (tree[0]), tree[1], poda (tree[2])

def esMinHeap(tree):
    if (tree is None):
        return True
    if (not (tree[0] is None)):
        if (tree[1] > tree[0][1]):
            return False
    if (not (tree[2] is None)):
        if (tree[1] > tree[2][1]):
            return False
    return esMinHeap (tree[0]) and esMinHeap (tree[2])        

def nodosInternos(tree):
    if (tree is None):
        return []
    if (tree[0] is None and tree[2] is None):
        return []
    else:
        return nodosInternos [tree[0]] + [tree[1]] + nodosInternos[tree[2]]
       
def toSubMinHeap(tree):
    if (tree is None):
        return None
    if (not(tree[0] is None)):
        x = toSubMinHeap (tree[0])
        if (tree[1] > x[1]):
            return toSubMinHeap (((tree[0][0],tree[1],tree[0][2]),tree[0][1],tree[2]))
    if (not (tree[2] is None)):
        z = toSubMinHeap (tree[2])
        if(tree[1] > z[1]):
             return toSubMinHeap ((tree[0],tree[2][1],(tree[2][0],tree[1],tree[2][2])))
    return tree

'''Ejemplos'''

def nNodos(tree):
    tree = (None, 3,((None, 1, None), 5, None))
    if(tree is None):
        return 0
    else:
        return 1 + nNodos(tree[0]) + nNodos(tree[2])

def altura(tree):
    if(tree is None):
        return 0
    else:
        return 1 + max(altura(tree[0]),altura(tree[2]))

def maxT(tree):
    if(tree is None):
        return 0
    else:
        return max(maxT(tree[0]),tree[1],maxT(tree[2]))       

def preorden(tree):
    if(tree is None):
        return []
    else:
        return [tree[1]] + preorden(tree[0]) +  preorden(tree[2])

def inorden(tree):
    if(tree is None):
        return []
    else:
        return [tree[0] + inorden(tree[1]) + inorden(tree[2])]    

def postorden(tree):
    if(tree is None):
        return []
    else:
        return [tree[0] + postorden(tree[2]) + postorden(tree[1])]

def zigzaguear(tree):
    if(tree is None):
        return []
    if(tree[0] is None):
        return tree[1]
    if(tree[0][2] is None):
        return tree[0][1]
    else:
        return zigzaguear(tree[0][2])         