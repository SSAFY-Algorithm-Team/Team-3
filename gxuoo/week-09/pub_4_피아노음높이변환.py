# 기출 4. 피아노 음높이 변환
# 소요시간: 15분 / 시도: 1회

def solution(notes, K):
    octaves = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    levels = [0, 1, 2, 3, 4, 5, 6, 7]
    answer = []

    for sound in notes:
        # 음 이름
        octave = sound[:-1]

        # 옥타브 번호
        level = int(sound[-1])

        # 0부터 95까지 가능
        index = level * 12 + octaves.index(octave)

        # K만큼 이동 후 최소, 최대 처리
        index -= K
        index = max(0, min(95, index))

        # 음 변환
        new_sound = octaves[index % 12]
        new_level = index // 12

        answer.append(new_sound + str(new_level))

    return answer


if __name__ == "__main__":
    print(solution(["C4", "D4", "E4"], 1))  # ["B3", "C#4", "D#4"]
    print(solution(["C0", "C#0", "C1", "C#1"], 2))  # ["C0", "C0", "A#0", "B0"]
