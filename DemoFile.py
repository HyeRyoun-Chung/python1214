# DemoFile.py

# #문자열 결합 연산
# url = "http://www.credu.com/?page=" + str(1)
# print(url)

# #위치 지정
# for  i in range(1,6):
#     print(i, "*", i, "=", i*i)

# print("---- 정렬지정 -----")
# for i in range(1,6):
#     print(i, "*", i, "=", str(i*i).rjust(3))

# print("---- 0으로 채우기 -----")
# for i in range(1,6):
#     print(i, "*", i, "=", str(i*i).zfill(3))

# # 서식문자
# print("{0:x}".format(10))
# print("{0:b}".format(10))
# print("{0:e}".format(4/3))
# print("{0:f}".format(4/3))
# print("{0:.2f}".format(4/3))
# print("{0:,}".format(150000000))

# 파일 쓰기(write text) 인코딩(유니코드)
# from os import path


# f = open("C:\\work\\demo.txt", "wt", encoding="utf-8")
# f.write("첫번째\n두번째\n세번째\n")
# f.close()

# # 파일 읽기(read text)
# # 특수문자 인식을 위해 \\ 사용
# f = open("C:\\work\\demo.txt", "rt", encoding="utf-8")
# # \\ 대신 / 사용해도 됨
# # f = open("C:/work/demo.txt", "rt", encoding="utf-8")
# # 하나의 문자열 변수로 받기
# result = f.read()
# print(result)

# print(f.tell())
# f.seek(0)

# # 한줄씩 처리
# print(f.readline(), end="")
# print(f.readline(), end="")

# # 전체를 리스트로 받기
# f.seek(0)
# lst = f.readlines()
# print(lst)

strA = "<<<   python is ver powerful   >>>"
# result = strA.strip("<> ")
# print(result)

# result2 = result.replace("python", "python egg")
# print(result2)
# print("demo.ppt".endswith("ppt"))
# print("MBC2580".isalnum())
# print("MBC:2580".isalnum())
# print("2580".isdecimal())

# print(result2.count("p"))
# # slicing해서 그 이후 구간부터 숫자  count
# print(result2.count("p", 7))

# print("--- 리스트 받기 ---")
# lst = result2.split()
# print(lst)
# print("---- 하나의 문자열 ---")
# print(":)".join(lst))

# #반복되는 문자열 생성
# names = ["전우치", "이순신", "김길동"]
# for name in names:
#     print("안녕하세요 {0}님 추운 겨울입니다.".format(name))
#     print("="*40)

#정규 표현식  : 특정한 패터 검색
import re
result = re.match("[0-9]*th", "35th")
result2 = re.search("[0-9]*th", " 35th")
# print(result.group())
print(result2.group())

result = re.search("apple", "this is apple")
print(result.group())

result2 = re.search("\d{4}", "올해는 2021년입니다.")
print(result2.group())

print("---우편번호----")
result = re.search("\d{5}", "우리 동네는 52301입니다.")
print(result.group())
