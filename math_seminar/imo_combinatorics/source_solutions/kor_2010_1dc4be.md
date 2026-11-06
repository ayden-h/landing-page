# kor_2010_1dc4be

KMO | South Korea | 2010 | The Second Day | 5

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [kor_2010_1dc4be](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2010_1dc4be.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: South Korea
- Title: KOREAN MATHEMATICAL OLYMPIAD
- Subtitle: 23rd Korean Mathematical Olympiad Final Round
- Year: 2010
- Organization: KOREAN MATHEMATICAL OLYMPIAD COMMITTEE; THE KOREAN MATHEMATICAL SOCIETY
- Publisher: THE KOREAN MATHEMATICAL SOCIETY
- Place: Seoul 135-703, KOREA
- Volume: 23
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

**KNOWN DEFECT:** Source weight formula has an exponent/reciprocal transcription defect. Use W22.

For the checked rewritten exposition, see `../reviewed_solutions/W22.md`.

## Supplied solution 1

We will prove that the minimum number $m$ of cookies is $2^n$. Let us write $A_{-n+1}, \dots, A_0(= A), A_1, A_2, \dots, A_{n-1}, A_n$ to denote the $2n$ people in the counterclockwise order.

First let us show that if $m < 2^n$, then there is a way to distribute $m$ cookies so that $A$ cannot get a cookie. Let $a_i$ be the amount of cookies given to $A_i$. Let $N = \sum_{i=-n+1}^{n} a_i 2^{|i|}$. Note that the value of $N$ is non-increasing when one passes a cookie to the neighbors. So let us initially give all $m$ cookies to $A_n$. Then $N = m2^{-n} < 1$. This means that even if we allow the people to pass cookies under the given rules, we still have $N < 1$ and therefore it is impossible for $A$ to have a cookie.

Now let us show that if $m = 2^n$, then there is a strategy to make $A$ have a cookie. Let $a_i$ be the amount of cookies given to $A_i$. By symmetry, we may assume that $\sum_{i=0}^{n-1} a_i \ge \sum_{i=0}^{n-1} a_{-i}$.

We ask $A_n$ to pass $\lfloor a_n/2 \rfloor$ cookies to $A_{n-1}$ by eating $\lfloor a_n/2 \rfloor$ cookies by himself. This allows us to assume that $A_0, A_1, A_2, \dots, A_{n-1}$ have at least $m/2 = 2^{n-1}$ cookies. (If $a_n$ is even, then this is O.K. because they will have at least $(m-a_n)/2 + a_n/2$ cookies. If $a_n$ was odd, then they will have at least $(m-a_n)/2 + (a_n-1)/2 = m/2 - 1/2$ cookies. Since $m$ is even, we can still conclude that $A_0, A_1, A_2, \dots, A_{n-1}$ have at least $m/2$ cookies.)

Now we claim that for $k = 1, 2, \dots, n-1$, if $A_0, A_1, A_2, \dots, A_k$ have at least $2^k$ cookies, then by passing cookies of $A_k$ to $A_{k-1}$, we may assume that $A_0, A_1, A_2, \dots, A_{k-1}$ have at least $2^{k-1}$ cookies. We may assume that $a_k > 2^{k-1}$. If $a_k = 2^k$, then we simply let $A_k$ pass $2^{k-1}$ cookies to $A_{k-1}$ by eating $2^{k-1}$ cookies. So we may assume $a_k < 2^{k-1} + 2^{k-1}$. Therefore there exists an integer $i \in \{1, 2, 3, \dots, k-1\}$ such that
$$
2^{k-1} + 2^{k-2} + \dots + 2^{k-i} < a_k \le 2^{k-1} + 2^{k-2} + \dots + 2^{k-i-1}.
$$

Note that
$$
\sum_{i=0}^{k-1} a_i \ge 2^k - a_k \ge 2^k - (2^{k-1} - 2^{k-2} + \dots + 2^{k-i-1}).
$$

Now if $A_k$ passes his cookies to $A_{k-1}$ as many as he can, then he can pass at least $2^{k-2} + 2^{k-3} + \dots + 2^{k-i-1}$ cookies.

Then $A_0, A_1, \dots, A_{k-1}$ have at least $\sum_{i=0}^{k-1} a_i + (2^{k-2} + \dots + 2^{k-i-1}) \ge 2^{k-1}$ cookies. This proves the claim.

By the above claim we can inductively make $A_0$ have at least $2^0 = 1$ cookies. $\square$

