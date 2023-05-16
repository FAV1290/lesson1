def get_summ(one, two, delimiter='&'):
    return f'{one}{delimiter}{two}'


def main():
    print(get_summ('Learn', 'python').upper())


if __name__ == "__main__":
    main()