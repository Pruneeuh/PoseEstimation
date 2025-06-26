import numpy as np 

# This script defines the camera parameters, rotation matrix, and translation matrix.
def camera() : 
  # Definition of the camera parameters
  # focal length
  fx = 60
  fy = 40
  # center
  cx = 0
  cy = 0

  A = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]]) # intraseca matrix of the camera (3*3)
  print("A = \n", A)
  return A

A = camera() 

def rotation_matrix() : 
  # Definition of the rotation matrix of the camera 
  R = np.array([[1, 0, 0],[0, -1, 0], [0, 0, -1]])
  print("R = \n",R)
  return R


def camera_position() : 
  # Definition of the translation matrix of the camera (the position)
  C = np.array([[0,0,6]])    # T = [tx,ty,tz]  (1*3)
  #C = C.reshape((3,1))                       # (3*1)
  print("C = \n",C)
  return C

# Definition of 3D points in the world coordinate system
def point3Daleatoire(x) :
  # Generation of one random points in 3D space 
  return np.array([[np.random.uniform(-x,x),np.random.uniform(-x,x),np.random.uniform(-x,x)]])

def pts_3D_4pts():
  # Generate randomly 4 3D points
  # Output : array which concatenate the 4 points = [ P1, P2, P3, P4 ] 

  P1 = point3Daleatoire(2)     # (1*3) -> pour P3P
  P2 = point3Daleatoire(2)
  P3 = point3Daleatoire(2)
  P4 = point3Daleatoire(2)
  
  points3D = np.concatenate((P1,P2,P3,P4),axis=0);     # (LIGNES 4* COLONNES 3) - xyz
  print("points3D = \n", points3D)
  return points3D

def projection3D2D(point3D,C,R,A) :
  # 3D point = [ Xw, Yw, Zw ]'   (1*3)
  # C : camera position matrix : (3*1)
  # R : camera rotation matrix : (3*3)
  # A : intraseca matrix of the camera : (3*3)
  # Output : return the coordonates of the point in 2D 

  PI = np.concatenate((np.eye(3),np.zeros((3,1))),axis=1)  # (3*4)
  print("C:",C,np.shape(C),type(C))
  print("R:",R,np.shape(R),type(R))

  Rt = np.concatenate((R,C),axis=1)               # (3*4)
  Rt = np.concatenate((Rt,np.array([[0,0,0,1]])),axis=0)   # (4*4)

  point3D_bis = np.concatenate((np.reshape(point3D,(3,1)),np.array([[1]])),axis=0)   #(4*1)
 
  point2D = A @ PI @ Rt @ point3D_bis   # 2D point = [u, v, w] (3*1)
  point2D = point2D / point2D[2]        # 2D point = [u, v, 1] (3*1)
  return point2D[:2]

def pts_2D_4pts(points3D,C,R,A): 
  # Gerenrate the 2D points from 3D points and camera's parameters
  # points3D : array with the 4 3D points = [ P1, P2, P3, P4 ] 
  # C : camera position matrix : (3*1)
  # R : camera rotation matrix : (3*3)
  # A : intraseca matrix of the camera : (3*3)

  # Recovery of each 3D point 
  P1 = np.array(points3D[0])
  P2 = np.array(points3D[1])
  P3 = np.array(points3D[2])
  P4 = np.array(points3D[3])
  
  
  # Projection from 3D to 2D of each point
  p1 = projection3D2D(P1,C,R,A)
  print("p1 = ", p1)
  p2 = projection3D2D(P2,C,R,A)
  print("p2 = ", p2)
  p3 = projection3D2D(P2,C,R,A)
  print("p3 = ", p3)
  p4 = projection3D2D(P4,C,R,A)
  print("p4 = ", p4)

  return [p1,p2,p3,p4]


def features_vectors(points3D,C) :
    '''
    This function computes the features vectors for P3P algorithm.
    args:
    points3D : array with the 4 3D points = [ P1, P2, P3, P4 ] (4*3) 
    but we only use the first three points for P3P
    C: camera position matrix : (1*3)
    returns:
    featuresVect : array with the features vectors (3*3)
    '''
    P1 = points3D[0]
    P2 = points3D[1]
    P3 = points3D[2]

    f1 = (P1 - C) / np.linalg.norm(P1 - C)
    f2 = (P2 - C) / np.linalg.norm(P2 - C)
    f3 = (P3 - C) / np.linalg.norm(P3 - C)
    
    featuresVect = np.concatenate((f1,f2,f3),axis=0)
    print("features vectors = \n",featuresVect)

    return featuresVect # Return the features vectors need in P3P