# 코드트리 2-3-2-01. 007
# class: 관련 있는 값들을 하나의 객체로 묶는 틀 / 예: 코드, 장소, 시간
# __init__: 객체 생성 시 초기값을 저장 / 예: Meeting('alpha', 'L', 13)
# self: 현재 객체 자신 / 예: self.time에 해당 객체의 시간을 저장
# 해설 참고: 객체 생성 후 속성으로 값을 꺼내 출력하는 구조

class Meeting:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time


secret_code, meeting_point, time = input().split()
meeting = Meeting(secret_code, meeting_point, int(time))

print(f'secret code : {meeting.secret_code}')
print(f'meeting point : {meeting.meeting_point}')
print(f'time : {meeting.time}')
