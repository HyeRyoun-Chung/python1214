# Fuction1.py

#함수 정의
def times(a,b):
    return a*b

print(times(3,4))

def setValue(newValue):
    x = newValue
    print(x)

result = setValue(5)
print(result)

def intersect(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

print(intersect("HAM", "SPAM"))