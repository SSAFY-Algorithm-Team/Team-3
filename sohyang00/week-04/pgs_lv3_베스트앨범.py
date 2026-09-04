# 프로그래머스 Lv3. 베스트앨범
# https://school.programmers.co.kr/learn/courses/30/lessons/42579


def solution(genres, plays):
    album = {}
    play_total = {}

    for index, (key, value) in enumerate(zip(genres, plays)):
        if not key in album:
            album[key] = []

        #{장르: [재생수, 고유번호]}
        album[key].append([value, index])

        #장르별 재생수 확인
        play_total[key] = play_total.get(key, 0) + value

    # 재생수 내림차순, 재생 수 동일하면 고유번호 오름차순 정렬
    for key in album:
        album[key].sort(key=lambda x:(-x[0], x[1]))

    # 장르 전체 재생수 내림차순 정렬
    play_total = dict(sorted(play_total.items(), key=lambda x:-x[1]))

    best_album = []
    # 재생수 내림차순으로 탐색
    for genre in play_total:
        # 곡은 2개까지만 탐색
        for _, index in album[genre][:2]:
            best_album.append(index)

    return best_album


solution(["classic", "pop", "classic", "classic", "pop"],
         [500, 600, 150, 800, 2500])
