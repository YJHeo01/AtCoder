제출 내역 : https://atcoder.jp/contests/abc390/submissions?f.Task=&f.LanguageName=&f.Status=&f.User=sk14cj

A (2:38)

<ul>
  <li>인접한 두 원소를 정확히 한 번 서로 바꾸는 연산을 통해, 수열 A를 오름차순으로 정렬할 수 있는지 판별하는 문제다.</li>
  <li>이때 나는 순간 당황했다. "정확히 한 번" 바꾸는 것을 통해 오름차순으로 정렬하는 방법이 떠오르지 않았기 때문이다.</li>
  <li>이때, 정확히 한 번 바꿔야 한다는 생각 대신, 버블 정렬을 통해 수를 교환한 횟수를 구해줘도 상관없다는 생각을 했다. 배열의 크기는 5로 고정되어 있으므로 시간복잡도 상으로도 문제가 없다.</li>
  <li>따라서, 버블 정렬을 구현하고, 오름차순으로 정렬하기 위해 수를 몇번 교환해주었는지 구하는 코드를 작성했다. 교환 횟수가 1이면 Yes, 아니면 No를 출력하도록 하였다.</li>
  <li>시간복잡도 O(5^2) = O(1)</li>
</ul>

B (5:13)

<ul>
  <li>주어진 수열이 등비수열인지 판별하는 문제</li>
  <li>인접한 두 원소끼리 나눗셈 연산을 해주고, 이 값들을 비교하는 방법이 가장 먼저 생각났지만, 부동소수점 오류가 발생하면 틀릴 수도 있다고 생각했다.</li>
  <li>인접한 세 원소가 등비수열인 경우 a*(r^(i-1)), a*(r^(i)), a*(r^(i+1))이 성립하고, 이때 중간 항의 제곱 = 좌측 항과 우측 항의 곱 = a*(r^(2*i))이 성립한다.</li>
  <li>길이가 2인 경우에는 위 성질을 활용할 수 없지만, 이 상황에서는 어차피 모두 등비수열이므로 상관없다.</li>
  <li>따라서 길이가 2인 경우에는 무조건 Yes를, 그렇지 않은 경우에는 모든 항에 대해 3번째 식이 성립하는지 체크해주고 Yes 혹은 No를 출력하는 코드를 작성했다.</li>
  <li>시간복잡도 O(N)</li>
</ul>


C (19:51, 2)

<ul>
  <li>격자에는 검은색, 흰색, ?색이 존재하는데, ?색을 자유롭게 칠해서 검정색으로 칠해진 모든 셀을 연결할 경우 하나의 직사각형을 이룰 수 있는지 판별하는 문제</li>
  <li>문제를 보고 가장 먼저 든 생각은, 검은색 격자의 x 최대,최소값, y 최대, 최소값을 구하고, 이 사이에 있는 격자 중 흰색이 포함되어 있지 않으면 No, 그렇지 않다면 Yes를 출력하도록 하였다.</li>
  <li>그러나, 이 풀이는 엣지 케이스를 고려하지 못하였다. 주어진 격자에 검은색이 하나도 존재하지 않는 경우에는 위 풀이가 성립할 수 없다.</li>
  <li>따라서 검은색 격자가 하나 이상 존재할 경우 기존 풀이 그대로 가고, 그렇지 않은 경우 ?가 하나 이상 존재하면 Yes를, 그렇지 않다면 No를 출력하도록 코드를 작성해서 AC 판정을 받았다.</li>
  <li>시간복잡도 O(H*W)</li>
</ul>

D (-)

풀다가 포기하고 E로 넘어갔다.

E (38:16)

<ul>
  <li>냅색 문제 변형</li>
  <li>3가지 비타민 중 가장 작은 값을 최대화 시키도록 음식의 조합을 골라야 한다.</li>
  <li>각 3가지 비타민에 대해, 각각 냅색을 이용해서 섭취한 칼로리 대비 가장 섭취 효율이 좋은 조합을 찾는다.</li>
  <li>3가지 비타민과 관련된 음식의 칼로리 섭취 제한을 각각 a,b,c라고 하고, 칼로리 총합의 제한이 X라고 할 때, a와 b값을 정해주면 c의 값은 자연스럽게 X-a-b로 정해진다.</li>
  <li>따라서 이 풀이의 시간복잡도는 O(X^2+3*X) = O(X^2)</li>
</ul>
