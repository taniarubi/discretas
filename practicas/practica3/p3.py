'''Funciones obligatorias'''
def potencia(x,n):
	if n <= 0:
		return 1

	if n % 2 == 0:
	    pot = potencia(x, n/2)
	    return pot * pot

	else:
	    pot = potencia(x, (n-1)/2)
	    return pot * pot * x    

def concatenaNones(a,b):
    if a > b:
        return ""
    else:
        c = a % 2
        if(c == 0):
            return (concatenaNones(a+1,b))
        else:
            return (str(a))+" " + (concatenaNones(a+2,b))
    
def mayor(n,a,b):
    if a > b:
        return [] 
    else:
        if n >= a or n > b:
            return [] + (mayor(n, a+1, b))
        else:
            return [a] + (mayor(n, a+1, b))

def contiene(l1,l2):
    if l1 == []:
        return True
    if len(l1) > len(l2):
        return False
    if l1[0] == l2[0]:
        return contiene(l1[1:],l2[1:])
    return contiene(l1,l2[1:])

def refleja(l):
    if l==[]:
        return []
    else:
        a = l[0]
        l = l[1:]
        return [a] + refleja(l) + [a]
    
def intercala(l1,l2):
    if l1 == [] and l2 == []:
        return []
    else:
        if l1 == []:
            cabeza2 = l2[0]
            l2 = l2[1:]
            return [cabeza2] + intercala(l1,l2)
        else:
            if l2 == []:
                cabeza1 = l1[0]
                l1 = l1[1:]
                return [cabeza1] + intercala(l1,l2)
            else:
                cabeza1 = l1[0]
                cabeza2 = l2[0]
                l1 = l1[1:]
                l2 = l2[1:]
                return [cabeza1] + [cabeza2] + intercala(l1,l2)    

'''Función para calificación extra'''           
def reversaN(l):
    if l == []:
        return []
    else:
        cola = l.pop()
        return [cola] + reversaN(l)
    