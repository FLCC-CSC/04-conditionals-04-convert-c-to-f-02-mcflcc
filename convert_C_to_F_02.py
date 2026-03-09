# FILE NAME - convert_C_to_F_02.py

# NAME: Mike Cintron
# DATE: 3.8.2026
# BRIEF DESCRIPTION:  Conversion, Celsius to Farenheit - Farenheit to Celsius, user decides which to convert



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print ('''===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius
      ''' )

selection = int(input("Please choose from the above menu: "))

if selection == 1:
    celcius = int(input("Enter a temperature to convert:  "))
    fahrenheit = (celcius * 9/5) + 32
    print(f"\n{celcius} degrees Celcius is {fahrenheit} degrees Fahrenheit.")

else:
    fahrenheit = int(input("Enter a temperature to convert: "))
    celcius = (fahrenheit - 32) * 5/9
    print(f"\n{fahrenheit} degrees Fahrenheit is {celcius} degrees Celsius.")













########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?







'''