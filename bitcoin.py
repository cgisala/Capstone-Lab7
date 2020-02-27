import requests
from pprint import pprint

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
coin_data = requests.get(url).json()

def main():
    # Prompt user to input how many bitcoins to convert to USD
    rate = get_bitcoin_rate(coin_data)
    bitcoin = user_input()

    usDollars = round(get_dollars(bitcoin, rate),2)


    print('\n***Results***')
    print(f'\n{bitcoin} bitcoin is equals to $ {usDollars}\n')

def get_bitcoin_rate(data):
    return data['bpi']['USD']['rate_float']

def get_dollars(bitcoin, rate):
    return bitcoin * rate

def user_input():
    while True:
        try:
            bitcoin = float(input('\nHow many bitcoin do you want to convert to USD? '))
            return bitcoin
        except:
            print('\n*** Error: please enter a decimal value ***')

if __name__ == '__main__':
    main()