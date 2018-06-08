#Celsius to Fahrenheit converter using F= C 9/5 + 32 iteratively.

temperatures=[10,-20,-289,100]

def convert(celsius):
  if celsius >= -273.15:
      fahrenheit = celsius*(9/5) + 32
      print("%f C = %f F" %(celsius, fahrenheit))
  else:
      print("Physical matter can't be at %f C" %celsius)

for i in temperatures:
  convert(i)
