wind_angl = float(input('Введите градус ветра: '))

if wind_angl > 360:
    wa = wind_angl % 360

def wind():
    if wa == 0:
        return print("N")
    elif wa == 90:
        return print("E")
    elif wa == 180:
        return print("S")
    elif wa == 270:
        return print("W")
    elif 0 <= wa < 90:
        return print("NE")
    elif 90 < wa < 180:
        return print("ES")
    elif 180 < wa < 270:
        return print("WS")
    elif 270 < wa < 360:
        return print("WN")

wind()