class Lock(BikeAccessory):
    def __init__(self, security_level=None, is_locked=None):
        self.security_level = security_level
        self.is_locked = is_locked
        super().__init__()

