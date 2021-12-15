# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):

        #멤버변수 숨기기 - 변수 앞에 __붙이기
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)

# #개발자 실수 - 변수가 외부에서 보임
# account1.balance = 15000000

print(account1)

# #외부에서 접근불가
# print(account1.__balance)

#백도어 존재, private 변수를 접근할 수 있는 방법이 존재
print(account1._BankAccount__balance)