def format_price(price):
    return f'Цена: {int(price)} руб.'


def main():
    result = format_price(56.24)
    print(result)


if __name__ == "__main__":
    main()