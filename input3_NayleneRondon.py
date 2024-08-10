#File Name: input3_NayleneRondon.py
#Lab 2_4
#Purpose:Request user's name, age, and income. Will print age as integer and
#Income as float.
#Author: Naylene Rondon
#Date:1/18/2017

#start

#Welcome
print("Welcome")

#Input
name = input("What is your name? ") #name
age = input("what is your age? ") #age
income = input("What is your income? ") #income

#Process
newAge = int(age) 
newIncome = float(income)  
    

#Output

print("Your name is ", name, ". Your age is ", newAge, ". Your income is ", newIncome)

#Original Above | Modified Below for aesthetic purposes using concatentating

# print("Your name is " + name + ". Your age is " + str(newAge)+ ". Your income is $" + str(newIncome)+ ".")

#end
