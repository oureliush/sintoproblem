from sympy import symbols, Eq, solve

x, y = symbols('d ')
equation = Eq(x**2 + 2*x - 3, 0) # Defines the equation x^2 + 2x - 3 = 0

solutions = solve(equation, x) # Solves for x
print(solutions)
