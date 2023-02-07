 # entrées : 
 # # - produits financiers nets de frais de placements de l'année pf
# - taux de distribution usuel td
# intérêts techniques IT = min garanti aux assurés
# fonction des taux spots
#dotation des PPE liste de 8 valeurs des 8 années précédentes (N-8,N-7...)

#on en déduit l'assiette disponible à reverser aux contrats :

def assiette_disponible(pf,td):
    return pf*td

# taux cible = taux spot 10 ans 


        #1€ placé aujd va rapporter le taux spot pdt 10ans 

def répartition_benefices(pf,td,IT,PPE,taux_cible,montant_contrat,hausse_max_marge_fi):
    ad = assiette_disponible(pf,td)
    benef_fi = 0
    #si l'assiette dispo couvre les IT
    if ad>IT:
        #si l'assiette + le PPE d'il y a 8 ans couvrent le taux cible*montant des contrats
        if ad+PPE[0]>taux_cible*montant_contrat:
            #si on peut en plus dégager le benef financier max réglementaire
            if ad+PPE[0]-hausse_max_marge_fi*ad > taux_cible*montant_contrat:
                #on sert le taux cible*le montant des contrats
                taux_servi = PPE[0] + taux_cible*montant_contrat
                #on conserve le benef financier max
                benef_fi += hausse_max_marge_fi*ad
                #et on dote la PPE du reste
                PPE = PPE.pop(0) 
                PPE.append(ad-taux_cible*montant_contrat-hausse_max_marge_fi*ad)
            #si on ne peut pas dégager le benef financier max
            else:
                #on sert le taux cible*le montant des contrats
                taux_servi = PPE[0] + taux_cible*montant_contrat
                #on garde le reste en benef financier (<benef financier max)
                benef_fi += ad-taux_servi
        #si l'assiette + le PPE d'il y a 8 ans ne couvrent pas le taux cible*montant des contrats
        else :
            #si l'assiette + toute la PPE couvrent le taux cible*le montant des contrats
            if ad + sum(PPE) > taux_cible*montant_contrat:
                taux_servi=ad+PPE[0]
                i=0
                #la PPE est diminuée (on considère qu'on la vide en partant des plus anciennes dotations)
                while taux_servi<taux_cible*montant_contrat:
                    if PPE[i+1]<taux_servi-taux_cible*montant_contrat:
                        taux_servi += PPE[i+1]
                        PPE[i+1] = 0
                        i += 1
                    else :
                        PPE[i+1] = taux_servi-taux_cible*montant_contrat
                        taux_servi = taux_cible*montant_contrat        
                #on sert le taux cible
                #la marge financière est inchangée
            #si l'assiette + toute la PPE ne couvrent pas le taux cible*le montant des contrats     
            else:
                #si la réduction de la marge financière permet d'atteindre le taux cible
                taux_servi = taux_cible*montant_contrat
                #la PPE de l'année n'est pas approvisionnée
                PPE.pop(0)
                PPE.append(0)
                #la marge fin est réduite
                
    #si l'assiette ne couvre pas les IT            
    else:
        taux_servi = IT + PPE[0]
        #la PPE de l'année n'est pas approvisionnée
        PPE.pop(0)
        PPE.append(0)

return taux_servi, PPE, benef_fi
