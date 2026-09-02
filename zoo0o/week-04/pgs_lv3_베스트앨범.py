# 프로그래머스 Lv3. 베스트앨범
# https://school.programmers.co.kr/learn/courses/30/lessons/42579
# 구현 > AI 사용

def solution(genres, plays):
    genre_total = {}
    genre_songs = {}

    # 1. 장르별 총 재생 횟수 + 노래 정보 저장
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        if genre not in genre_total:
            genre_total[genre] = 0
            genre_songs[genre] = []

        genre_total[genre] += play
        genre_songs[genre].append((i, play))

    # 2. 총 재생 횟수가 많은 장르부터 정렬
    sorted_genres = sorted(
        genre_total,
        key=genre_total.get,
        reverse=True
    )

    answer = []

    # 3. 각 장르의 노래를 재생 횟수가 많은 순서로 정렬
    for genre in sorted_genres:
        songs = genre_songs[genre]

        # songs.sort(key=lambda x: (-x[1], x[0]))
        songs.sort(key=lambda x: x[0])
        songs.sort(key=lambda x: x[1], reverse=True)

        # 4. 장르마다 최대 2곡의 고유번호 저장
        for song_id, play in songs[:2]:
            answer.append(song_id)

    return answer