from tkinter import Menu
from typing_extensions import Self


class Atm:
    def __init__(self):
        self.__pin=""
        self.__balance=0
        self.menu()
        print(id(self))
    def menu(self): #self is the object of this class
        input_choice=input("""PLEASE ENTER YOUR CHOICE
        -> PRESS 1 TO SET YOUR PIN
        -> PRESS 2 TO CHECK YOUR BALANCE AMOUNT
        -> PRESS 3 TO DEPOSIT MONEY
        -> PRESS 4 CASH WITHDRAWL
        -> PRESS 5 TO CHANGE PIN
        -> PRESS 6 TO PRINT INVOICE
        -> PRESS 0 TO EXIT\n""")
        

        if input_choice=="1":
            self.set_pin()
            
        elif input_choice=="2":
            self.balance_amount()
        elif input_choice=="3":
            self.deposit_money()
        elif input_choice=="4":
            self.cashwithdrawl()
        elif input_choice=="5":
            self.change_pin()
        elif input_choice=="6":
            self.printinvoice()
        elif input_choice=="0":
            print("THANKS FOR USING OUR ATM, COMEBACK AGAIN!!")
        else:
            print("ENTER A VALID CHOICE")
            
    def deposit_money(self):
        temp=input("ENTER YOUR PIN ")
        if temp==self.__pin:
            temp=int(input("Enter the amount you want to deposit "))
            self.__balance=self.__balance + temp
            print("MONEY HAS BEEN SUCCESSFULLY DEPOSITED")
        else:
            print("ENTER A VALID PIN")
        self.menu()
    
    def set_pin(self):
        self.__pin=input("ENTER YOUR PIN ")
        print("PIN SET SUCCESSFULLY")
        self.menu()
    
    def balance_amount(self):
        temp=input("ENTER YOUR PIN : ")
        if temp==self.__pin:
            print("YOUR BALANCE AMOUNT IS : ",self.__balance)
        else:
            print("ENTER A VAlID PIN")
        self.menu()

    def cashwithdrawl(self):
        temp=input("ENTER YOUR PIN ")
        if temp==self.__pin:
            amount=int(input("ENTER AMOUNT "))
            if amount<=self.__balance:
                self.__balance=self.__balance-amount
                print("TASK SUCCESSFUL")
            else:
                print("INSUFFICIENT BALANCE MONEY")
        self.menu()
    def change_pin(self):
        tempnewpin=input("ENTER YOUR PIN")
        if tempnewpin==self.__pin:
            newpin=self.__pin
            print("YOUR PIN HAS BEEN CHANGED SUCCESSFULLY")
        else:
            print("ENTER A VALID PIN")
        self.menu()
    def printinvoice(self):
        temp=input("ENTER YOUR PIN ")
        if temp==self.__pin:
            print("YOUR CUSTOMER ID IS : ",id(self),"\n","CURRENT AMOUNT IS :",self.__balance)
        else:
            print("ENTER VALID PIN")
        self.menu()


atm2=Atm()
print(atm2.menu())

