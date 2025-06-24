from initialisation_parametres import *
from algop3p_numpy import P3P
from test import *




A = camera()
R = rotation_matrix()
T = camera_translation()

points3D_4 = pts_3D_4pts()
points3D = pts_3D_3pts(points3D_4)
points2D_4 = pts_2D_4pts(points3D_4,T,R,A)

features_vectors = features_vectors(points3D,T)

solution_numpy = P3P(points3D,features_vectors)

affichage_erreur(solution_numpy,points2D_4,points3D_4,A)
