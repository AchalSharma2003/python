"""
Write a function called discount_price that takes original_price 
and discount_percent as parameters and prints the final 
price after discount.
"""


def discount_price(original_price,discount_percent):
    discount_amount = original_price*(discount_percent/100)
    print(f"final price is {original_price - discount_amount}")

discount_price(200,50)