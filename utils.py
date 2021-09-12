"""
    This file contains all the basic utility functions that can be used across
"""


# calculate tax based on tax percent and price
def calculate_tax(tax, item_price):
    return round((tax / 100) * float(item_price), 2)
