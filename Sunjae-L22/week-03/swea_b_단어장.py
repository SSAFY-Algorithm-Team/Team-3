import bisect
# 위에거는 시간초과난 코드... 리스트 말고 해시를 잘 사용하도록 하자

# class PAGE:
#     def __init__(self, no, word):
#         self.no = no
#         self.word = word

# def init() -> None:
#     # words -> 단어, 중요도, 등록 순서
#     # keys -> 정렬을 위해 사용
#     global words, current_page, keys
    
#     words = [["a", 1, 1]]
#     keys = ["a"]
#     current_page = 1
#     return

# # mWord : 추가할 단어(문자열)
# # mImportance : 등록할 단어의 중요도
# def add(mWord: str, mImportance: int) -> PAGE:
#     global words, current_page, keys

#     register = len(words) + 1
#     idx = bisect.bisect_left(keys, mWord)   # O(log N)
#     keys.insert(idx, mWord)                 # O(N) — 메모리 이동뿐
#     words.insert(idx, [mWord, mImportance, register])

#     current_page = idx
#     return PAGE(idx + 1, mWord)

# def move(mDir : int) -> PAGE:
#     global current_page
    
#     if mDir == 1:
#         current_page += 1
#         return PAGE(current_page+1, words[current_page][0])
#     elif mDir == -1:
#         current_page -= 1
#         return PAGE(current_page+1, words[current_page][0])

# def search(mStr : str) -> PAGE:
#     global words, current_page
    
#     # 단어장에서 단어만 
#     only_words = [w[0] for w in words]
    
#     # 검색에 성공하면! -> 3단계 우선순위
#     # 1) 만약 같은 단어가 있다면 바로 반환
#     if mStr in only_words:
#         found_word_page = only_words.index(mStr)
#         current_page = found_word_page
#         return PAGE(found_word_page+1, words[found_word_page][0])
    
#     # 2) 같은 단어가 없다면 그 단어로 시작하는 단어 중 중요도 가장 높은 단어
#     cur_max_imp = 0
#     start_with_mstr = []
#     page_hubo = []
#     for i in range(len(only_words)):
#         if only_words[i].startswith(mStr):
#             # 가장 높은 중요도 등장 -> 다 버리고 그것만 추가
#             if words[i][1] > cur_max_imp:
#                 cur_max_imp = words[i][1]
#                 start_with_mstr = [words[i][0]]
#                 page_hubo = [i]
#             # 중요도 동점 -> 3번 우선순위를 위해 후보 리스트에 추가
#             elif words[i][1] == cur_max_imp:
#                 start_with_mstr.append(words[i][0])
#                 page_hubo.append(i)
    
#     # 3) 만약 중요도 가장 높은 게 하나면 바로 그거, 여러개면 먼저 등록된거, 
#     #    0개면 검색 실패(-1 반환)
#     if len(start_with_mstr) == 0:
#         return PAGE(-1, words[current_page][0])
#     elif len(start_with_mstr) == 1:
#         current_page = page_hubo[0]
#         return PAGE(page_hubo[0]+1, start_with_mstr[0])
#     else:
#         idx = -1
#         page = -1
#         first_register = len(words) + 1
#         for i in range(len(start_with_mstr)):
#             if words[page_hubo[i]][2] < first_register:
#                 first_register = words[page_hubo[i]][2]
#                 idx = i
#                 page = page_hubo[i]
#         current_page = page
#         return PAGE(page+1, start_with_mstr[idx])
    
# def go(mNo : int) -> PAGE:
#     global words, current_page
    
#     current_page = mNo-1
#     return PAGE(current_page+1, words[current_page][0])

class PAGE:
    __slots__ = ('no', 'word')
    def __init__(self, no, word):
        self.no = no
        self.word = word
 
def init() -> None:
    global keys, best, current_page
    keys = ["a"]                      # 사전순 정렬 배열 (페이지 번호 담당)
    best = {"a": (-1, 1, "a")}        # 접두사 -> (-중요도, 등록순서, 단어)
    current_page = 0                  # 0-based 인덱스
 
def add(mWord: str, mImportance: int) -> PAGE:
    global current_page
    register = len(keys) + 1
    idx = bisect.bisect_left(keys, mWord)
    keys.insert(idx, mWord)
 
    cand = (-mImportance, register, mWord)
    for i in range(1, len(mWord) + 1):
        p = mWord[:i]
        cur = best.get(p)
        if cur is None or cand < cur:
            best[p] = cand
 
    current_page = idx
    return PAGE(idx + 1, mWord)
 
def move(mDir: int) -> PAGE:
    global current_page
    current_page += mDir
    return PAGE(current_page + 1, keys[current_page])
 
def search(mStr: str) -> PAGE:
    global current_page
    i = bisect.bisect_left(keys, mStr)
    if i < len(keys) and keys[i] == mStr:
        current_page = i
        return PAGE(i + 1, mStr)
 
    cur = best.get(mStr)
    if cur is None:
        return PAGE(-1, keys[current_page])
 
    word = cur[2]
    current_page = bisect.bisect_left(keys, word)
    return PAGE(current_page + 1, word)
 
def go(mNo: int) -> PAGE:
    global current_page
    current_page = mNo - 1
    return PAGE(mNo, keys[current_page])