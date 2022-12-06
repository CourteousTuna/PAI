from math import *

def IT(t):
    return t

def Proba_S(t): #proba survie 
    global mort
    return mort[t] #proba à l'instant t 

def prob(age_cont,t ):
    global rachat
    if age_cont>=8:
        print("à finir")
    else :
        print("à finir")        
    
    
def Proba_RS(t): #proba rachat structurel
    age_cont=date(t) #calcul age du compte 
    return prob(age_cont,t) #calcul proba en fonction de l'age du compte 

def deces(t,pm,tmg):
    if tmg==[]:
        p=Proba_S(t) #proba survie
        return pm*(1-p)

def Proba_RC(t): #proba rachat conjonc
    global conj
    if conj==True:
        print("pas de fonction")
    else : #modèle basique 
        return 0
        
        
        
def RT(t,pm,tmg): #Rachat total
    if tmg==[]: 
        d=deces(t,pm,tmg)
        ps=Proba_RS(t)
        pc=Proba_RC(t)
        return min([pm-d,pm*max([0,pc+ps])])

def RP(t):
    global rp
    return t


def PreN(t,pm,tmg): #calcul prestations nettes 
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

def PM(t,k,tmg): #calcul provision mathématique 
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
    conj=False
    rp=False 
    print(PM(10,invest_ini,tmg))
    
    