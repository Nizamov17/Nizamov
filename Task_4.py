class Car:
    def __init__(self, color, brand, body, speed, transmission):
        self.color = color
        self.brand = brand
        self.body = body
        self.speed = speed
        self.transmission = transmission

    def start(self):
        print("Машина начала движение")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print("Машина повернула", direction)

    def speed_up(self):
        self.speed += 20
        print("Машина ускорилась и едет со скоростью", self.speed)
        self.check_speed()

    def speed_down(self):
        self.speed -= 20
        print("Машина замедлилась и едет со скоростью", self.speed)

    def beep(self):
        print("Би-бип")

    def check_speed(self):
        if self.body == 'truck' and self.speed > 60:
            print("Скорость превышена! Разрешенная скорость 60 км/ч")
        elif self.body == 'sedan' and self.speed > 80:
            print("Скорость превышена! Разрешенная скорость 80 км/ч")


class Truck(Car):
    def __init__(self, color, brand, body, speed, transmission, max_weight):
        super().__init__(color, brand, body, speed, transmission)
        self.max_weight = max_weight

    def load(self, weight):
        if weight > self.max_weight:
            print("Машина перегружена")
        else:
            print("Машина загружена, можно ехать")


class Sedan(Car):
    pass


car = Sedan('black', 'Mercedes', 'sedan', 80, 'auto')
truck = Truck('white', 'Volvo', 'truck', 50, 'auto', 5000)

car.start()
car.turn('направо')
car.speed_up()
car.speed_down()
car.beep()
car.stop()

truck.start()
truck.turn('налево')
truck.speed_up()
truck.load(6000)
truck.speed_down()
truck.beep()
truck.stop()
