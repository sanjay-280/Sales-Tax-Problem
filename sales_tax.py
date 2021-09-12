from constants import BASIC_TAX, IMPORT_TAX
from utils import calculate_tax


class CalculateTax:
    """
    This class is used to calculate the tax for all the items present in the shopping cart
    """
    def calculate_total_tax(self, cart_details):
        for item in cart_details:
            basic_tax = 0
            import_tax = 0
            is_basic_tax = item['is_basic_tax']
            is_imported = item['is_imported']
            item_price = item['item_price']

            if is_basic_tax:
                basic_tax = self.__calculate_basic_tax(item_price)

            if is_imported:
                import_tax = self.__calculate_import_tax(item_price)

            # Calculating total tax for each item
            total_tax = basic_tax + import_tax
            item['total_tax'] = round(total_tax, 2)
            item['item_price'] = round(float(item_price) + total_tax, 2)

        return cart_details

    @staticmethod
    def __calculate_basic_tax(item_price):
        """
        :param item_price: Calculates basic tax w.r.t item price
        :return:
        """
        tax = calculate_tax(BASIC_TAX, item_price)
        return tax

    @staticmethod
    def __calculate_import_tax(item_price):
        """
        :param item_price: Calculates import tax w.r.t item price
        :return:
        """
        tax = calculate_tax(IMPORT_TAX, item_price)
        return tax

