
# print()
# proceed = input("Input the quantity sold per product. Type a to continue, x to exit\n>>> ")

# tv_desc = "TV"
# vcr_desc = "VCR"
# rc_desc = "Remote Controller"
# cd_desc = "CD Player"
# tr_desc = "Tape Recorder"

# tv_price = 400.00
# vcr_price = 220.00
# rc_price = 35.20
# cd_price = 300.00
# tr_price = 150.00

# if proceed == "a":
#     tv_sold = float(input("TV: "))
#     vcr_sold = float(input("VCR: "))
#     rc_sold = float(input("Remote Controller:"))
#     cd_sold = float(input("CD Player: "))
#     tr_sold = float(input("Tape Recorder: "))

#     print("QTY\tDESCRIPTION\t\tUNIT PRICE\t\tTOTAL PRICE")
#     print("---\t-----------\t\t----------\t\t-----------")
#     print(int(tv_sold), "\t", tv_desc, "\t\t\t", "{:.2f}".format(tv_price), "\t\t", "{:.2f}".format(tv_price*tv_sold))
#     print(int(vcr_sold), "\t", vcr_desc, "\t\t\t", "{:.2f}".format(vcr_price), "\t\t", "{:.2f}".format(vcr_price*vcr_sold))
#     print(int(rc_sold), "\t", rc_desc, "\t", "{:.2f}".format(rc_price), "\t\t\t", "{:.2f}".format(rc_price*rc_sold))
#     print(int(cd_sold), "\t", cd_desc, "\t\t", "{:.2f}".format(cd_price), "\t\t", "{:.2f}".format(cd_price*cd_sold))
#     print(int(tr_sold), "\t", tr_desc, "\t\t", "{:.2f}".format(tr_price), "\t\t", "{:.2f}".format(tr_price*tr_sold))
#     tot_sold = tv_sold + vcr_sold + rc_sold + cd_sold + tr_sold
#     tot_price = tv_price + vcr_price + rc_price + cd_price + tr_price
#     sub_tot = float(tot_sold*tot_price)
#     sales_tax = float(sub_tot * 0.0825)
#     tot = float(sub_tot + sales_tax)
#     print("\n\t\t\t\tSUBTOTAL\t\t", "{:.2f}".format(sub_tot))
#     print("\t\t\t\tTAX\t\t\t", "{:.2f}".format(sales_tax))
#     print("\t\t\t\tTOTAL\t\t\t", "{:.2f}".format(tot))
#     print("\n")


# elif proceed == "x":
#     print("Thank you for using this program!\n")
#     exit()

# else:
#     print("Incorrect key pressed. Shutting down .....\n")
#     exit()


import locale

def calculate_total_sold(products_sold):
    return sum(products_sold.values())

def calculate_subtotal(products_sold, product_prices):
    return sum(products_sold[product] * product_prices[product] for product in products_sold)

def calculate_tax(subtotal, tax_rate):
    return subtotal * tax_rate

def display_receipt(products_sold, product_prices, subtotal, tax):
    locale.setlocale(locale.LC_ALL, '')  # Set the locale to the user's default
    peso_sign = '₱'  # Peso sign
    print("\nQTY\tDESCRIPTION\t\t\tUNIT PRICE\t\tTOTAL PRICE")
    print("---\t------------------\t\t----------\t\t-----------")
    for product, quantity in products_sold.items():
        total_price = quantity * product_prices[product]
        unit_price_str = locale.currency(product_prices[product], grouping=True, symbol=False)
        total_price_str = locale.currency(total_price, grouping=True, symbol=False)
        print(f"{quantity}\t{product:20}\t\t{peso_sign}{unit_price_str}\t\t\t{peso_sign}{total_price_str}")
    subtotal_str = locale.currency(subtotal, grouping=True, symbol=False)
    tax_str = locale.currency(tax, grouping=True, symbol=False)
    total = subtotal + tax
    total_str = locale.currency(total, grouping=True, symbol=False)
    print("-"*75)
    print("\t\t\t\t\tSUBTOTAL\t\t{peso_sign}{subtotal_str}".format(peso_sign=peso_sign, subtotal_str=subtotal_str))
    print("\t\t\t\t\tTAX\t\t\t{peso_sign}{tax_str}".format(peso_sign=peso_sign, tax_str=tax_str))
    print("\t\t\t\t\tTOTAL\t\t\t{peso_sign}{total_str}".format(peso_sign=peso_sign, total_str=total_str))



def main():
    products = {
        "TV": 400.00,
        "VCR": 220.00,
        "Remote Controller": 35.20,
        "CD Player": 300.00,
        "Tape Recorder": 150.00
    }

    products_sold = {}
    proceed = input("Input the quantity sold per product. Type 'a' to continue, 'x' to exit\n>>> ")
    while proceed != "x":
        if proceed == "a":
            for product, _ in products.items():
                quantity = input(f"{product}: ")
                try:
                    products_sold[product] = int(quantity)
                except ValueError:
                    print("Please enter a valid quantity.")
                    break

            subtotal = calculate_subtotal(products_sold, products)
            tax = calculate_tax(subtotal, 0.0825)
            display_receipt(products_sold, products, subtotal, tax)
            products_sold.clear()

        else:
            print("Incorrect key pressed. Shutting down...")
            break

        proceed = input("\nInput the quantity sold per product. Type 'a' to continue, 'x' to exit\n>>> ")

    print("Thank you for using this program!")

if __name__ == "__main__":
    main()
