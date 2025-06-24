import numpy as np
from P3P_numpy import *

# Test of roots_cubic
def test_roots_cubic(a,b,c,d):
  print("f(x) = ",a,"*x**3 + ",b,"*x**2 + ",c,"*x + ",d)
  def f(x,a,b,c,d):

    return a*x**3 + b*x**2 + c*x + d


  roots = roots_cubic(a,b,c,d)

  print('Roots :', roots,'\n')

  valeur_ok = True
  for r in roots :
    y = f(r,a,b,c,d)
    print('f(r) = ',y,'\n')
    if np.linalg.norm(y) > 10**(-10) :
      valeur_ok = False
  print('Valeurs inférieures en norme à 10^(-10) : ',valeur_ok, '\n')


test_roots_cubic(np.random.uniform(-20,20),np.random.uniform(-20,20),np.random.uniform(-20,20),np.random.uniform(-20,20))

# Tests of roots_ferrari

def test_roots_ferrari(a0,a1,a2,a3,a4,):
  print("f(x) = ",a4,"*x**4 + ",a3,"*x**3 + ",a2,"*x**2 + ",a1,"*x + ",a0)

  def f(x,a0,a1,a2,a3,a4) :
    return a4*x**4+a3*x**3 + a2*x**2 + a1*x + a0

  roots = roots_ferrari(np.array([a0,a1,a2,a3,a4]))

  print('Roots :', roots,'\n')

  valeur_ok = True
  for r in roots :
    y = f(r,a0,a1,a2,a3,a4)
    print('f(r) = ',y,'\n')
    if np.linalg.norm(y) > 10**(-10) :
      valeur_ok = False
  print('Valeurs inférieures en norme à 10^(-10) : ',valeur_ok, '\n')

test_roots_ferrari(np.random.uniform(-20,20),np.random.uniform(-20,20),np.random.uniform(-20,20),np.random.uniform(-20,20),np.random.uniform(-20,20))
