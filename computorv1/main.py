import sys
from parser import EquationParser 
from second_degree import SecondDegreeSolver 

# TODO: don't print the last term if it's zero
def print_reduced_form(equation):
    print("Reduced form:", end = " ")
    for (idx, term) in enumerate(equation):

        if (idx < len(equation) and idx > 0):
            sign = " + "
            if (term < 0):
                sign = ' - '
                term *= -1

            print(sign, end = "");

        if term.is_integer():
            term = int(term)

        print ("{} * X^{}".format(term, idx), end ="")
        

    print(" = 0")
        

def print_polynomial_degree(degree):
    print("Polynomial degree:", degree)

def print_cant_solve_equation():
    print("The polynomial degree is strictly greater than 2, I can't solve.") 

if __name__ == "__main__":
    # get the polinomial equation from the arguments
    equations = sys.argv[1].split("=")

    # get the two equation seperated by =
    p = EquationParser(equations)
    equation = p.parseEquation()

    print_reduced_form(equation)
    print_polynomial_degree(p.get_polinomail_degree())
    
    if (p.get_polinomail_degree() > 2):
        print_cant_solve_equation()
        exit()
    elif (p.get_polinomail_degree() == 2):
        p_2_solver =  SecondDegreeSolver(equation)
        p_2_solver.solve_equation()
        
        
# print reduced form is working but just for polinomials that are secoend degree or
# lower my thoughts is that I need to change simplify_equation to work with any polinomial
# by parssing X^Index and put it the simplified_terms[index]