import numpy as np
from sympy import lambdify


def make_multivariate_funcs(expressions_list, symbols_list, J_mat):
    F_lambdas = [lambdify(symbols_list, expr, "numpy") for expr in expressions_list]
    J_lambdas = [
        [lambdify(symbols_list, J_mat[i, j], "numpy") for j in range(J_mat.shape[1])]
        for i in range(J_mat.shape[0])
    ]

    def F_func(x):
        return np.array([f(*x) for f in F_lambdas], dtype=complex)

    def J_func(x):
        return np.array([[entry(*x) for entry in row] for row in J_lambdas], dtype=complex)

    return F_func, J_func


def multivariate_newtons_method(init_guess, maxit, TOL, F_func, J_func):
    converged = True
    x = np.array(init_guess, dtype=complex)
    for k in range(maxit):
        F_val = F_func(x)
        J_val = J_func(x)
        if abs(np.linalg.det(J_val)) < TOL:
            converged = False
            break
        delta = np.linalg.solve(J_val, -F_val)
        new_x = x + delta
        if np.linalg.norm(new_x - x) < TOL:
            break
        x = new_x
        if k == maxit - 1:
            converged = False
            break
    return converged, x, k