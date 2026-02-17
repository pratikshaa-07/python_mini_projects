#---------------------
#Bank acc project
#--------------------
from datetime import datetime
class bank:
        def __init__(self,acc_num,holder_name,balance=0):
                self.acc_num=acc_num
                self.holder_name=holder_name
                self.__balance=balance
                self.transaction_history=[]
                if balance>0:
                        self.__add_transaction("First deposit",balance)

        def __add_transaction(self,trans_type,balance):
                self.transaction_history.append({
                        "type":trans_type,
                        "amount":balance,
                        "time":datetime.now().strftime("%Y-%m-%d %H:%M:%s")
                        })

        def deposit(self,amt):
                if amt>=0:
                        self.__balance+=amt
                        print("After deposite amount =",self.__balance,"rs")
                        self.__add_transaction("Deposit",amt)
                else:
                        print("Deposit failed Invalid amount")

        def withdraw(self,amt):
                if amt<=0:
                        print("Withdrwal failed! Amount must be +ve and greater than zero")
                elif self.__balance>=amt:
                        self.__balance-=amt
                        print("Withdrawal Done")
                        print("Remaining amount =",self.__balance)
                        self.__add_transaction("withdraw",amt)
                else:
                        print("Withdrwal Failed! Balance Is Insufficiant")

        def get_balance(self):
                return self.__balance

        def transfer(self,amt,target_acc):
                if amt<=0:
                        print("Transfer failed! Amount must be +ve and greater than zero")
                elif self.__balance<amt:
                        print("Transfer failed! Insufficiant Balance")
                else:
                        self.__balance-=amt
                        target_acc.__balance+=amt
                        self.__add_transaction("Transfer out",amt)
                        target_acc.__add_transaction("Transfer in",amt)
                        print("Transfer Done")
                        print("Remaining amount :",self.__balance,"rs")
        def __str__(self):
                return(f"Acc Num : {self.acc_num}\n" f"Holder name:{self.holder_name}\n" f"Balance : {self.__balance}")

        def history(self):
                print(f"\nTransaction history for {self.holder_name}")
                for trans in self.transaction_history:
                        print(trans)
p1=bank(56789,"xyz")
p1.deposit(1000)
p1.withdraw(500)
p1.history()
p2=bank(76810,"abc",500)
p1.transfer(200,p2)
print("balance in p2",p2.get_balance())

