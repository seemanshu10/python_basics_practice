def run_update_stock():

    product = {
        "name" : "camera",
        "price" : 1236,
        "stock" : 24
    }

    # Subtract 1 from stock using .get() with fallback 0
    product["stock"] =product.get("stock", 0) - 1
    
    print(product)

if __name__ == "__main__":
    run_update_stock()