from constants import BASIC_TAX_EXEMPT
from sales_tax import CalculateTax


# Added items in cart represented in list format
order_one = [
    '1 book at 12.49',
    '1 music CD at 14.99',
    '1 chocolate bar at 0.85'
]

order_two = [
    '1 imported box of chocolates at 10.00',
    '1 imported bottle of perfume at 47.50'
]

order_three = [
    '1 imported bottle of perfume at 27.99',
    '1 bottle of perfume at 18.99',
    '1 packet of headache pills at 9.75',
    '1 box of imported chocolates at 11.25',
]


class ShoppingCart:
    def __init__(self, item_list):
        self.item_list = item_list

    def finalize_cart(self):
        """
        Based on the item details passed it loops through all the items and extract necessary item details for
        calculating tax and displaying item details and returns array of objects.
        """
        cart_details = []
        for item in self.item_list:
            item_detail_object = {}
            item_detail = item.split(' ')
            last_index_of_list = len(item_detail) - 1
            item_name = self.__get_item_name(item_detail, last_index_of_list)
            item_quantity = item_detail[0]
            item_price = item_detail[last_index_of_list]

            item_detail_object['item_name'] = item_name
            item_detail_object['item_quantity'] = item_quantity
            item_detail_object['item_price'] = item_price
            final_object = self.__check_tax_constraints(item_detail_object, item_detail)
            cart_details.append(final_object)

        return cart_details

    @staticmethod
    def __get_item_name(item_list, last_index_of_list):
        """
        Gets item name from item list by deleting all the un-wanted details and joins the list.
        """
        new_item_list = item_list.copy()
        index_of_at = new_item_list.index('at')
        new_item_list.pop(last_index_of_list)
        new_item_list.pop(index_of_at)
        new_item_list.pop(0)
        item_name = ' '.join(new_item_list)
        return item_name

    @staticmethod
    def __check_tax_constraints(item_detail_object, item_detail):
        """
        Based on the item it modifies flag for calculating taxes if item name exists in tax exempt list then
        is_basic_tax is False and if the item contains imported then imported flag will be enabled.
        """
        is_basic_tax = True
        is_imported = False
        item_name = item_detail_object['item_name']

        if item_name in BASIC_TAX_EXEMPT:
            is_basic_tax = False

        if 'imported' in item_detail:
            is_imported = True

        item_detail_object['is_imported'] = is_imported
        item_detail_object['is_basic_tax'] = is_basic_tax

        return item_detail_object


# Prints order receipt based on items in the cart
def print_receipt(order_list):
    """
    :param order_list: Input param must be list
    :return:
    """
    if len(order_list) == 0:
        print("No items in cart")
    else:
        shopping_cart = ShoppingCart(order_list)
        cart_details = shopping_cart.finalize_cart()
        cart_after_tax = CalculateTax().calculate_total_tax(cart_details)
        total_sales_tax = []
        total_price = []
        print('-------------- AISLE ---------------')
        for item in cart_after_tax:
            total_sales_tax.append(item['total_tax'])
            total_price.append(item['item_price'])
            print(f"{item['item_quantity']} {item['item_name']}: {'{:.2f}'.format(item['item_price'])}")

        print(f'Sales Taxes: {"{:.2f}".format(sum(total_sales_tax))}')
        print(f'Total: {sum(total_price)}')
        print('------------ Thank You! ------------')


print_receipt(order_one)
