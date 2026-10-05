# 인덱스와 옥타브를 하나의 전체 인덱스로 합쳐서 계산

def solution(notes, K):
    piano = ["C", "C#", "D", "D#", "E", "F",
             "F#", "G", "G#", "A", "A#", "B"]

    result = []

    for note in notes:
        sound = note[:-1]
        octave = int(note[-1])

        idx = piano.index(sound)

        # C0부터 몇 번째 음인지
        total_idx = octave * 12 + idx

        # K > 0이면 낮아지므로 빼기
        new_idx = total_idx - K

        # C0 ~ B7 범위 처리
        if new_idx < 0:
            new_idx = 0
        elif new_idx > 95:
            new_idx = 95

        new_octave = new_idx // 12
        new_sound = piano[new_idx % 12]

        result.append(new_sound + str(new_octave))

    return result