class Tranport:
    def __init__(self, model, color, numberWheels, weight, speed):
        self.color = color
        self.model = model
        self.numberWheels = numberWheels
        self.weight = weight
        self.speed = speed

    def __str__(self):
        return 'Model: ' + self.model + '\nColor: ' + self.color + '\nNumber wheels: ' + str(self.numberWheels) + '\nWeight: ' + self.weight + '\nSpeed: ' + self.speed

    def drive(self):
        print('Drive!')

class Car(Tranport):
    def __init__(self, model, color, numberWheels, weight, speed):
        super().__init__(model, color, numberWheels, weight, speed)

    def __str__(self):
        return super(Car, self).__str__()

    def drive(self):
        print('Drive!')


class Motobike(Tranport):
    def __init__(self, model, color, numberWheels, weight, speed):
        super().__init__(model, color, numberWheels, weight, speed)

    def __str__(self):
        return super(Motobike, self).__str__()

    def drive(self):
        print('Drive!')

class Truck(Tranport):
    def __init__(self, model, color, numberWheels, weight, speed):
        super().__init__(model, color, numberWheels, weight, speed)

    def __str__(self):
        return super(Truck, self).__str__()

    def drive(self):
        print('Drive!')

class Bicycle(Tranport):
    def __init__(self, model, color, numberWheels, weight, speed):
        super().__init__(model, color, numberWheels, weight, speed)

    def __str__(self):
        return super(Bicycle, self).__str__()

    def drive(self):
        print('Drive!')

class Program():
    def transport(self, usertransport):
        if usertransport == 'Auto':
            print(Car('TOYOTA PRIUS', 'white',  4, '1470 mm', '180 km/h'))
            Car.drive(Car)
        elif usertransport == 'Motobike':
            print(Motobike('Harley-Davidson Breakout 114', 'vinous', 2, '665 mm', '300 km/h'))
            Motobike.drive(Motobike)
        elif usertransport == 'Truck':
            print(Truck('Камаз 4310', 'black', 6, '3450 mm', '85 km/h'))
            Truck.drive(Truck)
        elif usertransport == 'Bicycle':
            print(Bicycle('TERRA LINDA 2', 'red', 2, '178 mm', '20 km/h'))
            Bicycle.drive(Bicycle)

transport = input('Enter transport (Auto, Motobike, Truck, Bicycle): ')
Program.transport(Program, transport)