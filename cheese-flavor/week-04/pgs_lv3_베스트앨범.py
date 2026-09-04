# 프로그래머스 Lv3. 베스트앨범
# https://school.programmers.co.kr/learn/courses/30/lessons/42579
# 소요시간: 70분 / 시도: 3회


def solution(genres, plays):
    answer = []
    genres_rank = {}
    
    # 최대한 dict 연습 겸 써보기
    # 미리 다 정렬을 진행해서 진행 / 음수로 정렬 -> id번호랑 한번에 sort하려고

    for i in range(len(genres)):
        if genres[i] not in genres_rank:
            genres_rank[genres[i]] = []
        genres_rank[genres[i]].append((-plays[i], i)) 
    
    
    #총 재생 횟수용 리스트
    genre_totals = []

    for genre in genres_rank:
        total = 0
        for play, idx in genres_rank[genre]:
            total += play
        genre_totals.append((total, genre))
    
    genre_totals.sort()
    
    #총 재생수 많은 순에서 각각의 세부 곡 뽑아서 진행
    answer = []
    for total, genre in genre_totals:          
        songs = sorted(genres_rank[genre])
        
        count = 0
        for play, idx in songs:
            if count >= 2:                     
                break
            answer.append(idx)
            count += 1
    
    return answer