class Car(object):
    def __init__(self, name='General', model='GM', type_car='saloon', num_of_doors=4, num_of_wheels=4, speed=0):
        self.name = name
        self.model = model
        self.num_of_doors = num_of_doors
        self.num_of_wheels = num_of_wheels
        self.type_car = type_car
        self.speed = speed

        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            self.num_of_doors = 2

        if self.type_car == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4
            self.type_car = 'saloon'

    def is_saloon(self):
        if self.type_car == 'saloon':
            return True
        else:
            return False

    def drive(self, moving_speed):
        if 3 < moving_speed <= 7:
            self.speed = 77
            return self
        elif 0 < moving_speed <= 3:
            self.speed = 1000
            return self
        else:
            return self
