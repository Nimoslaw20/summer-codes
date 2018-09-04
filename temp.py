##Temperature

##def Temperature():
##    temp = eval(input('Enter a temperature in Celsius: '))
##    print('In Fahrenheit, that is', 9/5*temp+32)


def Temp2():
    temp = eval(input('Enter a temperature in Celsius: '))
    f_temp = int(9/5*temp+32)
    print('In Fahrenheit, that is', f_temp)
    print('  \n')
    if  f_temp > 212:
          print('That temperature is above the boiling point.')
    if f_temp < 32:
          print('That temperature is below the freezing point.')


##Temperature()
Temp2()
