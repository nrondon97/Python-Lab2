#File Name: sales_price_NayleneRondon.py
#Lab 2_5
#Purpose: Determine price after a 20% discount
#Author: Naylene Rondon
#Date:1/18/2017

#start

#input
price = input("What is the price? ")
print("The price is: " + price)

#process
twenty = float(price) *.20
discount = float(price) - (twenty)

#output
print("The discount is: ", twenty)
print("Final price is: " + str(discount)) #Testing Concatenating

#end
