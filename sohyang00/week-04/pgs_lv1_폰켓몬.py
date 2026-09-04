# 프로그래머스 Lv1. 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845


def solution(nums):
    count_pkm = len(nums)
    get_pkm = count_pkm//2
    pokemon = {}
    for pkm in nums:
        pokemon[pkm] = pokemon.get(pkm,0) + 1

    print(count_pkm, get_pkm)

    # if count_pkm 종류 >= get_pkm 수 => get_pkm 수
    # else count_pkm 종류 < get_pkm 수 => count_pkm 종류 수
    if len(pokemon) >= get_pkm:
        print(get_pkm)
        return get_pkm
    else:
        print(len(pokemon))
        return len(pokemon)

solution([3,3,3,2,2,2])