from newtons_method import newtons_method
import numpy as np
import numpy.polynomial.polynomial as poly


x = np.linspace(-1,1,3)
y = x

X, Y = np.meshgrid(x, y)

init_guesses = X + Y * 1j

rows = init_guesses.shape[0]
cols = init_guesses.shape[1]
roots = np.zeros((rows,cols), dtype=complex)
    
degree = int(input("what degree is the polynomial? "))
coeffs = []
for i in range(degree+1):
    coeffs.append(int(input("Coefficient on power " + str(i) + " term: ")))
print(coeffs)
maxit = 2000
TOL = 10e-13
p = poly.Polynomial(coeffs)
print(p)

for i in range(rows):
    for j in range(cols):
        init_guess = init_guesses[i,j]
        converged, root = newtons_method(init_guess, maxit, TOL, p)
        if converged == True:
            roots[i,j] = root
        else:
            roots[i,j] = np.nan
