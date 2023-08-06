class Account:
    def __init__(self,balance=10000):
        self.balance = balance
        
    #入金    
    def deposit(self,amount):
        self.balance += amount
        print("現在の残高は",self.balance,"円です。")   
    
    #出金
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("現在の残高は",self.balance,"円です。")   
            return True
        else:
            print("残高が不足しています。")
            return False
        
#動作部分
account = Account()
print("本日はどのようなご要件でしょうか。残高は",account.balance,"円です。")
res = int(input("入金=>1,出金=>2を押してください。"))



if res == 1:
    amo = int(input("いくら入金しますか。"))
    account.deposit(amo)
  
elif res == 2:
    amo =  int(input("いくら出金しますか。"))
    account.withdraw(amo)
   
else:
    print("1か2を入力してください。")