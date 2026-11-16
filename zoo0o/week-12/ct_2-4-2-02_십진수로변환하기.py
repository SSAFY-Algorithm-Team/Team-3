# 코드트리 2-4-2-02. 십진수로 변환하기 (Easy)
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-convert-to-decimal/description

# [2진수 → 10진수] 문자열로 입력받아 왼쪽 자릿수부터 순서대로 계산
# num은 지금까지 읽은 부분을 10진수로 변환한 값이며, 처음에는 0으로 초기화
# num = num * 2 + int(binary[i])
# 기존 값에 2를 곱해 2진수 기준 한 자리 밀고, 현재 숫자를 더하기
# binary[i]는 문자이므로 int()로 정수 변환 후 계산
# 예: "110" → num이 0 → 1 → 3 → 6으로 변화

binary = input()
num = 0
for i in range(len(binary)):
    num = num * 2 + int(binary[i])

print(num)
