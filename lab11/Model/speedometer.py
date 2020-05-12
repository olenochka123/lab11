class Speedometer(BikeAccessory):
    def __init__(self, speed=None, distance=None, is_on=None):
        self.speed = speed
        self.distance = distance
        self.is_on = is_on
        super().__init__()