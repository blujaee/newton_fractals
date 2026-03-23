import numpy as np
import numpy.polynomial.polynomial as poly

def newtons_method(init_guess, maxit, TOL, p):
    for k in range(maxit):
        f_x = p(init_guess)
        deriv = p.deriv()
        f_prime = deriv(init_guess)
        if abs(f_prime) < TOL:
            print("failed to converge due to division by 0")
            break
        new_guess = init_guess - (f_x / f_prime)
        if abs(new_guess-init_guess) < TOL:
            print("Converged at ", k, " iterations.")
            print("Root is: ", new_guess)
            break
        
        init_guess = new_guess
        if k == maxit-1:
            print("failed to converge, hit maxit")
            break
    
    return init_guess