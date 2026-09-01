import numpy as np

def exp_returns():
    while True:
        try:
            yearly_returns = list(map(float, input(
                f"Enter at least 4 of the last yearly returns as decimals separated by spaces: "
            ).split()))

            if len(yearly_returns) < 4:
                raise ValueError

            break

        except ValueError:
            print("**INVALID INPUT**")

    expected_return = np.mean(yearly_returns)

    print("Expected Return:", expected_return)

def volatility():
    while True:
        try:
            daily_prices = list(map(float, input(
                f"Enter 5 of the last daily closing prices separated by spaces: "
            ).split()))

            if len(daily_prices) != 5:
                raise ValueError

            break

        except ValueError:
            print("**INVALID INPUT**")

    annual_vol = np.std(daily_prices) * np.sqrt(252)
    print("Annual Volatility:", annual_vol)








