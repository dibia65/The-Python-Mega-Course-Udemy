#Celsius to Fahrenheit converter using F= C 9/5 + 32.

celsius = float(input("Celsius temperature: "))

if celsius >= -273.15:
    fahrenheit = celsius*(9/5) + 32
    print("Fahrenheit Temperature: %f" %(fahrenheit))
else:
    print("Physical matter can't be that cold..")
