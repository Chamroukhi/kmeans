# kmeans

principe de kmeans :

Début:
 
1) initialisation de nombre de classe(K) et les centres de groupe.

2)  pour chaque points(Xi) dans la base d'apprentissage et:
   | 
   |   pour tous les classe(K) faire:
   |  |
   |  |   -calculer la distance euclidienne D(c,x) entre le point(x) et la classe(c).
   |  | 
   |  |   -attribuer à x la classe qui minimise la distance  D(c,x).
   |  |
   |   fin pour
   |
   |   reclaculer les centres des groupes.
   |
    fin pour

Fin
