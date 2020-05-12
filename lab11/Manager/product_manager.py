from typing import List
from bike_accessory import BikeAccessory
from bike_type import BikeType
from doctest import testmod


class ProductManager:
    def __init__(self):
        self.list_of_products: List[BikeAccessory] = []

    def find_products_by_bike_type(self, bike_type: BikeType) -> List[BikeAccessory]:
        """
        Test of correct founding products in the list
        >>> product_manager = ProductManager()
        >>> product_manager.list_of_products.append(BikeAccessory(0, 'yulo1', 2000, 310, 'mercedes', 'grey', BikeType.MOUNTAIN))
        >>> product_manager.list_of_products.append(BikeAccessory(1, 'yulo2', 2000, 300, 'mercedes', 'grey', BikeType.URBAN))
        >>> product_manager.list_of_products.append(BikeAccessory(2, 'yulo3', 2000, 320, 'bmw','grey', BikeType.TRACK))
        >>> product_manager.list_of_products.append(BikeAccessory(3, 'yulo4', 2000, 20, 'nissan', 'grey', BikeType.TRACK))
        >>> list_of_founded_products_by_bike_type = product_manager.find_products_by_bike_type(BikeType.TRACK)
        >>> len(list_of_founded_products_by_bike_type)
        2
        """
        list_of_founded_products: List[BikeAccessory] = []
        for product in self.list_of_products:
            if product.bike_type == bike_type:
                list_of_founded_products.append(product)
        return list_of_founded_products

    def find_products_by_producer(self, producer) -> List[BikeAccessory]:
        """
        Test of correct founding products in the list
        >>> product_manager = ProductManager()
        >>> product_manager.list_of_products.append(BikeAccessory(0, 'yulo1', 2000, 310, 'mercedes', 'grey', BikeType.MOUNTAIN))
        >>> product_manager.list_of_products.append(BikeAccessory(1, 'yulo2', 2000, 300, 'mercedes', 'grey', BikeType.URBAN))
        >>> product_manager.list_of_products.append(BikeAccessory(2, 'yulo3', 2000, 320, 'bmw','grey', BikeType.TRACK))
        >>> product_manager.list_of_products.append(BikeAccessory(3, 'yulo4', 2000, 20, 'nissan', 'grey', BikeType.TRACK))
        >>> list_of_founded_products_by_producer = product_manager.find_products_by_producer('bmw')
        >>> len(list_of_founded_products_by_producer)
        1
        """
        list_of_founded_products: List[BikeAccessory] = []
        for product in self.list_of_products:
            if product.producer == producer:
                list_of_founded_products.append(product)
        return list_of_founded_products
