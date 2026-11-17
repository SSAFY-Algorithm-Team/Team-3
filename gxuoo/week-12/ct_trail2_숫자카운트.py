# 코드트리 Trail2. 숫자 카운트
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-numeric-count/description

n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

# Please write your code here.
cnt = 0
for x in range(1, 10):
    for y in range(1, 10):
        for z in range(1, 10):
            # 중복 숫자가 있으면 후보가 될 수 없음
            if x == y or y == z or x == z:
                continue
            cand = [x, y, z]

            ok = True
            for idx in range(n):
                num = a[idx]       
                s = b[idx]         
                bl = c[idx]        

                # 질문한 수를 자릿수 리스트로 분리
                hundreds = num // 100
                tens = (num // 10) % 10
                ones = num % 10
                guess = [hundreds, tens, ones]

                # 후보 수와 비교해서 스트라이크, 볼 세기
                strike = 0
                ball = 0
                for i in range(3):
                    if cand[i] == guess[i]:
                        strike += 1
                    elif cand[i] in guess:
                        ball += 1

                # 들은 결과와 하나라도 다르면 탈락
                if strike != s or ball != bl:
                    ok = False
                    break

            if ok:
                cnt += 1

print(cnt)
