#부모 클래스(공통 분모 정의) - 하위 클래스가 가지는 공통 정보를 부모 클래스로 선언
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    #인스턴스 메서드
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

#자식 클래스
class Student(Person):
    #상속받은 메서드 덮어쓰기(재정의, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        # self.name = name
        # self.phoneNumber = phoneNumber

        #Java, c#의 경우, super, base 키워드 존재
        #Phython은 부모를 가르키는 키워드가 없음
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID

    #보모의 인스턴스를 override
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
        print("Info(subject: {0},  studentID: {1} )".format(self.subject, self.studentID))


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
# print(p.__dict__) #object class에 정의 - 멤버변수를 dict 형식으로 출력
# print(s.__dict__)

p.printInfo()
s.printInfo()

