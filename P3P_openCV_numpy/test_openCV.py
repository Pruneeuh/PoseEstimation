from initialisation_parametres import *
from P3P_openCV import *
from test import *


A = camera()
R = rotation_matrix()
T = camera_translation()

points3D_4 = pts_3D_4pts()
points3D = pts_3D_3pts(points3D_4)
points2D_4 = pts_2D_4pts(points3D_4,T,R,A)
points2D = pts_2D_3pts(points2D_4)

solution_openCV = recup_solutions_openCV(points2D_4,points3D_4,A)

affichage_erreur(solution_openCV,points2D_4,points3D_4,A)
