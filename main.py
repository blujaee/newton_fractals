from newtons_method import newtons_method, make_newton_funcs
from multivariate_newtons_method import multivariate_newtons_method, make_multivariate_funcs
import numpy as np
from get_expressions import get_expressions

ROUND_DIGITS = 4
bound = 5
maxit = 2000
TOL = 1e-9

def round_root(root):
    r = np.atleast_1d(np.array(root, dtype=complex))
    return tuple(np.round(r.real, ROUND_DIGITS) + np.round(r.imag, ROUND_DIGITS) * 1j)

def run():
    F_mat, J_mat, expressions_list, symbols_list, symbols_dict = get_expressions()

    x = np.linspace(-bound, bound, 500)
    y = np.linspace(-bound, bound, 500)
    X, Y = np.meshgrid(x, y)
    init_guesses = X + Y * 1j

    rows = init_guesses.shape[0]
    cols = init_guesses.shape[1]
    convergence = np.zeros((rows, cols))
    roots = []
    iter_counts = np.zeros((rows, cols))
    max_k = 0

    expr = expressions_list[0]
    var = symbols_list[0]

    if len(symbols_list) == 1:
        f, f_prime = make_newton_funcs(expr, var)
    else:
        F_func, J_func = make_multivariate_funcs(expressions_list, symbols_list, J_mat)

    seen_roots = {}  # rounded root -> index

    for i in range(rows):
        for j in range(cols):
            if len(symbols_list) > 1:
                init_guess = np.array([X[i, j], Y[i, j]])
                converged, root, k = multivariate_newtons_method(init_guess, maxit, TOL, F_func, J_func)
            else:
                init_guess = init_guesses[i, j]
                converged, root, k = newtons_method(init_guess, maxit, TOL, f, f_prime)

            if converged:
                key = round_root(root)
                if key not in seen_roots:
                    seen_roots[key] = len(roots)
                    roots.append(root)
                convergence[i, j] = seen_roots[key]
                iter_counts[i, j] = k
                if k > max_k:
                    max_k = k
            else:
                convergence[i, j] = np.nan

    print(roots)
    return convergence, iter_counts, rows, cols, max_k, roots

