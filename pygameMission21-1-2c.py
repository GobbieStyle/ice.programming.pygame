class Incheon:
    population = 3000000

class Yeonsu(Incheon):
    pass

exam1 = Yeonsu()
exam2 = Yeonsu()

exam1.population = 400000

print(exam1.population)
print(exam2.population)