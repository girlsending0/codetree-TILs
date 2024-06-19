# 여러가지 key가 주어진 경우 이런식으로 class를 만들어서 푸는게 편함.

class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

student_list = []
n = int(input())

for _ in range(n):
    name, height, weight = tuple(input().split())
    student_list.append(Student(name, int(height), int(weight)))

student_list.sort(key = lambda x : (x.height, -x.weight)) # 기본은 ascending 정렬임. descending 정렬하려면 -를 붙여야함.

for st in student_list:
    print(st.name, st.height, st.weight)