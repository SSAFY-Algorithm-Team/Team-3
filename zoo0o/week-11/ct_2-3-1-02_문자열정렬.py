# 코드트리 2-3-1-02. 문자열정렬
# sorted(s): 문자를 오름차순으로 정렬한 리스트를 반환 / 예: 'cab' → ['a', 'b', 'c']
# ''.join(arr): 문자열 원소들을 구분자 없이 연결 / 예: ['a', 'b', 'c'] → 'abc'

s = input()
sorted_arr = sorted(s)
sorted_str = ''.join(sorted_arr)
print(sorted_str)
