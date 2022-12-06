from math import *

def IT(t):
    return t

def Proba_S(t):
    global mort
    return mort[t] #proba à l'instant t 

def prob(age_cont,t ):
    
    
    
    
def Proba_RS(t):
    age_cont=date(t) #calcul age du compte 
    return prob(age_cont,t) #calcul proba en fonction de l'age du compte 

def deces(t,pm,tmg):
    if tmg==[]:
        p=Proba_S(t) #proba survie
        return pm*(1-p)

def Proba_RC(t):
    global conj
    if conj==True:
        print("pas de fonction")
    else :
        return 0
        
        
        
def RT(t,pm,tmg):
    if tmg==[]: 
        d=deces(t,pm,tmg)
        ps=Proba_RS(t)
        pc=Proba_RC(t)

def RP(t):
    return t


def PreN(t,pm,tmg):
    d=deces(t,pm,tmg)
    rt=RT(t,pm) #rachat total
    rp=RP(t) #rachat partiel
    return d+rp+rt

def PriN(t):
    return t

def Arb(t):
    return t

def PMartR(t):
    return t

def PM(t,k,tmg):
    if t==0:
        return k
    else :
        ant=PM(t-1,k)        #provision mathématique (ie: valeur de l'assurance)
        sec=IT(t)            #??
        pre=PreN(t,ant,tmg)
        pri=PriN(t)          #prime d'assuré (ie:  ce que verse l'assuré)
        pb=PB(t)             #produit financier que l'assureur doit verser à l'assurer (ex: si l'assurance investit sur des obli à 10% d'interet elle reverse 85% de ces 10% à l'assuré)
        arb=Arb(t) 
        pmatr=PMatR(t)
        return ant+sec-pre+pri+arb+pb-pmatr
    
    
    
if __name__=="__main__":
    date_ini=2009
    invest_ini=108305261.24
    tmg=[]
    mort=[]
    rachat=[]
    print(PM(10,invest_ini,tmg))
    
print('hello')
print('kari')