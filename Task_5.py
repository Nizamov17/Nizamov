class TrafficLight:

    def __init__(self):
        self.__color = "red"

    def __color_change(self, color, duration):
        import time
        self.__color = color
        print(f"Traffic light is {color}")
        time.sleep(duration)

    def running(self):
        while True:
            self.__color_change("red", 1)
            self.__color_change("green", 2)
            self.__color_change("yellow", 0.5)

traffic_light = TrafficLight()
traffic_light.running()