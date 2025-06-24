from initialisation_parametres import *
from P3P_numpy import P3P
from P3P_openCV import *
from test import *

# Generate the camera matrixs
A = camera()
R = rotation_matrix()
T = camera_translation()

# Generate the 3D points 
points3D_4 = pts_3D_4pts()
points3D = pts_3D_3pts(points3D_4)

# Generate the 2D points
points2D_4 = pts_2D_4pts(points3D_4,T,R,A)
points2D = pts_2D_3pts(points2D_4)

# Generate the features vectors : fi = TPi / ||TPi||
features_vectors = features_vectors(points3D,T)

# Recover the P3P solutions 
solution_openCV = recup_solutions_openCV(points2D_4,points3D_4,A)
solution_numpy = P3P(points3D,features_vectors)

comparaison_numpy_openCV(solution_openCV,solution_numpy)
