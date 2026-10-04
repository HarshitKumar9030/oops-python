# class User:
#     user_count = 0

#     def __init__(self, username, email):
#           self.username = username
#           self.email = email
#           User.user_count += 1


#     def display_user(self):
#          print(f"Username: {self.username}, Email: {self.email}")


# user1 = User('harshit', 'harsht@hasdfh.com')
# user2 = User('aarav', 'aarav@hasdfh.com')


# print(User.user_count)


# Static Methods

class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}'s new balance is {self._balance}")
            self.__log_transaction("deposit", amount )

        else:
            print("Deposit amount must be positive")

    @staticmethod
    def is_valid_interest_rate(rate):
        return  0<= rate <= 5

    
    def _is_valid_amount(self, amount):
        return amount > 0

    def __log_transaction(self, transaction_type, amount):
        print(f"Logging {transaction_type} of ${amount}. New Balance: ${self._balance}")


account = BankAccount("Alice", 500)

account.deposit(200)
 