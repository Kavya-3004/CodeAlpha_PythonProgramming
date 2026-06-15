def stock_tracker():

    print("Stock Portfolio Tracker")

    stock_prices = {
        "tcs": 3500,
        "infosys": 1500,
        "wipro": 300
    }

    stock_name = input("Enter stock name: ").lower()

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        total_value = stock_prices[stock_name] * quantity

        print("Stock:", stock_name.upper())
        print("Quantity:", quantity)
        print("Price per share:", stock_prices[stock_name])
        print("Total Value:", total_value)

        file = open("portfolio_report.txt", "w")

        file.write("Stock Portfolio Report\n")
        file.write("----------------------\n")
        file.write(f"Stock: {stock_name.upper()}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Price per share: {stock_prices[stock_name]}\n")
        file.write(f"Total Value: {total_value}\n")

        file.close()

        print("Report saved successfully!")

    else:
        print("Sorry! Stock not found.")


stock_tracker()