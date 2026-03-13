def is_armstrong_number(number):
    cyfra = [int(c) for c in str(number)]
    ilosc = len(str(number))
    suma = 0
    for i in range(0,ilosc):
        suma += cyfra[i] ** ilosc
    print(suma)
    if number < 0:
        raise ValueError("Wartość nie poprawna")
    elif suma == number:
        return True
    else:
        return False


print(is_armstrong_number(153))

#wiem ze da sie latwiej