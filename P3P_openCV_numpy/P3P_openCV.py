import cv2
import numpy as np 

def recup_solutions_openCV(points2D, points3D, A) : 

  retval, rvec, tvecs =  cv2.solveP3P(points3D,points2D,A,None, flags = cv2.SOLVEPNP_P3P)
  solutions = np.zeros((4,3,4))     # (4*3*4)

  for i in range(len(rvec)) : 
    rodriguez = rvec[i]     # (3*1)
    R_P3P = cv2.Rodrigues(rodriguez)[0]    # rotation matrix : (3*3)
    print("R_P3P=",R_P3P,"\n")

    T_P3P = tvecs[i]    # déjà ok (3*1) ?? translation matrix : (1*3)
   # T_P3P = np.reshape(T_P3P,(3,1))    # (3*1)
    print("T=",T_P3P,"\n")

    solutions[i,:,:1]= T_P3P
    solutions[i,:,1:] = R_P3P
  return solutions

