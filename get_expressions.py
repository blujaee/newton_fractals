import sympy
from sympy.parsing.sympy_parser import parse_expr

def get_expressions():

    var_input = input("Enter variable names (e.g., 'x, y, z'): ")
    symbols_list = sympy.symbols(var_input, seq=True)
    symbols_dict = {s.name: s for s in symbols_list}

    expressions_list = []
    print(f"Enter expressions using variables: {var_input}. Type 'done' when finished.")
    while True:
        expr_input = input(f"Enter expression (or 'done'): ")
        if expr_input.lower() == 'done':
            break
        expr = parse_expr(expr_input, local_dict=symbols_dict)
        expressions_list.append(expr)

    F = sympy.Matrix(expressions_list)
    J = F.jacobian(symbols_list)
    
    return F, J, expressions_list, symbols_list, symbols_dict
