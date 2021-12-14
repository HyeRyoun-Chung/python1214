# Function2.py


#불변형과 가변형식
a = 1.2
print(id(a))
a = 2.3
print(id(a))

print('---가변형식---')
list = [1,2,3]
print(id(list))
list.append(list)
print(id(list))

#LGB 이름 규칙 - 지역/전역/built-in 순서로 변수 참조

# 전역변수
x = 2
def func1(a):
    return a+x

print(func1(1))

#지역변수 
def func2(a):
    x = 5
    return a+x

print(func2(1))

# 기본값이 있는 경우

def times(a = 10, b = 20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

print(connectURI("credu.com", "80"))
print(connectURI(port = "80", server="test.com"))

#가변인자 (입력되는 인자의 갯수가 다양한 경우)
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union("HAM", "SPAM"))
print(union("HAM", "SPAM", "EGG"))


# *과 ** 차이는?
# *는 가변만 있는 경우 즉, 필수인 arg가 없는 경우
# **는 필수 + 옵션인 경우, 필수 arg는 앞쪽에 쓰고 옵션인 arg를 **로 묶어서 뒤쪽에 쓴다

def userURIBuilder (server, port, **user):
    str = "http://" + server + "." + port + "/?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str

print(userURIBuilder("test.com", "8080", id = "kim", passwd = "1234"))
print(userURIBuilder("test.com", "8080", id = "kim", passwd = "1234", name = "mike"))


#람다함수(이름이 없는 간결한 함수 정의)
g = lambda x,y:x*y
print( g(3,4) )
print( g(5,6))
print ((lambda x:x*x)(3))
print(globals())