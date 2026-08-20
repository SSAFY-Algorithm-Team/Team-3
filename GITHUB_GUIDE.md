# 깃허브 사용 가이드

> 이 문서는 한 번 익히면 계속 쓰는 참조용입니다.
> 스터디 진행 방식은 [README](README.md)를 봐주세요.

---

## 목차

1. [최초 1회 설정](#최초-1회-설정)
2. [매주 반복하는 작업](#매주-반복하는-작업)
3. [폴더 구조](#폴더-구조)
4. [파일명 규칙](#파일명-규칙)
5. [커밋 컨벤션](#커밋-컨벤션)
6. [브랜치 정책](#브랜치-정책)
7. [문제가 생겼을 때](#문제가-생겼을-때)

---

## 최초 1회 설정

```bash
git clone https://github.com/SSAFY-Algorithm-Team/Team-3.git
cd Team-3
```

`git --version` 을 실행해서 **2.23 이상**인지 확인하세요.
그보다 낮으면 아래 `git switch` 명령이 동작하지 않으니 Git을 업데이트해주세요.

---

## 매주 반복하는 작업

이 5단계가 전부입니다.

```bash
# 1. main을 최신 상태로
git switch main
git pull

# 2. 이번 주 브랜치 만들기 (본인 깃허브 닉네임 사용)
git switch -c {닉네임}/week-01

# 3. 문제 풀고 커밋
git add .
git commit -m "solve: [SWEA 6190] 정곤이의 단조 증가하는 수 (D3)"   # SWEA
git commit -m "solve: [PGS Lv2] 소수 찾기"                      # 프로그래머스

# 4. 푸시
git push -u origin {닉네임}/week-01

# 5. GitHub 접속 → "Compare & pull request" 버튼 클릭
#    → 템플릿 작성 → Create pull request
```

> 💡 **커밋은 자주 하세요.** 문제 하나 풀 때마다 하나씩 커밋하면
> 나중에 어떤 순서로 풀었는지 기록이 남습니다.

### PR을 보낸 뒤 코드를 고치고 싶다면

같은 브랜치에 커밋하고 push하면 PR에 자동 반영됩니다. PR을 다시 만들 필요 없어요.

```bash
git add .
git commit -m "refactor: [SWEA 6190] 판정 로직 함수 분리"
git push
```

---

## 폴더 구조

```
main
├── README.md
├── docs/
│   └── GITHUB_GUIDE.md
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md
├── gxuoo/                          ← 본인 깃허브 닉네임
│   ├── week-01/
│   │   ├── swea_6190_정곤이의단조증가하는수.py
│   │   ├── swea_2805_농작물수확하기.py
│   │   └── ...
│   └── week-02/
└── cbdhoho/
└── cheese-flavor/
└── sohyang00/
└── Sunjae-L22/
└── zoo0o/
```

**본인 닉네임 폴더 안에만** 파일을 만들면 충돌이 나지 않습니다.
다른 사람 폴더는 건드리지 마세요.

---

## 파일명 규칙

| 출처         | 형식                       | 예시                                  |
| ------------ | -------------------------- | ------------------------------------- |
| SWEA         | `swea_{번호}_{문제명}.py`  | `swea_6190_정곤이의단조증가하는수.py` |
| 프로그래머스 | `pgs_lv{레벨}_{문제명}.py` | `pgs_lv2_소수찾기.py`                 |

프로그래머스는 목록에 문제 번호가 안 보이므로 **레벨**을 씁니다.
문제명으로 검색하면 바로 찾을 수 있어요.

### 파일 상단 주석 (권장)

```python
# SWEA 6190. 정곤이의 단조 증가하는 수
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWcPjEuKAFgDFAU4
# 소요시간: 45분 / 시도: 3회

# 프로그래머스 Lv2. 소수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 소요시간: 45분 / 시도: 3회
```

> ⚠️ **문제 지문 전문은 커밋하지 마세요.** 문제 번호와 링크만 남기면 충분합니다.

---

## 커밋 컨벤션

```
{타입}: [{출처} {번호}] {문제명} ({난이도})
```

| 타입       | 용도           | 예시                                                |
| ---------- | -------------- | --------------------------------------------------- |
| `solve`    | 문제 풀이      | `solve: [SWEA 6190] 정곤이의 단조 증가하는 수 (D3)` |
| `solve`    | 프로그래머스   | `solve: [PGS Lv2] 소수 찾기`                        |
| `refactor` | 기존 풀이 개선 | `refactor: [SWEA 6190] 판정 로직 함수 분리`         |
| `fix`      | 오답 수정      | `fix: [SWEA 2805] 경계 조건 처리`                   |
| `docs`     | 문서 수정      | `docs: README 2주차 문제 추가`                      |
| `chore`    | 저장소 관리    | `chore: 팀원별 주차 폴더 생성`                      |

---

## 브랜치 정책

- 브랜치명: `{닉네임}/week-{주차}` — 예: `gxuoo/week-01`
- **main에 직접 커밋 ❌** — 반드시 브랜치를 만들어 PR로
- PR 리뷰는 아직 하지 않습니다. **PR은 코드 확인용**이며, 세션 후 팀장이 일괄 머지합니다.
- 머지 후 브랜치는 삭제됩니다. 다음 주엔 새 브랜치를 만드세요.

---

## 문제가 생겼을 때

<details>
<summary><b>push할 때 403 에러가 나요</b></summary>

레포 쓰기(Write) 권한이 없는 경우입니다. **팀장에게 알려주세요.**

(팀장: Settings → Collaborators and teams에서 Write 권한 부여, 또는 조직 Base role을 Write로 변경)

</details>

<details>
<summary><b>git switch가 unknown command 라고 나와요</b></summary>

Git 버전이 2.23 미만입니다. 업데이트하거나, 임시로 아래를 쓰세요.

```bash
git checkout main         # git switch main
git checkout -b 브랜치명    # git switch -c 브랜치명
```

⚠️ `checkout`은 파일 되돌리기 기능도 겸해서 위험합니다.
`git checkout 파일명` 을 실행하면 수정사항이 **경고 없이 사라집니다.**
가능하면 Git을 업데이트하고 `switch`를 쓰세요.

</details>

<details>
<summary><b>브랜치를 잘못 만들었어요</b></summary>

```bash
git branch -m 새이름          # 현재 브랜치 이름 변경
git branch -D 지울브랜치명     # 다른 브랜치 삭제
```

</details>

<details>
<summary><b>main에 실수로 커밋했어요</b></summary>

```bash
git branch gxuoo/week-01        # 현재 상태로 새 브랜치 생성
git reset --hard origin/main  # main을 원격 상태로 되돌리기
git switch gxuoo/week-01        # 새 브랜치로 이동
```

</details>

<details>
<summary><b>커밋 메시지를 잘못 썼어요</b></summary>

아직 push하지 않았다면:

```bash
git commit --amend -m "올바른 메시지"
```

이미 push했다면 그냥 두세요. 다음부터 잘 쓰면 됩니다.

</details>

<details>
<summary><b>PR을 어디서 만드는지 모르겠어요</b></summary>

push하고 나서 GitHub 레포 페이지에 들어가면 상단에
**"Compare & pull request"** 노란 버튼이 뜹니다. 그걸 누르면 됩니다.

버튼이 안 보이면: Pull requests 탭 → New pull request →
base를 `main`, compare를 본인 브랜치로 선택

</details>

<details>
<summary><b>다른 사람 코드를 보고 싶어요</b></summary>

- **머지된 코드**: main 브랜치의 각자 닉네임 폴더
- **아직 PR 상태인 코드**: Pull requests 탭 → 해당 PR → **Files changed**

</details>
