import re

class EquationParser:
    def __init__(self, equations) -> None:
        self.equation_1 = equations[0]
        self.equation_2 = equations[1]
        self.equation_1_terms = []
        self.equation_2_terms = []
        self.combined_equation = []
        self.polynomial_degree = 0
        

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
            index = int(term.split(" * ")[1].split("^")[1])
            
            if (index > self.polynomial_degree):
                self.polynomial_degree = index
            
            if len(simplified_terms) <= index:
                simplified_terms.extend([0.0] * (index - len(simplified_terms) + 1))

            simplified_terms[index] += float(term.split(" * ")[0])

        
        return simplified_terms
