
import math
"""A program that allows the user to use two different financial calculators for their calculation:-
An Investment Calculator and A Home Loan Repayment Calculator.
"""
#Pseudocode
"""
start
show menu option to user - investment or bond calculator
if user choose investment calculator 
ask user to choose compound or simple interest type
ask user to input amount, interest rate and no of years
calculate simple or compound interest
output the calculated simple or compound interest
if user choose bond calculator
ask user to input present value of house, interest rate and no. of months
output the calculated  amount to repay each month 
error out for invalid option
stop
"""

#create a menu option for user to choose
print("-"*85)
print("\ninvestment - to calculate the amount of interest you will earn on your investment"
+ "\nbond       - to calculate the amount you will have to pay on a home loan\n"
+ "\nEnter either \'investment'  or \'bond' from the menu above to proceed : ")
print("-"*85)

pref_investment = input("\nEnter your option : ")
     
#investment calculator
#check the user input ignoring case
if pref_investment.lower() == 'investment':
        print("-"*50)
        deposit_amount = float(input("\nEnter the amount to deposit: "))
        rate_of_interest = float(input("\nEnter the rate of interest: "))
        no_of_year = float(input("\nEnter the number of years: "))
        interest_type = input("\nEnter Compound or Simple: ")

        #calculation for simple interest
          
        if interest_type.lower() == "Simple".lower():   
            total_amount = deposit_amount * (1 + rate_of_interest/100 * no_of_year)
            print(f"\nSimple Interest: " ,total_amount)
            print("-"*50)

        #calculation for compound interest
    
        elif interest_type.lower() == "Compound".lower():
             total_amount = deposit_amount * math.pow((1 + rate_of_interest/100), no_of_year)
             print(f"\nCompound Interest: ", total_amount)
             print("-"*50)

        else:
             print("Invalid Interest type")

#bond calculator
 
elif pref_investment.lower() == 'bond':
         present_value = float(input("\nEnter the present value of house: "))
         rate_of_interest = float(input("\nEnter the rate of interest: "))
         no_of_months = float(input("\nEnter the number of months: "))

         total_repayment = (((rate_of_interest/100)/12) * present_value)/(1 -( 1 + (rate_of_interest/100)/12 ) ** (-no_of_months))
         print(f"\nMoney to repay each month : ",(total_repayment)) 
         print("-"*50)    


else:
    print("\nYou have entered an invalid option\n")
