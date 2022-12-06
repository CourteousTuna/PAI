import xlrd

#document = xlrd.open_workbook("Hypotheses.xlsx")
#feuille_rachat = document.sheet_by_name('Rachat')
#feuille_assure = document.sheet_by_name('Assuré')
#feuille_actif = document.sheet_by_name('Actifs')
#feuille_courbe_taux = document.sheet_by_name('Courbe_taux')


courbe_taux = []

VM0= 10255014 
N=10000000
tx_coupon=0.06
T=10
freq=1


with open('courbe taux spot.csv') as f:
    data = f.read().splitlines()

for i in range(2,len(data)):
    donnee = data[i].split(';')
    courbe_taux.append(float(donnee[1].replace(',','.')[:-1])/100)


def fonction(tx_coupon,N,T,proba_defaut):
    global courbe_taux
    s=0
    for k in range(1,T+1):
        s+=tx_coupon*N*(1-proba_defaut)**k/(1+courbe_taux[k-1])**k
    s+=N*(1-proba_defaut)**T/(1+courbe_taux[T-1])**T
    return s

def calcul_proba_defaut(VM0,tx_coupon,N,T):
    a=0
    b=1
    c=fonction(tx_coupon,N,T,(a+b)/2)
    
    while abs(VM0-c) > 1:
        if VM0-c <= 0:
            a = (a+b)/2
        else:
            b = (a+b)/2
            
        c = fonction(tx_coupon,N,T,(a+b)/2)
    return (a+b)/2

proba_defaut=calcul_proba_defaut(VM0,tx_coupon,N,T)
print(f'Probabilité de défaut: {str(proba_defaut*100)[:4]} %')

def valeur_marche_avant_transaction(t):
    global tx_coupon
    global N
    global freq
    global proba_defaut
    global T
    s=0
    for i in range(t,T):
        s+=tx_coupon*(1-proba_defaut)**i/freq/(1+courbe_taux[T-t])**i
        
    s=N*(s+(1-proba_defaut)**T/(1+courbe_taux[T-t])**T)
    return s

VM_0=valeur_marche_avant_transaction(0)
VM_1=valeur_marche_avant_transaction(1)
VM_2=valeur_marche_avant_transaction(2)
VM_10=valeur_marche_avant_transaction(10)

print(f'Valeur de marché avant transaction à t=0 : {VM_0}')
print(f'Valeur de marché avant transaction à t=1 : {VM_1}')
print(f'Valeur de marché avant transaction à t=2 : {VM_2}')
print(f'Valeur de marché avant transaction à t=T : {VM_10}')
