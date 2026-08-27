# 알고리즘 스터디 (삼성 SW 역량테스트 B형 대비)

> SSAFY 알고리즘 스터디 · 6인 · 매주 목요일

📖 **처음 오셨나요? → [깃허브 사용 가이드](GITHUB_GUIDE.md)**

---

## 목표

삼성 SW 역량테스트 **B형(Professional)** 취득.

B형은 4시간 동안 1문제를 풀며, Main 함수는 수정하지 않고 주어진 함수 내용만 구현하는 형식입니다.
단순 구현보다 **"완전탐색을 어떻게 최적화할 것인가"** 를 묻는 문제가 주로 나옵니다.

**사용 언어: Python**

---

## 진행 방식

```
목 세션 ─── 금·토·일·월·화   각자 문제 풀이 → 브랜치에 커밋 & push
                    수 밤     PR 생성 (템플릿 작성)
                    목 밤     스터디 세션 (120분)
                    세션 후   팀장이 PR 일괄 머지
```

### 세션 타임테이블 (120분)

| 시간          | 내용                                            |
| ------------- | ----------------------------------------------- |
| 00:00 - 00:15 | 체크인 — 푼 문제 수, 소요시간, 막힌 지점 공유   |
| 00:15 - 00:55 | **자유 발표** — 5명 × 8분 (발표 5분 + 질문 3분) |
| 00:55 - 01:05 | 휴식                                            |
| 01:05 - 01:45 | **코어 문제 코드 비교** — 전원이 푼 1문제       |
| 01:45 - 02:00 | 공통 이슈 정리 + 다음 주 코어 문제 지정         |

### 자유 발표

- 각자 이번 주에 **가장 이야기하고 싶은 문제 1개**를 골라 발표합니다.
- 잘 푼 문제여도, **못 푼 문제여도 괜찮습니다.** 오히려 막힌 문제가 이야기하기 좋아요.
- 발표할 문제는 PR에 미리 적어주세요. (겹치면 팀장이 목요일 아침에 조정)

### 코어 문제 코드 비교

전원이 같은 문제를 풀어왔으니, 코드를 나란히 놓고 봅니다.

1. **각자 접근 방식 한 줄씩** (10분) — 자세한 설명 X, "저는 이렇게 했어요" 정도
2. **접근이 몇 갈래인지 정리** (5분) — 보통 2~3갈래로 묶입니다
3. **갈래별로 파고들기** (20분)
   - 각 방식의 연산 횟수는?
   - 코드가 짧은 쪽이 항상 나은가?
   - 경계 조건(N=1, 짝수 등)에서 안 터지나?
   - 틀린 사람은 어디서 틀렸나?
4. **정리** (5분) — "어느 게 정답"이 아니라 "언제 어느 게 유리한지"


---

## 규칙

1. **문제당 고민 상한 60분** — 넘으면 해설 참고 가능. 단 PR에 막힌 지점 체크 필수
2. **AI는 60분 이후에만** — 사용했다면 PR에 "어디서 막혀서 무엇을 물어봤는지" 기록
   (처벌이 아니라 기록입니다. 오히려 좋은 이야깃거리가 됩니다)
3. **PR 마감: 수요일 밤 12시**
4. **다 못 풀어도 세션에 옵니다** — 어디까지 했는지가 중요합니다
5. **3주차에 진행 방식 회고** — 안 맞는 룰은 그때 바꿉니다

---

<details>
<summary><h2>1주차 — SWEA D2~D3 구현 (17문제)</h2></summary>

**출처:** SWEA 역량테스트 리스트업 → IM 대비 추천 세트 (D2~D3만)

### 코어 문제 ⭐

전원 필수. 세션에서 다 같이 코드를 비교합니다.

| 번호      | 제목       | 난이도 | 링크                                                                                                              |
| --------- | ---------- | ------ | ----------------------------------------------------------------------------------------------------------------- |
| **25052** | **등산로** | D2     | [바로가기](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZiyl6OKpUjHBIP9) |

### D2 (10문제)

| 번호  | 제목                           | 링크                                                                                                              |
| ----- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| 10760 | 우주선착륙2                    | [바로가기](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXSHJueab1oDFAQT) |
| 12712 | 파리퇴치3                      | [바로가기](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXuARWAqDkQDFARa) |
| 1926  | 간단한 369게임                 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PTeo6AHUDFAUq)         |
| 1959  | 두 개의 숫자열                 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpoFaAS4DFAUq)         |
| 1979  | 어디에 단어가 들어갈 수 있을까 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq)         |
| 20230 | 풍선팡 보너스게임2             | [바로가기](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AY3FFOTaN7EDFAXh) |
| 25052 | 등산로                         | [바로가기](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZiyl6OKpUjHBIP9) |
| 25985 | 숫자열의 최대 곱               | [바로가기](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZvmEUAqG6LHBIQE) |
| 26045 | 부분 수열 판별                 | [바로가기](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZwe0FZaG1bHBIPa) |
| 26059 | 과일 등급 분류                 | [바로가기](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZwl9ifa3dLHBIT3) |

### D3 (7문제)

| 번호  | 제목                         | 링크                                                                                                      |
| ----- | ---------------------------- | --------------------------------------------------------------------------------------------------------- |
| 10761 | 신뢰                         | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXSVc1TqEAYDFAQT) |
| 11315 | 오목 판정                    | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXaSUPYqPYMDFASQ) |
| 1289  | 원재의 메모리 복구하기       | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV19AcoKI9sCFAZN) |
| 14555 | 공과 잡초                    | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYGtoa3qARcDFARC) |
| 2805  | 농작물 수확하기              | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB) |
| 3499  | 퍼펙트 셔플                  | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWGsRbk6AQIDFAVW) |
| 6190  | 정곤이의 단조 증가하는 수 ⭐ | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWcPjEuKAFgDFAU4) |

</details>

---

<details>
<summary><h2>2주차 — 완전탐색 (5문제 + 공통 1문제)</h2></summary>

**출처:** SWEA 역량테스트 리스트업 → A형 대비 추천 세트 / 프로그래머스 코딩테스트 고득점 Kit → 완전탐색

1주차는 D2~D3 구현 위주였다면, 2주차부터는 **완전탐색**으로 넘어갑니다.
"모든 경우를 어떻게 빠짐없이 만들 것인가" + "그걸 어떻게 줄일 것인가" 두 가지를 봅니다.

### 코어 문제 ⭐

전원 필수. 세션에서 다 같이 코드를 비교합니다.

| 번호     | 제목          | 난이도 | 링크                                                                                             |
| -------- | ------------- | ------ | ------------------------------------------------------------------------------------------------ |
| **5656** | **벽돌 깨기** | D3     | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo) |


### 공통 문제

조직 내 전체 스터디에서 다 같이 푼 문제입니다.

| 번호 | 제목      | 난이도 | 링크                                                                                             |
| ---- | --------- | ------ | ------------------------------------------------------------------------------------------------ |
| 1247 | 최적 경로 | D5     | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15OZ4qAPICFAYD) |

### SWEA (2문제)

| 번호 | 제목                 | 난이도 | 링크                                                                                             |
| ---- | -------------------- | ------ | ------------------------------------------------------------------------------------------------ |
| 1767 | 프로세서 연결하기    | D4     | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf) |
| 5656 | 벽돌 깨기 ⭐         | D3     | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo) |

### 프로그래머스 (3문제)

| 제목            | 난이도 | 링크                                                                    |
| --------------- | ------ | ----------------------------------------------------------------------- |
| 최소 직사각형   | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/86491) |
| 소수 찾기       | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42839) |
| 피로도          | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/87946) |

</details>

---

<details>
<summary><h2>3주차 — DFS/BFS + B형 기출 (11문제)</h2></summary>

**출처:** 프로그래머스 코딩테스트 고득점 Kit → DFS/BFS / SWEA → Pro (B형 기출)

3주차부터는 **유형별 학습 + B형 기출 병행** 으로 갑니다.

- **프로그래머스 DFS/BFS 세트는 전부** 풉니다 — 탐색 유형 감각 잡기용
- **B형 기출은 이틀에 1문제** 페이스로, 다음 목요일 세션 전까지 4문제를 풉니다

### 코어 문제 ⭐

전원 필수. 세션에서 다 같이 코드를 비교합니다.

| 제목              | 난이도 | 링크                                                                       |
| ----------------- | ------ | -------------------------------------------------------------------------- |
| **아이템 줍기**   | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/87694) |


### 프로그래머스 — DFS/BFS (7문제)

| 제목               | 난이도 | 링크                                                                       |
| ------------------ | ------ | -------------------------------------------------------------------------- |
| 타겟 넘버          | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/43165) |
| 게임 맵 최단거리   | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/1844)  |
| 네트워크           | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/43162) |
| 단어 변환          | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/43163) |
| 여행경로           | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/43164) |
| 아이템 줍기 ⭐     | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/87694) |
| 퍼즐 조각 채우기   | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/84021) |

### B형 기출 (4문제 · 이틀에 1문제)

| 순서 | 제목             | 권장 기간 | 링크                                     |
| ---- | ---------------- | --------- | ---------------------------------------- |
| 1 | 단어장 | 목 · 금 | [바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZt8IiBqxEDHBIN6&contestProbId=AZwdOG5aC2rHBIPa&probBoxId=AZt8IiBqxEHHBIN6&type=PROBLEM&problemBoxTitle=B%ED%98%95+%EA%B8%B0%EC%B6%9C&problemBoxCnt=31) |
| 2 | 기계식 주차장 | 토 · 일 | [바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZt8IiBqxEDHBIN6&contestProbId=AZvfGm7qDZ7HBIN6&probBoxId=AZt8IiBqxEHHBIN6&type=PROBLEM&problemBoxTitle=B%ED%98%95+%EA%B8%B0%EC%B6%9C&problemBoxCnt=31) |
| 3 | 타워디펜스게임 | 월 · 화 | [바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZt8IiBqxEDHBIN6&contestProbId=AZvfDDtKDNjHBIN6&probBoxId=AZt8IiBqxEHHBIN6&type=PROBLEM&problemBoxTitle=B%ED%98%95+%EA%B8%B0%EC%B6%9C&problemBoxCnt=31) |
| 4 | 빙하의 이동 | 수 · 목 | [바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZt8IiBqxEDHBIN6&contestProbId=AZve05OqCl3HBIN6&probBoxId=AZt8IiBqxEHHBIN6&type=PROBLEM&problemBoxTitle=B%ED%98%95+%EA%B8%B0%EC%B6%9C&problemBoxCnt=31) |

> 4번 문제는 PR 마감(수요일 밤) 이후에 걸치니, 마감 시점까지 진행한 만큼 커밋하고
> 남은 부분은 세션에서 이야기합니다.

</details>

---

<details open>
<summary><h2>4주차 — 해시 + SQL(SELECT) (8문제)</h2></summary>

**출처:** 프로그래머스 코딩테스트 고득점 Kit → 해시 / 프로그래머스 SQL 고득점 Kit → SELECT

4주차는 **문제 수를 줄였습니다.** 대신 두 가지를 새로 시작합니다.

- **해시 세트는 전부** 풉니다 — "무엇을 키로 잡을 것인가"를 반복해서 연습하는 세트입니다
- **SQL 코테 준비 시작** — SELECT 기초 3문제로 가볍게 발을 담급니다

### 코어 문제 ⭐

전원 필수. 세션에서 다 같이 코드를 비교합니다.

| 제목             | 난이도 | 링크                                                                       |
| ---------------- | ------ | -------------------------------------------------------------------------- |
| **베스트앨범**   | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42579) |

### 프로그래머스 — 해시 (5문제)

| 제목                   | 난이도 | 링크                                                                       |
| ---------------------- | ------ | -------------------------------------------------------------------------- |
| 완주하지 못한 선수     | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42576) |
| 폰켓몬                 | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/1845)  |
| 전화번호 목록          | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42577) |
| 의상                   | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42578) |
| 베스트앨범 ⭐          | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42579) |

### 프로그래머스 SQL — SELECT (3문제)

| 제목                         | 난이도 | 링크                                                                        |
| ---------------------------- | ------ | --------------------------------------------------------------------------- |
| 평균 일일 대여 요금 구하기   | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/151136) |
| 인기있는 아이스크림          | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/133024) |
| 과일로 만든 아이스크림 고르기 | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/133025) |

> SQL 문제는 `.sql` 파일로 제출합니다. 커밋 메시지는 `solve: [SQL Lv1] 인기있는 아이스크림` 형식으로 써주세요.

</details>

---

## 제출 방법 요약

```bash
git switch main
git pull
git switch -c {깃허브 닉네임}/week-04
# 문제 풀고 커밋
git push -u origin {깃허브 닉네임}/week-04
# GitHub에서 "Compare & pull request" 클릭
```

자세한 설명, 파일명 규칙, 오류 해결은 **[깃허브 사용 가이드](GITHUB_GUIDE.md)** 를 참고하세요.
