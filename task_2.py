class Road:
    def __init__(self, len_road, width_road):
        self._length = len_road
        self._width = width_road

    def calculate(self, thickness=5):
        print(f"Для Вашей дороги потребуется {self._length * self._width * 25 * thickness // 1000}т асфальта")


try:
    my_road = Road(20, 5000)
    my_road.calculate()
except KeyboardInterrupt:
    print("Exit!")