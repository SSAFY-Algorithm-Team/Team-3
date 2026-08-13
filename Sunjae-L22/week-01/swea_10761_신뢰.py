from collections import deque

T = int(input())

for test_case in range(1, T+1):
    total_input = list(input().split())

    # 입력받은 리스트의 첫번째 요소 : 작업의 개수
    work_n = int(total_input[0])

    # 작업 리스트 : 나머지 리스트
    work_list = total_input[1:]

    work_q = deque()
    orange_work_list = deque()
    blue_work_list = deque()

    # work_list를 작업 단위로 묶기
    for i in range(work_n):
        robot = work_list[i*2]
        btn = work_list[i*2 + 1]
        work_q.append((robot, btn))

        # A, B 각자 작업 리스트 만들어주기
        if robot == 'O':
            orange_work_list.append(int(btn))
        else:
            blue_work_list.append(int(btn))

    time = 0

    # 오렌지, 블루의 위치
    orange_loc = 1
    blue_loc = 1

    # 작업 리스트가 빌때까지
    while work_q:
        # 현재 작업 꺼내기
        now_working = work_q.popleft()
        target = int(now_working[1])

        # blue 작업할때 orange는 자기 다음 작업까지 최대한 이동하는 것이 핵심 로직!
        if now_working[0] == 'B':
            # B가 현재 작업 버튼까지 이동하고 버튼 누르기까지 걸리는 시간, blue의 위치는 현재 작업 중인 위치로 이동
            spent = abs(target - blue_loc) + 1
            blue_loc = target
            time += spent

            # 만약 오렌지한테 작업할 게 남아있다면
            if orange_work_list:
                # Blue가 작업을 끝내는동안 Orange가 최대한 이동 ->  다음 Orange 작업까지 이동거리보다 작으면 도착해있고(버튼은 못누름), 아니면 그 차이만큼 이동
                if spent >= abs(orange_work_list[0] - orange_loc):
                    orange_loc = orange_work_list[0]
                else:
                    # 오랜지 위치가 다음 작업 버튼보다 큰경우, spent만큼 아래로 이동
                    if orange_loc > orange_work_list[0]:
                        orange_loc -= spent
                    # 오렌지 위치가 다음 작업 버튼보다 작은 경우, spent만큼 위로 이동
                    else:
                        orange_loc += spent
            # blue가 작업 하나 끝냄
            blue_work_list.popleft()

        # 위랑 완전히 반대 경우(orange가 작업할 때 blue는 이동)
        else:
            spent = abs(target - orange_loc) + 1
            orange_loc = target
            time += spent
            if blue_work_list:
                if spent >= abs(blue_work_list[0] - blue_loc):
                    blue_loc = blue_work_list[0]
                else:
                    if blue_loc > blue_work_list[0]:
                        blue_loc -= spent
                    else:
                        blue_loc += spent
            orange_work_list.popleft()

    print(f"#{test_case} {time}")