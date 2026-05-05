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
        print("A result:", A.calculator(self, a, b))
        print("B result:", B.calculator(self, a, b))

obj = C()

# Print MRO
print("MRO -->", C.mro())