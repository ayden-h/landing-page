# bmo_2021_ac9fb9

BMO-SL | Balkan Mathematical Olympiad | 2021 | NUMBER THEORY | N7

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2021_ac9fb9](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2021_ac9fb9.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Balkan Mathematical Olympiad
- Title: 38th Balkan Mathematical Olympiad
- Subtitle: Shortlisted Problems with Solutions
- Year: 2021
- Editors: Christofides, Demetres; Karantanos, Demetris; Kouzaris, Stelios; Parayiou, Theoklitos; Stylianou, Stelios; Voskou, Marios
- Organization: BMO 2021 Organising Committee and Problem Selection Committee
- Place: Cyprus
- Series: Balkan Mathematical Olympiad
- Volume: 38

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Evidently, all right-angle triangles with integer sides are super-integer triangles. We will use the following notation $(a, b, c\{h\})$ to denote a super-integer triangle whose sides are $a$, $b$ and $c$ and the height of integer length is $h$. The height will be written in curly brackets next to the corresponding side and it will be omitted for right-angled triangles. It also follows that if $(a, b, c)$ is a super-integer triangle, then so is $(ka, kb, kc)$, where $k$ is a positive integer.

**Note.** In all cases of right-angled triangles one can check directly that they are right-angled by Pythagoras' Theorem or use the standard result that $(d(m^2 - n^2), 2dmn, d(m^2 + n^2))$ is a right-angled triangle. For non-right-angled triangles we will use Heron's formula that the area of the triangle is $\sqrt{s(s-a)(s-b)(s-c)}$ where $s$ is the semiperimeter. For the triangle to be super-integer we need that $s(s-a)(s-b)(s-c)$ is a perfect square, say $s = m^2$, and that $2m$ is a multiple of $a$ or $b$ or $c$. We will only make implicit use of the above.

From $(5, 5, 6\{4\})$ and $(5, 5, 8\{3\})$ it follows that $6$ and $8$ are good. From $(6, 8, 10)$ it then follows that $10$ is also good.

It thus follows if $a$ is good that $2a$ is also good. Indeed, consider a sequence of super-integer triangles showing that if $5$ is good then $a$ is good. Then the sequence of super-integer triangles of double the size of their edges show that since $10$ is good then $2a$ is good.

It easily follows that $12$, $16$, $20$ and $24$ are good. From $(5, 12, 13)$ it follows that $13$ and therefore also $26$ are good. From $(11\{12\}, 13, 20)$ and $(21\{12\}, 13, 20)$ it follows that $11$ and $21$ are good. From $(20, 21, 29)$ it follows that $29$ is good. From $(6\{20\}, 25, 29)$ it follows that $25$ is good.

We will say that a positive integer is nice if it is either good or equal to $1$ or $2$.

**Claim 1.** If $a$ is good and $b$ is nice then $ab$ is good.

**Proof of Claim.** The claim is trivial if $b = 1$ and we already proved the case $b = 2$. So assume that $b$ is good. Pick a sequence of super-integer triangles which shows that if $5$ is good then $b$ is good. Then the sequence of super-integer triangles $5$ times the size of their edges shows that since $25$ is good then $5b$ is also good. Now pick a sequence of super-integer triangles which shows that if $5$ is good then $b$ is good. Then the sequence of super-integer triangles $b$ times the size of their edges shows that since $5a$ is good then $ab$ is also good. $\square$

Next, from $(15, 20, 25)$ and $(7, 24, 25)$ we get that $15$, $7$ and therefore $14$ are good. From $(9, 12, 15)$ and $(8, 15, 17)$ we get that $9$, $17$ and therefore $18$ are good and finally from $(3\{24\}, 25, 26)$ and then $(3, 4, 5)$ we get that $3$ and $4$ are good.

We now have that all integers from $3$ to $18$ are good. To prove that the remaining integers larger than $18$ are good, we will proceed by strong induction. Assume that all integers from $3$ to $n-1$ are good for $n \ge 19$.

**Case 1.** If $n = 2m$ is even, then $3 \le m \le n-1$ so $m$ is good. By Claim 1, $n = 2m$ is also good.

**Case 2.** If $n$ is odd and composite, say $n = ab$, with $a, b > 1$, then $3 \le a, b \le n-1$ so $a, b$ are good. By Claim 1, $n = ab$ is also good.

**Case 3.** If $n$ is an odd prime of the form $4k + 1$, then by Fermat's sum of two squares theorem we can write $n = a^2 + b^2$. We may assume $a > b$. ($a \neq b$ as $n$ is prime.) Consider the triangle $(a^2 - b^2, 2ab, a^2 + b^2)$. This is a super-integer triangle since it is a right-angled triangle. We have $3 \le a^2 - b^2 \le n - 1$ so $a^2 - b^2$ is good. We also have $3 \le 2ab < a^2 + b^2 = n$ so $2ab$ is also good. Thus $n = a^2 + b^2$ is good as well.

**Case 4.** Assume $n$ is an odd prime of the form $4k + 3$. Note that $4k + 4$ is good by Case 1 as $2k + 2 < 4k + 3$. We also have that $4k + 5$ is good either by Case 2 (if it is composite) or by Case 3 (if it is prime) except if $4k + 5$ is a prime equal to $a^2 + 1$. (Because in this case, to use Case 3 we would need that $a^2 - 1 = n$ is good which is what we are trying to prove. But in this exceptional case $n = a^2 - 1 = (a - 1)(a + 1)$ is not prime.)

We will make use of the following Claim:

**Claim 2.** Let $a, b, \ell$ be positive integers such that $\ell > 1$ and $a \neq b$. If $\ell - 1, |a - b|, a, b$ are nice, and $\ell, a + b, a^2\ell + b^2$ are good, then $a^2\ell^2 + b^2$ is good.

**Proof of Claim.** By Claim 1, the numbers $|a^2 - b^2| = |a - b|(a + b)$ and $2ab$ are good. From the right-angled triangle $(2ab, |a^2 - b^2|, a^2 + b^2)$ it follows that $a^2 + b^2$ is good. So by Claim 1 $\ell(a^2 + b^2)$ is good. By Claim 1 $(\ell - 1)(a^2\ell + b^2)$ is also good. Finally, from the triangle $((\ell - 1)(a^2\ell + b^2) \{2\ell ab\}, \ell(a^2 + b^2), a^2\ell^2 + b^2)$, we get that $a^2\ell^2 + b^2$ is good. $\square$

From Claim 2 with $a = 2$, $b = 1$ and $\ell = k + 1$ to obtain that
$$
2^2(k+1)^2 + 1^2 = 4k^2 + 8k + 5 = 4(k+1) + (2k+1)^2
$$
is good. From Claim 2 with $a = 2$, $b = 2k + 1$ and $\ell = k + 1$ we obtain that
$$
2^2(k+1)^2 + (2k+1)^2 = (2k+2)^2 + (2k+1)^2
$$
is good. Since from Claim 1, $2(2k + 1)(2k + 2)$ is good, then from the right-angled triangle $(4k+3, 2(2k+1)(2k+2), (2k+2)^2 + (2k+1)^2)$ we finally deduce that $4k+3$ is good as required.

