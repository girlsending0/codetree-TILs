class Student:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time
    
a, b, c= tuple(input().split())
st = Student(a, b, c)
print('secret code :', st.secret_code)
print('meeting point :', st.meeting_point)
print('time :', st.time)