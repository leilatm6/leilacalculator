from tkinter import *
import math
class Graphic():
    def __init__(self):
        self.operand = '='
        self.number = 0
        self.number1 = 0
        self.float = 0
        self.equalres = False
        self.root = Tk()
        self.root.title("Leila Calculator")
        self.e = Entry(self.root, width=50)
        self.e.grid(row=0, column=0, columnspan=4)
        self.entrynum(self.number)

        button1 = Button(self.root, text="1", padx=40, pady=10,command=lambda: self.click(1))
        button1.grid(row=3, column=0)
        button2 = Button(self.root, text="2", padx=40, pady=10,command=lambda: self.click(2))
        button2.grid(row=3, column=1)
        button3 = Button(self.root, text="3", padx=40, pady=10,command=lambda: self.click(3))
        button3.grid(row=3, column=2)

        button4 = Button(self.root, text="4", padx=40, pady=10,command=lambda: self.click(4))
        button4.grid(row=2, column=0)
        button5 = Button(self.root, text="5", padx=40, pady=10,command=lambda: self.click(5))
        button5.grid(row=2, column=1)
        button6 = Button(self.root, text="6", padx=40, pady=10,command=lambda: self.click(6))
        button6.grid(row=2, column=2)

        button7 = Button(self.root, text="7", padx=40, pady=10,command=lambda: self.click(7))
        button7.grid(row=1, column=0)
        button8 = Button(self.root, text="8", padx=40, pady=10,command=lambda: self.click(8))
        button8.grid(row=1, column=1)
        button9 = Button(self.root, text="9", padx=40, pady=10,command=lambda: self.click(9))
        button9.grid(row=1, column=2)

        buttonpn = Button(self.root, text="±", padx=39, pady=10, command=lambda: self.operationclick("+/-"))
        buttonpn.grid(row=4, column=0)
        button0 = Button(self.root, text="0", padx=40, pady=10,command=lambda: self.click(0))
        button0.grid(row=4, column=1)
        buttondot = Button(self.root, text=".", padx=41, pady=10, command=lambda: self.operationclick("."))
        buttondot.grid(row=4, column=2)

        buttonmultiply = Button(self.root, text="x", padx=22, pady=10, command=lambda: self.operationclick("*"))
        buttonmultiply.grid(row=1, column=4)
        buttonminus = Button(self.root, text="-", padx=22, pady=10, command=lambda: self.operationclick("-"))
        buttonminus.grid(row=2, column=4)
        buttonplus = Button(self.root, text="+", padx=21, pady=10, command=lambda: self.operationclick("+"))
        buttonplus.grid(row=3, column=4)
        buttondevide = Button(self.root, text="/", padx=22, pady=10, command=lambda: self.operationclick("/"))
        buttondevide.grid(row=4, column=4)
        buttonequal = Button(self.root, text="=", padx=21, pady=10, command=self.equal)
        buttonequal.grid(row=5, column=4, rowspan=2)

        buttonclear = Button(self.root, text="x²", padx=39, pady=10, command=lambda: self.operationclick("**"))
        buttonclear.grid(row=5, column=0)
        buttonclear = Button(self.root, text="√x", padx=39, pady=10, command=lambda: self.operationclick("sqrt"))
        buttonclear.grid(row=5, column=1)
        buttonclear = Button(self.root, text="Clear", padx=30, pady=10, command=lambda: self.operationclick("clear"))
        buttonclear.grid(row=5, column=2)

        self.root.mainloop()

    def click(self, num):
        if self.equalres:
            self.number = 0
            self.entry("clear")
        if self.float:
            self.number = self.number + num / (10 ** self.float)
            self.number = round(self.number,self.float)
            self.float += 1
        else:
            self.number = self.number * 10 + num
        self.entrynum(self.number)

    def operationclick(self,operation):
        if operation == "+/-":
            self.number = -self.number
        elif operation == ".":
            self.float = 1
        elif operation == "clear":
            self.entry('clear')
        elif operation == "**":
            self.operand = '**'
            self.equal()
        elif operation == "sqrt":
            self.operand = 'sqrt'
            self.equal()
        elif operation == "+":
            self.number1 = self.number
            self.number = 0
            self.operand = '+'
            self.entry('clear')
        elif operation == "-":
            self.number1 = self.number
            self.number = 0
            self.operand = '-'
            self.entry('clear')
        elif operation == "*":
            self.number1 = self.number
            self.number = 0
            self.operand = '*'
            self.entry('clear')
        elif operation == "/":
            self.number1 = self.number
            self.number = 0
            self.operand = '/'
            self.entry('clear')

        self.entrynum(self.number)

    def equal(self):
        if self.operand == '+':
            self.number += self.number1
        elif self.operand == '-':
            self.number = self.number1 - self.number
        elif self.operand == '*':
            self.number *= self.number1
        elif self.operand == '/':
            self.number = self.number1 / self.number
        elif self.operand == '**':
            self.number = self.number ** 2
        elif self.operand == 'sqrt':
            self.number = self.number ** 0.5
        self.operand = '='
        self.entry("clear")
        self.entrynum(self.number)
        self.equalres = True

    def entrynum(self, num):
        self.e.delete(0, END)
        if num == 0 and self.operand != '=':
            return
        s = str(num)
        self.e.insert(0, s)
        if self.float and '.' not in s:
            self.e.insert(len(s), '.')



    def entry(self, operand):
        s = self.e.get()
        if operand == "clear":
            s = ""
            self.float = 0
            self.equalres = False
        elif operand == "neg":
            if not s:
                return
            if s[0] == '-':
                s = s[1:]
            else:
                s = '-' + s
        self.e.delete(0, END)
        self.e.insert(0, s)










