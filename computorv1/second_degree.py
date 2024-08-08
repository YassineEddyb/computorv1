import math

class SecondDegreeSolver:
    def __init__(self, equation) -> None:
        self.a = equation[2]
        self.b = equation[1]
        self.c = equation[0]
        self.delta = (self.b * self.b) - (4 * self.a * self.c)
    
    def solve_equation(self):
        # print(self.a, self.b, self.c, self.delta)
        if (self.delta == 0):
            print(self.get_one_solution())
        elif (self.delta > 0):
            solutions = self.get_two_solutions();
            print(solutions[0], "\n", solutions[1])
        else:
            print("No solution exist in real numbers.")

    
    def get_one_solution(self):
        pass

        
    def get_two_solutions(self):
        solution_1 = (- self.b + math.sqrt(self.delta)) / (2 * self.a)
        solution_2 = (- self.b - math.sqrt(self.delta)) / (2 * self.a)
        return [solution_1, solution_2]
