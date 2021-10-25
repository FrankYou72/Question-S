from sympy import symbols


def symbolize(vars):
    tbe = ""

    for var in vars:
        tbe += var
        if vars.index(var) < len(vars)-1:
            tbe += ","

    tbe += "=symbols('"

    for var in vars:
        tbe += var
        if vars.index(var) < len(vars)-1:
            tbe += ","

    tbe += "')"

    return tbe