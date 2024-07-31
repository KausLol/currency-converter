# simple program that converts amount from one currency to another, based on user inputs
import time
import requests

# https://app.exchangerate-api.com/dashboard
API_Key = "1a0ac6783f1b125020472bb7"


# main code
def main():
    print("\nWelcome to exchange rate calculator!\n")
    time.sleep(1)

    print(
        "This program allows you to convert convert amounts between a wide range "
        "of global currencies \nusing real-time exchange rates."
    )
    time.sleep(1.5)

    print(
        "Go to this URL to get details about all the valid currency codes: "
        "https://taxsummaries.pwc.com/glossary/currency-codes\n"
    )
    time.sleep(1.5)

    # asks users for inputs, returns exceptions if invalid format
    while True:
        try:
            src_currency = input(
                "Kindly enter the code of the currency you currently have and "
                "press enter. (Eg. USD, INR, EUR): "
            )

            target_currency = input(
                "\nKindly enter the code of the currency you want to convert to and "
                "press enter. (Eg. USD, INR, EUR): "
            )

            amount = float(
                input(
                    "\nKindly enter the amount of money you want to convert (Integer value only. "
                    "You may or may not add decimals): "
                )
            )

            print("\nPlease wait...")

            # fetches json data from the endpoint
            rate = fetch_data(src_currency, target_currency)

            # converts the amount into target currency
            final_amount = amount_convert(rate, amount)

            print(
                f"\nYour amount in {target_currency} is as follows: \n"
                f"{target_currency} {final_amount:,.2f}"
            )

            input("\nPress any key to exit...")
            exit()

        except KeyError:
            print(
                "\nPlease make sure you have entered the valid currency codes.\nRe-running the code... \n"
            )

        except ValueError:
            print(
                "\nKindly enter the amount in integer format.\nRe-running the code... \n"
            )


# gets data from the API endpoint
def fetch_data(input_currency_src, input_currency_target):
    currency_data = requests.get(
        f"https://v6.exchangerate-api.com/v6/{API_Key}/latest/{input_currency_src}"
    )
    final_currency_data = currency_data.json()

    exchange_rate = float(
        final_currency_data["conversion_rates"][f"{input_currency_target}"]
    )

    return exchange_rate


# converts amount into the target currency
def amount_convert(exchange_rate, user_amount):
    final_amount = round(user_amount * exchange_rate, 2)

    return final_amount


# runs the code
if __name__ == "__main__":
    main()
