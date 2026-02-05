import numpy as np

inventory = np.array([10, 0, 5, 0, 20, 0])

out_of_stock_indices = np.where(inventory == 0)
out_of_stock_products = inventory[out_of_stock_indices]

print("Out of Stock Products:", out_of_stock_products)


