# my calculator gives you the total price you will spend on gas depending on how many gallons you need and the price of gas.#

print("Welcome! This calculator will help you find out the total amount you will pay for your desired amount of gas.")

gas_price = input("What is the current price of gas at your gas station: ")
gallons = input("How many gallons of gas would you like to fill your car with: ")

total_price = float(gas_price) * float(gallons)

print(f"The total price you will pay for {gallons} gallons of gas at ${gas_price} per gallon is ${round(total_price, 2)}")