#takes input
temp = input('Enter the temperature in celcius: ')

#converts integer input based on celcius-fahrenheit conversion
tempF = round((float(temp) * (9/5)) + 32, 1)

#prints result
print(f'{temp} degree celcius is equal to {tempF} degree farhenheit')
