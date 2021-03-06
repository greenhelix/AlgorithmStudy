객관식
merge include

viewstub

launch mode single top (activity stack)
activity, fragment lifecylcle

intentservice

ViewModel
ARC???
==================
문제 설명
어떤 숫자 n을 각 자리의 숫자로 나누었을 때, 나누어떨어지면 그 숫자로 분열 가능하다고 합니다.

예를 들어 2232이라는 숫자는 2와 3 두 개의 숫자로 구성되어 있습니다. 또한, 2232는 2로도 나누어떨어지고, 3으로도 나누어 떨어집니다. 따라서 분열 가능한 횟수는 2입니다.
2232의 예에서와같이 2가 여러 번 나오더라도 분열 가능한 횟수를 셀 때는 2 한 번, 3 한 번으로 세며 중복해서 나오는 숫자 2는 고려하지 않습니다.

숫자 n이 매개변수로 주어질 때, n이 분열 가능한 횟수를 return 하도록 solution 함수를 완성하세요.

[※ 숫자는 0으로 나눌 수 없음을 유의하세요.]

제한사항
n은 1015 이하의 자연수입니다.
입출력 예
n result
2322 2
1234 2
입출력 예 설명
입출력 예 #1
문제의 예제와 같습니다.

입출력 예 #2
1234의 경우 다음과 같습니다.

1234는 1로 나누어떨어짐
1234는 2로 나누어떨어짐
1234는 3으로 나누어떨어지지 않음
1234는 4로 나누어떨어지지 않음
따라서 분열 가능한 횟수는 2이므로 2를 return 합니다.

==================
문제 설명
수강 내역(학정번호, 성적)이 주어졌을 때, 이를 깔끔하게 정리한 성적표를 구하려고 합니다. 아래는 민수의 수강 내역 중에서, 반복 수강으로 삭제된 과목들을 취소선으로 표시한 것입니다.

<수강 내역>

학정번호 성적
DS7651 A0
CA0055 D+
AI5543 C0
OS1808 B-
DS7651 B+
AI0001 F
DB0001 B-
AI5543 D+
DS7651 A+
OS1808 B-
성적은 아래에 나열된 13가지 중 하나로 표기됩니다.
A+, A0, A-, B+, B0, B-, C+, C0, C-, D+, D0, D-, F
나열된 순서대로 A+이 가장 좋은 학점이며, F가 가장 나쁜 학점입니다.
과목들은 학정번호 6자리 (알파벳 2 글자+숫자 4글자)로 구분됩니다.
학정 번호 6자리가 완전히 똑같아야 동일한 과목입니다.
3번째로 수강한 AI5543과 6번째로 수강한 AI0001은 서로 다른 과목입니다.
동일한 과목을 여러 번 수강한 경우에는 가장 좋은 성적만 인정되고, 나머지는 삭제됩니다.
DS7651은 3번 수강했으나, A+받은 것만 인정되었습니다.
가장 좋은 성적이 여러 개라면, 그중에서 가장 먼저 수강한것만 인정되고, 나머지는 삭제됩니다.
표에서 윗행에 나타난 것이 먼저 수강한 것입니다.
OS1808은 두 번 수강하여 두 번 모두 B-를 받았으나, 처음 수강한 것만 인정되고, 나머지는 삭제되었습니다.
위의 표를 정리하여, 삭제된 과목들을 제외하고 좋은 성적을 받은 과목부터 나열하면 다음과 같습니다. (성적이 같다면, 먼저 수강한 과목부터 나열하도록 합니다.)

<정리된 성적표>

학정번호 성적
DS7651 A+
OS1808 B-
DB0001 B-
AI5543 C0
CA0055 D+
AI0001 F
민수가 수강한 과목들과 성적이 담긴 문자열 배열 grades가 매개변수로 주어집니다. 이때, 문제에서 명시한 대로 정리된 성적표를 구해서 return 하도록 solution 함수를 완성해주세요.

제한사항
grades의 길이(=수강한 내역의 개수)는 1 이상 50,000 이하입니다.
grades에는 먼저 수강한 내역부터 차례대로 담겨져 있습니다.
grades의 각 원소는 길이가 8 또는 9인 문자열입니다.
grades의 각 원소는 학정번호 성적 형식입니다.
학정번호와 성적은 하나의 공백(스페이스)으로 구분되어 있습니다.
학정번호는 6자리이며, 처음 2자리는 알파벳 대문자, 다음 4자리는 숫자로 구성되어 있습니다.
성적은 1자리 또는 2자리이며, A+부터 F까지의 13가지 성적 중 하나입니다.
잘못된 학정번호나 성적은 입력으로 주어지지 않습니다.
return 값 설명
정리된 성적표를 문자열 형태로 배열에 담아서 return 합니다.
좋은 성적을 받은 것부터 학정번호 성적을 담습니다.
성적이 같다면, 먼저 수강한 과목부터 담습니다.
입출력 예
grades result
["DS7651 A0", "CA0055 D+", "AI5543 C0", "OS1808 B-", "DS7651 B+", "AI0001 F", "DB0001 B-", "AI5543 D+", "DS7651 A+", "OS1808 B-"] ["DS7651 A+", "OS1808 B-", "DB0001 B-", "AI5543 C0", "CA0055 D+", "AI0001 F"]
["DM0106 D-", "PL6677 B+", "DM0106 B+", "DM0106 B+", "PL6677 C0", "GP0000 A0"] ["GP0000 A0", "PL6677 B+", "DM0106 B+"]
입출력 예 설명
입출력 예 #1
문제 예시와 같습니다.

입출력 예 #2
삭제되는 수강 내역을 취소선으로 표시하면 아래와 같습니다.

<수강 내역>

학정번호 성적
DM0106 D-
PL6677 B+
DM0106 B+
DM0106 B+
PL6677 C0
GP0000 A0
위의 표에서 정리된 성적표를 구하면, 아래와 같습니다.

<정리된 성적표>

학정번호 성적
GP0000 A0
PL6677 B+
DM0106 B+

================
문제 설명
어떤 회사에서 제품을 만들기 위해 A 부품을 만드는 공장 a개, B 부품을 만드는 공장 b개를 세우려 합니다. 이 회사는 공장을 세울만한 부지 n개를 가지고 있는데, 이중 a + b개만큼의 부지를 선택해서 공장을 세우면 됩니다. 이때, 공장 부지는 2차원 평면상에 있는 점 형태로, 좌표 (x, y)로 표현합니다.

공장을 지을 위치가 잘 결정되었는지의 기준을 인접성 지수라고 하는데, 인접성 지수는 다음과 같이 계산합니다.

같은 부품을 만드는 공장들 간의 거리의 제곱을 모두 계산합니다.
거리는 두 점 사이의 직선거리를 사용합니다.
이 값들 중 최솟값을 인접성 지수라고 합니다.
예를 들어 A 부품 공장을 4개, B 부품 공장을 3개 세울 때, A 부품공장의 위치를 a1, a2, a3, a4, B 부품 공장의 위치를 b1, b2, b3라고 하겠습니다. 이때, A 부품공장에서 서로 다른 두 공장을 선택하는 방법은 다음과 같이 6가지입니다.

1. [a1, a2]
2. [a1, a3]
3. [a1, a4]
4. [a2, a3]
5. [a2, a4]
6. [a3, a4]
   또, B 부품공장에서 서로 다른 두 공장을 선택하는 방법은 다음과 같이 3가지입니다.

7. [b1, b2]
8. [b1, b3]
9. [b2, b3]
   이제 위의 1 ~ 9에 해당하는 총 9가지 쌍에 대해 거리 제곱을 계산한 값 중 최솟값이 인접성 지수입니다.

공장 부지의 위치를 나타내는 배열 x, y, A 부품 공장의 수 a, B 부품 공장의 수 b가 매개변수로 주어질 때, 인접성 지수가 최대가 되도록 공장을 배치한 후, 그 인접성 지수를 return 하는 solution 함수를 완성해주세요.

제한 사항
배열 x와 y의 길이는 1 이상 10 이하입니다.
x와 y의 길이는 같습니다.
x와 y의 i번 원소는 i번 공장부지의 좌표입니다.
x와 y의 모든 원소는 0 이상 10,000 이하인 정수입니다.
예를 들어 x[i] = X와 y[i] = Y인 경우 i번 공장부지의 좌표는 (X, Y)입니다.
a와 b는 2 이상 4 이하의 자연수입니다.
a + b는 배열 x와 y의 길이보다 작거나 같습니다.
한 공장 부지에는 공장을 하나만 세울 수 있습니다.
입출력 예
x y a b result
[0, 1, 2, 3, 4] [0, 1, 2, 3, 4] 2 2 18
[0, 1, 2, 3, 4] [0, 0, 0, 0, 0] 3 2 4
입출력 예 설명
입출력 예 #1

공장 부지 위치는 (0,0), (1,1), (2,2), (3,3), (4,4)이고, A 부품 공장을 2개 B 부품 공장을 2개 세우려 합니다. A 부품 공장을 (0,0), (4,4), B 부품 공장을 (1,1), (3,3) 위치에 세운다면 인접성 지수는 다음과 같이 계산합니다.

A 부품공장에서 서로 다른 두 공장을 선택하는 방법
공장 1 공장 2 두 공장 사이의 거리 제곱
(0,0) (4,4) 32
B 부품공장에서 서로 다른 두 공장을 선택하는 방법
공장 1 공장 2 두 공장 사이의 거리 제곱
(1,1) (3,3) 8
따라서 위와 같이 공장을 세울 경우, 2가지 쌍 중 최솟값인 8이 인접성 지수가 됩니다.

만약, A 부품 공장을 (0,0), (3,3), B 부품 공장을 (1,1), (4,4) 위치에 세운다면 인접성 지수는 다음과 같이 계산합니다.

A 부품공장에서 서로 다른 두 공장을 선택하는 방법
공장 1 공장 2 두 공장 사이의 거리 제곱
(0,0) (3,3) 18
B 부품공장에서 서로 다른 두 공장을 선택하는 방법
공장 1 공장 2 두 공장 사이의 거리 제곱
(1,1) (4,4) 18
따라서 이 경우에는 2가지 쌍 중 최솟값인 18이 인접성 지수가 됩니다.

이 외에도, 공장을 지을 수 있는 모든 경우를 고려해 봤을 때, 인접성 지수가 18보다 커지도록 공장 부지를 선택하는 방법은 없습니다. 따라서 인접성 지수가 최대가 되도록 공장을 세우는 방법은 다음과 같으며,

A → (0,0), (3,3), B → (1,1), (4,4)
또는

A → (1,1), (4,4), B → (0,0), (3,3)
이때의 인접성 지수인 18을 return 하면 됩니다.

입출력 예 #2

공장 부지 위치는 (0,0), (1,0), (2,0), (3,0), (4,0)이고, A 부품 공장을 3개 B 부품 공장을 2개 세우려 합니다.

A 부품 공장을 (0,0), (1,0), (3,0) B 부품 공장을 (2,0), (4,0) 위치에 세운다면 인접성 지수는 다음과 같이 계산합니다.

A 부품공장에서 서로 다른 두 공장을 선택하는 방법
공장 1 공장 2 두 공장 사이의 거리 제곱
(0,0) (1,0) 1
(0,0) (3,0) 9
(1,0) (3,0) 4
B 부품공장에서 서로 다른 두 공장을 선택하는 방법
공장 1 공장 2 두 공장 사이의 거리 제곱
(2,0) (4,0) 4
따라서 위의 4가지 쌍 중 최솟값인 1이 인접성 지수가 됩니다.

만약, A 부품 공장을 (0,0), (2,0), (4,0) B 부품 공장을 (1,0), (3,0) 위치에 세운다면 인접성 지수는 다음과 같이 계산합니다.

A 부품공장에서 서로 다른 두 공장을 선택하는 방법
공장 1 공장 2 두 공장 사이의 거리 제곱
(0,0) (2,0) 4
(0,0) (4,0) 16
(2,0) (4,0) 4
B 부품공장에서 서로 다른 두 공장을 선택하는 방법
공장 1 공장 2 두 공장 사이의 거리 제곱
(1,0) (3,0) 4
따라서 위의 4가지 쌍 중 최솟값인 4가 인접성 지수가 됩니다.

이 외에도, 공장을 지을 수 있는 모든 경우를 고려해 봤을 때, 인접성 지수가 4보다 커지도록 공장 부지를 선택하는 방법은 없습니다. 따라서 인접성 지수가 최대가 되도록 공장을 세우는 방법은 다음과 같으며,

A → (0,0), (2,0), (4,0), B → (1,0), (3,0)
이때의 인접성 지수인 4를 return 하면 됩니다.

=========================
HOUSE_LOCATIONS은 A마을에 있는 집에 대한 정보를 담은 테이블입니다. HOUSE_LOCATIONS 테이블 구조는 다음과 같으며, OWNER, X, Y는 각각 집주인과 2차원 평면에 나타낸 집의 좌표를 나타냅니다.

NAME TYPE
OWNER VARCHAR(N)
X INT
Y INT
문제
이 마을에 사는 사람은 1초에 위/아래/좌/우로 1칸씩만 걸을 수 있으며 대각선 방향으로 걷지 않습니다. 이때 Carlos의 집을 기준으로 도보로 가장 오래 걸리는 집은 누구의 집이고, 몇 초 동안 걸어야 하는지 조회하는 SQL 문을 작성해주세요. 같은 거리에 있는 집이 여럿인 경우, 이름이 사전 순으로 더 앞인 사람 1명만 보여주세요.

예시
예를 들어 다음과 같은 HOUSE_LOCATIONS 테이블이 있을 때,

OWNER X Y
Carlos 4 2
Peter 1 2
Ben 6 3
Jenny 3 5
이를 그림으로 표현하면

Screen Shot.png

Carlos의 집과 Peter의 집 사이 거리는 3
Carlos의 집과 Jenny의 집 사이 거리는 4
Carlos의 집과 Ben의 집 사이 거리는 3

입니다. 따라서 SQL을 실행하면 다음과 같이 출력되어야 합니다.

OWNER DISTANCE
Jenny 4
※ [실행] 시 주어지는 데이터와 [채점] 시 주어지는 데이터는 다릅니다. [실행] 시 Carlos의 집은 X = 4, Y = 2 위치에 있으나, [채점] 시 Carlos의 집은 다른 위치에 있습니다. 하드코딩을 하지 않도록 주의해주세요.
