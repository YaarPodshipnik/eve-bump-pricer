import pyperclip
from time import sleep
""" 
A tiny, simple, script to monitor cliboard for EVE online orders,
calculate new +/-0.01 price, and put it back to clipboard.
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

def get_updated_price(order, order_type):
    current_price = float(order[2].replace(" ISK", "").replace(",", ""))
    adjustment = +0.01 if order_type == "BUY" else -0.01
    new_price = current_price + adjustment
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

