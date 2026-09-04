# 프로그래머스 Lv3. 베스트앨범 (코어 문제)
# https://school.programmers.co.kr/learn/courses/30/lessons/42579
# 소요시간: 60분 / 시도: 3회

from collections import defaultdict

def solution(genres, plays):
    total = defaultdict(int)
    songs = defaultdict(list)
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        total[genre] += play            # 총 재생 횟수를 저장
        songs[genre].append((play, i))  # 노래 재생 횟수와 고유 번호 저장
    
    # 장르를 총 재생수 내림차순으로 정렬
    genre_list = []
    for genre in total:
        genre_list.append((total[genre], genre))
    genre_list.sort(reverse=True)
    
    # 장르마다 곡을 정렬해서 최대 2곡 뽑기
    answer = []
    for genre_total, genre in genre_list:
        song_list = songs[genre]
        song_list.sort(key=sort_key)
        
        count = 0
        for play, index in song_list:
            answer.append(index)
            count += 1
            if count == 2:
                break
    
    return answer


def sort_key(song):
    play, index = song
    return (-play, index)   # 재생 횟수, 고유 번호 정렬 기준이 반대 방향이기에, 하나의 방향으로 통일
