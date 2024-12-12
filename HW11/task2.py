class Math:
    def addition(self, a, b):
        res = a + b
        print(res)
    
    def subtraction(self, a, b):
        res = a - b
        print(res)
    
    def multiplication(self, a, b):
        res = a * b
        print(res)
    
    def division(self, a, b):
        res = a / b
        print(res)

math = Math()
a = 9
b = 3
math.addition(a, b)
math.subtraction(a, b)
math.multiplication(a, b)
math.division(a, b)