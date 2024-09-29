import re

class EquationParser:
    def __init__(self, equations) -> None:
        self.equation_1 = equations[0]
        self.equation_2 = equations[1]
        self.equation_1_terms = []
        self.equation_2_terms = []
        self.combined_equation = []
        self.polynomial_degree = 0
        self.var = ""
        

    def parseEquation(self):
        self.equation_1_terms = self.format_equation_to_have_pluses(self.equation_1)
        self.equation_2_terms = self.format_equation_to_have_pluses(self.equation_2)

        self.equation_1_terms = self.simplify_equation(self.equation_1_terms)
        self.equation_2_terms = self.simplify_equation(self.equation_2_terms)

        self.combine_the_two_equations()
        
        return self.combined_equation
    
    def get_polinomail_degree(self):
        return self.polynomial_degree

        
    def combine_the_two_equations(self):
        if len(self.equation_1_terms) < len(self.equation_2_terms):
            size = len(self.equation_1_terms)
        else:
            size = len(self.equation_2_terms)
            
        for i in range(0, size):
            self.combined_equation.append(self.equation_1_terms[i] + -1 * self.equation_2_terms[i])

        while size < len(self.equation_1_terms):
            self.combined_equation.append(self.equation_1_terms[size]) 
            size += 1
        while size < len(self.equation_2_terms):
            self.combined_equation.append(self.equation_2_terms[size] * -1) 
            size += 1
        
        
    def format_equation_to_have_pluses(self, equation):
        terms = re.split(" - ", equation)
        index = 1;
        while index < len(terms):
            terms[index] = '-' + terms[index]
            index += 1
        
        return " + ".join(terms).split(" + ")
    
    def simplify_equation(self, terms):
        simplified_terms = [0.0] * 3
        for term in terms:
            exponent = self.get_integer(term.split("*")[1].split("^")[1])
            self.check_for_varaible(term.split("*")[1].split("^")[0].strip())
            
            if (exponent > self.polynomial_degree):
                self.polynomial_degree = exponent 
            
            if len(simplified_terms) <= exponent:
                simplified_terms.extend([0.0] * (exponent - len(simplified_terms) + 1))

            coefficient = self.get_float(term.split("*")[0])
            simplified_terms[exponent] += coefficient 

        return simplified_terms

    def get_integer(self, string):
        try:
            num = int(string)
            return num
        except ValueError:
            self.print_error("exponent is not a variable")
            exit()

    def get_float(self, string):
        try:
            num = float(string)
            return num
        except ValueError:
            self.print_error("coefficient is not valid")
            exit()

    def check_for_varaible(self, string):
        if self.var == "":
            self.var = string
        elif self.var != string:
            self.print_error("variable don't match")
            exit()
        

    def print_error(self, error_message):
        print("Syntax Error:", error_message)
        

