import re

class EquationParser:
    def __init__(self, equations) -> None:
        self.equation_1 = equations[0]
        self.equation_2 = equations[1]
        self.equation_1_terms = []
        self.equation_2_terms = []
        self.combined_equation = [0,0,0]
        

    def parseEquation(self):
        self.equation_1_terms = self.format_equation_to_have_pluses(self.equation_1)
        self.equation_2_terms = self.format_equation_to_have_pluses(self.equation_2)

        self.equation_1_terms = self.simplify_equation(self.equation_1_terms)
        self.equation_2_terms = self.simplify_equation(self.equation_2_terms)

        self.combine_the_two_equations();
        
        return self.combined_equation;

        
    def combine_the_two_equations(self):
        for i in range (0, 3):
            self.combined_equation[i] = self.equation_1_terms[i] + -1 * self.equation_2_terms[i]
            
        
        
    def format_equation_to_have_pluses(self, equation):
        terms = re.split(" - ", equation)
        index = 1;
        while index < len(terms):
            terms[index] = '-' + terms[index]
            index += 1
        
        return " + ".join(terms).split(" + ")
    
    def simplify_equation(self, terms):
        simplified_terms = [0,0,0]
        for term in terms:
            if term.find("X^0") != -1:
                simplified_terms[0] += float(term.split(" * ")[0])
            elif term.find("X^1") != -1:
                simplified_terms[1] += float(term.split(" * ")[0])
            elif term.find("X^2") != -1:
                simplified_terms[2] += float(term.split(" * ")[0])
            else:
                print("The polynomial degree is strictly greater than 2, I can't solve.")

        
        return simplified_terms
