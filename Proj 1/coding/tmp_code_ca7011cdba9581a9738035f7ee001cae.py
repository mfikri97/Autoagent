import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

# Define your menu
menu = {
    "burger.png": 5.99,
    "pizza.png": 7.99,
    "salad.png": 4.99,
    "soda.png": 1.99
}

# Directory where menu images are stored
menu_dir = "./menu_images/" 

orders = []
total = 0.0

def get_image_similarity(imageA, imageB):
    s = ssim(imageA, imageB)
    return s

def what_is_the_order(order_image):
    max_ssim = 0
    max_ssim_item = None
    for item, price in menu.items():
        menu_item_image = cv2.imread(os.path.join(menu_dir, item))
        menu_item_image = cv2.cvtColor(menu_item_image, cv2.COLOR_BGR2GRAY)
        ssim_index = get_image_similarity(menu_item_image, order_image)
        if ssim_index > max_ssim:
            max_ssim = ssim_index
            max_ssim_item = item
    return max_ssim_item

def add_order(order_image_path):
    order_image = cv2.imread(order_image_path)
    order_image = cv2.cvtColor(order_image, cv2.COLOR_BGR2GRAY)
    ordered_item = what_is_the_order(order_image)
    orders.append(ordered_item)
    total += menu[ordered_item]

def print_order():
    for order in orders:
        print(f"Ordered: {order} \tPrice: ${menu[order]}")
    print(f"\nTotal: $ {round(total, 2)}")

# Order input (Replace with your order images paths)
orders_list = ["path_to_order1.png", "path_to_order2.png", "path_to_order3.png"]

for order in orders_list:
    add_order(order)

# Print the final order
print_order()