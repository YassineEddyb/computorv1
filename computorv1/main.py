import sys
from parser import EquationParser 

def print_reduced_form(equation):
    print("Reduced form: ", end = " ")
    for (idx, term) in enumerate(equation):
        if (term == 0):
            continue

        if (idx < len(equation) and idx > 0):
            sign = " + "
            if (term < 0):
                sign = ' - '
                term *= -1

            print(sign, end = "");

        print ("{} * X^{}".format(term, idx), end ="")
        

    print(" = 0")
        


if __name__ == "__main__":
    # get the polinomial equation from the arguments
    equations = sys.argv[1].split(" = ")

    # get the two equation seperated by =
    p = EquationParser(equations);
    equation = p.parseEquation()

    print_reduced_form(equation);