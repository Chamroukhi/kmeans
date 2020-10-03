import numpy as np
#import matplotlib.pyplot as plt

x=[[12,34,2],[56,78,3],[18,15,32],[19,30,12],[34,54,12],[30,40,9],[26,34,19],[13,8,17],[23,38,49],[32,9,29]]


#Début
 
#============================ initialisation: ============================#

#nombre de classe
nombre_classe=4

#nombre des variables explicatives x1,x2,...,xn
nombre_feature=3

#nombre d'observation (les points)
observation=8

#liste vide 
groupe=[]

#centroide
c=[[12,34,2],[56,78,3],[26,34,19],[19,30,12]]

if (len(c)<nombre_classe):
    print("vérifier les centres de classe")
elif(len(c[0])<nombre_feature):
    print("vérifier le nombre des features représente le point")
else:
#======== creation de groupe (nombre de groupe = nombre de classe) =========#
    for g in range(nombre_classe):
        groupe.append([])

#=========================== distance euclidienne ==========================#
    def distanceE(centre,point):
        """ distance euclidienne """
        s=0
        for i in range(nombre_feature):
            s=s+(pow((point[i]-centre[i]),2))
            d=np.sqrt(s)
            return d
        
#================================ affectation: =============================#

    for i in range(observation):
        distance=[]
        for k in range(nombre_classe):
            d=0
            d=distanceE(c[k], x[i])
            distance.append(d)
        classe=min(distance)   
        for k in range(nombre_classe):
            if classe == distance[k]:
            
                groupe[k].append(x[i])
            
#======================== recalculer les centroide =========================#
                for j in range(nombre_feature):
                    w=0
                    for l in range(len(groupe[k])):
                  
                        w=w+groupe[k][l][j]
                   
                    s=w/len(groupe[k])
                    c[k][j]=s

#=============================== affichage =================================#             
    for g in range(len(groupe)):
        print("groupe[",g,"] :",groupe[g])

    print("centroide",c)     




       
                    
"""
X1=[]
X2=[]
for i in range(observation):
 
  X1.append(x[i][0])

  X2.append(x[i][1])


plt.scatter(X1,X2)

plt.show()
 """                      
      


      
        
