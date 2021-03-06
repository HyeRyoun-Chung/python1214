#Function3.py

result = list(range(1,11))
print(result)

years = list(range(2000,2022))
print(years)

# -1 감소
numbers = list(range(10,0,-1))
print(numbers)

#리스트 컴프리헨션(함수로 반복, 필터링, 가공하기)
lst = list(range(1,11))
result = [i**2 for i in lst if i>5]
print(result)

#필터링하는 함수
#파스칼 표기법 : DemoCustomer 클리스명(형식이름)
#카멜 표기법 : gerBiggrtThan 변수명, 함수명, 메서드명
def getBiggerThan20(i):
    return i>20

lst = [10,25,30]
iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

print("--------람다함수----------")
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)