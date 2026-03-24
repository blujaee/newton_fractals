from newtons_method import newtons_method
from multivariate_newtons_method import multivariate_newtons_method
import numpy as np
import numpy.polynomial.polynomial as poly
import math as m

# only allow coefficient input for now and then later add trig fns and stuff 
    
num_poly = bool(input("How many polynomials?"))
for j in range(num_poly+1):
    degree = int(input("what degree is polynomial number " + str(j+1) + " ?"))
    coeffs = np.array([])
    if num_poly > 1:
        vector = np.array([])
        for i in range(num_poly):
            vector = np.append(vector, int(input("what degree is the polynomial?")))
    else:
        for i in range(degree+1):
            coeffs = np.append(coeffs, int(input("Coefficient on power " + str(i) + " term: ")))

norm_factor = 1 / coeffs[degree]
norm_coeffs = norm_factor * coeffs
cauchy_upper = 1 + np.max(np.abs(norm_coeffs))
if cauchy_upper <0:
    rounded_bound = m.floor(cauchy_upper)
else:
    rounded_bound = m.ceil(cauchy_upper)

x = np.linspace(-rounded_bound*2,rounded_bound*2,500)
y = x

X, Y = np.meshgrid(x, y)

init_guesses = X + Y * 1j

rows = init_guesses.shape[0]
cols = init_guesses.shape[1]
convergence = np.zeros((rows,cols))
roots = []
iter_counts = np.zeros((rows,cols))
colors = np.zeros((rows,cols,3))
maxit = 2000
TOL = 1e-6
p = poly.Polynomial(coeffs)
print(p)
max_k = 0

for i in range(rows):
    for j in range(cols):
        init_guess = init_guesses[i,j]
        if num_poly == 1:
            converged, root, k = multivariate_newtons_method(init_guess, maxit, TOL, p)
        else:
            converged, root, k = newtons_method(init_guess, maxit, TOL, p)
        if converged == True:
            for b,r in enumerate(roots):
                if abs(root - r) < TOL:
                    #print("no new roots to append")
                    convergence[i,j] = b
                    iter_counts[i,j] = k
                    if k > max_k:
                        max_k = k
                    break
            else:
                #print("adding root to list")
                roots.append(root)
                convergence[i,j] = len(roots) - 1 
                iter_counts[i,j] = k

        else:
            convergence[i,j] = np.nan
            
print(roots)
scaled_iter_counts = 1/np.max(iter_counts) * iter_counts
scaled_convergence = convergence + scaled_iter_counts
