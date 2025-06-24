import numpy as np
from P3P_numpy import *

# Test of roots_cubic
def test_polynomial_root_calculation_3rd_degree(a,b,c,d):
  print("---- Begin of test_polynomial_root_calculation_3rd_degree ----")


  # Polynomial whose roots we are looking for : 
  print("f(x) = ",a,"*x**3 + ",b,"*x**2 + ",c,"*x + ",d)

  # Calculation of the polynomial 
  def f(x,a,b,c,d):
    return a*x**3 + b*x**2 + c*x + d

  # Computation of the roots 
  roots = polynomial_root_calculation_3rd_degree(a,b,c,d)
  print('Roots :', roots,'\n')

  valeur_ok = True  # true if all roots values are close to zero (<10^(-10))

  for r in roots :
    # Calculation of the polynomial applied to the root 
    y = f(r,a,b,c,d)
    print('f(r) = ',y,'\n')

    if np.linalg.norm(y) > 10**(-10) :
      valeur_ok = False

  print('Valeurs inférieures en norme à 10^(-10) : ',valeur_ok, '\n')


test_polynomial_root_calculation_3rd_degree(np.random.uniform(-20,20),np.random.uniform(-20,20),np.random.uniform(-20,20),np.random.uniform(-20,20))

# Tests of roots_ferrari

def test_polynomial_root_calculation_4th_degree_ferrari(a0,a1,a2,a3,a4,):
  print("---- Begin of test_polynomial_root_calculation_4th_degree_ferrari ----")

  # Polynomial whose roots we are looking for : 
  print("f(x) = ",a4,"*x**4 + ",a3,"*x**3 + ",a2,"*x**2 + ",a1,"*x + ",a0)

  # Calculation of the polynomial 
  def f(x,a0,a1,a2,a3,a4) :
    return a4*x**4+a3*x**3 + a2*x**2 + a1*x + a0

  # Computation of the roots
  roots = polynomial_root_calculation_4th_degree_ferrari(np.array([a0,a1,a2,a3,a4]))
  print('Roots :', roots,'\n')

  valeur_ok = True # true if all roots values are close to zero (<10^(-10))

  for r in roots :
    # Calculation of the polynomial applied to the root 
    y = f(r,a0,a1,a2,a3,a4)
    print('f(r) = ',y,'\n')

    if np.linalg.norm(y) > 10**(-10) :
      valeur_ok = False
      
  print('Valeurs inférieures en norme à 10^(-10) : ',valeur_ok, '\n')

test_polynomial_root_calculation_4th_degree_ferrari(np.random.uniform(-20,20),np.random.uniform(-20,20),np.random.uniform(-20,20),np.random.uniform(-20,20),np.random.uniform(-20,20))
