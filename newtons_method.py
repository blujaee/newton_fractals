import numpy as np
from sympy import lambdify
def newtons_method(init_guess, maxit, TOL, expr, var):
    converged = True
    f = lambdify(var, expr, "numpy")
    deriv_expr = sympy.diff(expr, var)
    f_prime = lambdify(var, deriv_expr, "numpy")
    for k in range(maxit):
        f_x = f(init_guess)
        f_prime_x = f_prime(init_guess)
        if abs(f_prime_x) < TOL:
            #print("failed to complete iteration due to division by 0")
            converged = False
            break
        new_guess = init_guess - (f_x / f_prime_x)
        if abs(new_guess-init_guess) < TOL or abs(new_guess) < TOL:
            #print("Converged at ", k, " iterations.")
            #print("Root is: ", new_guess)
            break
        init_guess = new_guess
        if k == maxit-1:
            print("failed to converge, hit maxit")
            converged = False
            break
    
    return converged, init_guess, k