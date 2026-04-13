class Bank:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance
    def get_balance(self):
        print(self.__balance)

joy = Bank("Joy",1000)
joy.get_balance()