class Car():
    def __init__(self,model,color):
        self.model = model
        self.color = color

    def print_car(self):
        print("The Car Model is", self.model)
        print("The Car Color is", self.color)

audi_a5 = Car("Audi A5", "Black")
audi_a5.print_car()
