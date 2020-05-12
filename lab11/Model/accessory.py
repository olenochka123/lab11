from abc import ABC


class Accessory(ABC):

    def __init__(self, id, name, price,
                 weight,
                 producer, color):
        self.id = id
        self.name = name
        self.price = price
        self.weight = weight
        self.producer = producer
        self.color = color