class Flashlight(BikeAccessory):
    def __init__(self, flash_power=None, is_on=None):
        self.flash_power = flash_power
        self.is_on = is_on
        super().__init__()
