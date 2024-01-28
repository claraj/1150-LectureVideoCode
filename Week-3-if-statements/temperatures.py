# Temperature is a number and it can have a decimal place e.g. 22.4 so
# convert the data the user enters to a float and store in a float variable
temperature = float(input('Enter the current temperature in fahrenheit: '))

# decide if the temperature variable contains a number that is larger
# or smaller or equal to 32 (is it above or below or equal to freezing?)
if temperature > 32:
    print('It is above freezing')
elif temperature == 32:
    print('It is freezing')
else:
    print('It is below freezing')

# The program will pick one of these three options
