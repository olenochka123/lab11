from bike_accessory import BikeAccessory
from product_manager import ProductManager
from bike_type import BikeType
from doctest import testmod


class Utils:
    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    def sort_by_price(self, is_descending):
        """
        Sorts List of Products in given order, returns List of Products
        >>> ba1 = BikeAccessory(0, "yulo1", 20, 310, "mercedes", "grey", BikeType.MOUNTAIN)
        >>> ba2 = BikeAccessory(1, "yulo2", 567, 300, "mercedes", "grey", BikeType.URBAN)
        >>> ba3 = BikeAccessory(2, "yulo3", 87, 320, "bmw","grey", BikeType.TRACK)
        >>> ba4 = BikeAccessory(3, "yulo4", 583, 20, "nissan", "grey", BikeType.TRACK)
        >>> product_list = [ba1, ba2, ba3, ba4]
        >>> utils = Utils(product_list)
        >>> list_of_products_sorted_by_price = utils.sort_by_price(False)
        >>> [ba1.price]
        [20]
        >>> [product.price for product in list_of_products_sorted_by_price]
        [20, 87, 567, 583]
        >>> list_of_products_sorted_by_price = utils.sort_by_price(True)
        >>> [product.price for product in list_of_products_sorted_by_price]
        [583, 567, 87, 20]
        """
        if is_descending == False:
            list_of_products_sorted_by_price = sorted(self.list_of_products, key=lambda product: product.price, reverse=False)
        if is_descending == True:
            list_of_products_sorted_by_price = sorted(self.list_of_products, key=lambda product: product.price, reverse=True)
        return list_of_products_sorted_by_price

    def sort_by_weight(self, is_descending):
        """
        Sorts List of Products in given order, returns List of Products
        >>> ba1 = BikeAccessory(0, "yulo1", 20, 310, "mercedes", "grey", BikeType.MOUNTAIN)
        >>> ba2 = BikeAccessory(1, "yulo2", 567, 300, "mercedes", "grey", BikeType.URBAN)
        >>> ba3 = BikeAccessory(2, "yulo3", 87, 320, "bmw","grey", BikeType.TRACK)
        >>> ba4 = BikeAccessory(3, "yulo4", 583, 20, "nissan", "grey", BikeType.TRACK)
        >>> product_list = [ba1, ba2, ba3, ba4]
        >>> utils = Utils(product_list)
        >>> list_of_products_sorted_by_weight = utils.sort_by_weight(False)
        >>> [ba1.weight]
        [310]
        >>> [product.weight for product in list_of_products_sorted_by_weight]
        [20, 300, 310, 320]
        >>> list_of_products_sorted_by_weight = utils.sort_by_weight(True)
        >>> [product.weight for product in list_of_products_sorted_by_weight]
        [320, 310, 300, 20]
        """
        if is_descending == False:
            list_of_products_sorted_by_weight = sorted(self.list_of_products, key=lambda product: product.weight, reverse=False)
        if is_descending == True:
            list_of_products_sorted_by_weight = sorted(self.list_of_products, key=lambda product: product.weight, reverse=True)
        return list_of_products_sorted_by_weight