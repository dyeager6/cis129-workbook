#Define prices for coffee and muffin
coffee_price = 5
muffin_price = 4

#Define tax rate
tax_rate = 0.06

#Prompt user to enter number of desired menu items to order
#Convert the user input to integers
coffee_order = int(input('How many cups of coffee would you like to order? '))
muffin_order = int(input('How many muffins would you like to order? '))

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

#Define function that finds total of coffee and muffins purchased before calculating tax
def calculate_subtotal(coffee_total, muffin_total):
    subtotal = coffee_total + muffin_total
    return subtotal

#Assign variable to result
subtotal = float(calculate_subtotal(coffee_total, muffin_total))

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

print('***************************************')
print('My Coffee and Muffin Shop')
print('Number of coffees bought?')
print(coffee_order)
print('Number of muffins bought?')
print(muffin_order)
print('***************************************')

print('***************************************')
print('My Coffee and Muffin Shop Receipt')
print(coffee_order, 'Coffee at $5 each: $ ', coffee_total)
print(muffin_order, 'Muffin at $4 each: $ ', muffin_total)
print('6% tax: $ ', tax)
print('---------')
print('Total: $ ', total)
print('***************************************')
