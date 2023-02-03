
import csv


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dictionary = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list

    return dictionary

def main():
    INFORMATION_INDEX = 0
    products_dictionary = read_dictionary("products.csv", INFORMATION_INDEX)

    print()
    print(products_dictionary)
    print()

    with open("request.csv", "rt") as request_file:
        reader = csv.reader(request_file)
        next(reader)
        print("Requested Items")
        grand_total = 0
        
        for row_list in reader:
            # Request
            PRODUCT_NUMBER_INDEX = 0
            QUANTITY_INDEX = 1

            # Products
            NAME_INDEX = 1
            PRICE_INDEX = 2


            product_number = row_list[PRODUCT_NUMBER_INDEX]
            requested_quantity = int(row_list[QUANTITY_INDEX])

            product_name = products_dictionary[product_number][NAME_INDEX]
            product_price = float(products_dictionary[product_number][PRICE_INDEX])

            total_product_price = product_price * requested_quantity
            grand_total += total_product_price
            
            print(f"{product_name}: {requested_quantity} @ ${product_price:.2f} = ${total_product_price}")
        
        print()
        print(f"Total: ${grand_total:.2f}")
        print()




# Call main to start this program.
if __name__ == "__main__":
    main()