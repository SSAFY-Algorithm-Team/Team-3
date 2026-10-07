# SSAFY Data 6반 알고리즘 스터디 - Team 3

> 6인 · 매주 수요일

📖 **처음 오셨나요? → [깃허브 사용 가이드](GITHUB_GUIDE.md)**

---

## 목표

하반기 기업·공기업 **코딩테스트 합격**.

알고리즘은 유형별 문제와 실제 기출·응시 복기 문제를 함께 풀고,
SQL은 프로그래머스 SQL 고득점 Kit으로 병행합니다.

**사용 언어: Python**

---

## 진행 방식

```
수 세션 ─── 목·금·토·일·월   각자 문제 풀이 → 브랜치에 커밋 & push
                    화 밤     PR 생성 (템플릿 작성)
                    수 밤     스터디 세션 (120분)
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
- 발표할 문제는 PR에 미리 적어주세요. (겹치면 팀장이 수요일 아침에 조정)

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
3. **PR 마감: 화요일 밤 12시**
4. **다 못 풀어도 세션에 옵니다** — 어디까지 했는지가 중요합니다
5. **3주차에 진행 방식 회고** — 안 맞는 룰은 그때 바꿉니다

---

## SQL 트랙

5주차부터 SQL을 본격적으로 시작합니다. (**6·7주차는 알고리즘에 집중하기 위해, 8·9주차는 기출 세트로 쉽니다.** 10주차는 로드맵 대신 파트별 Lv3~4 문제를 맛봅니다 — 아래 표의 매핑을 다섯 주씩 밀었습니다.)
**프로그래머스 SQL 고득점 Kit 106문제를 8주에 완주**하는 것이 목표이고,
알고리즘 문제와 병행하므로 매주 알고리즘 세트 + SQL 한 묶음씩 가져갑니다.

<details>
<summary><b>📋 SQL 8주 로드맵 — 전체 106문제 (펼치기)</b></summary>

영역(SELECT/JOIN 등)이 아니라 **그 주에 쓰는 SQL 문법**을 기준으로 묶었습니다.

| SQL 주차 | 스터디 주차 | 주제                                            | 문제 수 | 난이도   |
| :------: | :---------: | ----------------------------------------------- | :-----: | -------- |
|    1     |  5주차 ✅   | 단일 테이블 기본 조회                           |   18    | Lv1 위주 |
|    —     |    6주차    | 쉬는 주 — 알고리즘 집중                         |    —    | —        |
|    —     |    7주차    | 쉬는 주 — 6주차 이월분 + SWEA 커리큘럼 완주     |    —    | —        |
|    —     |    8주차    | 쉬는 주 — 기출 세트 (SQL 1문제 포함)            |    —    | —        |
|    —     |    9주차    | 쉬는 주 — 코테 복기 + 기출 이월 (SQL 2문제)     |    —    | —        |
|    —     | **10주차**  | **파트별 Lv3~4 맛보기 — 6파트 × 2문제**         |   12    | Lv2~4    |
|    2     |   11주차    | 집계 함수                                       |   13    | Lv1~3    |
|    3     |   12주차    | NULL 처리 + GROUP BY 입문                       |   14    | Lv1~3    |
|    4     |   13주차    | GROUP BY 심화 + CASE                            |   12    | Lv2~4    |
|    5     |   14주차    | 문자열 · 날짜                                   |   14    | Lv1~3    |
|    6     |   15주차    | JOIN 기본                                       |   11    | Lv2~4    |
|    7     |   16주차    | 서브쿼리 + JOIN 심화                            |   12    | Lv2~5    |
|    8     |   17주차    | 종합 · 고난도                                   |   12    | Lv2~5    |

> 문제 수는 주차마다 다르지만 소요 시간은 비슷합니다.
> SQL 1주차는 18문제여도 전부 Lv1이라 1시간 남짓이고, 8주차는 12문제인데 Lv4 이상이 8개입니다.

> **스터디 주차 매핑은 잠정입니다.** 알고리즘 진도에 따라 한 주 쉬거나 밀릴 수 있고,
> 그때는 이 표의 매핑만 조정합니다. **SQL 주제 순서 자체는 바뀌지 않습니다.**

### SQL 진행 규칙

1. **언어는 MySQL로 통일** — 최근 추가된 문제는 Oracle을 지원하지 않습니다
2. **파일명**: `sql_lv{레벨}_{문제명}.sql` (예: `sql_lv1_인기있는아이스크림.sql`)
3. **커밋 메시지**: `solve: [SQL Lv1] 인기있는 아이스크림`
4. **Lv4 이상은 선택** — 필수 문제 리뷰를 먼저 끝내고 남는 시간에 다룹니다

### 세션에서 SQL을 다루는 방식

SQL은 문제당 5~15분이라 "못 푼 사람 설명 듣기"에 쓸 시간이 적습니다.
대신 **같은 문제를 다르게 푼 쿼리를 비교**하는 데 시간을 씁니다.
서브쿼리 / `HAVING` / `RANK()` 로 다 풀리는 문제가 많아서, 각자 다르게 풀어오면 그 자체로 토론거리가 됩니다.

</details>

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

| 번호     | 제목          | 난이도 | 링크                                                                                                      |
| -------- | ------------- | ------ | --------------------------------------------------------------------------------------------------------- |
| **5656** | **벽돌 깨기** | D3     | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo) |

### 공통 문제

조직 내 전체 스터디에서 다 같이 푼 문제입니다.

| 번호 | 제목      | 난이도 | 링크                                                                                                      |
| ---- | --------- | ------ | --------------------------------------------------------------------------------------------------------- |
| 1247 | 최적 경로 | D5     | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15OZ4qAPICFAYD) |

### SWEA (2문제)

| 번호 | 제목              | 난이도 | 링크                                                                                                      |
| ---- | ----------------- | ------ | --------------------------------------------------------------------------------------------------------- |
| 1767 | 프로세서 연결하기 | D4     | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf) |
| 5656 | 벽돌 깨기 ⭐      | D3     | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo) |

### 프로그래머스 (3문제)

| 제목          | 난이도 | 링크                                                                        |
| ------------- | ------ | --------------------------------------------------------------------------- |
| 최소 직사각형 | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/86491) |
| 소수 찾기     | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42839) |
| 피로도        | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/87946) |

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

| 제목            | 난이도 | 링크                                                                        |
| --------------- | ------ | --------------------------------------------------------------------------- |
| **아이템 줍기** | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/87694) |

### 프로그래머스 — DFS/BFS (7문제)

| 제목             | 난이도 | 링크                                                                        |
| ---------------- | ------ | --------------------------------------------------------------------------- |
| 타겟 넘버        | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/43165) |
| 게임 맵 최단거리 | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/1844)  |
| 네트워크         | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/43162) |
| 단어 변환        | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/43163) |
| 여행경로         | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/43164) |
| 아이템 줍기 ⭐   | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/87694) |
| 퍼즐 조각 채우기 | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/84021) |

### B형 기출 (4문제 · 이틀에 1문제)

| 순서 | 제목           | 권장 기간 | 링크                                                                                                                                                                                                                                            |
| ---- | -------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | 단어장         | 목 · 금   | [바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZt8IiBqxEDHBIN6&contestProbId=AZwdOG5aC2rHBIPa&probBoxId=AZt8IiBqxEHHBIN6&type=PROBLEM&problemBoxTitle=B%ED%98%95+%EA%B8%B0%EC%B6%9C&problemBoxCnt=31) |
| 2    | 기계식 주차장  | 토 · 일   | [바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZt8IiBqxEDHBIN6&contestProbId=AZvfGm7qDZ7HBIN6&probBoxId=AZt8IiBqxEHHBIN6&type=PROBLEM&problemBoxTitle=B%ED%98%95+%EA%B8%B0%EC%B6%9C&problemBoxCnt=31) |
| 3    | 타워디펜스게임 | 월 · 화   | [바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZt8IiBqxEDHBIN6&contestProbId=AZvfDDtKDNjHBIN6&probBoxId=AZt8IiBqxEHHBIN6&type=PROBLEM&problemBoxTitle=B%ED%98%95+%EA%B8%B0%EC%B6%9C&problemBoxCnt=31) |
| 4    | 빙하의 이동    | 수 · 목   | [바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZt8IiBqxEDHBIN6&contestProbId=AZve05OqCl3HBIN6&probBoxId=AZt8IiBqxEHHBIN6&type=PROBLEM&problemBoxTitle=B%ED%98%95+%EA%B8%B0%EC%B6%9C&problemBoxCnt=31) |

> 4번 문제는 PR 마감(수요일 밤) 이후에 걸치니, 마감 시점까지 진행한 만큼 커밋하고
> 남은 부분은 세션에서 이야기합니다.

</details>

---

<details>
<summary><h2>4주차 — 해시 + SQL(SELECT) (8문제)</h2></summary>

**출처:** 프로그래머스 코딩테스트 고득점 Kit → 해시 / 프로그래머스 SQL 고득점 Kit → SELECT

4주차는 **문제 수를 줄였습니다.** 대신 두 가지를 새로 시작합니다.

- **해시 세트는 전부** 풉니다 — "무엇을 키로 잡을 것인가"를 반복해서 연습하는 세트입니다
- **SQL 코테 준비 시작** — SELECT 기초 3문제로 가볍게 발을 담급니다

### 코어 문제 ⭐

전원 필수. 세션에서 다 같이 코드를 비교합니다.

| 제목           | 난이도 | 링크                                                                        |
| -------------- | ------ | --------------------------------------------------------------------------- |
| **베스트앨범** | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42579) |

### 프로그래머스 — 해시 (5문제)

| 제목               | 난이도 | 링크                                                                        |
| ------------------ | ------ | --------------------------------------------------------------------------- |
| 완주하지 못한 선수 | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42576) |
| 폰켓몬             | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/1845)  |
| 전화번호 목록      | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42577) |
| 의상               | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42578) |
| 베스트앨범 ⭐      | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42579) |

### 프로그래머스 SQL — SELECT (3문제)

| 제목                          | 난이도 | 링크                                                                         |
| ----------------------------- | ------ | ---------------------------------------------------------------------------- |
| 평균 일일 대여 요금 구하기    | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/151136) |
| 인기있는 아이스크림           | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/133024) |
| 과일로 만든 아이스크림 고르기 | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/133025) |

> SQL 문제는 `.sql` 파일로 제출합니다. 커밋 메시지는 `solve: [SQL Lv1] 인기있는 아이스크림` 형식으로 써주세요.

</details>

---

<details>
<summary><h2>5주차 — 스택/큐 · 힙 + SQL 본격 시작 (9 + 15문제)</h2></summary>

**출처:** 프로그래머스 코딩테스트 고득점 Kit → [스택/큐](https://school.programmers.co.kr/learn/courses/30/parts/12081), [힙](https://school.programmers.co.kr/learn/courses/30/parts/12117) / 프로그래머스 SQL 고득점 Kit → SQL 1주차

- **스택/큐 · 힙 세트는 전부** 풉니다 — "어떤 자료구조를 고르면 O(N²)이 O(N log N)이 되는가"를 보는 세트입니다
- **SQL은 이번 주부터 본격 시작** — SQL 1주차(단일 테이블 기본 조회) 15문제. 전부 Lv1이라 1시간 남짓 걸립니다

### 코어 문제 ⭐

전원 필수. 세션에서 다 같이 코드를 비교합니다.

| 제목                | 난이도 | 링크                                                                        |
| ------------------- | ------ | --------------------------------------------------------------------------- |
| **디스크 컨트롤러** | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42627) |

> 힙을 두 개 굴릴지, 정렬 후 하나만 굴릴지에서 갈립니다. "언제 힙에 넣는가"가 핵심.

<details>
<summary><b>🧩 알고리즘 — 스택/큐 · 힙 (9문제)</b></summary>

### 스택/큐 (6문제)

| 제목               | 난이도 | 링크                                                                        |
| ------------------ | ------ | --------------------------------------------------------------------------- |
| 같은 숫자는 싫어   | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/12906) |
| 기능개발           | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42586) |
| 올바른 괄호        | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/12909) |
| 프로세스           | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42587) |
| 다리를 지나는 트럭 | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42583) |
| 주식가격           | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42584) |

### 힙 (3문제)

| 제목               | 난이도 | 링크                                                                        |
| ------------------ | ------ | --------------------------------------------------------------------------- |
| 더 맵게            | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42626) |
| 디스크 컨트롤러 ⭐ | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42627) |
| 이중우선순위큐     | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42628) |

> Python은 `heapq`가 최소 힙만 지원합니다. `이중우선순위큐`에서 최대값을 뺄 때
> 부호를 뒤집을지, 힙 두 개를 동기화할지가 갈리는 지점입니다.

</details>

<details>
<summary><b>🗄️ SQL 1주차 — 단일 테이블 기본 조회 (15문제)</b></summary>

`SELECT` / `WHERE` / `ORDER BY` / `LIMIT` 만으로 전부 풀립니다.

| 제목                                      | 난이도 | 링크                                                                         |
| ----------------------------------------- | ------ | ---------------------------------------------------------------------------- |
| 모든 레코드 조회하기                      | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/59034)  |
| 역순 정렬하기                             | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/59035)  |
| 동물의 아이디와 이름                      | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/59403)  |
| 아픈 동물 찾기                            | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/59036)  |
| 어린 동물 찾기                            | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/59037)  |
| 여러 기준으로 정렬하기                    | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/59404)  |
| 상위 n개 레코드                           | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/59405)  |
| 조건에 맞는 도서 리스트 출력하기          | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/144853) |
| 12세 이하인 여자 환자 목록 출력하기       | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/132201) |
| 흉부외과 또는 일반외과 의사 목록 출력하기 | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/132203) |
| 강원도에 위치한 생산공장 목록 출력하기    | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/131112) |
| 조건에 부합하는 중고거래 댓글 조회하기    | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/164673) |
| Python 개발자 찾기                        | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/276013) |
| 가장 큰 물고기 10마리 구하기              | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/298517) |
| 특정 형질을 가지는 대장균 찾기            | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/301646) |

> SQL 1주차 세트는 원래 18문제인데, `평균 일일 대여 요금 구하기` · `인기있는 아이스크림` ·
> `과일로 만든 아이스크림 고르기` 3개는 4주차에 이미 풀었으므로 15문제입니다.

**발제 주제 — SQL 실행 순서**

`FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`

이걸 첫 주에 못 박아두면 "WHERE에 별칭을 왜 못 쓰는지", "HAVING과 WHERE의 차이" 같은 질문이 이후 전부 정리됩니다.
`특정 형질을 가지는 대장균 찾기`는 비트 연산(`&`)을 쓰는 유일한 Lv1이라 여기서 짚어두면 나중이 수월합니다.

</details>

</details>

---

<details>
<summary><h2>6주차 — SWEA 커리큘럼 전 범위 (40문제) · 7주차로 이월</h2></summary>

**출처:** SWEA Solving Club → [16기 대전 6반 알고리즘](https://swexpertacademy.com/main/talk/solvingClub/clubDetail.do?solveclubId=AZ9kDS86wCTHBITH)

> ♻️ **이 세트는 7주차로 이월되었습니다.** 팀원 전원이 하반기 기업 서류 마감과 겹쳐 시간을 내기 어려웠습니다.
> 아래 문제 목록은 그대로 유효하니, 진행은 **7주차 섹션**을 기준으로 하세요.

이번 주는 9/15 A형 테스트, 9/19 B형 테스트를 대비하기 위해 **알고리즘에만 집중합니다. SQL은 쉽니다.**

> **제출은 SWEA 사이트 + 레포 둘 다** 입니다. 문제함 제출현황이 세션 체크인 자료가 되니
> 사이트 제출을 빠뜨리지 마세요. 파일명은 평소와 같이 `swea_{번호}_{문제명}.py` 입니다.

> `어디에 단어가 들어갈 수 있을까`(1979) · `농작물 수확하기`(2805) 는 **1주차에 이미 푼 문제**입니다.
> 다시 풀어도 좋고, 1주차 코드를 Solving Club에 제출만 해서 문제함을 채워도 됩니다.

### 코어 문제 ⭐

전원 필수. 세션에서 다 같이 코드를 비교합니다.

| 번호     | 제목                              | 난이도 | 링크                                                                                                      |
| -------- | --------------------------------- | :----: | --------------------------------------------------------------------------------------------------------- |
| **2115** | **[모의 SW 역량테스트] 벌꿀채취** |  모의  | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V4A46AdIDFAWu) |

<details>
<summary><b>🧩 문제함 8개 — 전체 40문제 (펼치기)</b></summary>

#### 알고리즘 기본 (6문제)

| 번호 | 제목                                        | 난이도 | 링크                                                                                                      |
| ---- | ------------------------------------------- | :----: | --------------------------------------------------------------------------------------------------------- |
| 9490 | 풍선팡                                      |   D2   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXAerAPaVXMDFARP) |
| 4834 | [S/W 문제해결 기본] 1일차 - 숫자 카드       |   D2   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTLVouKpUgDFAVT) |
| 4828 | [S/W 문제해결 기본] 1일차 - min max         |   D2   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTLQZwKon4DFAVT) |
| 2001 | 파리 퇴치                                   |   D2   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq) |
| 1979 | 어디에 단어가 들어갈 수 있을까 (1주차 중복) |   D2   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq) |
| 1961 | 숫자 배열 회전                              |   D2   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq) |

> D2 워밍업 세트입니다. `파리 퇴치` · `풍선팡` 은 델타 배열을 어떻게 잡는지만 보고 빠르게 넘어가세요.

<sub>[문제함 바로가기 · 제출현황](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kDS86wCXHBITH&leftPage=1)</sub>

#### 재귀 (4문제)

| 번호 | 제목                                 | 난이도 | 링크                                                                                                      |
| ---- | ------------------------------------ | :----: | --------------------------------------------------------------------------------------------------------- |
| 6808 | 규영이와 인영이의 카드게임           |   D3   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWgv9va6HnkDFAW0) |
| 4836 | [S/W 문제해결 기본] 2일차 - 색칠하기 |   D2   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTLZMRKpsYDFAVT) |
| 2805 | 농작물 수확하기 (1주차 중복)         |   D3   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB) |
| 1210 | [S/W 문제해결 기본] 2일차 - Ladder1  |   D4   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh) |

> `Ladder1` 은 재귀로도 역추적으로도 풀립니다. `규영이와 인영이의 카드게임` 은 순열 + 재귀가 붙는 첫 문제입니다.

<sub>[문제함 바로가기 · 제출현황](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawC3HBITH&leftPage=1)</sub>

#### 순열과 조합 (5문제)

| 번호 | 제목                                          | 난이도 | 링크                                                                                                      |
| ---- | --------------------------------------------- | :----: | --------------------------------------------------------------------------------------------------------- |
| 4831 | [S/W 문제해결 기본] 1일차 - 전기버스          |   D3   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTLS24ao9ADFAVT) |
| 4014 | [모의 SW 역량테스트] 활주로 건설              |  모의  | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeW7FakkUDFAVH) |
| 4012 | [모의 SW 역량테스트] 요리사                   |  모의  | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH) |
| 2382 | [모의 SW 역량테스트] 미생물 격리              |  모의  | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV597vbqAH0DFAVl) |
| 1240 | [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드 |   D3   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15FZuqAL4CFAYD) |

> `요리사` 는 조합, `활주로 건설` 은 부분집합, `미생물 격리` 는 시뮬레이션입니다. **같은 문제함 안에서 쓰는 도구가 다릅니다.**

<sub>[문제함 바로가기 · 제출현황](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawC7HBITH&leftPage=1)</sub>

#### 스택과 큐 (5문제)

| 번호 | 제목                                   | 난이도 | 링크                                                                                                      |
| ---- | -------------------------------------- | :----: | --------------------------------------------------------------------------------------------------------- |
| 5432 | 쇠막대기 자르기                        |   D4   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVl47b6DGMDFAXm) |
| 2477 | [모의 SW 역량테스트] 차량 정비소       |  모의  | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV6c6bgaIuoDFAXy) |
| 1225 | [S/W 문제해결 기본] 7일차 - 암호생성기 |   D3   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14uWl6AF0CFAYD) |
| 1222 | [S/W 문제해결 기본] 6일차 - 계산기1    |   D4   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14mbSaAEwCFAYD) |
| 1220 | [S/W 문제해결 기본] 5일차 - Magnetic   |   D3   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14hwZqABsCFAYD) |

> `계산기1` 은 중위 → 후위 변환, `Magnetic` 은 스택을 안 써도 풀리는 문제입니다. 후자는 "왜 스택 문제함에 있는가"를 같이 이야기해 볼 만합니다.

<sub>[문제함 바로가기 · 제출현황](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawC_HBITH&leftPage=1)</sub>

#### 트리와 그래프 (4문제)

| 번호 | 제목                                  | 난이도 | 링크                                                                                                      |
| ---- | ------------------------------------- | :----: | --------------------------------------------------------------------------------------------------------- |
| 5178 | [S/W 문제해결 기본] 8일차 - 노드의 합 |   D3   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTa2VIq4mYDFAVT) |
| 5176 | [S/W 문제해결 기본] 8일차 - 이진탐색  |   D2   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTa0jjq4ggDFAVT) |
| 1232 | [S/W 문제해결 기본] 9일차 - 사칙연산  |   D4   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV141J8KAIcCFAYD) |
| 1231 | [S/W 문제해결 기본] 9일차 - 중위순회  |   D4   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV140YnqAIECFAYD) |

> 배열로 트리를 표현하는 연습 세트입니다. `사칙연산` 은 후위 순회로 계산하는 문제라 6일차 `계산기1` 과 짝으로 보면 좋습니다.

<sub>[문제함 바로가기 · 제출현황](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawDDHBITH&leftPage=1)</sub>

#### DFS (6문제)

| 번호 | 제목                                  | 난이도 | 링크                                                                                                      |
| ---- | ------------------------------------- | :----: | --------------------------------------------------------------------------------------------------------- |
| 4008 | [모의 SW 역량테스트] 숫자 만들기      |  모의  | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeRZV6kBUDFAVH) |
| 2819 | 격자판의 숫자 이어 붙이기             |   D4   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB) |
| 2115 | [모의 SW 역량테스트] 벌꿀채취 ⭐      |  모의  | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V4A46AdIDFAWu) |
| 1865 | 동철이의 일 분배                      |   D4   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LuHfqDz8DFAXc) |
| 1486 | 장훈이의 높은 선반                    |   D4   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b7Yf6ABcBBASw) |
| 1244 | [S/W 문제해결 응용] 2일차 - 최대 상금 |   D3   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD) |

> 모의 역량테스트 문제가 3개라 이번 주 체감 난이도의 대부분이 여기에 있습니다. 시간을 넉넉히 잡으세요.

<sub>[문제함 바로가기 · 제출현황](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawDHHBITH&leftPage=1)</sub>

#### BFS (5문제)

| 번호 | 제목                                 | 난이도 | 링크                                                                                                      |
| ---- | ------------------------------------ | :----: | --------------------------------------------------------------------------------------------------------- |
| 1953 | [모의 SW 역량테스트] 탈주범 검거     |  모의  | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq) |
| 1249 | [S/W 문제해결 응용] 4일차 - 보급로   |   D4   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD) |
| 1238 | [S/W 문제해결 기본] 10일차 - Contact |   D4   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD) |
| 1227 | [S/W 문제해결 기본] 7일차 - 미로2    |   D4   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14wL9KAGkCFAYD) |
| 1226 | [S/W 문제해결 기본] 7일차 - 미로1    |   D4   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14vXUqAGMCFAYD) |

> `미로1` → `미로2` → `보급로` 순으로 풀면 "단순 도달 판정 → 최단거리 → 가중치" 로 자연스럽게 올라갑니다. `보급로` 는 BFS로는 안 되고 다익스트라가 필요합니다.

<sub>[문제함 바로가기 · 제출현황](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawDLHBITH&leftPage=1)</sub>

#### heap과 BackTracking (5문제)

| 번호 | 제목                                 | 난이도 | 링크                                                                                                      |
| ---- | ------------------------------------ | :----: | --------------------------------------------------------------------------------------------------------- |
| 9280 | 진용이네 주차타워                    |   D3   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AW9j74FacD0DFAUY) |
| 5215 | 햄버거 다이어트                      |   D3   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWT-lPB6dHUDFAVT) |
| 5189 | [S/W 문제해결 구현] 2일차 - 전자카트 |   D3   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTtmmdKeD8DFAVT) |
| 2930 | 힙                                   |   D3   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV-Tj7ya3jYDFAXr) |
| 2817 | 부분 수열의 합                       |   D3   | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7IzvG6EksDFAXB) |

> `부분 수열의 합` · `햄버거 다이어트` 는 백트래킹, `힙` · `전자카트` 는 자료구조 문제입니다. `진용이네 주차타워` 는 그리디에 가깝습니다.

<sub>[문제함 바로가기 · 제출현황](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawDPHBITH&leftPage=1)</sub>

</details>

<details>
<summary><b>🗄️ SQL — 이번 주는 쉽니다</b></summary>

6주차는 SQL을 넣지 않습니다. SWEA 40문제와 SQL 13문제를 같은 주에 얹으면 둘 다 건성으로 하게 됩니다.

**SQL 2주차(집계 함수, 13문제)는 8주차로 밀립니다.** (6주차 세트가 7주차로 이월되면서 한 주 더 밀렸습니다.)
위 [SQL 트랙](#sql-트랙) 섹션의 매핑 표를 두 주씩 조정했습니다. 주제 순서는 그대로입니다.

</details>

</details>

---

<details>
<summary><h2>7주차 — SWEA 커리큘럼 완주 (6주차 이월 40문제 + 신규 문제함 7개)</h2></summary>

**출처:** SWEA Solving Club → [16기 대전 6반 알고리즘](https://swexpertacademy.com/main/talk/solvingClub/clubDetail.do?solveclubId=AZ9kDS86wCTHBITH)

6주차는 팀원 전원이 **하반기 기업 서류 마감**과 겹쳐 시간을 내기 어려웠습니다.
그래서 6주차 세트(문제함 8개 · 40문제)를 **7주차로 이월**하고, 남은 문제함 7개를 더해
이번 주에 **Solving Club 커리큘럼 15개 문제함을 전부** 마무리합니다.

> ⚠️ **분량이 큽니다. 다 못 푸는 게 기본값입니다.**
> 이월분은 **6주차에 못 푼 것만** 채우면 되고, 이번 주의 메인은 신규 7개 문제함입니다.
> 규칙 4번(_다 못 풀어도 세션에 옵니다_)이 이번 주에 제일 중요합니다. 어디까지 갔는지만 PR에 적어주세요.

> **제출은 SWEA 사이트 + 레포 둘 다** 입니다. 문제함 제출현황이 세션 체크인 자료가 됩니다.
> 6주차에 이미 푼 코드는 `week-06` 폴더에 둔 그대로 두고, **이번 주에 새로 푼 것만 `week-07`** 에 올립니다.
> 파일명은 평소와 같이 `swea_{번호}_{문제명}.py` 입니다.

### 코어 문제 ⭐

6주차 코어 문제를 그대로 가져갑니다. 아직 다 같이 못 봤습니다.

| 번호     | 제목                              | 난이도 | 링크                                                                                                      |
| -------- | --------------------------------- | :----: | --------------------------------------------------------------------------------------------------------- |
| **2115** | **[모의 SW 역량테스트] 벌꿀채취** |  모의  | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V4A46AdIDFAWu) |

### 이번 주 우선순위

1. **코어 문제** (2115 벌꿀채취) — 전원 필수
2. **신규 문제함 7개** — 이번 주 메인. 위에서 아래 순서대로 푸세요
3. **6주차 이월분** — 못 푼 것 위주로, 남는 시간에

<details>
<summary><b>🆕 신규 문제함 7개 (펼치기)</b></summary>

문제함 이름은 SWEA 사이트 표기 그대로입니다.

| 문제함                    | 다루는 것                                                                            | 링크                                                                                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Greedy Algorithm**      | 정렬한 뒤 앞에서부터 집기. "왜 그 선택이 최적인가"를 말로 설명할 수 있어야 하는 유형 | [문제함 바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawDTHBITH&leftPage=1) |
| **Disjoint Set**          | Union-Find. 경로 압축 · union by rank 까지 한 번에 익히고 넘어가기                   | [문제함 바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawDXHBITH&leftPage=1) |
| **Minimum Spanning Tree** | 크루스칼(정렬 + Union-Find) · 프림(heap). Disjoint Set 이 그대로 재료로 쓰입니다     | [문제함 바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawDbHBITH&leftPage=2) |
| **Short Path**            | 다익스트라 · 플로이드 워셜. "간선 가중치가 있으면 BFS로 안 된다"를 확인하는 세트     | [문제함 바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawDfHBITH&leftPage=2) |
| **Dinamic Programming**   | 점화식 세우기. 메모이제이션(재귀) ↔ 타뷸레이션(반복) 둘 다 써보기                    | [문제함 바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawDjHBITH&leftPage=2) |
| **Sort**                  | 정렬 알고리즘 직접 구현 + 정렬을 전처리로 쓰는 문제                                  | [문제함 바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawDnHBITH&leftPage=2) |
| **Extra**                 | 앞 문제함에 안 들어간 나머지. 유형이 안 적혀 있으니 "무슨 유형인지 맞히기" 부터      | [문제함 바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawDrHBITH&leftPage=2) |

> **순서를 지켜서 푸세요.** `Disjoint Set` → `Minimum Spanning Tree` 는 앞이 뒤의 재료이고,
> 6주차 BFS 문제함의 `보급로` 에서 "BFS로는 안 되고 다익스트라가 필요했던" 이유가 `Short Path` 에서 정리됩니다.

> 문제함 상세 목록은 Solving Club 로그인이 필요해 여기에 옮겨두지 못했습니다.
> 문제 수와 목록은 각 문제함 링크에서 확인하세요.

</details>

<details>
<summary><b>♻️ 6주차 이월 — 문제함 8개 · 40문제 (펼치기)</b></summary>

문제 목록은 위 **6주차 섹션**을 펼치면 그대로 있습니다. 여기서는 문제함만 정리합니다.

| 문제함              | 문제 수 | 링크                                                                                                                                                        |
| ------------------- | :-----: | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 알고리즘 기본       |    6    | [문제함 바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kDS86wCXHBITH&leftPage=1) |
| 재귀                |    4    | [문제함 바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawC3HBITH&leftPage=1) |
| 순열과 조합         |    5    | [문제함 바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawC7HBITH&leftPage=1) |
| 스택과 큐           |    5    | [문제함 바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawC_HBITH&leftPage=1) |
| 트리와 그래프       |    4    | [문제함 바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawDDHBITH&leftPage=1) |
| DFS                 |    6    | [문제함 바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawDHHBITH&leftPage=1) |
| BFS                 |    5    | [문제함 바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawDLHBITH&leftPage=1) |
| heap과 BackTracking |    5    | [문제함 바로가기](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawDPHBITH&leftPage=1) |

> `어디에 단어가 들어갈 수 있을까`(1979) · `농작물 수확하기`(2805) 는 **1주차에 이미 푼 문제**입니다.
> 1주차 코드를 Solving Club에 제출만 해서 문제함을 채워도 됩니다.

</details>

<details>
<summary><b>🗄️ SQL — 이번 주도 쉽니다</b></summary>

7주차도 SQL을 넣지 않습니다. 이월분까지 얹힌 주에 SQL 13문제를 더하면 둘 다 건성으로 하게 됩니다.

**SQL 2주차(집계 함수, 13문제)는 8주차로 밀립니다.** 위 [SQL 트랙](#sql-트랙) 섹션의 매핑 표를 조정했습니다.
주제 순서는 그대로입니다.

여유 있는 사람은 `SUM` / `AVG` / `COUNT` / `MAX` / `MIN` 이 `NULL` 을 어떻게 다루는지만 미리 봐두면
8주차가 훨씬 수월합니다. (`COUNT(*)` 와 `COUNT(컬럼)` 이 다른 값을 돌려주는 이유)

</details>

</details>

---

<details>
<summary><h2>8주차 — 기출 (알고리즘 4 + SQL 1문제)</h2></summary>

**출처:** 2026 하반기 코딩테스트 기출 복원

7주차로 SWEA 커리큘럼을 마쳤으니, 이번 주는 **실제 코딩테스트에 나온 문제**를 풉니다.
문제 수는 적지만 **시험처럼 푸는 게 목표**입니다. 문제당 시간을 재고, PR에 소요 시간을 적어주세요.

> 🔒 **출처는 공개하지 않습니다.** 문제 복원본이라 출처명을 README · PR · 커밋 메시지 · 파일명 어디에도 적지 마세요.
> 온라인 저지 링크가 없어서 **문제 본문을 아래에 옮겨두었습니다.** 예시 입출력으로 직접 확인하세요.

> **파일명**은 `pub_{번호}_{문제명}.py` (SQL은 `.sql`) 입니다. 예: `pub_1_타일뒤집기.py`, `pub_5_결제실패조회.sql`
> 커밋 메시지는 `solve: [기출 1] 타일 뒤집기` 형식으로 써주세요.

### 코어 문제 ⭐

전원 필수. 세션에서 다 같이 코드를 비교합니다.

| 번호  | 제목            | 유형     |
| :---: | --------------- | -------- |
| **1** | **타일 뒤집기** | 알고리즘 |

### 문제 목록

| 번호 | 제목               | 유형     |
| :--: | ------------------ | -------- |
|  1   | 타일 뒤집기 ⭐     | 알고리즘 |
|  2   | 최대 점수 차       | 알고리즘 |
|  3   | 정상 거래 개수     | 알고리즘 |
|  4   | 행동 우선순위 처리 | 알고리즘 |
|  5   | 결제 실패 조회     | SQL      |

<details>
<summary><b>1. 타일 뒤집기 ⭐</b></summary>

우주선 외벽에는 총 `n` 개의 양면 타일이 있습니다. 각 타일은 다음 두 면 중 하나가 바깥을 향합니다.

- **H 면**: `h1` 도 이상 `h2` 도 이하의 온도를 견딤
- **C 면**: `c1` 도 이상 `c2` 도 이하의 온도를 견딤

현재 H 면이 `a` 개, C 면이 `b` 개라면 `a + b = n` 이고, 우주선이 견딜 수 있는 온도 범위는 다음과 같습니다.

```
(h1 × a + c1 × b) / n  ~  (h2 × a + c2 × b) / n
```

우주선은 `temperature` 에 주어진 온도를 순서대로 지나갑니다.
각 온도에서 우주선이 해당 온도를 견딜 수 있도록 타일을 뒤집어야 하며, 타일 하나를 뒤집는 데 1회의 조작이 필요합니다.
처음에는 모든 타일의 H 면이 바깥을 향하고 있습니다.

모든 온도를 안전하게 통과하기 위해 필요한 **최소 타일 뒤집기 횟수**를 구하세요.

**예시**

| n   | h1  | h2  | c1  | c2  | temperature                  | result |
| --- | --- | --- | --- | --- | ---------------------------- | :----: |
| 10  | 0   | 50  | -50 | 0   | `[30, -20, -5, 10, 31, -50]` |   12   |

</details>

<details>
<summary><b>2. 최대 점수 차</b></summary>

여러 팀이 경기를 진행하고 있습니다. 각 팀의 최초 점수는 모두 0점입니다.
경기 중 발생한 득점 정보가 2차원 배열 `scores` 에 `[팀 번호, 획득 점수]` 형태로 순서대로 주어집니다.

각 득점이 발생할 때마다 해당 팀의 점수에 획득한 점수를 누적하고,
그 후 모든 팀의 현재 점수 중 **최댓값과 최솟값의 차이**를 계산합니다.

경기가 진행되는 동안 발생한 점수 차 중 **가장 큰 값**을 반환하세요.

**예시**

```
scores = [[1, 2], [2, 3], [3, 1], [4, 5], [2, 3], [1, 4]]

초기       : [0, 0, 0, 0]
[1, 2]    : [2, 0, 0, 0] → 차이 2
[2, 3]    : [2, 3, 0, 0] → 차이 3
[3, 1]    : [2, 3, 1, 0] → 차이 3
[4, 5]    : [2, 3, 1, 5] → 차이 4
[2, 3]    : [2, 6, 1, 5] → 차이 5
[1, 4]    : [6, 6, 1, 5] → 차이 5

result = 5
```

</details>

<details>
<summary><b>3. 정상 거래 개수</b></summary>

각 거래 정보는 길이 4의 배열 `[약정 증권 수량, 전달된 증권 수량, 약정 대금, 지급된 대금]` 으로 주어집니다.

다음 두 조건을 **모두** 만족하면 해당 거래가 정상적으로 처리된 것으로 판단합니다.

- 약정 증권 수량과 전달된 증권 수량이 같다.
- 약정 대금과 지급된 대금이 같다.

거래 정보가 담긴 2차원 정수 배열 `transactions` 가 주어질 때, 정상적으로 처리된 거래의 개수를 반환하세요.

**예시**

```
transactions = [
    [100, 100, 5000, 5000],
    [200, 190, 8000, 8000],
    [150, 150, 7000, 6900],
    [300, 300, 12000, 12000]
]

result = 2   # 첫 번째와 네 번째 거래만 수량과 대금이 모두 일치
```

</details>

<details>
<summary><b>4. 행동 우선순위 처리</b></summary>

게임 캐릭터에게 수행할 행동 명령이 `actions` 배열로 주어집니다.
각 행동은 `[주문 시간, 우선순위, 행동 시간]` 형태입니다.

- **주문 시간**: 행동이 요청되는 시각
- **우선순위**: 숫자가 작을수록 우선순위가 높다. 모든 행동의 우선순위는 서로 다르다.
- **행동 시간**: 행동을 완료하는 데 필요한 시간

캐릭터가 아무 행동도 수행하지 않을 때 주문이 들어오면 즉시 해당 행동을 시작합니다.
행동 수행 중 새로운 주문이 들어오면 다음 규칙을 따릅니다.

- 새로운 행동의 우선순위가 **더 높으면** 현재 행동을 중단하고 새로운 행동을 시작한다. 중단된 행동은 다시 수행하지 않는다.
- 새로운 행동의 우선순위가 **더 낮으면** 새로운 행동을 버린다.
- 행동을 끝까지 수행하면 해결한 것으로 처리한다.

모든 주문을 처리한 뒤 `[중단된 행동 수, 해결한 행동 수, 버린 행동 수]` 를 반환하세요.

**예시**

```
actions = [[0, 4, 5], [2, 1, 3], [3, 5, 2], [7, 2, 2]]

result = [1, 2, 1]
```

</details>

<details>
<summary><b>5. 결제 실패 조회 (SQL)</b></summary>

결제 예정 정보를 담은 `PAYMENTS` 테이블과 실제 결제 시도 내역을 담은 `PAYMENT_ATTEMPTS` 테이블이 있습니다.

**PAYMENTS**

| PAYMENT_ID | SCHEDULED_DATE |
| ---------- | -------------- |
| 01         | 2026-09-01     |
| 02         | 2026-09-03     |
| 03         | 2026-09-05     |
| 04         | 2026-09-07     |
| 05         | 2026-09-10     |

**PAYMENT_ATTEMPTS**

| PAYMENT_ID | ATTEMPT_ID | PAYMENT_DATE | STATUS  |
| ---------- | ---------- | ------------ | ------- |
| 01         | 1          | 2026-09-01   | SUCCESS |
| 02         | 2          | 2026-09-02   | FAIL    |
| 02         | 3          | 2026-09-03   | FAIL    |
| 04         | 4          | 2026-09-06   | FAIL    |
| 04         | 5          | 2026-09-08   | SUCCESS |
| 05         | 6          | 2026-09-08   | FAIL    |
| 05         | 7          | 2026-09-10   | SUCCESS |

결제 예정일 **이전 또는 당일에 SUCCESS** 한 결제만 정상적으로 완료된 결제로 판단합니다.
다음과 같은 경우에는 실패한 결제로 판단합니다.

- 결제 예정일까지 시도한 결제가 모두 FAIL 인 경우
- 결제 시도 자체가 없는 경우
- SUCCESS 기록이 있더라도 결제 예정일보다 늦게 성공한 경우

실패한 모든 `PAYMENT_ID` 를 조회하세요. 결과는 `PAYMENT_ID` 기준 **내림차순** 정렬합니다.

**실행 결과**

| PAYMENT_ID |
| ---------- |
| 04         |
| 03         |
| 02         |

> 01 · 05는 예정일 당일에 성공해서 정상, 02는 전부 실패, 03은 시도 없음, 04는 예정일 이후 성공이라 실패입니다.

</details>

<details>
<summary><b>🗄️ SQL 트랙 — 이번 주도 쉽니다</b></summary>

**SQL 2주차(집계 함수, 13문제)는 9주차로 밀립니다.** 위 [SQL 트랙](#sql-트랙) 섹션의 매핑 표를 조정했습니다.
주제 순서는 그대로입니다. 기출 5번이 SQL이라 SQL 감각은 이번 주에도 이어집니다.

</details>

</details>

---

<details open>
<summary><h2>9주차 — 코테 복기 + 기출 (알고리즘 5 + SQL 2문제)</h2></summary>

**출처:** 2026 하반기 기업 코딩테스트 응시 복기 / 8주차 기출 세트에서 다루지 않은 문제

이번 주도 기출 주간입니다. 두 묶음으로 나뉩니다.

- **코테 복기 (1~3번)** — 팀원이 직접 응시하고 복원한 문제입니다. 기억에 의존한 복원이라 **원문과 세부 표현이 다를 수 있습니다.**
- **기출 (4~7번)** — 8주차와 같은 출처에서, 지난주에 풀지 않은 알고리즘 2문제 + SQL 2문제입니다.

8주차처럼 **시험처럼 푸는 게 목표**입니다. 문제당 시간을 재고, PR에 소요 시간을 적어주세요.

> 🔒 **출처는 공개하지 않습니다.** 출처명을 README · PR · 커밋 메시지 · 파일명 어디에도 적지 마세요.
> 온라인 저지 링크가 없어서 **문제 본문을 아래에 옮겨두었습니다.** 예시 입출력으로 직접 확인하세요.

> **파일명**은 복기 문제는 `rev_{번호}_{문제명}.py`, 기출은 8주차와 같이 `pub_{번호}_{문제명}.py` (SQL은 `.sql`) 입니다.
> 예: `rev_2_로봇청소기커버리지.py`, `pub_4_피아노음높이변환.py`, `pub_7_최대조개수.sql`
> 커밋 메시지는 `solve: [복기 2] 로봇청소기 커버리지`, `solve: [기출 4] 피아노 음높이 변환` 형식으로 써주세요.

### 코어 문제 ⭐

전원 필수. 세션에서 다 같이 코드를 비교합니다.

| 번호  | 제목                    | 유형     |
| :---: | ----------------------- | -------- |
| **2** | **로봇청소기 커버리지** | 알고리즘 |

> 로봇이 최대 30대입니다. 로봇마다 따로 탐색해도 되는지, 한 번에 처리할 수 있는지부터 따져보고 들어가세요.

### 문제 목록

| 번호 | 제목                   | 구분      | 유형     |
| :--: | ---------------------- | --------- | -------- |
|  1   | 가위바위보 전파        | 코테 복기 | 알고리즘 |
|  2   | 로봇청소기 커버리지 ⭐ | 코테 복기 | 알고리즘 |
|  3   | 함정 피해 멀리 가기    | 코테 복기 | 알고리즘 |
|  4   | 피아노 음높이 변환     | 기출      | 알고리즘 |
|  5   | 포화 N진 트리의 레벨   | 기출      | 알고리즘 |
|  6   | 달러 거래 손익         | 기출      | SQL      |
|  7   | 최대 조 개수           | 기출      | SQL      |

<details>
<summary><b>1. 가위바위보 전파</b></summary>

`1` 번부터 `N` 번까지 노드가 있고, 각 노드는 **다른 노드 하나를 가리킵니다.** `points[i]` 는 `i+1` 번 노드가 가리키는 노드 번호입니다.

모든 노드는 가위·바위·보 중 하나의 속성을 가집니다. `arr[i]` 가 `i+1` 번 노드의 속성이고, `1` 은 가위, `2` 는 바위, `3` 은 보입니다.

매초, 각 노드는 **자신을 가리키는 노드들**을 살펴봅니다. 그중 자신을 이기는 속성이 있다면 그 속성으로 바뀝니다.
예를 들어 1번이 2번을 가리키고 1번이 바위, 2번이 가위라면 2번은 바위가 됩니다.

한 초 안에서 **모든 노드의 변화는 동시에** 일어납니다. 앞 노드가 바뀐 결과가 같은 초의 뒤 노드 판정에 영향을 주지 않습니다.

`T` 초가 지난 뒤의 `arr` 을 반환하세요.

**제한**

- `1 ≤ N ≤ 5,000`
- `1 ≤ T ≤ 50`
- `points` 는 1부터 시작하는 번호이며 자기 자신을 가리킬 수 있습니다.
- `arr[i] ∈ {1, 2, 3}`

**예시**

| points         | arr            |  T  | result         |
| -------------- | -------------- | :-: | -------------- |
| `[2, 1, 4, 3]` | `[2, 1, 3, 1]` |  1  | `[2, 2, 1, 1]` |
| `[2, 3, 1]`    | `[2, 1, 3]`    |  3  | `[2, 1, 3]`    |

> 두 번째 예제는 주기 3으로 진동해서 3초 뒤 처음 상태로 돌아옵니다.

</details>

<details>
<summary><b>2. 로봇청소기 커버리지 ⭐</b></summary>

`n × n` 크기의 사무실이 있습니다. 칸의 좌표는 `(행, 열)` 이고 각각 `1` 부터 `n` 까지입니다.

`robots` 에는 로봇청소기가 놓인 칸들이 `[행, 열]` 형태로 주어집니다.

`walls` 의 각 원소 `[r1, c1, r2, c2]` 는 인접한 두 칸 `(r1, c1)` 과 `(r2, c2)` **사이에 벽이 있다**는 뜻입니다. 벽이 있으면 두 칸 사이를 오갈 수 없습니다.

로봇청소기는 상하좌우로만 이동하며, 거리 `q` 만큼 청소할 수 있습니다.
즉 어떤 로봇에서 벽을 통과하지 않고 `q` 칸 이내로 갈 수 있는 칸은 청소됩니다.

**사무실의 모든 칸이 청소되려면 `q` 가 최소 얼마여야 하는지** 구하세요.

**제한**

- `1 ≤ n ≤ 100`
- `1 ≤ robots.length ≤ 30`
- 대각선 이동은 불가능합니다.
- 모든 칸은 어떤 로봇에서든 도달 가능함이 보장됩니다.
- 반환값은 정수입니다.

**예시**

| n   | robots                         | walls     | result |
| --- | ------------------------------ | --------- | :----: |
| 3   | `[[1, 1]]`                     | `[]`      |   4    |
| 5   | `[[1, 1], [5, 5]]`             | `[]`      |   4    |
| 8   | `[[1,1], [1,8], [8,1], [8,8]]` | 아래 참고 |   8    |

```
walls = [[3,4,4,4], [3,5,4,5], [5,4,6,4], [5,5,6,5],
         [4,3,4,4], [5,3,5,4], [4,5,4,6],
         [2,2,2,3], [2,6,2,7], [7,2,7,3], [7,6,7,7],
         [1,4,1,5], [8,4,8,5]]
```

> 첫 예제는 (1,1)에서 (3,3)까지 4칸이 가장 멉니다.
> 세 번째 예제는 가운데 2×2 구역 (4,4)~(5,5)가 벽으로 둘러싸여 있고 (5,5) 오른쪽에만 틈이 있습니다.
> 로봇이 네 귀퉁이에 다 있어도 그 틈으로 빙 돌아 들어가야 해서 (4,4)가 8칸으로 가장 멉니다.

</details>

<details>
<summary><b>3. 함정 피해 멀리 가기</b></summary>

말이 `0` 번 칸에서 출발합니다. 주사위는 `1` 부터 `n` 까지의 눈을 가지고 있고,
`n + 1` 의 배수인 칸(`n+1`, `2(n+1)`, …)은 **함정 칸**입니다.
함정 칸에 도착하면 즉시 `0` 번 칸으로 돌아갑니다. 출발점 `0` 은 함정이 아닙니다.

`rolls` 에는 매 턴 나온 주사위 눈이 순서대로 주어집니다. 각 턴마다 둘 중 하나를 고를 수 있습니다.

- `rolls[i]` 만큼 앞으로 이동한다
- 출발점 `0` 번 칸으로 돌아간다

모든 턴이 끝났을 때 그 자리에 있을 필요는 없습니다. **도달할 수 있는 안전 칸 중 제일 먼 칸의 번호**를 구하세요.

**제한**

- `1 ≤ rolls.length ≤ 500,000`
- `1 ≤ n ≤ 6` — 주사위의 눈금 수입니다.
- `1 ≤ rolls[i] ≤ n`

**예시**

| rolls                            |  n  | result |
| -------------------------------- | :-: | :----: |
| `[2, 3, 4, 2, 2]`                |  4  |   11   |
| `[2, 2, 2]`                      |  2  |   4    |
| `[3, 1, 4, 1, 5, 2, 6, 5, 3, 5]` |  6  |   32   |

> 첫 예제는 함정이 5, 10, 15…입니다. 첫 턴을 버리고 3+4+2+2를 이어서 받으면 11에 도달합니다.
> 두 번째 예제는 함정이 3, 6, 9인데, 2를 두 번 받으면 함정 3을 뛰어넘어 4까지 갑니다. 한 번 더 받으면 6이라 거기서 멈춰야 합니다.
> 세 번째 예제는 첫 눈 3만 버리면 남은 아홉 번을 한 번도 함정을 밟지 않고 이어 받아 32까지 갑니다.

</details>

<details>
<summary><b>4. 피아노 음높이 변환</b></summary>

피아노의 음은 `C0` 부터 `B7` 까지 존재하며, 한 옥타브의 음 순서는 다음과 같습니다.

```
C, C#, D, D#, E, F, F#, G, G#, A, A#, B
```

`E#` 과 `B#` 은 존재하지 않습니다.

문자열 배열 `notes` 와 0이 아닌 정수 `K` 가 주어집니다. 각 음에 대해 `K` 만큼 음높이를 이동합니다.

- `K > 0` 이면 음을 `K` 칸 **낮춥니다.**
- `K < 0` 이면 음을 `|K|` 칸 **높입니다.**
- `C0` 보다 낮아지는 경우 `C0` 으로 고정합니다.
- `B7` 보다 높아지는 경우 `B7` 으로 고정합니다.

변환된 음을 문자열 배열로 반환하세요.

**예시**

| notes                        |  K  | result                      |
| ---------------------------- | :-: | --------------------------- |
| `["C4", "D4", "E4"]`         |  1  | `["B3", "C#4", "D#4"]`      |
| `["C0", "C#0", "C1", "C#1"]` |  2  | `["C0", "C0", "A#0", "B0"]` |

</details>

<details>
<summary><b>5. 포화 N진 트리의 레벨</b></summary>

`0` 부터 `v-1` 까지 서로 다른 번호를 가진 `v` 개의 노드로 이루어진 **포화 N진 트리**가 있습니다.
포화 N진 트리에서 자식을 가지는 모든 노드는 동일한 개수의 자식을 가집니다.

트리의 간선 정보를 담은 2차원 정수 배열 `edges` 가 주어집니다.
`edges[i] = [a, b]` 는 노드 `a` 와 노드 `b` 가 연결되어 있음을 의미하며, **부모와 자식의 방향은 주어지지 않습니다.**

루트 노드의 레벨을 `1` 이라고 할 때, 각 노드의 레벨을 **노드 번호 순서대로** 배열에 담아 반환하세요.

**예시 1**

```
v = 7
edges = [[3,4], [4,0], [2,1], [6,1], [1,3], [4,5]]

        3
      /   \
     1     4
    / \   / \
   2   6 0   5

result = [3, 2, 3, 1, 2, 3, 3]
```

**예시 2**

```
v = 5
edges = [[1,0], [1,2], [3,1], [4,1]]

       1
    / / \ \
   0 2   3 4

result = [2, 1, 2, 2, 2]
```

</details>

<details>
<summary><b>6. 달러 거래 손익 (SQL)</b></summary>

사용자들의 달러 거래 내역을 담은 `USD_TABLES` 테이블이 있습니다.

| Column name | Type    | Nullable |
| ----------- | ------- | -------- |
| USER_ID     | INTEGER | FALSE    |
| TRADE_SEQ   | INTEGER | FALSE    |
| TRADE_TYPE  | VARCHAR | FALSE    |
| RATE        | INTEGER | FALSE    |

- `USER_ID` 와 `TRADE_SEQ` 의 조합이 기본 키입니다.
- `TRADE_TYPE` 은 `BUY`(달러 매수) 또는 `SELL`(달러 매도) 중 하나입니다.
- `TRADE_SEQ` 가 작을수록 먼저 발생한 거래이며, 모든 거래 금액은 **100달러로 고정**되어 있습니다.

사용자가 달러를 매도할 때는 아직 매도하지 않은 달러 중 **가장 오래전에 매수한 거래부터 판매**합니다. 즉, 선입선출(FIFO) 방식으로 매수와 매도를 매칭합니다.
모든 `SELL` 거래가 발생하는 시점에는 해당 사용자가 이전에 매수하고 아직 매도하지 않은 100달러가 최소 한 건 이상 존재합니다.

한 번의 매도 거래에서 발생한 손익은 다음과 같습니다.

```
(매도 당시 환율 - 매칭된 매수 당시 환율) × 100
```

사용자별로 다음 값을 조회하세요.

- `PROFIT` : 모든 매도 거래에서 발생한 손익의 합
- `PROFIT_COUNT` : 손익이 0보다 큰 매도 거래의 수 (손익이 0인 거래는 포함하지 않음)

아직 매도 거래를 하지 않은 사용자도 결과에 포함하며, 이 경우 `PROFIT` 과 `PROFIT_COUNT` 를 모두 `0` 으로 출력합니다.
출력 컬럼은 `USER_ID, PROFIT, PROFIT_COUNT` 이고, 결과는 `USER_ID` 기준 **내림차순** 정렬합니다.

**USD_TABLES**

| USER_ID | TRADE_SEQ | TRADE_TYPE | RATE |
| ------- | --------- | ---------- | ---- |
| 1       | 1         | BUY        | 1300 |
| 1       | 2         | BUY        | 1350 |
| 1       | 3         | SELL       | 1400 |
| 1       | 4         | BUY        | 1280 |
| 1       | 5         | SELL       | 1320 |
| 2       | 1         | BUY        | 1400 |
| 2       | 2         | SELL       | 1350 |
| 3       | 1         | BUY        | 1290 |
| 3       | 2         | BUY        | 1310 |
| 4       | 1         | BUY        | 1250 |
| 4       | 2         | SELL       | 1250 |

사용자 1은 FIFO에 따라 다음과 같이 매칭됩니다.

| SELL         | 매수 환율 | 매도 환율 | 손익  |
| ------------ | :-------: | :-------: | :---: |
| 첫 번째 SELL |   1300    |   1400    | 10000 |
| 두 번째 SELL |   1350    |   1320    | -3000 |

따라서 사용자 1의 `PROFIT` 은 `7000`, `PROFIT_COUNT` 는 `1` 입니다.

**실행 결과**

| USER_ID | PROFIT | PROFIT_COUNT |
| ------- | ------ | ------------ |
| 4       | 0      | 0            |
| 3       | 0      | 0            |
| 2       | -5000  | 0            |
| 1       | 7000   | 1            |

</details>

<details>
<summary><b>7. 최대 조 개수 (SQL)</b></summary>

합격자들의 ID와 사용 가능한 프로그래밍 언어가 `APPLICANTS` 테이블에 다음과 같이 주어집니다.

| ID   | PROGRAMMING_LANGUAGE |
| ---- | -------------------- |
| 1442 | C++                  |
| 1445 | C++                  |
| 1467 | C                    |
| 1576 | C                    |
| 1677 | C++                  |
| 1678 | JAVA                 |
| 1889 | PYTHON               |
| 1899 | PYTHON               |
| 1900 | C#                   |
| 1903 | C#                   |
| 2003 | JAVA                 |
| 2055 | JAVA                 |

하나의 조에는 다음 5개의 프로그래밍 언어를 사용하는 사람이 **각각 최소 1명 이상** 포함되어야 합니다.

```
C++, C, JAVA, PYTHON, C#
```

한 사람은 하나의 조에만 속할 수 있습니다.
조건을 만족하도록 만들 수 있는 **최대 조의 개수**를 구하는 SQL을 작성하세요.

**예시**

```
1조 (1442, 1467, 1677, 1678, 1889, 1900)
2조 (1445, 1576, 1899, 1903, 2003, 2055)

result = 2
```

</details>

<details>
<summary><b>🗄️ SQL 트랙 — 이번 주도 쉽니다</b></summary>

**SQL 2주차(집계 함수, 13문제)는 10주차로 밀립니다.** 위 [SQL 트랙](#sql-트랙) 섹션의 매핑 표를 조정했습니다.
주제 순서는 그대로입니다. 기출 6·7번이 SQL이라 SQL 감각은 이번 주에도 이어집니다.

</details>

</details>

---

<details>
<summary><h2>10주차 — DP + SQL 파트별 심화 (5 + 12문제)</h2></summary>

**출처:** 프로그래머스 코딩테스트 고득점 Kit → [동적계획법(DP)](https://school.programmers.co.kr/learn/courses/30/parts/12263) / [프로그래머스 SQL 고득점 Kit](https://school.programmers.co.kr/learn/challenges?tab=sql_practice_kit) → 파트별 2문제

두 달 만에 유형별 세트로 돌아옵니다.

- **DP 세트는 전부** 풉니다. 5문제 모두 Lv3 이상이니 "점화식을 세우기 전에 상태를 어떻게 정의하는가"에 시간을 쓰세요
- **SQL은 로드맵 순서 대신 파트별로 어려운 문제를 맛봅니다.** SQL Kit 6개 파트에서 Lv3~4를 2문제씩 골랐습니다. Lv3 이상이 1문제뿐인 파트(SUM·MAX·MIN, IS NULL)는 Lv2로 채웠습니다

> **파일명**은 평소와 같이 `pgs_lv{레벨}_{문제명}.py`, SQL은 `sql_lv{레벨}_{문제명}.sql` 입니다. 예: `pgs_lv3_N으로표현.py`, `sql_lv4_입양시각구하기2.sql`
> 커밋 메시지는 `solve: [SQL Lv4] 입양 시각 구하기(2)` 형식으로 써주세요.

### 코어 문제 ⭐

전원 필수. 세션에서 다 같이 코드를 비교합니다.

| 제목           | 난이도 | 링크                                                                        |
| -------------- | ------ | --------------------------------------------------------------------------- |
| **N으로 표현** | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42895) |

> "N을 k번 써서 만들 수 있는 수의 집합"을 상태로 잡는 순간 풀립니다.
> 집합 DP로 풀었는지, BFS처럼 풀었는지에서 갈립니다.

<details>
<summary><b>🧩 알고리즘 — 동적계획법(DP) (5문제)</b></summary>

| 제목          | 난이도 | 링크                                                                        |
| ------------- | ------ | --------------------------------------------------------------------------- |
| N으로 표현 ⭐ | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42895) |
| 정수 삼각형   | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/43105) |
| 등굣길        | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42898) |
| 사칙연산      | Lv4    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/1843)  |
| 도둑질        | Lv4    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42897) |

> `도둑질`은 집이 원형으로 놓여 있습니다. 첫 집과 마지막 집을 둘 다 털 수 없다는 조건을
> DP 하나로 처리할지, 두 번 돌릴지가 갈리는 지점입니다.

</details>

<details>
<summary><b>🗄️ SQL — 파트별 Lv3~4 (12문제)</b></summary>

파트마다 그 파트의 핵심 문법이 가장 잘 드러나는 문제로 골랐습니다.

| 파트          | 제목                                          | 난이도 | 포인트                           | 링크                                                                         |
| ------------- | --------------------------------------------- | :----: | -------------------------------- | ---------------------------------------------------------------------------- |
| SELECT        | 오프라인/온라인 판매 데이터 통합하기          |  Lv4   | `UNION ALL` + 빈 컬럼 채우기     | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/131537) |
| SELECT        | 대장균의 크기에 따라 분류하기 2               |  Lv3   | 윈도 함수로 백분위 나누기        | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/301649) |
| SUM, MAX, MIN | 물고기 종류 별 대어 찾기                      |  Lv3   | 그룹별 최댓값을 가진 행 찾기     | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/293261) |
| SUM, MAX, MIN | 연도별 대장균 크기의 편차 구하기              |  Lv2   | 그룹 집계값을 행마다 붙이기      | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/299310) |
| GROUP BY      | 입양 시각 구하기(2)                           |  Lv4   | 0건인 그룹까지 출력하기          | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/59413)  |
| GROUP BY      | 년, 월, 성별 별 상품 구매 회원 수 구하기      |  Lv4   | 여러 컬럼 그룹 + `COUNT(DISTINCT)` | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/131532) |
| IS NULL       | 업그레이드 할 수 없는 아이템 구하기           |  Lv3   | "자식이 없는" 행 찾기            | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/273712) |
| IS NULL       | ROOT 아이템 구하기                            |  Lv2   | "부모가 없는" 행 찾기            | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/273710) |
| JOIN          | 특정 기간동안 대여 가능한 자동차들의 대여비용 구하기 |  Lv4   | 기간 겹침 판정 + 할인 조인       | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/157339) |
| JOIN          | FrontEnd 개발자 찾기                          |  Lv4   | `=` 가 아닌 조건으로 조인 (비트) | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/276035) |
| String, Date  | 조건에 맞는 사용자 정보 조회하기              |  Lv3   | 문자열 자르고 이어 붙이기        | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/164670) |
| String, Date  | 조건별로 분류하여 주문상태 출력하기           |  Lv3   | 날짜 비교 + `CASE`               | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/131113) |

> IS NULL 두 문제는 같은 `ITEM_TREE` 테이블을 씁니다. `ROOT 아이템`을 먼저 풀고
> `업그레이드 할 수 없는 아이템`으로 넘어가면 "부모 쪽 NULL"과 "자식 쪽 NULL"을 나란히 비교할 수 있습니다.

> 이번 주에 푼 12문제는 이후 로드맵 주차에서 빠집니다.

</details>

</details>

---

## 제출 방법 요약

```bash
git switch main
git pull
git switch -c {깃허브 닉네임}/week-10
# 문제 풀고 커밋
git push -u origin {깃허브 닉네임}/week-10
# GitHub에서 "Compare & pull request" 클릭
```

자세한 설명, 파일명 규칙, 오류 해결은 **[깃허브 사용 가이드](GITHUB_GUIDE.md)** 를 참고하세요.
