def give_cookies(total, first_number, second_number):
    if first_number + second_number == total:
        apples = bin(first_number).count("1") + bin(second_number).count("1")
        print(f"{apples}")
    else:
        print(f"los numeros {first_number} + {second_number} sumados no son iguales a {total}")
