from .Q_data import *
from .questionS import get_vars
import json

def refactor():
    refactored = {}

    for key in Packs.keys():
        refactored[key] = {}

        variables = Packs[key][0]
        equations = Packs[key][1]
        quantities = Packs[key][2]
        units = Packs[key][3]

        for theme in equations.keys():
            refactored[key][theme] = {}
            refactored[key][theme]["equation"] = str(equations[theme][0])
            refactored[key][theme]["problem"] = equations[theme][1]
            
            var_dict = get_vars(equations[theme][0], variables)
            refactored[key][theme]["variables"] = list(var_dict.keys())
            
            refactored[key][theme]["quantities"] = {}
            refactored[key][theme]["units"] = {}
            refactored[key][theme]['equations'] = {}

            for var in var_dict.keys():
                equation = solve(equations[theme][0], variables[var_dict[var]])
                refactored[key][theme]['equations'][var] = (str(equation))

                for q in quantities.keys():
                    if str(q) == var:
                        refactored[key][theme]["quantities"][var] = quantities[q]

                for unit in units.keys():
                    if str(unit) == var:
                        un = units[unit][0]
                        limits = units[unit][1]
                        min_limit = limits[0]
                        max_limit = limits[1]
                        factor = limits[2]

                        try:
                            min_power = limits[3]
                            max_power = limits[4]
                        except:
                            min_power = False
                            max_power = False

                        refactored[key][theme]["units"][var] = {}
                        refactored[key][theme]["units"][var]["unit"] = un
                        refactored[key][theme]["units"][var]["minLimit"] = min_limit
                        refactored[key][theme]["units"][var]["maxLimit"] = max_limit
                        refactored[key][theme]["units"][var]["factor"] = factor

                        if min_power and max_power:
                            refactored[key][theme]["units"][var]["minPower"] = min_power
                            refactored[key][theme]["units"][var]["maxPower"] = max_power

    with open('q_data.json', 'w', encoding="utf8") as db:
        json.dump(refactored, db, indent=4, ensure_ascii=False)

    return refactored
