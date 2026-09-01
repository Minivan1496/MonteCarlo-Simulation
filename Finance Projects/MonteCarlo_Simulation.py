import numpy as np
import matplotlib.pyplot as plt
from Finance import (exp_returns, volatility)


def monte_carlo():

    while True:
        try:
            stock_price = float(input("Enter the current stock price: ")) # This refers to the current stock price

            expected_return_input = input(
                "Enter the expected return (type 'no' if unknown): "      # Expected return = sum of historical prices over n years/n
            ).strip().lower()

            if expected_return_input == "no":
                expected_return = exp_returns()
            else:
                expected_return = float(expected_return_input)

            volatility_input = float(input("Enter the volatility (type 'no' if unknown): ")) # Volatility is the standard deviation

            if volatility_input == "no":
                vola = volatility()
            else:
                vola = float(volatility_input)

            t = float(input("Enter the total time being simulated: "))  # Typically 1 year

            n = int(input("Enter the number of time steps:"))   #Typically 252

            break

        except ValueError:
            print("Please enter a numeric value or 'no'.")

    prices = [stock_price]

    for i in range(n):
        s = stock_price * np.exp((expected_return - 0.5 * vola**2)*(t/n) + vola * np.sqrt(t/n) * np.random.normal())

        prices.append(s)

    plt.plot(prices)
    plt.xlabel("Trading Days")
    plt.ylabel("Stock Price")
    plt.title("Simulated Stock Price")
    plt.show()

print(monte_carlo())




