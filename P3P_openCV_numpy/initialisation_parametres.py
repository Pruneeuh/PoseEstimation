import numpy as np 

def camera() : 
  # Definition of the camera parameters
    # focal length
  fx = 60
  fy = 40
    # center
  cx = 0
  cy = 0

  A = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]]) # intraseca matrix of the camera (3*3)
  return A

A = camera()

def rotation_matrix() : 
  R = np.array([[1, 0, 0],[0, -1, 0], [0, 0, -1]])
  print("R = \n",R)
  return R

def camera_translation() : 
  T = np.array([[0,0,6]])    # T = [tx,ty,tz]  (1*3)
  T = T.reshape((3,1))                       # (3*1)
  print("T = \n",T)
  return T

def point3Daleatoire(x) :
  return np.array([[np.random.uniform(-x,x),np.random.uniform(-x,x),np.random.uniform(-x,x)]])

def pts_3D_4pts():
  # generate randomly 4 3D points 

  P1 = point3Daleatoire(2)     # (1*3) -> pour P3P
  P2 = point3Daleatoire(2)
  P3 = point3Daleatoire(2)
  P4 = point3Daleatoire(2)
  
  points3D = np.concatenate((P1,P2,P3,P4),axis=0);     # (3*3)
  return points3D

def pts_3D_3pts(pts_3D_4pts):
  # return only the 3 first points uses in P3P

  return pts_3D_4pts[:,:3]

def projection3D2D(point3D,T,R,A) :
  # 3D point = [ Xw, Yw, Zw ]'   (1*3)
  # T : camera translation matrix : (3*1)
  # R : camera rotation matrix : (3*3)
  # A : intraseca matrix of the camera : (3*3)

  PI = np.concatenate((np.eye(3),np.zeros((3,1))),axis=1)  # (3*4)
  
  Rt = np.concatenate((R,T),axis=1)               # (3*4)
  Rt = np.concatenate((Rt,np.array([[0,0,0,1]])),axis=0)   # (4*4)

  point3D_bis = np.concatenate((np.reshape(point3D,(3,1)),np.array([[1]])),axis=0)   #(4*1)
 
  point2D = A @ PI @ Rt @ point3D_bis   # 2D point = [u, v, w] (3*1)
  point2D = point2D / point2D[2]        # 2D point = [u, v, 1] (3*1)
  return point2D[:2]


def pts_2D_4pts(points3D,T,R,A): 
  # Gerenrate the 2pt from  3d points and camera's parameters
  P1 = points3D[0]
  P2 = points3D[1]
  P3 = points3D[2]
  P4 = points3D[3]
  print(np.shape(P1))

  p1 = projection3D2D(P1,T,R,A)   # (2*1)
  p1 = np.reshape(p1,(1,2))       # (1,2)
  p2 = projection3D2D(P2,T,R,A)
  p2 = np.reshape(p2,(1,2))
  p3 = projection3D2D(P3,T,R,A)
  p3 = np.reshape(p3,(1,2))
  p4 = projection3D2D(P4,T,R,A)
  p4 = np.reshape(p4,(1,2))

  points2D = np.concatenate((p1,p2,p3,p4),axis=0) #(4*2)
  return points2D

def pts_2D_3pts(points_2D_4pts) : 
  return points_2D_4pts[:,:3]

def features_vectors(points3D,T) :
  P1 = points3D[0]
  P2 = points3D[1]
  P3 = points3D[2]

  f1 = (P1 - np.transpose(T)) / np.linalg.norm(P1 - T)
  f2 = (P2 - np.transpose(T)) / np.linalg.norm(P2 - T)
  f3 = (P3 - np.transpose(T)) / np.linalg.norm(P3 - T)
  
  featuresVect = np.concatenate((f1,f2,f3),axis=0)
  print("featuresVect = \n",featuresVect)
  return featuresVect