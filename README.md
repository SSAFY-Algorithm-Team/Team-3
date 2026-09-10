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

## SQL 트랙

5주차부터 SQL을 본격적으로 시작합니다. (**6주차는 알고리즘에 집중하기 위해 한 주 쉽니다** — 아래 표의 매핑을 한 주씩 밀었습니다.)
**프로그래머스 SQL 고득점 Kit 106문제를 8주에 완주**하는 것이 목표이고,
알고리즘 문제와 병행하므로 매주 알고리즘 세트 + SQL 한 묶음씩 가져갑니다.

<details>
<summary><b>📋 SQL 8주 로드맵 — 전체 106문제 (펼치기)</b></summary>

영역(SELECT/JOIN 등)이 아니라 **그 주에 쓰는 SQL 문법**을 기준으로 묶었습니다.

| SQL 주차 | 스터디 주차 | 주제 | 문제 수 | 난이도 |
| :---: | :---: | --- | :---: | --- |
| 1 | 5주차 ✅ | 단일 테이블 기본 조회 | 18 | Lv1 위주 |
| — | **6주차** | **쉬는 주 — 알고리즘 집중** | — | — |
| 2 | 7주차 | 집계 함수 | 13 | Lv1~3 |
| 3 | 8주차 | NULL 처리 + GROUP BY 입문 | 14 | Lv1~3 |
| 4 | 9주차 | GROUP BY 심화 + CASE | 12 | Lv2~4 |
| 5 | 10주차 | 문자열 · 날짜 | 14 | Lv1~3 |
| 6 | 11주차 | JOIN 기본 | 11 | Lv2~4 |
| 7 | 12주차 | 서브쿼리 + JOIN 심화 | 12 | Lv2~5 |
| 8 | 13주차 | 종합 · 고난도 | 12 | Lv2~5 |

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

<details>
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

<details>
<summary><h2>5주차 — 스택/큐 · 힙 + SQL 본격 시작 (9 + 15문제)</h2></summary>

**출처:** 프로그래머스 코딩테스트 고득점 Kit → [스택/큐](https://school.programmers.co.kr/learn/courses/30/parts/12081), [힙](https://school.programmers.co.kr/learn/courses/30/parts/12117) / 프로그래머스 SQL 고득점 Kit → SQL 1주차

- **스택/큐 · 힙 세트는 전부** 풉니다 — "어떤 자료구조를 고르면 O(N²)이 O(N log N)이 되는가"를 보는 세트입니다
- **SQL은 이번 주부터 본격 시작** — SQL 1주차(단일 테이블 기본 조회) 15문제. 전부 Lv1이라 1시간 남짓 걸립니다

### 코어 문제 ⭐

전원 필수. 세션에서 다 같이 코드를 비교합니다.

| 제목                  | 난이도 | 링크                                                                       |
| --------------------- | ------ | -------------------------------------------------------------------------- |
| **디스크 컨트롤러**   | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42627) |

> 힙을 두 개 굴릴지, 정렬 후 하나만 굴릴지에서 갈립니다. "언제 힙에 넣는가"가 핵심.

<details>
<summary><b>🧩 알고리즘 — 스택/큐 · 힙 (9문제)</b></summary>

### 스택/큐 (6문제)

| 제목                | 난이도 | 링크                                                                       |
| ------------------- | ------ | -------------------------------------------------------------------------- |
| 같은 숫자는 싫어    | Lv1    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/12906) |
| 기능개발            | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42586) |
| 올바른 괄호         | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/12909) |
| 프로세스            | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42587) |
| 다리를 지나는 트럭  | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42583) |
| 주식가격            | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42584) |

### 힙 (3문제)

| 제목                 | 난이도 | 링크                                                                       |
| -------------------- | ------ | -------------------------------------------------------------------------- |
| 더 맵게              | Lv2    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42626) |
| 디스크 컨트롤러 ⭐   | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42627) |
| 이중우선순위큐       | Lv3    | [바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42628) |

> Python은 `heapq`가 최소 힙만 지원합니다. `이중우선순위큐`에서 최대값을 뺄 때
> 부호를 뒤집을지, 힙 두 개를 동기화할지가 갈리는 지점입니다.

</details>

<details>
<summary><b>🗄️ SQL 1주차 — 단일 테이블 기본 조회 (15문제)</b></summary>

`SELECT` / `WHERE` / `ORDER BY` / `LIMIT` 만으로 전부 풀립니다.

| 제목                                      | 난이도 | 링크                                                                        |
| ----------------------------------------- | ------ | --------------------------------------------------------------------------- |
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

<details open>
<summary><h2>6주차 — SWEA 커리큘럼 전 범위 (40문제)</h2></summary>

**출처:** SWEA Solving Club → [16기 대전 6반 알고리즘](https://swexpertacademy.com/main/talk/solvingClub/clubDetail.do?solveclubId=AZ9kDS86wCTHBITH)

이번 주는 9/15 A형 테스트, 9/19 B형 테스트를 대비하기 위해 **알고리즘에만 집중합니다. SQL은 쉽니다.**

> **제출은 SWEA 사이트 + 레포 둘 다** 입니다. 문제함 제출현황이 세션 체크인 자료가 되니
> 사이트 제출을 빠뜨리지 마세요. 파일명은 평소와 같이 `swea_{번호}_{문제명}.py` 입니다.

> `어디에 단어가 들어갈 수 있을까`(1979) · `농작물 수확하기`(2805) 는 **1주차에 이미 푼 문제**입니다.
> 다시 풀어도 좋고, 1주차 코드를 Solving Club에 제출만 해서 문제함을 채워도 됩니다.

### 코어 문제 ⭐

전원 필수. 세션에서 다 같이 코드를 비교합니다.

| 번호 | 제목 | 난이도 | 링크 |
| ---- | ---- | :----: | ---- |
| **2115** | **[모의 SW 역량테스트] 벌꿀채취** | 모의 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V4A46AdIDFAWu) |

<details>
<summary><b>🧩 문제함 8개 — 전체 40문제 (펼치기)</b></summary>

#### 알고리즘 기본 (6문제)

| 번호 | 제목 | 난이도 | 링크 |
| ---- | ---- | :----: | ---- |
| 9490 | 풍선팡 | D2 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXAerAPaVXMDFARP) |
| 4834 | [S/W 문제해결 기본] 1일차 - 숫자 카드 | D2 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTLVouKpUgDFAVT) |
| 4828 | [S/W 문제해결 기본] 1일차 - min max | D2 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTLQZwKon4DFAVT) |
| 2001 | 파리 퇴치 | D2 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq) |
| 1979 | 어디에 단어가 들어갈 수 있을까 (1주차 중복) | D2 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq) |
| 1961 | 숫자 배열 회전 | D2 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq) |

> D2 워밍업 세트입니다. `파리 퇴치` · `풍선팡` 은 델타 배열을 어떻게 잡는지만 보고 빠르게 넘어가세요.

<sub>[문제함 바로가기 · 제출현황](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kDS86wCXHBITH&leftPage=1)</sub>

#### 재귀 (4문제)

| 번호 | 제목 | 난이도 | 링크 |
| ---- | ---- | :----: | ---- |
| 6808 | 규영이와 인영이의 카드게임 | D3 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWgv9va6HnkDFAW0) |
| 4836 | [S/W 문제해결 기본] 2일차 - 색칠하기 | D2 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTLZMRKpsYDFAVT) |
| 2805 | 농작물 수확하기 (1주차 중복) | D3 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB) |
| 1210 | [S/W 문제해결 기본] 2일차 - Ladder1 | D4 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh) |

> `Ladder1` 은 재귀로도 역추적으로도 풀립니다. `규영이와 인영이의 카드게임` 은 순열 + 재귀가 붙는 첫 문제입니다.

<sub>[문제함 바로가기 · 제출현황](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawC3HBITH&leftPage=1)</sub>

#### 순열과 조합 (5문제)

| 번호 | 제목 | 난이도 | 링크 |
| ---- | ---- | :----: | ---- |
| 4831 | [S/W 문제해결 기본] 1일차 - 전기버스 | D3 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTLS24ao9ADFAVT) |
| 4014 | [모의 SW 역량테스트] 활주로 건설 | 모의 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeW7FakkUDFAVH) |
| 4012 | [모의 SW 역량테스트] 요리사 | 모의 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH) |
| 2382 | [모의 SW 역량테스트] 미생물 격리 | 모의 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV597vbqAH0DFAVl) |
| 1240 | [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드 | D3 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15FZuqAL4CFAYD) |

> `요리사` 는 조합, `활주로 건설` 은 부분집합, `미생물 격리` 는 시뮬레이션입니다. **같은 문제함 안에서 쓰는 도구가 다릅니다.**

<sub>[문제함 바로가기 · 제출현황](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawC7HBITH&leftPage=1)</sub>

#### 스택과 큐 (5문제)

| 번호 | 제목 | 난이도 | 링크 |
| ---- | ---- | :----: | ---- |
| 5432 | 쇠막대기 자르기 | D4 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVl47b6DGMDFAXm) |
| 2477 | [모의 SW 역량테스트] 차량 정비소 | 모의 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV6c6bgaIuoDFAXy) |
| 1225 | [S/W 문제해결 기본] 7일차 - 암호생성기 | D3 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14uWl6AF0CFAYD) |
| 1222 | [S/W 문제해결 기본] 6일차 - 계산기1 | D4 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14mbSaAEwCFAYD) |
| 1220 | [S/W 문제해결 기본] 5일차 - Magnetic | D3 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14hwZqABsCFAYD) |

> `계산기1` 은 중위 → 후위 변환, `Magnetic` 은 스택을 안 써도 풀리는 문제입니다. 후자는 "왜 스택 문제함에 있는가"를 같이 이야기해 볼 만합니다.

<sub>[문제함 바로가기 · 제출현황](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawC_HBITH&leftPage=1)</sub>

#### 트리와 그래프 (4문제)

| 번호 | 제목 | 난이도 | 링크 |
| ---- | ---- | :----: | ---- |
| 5178 | [S/W 문제해결 기본] 8일차 - 노드의 합 | D3 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTa2VIq4mYDFAVT) |
| 5176 | [S/W 문제해결 기본] 8일차 - 이진탐색 | D2 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTa0jjq4ggDFAVT) |
| 1232 | [S/W 문제해결 기본] 9일차 - 사칙연산 | D4 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV141J8KAIcCFAYD) |
| 1231 | [S/W 문제해결 기본] 9일차 - 중위순회 | D4 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV140YnqAIECFAYD) |

> 배열로 트리를 표현하는 연습 세트입니다. `사칙연산` 은 후위 순회로 계산하는 문제라 6일차 `계산기1` 과 짝으로 보면 좋습니다.

<sub>[문제함 바로가기 · 제출현황](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawDDHBITH&leftPage=1)</sub>

#### DFS (6문제)

| 번호 | 제목 | 난이도 | 링크 |
| ---- | ---- | :----: | ---- |
| 4008 | [모의 SW 역량테스트] 숫자 만들기 | 모의 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeRZV6kBUDFAVH) |
| 2819 | 격자판의 숫자 이어 붙이기 | D4 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB) |
| 2115 | [모의 SW 역량테스트] 벌꿀채취 ⭐ | 모의 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V4A46AdIDFAWu) |
| 1865 | 동철이의 일 분배 | D4 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LuHfqDz8DFAXc) |
| 1486 | 장훈이의 높은 선반 | D4 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b7Yf6ABcBBASw) |
| 1244 | [S/W 문제해결 응용] 2일차 - 최대 상금 | D3 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD) |

> 모의 역량테스트 문제가 3개라 이번 주 체감 난이도의 대부분이 여기에 있습니다. 시간을 넉넉히 잡으세요.

<sub>[문제함 바로가기 · 제출현황](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawDHHBITH&leftPage=1)</sub>

#### BFS (5문제)

| 번호 | 제목 | 난이도 | 링크 |
| ---- | ---- | :----: | ---- |
| 1953 | [모의 SW 역량테스트] 탈주범 검거 | 모의 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq) |
| 1249 | [S/W 문제해결 응용] 4일차 - 보급로 | D4 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD) |
| 1238 | [S/W 문제해결 기본] 10일차 - Contact | D4 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD) |
| 1227 | [S/W 문제해결 기본] 7일차 - 미로2 | D4 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14wL9KAGkCFAYD) |
| 1226 | [S/W 문제해결 기본] 7일차 - 미로1 | D4 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14vXUqAGMCFAYD) |

> `미로1` → `미로2` → `보급로` 순으로 풀면 "단순 도달 판정 → 최단거리 → 가중치" 로 자연스럽게 올라갑니다. `보급로` 는 BFS로는 안 되고 다익스트라가 필요합니다.

<sub>[문제함 바로가기 · 제출현황](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawDLHBITH&leftPage=1)</sub>

#### heap과 BackTracking (5문제)

| 번호 | 제목 | 난이도 | 링크 |
| ---- | ---- | :----: | ---- |
| 9280 | 진용이네 주차타워 | D3 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AW9j74FacD0DFAUY) |
| 5215 | 햄버거 다이어트 | D3 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWT-lPB6dHUDFAVT) |
| 5189 | [S/W 문제해결 구현] 2일차 - 전자카트 | D3 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTtmmdKeD8DFAVT) |
| 2930 | 힙 | D3 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV-Tj7ya3jYDFAXr) |
| 2817 | 부분 수열의 합 | D3 | [바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7IzvG6EksDFAXB) |

> `부분 수열의 합` · `햄버거 다이어트` 는 백트래킹, `힙` · `전자카트` 는 자료구조 문제입니다. `진용이네 주차타워` 는 그리디에 가깝습니다.

<sub>[문제함 바로가기 · 제출현황](https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawDPHBITH&leftPage=1)</sub>

</details>

<details>
<summary><b>🗄️ SQL — 이번 주는 쉽니다</b></summary>

6주차는 SQL을 넣지 않습니다. SWEA 40문제와 SQL 13문제를 같은 주에 얹으면 둘 다 건성으로 하게 됩니다.

**SQL 2주차(집계 함수, 13문제)는 7주차로 밀립니다.** 위 [SQL 트랙](#sql-트랙) 섹션의 매핑 표를 한 주씩 조정했습니다.
주제 순서는 그대로입니다.

여유 있는 사람은 `SUM` / `AVG` / `COUNT` / `MAX` / `MIN` 이 `NULL` 을 어떻게 다루는지만 미리 봐두면
7주차가 훨씬 수월합니다. (`COUNT(*)` 와 `COUNT(컬럼)` 이 다른 값을 돌려주는 이유)

</details>

</details>

---

## 제출 방법 요약

```bash
git switch main
git pull
git switch -c {깃허브 닉네임}/week-06
# 문제 풀고 커밋
git push -u origin {깃허브 닉네임}/week-06
# GitHub에서 "Compare & pull request" 클릭
```

자세한 설명, 파일명 규칙, 오류 해결은 **[깃허브 사용 가이드](GITHUB_GUIDE.md)** 를 참고하세요.
