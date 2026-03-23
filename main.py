from newtons_method import newtons_method
import numpy as np
import numpy.polynomial.polynomial as poly

degree = int(input("what degree is the polynomial? "))
coeffs = []
for i in range(degree+1):
    coeffs.append(int(input("Coefficient on power " + str(i) + " term: ")))
print(coeffs)
init_guess = int(input("Enter an initial guess: "))
maxit = 2000
TOL = 10e-13
p = poly.Polynomial(coeffs)
print(p)
newtons_method(init_guess, maxit, TOL, p)
