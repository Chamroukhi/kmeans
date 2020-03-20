# kmeans

principe de kmeans :

Début:
 
1. Initialisation de nombre de classe(K) et les centres de groupe.

2. Pour chaque points(Xi) dans la base d'apprentissage et:

    
      Pour tous les classe(K) faire:
    
         -calculer la distance euclidienne D(c,x) entre le point(x) et la classe(c).
       
         -attribuer à x la classe qui minimise la distance  D(c,x).

      fin pour

2. Pour chaque points(X) dans la base d'apprentissage et:

    
      . Pour tous les classe(K) faire:
    
           -calculer la distance euclidienne D(c,x) entre le point(x) et la classe(c).
       
           -attribuer à x la classe qui minimise la distance  D(c,x).

      . fin pour


      reclaculer les centres des groupes.
   
    fin pour


3. Fin
