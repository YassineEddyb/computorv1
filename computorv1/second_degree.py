import math

class SecondDegreeSolver:
    def __init__(self, equation) -> None:
        self.a = equation[2]
        self.b = equation[1]
        self.c = equation[0]
        self.delta = (self.b * self.b) - (4 * self.a * self.c)
    
    def solve_equation(self):
        if (self.delta == 0):
            self.print_solution(self.get_one_solution())
        elif (self.delta > 0):
            solutions = self.get_two_solutions()
            self.print_solution(solutions[0])
            self.print_solution(solutions[1])
        else:
            print("No solution exist in real numbers.")

    def print_solution(sefl, number):
        print("{:.6f}".format(number))
    
    def get_one_solution(self):
        return (- self.b) / (2 * self.a)

        
    def get_two_solutions(self):
        solution_1 = (- self.b + math.sqrt(self.delta)) / (2 * self.a)
        solution_2 = (- self.b - math.sqrt(self.delta)) / (2 * self.a)
        return [solution_1, solution_2]
