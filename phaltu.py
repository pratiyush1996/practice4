def temp_celcius():
    tc = (5 / 9) * (tf - 32)
    return tc


def temp_farenhite():
    tf = (9 / 5) * (tc + 32)
    return tf


def windchill():
    win = (35.74 + (0.6215 * T) -(35.75 * (v ** 0.16) + ((0.4275 * T) * (v ** 0.16))))
    return win


print("""enter degree of temperature C/F or c/f
               to convert the temperature""")

choice = input("enter choice")
if choice == 'C' or choice == 'c':
    tf = int(input("enter the farenhite temp."))
    print(temp_celcius())
if choice == 'F' or choice == 'f':
    tc = int(input("enter the celcius temperature"))
    print(temp_farenhite())

print("Do you want to calculate wind chill,Y/N")

wc = input("")
if wc == 'Y':
    T = int(input("enter the temp. in farenhite"))
    v = int(input("enter the wind speed"))
    print(windchill())

