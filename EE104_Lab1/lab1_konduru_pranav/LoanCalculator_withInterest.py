# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 18:56:49 2020

Reference: https://www.geeksforgeeks.org/python-loan-calculator-using-tkinter/?ref=rp
"""
# Import tkinter 
from tkinter import *
class LoanCalculator: 

	def __init__(self): 

		window = Tk() # Create a window 
		window.title("Loan Calculator") # Set title 
		# create the input boxes. 
		Label(window, text = "Annual %Interest Rate").grid(row = 1, column = 1, sticky = W) 
		Label(window, text = "Number of Years").grid(row = 2, column = 1, sticky = W) 
		Label(window, text = "Loan Amount").grid(row = 3, column = 1, sticky = W)
		#Label(window, text = "Principal").grid(row = 3, column = 1, sticky = W)  
		Label(window, text = "Monthly Payment").grid(row = 4, column = 1, sticky = W) 
		Label(window, text = "Total Payment").grid(row = 5, column = 1, sticky = W) 
		Label(window, text = "Total Interest Paid").grid(row = 6, column = 1, sticky = W) 

		# for taking inputs 
		self.annualInterestRateVar = StringVar() 
		Entry(window, textvariable = self.annualInterestRateVar, justify = RIGHT).grid(row = 1, column = 2) # Boxes

		self.numberOfYearsVar = StringVar()	
		Entry(window, textvariable = self.numberOfYearsVar, justify = RIGHT).grid(row = 2, column = 2) 

		self.loanAmountVar = StringVar() 
		Entry(window, textvariable = self.loanAmountVar, justify = RIGHT).grid(row = 3, column = 2)

		self.monthlyPaymentVar = StringVar()
		Entry(window, textvariable = self.monthlyPaymentVar, justify = RIGHT).grid(row = 4, column = 2) 
		lblMonthlyPayment = Label(window, textvariable = self.monthlyPaymentVar).grid(row = 4, column = 2, sticky = E) 

		self.totalPaymentVar = StringVar() 
		Entry(window, textvariable = self.totalPaymentVar, justify = RIGHT).grid(row = 5, column = 2) 
		lblTotalPayment = Label(window, textvariable = self.totalPaymentVar).grid(row = 5, column = 2, sticky = E) 
		
		# For total interest 
		self.totalInteresttVar = StringVar()
		Entry(window, textvariable = self.totalInteresttVar, justify = RIGHT).grid(row = 6, column = 2)  
		lblTotalInterest = Label(window, textvariable = self.totalInteresttVar).grid(row = 6, column = 2, sticky = E)

		# create the button 
		btComputePayment = Button(window, text = "Compute Payment", command = self.computePayment).grid(row = 6, column = 3, sticky = E) 
		window.mainloop() # Create an event loop 


	# compute the total payment. 
	def computePayment(self):
		monthlyPayment = self.getMonthlyPayment( 
		float(self.loanAmountVar.get()), 
		float(self.annualInterestRateVar.get()) / 1200, # Interest is already divided by 12 here
		int(self.numberOfYearsVar.get())) 

		self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f')) 
		totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberOfYearsVar.get())

		totalInterest = float(totalPayment) - float(self.loanAmountVar.get()) # computing total interest (subtract principal/loan amount from total)
		
		self.totalPaymentVar.set(format(totalPayment, '10.2f')) # Total payment
		self.totalInteresttVar.set(format(totalInterest, '10.2f')) 
	
	# compute the monthly payment
	# Performs monthly payment operation using the formula 
	def getMonthlyPayment(self, loanAmountVar, monthlyInterestRate, numberOfYearsVar):
		numberOfPeriodsVar = numberOfYearsVar * 12 
		#monthlyPayment = loanAmount * monthlyInterestRate / (1
		#- 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        
        #Formula change
		monthlyPayment = loanAmountVar * (monthlyInterestRate * (1 
		+ monthlyInterestRate) ** numberOfPeriodsVar) / (((1 
		+ monthlyInterestRate) ** (numberOfPeriodsVar)) - 1)
                                                     
		return monthlyPayment; 
		root = Tk() # create the widget 

# call the class to run the program. 
LoanCalculator() 
