""" Module to compute the total cost of all sales given a price catalogue and a sales record. """
import json
import sys
import time

def compute_sales(price_catalogue_file, sales_record_file):
    """ Compute the total cost of all sales given a price catalogue and a sales record. """
    # Load the price catalogue
    with open(price_catalogue_file, encoding='utf-8') as f:
        price_catalogue_json = json.load(f)

    # Load the sales record
    with open(sales_record_file, encoding='utf-8') as f:
        sales_record_json = json.load(f)

    # Compute the total cost for all sales
    total_cost = 0
    for sale in sales_record_json:
        product_id = sale['Product']
        quantity = sale['Quantity']
        for item in price_catalogue_json:
            if product_id == item['title']:
                total_cost += item['price'] * quantity

    # Print the total cost
    print(f"Total cost of all sales: ${total_cost}")

    # Write the results to the output file
    with open("SalesResults.txt", "w", encoding='utf-8') as f:
        f.write(f"Total cost of all sales: ${total_cost}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)

    start_time = time.time()

    price_catalogue = sys.argv[1]
    sales_record = sys.argv[2]

    compute_sales(price_catalogue, sales_record)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time} seconds")
