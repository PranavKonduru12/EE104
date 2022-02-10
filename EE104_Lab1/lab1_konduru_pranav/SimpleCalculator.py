# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 19:03:47 2020

Reference: https://www.geeksforgeeks.org/python-simple-calculator-using-tkinter/?ref=rp
"""


# importing Tkinter and math 
# from sqlite3 import Row
from multiprocessing.sharedctypes import Value
from tkinter import *
import math
# from tkinter.font import _FontDescription, Font 

# calc class 
class calc: 

	def getandreplace(self): 

		"""replace x with * and ÷ with /"""
		self.expression = self.e.get() 
		self.newtext=self.expression.replace('/','/') 
		self.newtext=self.newtext.replace('x','*') 


	def equals(self): 
		"""when the equal button is pressed"""
		self.getandreplace() 
		try: 
			# evaluate the expression using the eval function 
			self.value= eval(self.newtext) 
		except SyntaxError or NameError: 
			self.e.delete(0,END) 
			self.e.insert(0,'Invalid Input!') 
		else: 
			self.e.delete(0,END) 
			self.e.insert(0,self.value) 

	def squareroot(self): 
		"""squareroot method"""
		self.getandreplace() 
		try: 
			# evaluate the expression using the eval function 
			self.value= eval(self.newtext) 
		except SyntaxError or NameError: 
			self.e.delete(0,END) 
			self.e.insert(0,'Invalid Input!') 
		else: 
			self.sqrtval=math.sqrt(self.value) 
			self.e.delete(0,END) 
			self.e.insert(0,self.sqrtval) 
	
	def square(self): 
		"""square method"""
		self.getandreplace() 
		try: 
			#evaluate the expression using the eval function 
			self.value= eval(self.newtext) 
		except SyntaxError or NameError: 
			self.e.delete(0,END) 
			self.e.insert(0,'Invalid Input!') 
		else: 
			self.sqval=math.pow(self.value,2) 
			self.e.delete(0,END) 
			self.e.insert(0,self.sqval) 

	# Changes
	def cube(self): 
		"""cube method"""
		self.getandreplace() 
		try: 
			#evaluate the expression using the eval function 
			self.value= eval(self.newtext) 
		except SyntaxError or NameError: 
			self.e.delete(0,END) 
			self.e.insert(0,'Invalid Input!') 
		else: 
			self.cqval=math.pow(self.value,3) 
			self.e.delete(0,END) 
			self.e.insert(0,self.cqval)

	def cosine(self): 
		"""cosinen method"""
		self.getandreplace() 
		try: 
			#evaluate the expression using the eval function 
			self.value= eval(self.newtext) 
		except SyntaxError or NameError: 
			self.e.delete(0,END) 
			self.e.insert(0,'Invalid Input!') 
		else: 
			self.degrees = math.radians(self.value) # Converts degrees to radians as cos() only accepts radians
			self.cosval=math.cos(self.degrees)
			self.e.delete(0,END) 
			self.e.insert(0,self.cosval)
	

	def sine(self): 
		"""sine method"""
		self.getandreplace() 
		try: 
			#evaluate the expression using the eval function 
			self.value= eval(self.newtext) 
		except SyntaxError or NameError: 
			self.e.delete(0,END) 
			self.e.insert(0,'Invalid Input!') 
		else: 
			self.degrees = math.radians(self.value) 
			self.sinval=math.sin(self.degrees)
			self.e.delete(0,END) 
			self.e.insert(0,self.sinval)
	
	def clearall(self): 
			"""when clear button is pressed,clears the text input area"""
			self.e.delete(0,END) 

	def clear1(self): 
			self.txt=self.e.get()[:-1] 
			self.e.delete(0,END) 
			self.e.insert(0,self.txt) 

	def action(self,argi): 
			"""pressed button's value is inserted into the end of the text area"""
			self.e.insert(END,argi) 

	def __init__(self,master): 
			"""Constructor method"""
			master.title('Calulator') 
			master.geometry() 
			self.e = Entry(master) 
			self.e.grid(row=0,column=0,columnspan=6,pady=3) 
			self.e.focus_set() #Sets focus on the input text area 

			# Generating Buttons 
			Button(master,text="=",width=23,height=3,fg="black", 
				bg="white",command=lambda:self.equals()).grid( 
									row=4, column=4,columnspan=3) 

			Button(master,text='AC',width=5,height=3, 
						fg="black", bg="white", 
			command=lambda:self.clearall()).grid(row=1, column=5) 


			Button(master,text='C',width=5,height=3, 
				fg="black",bg="white", 
				command=lambda:self.clear1()).grid(row=1, column=6) 

			Button(master,text="+",width=5,height=3, 
				fg="black",bg="white", 
				command=lambda:self.action('+')).grid(row=4, column=3) 

			Button(master,text="x",width=5,height=3, 
					fg="black",bg="white", 
					command=lambda:self.action('x')).grid(row=2, column=3) 

			Button(master,text="-",width=5,height=3, 
					fg="black",bg="white", 
					command=lambda:self.action('-')).grid(row=3, column=3) 

			Button(master,text="÷",width=5,height=3, 
				fg="black",bg="white", 
				command=lambda:self.action('/')).grid(row=1, column=3) 

			Button(master,text="%",width=5,height=3, 
				fg="black",bg="white", 
				command=lambda:self.action('%')).grid(row=4, column=2) 

			Button(master,text="7",width=5,height=3, 
				fg="black",bg="white", 
				command=lambda:self.action('7')).grid(row=1, column=0) 

			Button(master,text="8",width=5,height=3, 
				fg="black",bg="white", 
				command=lambda:self.action(8)).grid(row=1, column=1) 

			Button(master,text="9",width=5,height=3, 
				fg="black",bg="white", 
				command=lambda:self.action(9)).grid(row=1, column=2) 

			Button(master,text="4",width=5,height=3, 
				fg="black",bg="white", 
				command=lambda:self.action(4)).grid(row=2, column=0) 

			Button(master,text="5",width=5,height=3, 
				fg="black",bg="white", 
				command=lambda:self.action(5)).grid(row=2, column=1) 

			Button(master,text="6",width=5,height=3, 
				fg="black",bg="white", 
				command=lambda:self.action(6)).grid(row=2, column=2) 

			Button(master,text="1",width=5,height=3, 
				fg="black",bg="white", 
				command=lambda:self.action(1)).grid(row=3, column=0) 

			Button(master,text="2",width=5,height=3, 
				fg="black",bg="white", 
				command=lambda:self.action(2)).grid(row=3, column=1) 

			Button(master,text="3",width=5,height=3, 
				fg="black",bg="white", 
				command=lambda:self.action(3)).grid(row=3, column=2) 

			Button(master,text="0",width=5,height=3, 
				fg="black",bg="white", 
				command=lambda:self.action(0)).grid(row=4, column=0) 

			Button(master,text=".",width=5,height=3, 
				fg="black",bg="white", 
				command=lambda:self.action('.')).grid(row=4, column=1) 

			Button(master,text="(",width=5,height=3, 
				fg="black",bg="white", 
				command=lambda:self.action('(')).grid(row=2, column=4) 

			Button(master,text=")",width=5,height=3, 
				fg="black",bg="white", 
				command=lambda:self.action(')')).grid(row=2, column=5) 

			Button(master,text="?",width=5,height=3, 
				fg="black",bg="white", 
				command=lambda:self.squareroot()).grid(row=1, column=4) 

			Button(master,text="x²",width=5,height=3, 
				fg="black",bg="white", 
				command=lambda:self.square()).grid(row=3, column=5) 
			Button(master, text="x³", width=5,height=3,			# Cube button
				fg="black",bg="white",
				command=lambda:self.cube()).grid(row=3,column=4)
			Button(master, text="cos()", width=5,height=3,
				fg="black",bg="white",
				command=lambda:self.cosine()).grid(row=2,column=6)
			Button(master, text="sin()", width=5,height=3,
				fg="black",bg="white",
				command=lambda:self.sine()).grid(row=3,column=6)
			
			

# Driver Code 
root = Tk() 

obj=calc(root) # object instantiated 

root.mainloop() 
