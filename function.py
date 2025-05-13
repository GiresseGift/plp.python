# def calculate_disconut

from datetime import datetime
print("my current time :")
print(datetime.now())

def greet(name: str) -> None:
    """My name Giresse."""
    return F"Hello, {name}!"

print(greet("Giresse"))

orignal_price = 1500
discount_percent = 20
discount_amount = 1500 * (20/100)
discounted_price = 1500 - 300


def calculate_discount(orignal_price, discount_percent):
    orignal_price * discount_percent/100
    discount_amount - orignal_price
    return discounted_price

print(f"orignal_price:{orignal_price}")      
print(f"discount_amount:{discount_amount}")      
print(f"discounted_price:{discounted_price}")

calculate_discount(orignal_price, discount_percent)
      
     



