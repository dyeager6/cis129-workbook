{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "489e4a50-ce7d-4f7b-be43-df1cb8e5f794",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the monthly sales amount: $ 125000\n",
      "Enter percentage of sales increase: 4.5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The store bonus amount is $ 6000\n",
      "The employee bonus amount is $ 50\n"
     ]
    }
   ],
   "source": [
    "# Module 4 Lab-4\n",
    "# Dolan Yeager\n",
    "# 10/9/24\n",
    "# This program will calculate store bonus based on monthly sales and employee bonus based on sales increase\n",
    "\n",
    "# declare local variables\n",
    "monthlySales = 0  # monthly sales amount\n",
    "storeAmount = 0  # store bonus amount\n",
    "empAmount = 0  # employee bonus amount\n",
    "salesIncrease = 0  # percent of sales increase\n",
    "prompt = ('Enter the monthly sales amount: $') # prompt will be a string literal\n",
    "\n",
    "# This code gets the monthly sales\n",
    "monthlySales = float(input(prompt))\n",
    "\n",
    "# This code determines the storeAmount bonus\n",
    "if monthlySales >= 110000:\n",
    "    storeAmount = 6000\n",
    "elif monthlySales >= 100000:\n",
    "    storeAmount = 5000\n",
    "elif monthlySales >= 90000:\n",
    "    storeAmount = 4000\n",
    "elif monthlySales >= 80000:\n",
    "    storeAmount = 3000\n",
    "else:\n",
    "    storeAmount = 0\n",
    "\n",
    "# This code gets the percent of increase in sales\n",
    "salesIncrease = float(input('Enter percentage of sales increase:'))\n",
    "salesIncrease = salesIncrease / 100\n",
    "\n",
    "# This code determines the empAmount bonus\n",
    "if salesIncrease >= .05:\n",
    "\tempAmount = 75\n",
    "elif salesIncrease >= .04:\n",
    "\tempAmount = 50\n",
    "elif salesIncrease >= .03:\n",
    "\tempAmount = 40\n",
    "else:\n",
    "\tempAmount = 0\n",
    "        \n",
    "# This code prints the bonus information\n",
    "print('The store bonus amount is $', storeAmount)\n",
    "print('The employee bonus amount is $', empAmount)\n",
    "if (storeAmount == 6000 ) and (empAmount == 75):\n",
    "\tprint('Congrats! You have reached the highest bonus amounts possible! ')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fa3e12bd-9186-4fe0-b6c3-86bce9292f7f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
