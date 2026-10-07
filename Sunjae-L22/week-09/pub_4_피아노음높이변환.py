# 피아노 음높이 변환
# 소요시간 : 10분

notes = ["C4", "D4", "E4"]
K = 1

notes_2 = ["C0", "C#0", "C1", "C#1"]
K_2 = 2

def solution(notes, K):
    names = [
        "C", "C#", "D", "D#", "E", "F",
        "F#", "G", "G#", "A", "A#", "B"
    ]
    answer = []

    for note in notes:
        name = note[:-1]        # "C#4" → "C#"
        octave = int(note[-1])  # "C#4" → 4

        # 음을 0~95 사이의 번호로 변환
        number = octave * 12 + names.index(name)

        # K가 양수면 낮추고, 음수면 높임
        number = number - K

        # C0보다 낮아지거나 B7보다 높아지면 고정
        if number < 0:
            number = 0
        elif number > 95:
            number = 95

        # 번호를 다시 음 이름과 옥타브로 변환
        new_name = names[number % 12]
        new_octave = number // 12

        answer.append(new_name + str(new_octave))

    return answer

print(solution(notes, K))
print(solution(notes_2, K_2))