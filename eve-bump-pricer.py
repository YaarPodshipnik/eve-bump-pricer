import pyperclip
from math import log10, floor
from time import sleep

""" 
A tiny, simple, script to monitor cliboard for EVE online orders,
calculate new price accodring to March 2020 tick rules, and 
put it back to clipboard.
Helps dealing with updating multiple orders (no EULA-breaking
automation).
"""

len_buy = 7
len_sell = 5
frequency_Hz = 4

def get_order():
    content = pyperclip.paste()
    content = content.split("\t")
    c_len = len(content)
    if (c_len == len_buy or c_len == len_sell) and content[2].endswith(" ISK"):
        content_type = "BUY" if c_len == len_buy else "SELL"
        return content, content_type
    else:
        return None, None

def bump_price(price, direction = 1):
    if price < 0:
        raise ValueError("price can't be negative")
    if direction not in [1, -1]:
        raise ValueError(
            "direction must be either 1 (increase price) or -1 (decrease price)")
    most_significant = float(str(price)[:4])
    mag_most_significant = floor(log10(most_significant))
    mag_input = floor(log10(abs(price)))
    mag_bump = -2 if mag_input < 3 else (mag_input - mag_most_significant)
    bump  = 10 ** mag_bump 
    bumped = price + (direction * bump)
    if mag_input < 3:
        return bumped
    else:
        mag_round = mag_most_significant - mag_input
        return round(bumped, mag_round)
    
def get_updated_price(order, order_type):
    current_price = float(order[2].replace(" ISK", "").replace(",", ""))
    direction = +1 if order_type == "BUY" else -1
    new_price = bump_price(current_price, direction)
    new_price = f"{new_price:.2f}"
    print(f"{order_type} order, old price {current_price}, new price {new_price}")
    return new_price

def put_price(new_price):
    pyperclip.copy(new_price)
    print(f"Put {new_price} in clipboard")

print("This is EVE Online Pricing Helper!")
while (True):
    sleep(1/frequency_Hz)
    order, order_type = get_order()
    if order:
        price = get_updated_price(order, order_type)
        put_price(price)

