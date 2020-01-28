class Incheon:
    name = '인천광역시'
    population = 3000000

    def intro(self):
        print('인천에 오신 것을 환영합니다')

class Yeonsu(Incheon):
    def __init__(self, name):
        self.name = name

    def intro_Yeonsu(self):
        print('여기는 ', self.name)


exam = Yeonsu('연수구')

exam.intro()
exam.intro_Yeonsu()
print(exam.name)
print(exam.population)
