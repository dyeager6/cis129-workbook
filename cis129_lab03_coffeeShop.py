#Define prices for coffee and muffin
coffee_price = 5
muffin_price = 4

#Add tea and sandwich to menu and define prices for both
tea_price = 4
sandwich_price = 6

#Define tax rate
tax_rate = 0.06

#Prompt user to enter number of desired menu items to order
#Convert the user input to integers
coffee_order = int(input('How many cups of coffee would you like to order? '))
muffin_order = int(input('How many muffins would you like to order? '))
tea_order = int(input('How many cups of tea would you like to order? '))
sandwich_order = int(input('How many sandwiches would you like to order? '))

#Define function that multiplies price of coffee by number of cups of coffee ordered by the user
def calculate_coffee_total(coffee_price, coffee_order):
    coffee_total = coffee_price * coffee_order
    return coffee_total

#Assign variable to result as converted to an integer
coffee_total = calculate_coffee_total(coffee_price, coffee_order)

#Define function that multiplies price of muffin by number of muffins ordered by the user
def calculate_muffin_total(muffin_price, muffin_order):
    muffin_total = muffin_price * muffin_order
    return muffin_total

#Assign variable to result
muffin_total = calculate_muffin_total(muffin_price, muffin_order)

#Define function that multiplies price of tea by number of cups of tea ordered by the user
def calculate_tea_total(tea_price, tea_order):
    tea_total = tea_price * tea_order
    return tea_total

#Assign variable to result
tea_total = calculate_tea_total(tea_price, tea_order)

#Define function that multiplies price of sandwich by number of sandwiches ordered by the user
def calculate_sandwich_total(sandwich_price, sandwich_order):
    sandwich_total = sandwich_price * sandwich_order
    return sandwich_total

#Assign variable to result
sandwich_total = calculate_sandwich_total(sandwich_price, sandwich_order)

#Define function that finds total of menu items purchased before calculating tax
def calculate_subtotal(coffee_total, muffin_total, tea_total, sandwich_total):
    subtotal = coffee_total + muffin_total + tea_total + sandwich_total
    return subtotal

#Assign variable to result
subtotal = float(calculate_subtotal(coffee_total, muffin_total, tea_total, sandwich_total))

#Define function that returns calculated tax from subtotal
#Rounded to two decimal places
def calculate_tax(subtotal, tax_rate):
    tax = subtotal * tax_rate
    tax = round(tax, 2)
    return tax

#Assign variable to result
tax = calculate_tax(subtotal, tax_rate)

#Define function that returns total price after calculating tax
def calculate_total(subtotal, tax):
    total = subtotal + tax
    return total

#Assign variable to result
total = calculate_total(subtotal, tax)

#Display name of shop on receipt
#Add in new menu items

print('***************************************')
print('My Coffee and Muffin Shop')
print('Number of coffees bought?')
print(coffee_order)
print('Number of muffins bought?')
print(muffin_order)
print('Number of teas bought?')
print(tea_total)
print('Number of sandwiches bought?')
print(sandwich_total)
print('***************************************')

print('***************************************')
print('My Coffee and Muffin Shop Receipt')
print(coffee_order, 'Coffee at $5 each: $ ', coffee_total)
print(muffin_order, 'Muffin at $4 each: $ ', muffin_total)
print(tea_order, 'Tea at $4 each: $ ', tea_total)
print(sandwich_order, 'Sandwich at $6 each: $ ', sandwich_total)
print('6% tax: $ ', tax)
print('---------')
print('Total: $ ', total)
print('***************************************')

print('Thank you for your business and have a great day!')
