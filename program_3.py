def calculate_total_purchase(subtotal=None):
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item,
    price_1 = float(input("Price of first item:"))
    price_2 = float(input("Price of second item:"))
    price_3 = float(input("Price of third item:"))
    price_4 = float(input("Price of fourth item:"))
    price_5 = float(input("Price of fifth item:"))

    # then displays the subtotal of the sale,
    presubtotal = price_1 + price_2 + price_3 + price_4 + price_5
    subtotal = round(presubtotal , 2)
    print("subtotal:" , subtotal)
    # the amount of sales tax, and the total.
    pretotal = (0.07 * subtotal) + subtotal
    total = round(pretotal , 2)
    print("total:" , total)
    # Assume the sales tax is 7 percent.

calculate_total_purchase()