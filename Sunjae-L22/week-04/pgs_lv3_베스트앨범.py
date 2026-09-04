# 프로그래머스 Lv2. 의상
# https://school.programmers.co.kr/learn/courses/30/lessons/42579
# 소요시간: 40분 / 시도: 1회

from collections import defaultdict

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = []
    music_play = defaultdict(int)
    genre_play = defaultdict(list)
    idx_list = range(len(genres))
    
    # 장르별 총 재상 횟수 -> music_play
    # 장르별 어떤 노래들 있는지 -> genre_play
    for genre, play, idx in zip(genres, plays, idx_list):
        music_play[genre] += play
        genre_play[genre].append(idx)

    sorted_genres = sorted(music_play, key = lambda g: -music_play[g])

    for genre in sorted_genres:
        songs = sorted(genre_play[genre], key = lambda i: (-plays[i], i))
        answer.extend(songs[:2])

    # print(music_play)
    # print(genre_play)
    return answer

print(solution(genres, plays))