class A:
    def feature_a(self):
        return "Feature from A"
    def calculator(self, a, b):
        return a + b

class B:
    def feature_b(self):
        return "Feature from B"
    
    def calculator(self, a, b):
        return a * b

class C(A, B):
    def show(self, a, b):
        result = self.calculator(a, b)
        a_result = A.calculator(self, a, b) 
        b_result = B.calculator(self, a, b)
        print("self -->", result)
        print("a_result -->", a_result)
        print("b_result -->", b_result)
    pass


obj = C()
obj.show(2, 4)