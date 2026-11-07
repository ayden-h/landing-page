---
title: "Olympiad Number Theory: Collected Problems"
author: "Ayden Bi"
date: "Research edition • 6 November 2026"
lang: en-US
---

# Scope and attribution {.unnumbered}

This volume contains sixteen restated problems from the checked core, followed by 477 source-provided statements. It is a partial collection. Source classifications, numbering and transcriptions are not all independently verified. Mixed-domain records may occur in other subject volumes. The corresponding proofs are in the separate worked volume and the individually labeled source-solution files.

The source statements are reproduced under MathNet's CC BY 4.0 fallback where recovered metadata contains no explicit original rights assertion. The complete package preserves original booklet credits and metadata. Figure-dependent statements and records with uncertain or explicit original rights remain source pointers. Original source wording is retained apart from logged typesetting compatibility repairs. The checked core is separately restated and corrected.

MathNet: Shaden Alshammari, Kevin Wen, Abrar Zainal, Mark Hamilton, Navid Safaei, Sultan Albarakati, William T. Freeman and Antonio Torralba, *MathNet: A Global Multimodal Benchmark for Mathematical Reasoning and Retrieval*, ICLR 2026. Sources: https://mathnet.mit.edu/ ; https://huggingface.co/datasets/ShadenA/MathNet ; https://creativecommons.org/licenses/by/4.0/ . Original source contributors are credited in the ledger and individual problem files.

Read Coverage_Report.md for exact counts, historical gaps, withheld records and the distinction between actual contests, shortlists and selection material. The author credit identifies this compiled edition and its authored expositions, not authorship of the historical problems.

# The sixteen checked-core problems

## N01. A valuation makes the square small

**Source:** IMO shortlist 2006, N1. **Record:** `imo_2006_bc0ae3`.

Determine all integer solutions of $1+2^x+2^{2x+1}=y^2$.

## N02. Sample digits at exponentially growing places

**Source:** IMO shortlist 2006, N2. **Record:** `imo_2006_472d44`.

A decimal expansion represents a rational number in $(0,1)$. Form a new decimal by taking its digits in positions $2,4,8,16,\ldots$. Prove that the new number is rational (possibly an endpoint such as zero).

## N03. One modulus replaces all moduli

**Source:** IMO shortlist 2007, N2. **Record:** `imo_2007_886291`.

Integers $b,n>1$ satisfy: for every integer $k>1$, some integer $a$ has $a^n\equiv b\pmod k$. Prove that $b$ is an integer $n$th power.

## N04. Multiply three divided differences

**Source:** IMO shortlist 2008, N1. **Record:** `imo_2008_dbd5d0`.

For positive integer $n$, prime $p$, and arbitrary integers $a,b,c$, suppose $a^n+pb=b^n+pc=c^n+pa$. Prove $a=b=c$.

## N05. Simultaneous factorial valuations

**Source:** IMO shortlist 2007, N7. **Record:** `imo_2007_e1c86b`.

For any positive integer $d$ and finitely many primes $p_1,\ldots,p_k$, show that infinitely many $n>0$ satisfy $d\mid v_{p_i}(n!)$ for every $i$.

## N06. Finite agreement versus eternal agreement

**Source:** IMO shortlist 2009, N2. **Record:** `imo_2009_cf1420`.

Call an integer balanced when its number of prime factors, counted with multiplicity, is even; include $1$. (a) Find distinct positive $a,b$ for which $(n+a)(n+b)$ is balanced for all $1\le n\le50$. (b) Prove that if this holds for every positive $n$, then $a=b$.

## N07. Divisibility squeezes a function

**Source:** IMO shortlist 2013, N1. **Record:** `imo_2013_a67bc4`.

Find all $f:\mathbb Z_{>0}\to\mathbb Z_{>0}$ satisfying $m^2+f(n)\mid mf(m)+n$ for all positive $m,n$.

## N08. Two primes eliminate a factorial

**Source:** IMO 2019, Problem 4; shortlist N1. **Record:** `imo_2019_8eb868`.

Find positive integers $m,n$ with $m!=\prod_{i=0}^{n-1}(2^n-2^i)$.

## N09. A cubic equation collapses to a short list

**Source:** IMO shortlist 2019, N2. **Record:** `imo_2019_199a44`.

Classify positive integer triples satisfying $a^3+b^3+c^3=(abc)^2$.

## N10. Polynomial-root closure fills the integers

**Source:** IMO shortlist 2019, N3. **Record:** `imo_2019_05dd86`.

A set $S\subseteq\mathbb Z$ contains $2^a-2^b$ for all positive $a,b$ and contains every integer root of every nonconstant polynomial with coefficients in $S$. Prove $S=\mathbb Z$.

## N11. Classify the good binomial indices

**Source:** IMO shortlist 2019, N5. **Record:** `imo_2019_aedde5`.

For fixed positive $a$, call $b>0$ good if $an+1\mid\binom{an}{b}-1$ whenever $an\ge b$. If $b$ is good and $b+2$ is not, prove $b+1$ prime.

## N12. A Jacobi-symbol obstruction

**Source:** IMO shortlist 2022, N8. **Record:** `imo_2022_264ed6`.

Show $2^n+65$ never divides $5^n-3^n$ for positive integer $n$.

## N13. Reverse the ordered divisor list

**Source:** IMO shortlist 2023, N1. **Record:** `imo_2023_2e005b`.

Let $1=d_1<\cdots<d_k=n$ be all positive divisors of a composite $n$. Classify $n$ for which $d_i\mid d_{i+1}+d_{i+2}$ for $1\le i\le k-2$.

## N14. The odd part controls all divisors

**Source:** IMO shortlist 2024, N1. **Record:** `imo_2024_268bb8`.

Find positive $n$ such that every divisor $d$ of $n$ has either $d+1\mid n$ or $d+1$ prime.

## N15. Vieta jumping with every inequality checked

**Source:** IMO 1988, Problem 6. Official paper: [PDF](https://www.imo-official.org/assets/documents/problems/1988/1988_eng.pdf).

For positive integers $a,b$ with $ab+1\mid a^2+b^2$, prove that $(a^2+b^2)/(ab+1)$ is a perfect square.

## N16. Arithmetic descent in a nonlinear recurrence

**Source:** IMO 2017, Problem 1. Official paper: [PDF](https://www.imo-official.org/assets/documents/problems/2017/2017_eng.pdf).

Start at an integer $a_0>1$. Replace a square by its positive square root and replace a nonsquare by that number plus three. Determine which initial values cause some integer to occur infinitely often.


# APMO source statements

## 1989 — 2

**Record:** `apm_1989_7c3bdc`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1989_7c3bdc.json.gz).

Prove that the equation
$$
6\left(6 a^{2}+3 b^{2}+c^{2}\right)=5 n^{2}
$$
has no solutions in integers except $a=b=c=n=0$.


## 1993 — 4

**Record:** `apm_1993_7c1d15`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1993_7c1d15.json.gz).

Determine all positive integers $n$ for which the equation
$$
x^{n}+(2+x)^{n}+(2-x)^{n}=0
$$
has an integer as a solution.


## 1994 — 4

**Record:** `apm_1994_74e082`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1994_74e082.json.gz).

Is there an infinite set of points in the plane such that no three points are collinear, and the distance between any two points is rational?


## 1994 — 3

**Record:** `apm_1994_d14140`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1994_d14140.json.gz).

Let $n$ be an integer of the form $a^{2}+b^{2}$, where $a$ and $b$ are relatively prime integers and such that if $p$ is a prime, $p \leq \sqrt{n}$, then $p$ divides $a b$. Determine all such $n$.

Answer: $n=2,5,13$.


## 2003 — 3

**Record:** `apm_2003_9d299c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2003_9d299c.json.gz).

Let $k \geq 14$ be an integer, and let $p_{k}$ be the largest prime number which is strictly less than $k$. You may assume that $p_{k} \geq 3k/4$. Let $n$ be a composite integer. Prove:

a. if $n = 2p_{k}$, then $n$ does not divide $(n-k)!$;

b. if $n > 2p_{k}$, then $n$ divides $(n-k)!$.


## 2004 — 1

**Record:** `apm_2004_1843da`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2004_1843da.json.gz).

Determine all finite nonempty sets $S$ of positive integers satisfying
$$
\frac{i+j}{(i, j)} \quad \text{is an element of } S \text{ for all } i, j \text{ in } S,
$$
where $(i, j)$ is the greatest common divisor of $i$ and $j$.


## 2005 — Problem 3

**Record:** `apm_2005_252bb2`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2005_252bb2.json.gz).

Prove that there exists a triangle which can be cut into 2005 congruent triangles.


## 2005 — Problem 1

**Record:** `apm_2005_f8ae2c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2005_f8ae2c.json.gz).

Prove that for every irrational real number $a$, there are irrational real numbers $b$ and $b^{\prime}$ so that $a+b$ and $a b^{\prime}$ are both rational while $a b$ and $a+b^{\prime}$ are both irrational.


## 2007 — Problem 1

**Record:** `apm_2007_ca2bc8`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2007_ca2bc8.json.gz).

Let $S$ be a set of 9 distinct integers all of whose prime factors are at most $3$. Prove that $S$ contains 3 distinct integers such that their product is a perfect cube.


## 2008 — Problem 5

**Record:** `apm_2008_eadb1c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2008_eadb1c.json.gz).

Let $a$, $b$, $c$ be integers satisfying $0 < a < c - 1$ and $1 < b < c$. For each $k$, $0 \leq k \leq a$, let $r_{k}$, $0 \leq r_{k} < c$, be the remainder of $k b$ when divided by $c$. Prove that the two sets $\{r_{0}, r_{1}, r_{2}, \ldots, r_{a}\}$ and $\{0, 1, 2, \ldots, a\}$ are different.


## 2010 — 2

**Record:** `apm_2010_deb386`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2010_deb386.json.gz).

For a positive integer $k$, call an integer a pure $k$-th power if it can be represented as $m^{k}$ for some integer $m$. Show that for every positive integer $n$ there exist $n$ distinct positive integers such that their sum is a pure $2009$-th power, and their product is a pure $2010$-th power.


## 2016 — 2

**Record:** `apm_2016_55401b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2016_55401b.json.gz).

A positive integer is called fancy if it can be expressed in the form
$$
2^{a_{1}} + 2^{a_{2}} + \cdots + 2^{a_{100}}
$$
where $a_{1}, a_{2}, \ldots, a_{100}$ are non-negative integers that are not necessarily distinct.
Find the smallest positive integer $n$ such that no multiple of $n$ is a fancy number.


## 2019 — 4

**Record:** `apm_2019_3a3563`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2019_3a3563.json.gz).

Consider a $2018 \times 2019$ board with integers in each unit square. Two unit squares are said to be neighbours if they share a common edge. In each turn, you choose some unit squares. Then for each chosen unit square the average of all its neighbours is calculated. Finally, after these calculations are done, the number in each chosen unit square is replaced by the corresponding average. Is it always possible to make the numbers in all squares become the same after finitely many turns?


## 2020 — 3

**Record:** `apm_2020_f3d3c1`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2020_f3d3c1.json.gz).

Determine all positive integers $k$ for which there exist a positive integer $m$ and a set $S$ of positive integers such that any integer $n>m$ can be written as a sum of distinct elements of $S$ in exactly $k$ ways.


## 2022 — 1

**Record:** `apm_2022_789d8c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2022_789d8c.json.gz).

Find all pairs $(a, b)$ of positive integers such that $a^{3}$ is a multiple of $b^{2}$ and $b-1$ is a multiple of $a-1$. Note: An integer $n$ is said to be a multiple of an integer $m$ if there is an integer $k$ such that $n=k m$.


## 2022 — 3

**Record:** `apm_2022_a90b58`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2022_a90b58.json.gz).

Find all positive integers $k<202$ for which there exists a positive integer $n$ such that
$$
\left\{\frac{n}{202}\right\}+\left\{\frac{2 n}{202}\right\}+\cdots+\left\{\frac{k n}{202}\right\}=\frac{k}{2}
$$
where $\{x\}$ denote the fractional part of $x$.
Note: $\{x\}$ denotes the real number $k$ with $0 \leq k<1$ such that $x-k$ is an integer.


## 2024 — 4

**Record:** `apm_2024_299020`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2024_299020.json.gz).

Prove that for every positive integer $t$ there is a unique permutation $a_{0}, a_{1}, \ldots, a_{t-1}$ of $0,1, \ldots, t-1$ such that, for every $0 \leq i \leq t-1$, the binomial coefficient $\binom{t+i}{2 a_{i}}$ is odd and $2 a_{i} \neq t+i$.


## 2025 — 5

**Record:** `apm_2025_092270`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2025_092270.json.gz).

Consider an infinite sequence $a_{1}, a_{2}, \ldots$ of positive integers such that
$$
100!\left(a_{m}+a_{m+1}+\cdots+a_{n}\right) \quad \text{ is a multiple of } a_{n-m+1} a_{n+m}
$$
for all positive integers $m, n$ such that $m \leq n$.
Prove that the sequence is either bounded or linear.

Observation: A sequence of positive integers is bounded if there exists a constant $N$ such that $a_{n}<N$ for all $n \in \mathbb{Z}_{>0}$. A sequence is linear if $a_{n}=n \cdot a_{1}$ for all $n \in \mathbb{Z}_{>0}$.


## 2025 — 3

**Record:** `apm_2025_7619c0`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2025_7619c0.json.gz).

Let $P(x)$ be a non-constant polynomial with integer coefficients such that $P(0) \neq 0$. Let $a_{1}, a_{2}, a_{3}, \ldots$ be an infinite sequence of integers such that $P(i-j)$ divides $a_{i}-a_{j}$ for all distinct positive integers $i, j$. Prove that the sequence $a_{1}, a_{2}, a_{3}, \ldots$ must be constant, that is, $a_{n}$ equals a constant $c$ for all $n$ positive integer.



# BMO source statements

## 2004 — Problema 2

**Record:** `rou_2004_97964e`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2004_97964e.json.gz).

Pentru orice număr natural nenul $n$, suma $1+\frac{1}{2}+\ldots+\frac{1}{n}$ se scrie sub forma $\frac{p_{n}}{q_{n}}$ unde $p_{n}$ şi $q_{n}$ sunt numere naturale prime între ele.

a. Arătați că $p_{67}$ nu se divide cu 3.

b. Determinați toate numerele naturale nenule $n$, pentru care $p_{n}$ este divizibil cu 3.


## 2004 — 2.

**Record:** `rou_2004_bc7201`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2004_bc7201.json.gz).

Rezolvaţi în mulţimea numerelor prime ecuaţia
$$
x^{y} - y^{x} = x y^{2} - 19
$$


## 2008 — 5

**Record:** `mkd_2008_1e28f4`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_1e28f4.json.gz).

Prove that the sum of six consecutive positive integers, such that each of them is not divisible with $7$, is divisible with $21$ but it's not divisible with $42$. Find six such numbers which sum is a four-digit number that is a square of a positive integer.


## 2008 — 2

**Record:** `mkd_2008_262618`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_262618.json.gz).

Which digit has to be put in the place of the star in the number $2008*$ in order to be divisible with $6$?


## 2008 — 2

**Record:** `mkd_2008_2b2e13`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_2b2e13.json.gz).

a) Find the smallest positive integer which multiplied by $2520$ gives a square of a positive integer.

b) Prove that the sum of two consecutive odd integers is divisible with $4$.


## 2008 — 3

**Record:** `mkd_2008_3ec66c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_3ec66c.json.gz).

Let $n$ be a positive integer. Does $(2n-3)(2n-1)(2n+1)(2n+3)+16$ equal the square of a positive integer? Does the number $2005 \times 2007 \times 2009 \times 2011 + 16$ equal the square of a positive integer?


## 2008 — 4

**Record:** `mkd_2008_523d54`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_523d54.json.gz).

Let $c$ be a positive integer. The sequence $a_1, a_2, \dots, a_n, \dots$ is defined by $a_1 = c$, and $a_{n+1} = a_n^2 + a_n + c^3$, for every positive integer $n$. Find all values of $c$ for which there exist some integers $k \ge 1$ and $m \ge 2$, such that $a_k^2 + c^3$ is the $m$th power of some positive integer.


## 2008 — 1

**Record:** `mkd_2008_5246a5`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_5246a5.json.gz).

Prove that if $a+\frac{b}{a}-\frac{1}{b}$ is an integer, then it is a perfect square, where $a,b \in \mathbb{N}$.


## 2008 — 3

**Record:** `mkd_2008_5d913f`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_5d913f.json.gz).

One school has less than $400$ students in $6$th grade. They are divided in several classes. Six of them have equal number of students and together they have more than $150$ students. In the remaining classes there are $15\%$ more students than in these six classes together. How many students of $6$th grade are there in the school?


## 2008 — 3. (B)

**Record:** `mkd_2008_5f4949`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_5f4949.json.gz).

Prove that if $n$ is an odd natural number, then $n^3 + 3n^2 - n - 3$ is divisible by 48.


## 2008 — 3

**Record:** `mkd_2008_5fde01`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_5fde01.json.gz).

On training in a football club there were 225 children and 105 balls. The children were split in few equal groups. The coaches gave to each group equal number of balls. How many groups were formed and how many balls did every group get? How many solutions does the problem have?


## 2008 — 1. (A)

**Record:** `mkd_2008_60b4d0`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_60b4d0.json.gz).

The sequence $49$, $4489$, $444889$, ... is given so that the number $48$ is put in the middle of the preceding term. Prove that every term in the sequence is perfect square.


## 2008 — 1

**Record:** `mkd_2008_7ac7f5`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_7ac7f5.json.gz).

The ratios $\frac{3a5b}{36}$ and $\frac{4c7d}{45}$ are positive integers, where $a, b, c, d$ are digits. Order all numbers of this kind by size.


## 2008 — 3

**Record:** `mkd_2008_8fbac0`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_8fbac0.json.gz).

Let $n$ be a positive integer. The rectangle $ABCD$ with side lengths $AB = 90n + 1$ and $BC = 90n + 5$ is partitioned into unit squares with sides parallel to the sides of $ABCD$. Let $S$ be the set of all points which are vertices of these unit squares. Prove that the number of lines which pass through at least two points from $S$ is divisible by 4.


## 2008 — 1

**Record:** `mkd_2008_90b227`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_90b227.json.gz).

Is the sum $1^{2008} + 2^{2008} + 3^{2008} + 4^{2008} + 5^{2008} + 6^{2008}$ divisible with $5$? Explain your answer.


## 2008 — 3. (A)

**Record:** `mkd_2008_af49f5`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_af49f5.json.gz).

The roots of the quadratic equation $x^2 + p x + q = 0$ are integers. Find the numbers $p$ and $q$ and the roots of the equation, if $p + q = 198$.


## 2008 — 1. (AB)

**Record:** `mkd_2008_b40ab1`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_b40ab1.json.gz).

Solve the equation $a^2 + 2ab + 2b^2 = 13$, where $a, b \in \mathbb{Z}$.


## 2008 — 4

**Record:** `mkd_2008_bfdaf7`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_bfdaf7.json.gz).

Find all triples of positive integers $(x, y, z)$ such that
$$
xyz + xy + yz + zx + x + y + z = 243.
$$


## 2008 — 1

**Record:** `mkd_2008_decec2`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_decec2.json.gz).

How many numbers divisible by $30^{2008}$ are not divisible by $20^{2007}$?


## 2008 — 3

**Record:** `mkd_2008_e7301f`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_e7301f.json.gz).

Find the digits $A$, $B$, $C$ such that the given multiplication procedure is correct:
$$
\begin{array}{cc}
\overline{ABC} \cdot \overline{BAC} \\
\multicolumn{2}{c}{---} \\
--A & \\
\multicolumn{2}{c}{---B} \\
\end{array}
$$
Where $\overline{ABC} \cdot C = \overline{---A}$, $\overline{ABC} \cdot A = \overline{---A}$, $\overline{ABC} \cdot B = \overline{---B}$. Distinct letters denote distinct digits and every "-" denotes one digit.


## 2008 — 1

**Record:** `mkd_2008_f95407`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_f95407.json.gz).

Determine the sum of all odd 3-digit numbers whose product of digits is equal to $140$.


## 2008 — 4

**Record:** `mkd_2008_fbf396`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_fbf396.json.gz).

Find all three digit numbers equal to the sum of the factorials of their digits.


## 2009 — 1

**Record:** `bmo_2009_bfe224`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2009_bfe224.json.gz).

Find all integer solutions of the equation
$$
3^{x} - 5^{y} = z^{2}
$$


## 2009 — 4

**Record:** `grc_2009_78d09d`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/greece/grc_2009_78d09d.json.gz).

Let $\mathbb{N}^* = \{1,2,3,...\}$ be the set of positive integers. Find all functions $f: \mathbb{N}^* \rightarrow \mathbb{N}^*$ such that
$$
f(f(m)^2 + 2f(n)^2) = m^2 + 2n^2, \text{ for all } m, n \in \mathbb{N}^*.
$$


## 2009 — 5.

**Record:** `mkd_2009_0f7a73`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_0f7a73.json.gz).

In the set of integers, solve the equation
$$
x^{2010} - 2006 = 4y^{2009} + 4y^{2008} + 2007y.
$$


## 2009 — 1.

**Record:** `mkd_2009_410ade`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_410ade.json.gz).

Да се определат сите природни броеви $x$, $y$ и $z$ за кои $1 + 2^x 3^y = z^2$.


## 2009 — 3А.

**Record:** `mkd_2009_573297`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_573297.json.gz).

Дадени се 21 плочка во облик на квадратче, со иста димензија. На четири плочки е запишан бројот 1; на две плочки е запишан бројот 2; на седум плочки е запишан бројот 3; на 8 плочки е запишан бројот 4. Користејќи 20 од тие плочки, Димитар формирал правоаголник со димензии 4 на 5. За формираниот правоаголник збирот на броевите во секоја редица е иста, и збирот на броевите во секоја колона е иста. Кој број стои на неискористената плочка?


## 2009 — 1.

**Record:** `mkd_2009_a046c9`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_a046c9.json.gz).

Find all positive integers $x$, $y$ and $z$ such that $1 + 2^x 3^y = z^2$.


## 2009 — 1Б.

**Record:** `mkd_2009_a0c7fc`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_a0c7fc.json.gz).

Нека $a$ и $b$ се природни броеви. Докажи дека $a^2 + ab + b^2$ е делител на бројот $(a+b)^6 - a^6$.


## 2009 — 1А.

**Record:** `mkd_2009_b78c29`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_b78c29.json.gz).

Броевите $m$ и $n$ се взаемно прости. Дропката $\frac{3n-m}{5n+2m}$ може да се скрати со некој природен број. Определи го бројот со кој коже да се скрати.


## 2009 — 1А.

**Record:** `mkd_2009_eb1908`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_eb1908.json.gz).

Определи ги сите цели броеви $x$, за кои $\log_2(x^2 - 4x - 1)$ е исто така цел број.


## 2009 — 3Б.

**Record:** `mkd_2009_ee8242`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_ee8242.json.gz).

Во равенството $25!=15\ 511 \times 10\ 043\ 330\ \text{у}85\ 984\ z00\ 000$ определи ги цифрите $x,y$ и $z$ за да тоа е точно.


## 2009 — 1АБ.

**Record:** `mkd_2009_f6a112`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_f6a112.json.gz).

Аритметичката прогресија се состои од цели броеви. Збирот на првите $n$ членови на прогресијата е степен на бројот 2. Докажи дека и $n$ е степен на бројот 2.


## 2010 — Problem 4.

**Record:** `mkd_2010_746cb3`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2010_746cb3.json.gz).

For each integer $n$ ($n \ge 2$) let $f(n)$ denote the sum of all positive integers that are at most $n$ and not relatively prime to $n$.
Prove that $f(n+p) \neq f(n)$ for each such $n$ and for every prime $p$.


## 2011 — 3

**Record:** `mkd_2011_88da3c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2011_88da3c.json.gz).

Find all natural numbers $n$ for which each natural number having $n-1$ digits '1' and one digit '7' in its decimal representation is prime.


## 2011 — 3

**Record:** `mkd_2011_c1004b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2011_c1004b.json.gz).

Let $S$ be a finite set of positive integers which has the following property: if $x$ is a member of $S$, then so are all positive divisors of $x$. A non-empty subset $T$ of $S$ is a good if whenever $x, y \in T$ and $x < y$, the ratio $y/x$ is a power of a prime number. A non-empty subset $T$ of $S$ is bad if whenever $x, y \in T$ and $x < y$, the ratio $y/x$ is not a power of a prime number. We agree that a singleton subset of $S$ is both good and bad. Let $k$ be the largest possible size of a good subset of $S$. Prove that $k$ is also the smallest number of pairwise-disjoint bad subset whose union is $S$.


## 2012 — 4

**Record:** `mkd_2012_f9bf27`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2012_f9bf27.json.gz).

Let $\mathbb{Z}^+$ be the set of all positive integers. Find all functions $f: \mathbb{Z}^+ \to \mathbb{Z}^+$ such that $f(n!) = f(n)!$, and $m-n$ divides $f(m)-f(n)$ for all distinct positive integers $m$ and $n$.


## 2013 — Problem 2.

**Record:** `grc_2013_833126`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/greece/grc_2013_833126.json.gz).

Determine all positive integers $x, y$ and $z$ such that
$$
x^5 + 4y^2 = 2013^2.
$$


## 2013 — Problem 2

**Record:** `rou_2013_42c8a1`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2013_42c8a1.json.gz).

Determine all positive integers $x$, $y$ and $z$ such that
$$
x^{5} + 4^{y} = 2013^{z}
$$

Problem:
Să se determine toate numerele naturale nenule $x$, $y$ şi $z$ astfel încât
$$
x^{5} + 4^{y} = 2013^{z}
$$


## 2014 — 2

**Record:** `mkd_2014_94c000`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2014_94c000.json.gz).

A special number is a positive integer $n$ for which there exist positive integer $a$, $b$, $c$ and $d$ with
$$
n = \frac{a^3 + 2b^3}{c^3 + 2d^3}
$$
Prove that
(a) There are infinitely many special numbers;
(b) 2014 is not a special number.


## 2015 — NT5.

**Record:** `bmo_2015_0b84eb`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2015_0b84eb.json.gz).

For an arbitrary positive integer $s$, we denote by $v_2(s)$ the exponent of the biggest power of $2$ which divides $s$, i.e. $2^{v_2(s)}$ is a divisor of $s$, but $2^{v_2(s)+1}$ is not. Show that for every positive integer $m$ the following equality holds:
$$
v_2\left(\prod_{n=1}^{2^m} \binom{2n}{n}\right) = m2^{m-1} + 1.
$$


## 2015 — NT2.

**Record:** `bmo_2015_2acf30`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2015_2acf30.json.gz).

Define the sequence $(a_n)_{n \ge 0}$ by $a_0 = 0$, $a_1 = 1$, $a_2 = 2$, $a_3 = 6$, and
$$
a_{n+4} = 2a_{n+3} + a_{n+2} - 2a_{n+1} - a_n, \quad n \ge 0.
$$

Prove that $n^2$ divides $a_n$ for infinitely many positive integers $n$.


## 2015 — NT6.

**Record:** `bmo_2015_5cab36`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2015_5cab36.json.gz).

Prove that among any $20$ consecutive positive integers there exists a number $d$ such that for each positive integer $n$ we have the inequality
$$
n\sqrt{d}\{n\sqrt{d}\} > \frac{5}{2}
$$
where $\{x\}$ denotes the fractional part of the real number $x$.


## 2015 — NT4.

**Record:** `bmo_2015_663a0f`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2015_663a0f.json.gz).

Find all the pairs positive numbers $(x, y)$ with the following property:
If $\alpha, \beta$ are relatively prime and positive divisors of the number $x^3 + y^3$ then $\alpha + \beta - 1$ is a divisor of $x^3 + y^3$.


## 2015 — NT3.

**Record:** `bmo_2015_b800ec`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2015_b800ec.json.gz).

Let $a$ be a positive integer. For all positive integers $n$, we define
$$
a_n = 1 + a + a^2 + \dots + a^{n-1}.
$$
Let also $s, t$ be two different positive integers satisfying the following property: If $p$ is a prime divisor of $s-t$ then $p$ also divides $a-1$. Prove that the number
$$
\frac{a_s - a_t}{s - t}
$$
is an integer.


## 2015 — NT7.

**Record:** `bmo_2015_f4f776`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2015_f4f776.json.gz).

Two positive integers $m$ and $n$ will be called *anagrams*, if each decimal digit $a$ appears as many times in the decimal representation of $m$ as in that of $n$. Is it possible to find four different positive integers such that each of them is an anagram of the sum of the other three?


## 2017 — NT2

**Record:** `bmo_2017_358dfc`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2017_358dfc.json.gz).

Find all functions $f: \mathbb{Z}_{>0} \to \mathbb{Z}_{>0}$ such that the number $x f(x) + f^2(y) + 2x f(y)$ is a perfect square for all positive integers $x, y$.


## 2017 — NT1

**Record:** `bmo_2017_451f8d`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2017_451f8d.json.gz).

Find all pairs $(x, y)$ of positive integers such that
$$
x^3 + y^3 = x^2 + 42xy + y^2.
$$


## 2017 — NT4

**Record:** `bmo_2017_61978a`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2017_61978a.json.gz).

Find all pairs of positive integers $(x, y)$, such that $x^2$ is divisible by $2xy^2 - y^3 + 1$.


## 2017 — NT3

**Record:** `bmo_2017_c8589e`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2017_c8589e.json.gz).

Prove that for all positive integer $n$, there is a positive integer $m$, that $7^n \mid 3^m + 5^m - 1$.


## 2018 — 3

**Record:** `mkd_2018_3ac94a`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2018_3ac94a.json.gz).

Alice and Bob play the following game: They start with two non-empty piles of coins. Taking turns, with Alice playing first, each player chooses a pile with an even number of coins and moves half of this pile to the other pile. The game ends if a player cannot move, in which case the other player wins.
Determine all pairs $(a,b)$ of positive integers such that if initially the two piles have $a$ and $b$ coins respectively, then Bob has a winning strategy.


## 2018 — 4

**Record:** `mkd_2018_8a1269`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2018_8a1269.json.gz).

Find all primes $p$ and $q$ such that $3p^{q-1}$ divides $11^p+17^p$.



# BMO-SL source statements

## 2010 — NT2

**Record:** `bmo_2010_739d15`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2010_739d15.json.gz).

Find all pairs of integers $(x, y)$, such that $x^3 = 2y^2 + 1$.


## 2010 — C2

**Record:** `bmo_2010_82e1d0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2010_82e1d0.json.gz).

A grasshopper jumps on the plane from an integer point (point with all integer coordinates) to another integer point according to the following rules: His first jump is of length $\sqrt{98}$, his second jump is of length $\sqrt{149}$, his next jump is of length $\sqrt{98}$, and so on, alternatively. What is the least possible odd number of moves in which the grasshopper could return to his starting point?


## 2012 — N1

**Record:** `bmo_2012_46d8dc`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2012_46d8dc.json.gz).

A sequence $(a_n)_{n=1}^\infty$ of positive integers satisfies the condition $a_{n+1} = a_n + \tau(n)$ for all positive integers $n$ where $\tau(n)$ is the number of positive integer divisors of $n$. Determine whether two consecutive terms of this sequence can be perfect squares.


## 2012 — N2

**Record:** `bmo_2012_907bbf`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2012_907bbf.json.gz).

Let the sequences $(a_n)_{n=1}^\infty$ and $(b_n)_{n=1}^\infty$ satisfy $a_0 = b_0 = 1$, $a_n = 9a_{n-1} - 2b_{n-1}$ and $b_n = 2a_{n-1} + 4b_{n-1}$ for all positive integers $n$. Let $c_n = a_n + b_n$ for all positive integers $n$. Prove that there do not exist positive integers $k, r, m$ such that $c_r^2 = c_k c_m$.


## 2014 — A6

**Record:** `bmo_2014_2198db`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_2198db.json.gz).

The sequence $a_0, a_1, \dots$ is defined by the initial conditions $a_0 = 1$, $a_1 = 6$ and the recursion $a_{n+1} = 4a_n - a_{n-1} + 2$ for $n > 1$. Prove that $a_{2^k-1}$ has at least three prime factors for every positive integer $k > 3$.


## 2014 — N3

**Record:** `bmo_2014_35e42c`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_35e42c.json.gz).

Prove that there exist infinitely many non isosceles triangles with rational side lengths, rational lengths of altitudes, and perimeter equal to $3$.


## 2014 — N4

**Record:** `bmo_2014_46bb41`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_46bb41.json.gz).

A positive integer $n$ is called *super special* if it can be represented in the form $n = \frac{x^3 + 2y^3}{u^3 + 2v^3}$ for some positive integers $x, y, u, v$. Prove that:
(a) There are infinitely many super special positive integers;
(b) 2014 is not super special.


## 2014 — C2

**Record:** `bmo_2014_5daa9c`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_5daa9c.json.gz).

Let $M = \{1, 2, \dots, 2013\}$ and let $\Gamma$ be a circle. For every nonempty subset $\mathcal{A}$ of the set $M$, denote by $S(\mathcal{A})$ the sum of elements of the set $\mathcal{A}$, and define $S(\emptyset) = 0$ ($\emptyset$ is the empty set). Is it possible to join every subset $\mathcal{A}$ of $M$ with some point $A$ on the circle $\Gamma$ so that following conditions are fulfilled:
1. Different subsets are joined with different points;
2. All joined points are vertices of a regular polygon;
3. If $A_1, A_2, \dots, A_k$ are some of the joined points, $k > 2$, such that $A_1A_2 \dots A_k$ is a regular $k$-gon, then 2014 divides $S(\mathcal{A}_1) + S(\mathcal{A}_2) + \dots + S(\mathcal{A}_k)$?


## 2014 — N6

**Record:** `bmo_2014_8cd9b9`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_8cd9b9.json.gz).

Let $f: N \rightarrow N$ be a function from the positive integers to the positive integers for which $f(1) = 1$, $f(2n) = f(n)$ and $f(2n+1) = f(n)+f(n+1)$ for all $n \in N$. Prove that for any natural number $n$, the number of odd natural numbers $m$ such that $f(m) = n$ is equal to the number of positive integers not greater than $n$ having no common prime factors with $n$.


## 2014 — N2

**Record:** `bmo_2014_940992`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_940992.json.gz).

Let $p$ be a prime number and $x_1, x_2, \dots, x_p$ be integers. Show that if
$$
x_1^n + x_2^n + \dots + x_p^n \equiv 0 \pmod{p}
$$
for all positive integers $n$ then $x_1 \equiv x_2 \equiv \dots \equiv x_p \pmod{p}$.


## 2014 — A3

**Record:** `bmo_2014_96ebbd`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_96ebbd.json.gz).

The sequence $a_1, a_2, a_3, \dots$ is defined by $a_1 = a_2 = 1$, $a_{2n+1} = 2a_{2n} - a_n$ and $a_{2n+2} = 2a_{2n+1}$ for $n \in \mathbb{N}$. Prove that if $n > 3$ and $n - 3$ is divisible by 8 then $a_n$ is divisible by 5.


## 2014 — N1

**Record:** `bmo_2014_b41461`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_b41461.json.gz).

Let $n$ be a positive integer, $g(n)$ be the number of positive divisors of $n$ of the form $6k + 1$ and $h(n)$ be the number of positive divisors of $n$ of the form $6k - 1$, where $k$ is a nonnegative integer. Find all positive integers $n$ such that $g(n)$ and $h(n)$ have different parity.


## 2014 — N5

**Record:** `bmo_2014_ff005c`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_ff005c.json.gz).

Let $a, b, c, p, q, r$ be positive integers such that $a^p + b^q + c^r = a^q + b^r + c^p = a^r + b^p + c^q$.
Prove that $a = b = c$ or $p = q = r$.


## 2016 — C1.

**Record:** `bmo_2016_6d4fd5`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2016_6d4fd5.json.gz).

Let positive integers $K$ and $d$ be given. Prove that there exists a positive integer $n$ and a sequence of $K$ positive integers $b_1, b_2, \dots, b_K$ such that the number $n$ is a $d$-digit palindrome in all number bases $b_1, b_2, \dots, b_K$.


## 2016 — N5.

**Record:** `bmo_2016_715bc2`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2016_715bc2.json.gz).

A positive integer $n$ is *downhill* if its decimal representation $\overline{a_k a_{k-1} \dots a_0}$ satisfies $a_k \ge a_{k-1} \ge \dots \ge a_0$. A real-coefficient polynomial $P$ is *integer-valued* if $P(n)$ is an integer for all integer $n$, and *downhill-integer-valued* if $P(n)$ is an integer for all downhill positive integers $n$. Is it true that every downhill-integer-valued polynomial is also integer-valued?


## 2017 — A5

**Record:** `bmo_2017_3e1abd`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2017_3e1abd.json.gz).

Consider integers $m \ge 2$ and $n \ge 1$. Show that there is a polynomial $P(x)$ of degree equal to $n$ with integer coefficients such that $P(0), P(1), \dots, P(n)$ are all perfect powers of $m$.


## 2017 — A3

**Record:** `bmo_2017_7d83b0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2017_7d83b0.json.gz).

Find all the functions $f: \mathbb{N} \to \mathbb{N}$ such that:
$$
n + f(m) \mid f(n) + n f(m) \quad (1)
$$
for any $m, n \in \mathbb{N}$


## 2019 — TN1

**Record:** `bmo_2019_404973`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2019_404973.json.gz).

Let $\mathbb{P}$ be the set of all prime numbers. Find all functions $f: \mathbb{P} \to \mathbb{P}$ such that
$$
f(p)^{f(q)} + q^p = f(q)^{f(p)} + p^q
$$
holds for all $p, q \in \mathbb{P}$.


## 2019 — A1

**Record:** `bmo_2019_6e2bee`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2019_6e2bee.json.gz).

Let $a_0$ be an arbitrary positive integer. Let $\{a_n\}$ be an infinite sequence of positive integers such that for every positive integer $n$ the term $a_n$ is the smallest positive integer such that $a_0 + a_1 + \dots + a_n$ is divisible by $n$. Prove that there is a positive integer $N$ such that $a_{n+1} = a_n$ for all $n \ge N$.

Let $a_0$ be an arbitrary positive integer. Consider the infinite sequence $(a_n)_{n \ge 1}$, defined inductively as follows: given $a_0, a_1, \dots, a_{n-1}$ define the term $a_n$ as the smallest positive integer such that $a_0 + a_1 + \dots + a_n$ is divisible by $n$. Prove that there exists a positive integer $M$ such that $a_{n+1} = a_n$ for all $n \ge M$.


## 2019 — TN2

**Record:** `bmo_2019_a02111`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2019_a02111.json.gz).

Let $S \subset \{1, \dots, n\}$ be a nonempty set, where $n$ is a positive integer. We denote by $s$ the greatest common divisor of the elements of the set $S$. We assume that $s \neq 1$ and let $d$ be its smallest divisor greater than $1$. Let $T \subset \{1, \dots, n\}$ be a set such that $S \subset T$ and $|T| \geq 1 + \lfloor \frac{n}{d} \rfloor$. Prove that the greatest common divisor of the elements in $T$ is $1$.

Let $n$ ($n \geq 1$) be a positive integer and $U = \{1, \dots, n\}$. Let $S$ be a nonempty subset of $U$ and let $d$ ($d \neq 1$) be the smallest common divisor of all elements of the set $S$. Find the smallest positive integer $k$ such that for any subset $T$ of $U$, consisting of $k$ elements, with $S \subset T$, the greatest common divisor of all elements of $T$ is equal to $1$.


## 2020 — N2

**Record:** `bmo_2020_327627`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2020_327627.json.gz).

A number of $N$ children are at a party, and they sit in a circle to play a game of Pass the Parcel. Because the host has no other form of entertainment, the parcel has infinitely many layers. On turn $i$, starting with $i = 1$, the following two things happen in order:
(1) The parcel is passed $i^2$ positions clockwise; and
(2) The child currently holding the parcel unwraps a layer and claims the prize inside. For what values of $N$ will every child receive a prize?


## 2021 — C2

**Record:** `bmo_2021_958307`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2021_958307.json.gz).

Let $K$ and $N > K$ be fixed positive integers. Let $n$ be a positive integer and let $a_1, a_2, \dots, a_n$ be distinct integers. Suppose that whenever $m_1, m_2, \dots, m_n$ are integers, not all equal to $0$, such that $|m_i| \le K$ for each $i$, then the sum
$$
\sum_{i=1}^{n} m_i a_i
$$
is not divisible by $N$. What is the largest possible value of $n$?


## 2021 — N7

**Record:** `bmo_2021_ac9fb9`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2021_ac9fb9.json.gz).

A *super-integer* triangle is defined to be a triangle whose lengths of all sides and at least one height are positive integers. We will deem certain positive integer numbers to be *good* with the condition that if the lengths of two sides of a super-integer triangle are two (not necessarily different) good numbers, then the length of the remaining side is also a good number. Let $5$ be a good number. Prove that all integers larger than $2$ are good numbers.


## 2022 — C5.

**Record:** `bmo_2022_36e10e`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2022_36e10e.json.gz).

A cube of side length $2021$ is given. In how many ways can we place a $1 \times 1 \times 1$ cubelet on the border of this cube in such a way that the newly formed solid can be completely filled using $k \times 1 \times 1$, $1 \times k \times 1$ and $1 \times 1 \times k$ cuboids, for some $k \in \mathbb{N} \setminus \{1\}$?


## 2022 — N2.

**Record:** `bmo_2022_380ffa`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2022_380ffa.json.gz).

Let $a$, $b$, $n$ be positive integers such that:
(i) $a^{2021} \mid n$ and $b^{2021} \mid n$
(ii) $2022 \mid a - b$ and $a > b$.
Prove that there is a subset of the divisors of the number $n$ having sum of elements divisible by $2022$ but not by $2022^2$.


## 2022 — C1.

**Record:** `bmo_2022_9167c0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2022_9167c0.json.gz).

There are 100 positive integer numbers written on a board. At each step, Alex composes 50 fractions using each number written on the board exactly once, brings these fractions to their irreducible form, and then replaces the 100 numbers on the board with the new numerators and denominators to create 100 new numbers. Find the smallest positive integer $n$ such that regardless of the values of the initial 100 numbers, after $n$ steps Alex can arrange to have on the board only pairwise coprime numbers.


## 2022 — N4.

**Record:** `bmo_2022_977a4b`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2022_977a4b.json.gz).

A hare and a tortoise run in the same direction, at constant but different speeds, around the base of a tall square tower. They start together at the same vertex, and the run ends when both return to the initial vertex simultaneously for the first time. Suppose the hare runs with speed $1$, and the tortoise with speed less than $1$. For what rational numbers $x$ is it true that, if the tortoise runs with speed $x$, the fraction of the entire run for which the tortoise can see the hare is also $x$?


## 2023 — N2

**Record:** `bmo_2023_82c96f`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2023_82c96f.json.gz).

Find all positive integers $n$ such that there exist positive integers $a$, $b$, $c$ satisfying $\gcd(a, b, c) = 1$ and $a + b + c = \gcd(ab + c, ac - b) = n$.


## 2023 — N1

**Record:** `bmo_2023_8709be`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2023_8709be.json.gz).

For positive integers $a, b, c$ (not necessarily distinct), suppose that $a + bc$, $b + ca$, and $c + ab$ are all perfect squares. Prove that
$$
a^2(b + c) + b^2(c + a) + c^2(a + b) + 2abc
$$
can be written as the sum of two square numbers.


## 2023 — N3

**Record:** `bmo_2023_e5c358`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2023_e5c358.json.gz).

For each positive integer $n$, denote by $\omega(n)$ the number of prime divisors of $n$. Find all polynomials $f(x)$ with integer coefficients, such that if $n$ is a positive integer satisfying $\omega(n) > 2023^{2023}$, then $f(n)$ is also a positive integer with
$$
\omega(f(n)) \le \omega(n).
$$


## 2024 — N4.

**Record:** `bmo_2024_0c40d1`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2024_0c40d1.json.gz).

Let $k$ be a positive integer. Find all sequences $(a_n)_{n \ge 1}$ of positive integers such that
$$
a_{n+2}(a_{n+1} - k) = a_n(a_{n+1} + k)
$$
for all $n \ge 1$.


## 2024 — N2.

**Record:** `bmo_2024_12ce9d`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2024_12ce9d.json.gz).

Prove that for every integer $n$, the number $n^4 - 12n^2 + 144$ is not a perfect cube of an integer.


## 2024 — N5.

**Record:** `bmo_2024_3a17e7`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2024_3a17e7.json.gz).

Let $a$ and $b$ be distinct positive integers such that $3^a + 2$ is divisible by $3^b + 2$. Prove that $a > b^2$.


## 2024 — C4.

**Record:** `bmo_2024_3c60be`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2024_3c60be.json.gz).

Prove that for every positive integer $k$ there exists an integer $n$ and distinct primes $p_1, p_2, \dots, p_k$ such that, if $A(n)$ denotes the number of integers in $\{1, 2, \dots, n\}$ which are relatively prime to $p_1p_2\dots p_k$, then
$$
\left| n \left(1 - \frac{1}{p_1}\right) \left(1 - \frac{1}{p_2}\right) \cdots \left(1 - \frac{1}{p_k}\right) - A(n) \right| > 2^{k-3}.
$$


## 2024 — N1.

**Record:** `bmo_2024_54aaec`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2024_54aaec.json.gz).

Let $n$ be a fixed natural number and
$$
S_n = \{\overline{c_n c_{n-1} \dots c_1}_{(10)} \mid c_1, \dots, c_{n-1}, c_n \in \{1, 2, 3, 4\}\}.
$$
Are there distinct numbers $x$ and $y$, $x, y \in S_n$, such that $4^n \mid x - y$?


## 2024 — A2.

**Record:** `bmo_2024_c7a652`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2024_c7a652.json.gz).

Prove that there is a positive integer number $n$ such that the decimal representation of the number:
$$
\sum_{k=1}^{\lfloor \frac{n}{3} \rfloor} \binom{n}{3k} 8^k
$$
ends in 2023 digits 8.


## 2024 — N7.

**Record:** `bmo_2024_cfc998`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2024_cfc998.json.gz).

Let $a, b$ be positive integers such that $a + 1, b + 1$ and $ab$ are all perfect squares. Prove that $\text{gcd}(a, b) + 1$ is also a perfect square.


## 2025 — N1

**Record:** `bmo_2025_2f713f`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_2f713f.json.gz).

Let $k$ be a positive integer and let $n_1, n_2, \dots, n_k > 1$ be $k$ distinct integers such that
$$
n_1! + \dots + n_k! = a^{n_1}
$$
for some positive integer $a$. Prove that at least one of $n_1, n_2, \dots, n_k$ is prime.


## 2025 — N6

**Record:** `bmo_2025_613b0e`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_613b0e.json.gz).

Find all polynomials $P(x)$ with integer coefficients such that there exists a positive integer $N$ such that for all positive integers $n > N$ we have $P(n) > 0$ and
$$
n + P(n) \mid n^{P(n)} + P(n)^n.
$$


## 2025 — N5

**Record:** `bmo_2025_7480b3`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_7480b3.json.gz).

Let $k > 2$ be a given positive integer. Find all positive integers $d$, for which there exists a polynomial $P(x)$ with integer coefficients such that $\deg P(x) = d$ and $11^k \mid 2025^n + P(n)$ for all positive integers $n > k$.


## 2025 — N3

**Record:** `bmo_2025_75a6a6`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_75a6a6.json.gz).

Given a positive integer $k$, a pair of positive integers $(a, b)$ is said to be $k$-nice if $a \mid b^k + 1$ and $b \mid a^k + 1$. For which positive integers $k$ are there infinitely many $k$-nice pairs?


## 2025 — N2

**Record:** `bmo_2025_b9b8f0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_b9b8f0.json.gz).

A positive integer $n > 1$ is called good if there exists some permutation of the numbers $1, 2, 3, \dots, n$, denoted by $(a_1, a_2, a_3, \dots, a_n)$ such that $a_i$ and $a_{i+1}$ have different parities for every $1 \le i \le n-1$; and for every $1 \le k \le n$, the sum $a_1 + a_2 + \dots + a_k$ is a quadratic residue modulo $n$. Prove that there exist infinitely many good numbers, as well as infinitely many numbers which are not good.
*Remark: Here an integer $x$ is considered a quadratic residue modulo $n$ if there exists an integer $y$ such that $x \equiv y^2 \pmod{n}$.*


## 2025 — N4

**Record:** `bmo_2025_e84c87`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_e84c87.json.gz).

Let $a$, $b$ and $k$ be positive integers. Suppose that for any integer $n \ge 2025$ there exists a positive integer $x_n > n$ such that $x_n \mid n^2 + a$ and $x_n + k \mid n^2 + b$. Prove that $k = b - a$.



# CMO-China source statements

## 2023 — 1

**Record:** `chn_2023_b3eef6`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_b3eef6.json.gz).

Determine the smallest real number $\lambda$ with the following property: every positive integer $n$ can be written as a product $n = x_1x_2\cdots x_{2023}$, with each $x_i$ either a prime number or a positive integer that is less than or equal to $n^\lambda$.


## 2023 — 3

**Record:** `chn_2023_ee4f6e`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_ee4f6e.json.gz).

Fix a prime number $p \ge 5$, and put $\Omega = \{1, 2, \dots, p\}$. For any $x, y \in \Omega$, define
$$
r(x, y) = \begin{cases} y - x, & \text{if } y \ge x, \\ y - x + p, & \text{if } y < x. \end{cases}
$$
For a nonempty subset $A$ of $\Omega$, define
$$
f(A) = \sum_{x \in A} \sum_{y \in A} (r(x, y))^2.
$$
We say that a subset $A$ of $\Omega$ is *good* if $0 < |A| < p$ and for any subset $B$ of $\Omega$ with $|B| = |A|$, we have $f(B) \ge f(A)$.
Determine the maximal positive integer $L$, such that there exist pairwise distinct good subsets $A_1, A_2, \dots, A_L$ of $\Omega$ such that $A_1 \subset A_2 \subset \dots \subset A_L$.


## 2024 — 5

**Record:** `chn_2024_465231`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2024_465231.json.gz).

We say a prime number $p$ is “good”, if there exists a bijection $f$ from the set $\{0, 1, \dots, p-1\}$ to itself satisfying the following condition: for any pair of elements $a, b \in \{0, 1, \dots, p-1\}$, if $p \mid a^2 - b$, then $|f(a) - f(b)| \le 2024$. If no such bijection $f$ exists, we say that the prime $p$ is “bad”.

Prove that there exist infinitely many good primes, and there exist infinitely many bad primes.


## 2024 — 3

**Record:** `chn_2024_86460e`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2024_86460e.json.gz).

Let $a_1 > a_2 > \dots > a_n > 1$ be positive integers. Let $M$ denote the least common multiple of $a_1, a_2, \dots, a_n$. For a finite set of integers $X$, define
$$
f(X) = \min_{1 \le i \le n} \sum_{x \in X} \left\{ \frac{x}{a_i} \right\}.
$$
Here $\{u\} = u - \lfloor u \rfloor$ is the fractional part of the real number $u$. Put $f(\emptyset) = 0$. We say a set $X$ is *minimal*, if for any proper subset $Y \subsetneq X$, we have $f(Y) < f(X)$.
Prove that, if $X$ is a minimal finite set of integers and if $f(X) \ge \frac{2}{a_n}$, then
$$
|X| \le f(X) \cdot M.
$$
Here for a finite set $X$, we use $|X|$ to denote the number of elements in $X$.



# China-TST source statements

## 2014 — 3

**Record:** `chn_2014_1a3af5`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2014_1a3af5.json.gz).

Show that there are no 2-tuples $(x, y)$ of positive integers satisfying the equation
$$
(x+1)(x+2)\cdots(x+2014) = (y+1)(y+2)\cdots(y+4028).
$$


## 2014 — 6

**Record:** `chn_2014_452457`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2014_452457.json.gz).

For positive integer $k > 1$, let $f(k)$ be the number of ways of factoring $k$ into product of positive integers greater than 1 (The order of factors are not counted, for example $f(12) = 4$, as $12$ can be factored in these 4 ways: $12$, $2 \times 6$, $3 \times 4$, $2 \times 2 \times 3$).

**Prove:** If $n$ is a positive integer greater than 1, $p$ is a prime factor of $n$, then $f(n) \le \frac{n}{p}$.


## 2014 — 4

**Record:** `chn_2014_c8fce5`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2014_c8fce5.json.gz).

Let $k$ be a fixed odd integer, $k > 3$. Prove: There exist infinitely many positive integers $n$, such that there are two positive integers $d_1, d_2$ satisfying $d_1, d_2$ each dividing $\frac{n^2+1}{2}$, and $d_1 + d_2 = n + k$.


## 2021 — 4

**Record:** `chn_2021_0faf8c`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_0faf8c.json.gz).

For a positive integer $n$, let $\varphi(n)$ represent the number of positive integers not exceeding $n$ and relatively prime to $n$. Find all functions $f:\mathbb{N}_+ \to \mathbb{N}_+$ satisfying that for any positive integers $m, n$ with $m \ge n$,
$$f(m\varphi(n^3)) = f(m)\varphi(n^3).$$


## 2021 — 5

**Record:** `chn_2021_28dfb3`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_28dfb3.json.gz).

Given positive integers $n$, $r$ and distinct prime numbers $p_1$, $p_2$, $\dots$, $p_r$. Initially, there are $(n+1)^r$ numbers on the blackboard: $p_1^{i_1} p_2^{i_2} \cdots p_r^{i_r}$ ($0 \le i_1, i_2, \dots, i_r \le n$). Alice and Bob take turns (Alice goes first) to make the following moves, until only one number is left on the blackboard:
* Every time, Alice erases two numbers (can be identical) and writes their greatest common divisor on the blackboard.
* Every time, Bob erases two numbers (can be identical) and writes their least common multiple on the blackboard.
Find the least integer $M$, such that Alice can guarantee the remaining number does not exceed $M$.


## 2021 — 3

**Record:** `chn_2021_36327e`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_36327e.json.gz).

Given positive integers $a$, $b$, $c$ which are pairwise coprime. Let $f(n)$ represent the number of nonnegative integer solutions $(x, y, z)$ of the equation $a x + b y + c z = n$. Prove: there exist real constants $\alpha$, $\beta$, $\gamma$, such that for every nonnegative real number $n$,
$$
|f(n) - (\alpha n^2 + \beta n + \gamma)| < \frac{a+b+c}{12}.
$$


## 2021 — 4

**Record:** `chn_2021_8156cd`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_8156cd.json.gz).

For each positive integer $N$, let $\tau(N)$ be the number of positive factors of $N$; $\omega(N)$ be the number of distinct prime factors of $N$; $\Omega(N)$ be the number of prime factors (counts multiplicities) of $N$. Prove: for each positive integer $n$,
$$
\sum_{m=1}^{n} 5^{\omega(m)} \le \sum_{k=1}^{n} \lfloor \frac{n}{k} \rfloor \tau(k)^2 \le \sum_{m=1}^{n} 5^{\Omega(m)}.
$$

Here, $\lfloor x \rfloor$ is the largest integer not exceeding $x$.


## 2021 — 2

**Record:** `chn_2021_85d786`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_85d786.json.gz).

Given $2021$ distinct positive integers $a_1, a_2, \dots, a_{2021}$. Define the sequence $\{a_n\}$ inductively as follows: for each integer $n \ge 2022$, $a_n$ is the smallest positive integer different from $a_1, a_2, \dots, a_{n-1}$ and not dividing the product $a_{n-1}a_{n-2}\dots a_{n-2021}$. Prove: there exists a positive integer $M$, such that all integers greater than or equal to $M$ appear in $\{a_n\}$.


## 2021 — 3

**Record:** `chn_2021_ab96ca`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_ab96ca.json.gz).

Let $S(k)$ denote the sum of all digits of $k$ in base 10. Find all integers $n \ge 2$ and rational numbers $\beta \in (0,1)$, such that there exist $n$ distinct positive integers $a_1, a_2, \dots, a_n$ that satisfy: for any subset $I \subseteq \{1, 2, \dots, n\}$ with two or more elements,
$$ S\left(\sum_{i \in I} a_i\right) = \beta \cdot \sum_{i \in I} S(a_i). $$


## 2022 — 6

**Record:** `chn_2022_43fc7f`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_43fc7f.json.gz).

Given a positive integer $n$, let $D$ denote the set of all positive divisors of $n$. Let $A$ and $B$ be subsets of $D$ satisfying: for any $a \in A$ and $b \in B$, we have $a \nmid b$ and $b \nmid a$. Prove that
$$
\sqrt{|A|} + \sqrt{|B|} \le \sqrt{|D|}.
$$


## 2022 — 2

**Record:** `chn_2022_4d5044`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_4d5044.json.gz).

Given a prime number $p$ and an infinite set $A \subset \mathbb{Z}$. Show that one can always find a subset $B$ of $A$, $B$ contains $2p-2$ elements, and for any $p$ distinct elements of $B$, their arithmetic mean does not belong to $A$.

(Contributed by Fu Yunhao)


## 2023 — 2

**Record:** `chn_2023_200f9d`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_200f9d.json.gz).

Let $a$, $b$, and $d$ be integers satisfying $d \ge 0$, $|a| \ge 2$, and $b \ge (|a| + 1)^{d+1}$. Suppose $f(x)$ is a real-coefficient polynomial of degree $d$, and for each positive integer $n$, let $r_n$ denote the remainder of $\lfloor f(n)a^n \rfloor$ modulo $b$.

*Proof:* If the sequence $r_n$ is ultimately periodic, then $f(x)$ is a rational-coefficient polynomial.

*Note 1:* For every real number $x$, $\lfloor x \rfloor$ denotes the largest integer that is not greater than $x$.

*Note 2:* A sequence $a_n$ is called *ultimately periodic* if there exist positive integers $n_0$ and $T$ such that for every integer $n \ge n_0$, we have $a_{n+T} = a_n$.


## 2023 — 1

**Record:** `chn_2023_8e18d4`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_8e18d4.json.gz).

Does there exist an irrational number $x$ such that there are at most finitely many positive integers $n$ satisfying
$$
\{kx\} \geq \frac{1}{n+1}
$$
for every $k \in \{1, \dots, n\}$?

Note: Here, for a positive real number $y$, $\{y\}$ denotes the fractional part of $y$.


## 2023 — 5

**Record:** `chn_2023_f22969`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_f22969.json.gz).

Given a prime number $p$ and a positive real number $\lambda$ less than $1$. Let $k$ be an integer, and let $S$ and $T$ be sets consisting of consecutive $s$ and $t$ integers, respectively, satisfying $1 \le s \le t < \frac{\lambda}{12}p$. Furthermore, assume that the number of elements in the set
$$
\{(x, y) \in S \times T : kx \equiv y \pmod{p}\}
$$
is not less than $1 + \lambda s$. Prove that there exist integers $a$ and $b$ satisfying
$$
ka \equiv b \pmod{p}, \quad 0 < a \le \frac{1}{\lambda}, \quad |b| \le \frac{t}{\lambda s}.
$$


## 2025 — Problem 6

**Record:** `chn_2025_0db89f`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_0db89f.json.gz).

Given an odd prime $p$. Find the largest positive integer $n$ such that there exist $n$ integer-coordinate points $A_1, A_2, \dots, A_n$ in the plane, with no three collinear, and for any $1 \le i < j < k \le n$, twice the area of triangle $A_iA_jA_k$ is **not** divisible by $p$.


## 2025 — Problem 7

**Record:** `chn_2025_279d85`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_279d85.json.gz).

Given a positive integer $k$, let integers $a, b$ (not both zero) satisfy $0 \le a < k$, $0 \le b < k+1$. Define the sequence $\{T_n\}_{n \ge k}$ as follows:
$$
T_k = a, \quad T_{k+1} = b,
$$
and for $n \ge k + 2$,
$$
T_n \equiv T_{n-1} + T_{n-2} \pmod{n} \quad \text{with} \quad 0 \le T_n < n.
$$
Concatenating the decimal expansions of $T_k, T_{k+1}, \dots$ after the decimal point yields an infinite decimal $x = 0.T_kT_{k+1}\dots$. For example, if $k = 66$, $a = 5$, $b = 20$, then $T_{66} = 5$, $T_{67} = 20$, $T_{68} = 25$, $T_{69} = 45$, $T_{70} = 0$, $T_{71} = 45$, $T_{72} = 45$, $T_{73} = 17$, etc., so $x = 0.52025450454517\dots$.
Prove that $x$ is irrational.


## 2025 — Problem 3

**Record:** `chn_2025_584da0`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_584da0.json.gz).

Let $k$, $l$, $n$ be positive integers, and let $a_1, a_2, \dots, a_k \in \{1, 2, \dots, n\}$ satisfy the following three conditions:
(1) $n \ge 3$, $l \le n-2$, and $l-k \le \frac{n-3}{2}$;
(2) For each $t \in \{1, 2, \dots, l\}$, there exists a non-empty subset $I \subseteq \{1, 2, \dots, k\}$ such that
$$
\sum_{i \in I} a_i \equiv t \pmod{n};
$$
(3) For each $t \in \{l+1, l+2, \dots, n\}$, there does not exist a non-empty subset $I \subseteq \{1, 2, \dots, k\}$ such that
$$
\sum_{i \in I} a_i \equiv t \pmod{n}.
$$
Prove that $a_1 + a_2 + \dots + a_k = l$.


## 2025 — Problem 11

**Record:** `chn_2025_73d79f`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_73d79f.json.gz).

Given a positive integer $n \ge 4$, prove that the equation
$$
(2^x - 1)(5^x - 1) = y^n
$$
has no positive integer solutions $(x, y)$.


## 2025 — Problem 10

**Record:** `chn_2025_d8572e`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_d8572e.json.gz).

Given an odd integer $n \ge 3$ and a regular $n$-gon with vertex set $V$, let $\mathcal{P}$ denote the set of all regular polygons with vertices in $V$. For example, if $n = 15$, then $\mathcal{P}$ includes 1 regular 15-gon, 3 regular pentagons, and 5 equilateral triangles.

Two players, Alice and Bob, play the following game. Initially, all points in $V$ are uncolored. Alice moves first, and they take turns coloring an uncolored point in $V$: Alice colors red, and Bob colors blue. The game ends when all points are colored. A polygon in $\mathcal{P}$ is called **red-dominated** if it has more red vertices than blue ones.

Find the largest integer $k$ such that, no matter how Bob plays, Alice can guarantee at least $k$ red-dominated polygons in $\mathcal{P}$ at the end.



# EGMO source statements

## 2012 — Problem 5

**Record:** `egm_2012_84a668`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2012_84a668.json.gz).

The numbers $p$ and $q$ are prime and satisfy
$$
\frac{p}{p+1}+\frac{q+1}{q}=\frac{2 n}{n+2}
$$
for some positive integer $n$. Find all possible values of $q-p$.


## 2012 — Problem 4.

**Record:** `egm_2012_b764d7`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2012_b764d7.json.gz).

A set $A$ of integers is called sum-full if $A \subseteq A+A$, i.e. each element $a \in A$ is the sum of some pair of (not necessarily different) elements $b, c \in A$. A set $A$ of integers is said to be zero-sum-free if $0$ is the only integer that cannot be expressed as the sum of the elements of a finite nonempty subset of $A$.

Does there exist a sum-full zero-sum-free set of integers?


## 2012 — Problema 4

**Record:** `rou_2012_f18db0`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2012_f18db0.json.gz).

O mulţime $A$ de numere întregi se zice sumă-plină dacă $A \subseteq A+A$, adică orice element $a \in A$ este suma unei perechi (nu neapărat unice) de elemente (nu neapărat distincte) $b, c \in A$. O mulţime $A$ de numere întregi se zice liberă-de-sume-zero dacă $0$ este singurul număr întreg care nu poate fi exprimat ca suma elementelor unei submulţimi finite nevide a lui $A$.
Există oare o muļime sumă-plină liberă-de-sume-zero de numere întregi?


## 2013 — Problem 4.

**Record:** `egm_2013_34529d`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2013_34529d.json.gz).

Find all positive integers $a$ and $b$ for which there are three consecutive integers at which the polynomial
$$
P(n)=\frac{n^{5}+a}{b}
$$
takes integer values.


## 2013 — Problem 3.

**Record:** `egm_2013_6d183f`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2013_6d183f.json.gz).

Let $n$ be a positive integer.

a. Prove that there exists a set $S$ of $6 n$ pairwise different positive integers, such that the least common multiple of any two elements of $S$ is no larger than $32 n^{2}$.

b. Prove that every set $T$ of $6 n$ pairwise different positive integers contains two elements the least common multiple of which is larger than $9 n^{2}$.


## 2014 — 4.

**Record:** `egm_2014_0cc86d`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2014_0cc86d.json.gz).

Determine all integers $n \geq 2$ for which there exist integers $x_{1}, x_{2}, \ldots, x_{n-1}$ satisfying the condition that if $0 < i < n$, $0 < j < n$, $i \neq j$ and $n$ divides $2i + j$, then $x_{i} < x_{j}$.


## 2014 — 3.

**Record:** `egm_2014_f90a36`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2014_f90a36.json.gz).

We denote the number of positive divisors of a positive integer $m$ by $d(m)$ and the number of distinct prime divisors of $m$ by $\omega(m)$. Let $k$ be a positive integer. Prove that there exist infinitely many positive integers $n$ such that $\omega(n)=k$ and $d(n)$ does not divide $d\left(a^{2}+b^{2}\right)$ for any positive integers $a, b$ satisfying $a+b=n$.


## 2015 — 5

**Record:** `mkd_2015_cdfbb6`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2015_cdfbb6.json.gz).

Let $m, n$ be positive integers with $m > 1$. Anastasia partitions the integers $1, 2, \dots, 2m$ into $m$ pairs. Boris then chooses one integer from each pair and finds the sum of these chosen integers. Prove that Anastasia can select the pairs so that Boris cannot make his sum equal to $n$.


## 2015 — 3

**Record:** `mkd_2015_de03cc`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2015_de03cc.json.gz).

Let $m, n$ be integers greater than $1$, and let $a_1, a_2, \dots, a_m$ be positive integers not greater than $n^m$. Prove that there exist positive integers $b_1, b_2, \dots, b_m$ not greater than $n$ such that
$$
\text{gcd}(a_1 + b_1, a_2 + b_2, a_3 + b_3, \dots, a_m + b_m) < n,
$$
where $\text{gcd}(x_1, x_2, \dots, x_m)$ denotes the greatest common divisor of $x_1, x_2, \dots, x_m$.


## 2016 — Problem 6.

**Record:** `rou_2016_cc4647`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2016_cc4647.json.gz).

Let $S$ be the set of all positive integers $n$ such that $n^4$ has a divisor in the range $n^2+1, n^2+2, \dots, n^2+2n$. Prove that there are infinitely many elements of $S$ of each of the forms $7m$, $7m+1$, $7m+2$, $7m+5$, $7m+6$ and no elements of $S$ of the form $7m+3$ or $7m+4$, where $m$ is an integer.


## 2020 — Problem 6

**Record:** `egm_2020_2eb0ec`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2020_2eb0ec.json.gz).

Let $m > 1$ be an integer. A sequence $a_{1}, a_{2}, a_{3}, \ldots$ is defined by $a_{1} = a_{2} = 1$, $a_{3} = 4$, and for all $n \geq 4$,
$$
a_{n} = m\left(a_{n-1} + a_{n-2}\right) - a_{n-3}.
$$
Determine all integers $m$ such that every term of the sequence is a square.


## 2023 — Problem 5

**Record:** `egm_2023_fc0b21`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2023_fc0b21.json.gz).

We are given a positive integer $s \geqslant 2$. For each positive integer $k$, we define its twist $k^{\prime}$ as follows: write $k$ as $a s+b$, where $a, b$ are non-negative integers and $b<s$, then $k^{\prime}=b s+a$. For the positive integer $n$, consider the infinite sequence $d_{1}, d_{2}, \ldots$ where $d_{1}=n$ and $d_{i+1}$ is the twist of $d_{i}$ for each positive integer $i$.
Prove that this sequence contains 1 if and only if the remainder when $n$ is divided by $s^{2}-1$ is either 1 or $s$.


## 2024 — Problem 1

**Record:** `egm_2024_86f588`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2024_86f588.json.gz).

Two different integers $u$ and $v$ are written on a board. We perform a sequence of steps. At each step we do one of the following two operations:

(i) If $a$ and $b$ are different integers on the board, then we can write $a+b$ on the board, if it is not already there.

(ii) If $a, b$ and $c$ are three different integers on the board, and if an integer $x$ satisfies $a x^{2}+b x+c=0$, then we can write $x$ on the board, if it is not already there.

Determine all pairs of starting numbers $(u, v)$ from which any integer can eventually be written on the board after a finite sequence of steps.


## 2024 — Problem 3

**Record:** `egm_2024_96da66`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2024_96da66.json.gz).

We call a positive integer $n$ peculiar if, for any positive divisor $d$ of $n$, the integer $d(d+1)$ divides $n(n+1)$. Prove that for any four different peculiar positive integers $A, B, C$ and $D$, the following holds:
$$
\operatorname{gcd}(A, B, C, D)=1
$$
Here $\operatorname{gcd}(A, B, C, D)$ is the largest positive integer that divides all of $A, B, C$ and $D$.


## 2024 — Problem 5

**Record:** `egm_2024_efd366`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2024_efd366.json.gz).

Let $\mathbb{N}$ denote the set of positive integers. Find all functions $f: \mathbb{N} \rightarrow \mathbb{N}$ such that the following assertions are true for every pair of positive integers $(x, y)$:
- $x$ and $f(x)$ have the same number of positive divisors.
- If $x$ does not divide $y$ and $y$ does not divide $x$, then
$$
\operatorname{gcd}(f(x), f(y)) > f(\operatorname{gcd}(x, y))
$$
Here $\operatorname{gcd}(m, n)$ is the largest positive integer that divides both $m$ and $n$.



# IMO source statements

## 1983 — 3.

**Record:** `esp_1983_fa6627`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_1983_fa6627.json.gz).

Sean $a$, $b$, $c$ enteros positivos, dos a dos primos entre sí. Demostrar que $2abc - ab - bc - ca$ es el mayor entero que no puede expresarse en la forma $x\,bc + y\,ca + z\,ab$, donde $x$, $y$, y $z$ son enteros no negativos.


## 1985 — 2.

**Record:** `esp_1985_31cbd9`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_1985_31cbd9.json.gz).

Sean $n$ y $k$ dos números naturales primos entre sí, con $0 < k < n$. Cada número del conjunto $\mathcal{M} = \{1, 2, \ldots, n-1\}$ se colorea o bien en azul, o bien en blanco. Se sabe que

1) Para cada $i \in \mathcal{M}$, los elementos $i$ y $n-i$ tienen el mismo color.

2) Para cada $i \in \mathcal{M}$, $i \neq k$, los elementos $i$ y $|i-k|$ tienen el mismo color.

Demostrar que todos los elementos de $\mathcal{M}$ tienen el mismo color.


## 1985 — 4.

**Record:** `esp_1985_417bfe`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_1985_417bfe.json.gz).

Sea $\mathcal{M}$ un conjunto de 1985 enteros positivos distintos, ninguno de los cuales tiene divisores primos mayores que 26. Demostrar que $\mathcal{M}$ contiene como mínimo un subconjunto de cuatro elementos distintos, cuyo producto es la cuarta potencia de un entero.


## 1986 — 1.

**Record:** `esp_1986_584faa`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_1986_584faa.json.gz).

Sea $d$ un entero positivo distinto de $2$, $5$ y $13$. Demostrar que se pueden encontrar elementos distintos $a, b$ en el conjunto $\{2, 5, 13, d\}$, de manera que $ab - 1$ no sea un cuadrado perfecto.


## 2005 — 4

**Record:** `usa_2005_2bd0e7`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2005_2bd0e7.json.gz).

Consider the sequence $a_1, a_2, \dots$ defined by
$$
a_n = 2^n + 3^n + 6^n - 1.
$$
for all positive integers $n$. Determine all positive integers that are relatively prime to every term of the sequence.


## 2005 — 2

**Record:** `usa_2005_9b3d8f`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2005_9b3d8f.json.gz).

Let $a_1, a_2, \dots$ be a sequence of integers with infinitely many positive and infinitely many negative terms. Suppose that for each positive integer $n$, the numbers $a_1, a_2, \dots, a_n$ leave distinct remainders upon division by $n$. Prove that every integer occurs exactly once in the sequence.


## 2013 — 6

**Record:** `esp_2013_8adf5f`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_2013_8adf5f.json.gz).

Sea $n \ge 3$ un número entero. Se considera una circunferencia en la que se han marcado $n+1$ puntos igualmente espaciados. Cada punto se etiqueta con uno de los números $0, 1, \dots, n$ de manera que cada número se usa exactamente una vez. Dos distribuciones de etiquetas se consideran la misma si una se puede obtener de la otra por una rotación de la circunferencia. Una distribución de etiquetas se llama bonita si, para cualesquiera cuatro etiquetas $a < b < c < d$, con $a + d = b + c$, la cuerda que une los puntos etiquetados $a$ y $d$ no corta la cuerda que une los puntos etiquetados $b$ y $c$. Sea $M$ el número de distribuciones bonitas y $N$ el número de pares ordenados $(x, y)$ de enteros positivos tales que $x + y \le n$ y $\text{mcd}(x, y) = 1$. Demostrar que $M = N + 1$.


## 2014 — Exercice 10

**Record:** `fra_2014_8e92eb`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/france/fra_2014_8e92eb.json.gz).

Déterminer tous les polynômes $P$ à coefficients entiers pour lesquels l'ensemble $P(\mathbb{N})$ contient une suite géométrique infinie de raison $a$ avec $a \notin\{-1,0,1\}$ et de premier terme non nul.



# IMO-SL source statements

## 2006 — N5

**Record:** `imo_2006_00ba5c`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_00ba5c.json.gz).

Find all integer solutions of the equation
$$
\frac{x^{7}-1}{x-1}=y^{5}-1
$$


## 2006 — N7

**Record:** `imo_2006_2a7e32`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_2a7e32.json.gz).

Prove that, for every positive integer $n$, there exists an integer $m$ such that $2^{m}+m$ is divisible by $n$.


## 2006 — N6

**Record:** `imo_2006_3525c9`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_3525c9.json.gz).

Let $a > b > 1$ be relatively prime positive integers. Define the weight of an integer $c$, denoted by $w(c)$, to be the minimal possible value of $|x| + |y|$ taken over all pairs of integers $x$ and $y$ such that
$$
a x + b y = c.
$$
An integer $c$ is called a local champion if $w(c) \geq w(c \pm a)$ and $w(c) \geq w(c \pm b)$.
Find all local champions and determine their number.


## 2006 — N2

**Record:** `imo_2006_472d44`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_472d44.json.gz).

**Source issue:** Sampled decimal need not lie strictly between zero and one. Endpoint possibility retained in N02.

For $x \in (0,1)$ let $y \in (0,1)$ be the number whose $n$th digit after the decimal point is the $\left(2^{n}\right)$th digit after the decimal point of $x$. Show that if $x$ is rational then so is $y$.

(Canada)


## 2006 — N1

**Record:** `imo_2006_bc0ae3`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_bc0ae3.json.gz).

Determine all pairs $(x, y)$ of integers satisfying the equation
$$
1 + 2^{x} + 2^{2x+1} = y^{2}
$$


## 2006 — N4

**Record:** `imo_2006_bf7806`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_bf7806.json.gz).

Let $P$ be a polynomial of degree $n>1$ with integer coefficients and let $k$ be any positive integer. Consider the polynomial $Q(x)=P(P(\ldots P(P(x)) \ldots))$, with $k$ pairs of parentheses. Prove that $Q$ has no more than $n$ integer fixed points, i.e. integers satisfying the equation $Q(x)=x$.
(Romania)


## 2006 — N3

**Record:** `imo_2006_ffa2b8`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_ffa2b8.json.gz).

The sequence $f(1), f(2), f(3), \ldots$ is defined by
$$
f(n)=\frac{1}{n}\left(\left\lfloor\frac{n}{1}\right\rfloor+\left\lfloor\frac{n}{2}\right\rfloor+\cdots+\left\lfloor\frac{n}{n}\right\rfloor\right),
$$
where $\lfloor x\rfloor$ denotes the integer part of $x$.

a. Prove that $f(n+1)>f(n)$ infinitely often.

b. Prove that $f(n+1)<f(n)$ infinitely often.


## 2007 — C3

**Record:** `imo_2007_104cb8`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_104cb8.json.gz).

Find all positive integers $n$, for which the numbers in the set $S=\{1,2, \ldots, n\}$ can be colored red and blue, with the following condition being satisfied: the set $S \times S \times S$ contains exactly $2007$ ordered triples $(x, y, z)$ such that (i) $x, y, z$ are of the same color and (ii) $x+y+z$ is divisible by $n$.


## 2007 — N1

**Record:** `imo_2007_16b745`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_16b745.json.gz).

Find all pairs $(k, n)$ of positive integers for which $7^{k}-3^{n}$ divides $k^{4}+n^{2}$.


## 2007 — N3

**Record:** `imo_2007_2b3b32`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_2b3b32.json.gz).

Let $X$ be a set of $10000$ integers, none of them is divisible by $47$. Prove that there exists a $2007$-element subset $Y$ of $X$ such that $a-b+c-d+e$ is not divisible by $47$ for any $a, b, c, d, e \in Y$.


## 2007 — N2

**Record:** `imo_2007_886291`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_886291.json.gz).

Let $b$, $n > 1$ be integers. Suppose that for each $k > 1$ there exists an integer $a_{k}$ such that $b - a_{k}^{n}$ is divisible by $k$. Prove that $b = A^{n}$ for some integer $A$.


## 2007 — C5

**Record:** `imo_2007_be294f`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_be294f.json.gz).

In the Cartesian coordinate plane define the strip $S_{n}=\{(x, y) \mid n \leq x<n+1\}$ for every integer $n$. Assume that each strip $S_{n}$ is colored either red or blue, and let $a$ and $b$ be two distinct positive integers. Prove that there exists a rectangle with side lengths $a$ and $b$ such that its vertices have the same color.


## 2007 — N7

**Record:** `imo_2007_e1c86b`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_e1c86b.json.gz).

For a prime $p$ and a positive integer $n$, denote by $\nu_{p}(n)$ the exponent of $p$ in the prime factorization of $n!$. Given a positive integer $d$ and a finite set $\{p_{1}, \ldots, p_{k}\}$ of primes. Show that there are infinitely many positive integers $n$ such that $d \mid \nu_{p_{i}}(n)$ for all $1 \leq i \leq k$.


## 2007 — N4

**Record:** `imo_2007_f1ecad`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_f1ecad.json.gz).

For every integer $k \geq 2$, prove that $2^{3k}$ divides the number
$$
\binom{2^{k+1}}{2^{k}} - \binom{2^{k}}{2^{k-1}}
$$


## 2008 — N3

**Record:** `imo_2008_032bdc`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_032bdc.json.gz).

Let $a_{0}, a_{1}, a_{2}, \ldots$ be a sequence of positive integers such that the greatest common divisor of any two consecutive terms is greater than the preceding term; in symbols, $\operatorname{gcd}\left(a_{i}, a_{i+1}\right)>a_{i-1}$. Prove that $a_{n} \geq 2^{n}$ for all $n \geq 0$.


## 2008 — C2

**Record:** `imo_2008_06a8f7`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_06a8f7.json.gz).

For every positive integer $n$ determine the number of permutations $(a_{1}, a_{2}, \ldots, a_{n})$ of the set $\{1,2, \ldots, n\}$ with the following property:
$$
2(a_{1}+a_{2}+\cdots+a_{k}) \quad \text{is divisible by} \ k \quad \text{for} \ k=1,2, \ldots, n.
$$


## 2008 — N5

**Record:** `imo_2008_40ef71`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_40ef71.json.gz).

For every $n \in \mathbb{N}$ let $d(n)$ denote the number of (positive) divisors of $n$. Find all functions $f: \mathbb{N} \rightarrow \mathbb{N}$ with the following properties:
(i) $d(f(x))=x$ for all $x \in \mathbb{N}$;
(ii) $f(x y)$ divides $(x-1) y^{x y-1} f(x)$ for all $x, y \in \mathbb{N}$.


## 2008 — A4

**Record:** `imo_2008_4e4b33`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_4e4b33.json.gz).

For an integer $m$, denote by $t(m)$ the unique number in $\{1,2,3\}$ such that $m+t(m)$ is a multiple of $3$. A function $f: \mathbb{Z} \rightarrow \mathbb{Z}$ satisfies $f(-1)=0$, $f(0)=1$, $f(1)=-1$ and
$$
f\left(2^{n}+m\right)=f\left(2^{n}-t(m)\right)-f(m) \quad \text{ for all integers } m, n \geq 0 \text{ with } 2^{n}>m.
$$

Prove that $f(3p) \geq 0$ holds for all integers $p \geq 0$.


## 2008 — N4

**Record:** `imo_2008_5311eb`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_5311eb.json.gz).

Let $n$ be a positive integer. Show that the numbers
$$
\binom{2^{n}-1}{0}, \quad\binom{2^{n}-1}{1}, \quad\binom{2^{n}-1}{2}, \quad \ldots, \quad\binom{2^{n}-1}{2^{n-1}-1}
$$
are congruent modulo $2^{n}$ to $1,3,5, \ldots, 2^{n}-1$ in some order.


## 2008 — A6

**Record:** `imo_2008_96b2a5`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_96b2a5.json.gz).

Let $f: \mathbb{R} \rightarrow \mathbb{N}$ be a function which satisfies
$$
f\left(x+\frac{1}{f(y)}\right)=f\left(y+\frac{1}{f(x)}\right) \quad \text{ for all } x, y \in \mathbb{R}
$$
Prove that there is a positive integer which is not a value of $f$.


## 2008 — C3

**Record:** `imo_2008_bdc772`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_bdc772.json.gz).

In the coordinate plane consider the set $S$ of all points with integer coordinates. For a positive integer $k$, two distinct points $A, B \in S$ will be called $k$-friends if there is a point $C \in S$ such that the area of the triangle $A B C$ is equal to $k$. A set $T \subset S$ will be called a $k$-clique if every two points in $T$ are $k$-friends. Find the least positive integer $k$ for which there exists a $k$-clique with more than 200 elements.


## 2008 — N2

**Record:** `imo_2008_c0450d`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_c0450d.json.gz).

Let $a_{1}, a_{2}, \ldots, a_{n}$ be distinct positive integers, $n \geq 3$. Prove that there exist distinct indices $i$ and $j$ such that $a_{i}+a_{j}$ does not divide any of the numbers $3 a_{1}, 3 a_{2}, \ldots, 3 a_{n}$.


## 2008 — N1

**Record:** `imo_2008_dbd5d0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_dbd5d0.json.gz).

Let $n$ be a positive integer and let $p$ be a prime number. Prove that if $a, b, c$ are integers (not necessarily positive) satisfying the equations
$$
a^{n}+p b=b^{n}+p c=c^{n}+p a,
$$
then $a=b=c$.


## 2009 — N1

**Record:** `imo_2009_af95e8`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2009_af95e8.json.gz).

A social club has $n$ members. They have the membership numbers $1, 2, \ldots, n$, respectively. From time to time members send presents to other members, including items they have already received as presents from other members. In order to avoid the embarrassing situation that a member might receive a present that he or she has sent to other members, the club adds the following rule to its statutes at one of its annual general meetings:

"A member with membership number $a$ is permitted to send a present to a member with membership number $b$ if and only if $a(b-1)$ is a multiple of $n$."

Prove that, if each member follows this rule, none will receive a present from another member that he or she has already sent to other members.

Alternative formulation: Let $G$ be a directed graph with $n$ vertices $v_{1}, v_{2}, \ldots, v_{n}$, such that there is an edge going from $v_{a}$ to $v_{b}$ if and only if $a$ and $b$ are distinct and $a(b-1)$ is a multiple of $n$. Prove that this graph does not contain a directed cycle.


## 2009 — N2

**Record:** `imo_2009_cf1420`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2009_cf1420.json.gz).

A positive integer $N$ is called balanced, if $N=1$ or if $N$ can be written as a product of an even number of not necessarily distinct primes. Given positive integers $a$ and $b$, consider the polynomial $P$ defined by $P(x)=(x+a)(x+b)$.

a. Prove that there exist distinct positive integers $a$ and $b$ such that all the numbers $P(1)$, $P(2)$, $\ldots$, $P(50)$ are balanced.

b. Prove that if $P(n)$ is balanced for all positive integers $n$, then $a=b$.


## 2010 — A5

**Record:** `imo_2010_18587d`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2010_18587d.json.gz).

Denote by $\mathbb{Q}^{+}$ the set of all positive rational numbers. Determine all functions $f: \mathbb{Q}^{+} \rightarrow \mathbb{Q}^{+}$ which satisfy the following equation for all $x, y \in \mathbb{Q}^{+}$:
$$
f\left(f(x)^{2} y\right)=x^{3} f(x y)
$$


## 2010 — N6

**Record:** `imo_2010_3a2ab0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2010_3a2ab0.json.gz).

The rows and columns of a $2^{n} \times 2^{n}$ table are numbered from $0$ to $2^{n}-1$. The cells of the table have been colored with the following property being satisfied: for each $0 \leq i, j \leq 2^{n}-1$, the $j$th cell in the $i$th row and the $(i+j)$th cell in the $j$th row have the same color. (The indices of the cells in a row are considered modulo $2^{n}$.)

Prove that the maximal possible number of colors is $2^{n}$.

(Iran)


## 2010 — N3

**Record:** `imo_2010_4b0c7b`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2010_4b0c7b.json.gz).

Find the smallest number $n$ such that there exist polynomials $f_{1}, f_{2}, \ldots, f_{n}$ with rational coefficients satisfying
$$
x^{2}+7=f_{1}(x)^{2}+f_{2}(x)^{2}+\cdots+f_{n}(x)^{2}
$$


## 2010 — N5

**Record:** `imo_2010_970d18`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2010_970d18.json.gz).

Let $\mathbb{N}$ be the set of all positive integers. Find all functions $f: \mathbb{N} \rightarrow \mathbb{N}$ such that the number $(f(m)+n)(m+f(n))$ is a square for all $m, n \in \mathbb{N}$.
(U.S.A.)


## 2010 — N4

**Record:** `imo_2010_ae862f`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2010_ae862f.json.gz).

Let $a, b$ be integers, and let $P(x) = a x^{3} + b x$. For any positive integer $n$ we say that the pair $(a, b)$ is $n$-good if $n \mid P(m) - P(k)$ implies $n \mid m - k$ for all integers $m, k$. We say that $(a, b)$ is very good if $(a, b)$ is $n$-good for infinitely many positive integers $n$.

a. Find a pair $(a, b)$ which is $51$-good, but not very good.

b. Show that all $2010$-good pairs are very good.

(Turkey)


## 2010 — C7

**Record:** `imo_2010_c12e74`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2010_c12e74.json.gz).

Let $P_{1}, \ldots, P_{s}$ be arithmetic progressions of integers, the following conditions being satisfied:
(i) each integer belongs to at least one of them;
(ii) each progression contains a number which does not belong to other progressions.
Denote by $n$ the least common multiple of steps of these progressions; let $n=p_{1}^{\alpha_{1}} \ldots p_{k}^{\alpha_{k}}$ be its prime factorization. Prove that
$$
s \geq 1+\sum_{i=1}^{k} \alpha_{i}\left(p_{i}-1\right)
$$


## 2011 — N7

**Record:** `imo_2011_359cb8`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2011_359cb8.json.gz).

Let $p$ be an odd prime number. For every integer $a$, define the number
$$
S_{a} = \frac{a}{1} + \frac{a^{2}}{2} + \cdots + \frac{a^{p-1}}{p-1}.
$$
Let $m$ and $n$ be integers such that
$$
S_{3} + S_{4} - 3 S_{2} = \frac{m}{n}
$$
Prove that $p$ divides $m$.


## 2011 — N6

**Record:** `imo_2011_b111da`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2011_b111da.json.gz).

Let $P(x)$ and $Q(x)$ be two polynomials with integer coefficients such that no nonconstant polynomial with rational coefficients divides both $P(x)$ and $Q(x)$. Suppose that for every positive integer $n$ the integers $P(n)$ and $Q(n)$ are positive, and $2^{Q(n)}-1$ divides $3^{P(n)}-1$. Prove that $Q(x)$ is a constant polynomial.


## 2011 — N8

**Record:** `imo_2011_beb7a1`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2011_beb7a1.json.gz).

Let $k$ be a positive integer and set $n=2^{k}+1$. Prove that $n$ is a prime number if and only if the following holds: there is a permutation $a_{1}, \ldots, a_{n-1}$ of the numbers $1,2, \ldots, n-1$ and a sequence of integers $g_{1}, g_{2}, \ldots, g_{n-1}$ such that $n$ divides $g_{i}^{a_{i}}-a_{i+1}$ for every $i \in\{1,2, \ldots, n-1\}$, where we set $a_{n}=a_{1}$.


## 2011 — N3

**Record:** `imo_2011_f26960`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2011_f26960.json.gz).

Let $n \geq 1$ be an odd integer. Determine all functions $f$ from the set of integers to itself such that for all integers $x$ and $y$ the difference $f(x)-f(y)$ divides $x^{n}-y^{n}$.


## 2012 — N8

**Record:** `imo_2012_35e1cc`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2012_35e1cc.json.gz).

Prove that for every prime $p > 100$ and every integer $r$ there exist two integers $a$ and $b$ such that $p$ divides $a^{2} + b^{5} - r$.


## 2013 — C7

**Record:** `imo_2013_5a8513`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_5a8513.json.gz).

Let $n \geqslant 2$ be an integer. Consider all circular arrangements of the numbers $0,1, \ldots, n$; the $n+1$ rotations of an arrangement are considered to be equal. A circular arrangement is called beautiful if, for any four distinct numbers $0 \leqslant a, b, c, d \leqslant n$ with $a+c=b+d$, the chord joining numbers $a$ and $c$ does not intersect the chord joining numbers $b$ and $d$.
Let $M$ be the number of beautiful arrangements of $0,1, \ldots, n$. Let $N$ be the number of pairs ( $x, y$ ) of positive integers such that $x+y \leqslant n$ and $\operatorname{gcd}(x, y)=1$. Prove that
$$
M=N+1 .
$$


## 2013 — N4

**Record:** `imo_2013_a40b79`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_a40b79.json.gz).

Determine whether there exists an infinite sequence of nonzero digits $a_{1}, a_{2}, a_{3}, \ldots$ and a positive integer $N$ such that for every integer $k > N$, the number $\overline{a_{k} a_{k-1} \ldots a_{1}}$ is a perfect square.


## 2013 — N7

**Record:** `imo_2013_a66da8`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_a66da8.json.gz).

Let $\nu$ be an irrational positive number, and let $m$ be a positive integer. A pair $(a, b)$ of positive integers is called good if
$$
a\lceil b \nu\rceil-b\lfloor a \nu\rfloor=m
$$
A good pair $(a, b)$ is called excellent if neither of the pairs $(a-b, b)$ and $(a, b-a)$ is good. (As usual, by $\lfloor x\rfloor$ and $\lceil x\rceil$ we denote the integer numbers such that $x-1<\lfloor x\rfloor \leqslant x$ and $x \leqslant\lceil x\rceil<x+1$.)
Prove that the number of excellent pairs is equal to the sum of the positive divisors of $m$.


## 2013 — N1

**Record:** `imo_2013_a67bc4`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_a67bc4.json.gz).

Let $\mathbb{Z}_{>0}$ be the set of positive integers. Find all functions $f: \mathbb{Z}_{>0} \rightarrow \mathbb{Z}_{>0}$ such that
$$
m^{2}+f(n) \mid m f(m)+n
$$
for all positive integers $m$ and $n$.


## 2013 — N6

**Record:** `imo_2013_b65c98`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_b65c98.json.gz).

Determine all functions $f: \mathbb{Q} \longrightarrow \mathbb{Z}$ satisfying
$$
f\left(\frac{f(x)+a}{b}\right)=f\left(\frac{x+a}{b}\right)
$$
for all $x \in \mathbb{Q}$, $a \in \mathbb{Z}$, and $b \in \mathbb{Z}_{>0}$. (Here, $\mathbb{Z}_{>0}$ denotes the set of positive integers.)


## 2013 — A5

**Record:** `imo_2013_ca3c20`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_ca3c20.json.gz).

Let $\mathbb{Z}_{\geqslant 0}$ be the set of all nonnegative integers. Find all the functions $f: \mathbb{Z}_{\geqslant 0} \rightarrow \mathbb{Z}_{\geqslant 0}$ satisfying the relation
$$
f(f(f(n)))=f(n+1)+1
$$
for all $n \in \mathbb{Z}_{\geqslant 0}$.


## 2014 — N6

**Record:** `imo_2014_da4751`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2014_da4751.json.gz).

Let $a_{1} < a_{2} < \cdots < a_{n}$ be pairwise coprime positive integers with $a_{1}$ being prime and $a_{1} \geqslant n+2$. On the segment $I = [0, a_{1} a_{2} \cdots a_{n}]$ of the real line, mark all integers that are divisible by at least one of the numbers $a_{1}, \ldots, a_{n}$. These points split $I$ into a number of smaller segments. Prove that the sum of the squares of the lengths of these segments is divisible by $a_{1}$.


## 2015 — N6

**Record:** `imo_2015_207240`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2015_207240.json.gz).

Let $\mathbb{Z}_{>0}$ denote the set of positive integers. Consider a function $f: \mathbb{Z}_{>0} \rightarrow \mathbb{Z}_{>0}$. For any $m, n \in \mathbb{Z}_{>0}$ we write $f^{n}(m)=\underbrace{f(f(\ldots f}_{n}(m) \ldots))$. Suppose that $f$ has the following two properties:
(i) If $m, n \in \mathbb{Z}_{>0}$, then $\frac{f^{n}(m)-m}{n} \in \mathbb{Z}_{>0}$;
(ii) The set $\mathbb{Z}_{>0} \backslash\left\{f(n) \mid n \in \mathbb{Z}_{>0}\right\}$ is finite.
Prove that the sequence $f(1)-1, f(2)-2, f(3)-3, \ldots$ is periodic.


## 2015 — N8

**Record:** `imo_2015_2ed1a0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2015_2ed1a0.json.gz).

For every positive integer $n$ with prime factorization $n=\prod_{i=1}^{k} p_{i}^{\alpha_{i}}$, define
$$
\mho(n)=\sum_{i: p_{i}>10^{100}} \alpha_{i}
$$
That is, $\mho(n)$ is the number of prime factors of $n$ greater than $10^{100}$, counted with multiplicity.
Find all strictly increasing functions $f: \mathbb{Z} \rightarrow \mathbb{Z}$ such that
$$
\mho(f(a)-f(b)) \leqslant \mho(a-b) \quad \text{ for all integers } a \text{ and } b \text{ with } a>b .
$$


## 2015 — A5

**Record:** `imo_2015_557c5a`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2015_557c5a.json.gz).

Let $2 \mathbb{Z} + 1$ denote the set of odd integers. Find all functions $f: \mathbb{Z} \rightarrow 2 \mathbb{Z} + 1$ satisfying
$$
f(x + f(x) + y) + f(x - f(x) - y) = f(x + y) + f(x - y)
$$
for every $x, y \in \mathbb{Z}$.


## 2015 — C2

**Record:** `imo_2015_ae4598`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2015_ae4598.json.gz).

Let $\mathcal{V}$ be a finite set of points in the plane. We say that $\mathcal{V}$ is balanced if for any two distinct points $A, B \in \mathcal{V}$, there exists a point $C \in \mathcal{V}$ such that $AC = BC$. We say that $\mathcal{V}$ is center-free if for any distinct points $A, B, C \in \mathcal{V}$, there does not exist a point $P \in \mathcal{V}$ such that $PA = PB = PC$.

a. Show that for all $n \geqslant 3$, there exists a balanced set consisting of $n$ points.

b. For which $n \geqslant 3$ does there exist a balanced, center-free set consisting of $n$ points?


## 2015 — N5

**Record:** `imo_2015_b0fc63`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2015_b0fc63.json.gz).

Determine all triples $(a, b, c)$ of positive integers for which $a b - c$, $b c - a$, and $c a - b$ are powers of $2$.

Explanation: A power of $2$ is an integer of the form $2^{n}$, where $n$ denotes some nonnegative integer.


## 2015 — N7

**Record:** `imo_2015_b5a2eb`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2015_b5a2eb.json.gz).

Let $\mathbb{Z}_{>0}$ denote the set of positive integers. For any positive integer $k$, a function $f: \mathbb{Z}_{>0} \rightarrow \mathbb{Z}_{>0}$ is called $k$-good if $\operatorname{gcd}(f(m)+n, f(n)+m) \leqslant k$ for all $m \neq n$. Find all $k$ such that there exists a $k$-good function.


## 2015 — C6

**Record:** `imo_2015_f31319`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2015_f31319.json.gz).

Let $S$ be a nonempty set of positive integers. We say that a positive integer $n$ is clean if it has a unique representation as a sum of an odd number of distinct elements from $S$. Prove that there exist infinitely many positive integers that are not clean.
(U.S.A.)


## 2016 — N6

**Record:** `imo_2016_263da3`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2016_263da3.json.gz).

Denote by $\mathbb{N}$ the set of all positive integers. Find all functions $f: \mathbb{N} \rightarrow \mathbb{N}$ such that for all positive integers $m$ and $n$, the integer $f(m)+f(n)-m n$ is nonzero and divides $m f(m)+n f(n)$.


## 2016 — N5

**Record:** `imo_2016_4a0292`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2016_4a0292.json.gz).

Let $a$ be a positive integer which is not a square number. Denote by $A$ the set of all positive integers $k$ such that
$$
k = \frac{x^{2} - a}{x^{2} - y^{2}}
$$
for some integers $x$ and $y$ with $x > \sqrt{a}$. Denote by $B$ the set of all positive integers $k$ such that (1) is satisfied for some integers $x$ and $y$ with $0 \leqslant x < \sqrt{a}$. Prove that $A = B$.


## 2016 — N3

**Record:** `imo_2016_7f52b3`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2016_7f52b3.json.gz).

Define $P(n) = n^{2} + n + 1$. For any positive integers $a$ and $b$, the set
$$
\{P(a), P(a+1), P(a+2), \ldots, P(a+b)\}
$$
is said to be fragrant if none of its elements is relatively prime to the product of the other elements. Determine the smallest size of a fragrant set.


## 2016 — N7

**Record:** `imo_2016_c1bb34`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2016_c1bb34.json.gz).

Let $n$ be an odd positive integer. In the Cartesian plane, a cyclic polygon $P$ with area $S$ is chosen. All its vertices have integral coordinates, and the squares of its side lengths are all divisible by $n$. Prove that $2 S$ is an integer divisible by $n$.


## 2016 — C2

**Record:** `imo_2016_f9df36`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2016_f9df36.json.gz).

Find all positive integers $n$ for which all positive divisors of $n$ can be put into the cells of a rectangular table under the following constraints:
- each cell contains a distinct divisor;
- the sums of all rows are equal; and
- the sums of all columns are equal.


## 2016 — N8

**Record:** `imo_2016_fa5aef`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2016_fa5aef.json.gz).

Find all polynomials $P(x)$ of odd degree $d$ and with integer coefficients satisfying the following property: for each positive integer $n$, there exist $n$ positive integers $x_{1}, x_{2}, \ldots, x_{n}$ such that $\frac{1}{2}<\frac{P\left(x_{i}\right)}{P\left(x_{j}\right)}<2$ and $\frac{P\left(x_{i}\right)}{P\left(x_{j}\right)}$ is the $d$-th power of a rational number for every pair of indices $i$ and $j$ with $1 \leqslant i, j \leqslant n$.


## 2017 — N2

**Record:** `imo_2017_2878d3`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2017_2878d3.json.gz).

Let $p \geqslant 2$ be a prime number. Eduardo and Fernando play the following game making moves alternately: in each move, the current player chooses an index $i$ in the set $\{0,1, \ldots, p-1\}$ that was not chosen before by either of the two players and then chooses an element $a_{i}$ of the set $\{0,1,2,3,4,5,6,7,8,9\}$. Eduardo has the first move. The game ends after all the indices $i \in\{0,1, \ldots, p-1\}$ have been chosen. Then the following number is computed:
$$
M=a_{0}+10 \cdot a_{1}+\cdots+10^{p-1} \cdot a_{p-1}=\sum_{j=0}^{p-1} a_{j} \cdot 10^{j}
$$
The goal of Eduardo is to make the number $M$ divisible by $p$, and the goal of Fernando is to prevent this.
Prove that Eduardo has a winning strategy.


## 2017 — N7

**Record:** `imo_2017_f79d3e`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2017_f79d3e.json.gz).

Say that an ordered pair $(x, y)$ of integers is an irreducible lattice point if $x$ and $y$ are relatively prime. For any finite set $S$ of irreducible lattice points, show that there is a homogenous polynomial in two variables, $f(x, y)$, with integer coefficients, of degree at least 1, such that $f(x, y)=1$ for each $(x, y)$ in the set $S$.

Note: A homogenous polynomial of degree $n$ is any nonzero polynomial of the form
$$
f(x, y)=a_{0} x^{n}+a_{1} x^{n-1} y+a_{2} x^{n-2} y^{2}+\cdots+a_{n-1} x y^{n-1}+a_{n} y^{n} .
$$


## 2018 — N7

**Record:** `imo_2018_11785f`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2018_11785f.json.gz).

Let $n \geqslant 2018$ be an integer, and let $a_{1}, a_{2}, \ldots, a_{n}, b_{1}, b_{2}, \ldots, b_{n}$ be pairwise distinct positive integers not exceeding $5n$. Suppose that the sequence
$$
\frac{a_{1}}{b_{1}}, \frac{a_{2}}{b_{2}}, \ldots, \frac{a_{n}}{b_{n}}
$$
forms an arithmetic progression. Prove that the terms of the sequence are equal.


## 2018 — N6

**Record:** `imo_2018_174f68`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2018_174f68.json.gz).

Let $f:\{1,2,3, \ldots\} \rightarrow\{2,3, \ldots\}$ be a function such that $f(m+n) \mid f(m)+f(n)$ for all pairs $m, n$ of positive integers. Prove that there exists a positive integer $c>1$ which divides all values of $f$.


## 2018 — A3

**Record:** `imo_2018_1d7f33`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2018_1d7f33.json.gz).

Given any set $S$ of positive integers, show that at least one of the following two assertions holds:
(1) There exist distinct finite subsets $F$ and $G$ of $S$ such that $\sum_{x \in F} 1 / x = \sum_{x \in G} 1 / x$;
(2) There exists a positive rational number $r < 1$ such that $\sum_{x \in F} 1 / x \neq r$ for all finite subsets $F$ of $S$.


## 2018 — C6

**Record:** `imo_2018_556799`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2018_556799.json.gz).

Let $a$ and $b$ be distinct positive integers. The following infinite process takes place on an initially empty board.
(i) If there is at least a pair of equal numbers on the board, we choose such a pair and increase one of its components by $a$ and the other by $b$.
(ii) If no such pair exists, we write down two times the number $0$.
Prove that, no matter how we make the choices in (i), operation (ii) will be performed only finitely many times.


## 2018 — N2

**Record:** `imo_2018_9d5567`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2018_9d5567.json.gz).

Let $n > 1$ be a positive integer. Each cell of an $n \times n$ table contains an integer. Suppose that the following conditions are satisfied:
(i) Each number in the table is congruent to $1$ modulo $n$;
(ii) The sum of numbers in any row, as well as the sum of numbers in any column, is congruent to $n$ modulo $n^{2}$.
Let $R_{i}$ be the product of the numbers in the $i^{\text{th}}$ row, and $C_{j}$ be the product of the numbers in the $j^{\text{th}}$ column. Prove that the sums $R_{1} + \cdots + R_{n}$ and $C_{1} + \cdots + C_{n}$ are congruent modulo $n^{4}$.


## 2019 — N3

**Record:** `imo_2019_05dd86`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_05dd86.json.gz).

**Source issue:** Zero-polynomial convention would trivialize the closure condition; the substantive nonconstant version is made explicit in N10.

We say that a set $S$ of integers is rootiful if, for any positive integer $n$ and any $a_{0}, a_{1}, \ldots, a_{n} \in S$, all integer roots of the polynomial $a_{0}+a_{1} x+\cdots+a_{n} x^{n}$ are also in $S$. Find all rootiful sets of integers that contain all numbers of the form $2^{a}-2^{b}$ for positive integers $a$ and $b$.


## 2019 — N7

**Record:** `imo_2019_152467`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_152467.json.gz).

Prove that there is a constant $c>0$ and infinitely many positive integers $n$ with the following property: there are infinitely many positive integers that cannot be expressed as the sum of fewer than $c n \log (n)$ pairwise coprime $n^{\text{th}}$ powers.


## 2019 — N2

**Record:** `imo_2019_199a44`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_199a44.json.gz).

**Source issue:** One imported proof has a malformed square-root bound; N09 uses a separately checked inequality chain.

Find all triples $(a, b, c)$ of positive integers such that $a^{3} + b^{3} + c^{3} = (a b c)^{2}$.


## 2019 — N1

**Record:** `imo_2019_8eb868`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_8eb868.json.gz).

Find all pairs $(m, n)$ of positive integers satisfying the equation
$$
\left(2^{n}-1\right)\left(2^{n}-2\right)\left(2^{n}-4\right) \cdots\left(2^{n}-2^{n-1}\right)=m!
$$


## 2019 — A7

**Record:** `imo_2019_aeca2a`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_aeca2a.json.gz).

Let $\mathbb{Z}$ be the set of integers. We consider functions $f: \mathbb{Z} \rightarrow \mathbb{Z}$ satisfying
$$
f(f(x+y)+y)=f(f(x)+y)
$$
for all integers $x$ and $y$. For such a function, we say that an integer $v$ is $f$-rare if the set
$$
X_{v}=\{x \in \mathbb{Z}: f(x)=v\}
$$
is finite and nonempty.

a. Prove that there exists such a function $f$ for which there is an $f$-rare integer.

b. Prove that no such function $f$ can have more than one $f$-rare integer.


## 2019 — N5

**Record:** `imo_2019_aedde5`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_aedde5.json.gz).

**Source issue:** One imported alternate proof reverses a binomial ratio and invokes unnecessary Dirichlet machinery. N11 proves the exact criterion directly.

Let $a$ be a positive integer. We say that a positive integer $b$ is $a$-good if $\binom{a n}{b}-1$ is divisible by $a n+1$ for all positive integers $n$ with $a n \geqslant b$. Suppose $b$ is a positive integer such that $b$ is $a$-good, but $b+2$ is not $a$-good. Prove that $b+1$ is prime.


## 2019 — N8

**Record:** `imo_2019_ca3568`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_ca3568.json.gz).

Let $a$ and $b$ be two positive integers. Prove that the integer
$$
a^{2} + \left\lceil \frac{4 a^{2}}{b} \right\rceil
$$
is not a square. (Here $\lceil z\rceil$ denotes the least integer greater than or equal to $z$.)


## 2019 — N6

**Record:** `imo_2019_ce6a78`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_ce6a78.json.gz).

Let $H=\{\lfloor i \sqrt{2}\rfloor: i \in \mathbb{Z}_{>0}\}=\{1,2,4,5,7, \ldots\}$, and let $n$ be a positive integer. Prove that there exists a constant $C$ such that, if $A \subset\{1,2, \ldots, n\}$ satisfies $|A| \geqslant C \sqrt{n}$, then there exist $a, b \in A$ such that $a-b \in H$. (Here $\mathbb{Z}_{>0}$ is the set of positive integers, and $\lfloor z\rfloor$ denotes the greatest integer less than or equal to $z$.)


## 2021 — A2

**Record:** `imo_2021_18d4a8`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_18d4a8.json.gz).

For every integer $n \geqslant 1$ consider the $n \times n$ table with entry $\left\lfloor\frac{ij}{n+1}\right\rfloor$ at the intersection of row $i$ and column $j$, for every $i=1, \ldots, n$ and $j=1, \ldots, n$. Determine all integers $n \geqslant 1$ for which the sum of the $n^{2}$ entries in the table is equal to $\frac{1}{4} n^{2}(n-1)$.


## 2021 — N4

**Record:** `imo_2021_1c3cfc`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_1c3cfc.json.gz).

Alice is given a rational number $r>1$ and a line with two points $B \neq R$, where point $R$ contains a red bead and point $B$ contains a blue bead. Alice plays a solitaire game by performing a sequence of moves. In every move, she chooses a (not necessarily positive) integer $k$, and a bead to move. If that bead is placed at point $X$, and the other bead is placed at $Y$, then Alice moves the chosen bead to point $X^{\prime}$ with $\overrightarrow{Y X^{\prime}}=r^{k} \overrightarrow{Y X}$.

Alice's goal is to move the red bead to the point $B$. Find all rational numbers $r>1$ such that Alice can reach her goal in at most 2021 moves.


## 2021 — C1

**Record:** `imo_2021_5bfb5f`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_5bfb5f.json.gz).

Let $S$ be an infinite set of positive integers, such that there exist four pairwise distinct $a, b, c, d \in S$ with $\operatorname{gcd}(a, b) \neq \operatorname{gcd}(c, d)$. Prove that there exist three pairwise distinct $x, y, z \in S$ such that $\operatorname{gcd}(x, y)=\operatorname{gcd}(y, z) \neq \operatorname{gcd}(z, x)$.


## 2021 — N6

**Record:** `imo_2021_862aab`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_862aab.json.gz).

Determine all integers $n \geqslant 2$ with the following property: every $n$ pairwise distinct integers whose sum is not divisible by $n$ can be arranged in some order $a_{1}, a_{2}, \ldots, a_{n}$ so that $n$ divides $1 \cdot a_{1}+2 \cdot a_{2}+\cdots+n \cdot a_{n}$.


## 2021 — N8

**Record:** `imo_2021_bfcfa1`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_bfcfa1.json.gz).

For a polynomial $P(x)$ with integer coefficients let $P^{1}(x)=P(x)$ and $P^{k+1}(x)= P\left(P^{k}(x)\right)$ for $k \geqslant 1$. Find all positive integers $n$ for which there exists a polynomial $P(x)$ with integer coefficients such that for every integer $m \geqslant 1$, the numbers $P^{m}(1), \ldots, P^{m}(n)$ leave exactly $\left\lceil n / 2^{m}\right\rceil$ distinct remainders when divided by $n$.


## 2021 — N5

**Record:** `imo_2021_d10161`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_d10161.json.gz).

Prove that there are only finitely many quadruples $(a, b, c, n)$ of positive integers such that
$$
n! = a^{n-1} + b^{n-1} + c^{n-1}
$$


## 2021 — N7

**Record:** `imo_2021_dbdd71`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_dbdd71.json.gz).

Let $a_{1}, a_{2}, a_{3}, \ldots$ be an infinite sequence of positive integers such that $a_{n+2m}$ divides $a_{n} + a_{n+m}$ for all positive integers $n$ and $m$. Prove that this sequence is eventually periodic, i.e. there exist positive integers $N$ and $d$ such that $a_{n} = a_{n+d}$ for all $n > N$.


## 2022 — N8.

**Record:** `imo_2022_264ed6`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2022_264ed6.json.gz).

Prove that $5^{n}-3^{n}$ is not divisible by $2^{n}+65$ for any positive integer $n$.


## 2022 — C6.

**Record:** `imo_2022_783196`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2022_783196.json.gz).

Let $n$ be a positive integer. We start with $n$ piles of pebbles, each initially containing a single pebble. One can perform moves of the following form: choose two piles, take an equal number of pebbles from each pile and form a new pile out of these pebbles. For each positive integer $n$, find the smallest number of non-empty piles that one can obtain by performing a finite sequence of moves of this form.


## 2022 — N5.

**Record:** `imo_2022_d417bb`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2022_d417bb.json.gz).

For each $1 \leqslant i \leqslant 9$ and $T \in \mathbb{N}$, define $d_{i}(T)$ to be the total number of times the digit $i$ appears when all the multiples of $1829$ between $1$ and $T$ inclusive are written out in base $10$.
Show that there are infinitely many $T \in \mathbb{N}$ such that there are precisely two distinct values among $d_{1}(T), d_{2}(T), \ldots, d_{9}(T)$.


## 2023 — N5.

**Record:** `imo_2023_1ffb42`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2023_1ffb42.json.gz).

Let $a_{1} < a_{2} < a_{3} < \cdots$ be positive integers such that $a_{k+1}$ divides $2(a_{1} + a_{2} + \cdots + a_{k})$ for every $k \geqslant 1$. Suppose that for infinitely many primes $p$, there exists $k$ such that $p$ divides $a_{k}$. Prove that for every positive integer $n$, there exists $k$ such that $n$ divides $a_{k}$.


## 2023 — N1.

**Record:** `imo_2023_2e005b`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2023_2e005b.json.gz).

Determine all positive, composite integers $n$ that satisfy the following property: if the positive divisors of $n$ are $1=d_{1}<d_{2}<\cdots<d_{k}=n$, then $d_{i}$ divides $d_{i+1}+d_{i+2}$ for every $1 \leqslant i \leqslant k-2$.


## 2023 — N8.

**Record:** `imo_2023_3c0851`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2023_3c0851.json.gz).

Let $\mathbb{Z}_{>0}$ be the set of positive integers. Determine all functions $f: \mathbb{Z}_{>0} \rightarrow \mathbb{Z}_{>0}$ such that
$$
f^{b f(a)}(a+1) = (a+1) f(b)
$$
holds for all $a, b \in \mathbb{Z}_{>0}$, where $f^{k}(n) = f(f(\cdots f(n) \cdots))$ denotes the composition of $f$ with itself $k$ times.


## 2023 — N7.

**Record:** `imo_2023_4786b3`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2023_4786b3.json.gz).

Let $a, b, c, d$ be positive integers satisfying
$$
\frac{a b}{a+b}+\frac{c d}{c+d}=\frac{(a+b)(c+d)}{a+b+c+d}
$$
Determine all possible values of $a+b+c+d$.


## 2023 — N6.

**Record:** `imo_2023_693aff`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2023_693aff.json.gz).

A sequence of integers $a_{0}, a_{1}, a_{2}, \ldots$ is called kawaii, if $a_{0}=0, a_{1}=1$, and, for any positive integer $n$, we have
$$
\left(a_{n+1}-3 a_{n}+2 a_{n-1}\right)\left(a_{n+1}-4 a_{n}+3 a_{n-1}\right)=0 .
$$
An integer is called kawaii if it belongs to a kawaii sequence.
Suppose that two consecutive positive integers $m$ and $m+1$ are both kawaii (not necessarily belonging to the same kawaii sequence). Prove that 3 divides $m$, and that $m / 3$ is kawaii.


## 2023 — N4.

**Record:** `imo_2023_706002`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2023_706002.json.gz).

Let $a_{1}, a_{2}, \ldots, a_{n}, b_{1}, b_{2}, \ldots, b_{n}$ be $2n$ positive integers such that the $n+1$ products
$$
\begin{gathered}
a_{1} a_{2} a_{3} \cdots a_{n}, \\
b_{1} a_{2} a_{3} \cdots a_{n}, \\
b_{1} b_{2} a_{3} \cdots a_{n}, \\
\vdots \\
b_{1} b_{2} b_{3} \cdots b_{n}
\end{gathered}
$$
form a strictly increasing arithmetic progression in that order. Determine the smallest positive integer that could be the common difference of such an arithmetic progression.


## 2024 — A1

**Record:** `imo_2024_071598`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2024_071598.json.gz).

Determine all real numbers $\alpha$ such that the number
$$
\lfloor\alpha\rfloor+\lfloor 2 \alpha\rfloor+\cdots+\lfloor n \alpha\rfloor
$$
is a multiple of $n$ for every positive integer $n$. (Here $\lfloor z\rfloor$ denotes the greatest integer less than or equal to $z$.)


## 2024 — C2

**Record:** `imo_2024_0968d7`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2024_0968d7.json.gz).

Let $n$ be a positive integer. The integers $1, 2, 3, \ldots, n^{2}$ are to be written in the cells of an $n \times n$ board such that each integer is written in exactly one cell and each cell contains exactly one integer. For every integer $d$ with $d \mid n$, the $d$-division of the board is the division of the board into $(n / d)^{2}$ nonoverlapping sub-boards, each of size $d \times d$, such that each cell is contained in exactly one $d \times d$ sub-board.

We say that $n$ is a cool number if the integers can be written on the $n \times n$ board such that, for each integer $d$ with $d \mid n$ and $1 < d < n$, in the $d$-division of the board, the sum of the integers written in each $d \times d$ sub-board is not a multiple of $d$.

Determine all even cool numbers.


## 2024 — A6

**Record:** `imo_2024_240890`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2024_240890.json.gz).

Let $a_{0}, a_{1}, a_{2}, \ldots$ be an infinite strictly increasing sequence of positive integers such that for each $n \geqslant 1$ we have
$$
a_{n} \in\left\{\frac{a_{n-1}+a_{n+1}}{2}, \sqrt{a_{n-1} \cdot a_{n+1}}\right\}
$$
Let $b_{1}, b_{2}, \ldots$ be an infinite sequence of letters defined as
$$
b_{n}= \begin{cases}A, & \text{ if } a_{n}=\frac{1}{2}\left(a_{n-1}+a_{n+1}\right) \\ G, & \text{ otherwise }\end{cases}
$$
Prove that there exist positive integers $n_{0}$ and $d$ such that for all $n \geqslant n_{0}$ we have $b_{n+d}=b_{n}$.


## 2024 — N1

**Record:** `imo_2024_268bb8`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2024_268bb8.json.gz).

Find all positive integers $n$ with the following property: for all positive divisors $d$ of $n$, we have that $d+1 \mid n$ or $d+1$ is prime.


## 2024 — N6

**Record:** `imo_2024_3f4e9a`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2024_3f4e9a.json.gz).

Let $n$ be a positive integer. We say that a polynomial $P$ with integer coefficients is $n$-good if there exists a polynomial $Q$ of degree 2 with integer coefficients such that $Q(k)(P(k)+Q(k))$ is never divisible by $n$ for any integer $k$.
Determine all integers $n$ such that every polynomial with integer coefficients is an $n$-good polynomial.


## 2024 — A2

**Record:** `imo_2024_5877d2`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2024_5877d2.json.gz).

**Source issue:** The cost-table explanation has row/index slips; the variables are x_0 through x_n. Corrected in A11.

Let $n$ be a positive integer. Find the minimum possible value of
$$
S = 2^{0} x_{0}^{2} + 2^{1} x_{1}^{2} + \cdots + 2^{n} x_{n}^{2}
$$
where $x_{0}, x_{1}, \ldots, x_{n}$ are nonnegative integers such that $x_{0} + x_{1} + \cdots + x_{n} = n$.


## 2024 — N7

**Record:** `imo_2024_7201b9`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2024_7201b9.json.gz).

Let $\mathbb{Z}_{>0}$ denote the set of positive integers. Let $f: \mathbb{Z}_{>0} \rightarrow \mathbb{Z}_{>0}$ be a function satisfying the following property: for $m, n \in \mathbb{Z}_{>0}$, the equation
$$
f(m n)^2 = f\left(m^2\right) f(f(n)) f(m f(n))
$$
holds if and only if $m$ and $n$ are coprime.
For each positive integer $n$, determine all the possible values of $f(n)$.


## 2024 — N2

**Record:** `imo_2024_8acaec`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2024_8acaec.json.gz).

**Source issue:** Attached source solution concerns an unrelated finite-set problem. Its solution text is withheld from this edition; the statement and pointer retain a mismatch warning.

Determine all sequences $a_{1}, a_{2}, \ldots$ of positive integers such that, for any pair of positive integers $m \leqslant n$, the arithmetic and geometric means
$$
\frac{a_{m}+a_{m+1}+\cdots+a_{n}}{n-m+1} \quad \text{ and } \quad \left(a_{m} a_{m+1} \cdots a_{n}\right)^{\frac{1}{n-m+1}}
$$
are both integers.



# IMO-TST source statements

## 2001 — 5

**Record:** `usa_2001_196610`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2001_196610.json.gz).

Let $S$ be a set of integers (not necessarily positive) such that

a. there exist $a, b \in S$ with $\gcd(a, b) = \gcd(a - 2, b - 2) = 1$;

b. if $x$ and $y$ are elements of $S$ (possibly equal), then $x^2 - y$ also belongs to $S$.

Prove that $S$ is the set of all integers.


## 2001 — 4

**Record:** `usa_2001_9b2113`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2001_9b2113.json.gz).

Let $n$ be an odd integer greater than $1$ and let $c_1, c_2, \dots, c_n$ be integers. For each permutation $a = (a_1, a_2, \dots, a_n)$ of $\{1, 2, \dots, n\}$, define $S(a) = \sum_{i=1}^n c_i a_i$. Prove that there exist permutations $b$ and $c$, $b \neq c$, such that $n!$ divides $S(b) - S(c)$.


## 2001 — 8

**Record:** `usa_2001_a49c5f`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2001_a49c5f.json.gz).

Find all pairs of nonnegative integers $(m, n)$ such that
$$
(m + n - 5)^2 = 9mn.
$$


## 2001 — 6

**Record:** `usa_2001_c629af`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2001_c629af.json.gz).

Let $a > b > c > d$ be positive integers and suppose
$$
ac + bd = (b + d + a - c)(b + d - a + c).
$$
Prove that $ab + cd$ is not prime.


## 2001 — 3

**Record:** `usa_2001_e83e65`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2001_e83e65.json.gz).

For a set $S$, let $|S|$ denote the number of elements in $S$. Let $A$ be a set of positive integers with $|A| = 2001$. Prove that there exists a set $B$ such that
(i) $B \subseteq A$;
(ii) $|B| \geq 668$;
(iii) for any $u, v \in B$ (not necessarily distinct), $u + v \notin B$.


## 2001 — 6

**Record:** `vnm_2001_95fe00`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2001_95fe00.json.gz).

Let be given a sequence of positive integers $\{a_n\}$, $n = 1, 2, 3, \ldots$, satisfying the condition
$$
0 < a_{n+1} - a_n \le 2001
$$
for every $n = 1, 2, 3, \ldots$. Prove that there exists an infinite number of couples of positive integers $(p, q)$ such that $p < q$ and $a_p$ is a divisor of $a_q$.


## 2001 — 1

**Record:** `vnm_2001_ff5434`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2001_ff5434.json.gz).

The sequence of integers $\{a_n\}$, $n = 0, 1, 2, \ldots$, is defined by:
$a_0 = 1$ and $a_n = a_{n-1} + a_{\lceil n/3 \rceil}$ for every $n = 1, 2, 3, \ldots$.
Prove that for every prime number $p \le 13$, there exists an infinite number of natural numbers $k$ such that $a_k$ is divisible by $p$.
([x] denotes the integral part of x).


## 2003 — 6

**Record:** `vnm_2003_7f3457`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2003_7f3457.json.gz).

Let $n$ be a positive integer. Prove that the number $2^n + 1$ has no prime divisor of the form $8k-1$, where $k$ is a positive integer.


## 2004 — 5

**Record:** `usa_2004_33bab6`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2004_33bab6.json.gz).

Let $A = (0,0,0)$ be the origin in the three dimensional coordinate space. The *weight* of a point is the sum of the absolute values of its coordinates. A point is a *primitive lattice point* if all its coordinates are integers with their greatest common divisor equal to 1. A square $ABCD$ is called a *unbalanced primitive integer square* if it has integer side length and the points $B$ and $D$ are primitive lattice points with different weights.
Show that there are infinitely many unbalanced primitive integer squares $AB_iC_iD_i$ such that the plane containing the squares are not parallel to each other.


## 2004 — 2

**Record:** `usa_2004_7153d3`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2004_7153d3.json.gz).

Suppose $a_1, \dots, a_n$ are integers whose greatest common divisor is $1$. Let $S$ be a set of integers with the following properties.

a. For $i = 1, \dots, n$, $a_i \in S$.

b. For $i, j = 1, \dots, n$ (not necessarily distinct), $a_i - a_j \in S$.

c. For any integers $x, y \in S$, if $x + y \in S$, then $x - y \in S$.

Prove that $S$ must be equal to the set of all integers.


## 2004 — 3

**Record:** `usa_2004_954202`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2004_954202.json.gz).

A $2004 \times 2004$ array of points is drawn. Find the largest integer $n$ such that it is possible to draw a convex $n$-sided polygon whose vertices lie on the points of the array.


## 2006 — 4

**Record:** `usa_2006_590ebb`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2006_590ebb.json.gz).

Let $n$ be a positive integer. Find, with proof, the least positive integer $d_n$ which cannot be expressed in the form
$$
\sum_{i=1}^{n} (-1)^{a_i} 2^{b_i},
$$
where $a_i$ and $b_i$ are nonnegative integers for each $i$.


## 2007 — 6

**Record:** `usa_2007_c129df`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2007_c129df.json.gz).

For a polynomial $P(x)$ with integer coefficients, $r(2i - 1)$ (for $i = 1, 2, 3, \dots, 512$) is the remainder obtained when $P(2i - 1)$ is divided by $1024$. The sequence
$$
(r(1), r(3), \dots, r(1023))
$$
is called the *remainder sequence* of $P(x)$. A remainder sequence is called *complete* if it is a permutation of $(1, 3, 5, \dots, 1023)$. Prove that there are no more than $2^{35}$ different complete remainder sequences.


## 2008 — 6

**Record:** `usa_2008_7bcea0`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2008_7bcea0.json.gz).

Let $n$ be a positive integer not divisible by the cube of a prime. Given an integer-coefficient polynomial $f(x)$, define its *signature modulo* $n$ to be the (ordered) sequence $f(1), \dots, f(n)$ modulo $n$. Of the $n^n$ such $n$-term sequences of integers modulo $n$, how many are the signature of some polynomial $f(x)$?


## 2008 — 4

**Record:** `usa_2008_92d482`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2008_92d482.json.gz).

Prove that for no integer $n$ is $n^7 + 7$ a perfect square.


## 2009 — 3

**Record:** `usa_2009_3358a9`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2009_3358a9.json.gz).

For each positive integer $n$, let $c(n)$ be the largest real number such that
$$
c(n) \leq \left| \frac{f(a) - f(b)}{a - b} \right|
$$
for all triples $(f, a, b)$ such that
* $f$ is a polynomial of degree $n$ taking integers to integers, and
* $a, b$ are integers with $f(a) \neq f(b)$.

Find $c(n)$.


## 2010 — 2

**Record:** `sgp_2010_c6cc18`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/singapore/sgp_2010_c6cc18.json.gz).

A subset $T$ of $\{7, 8, ..., 26\}$ does not contain three elements whose product is a perfect square. Determine the maximum number of elements in $T$.


## 2010 — 6

**Record:** `usa_2010_061aff`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2010_061aff.json.gz).

Let $T$ be a finite set of positive integers greater than $1$. A subset $S$ of $T$ is called *good*, if for every $t \in T$ there exists some $s \in S$ with $\gcd(s, t) > 1$. Prove that the number of good subsets of $T$ is odd.


## 2010 — 9

**Record:** `usa_2010_775cb8`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2010_775cb8.json.gz).

Determine whether or not there exists a positive integer $k$ such that $p = 6k + 1$ is prime and
$$
\binom{3k}{k} \equiv 1 \pmod{p}.
$$
(This problem was suggested by Gabriel Carroll.)


## 2010 — 1

**Record:** `usa_2010_7c7be7`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2010_7c7be7.json.gz).

Let $P(x)$ be a polynomial with integer coefficients such that $P(0) = 0$ and
$$
\text{gcd}(P(0), P(1), P(2), \dots) = 1.
$$
Prove that there are infinitely many positive integers $n$ such that
$$
\text{gcd}(P(n) - P(0), P(n+1) - P(1), P(n+2) - P(2), \dots) = n.
$$


## 2010 — 5

**Record:** `usa_2010_7fb109`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2010_7fb109.json.gz).

Define the sequence $a_1, a_2, a_3, \dots$ by $a_1 = 1$ and
$$
a_n = a_{\lfloor n/2 \rfloor} + a_{\lfloor n/3 \rfloor} + \dots + a_{\lfloor n/n \rfloor} + 1
$$
for $n > 1$. Prove that there are infinitely many $n$ such that
$$
a_n \equiv n \pmod{2^{2010}}.
$$
(This problem was suggested by Gabriel Carroll.)


## 2010 — Problem 2

**Record:** `vnm_2010_bebf2f`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2010_bebf2f.json.gz).

For each positive integer $n$, consider the set
$$
T_n = \{ 11(h + k) + 10(n^h + n^k) \mid h, k \in \mathbb{N} \text{ và } 1 \le h \le k \le 10 \}.
$$
Find all positive integers $n$, such that the set $T_n$ has the following property: For all $a, b$ in $T_n$ with $a \ne b$, we always have $a - b$ is not divisible by $110$.
($N$ denotes the set of non-negative integers).


## 2011 — 3

**Record:** `usa_2011_8b387a`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2011_8b387a.json.gz).

Let $p$ be a prime. We say that a sequence of integers $\{z_n\}_{n=0}^{\infty}$ is a $p$-pod if for each $e \ge 0$, there is an $N \ge 0$ such that whenever $m \ge N$, $p^e$ divides the sum
$$
\sum_{k=0}^{m} (-1)^k \binom{m}{k} z_k.
$$

Prove that if both sequences $\{x_n\}_{n=0}^{\infty}$ and $\{y_n\}_{n=0}^{\infty}$ are $p$-pods, then the sequence $\{x_n y_n\}_{n=0}^{\infty}$ is a $p$-pod.


## 2011 — 6

**Record:** `usa_2011_ff9f97`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2011_ff9f97.json.gz).

A polynomial $P(x)$ is called *nice* if $P(0) = 1$ and the nonzero coefficients of $P(x)$ alternate between $1$ and $-1$ when written in order. Suppose $P(x)$ is nice, and let $m$ and $n$ be two relatively prime positive integers. Show that
$$
Q(x) = P(x^n) \cdot \frac{(x^{mn} - 1)(x - 1)}{(x^m - 1)(x^n - 1)}
$$
is nice as well.


## 2011 — 5

**Record:** `vnm_2011_5f2ce6`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2011_5f2ce6.json.gz).

Find all positive integer $n$ such that $2^{n+2} \cdot (2^n - 1) - 8 \cdot 3^n + 1$ is a perfect square.


## 2011 — 1

**Record:** `vnm_2011_f6e2ec`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2011_f6e2ec.json.gz).

1. At the point $(1, 1)$ of the coordinate plane $(Oxy)$, there is a cào cào. From that point the cào cào can only jump to other integral points by the rule: from the positive integral point $A$, the cào cào jumps to the positive integral point $B$ if the triangle $OAB$ has area equal to $\frac{1}{2}$.

1/ Find all points $(m, n)$ to which the cào cào can jump to after a finite number of jumps, starting from the point $(1, 1)$.

2/ Let $(m, n)$ be a positive integral point with property mentioned in 1/. Show that there exists a way, in which the cào cào can jump from point $(1, 1)$ to point $(m, n)$ with not more than $|m - n|$ jumps.


## 2012 — 8

**Record:** `ind_2012_2ce73f`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2012_2ce73f.json.gz).

Let $S$ be a nonempty set of primes satisfying the property that for each proper subset $P$ of $S$, all the prime factors of the number $\left(\prod_{p \in P} p\right) - 1$ are also in $S$. Determine all possible such sets $S$.


## 2012 — 3

**Record:** `usa_2012_485e07`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2012_485e07.json.gz).

Prove that there exists a real constant $c$ such that for any pair $(x, y)$ of real numbers, there exist relatively prime integers $m$ and $n$ satisfying the relation
$$\sqrt{(x-m)^2 + (y-n)^2} < c \log(x^2 + y^2 + 2).$$
(This problem was suggested by Daniel Kane.)


## 2012 — 7

**Record:** `usa_2012_5abc60`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2012_5abc60.json.gz).

Determine all positive integers $n$, $n \ge 2$, such that the following statement is true:
If $(a_1, a_2, \ldots, a_n)$ is a sequence of positive integers with $a_1 + a_2 + \cdots + a_n = 2n - 1$, then there is a block of (at least two) consecutive terms in the sequence with their (arithmetic) mean being an integer.


## 2012 — 8

**Record:** `usa_2012_7b943f`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2012_7b943f.json.gz).

Let $x_0, x_1, \dots, x_{n_0-1}$ be integers, and let $d_1, d_2, \dots, d_k$ be positive integers with $n_0 = d_1 > d_2 > \dots > d_k$ and $\gcd(d_1, d_2, \dots, d_k) = 1$. For every integer $n \ge n_0$, define
$$
x_n = \left\lfloor \frac{x_{n-d_1} + x_{n-d_2} + \dots + x_{n-d_k}}{k} \right\rfloor.
$$
Show that the sequence $\{x_n\}$ is eventually constant.


## 2012 — 8.

**Record:** `usa_2012_893048`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2012_893048.json.gz).

Find all pairs $(a, n)$ of positive integers with $n > 1$ such that for every prime $p$ dividing $a^n - 1$, there exists $0 < k < n$ such that $p$ divides $a^k - 1$.


## 2012 — 5

**Record:** `usa_2012_c103be`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2012_c103be.json.gz).

Determine all positive integers $n$ such that the (3-variable) polynomial
$$
P_n(x, y, z) = (x - y)^{2n}(y - z)^{2n} + (y - z)^{2n}(z - x)^{2n} + (z - x)^{2n}(x - y)^{2n}
$$
divides the (3-variable) polynomial
$$
Q_n(x, y, z) = [(x - y)^{2n} + (y - z)^{2n} + (z - x)^{2n}]^{2n}.
$$


## 2012 — 3.

**Record:** `usa_2012_e9f6ee`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2012_e9f6ee.json.gz).

Determine, with proof, whether or not there exist integers $a, b, c > 2010$ satisfying the equation
$$
a^3 + 2b^3 + 4c^3 = 6abc + 1.
$$


## 2012 — Bài 3

**Record:** `vnm_2012_f548c9`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_f548c9.json.gz).

Cho trước một số nguyên tố $p$ không nhỏ hơn $17$. Chứng minh rằng $t=3$ là số nguyên dương lớn nhất có tính chất: Với mọi bộ số nguyên $a, b, c, d$ sao cho $abc$ không chia hết cho $p$, nhưng $a+b+c$ chia hết cho $p$ thì luôn tồn tại $x, y, z \in \{0, 1, ..., \lfloor \frac{p}{t} \rfloor - 1\}$ để $ax+by+cz+d$ chia hết cho $p$. ($\lfloor \frac{p}{t} \rfloor$ kí hiệu số nguyên lớn nhất không vượt quá $\frac{p}{t}$).


## 2013 — 3

**Record:** `ind_2013_5ef73e`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2013_5ef73e.json.gz).

For a positive integer $n$, a sum-friendly odd partition of $n$ is a sequence $(a_1, a_2, \dots, a_k)$ of odd positive integers with $a_1 \le a_2 \le \dots \le a_k$ and $a_1 + a_2 + \dots + a_k = n$ such that for all positive integers $m \le n$, $m$ can be uniquely written as a subsum $m = a_{i_1} + a_{i_2} + \dots + a_{i_r}$. (Two subsums $a_{i_1} + a_{i_2} + \dots + a_{i_r}$, and $a_{j_1} + a_{j_2} + \dots + a_{j_s}$ with $i_1 < i_2 < \dots < i_r$ and $j_1 < j_2 < \dots < j_s$ are considered the same if $r = s$ and $a_{i_l} = a_{j_l}$ for $1 \le l \le r$.) For example, $(1, 1, 3, 3)$ is a sum-friendly odd partition of $8$. Find the number of sum-friendly odd partitions of $9999$.


## 2013 — 7.

**Record:** `usa_2013_536721`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2013_536721.json.gz).

Prove that the ratio
$$
\frac{1^1 + 3^3 + 5^5 + \dots + (2^{2012} - 1)^{(2^{2012} - 1)}}{2^{2012}}
$$
is an odd integer.


## 2013 — 1.

**Record:** `usa_2013_bfa49c`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2013_bfa49c.json.gz).

Find all infinite sequences $a_1, a_2, \dots$ of positive integers satisfying the following properties:

a. $a_1 < a_2 < a_3 < \dots$,

b. there are no positive integers $i, j, k$, not necessarily distinct, such that $a_i + a_j = a_k$,

c. there are infinitely many positive integers $k$ such that $a_k = 2k - 1$.


## 2014 — 2.

**Record:** `usa_2014_402d1a`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2014_402d1a.json.gz).

A finite sequence of integers $a_1, a_2, \dots, a_n$ is called *regular* if there exists a real number $x$ satisfying
$$
\lfloor kx \rfloor = a_k \quad \text{for } 1 \le k \le n.
$$
Given a regular sequence $a_1, a_2, \dots, a_n$, for $1 \le k \le n$ we say the term $a_k$ is *forced* if the following condition is satisfied: the sequence
$$
a_1, a_2, \dots, a_{k-1}, b
$$
is regular if and only if $b = a_k$. Find the maximum possible number of forced terms in a regular sequence with 1000 terms.


## 2014 — 6.

**Record:** `usa_2014_76068d`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2014_76068d.json.gz).

For a prime $p$, a subset $S$ of residues modulo $p$ is called a *sum-free multiplicative subgroup of $\mathbb{F}_p$* if:

* there is a nonzero residue $\alpha$ modulo $p$ such that $S = \{1, \alpha^1, \alpha^2, \dots\}$ (all considered mod $p$), and
* there are no $a, b, c \in S$ (not necessarily distinct) such that $a + b \equiv c \pmod p$.

Prove that for every integer $N$, there is a prime $p$ and a sum-free multiplicative subgroup $S$ of $\mathbb{F}_p$ such that $|S| \ge N$.


## 2014 — 2.

**Record:** `usa_2014_ee6270`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2014_ee6270.json.gz).

Let $a_1, a_2, a_3, \dots$ be a sequence of integers, with the property that every consecutive group of $a_i$'s averages to a perfect square. More precisely, for every positive integers $n$ and $k$, the quantity
$$
\frac{a_n + a_{n+1} + \dots + a_{n+k-1}}{k}
$$
is always the square of an integer. Prove that the sequence must be constant (all $a_i$ are equal to the same perfect square).


## 2014 — 9.

**Record:** `usa_2014_ef9290`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2014_ef9290.json.gz).

Let $r$ be a rational number in the interval $[-1, 1]$, and let $\theta = \cos^{-1} r$. Call a subset $S$ of the plane good if $S$ is unchanged upon rotation by $\theta$ around any point of $S$ (in both clockwise and counterclockwise directions). Determine all values of $r$ satisfying the following property: The midpoint of any two points in a good set also lies in the set.

(This problem was suggested by Ricky Liu.)


## 2014 — 8.

**Record:** `usa_2014_f1b5d5`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2014_f1b5d5.json.gz).

Define a function $f : \mathbb{N} \to \mathbb{N}$ by $f(1) = 1$, $f(n + 1) = f(n) + 2^{f(n)}$ for every positive integer $n$. Prove that $f(1), f(2), \dots, f(3^{2013})$ leave distinct remainders when divided by $3^{2013}$.

(This problem was suggested by Evan O'Dorney.)


## 2015 — 3

**Record:** `vnm_2015_0a1466`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2015_0a1466.json.gz).

a) Find all positive integers $k$ with the property $T(20)$, where a positive integer $k$ has the property $T(m)$ if for any positive integer $a$, there exists a positive integer $n$ such that
$$
1^k + 2^k + \dots + n^k \equiv a \pmod{m}.
$$

b) Find the smallest positive integer $k$ with the property $T(20^{15})$.


## 2016 — 2

**Record:** `ind_2016_c1a286`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2016_c1a286.json.gz).

Let $n$ be a natural number. A sequence $x_1, x_2, \dots, x_{n^2}$ is called *n-*good if each $x_i$ is an element of $\{1, 2, \dots, n\}$ and the ordered pairs $(x_i, x_{i+1})$ are all different for $i = 1, 2, \dots, n^2$ (here we consider the subscripts modulo $n^2$). Two *n-*good sequences $x_1, x_2, \dots, x_{n^2}$ and $y_1, y_2, \dots, y_{n^2}$ are called *similar* if there exists an integer $k$ such that $y_i = x_{i+k}$ for all $i = 1, 2, \dots, n^2$ (again taking the subscripts modulo $n^2$). Suppose that there exists a non-trivial permutation $\sigma$ of $\{1, 2, \dots, n\}$ and an *n-*good sequence $x_1, x_2, \dots, x_{n^2}$ which is similar to $\sigma(x_1), \sigma(x_2), \dots, \sigma(x_{n^2})$. Show that $n \equiv 2 \pmod{4}$.


## 2017 — Problem 6

**Record:** `vnm_2017_e0f625`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2017_e0f625.json.gz).

For a positive integer $n$, consider $a_1, a_2, \dots, a_{2n}$ as a permutation of the first $2n$ positive integers. A permutation is called "nice" if $a_i + a_{n+i} = 2n+1$, $i = 1, 2, 3, \dots, n$ and $a_i - a_{i+1}$ is not congruent to $a_j - a_{j+1}$ modulo $2n+1$ for all $1 \le i < j \le 2n$ (suppose that $a_{2n+1} = a_1$).

1. For $n = 6$, give an example of the nice permutation.
2. Prove that for all $n$, there always exist some nice permutation.


## 2018 — TSTST 1

**Record:** `usa_2018_1d04a5`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2018_1d04a5.json.gz).

As usual, let $\mathbb{Z}[x]$ denote the set of single-variable polynomials in $x$ with integer coefficients.
Find all functions $\theta : \mathbb{Z}[x] \to \mathbb{Z}$ such that for any polynomials $p, q \in \mathbb{Z}[x]$,
* $\theta(p + 1) = \theta(p) + 1$, and
* if $\theta(p) \neq 0$ then $\theta(p)$ divides $\theta(p \cdot q)$.


## 2018 — TSTST 8

**Record:** `usa_2018_46b003`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2018_46b003.json.gz).

For which positive integers $b > 2$ do there exist infinitely many positive integers $n$ such that $n^2$ divides $b^n + 1$?
This problem is sort of the union of IMO 1990/3 and IMO 2000/5.


## 2018 — TSTST 4

**Record:** `usa_2018_5b516b`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2018_5b516b.json.gz).

For an integer $n > 0$, denote by $\mathcal{F}(n)$ the set of integers $m > 0$ for which the polynomial $p(x) = x^2 + mx + n$ has an integer root.

a. Let $S$ denote the set of integers $n > 0$ for which $\mathcal{F}(n)$ contains two consecutive integers. Show that $S$ is infinite but
$$
\sum_{n \in S} \frac{1}{n} \le 1.
$$

b. Prove that there are infinitely many positive integers $n$ such that $\mathcal{F}(n)$ contains three consecutive integers.


## 2019 — TST 4

**Record:** `usa_2019_272f92`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2019_272f92.json.gz).

We say a function $f: \mathbb{Z}_{\ge 0} \times \mathbb{Z}_{\ge 0} \to \mathbb{Z}$ is *great* if for any nonnegative integers $m$ and $n$,
$$
f(m+1, n+1)f(m, n) - f(m+1, n)f(m, n+1) = 1.
$$
If $A = (a_0, a_1, \dots)$ and $B = (b_0, b_1, \dots)$ are two sequences of integers, we write $A \sim B$ if there exists a great function $f$ satisfying $f(n, 0) = a_n$ and $f(0, n) = b_n$ for every nonnegative integer $n$ (in particular, $a_0 = b_0$).
Prove that if $A, B, C$, and $D$ are four sequences of integers satisfying $A \sim B, B \sim C$, and $C \sim D$, then $D \sim A$.


## 2019 — TST 2

**Record:** `usa_2019_377e55`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2019_377e55.json.gz).

Let $\mathbb{Z}/n\mathbb{Z}$ denote the set of integers considered modulo $n$ (hence $\mathbb{Z}/n\mathbb{Z}$ has $n$ elements). Find all positive integers $n$ for which there exists a bijective function $g: \mathbb{Z}/n\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$, such that the 101 functions
$$
g(x),\ g(x) + x,\ g(x) + 2x,\ \dots,\ g(x) + 100x
$$
are all bijections on $\mathbb{Z}/n\mathbb{Z}$.


## 2019 — TSTST 7

**Record:** `usa_2019_412886`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2019_412886.json.gz).

Let $f: \mathbb{Z} \rightarrow \{1, 2, \dots, 10^{100}\}$ be a function satisfying
$$
\text{gcd}(f(x), f(y)) = \text{gcd}(f(x), x - y)
$$
for all integers $x$ and $y$. Show that there exist positive integers $m$ and $n$ such that $f(x) = \text{gcd}(m + x, n)$ for all integers $x$.


## 2019 — TSTST 6

**Record:** `usa_2019_c48ff2`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2019_c48ff2.json.gz).

Suppose $P$ is a polynomial with integer coefficients such that for every positive integer $n$, the sum of the decimal digits of $|P(n)|$ is not a Fibonacci number. Must $P$ be constant?
(A *Fibonacci number* is an element of the sequence $F_0, F_1, \dots$ defined recursively by $F_0 = 0$, $F_1 = 1$, and $F_{k+2} = F_{k+1} + F_k$ for $k \ge 0$.)


## 2020 — TSTST 8

**Record:** `usa_2020_391adb`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2020_391adb.json.gz).

For every positive integer $N$, let $\sigma(N)$ denote the sum of the positive integer divisors of $N$. Find all integers $m \ge n \ge 2$ satisfying
$$
\frac{\sigma(m) - 1}{m - 1} = \frac{\sigma(n) - 1}{n - 1} = \frac{\sigma(mn) - 1}{mn - 1}.
$$


## 2020 — TSTST 3

**Record:** `usa_2020_992de5`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2020_992de5.json.gz).

We say a nondegenerate triangle whose angles have measures $\theta_1, \theta_2, \theta_3$ is *quirky* if there exists integers $r_1, r_2, r_3$, not all zero, such that
$$
r_1\theta_1 + r_2\theta_2 + r_3\theta_3 = 0.
$$
Find all integers $n \ge 3$ for which a triangle with side lengths $n-1, n, n+1$ is quirky.


## 2020 — TSTST 4

**Record:** `usa_2020_c1b077`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2020_c1b077.json.gz).

Find all pairs of positive integers $(a, b)$ satisfying the following conditions:
(i) $a$ divides $b^4 + 1$,
(ii) $b$ divides $a^4 + 1$,
(iii) $\lfloor\sqrt{a}\rfloor = \lfloor\sqrt{b}\rfloor$.


## 2021 — TST 1

**Record:** `usa_2021_c4710d`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2021_c4710d.json.gz).

Determine all integers $s \ge 4$ for which there exist positive integers $a, b, c, d$ such that $s = a+b+c+d$ and $s$ divides $abc + abd + acd + bcd$.


## 2021 — Problem 6.

**Record:** `vnm_2021_ecd237`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2021_ecd237.json.gz).

Let $n \ge 3$ be a positive integer and $p$ be a prime number such that $p > 6^{n-1} - 2^n + 1$. Let $S$ be the set of $n$ positive integers with different residues modulo $p$. Show that there exists a positive integer $c$ such that there are exactly two ordered triples $(x, y, z) \in S^3$ with distinct elements, such that $x - y + z - c$ is divisible by $p$.


## 2022 — 5

**Record:** `chn_2022_5a13de`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_5a13de.json.gz).

Given a positive integer $n$, let $D$ be the set of positive divisors of $n$, and let $f: D \to \mathbb{Z}$ be a function. Prove that the following are equivalent:
(A) for any positive divisor $m$ of $n$,
$$
n \mid \sum_{d|m} f(d) \binom{n/d}{m/d};
$$
(B) for any positive divisor $k$ of $n$,
$$
k \mid \sum_{d|k} f(d).
$$


## 2022 — 5

**Record:** `chn_2022_78f104`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_78f104.json.gz).

Prove that there exist two positive real numbers $C$ and $\alpha > \frac{1}{2}$, such that, for any positive integer $n$, there is a subset $A$ of $\{1, 2, \dots, n\}$ with $|A| \ge Cn^\alpha$, such that the difference between any pair of different numbers in $A$ is not a perfect square.


## 2022 — 3

**Record:** `chn_2022_bec0c9`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_bec0c9.json.gz).

Let $a_1, a_2, \dots, a_n$ be $n$ positive integers that are not divisible one another, i.e. for any $i \neq j$, $a_i$ is not divisible by $a_j$. Show that
$$
a_1 + a_2 + \dots + a_n \geq 1.1n^2 - 2n.
$$


## 2022 — 3

**Record:** `chn_2022_f17616`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_f17616.json.gz).

Fix an integer $n \ge 2$. Find all $n$-tuples $(a_1, a_2, \dots, a_n)$ of integers satisfying the following two conditions:
(1) $a_1$ is odd, $1 < a_1 \le a_2 \le \dots \le a_n$, and $M = \frac{1}{2^n}(a_1 - 1)a_2 \dots a_n$ is an integer; and
(2) there exist $M$ different $n$-tuples $(c_{i,1}, c_{i,2}, \dots, c_{i,n})$ with $i = 1, 2, \dots, M$, such that for all $1 \le i < j \le M$, there exists $k \in \{1, 2, \dots, n\}$ such that
$$
c_{i,k} - c_{j,k} \not\equiv -1, 0, 1 \pmod{a_k}.
$$


## 2022 — Problem 5

**Record:** `vnm_2022_841202`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2022_841202.json.gz).

A fractional number $x$ is called ‘pretty’ if it has finite expression in base $b$ numeral system where $b$ is a positive integer in $[2; 2022]$. Prove that there exists finite positive integers $n \ge 4$ such that with every $m$ in $\left(\frac{2n}{3}, n\right)$, there is at least one pretty number among two numbers $\frac{m}{n-m}$ and $\frac{n-m}{m}$.


## 2023 — 1

**Record:** `chn_2023_321a77`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_321a77.json.gz).

Given an integer $n > 1$ and an integer $a$ that is coprime with $n$. There is a country consisting of $n$ islands $D_1, D_2, \dots, D_n$. For any two different islands $D_i$ and $D_j$, there is a one-way ferry from $D_i$ to $D_j$ if and only if $ij \equiv ia \pmod{n}$. A tourist hopes to visit as many islands as possible. He can first fly to any island he chooses to start the tour, and afterwards can only use the one-way ferry to tour freely between islands in this country. Find the maximum possible number of different islands that the tourist can visit.


## 2023 — 3

**Record:** `chn_2023_4ceef1`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_4ceef1.json.gz).

(1) Given coprime positive integers $a, b$. Prove: There exist real numbers $\lambda, \beta$ such that for any positive integer $m$, it holds that
$$
\lambda m - \beta \le \sum_{k=1}^{m-1} \left\{ \frac{ak}{m} \right\} \cdot \left\{ \frac{bk}{m} \right\} \le \lambda m + \beta.
$$

(2) Prove: there exists a positive integer $N$, such that for any prime $p > N$, the following proposition holds:
If the positive integers $a, b, c$ satisfy that $(a+b)(a+c)(b+c)$ is not divisible by $p$, then there exist at least $\lfloor \frac{p}{12} \rfloor$ elements $k$ in the set $\{1, 2, \dots, p-1\}$ such that
$$
\left\{ \frac{ak}{p} \right\} + \left\{ \frac{bk}{p} \right\} + \left\{ \frac{ck}{p} \right\} \le 1.
$$
Here, $\lfloor x \rfloor$ represents the greatest integer not exceeding $x$, and $\{x\} = x - \lfloor x \rfloor$ represents the fractional part of $x$.


## 2023 — 4

**Record:** `chn_2023_68131c`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_68131c.json.gz).

For positive integers $m, n$, define
$$
S(m, n) = \{(a, b) \in \mathbb{Z}^2 \mid 1 \le a \le m, 1 \le b \le n, \gcd(a, b) = 1\}.
$$
Prove: for any positive integers $d, r$, there exist integers $m, n$ not less than $d$, such that $|S(m, n)| \equiv r \pmod{d}$. Here, $|A|$ represents the number of elements in the finite set $A$.


## 2023 — 2

**Record:** `ind_2023_438140`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2023_438140.json.gz).

Let $g: \mathbb{N} \to \mathbb{N}$ be a bijective function and suppose that $f: \mathbb{N} \to \mathbb{N}$ is a function such that:
• For all naturals $x$, $f^{2023}(x) = x$
• For all naturals $x, y$ such that $x \mid y$, we have $f(x) \mid g(y)$.
Prove that $f(x) = x$.


## 2023 — USA TST 2023/5

**Record:** `usa_2023_9d8847`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2023_9d8847.json.gz).

Let $m$ and $n$ be fixed positive integers. Tsvety and Freyja play a game on an infinite grid of unit square cells. Tsvety has secretly written a real number inside of each cell so that the sum of the numbers within every rectangle of size either $m \times n$ or $n \times m$ is zero. Freyja wants to learn all of these numbers.

One by one, Freyja asks Tsvety about some cell in the grid, and Tsvety truthfully reveals what number is written in it. Freyja wins if, at any point, Freyja can simultaneously deduce the number written in every cell of the entire infinite grid. (If this never occurs, Freyja has lost the game and Tsvety wins.)

In terms of $m$ and $n$, find the smallest number of questions that Freyja must ask to win, or show that no finite number of questions can suffice.


## 2023 — 9

**Record:** `usa_2023_cb6858`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2023_cb6858.json.gz).

Let $p$ be a fixed prime and let $a \ge 2$ and $e \ge 1$ be fixed integers. Given a function $f: \mathbb{Z}/a\mathbb{Z} \to \mathbb{Z}/p^e\mathbb{Z}$ and an integer $k \ge 0$, the $k$th finite difference, denoted $\Delta^k f$, is the function from $\mathbb{Z}/a\mathbb{Z}$ to $\mathbb{Z}/p^e\mathbb{Z}$ defined recursively by
$$
\begin{aligned}
\Delta^0 f(n) &= f(n) \\
\Delta^k f(n) &= \Delta^{k-1} f(n+1) - \Delta^{k-1} f(n) \quad \text{for } k = 1, 2, \dots
\end{aligned}
$$
Determine the number of functions $f$ such that there exists some $k \ge 1$ for which $\Delta^k f = f$.


## 2023 — 4

**Record:** `vnm_2023_77dbf4`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2023_77dbf4.json.gz).

Given are two coprime positive integers $a, b$ with $b$ odd and $a > 2$. The sequence $(x_n)$ is defined by $x_0 = 2$, $x_1 = a$ and $x_{n+2} = a x_{n+1} + b x_n$ for $n \ge 1$. Prove that

a) If $a$ is even then there do not exist positive integers $m, n, p$ such that $\frac{x_m}{x_n x_p}$ is a positive integer.

b) If $a$ is odd then there do not exist positive integers $m, n, p$ such that $mnp$ is even and $\frac{x_m}{x_n x_p}$ is a perfect square.


## 2024 — 4

**Record:** `chn_2024_7ed496`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2024_7ed496.json.gz).

Let $m > 1$ be an integer. It is known that there exists a prime number in the interval $[2m - \sqrt{m} + 1, 2m]$. Prove that among any $m$ pairwise distinct positive integers $a_1, a_2, \dots, a_m$, there exist two numbers $a_i$ and $a_j$ ($1 \le i, j \le m$) such that
$$
\frac{a_i}{(a_i, a_j)} \ge m,
$$
where $(a_i, a_j)$ denotes the greatest common divisor of the positive integers $a_i$ and $a_j$.


## 2024 — 2.

**Record:** `ind_2024_0dddaf`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2024_0dddaf.json.gz).

* $a^{2n} - a$ is divisible by $n$,
* $\sum_{k=1}^{n} k^{2024} a^{2k}$ is not divisible by $n$.
Prove that $n$ has a prime factor *smaller* than $2024$.


## 2024 — 1.

**Record:** `ind_2024_8f9865`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2024_8f9865.json.gz).

Let $n$ be a positive integer. Let $s: \mathbb{N} \to \{1, \dots, n\}$ be a function such that $n$ divides $m - s(m)$ for all positive integers $m$. Let $a_0, a_1, a_2, \dots$ be a sequence such that $a_0 = 0$ and
$$
a_k = a_{k-1} + s(k) \text{ for all } k \ge 1.
$$
Find all $n$ for which this sequence contains all the residues modulo $(n+1)^2$.


## 2024 — 3

**Record:** `ind_2024_be9bfd`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2024_be9bfd.json.gz).

Let $P(x) \in \mathbb{Q}[x]$ be a polynomial with rational coefficients and degree $d \ge 2$. Prove there is no infinite sequence $a_0, a_1, \dots$ of rational numbers such that $P(a_i) = a_{i-1} + i$ for all $i \ge 1$.


## 2024 — 2.

**Record:** `ind_2024_d0a341`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2024_d0a341.json.gz).

There are $n \ge 3$ particles on a circle situated at the vertices of a regular $n$-gon. All these particles move on the circle with the same constant speed. One of the particles moves in the clockwise direction while all others move in the anti-clockwise direction. When particles collide, that is, they are all at the same point, they all reverse the direction of their motion and continue with the same speed as before.
Let $s$ be the smallest number of collisions after which all particles return to their original positions. Find $s$.


## 2025 — Problem 1.

**Record:** `chn_2025_2bb7dd`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_2bb7dd.json.gz).

Find all positive integers $m$ such that there exists an infinite set $A$ of positive integers satisfying: for any $m$ distinct elements $a_1, a_2, \dots, a_m$ in $A$, both $a_1+a_2+\dots+a_m$ and $a_1a_2\cdots a_m$ are square-free.

*Note: A positive integer $n$ is called square-free if it is not divisible by the square of any prime number.*


## 2025 — Problem 8.

**Record:** `chn_2025_d307ea`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_d307ea.json.gz).

Given an odd positive integer $n$, let $m = \frac{n+1}{2}$. Let positive integers $a_1, a_2, \dots, a_m$ be pairwise incongruent modulo $n$, and positive integers $b_1, b_2, \dots, b_m$ be pairwise incongruent modulo $n$. Prove that the set
$$
C = \{a_i + b_j \text{ (least nonnegative residue modulo } n) \mid i, j \in \{1, 2, \dots, m\}, i \neq j\}
$$
has more than $n - \sqrt{n} - \frac{1}{2}$ elements.


## 2025 — Problem 12.

**Record:** `chn_2025_e6abc2`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_e6abc2.json.gz).

Find all functions $f : \mathbb{Z} \to \mathbb{Z}$ satisfying:
(1) For any positive integer $M$, there exists an integer $k$ with $|f(k)| \ge M$;
(2) For any integers $m, n$,
$$2f(m)f(n) - f(m - n) - 1$$ is a perfect square.


## 2025 — Problem 7.

**Record:** `chn_2025_f857cf`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_f857cf.json.gz).

Given integer sequences $\{x_n\}_{n \ge 1}$, $\{y_n\}_{n \ge 1}$. Prove that there exists an integer sequence $\{z_n\}_{n \ge 1}$ such that for any positive integer $n$,
$$
\sum_{k|n} k z_k^{n/k} = \left( \sum_{k|n} k x_k^{n/k} \right) \cdot \left( \sum_{k|n} k y_k^{n/k} \right).
$$
Here all three sums are taken over all positive divisors $k$ of $n$. For example, when $n = 6$:
$$
6z_6 + 3z_3^2 + 2z_2^3 + z_1^6 = (6x_6 + 3x_3^2 + 2x_2^3 + x_1^6) \cdot (6y_6 + 3y_3^2 + 2y_2^3 + y_1^6).
$$


## 2025 — Problem 8

**Record:** `usa_2025_24dab7`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_24dab7.json.gz).

Find all polynomials $f$ with integer coefficients such that for all positive integers $n$, $n$ divides $\underbrace{f(f(\dots(f(0))\dots))}_{n+1 \text{ f's}} -1$.


## 2025 — Problem 4

**Record:** `usa_2025_508602`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_508602.json.gz).

Let $n \ge 2$ be a positive integer. Let $a_1, a_2, \dots, a_n$ be a sequence of positive integers such that
$$
\gcd(a_1, a_2), \gcd(a_2, a_3), \dots, \gcd(a_{n-1}, a_n)
$$
is a strictly increasing sequence. Find, in terms of $n$, the maximum possible value of
$$
\frac{1}{a_1} + \frac{1}{a_2} + \dots + \frac{1}{a_n}.
$$
over all such sequences.


## 2025 — 6

**Record:** `usa_2025_abaaab`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_abaaab.json.gz).

Prove that there exists a real number $\varepsilon > 0$ such that there are infinitely many sequences of integers $0 < a_1 < a_2 < \dots < a_{2025}$ satisfying
$$
\text{gcd}(a_1^2 + 1, a_2^2 + 1, \dots, a_{2025}^2 + 1) > a_{2025}^{1+\varepsilon}.
$$


## 2025 — Problem 3

**Record:** `usa_2025_b0a732`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_b0a732.json.gz).

Let $a_1$, $a_2$, $r$, and $s$ be positive integers with $r$ and $s$ odd. The sequence $a_1$, $a_2$, $a_3$, $\dots$ is defined by
$$
a_{n+2} = r a_{n+1} + s a_n
$$
for all $n \ge 1$. Determine the maximum possible number of integers $1 \le l \le 2025$ such that $a_l$ divides $a_{l+1}$, over all possible choices of $a_1$, $a_2$, $r$, and $s$.


## 2025 — 1

**Record:** `usa_2025_c87ac0`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_c87ac0.json.gz).

Let $n$ be a positive integer. Ana and Banana play a game. Banana thinks of a function $f: \mathbb{Z} \to \mathbb{Z}$ and a prime number $p$. He tells Ana that $f$ is nonconstant, $p < 100$, and $f(x+p) = f(x)$ for all integers $x$. Ana's goal is to determine the value of $p$. She writes down $n$ integers $x_1, \dots, x_n$. After seeing this list, Banana writes down $f(x_1), \dots, f(x_n)$ in order. Ana wins if she can determine the value of $p$ from this information. Find the smallest value of $n$ for which Ana has a winning strategy.


## 2025 — TST 1

**Record:** `usa_2025_d1cd24`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_d1cd24.json.gz).

Let $n$ be a positive integer. Ana and Banana play a game. Banana thinks of a function $f: \mathbb{Z} \to \mathbb{Z}$ and a prime number $p$. He tells Ana that $f$ is nonconstant, $p < 100$, and $f(x+p) = f(x)$ for all integers $x$. Ana's goal is to determine the value of $p$. She writes down $n$ integers $x_1, \dots, x_n$. After seeing this list, Banana writes down $f(x_1), \dots, f(x_n)$ in order. Ana wins if she can determine the value of $p$ from this information. Find the smallest value of $n$ for which Ana has a winning strategy.


## 2025 — 5

**Record:** `usa_2025_e105bb`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_e105bb.json.gz).

A pond has $2025$ lily pads arranged in a circle. Two frogs, Alice and Bob, begin on different lily pads. A frog jump is a jump which travels $2$, $3$, or $5$ positions clockwise. Alice and Bob each make a series of frog jumps, and each frog ends on the same lily pad that it started from. Given that each lily pad is the destination of exactly one jump, prove that each frog completes exactly two laps around the pond (i.e. travels $4050$ positions in total).



# IMOTC source statements

## 2023 — Problem 3

**Record:** `ind_2023_092f9b`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2023_092f9b.json.gz).

Prove that for all integers $k > 2$, there exists $k$ distinct positive integers $a_1, \dots, a_k$ such that
$$
\sum_{1 \le i < j \le k} \frac{1}{a_i a_j} = 1.
$$


## 2023 — Problem 2

**Record:** `ind_2023_2c3746`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2023_2c3746.json.gz).

Let $S(k)$ denote the sum of digits (in base 10) of any positive integer $k$. Does there exist a positive integer $N$ so that $S(2^n) \le S(2^{n+1})$ for all integers $n > N$?


## 2023 — Problem 1

**Record:** `ind_2023_407ed2`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2023_407ed2.json.gz).

The numbers $1$, $2$, $3$, $4$, $\ldots$, $39$ are written on a blackboard. In one step we are allowed to choose two numbers $a$ and $b$ on the blackboard such that $a$ divides $b$, and replace $a$ and $b$ by the single number $\frac{b}{a}$. This process is continued till no number on the board divides any other number. Let $S$ be the set of numbers which is left on the board at the end. What is the smallest possible value of $|S|$?


## 2023 — Problem 3

**Record:** `ind_2023_d9a3be`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2023_d9a3be.json.gz).

Let $n$ be any positive integer, and let $S(n)$ denote the number of permutations $\tau$ of $\{1, \dots, n\}$ such that $k^4 + (\tau(k))^4$ is prime for all $k = 1, \dots, n$. Show that $S(n)$ is always a square.



# IranMO source statements

## 2015 — 4

**Record:** `irn_2015_4e48b5`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/iran/irn_2015_4e48b5.json.gz).

Let $n$ be a natural number. Determine the smallest natural number $k$ such that among any $k$ natural numbers, it is always possible to select an even number of them having a sum divisible by $n$.


## 2015 — 3

**Record:** `irn_2015_6b4790`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/iran/irn_2015_6b4790.json.gz).

a) Consider $n$ coprime natural numbers greater than $1$ like $d_1, d_2, \dots, d_n$ and arbitrary natural numbers $r_1, r_2, \dots, r_n$. Prove that there exists a natural number $x$, $1 \le x \le 3^n$, that satisfies the following system of modular inequalities:
$$
\begin{array}{l}
x \not\equiv r_1 \pmod{d_1} \\
x \not\equiv r_2 \pmod{d_2} \\
\vdots \\
x \not\equiv r_n \pmod{d_n}
\end{array}
$$

b) For each real number $\epsilon > 0$, prove that there exists a number $N$ such that for each natural number $n > N$ and natural numbers $d_1, d_2, \dots, d_n$ and $r_1, r_2, \dots, r_n$, where $d_i$'s ($1 \le i \le n$) are coprime, the above system of inequalities has a solution $x$ that $1 \le x \le (2 + \epsilon)^n$.


## 2015 — 11

**Record:** `irn_2015_c7ea96`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/iran/irn_2015_c7ea96.json.gz).

Permutation $(a_1, a_2, \dots, a_n)$ of the set $\{1, 2, \dots, n\}$ is called **messy** if for any three indices $1 \le i < j < k \le n$, $a_i + a_k - 2a_j$ is not divisible by $n$. Find all natural numbers $n \ge 3$ for which there exists a messy permutation of the set $\{1, 2, \dots, n\}$.



# JMO source statements

## 2006 — 2

**Record:** `jpn_2006_966084`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2006_966084.json.gz).

Find every integer $k$ that satisfies the following condition.
There are infinitely many triplet $(a, b, c)$ of integers such that $(a^2 - k)(b^2 - k) = c^2 - k$.


## 2006 — 8

**Record:** `jpn_2006_a53c60`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2006_a53c60.json.gz).

Tomohiro and Akinori read mathematical books as follows. Akinori reads 2 pages a day. Tomohiro reads 3 pages a day. However, each of the two stop reading of that day if he reaches the end of a chapter.

There is a mathematical book which consists of 10 chapters and 120 pages. Find the smallest value of the difference between the number of days in which Akinori reads the book and that of Tomohiro. A new chapter always begins with a new page.


## 2006 — 7

**Record:** `jpn_2006_b8b23e`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2006_b8b23e.json.gz).

$x$, $y$ and $z$ are distinct 2-digit positive integers. The first digit of $x$ is equal to the second digit of $y$, the first digit of $y$ is equal to the second digit of $z$, and the first digit of $z$ is equal to the second digit of $x$. How many positive integers can be the greatest common divisor of $x$, $y$ and $z$?


## 2006 — 4

**Record:** `jpn_2006_e5e5b8`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2006_e5e5b8.json.gz).

Find three distinct positive integers which minimize their sum under the condition that any two of them add up to a perfect square.


## 2007 — 9

**Record:** `jpn_2007_529992`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_529992.json.gz).

How many pairs of integers $(a, b)$ satisfy $a^2 b^2 = 4a^5 + b^3$?


## 2007 — 1

**Record:** `jpn_2007_6677e6`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_6677e6.json.gz).

Let $n$ be a positive integer. Two people $P$, $Q$ play a game in which they call an integer $m$ ($1 \le m \le n$) alternately. $P$ calls the first number. They cannot call the numbers which are already called by themselves or by their opponent. The game is over when neither can call numbers. If the sum of the numbers that $A$ has called is divisible by $3$, $P$ wins, otherwise $Q$ wins. Find all $n$ which satisfy the condition below.

Condition: $P$ can win the game whatever $Q$ does.


## 2007 — 2

**Record:** `jpn_2007_6b2668`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_6b2668.json.gz).

Determine ten's place of $11^{12^{13}}$. ($12^{13}$th power of $11$, not $13$th power of $11^{12}$.)


## 2007 — 10

**Record:** `jpn_2007_a14cf1`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_a14cf1.json.gz).

There are some cards with positive integers on them, and the sum of these integers is $2007$. For any integer $1 \le k \le 2006$ we can choose some cards so that the sum of the numbers written on those cards is $k$, and there is only one way (if cards with same number are considered to be the same) to do so for each $k$. How many kinds of such a set of cards are possible?


## 2007 — 11

**Record:** `jpn_2007_b2e5f1`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_b2e5f1.json.gz).

In a mathematical competition, gold medals are given to $\lfloor \frac{n}{a} \rfloor$ people, silver medals to $\lfloor \frac{n}{b} \rfloor$ and bronze medals to $\lfloor \frac{n}{c} \rfloor$ ($a \ge b \ge c$ are integer constants and $n$ is the number of participants). No one gets two or more medals. Determine all triplets $(a, b, c)$ with the following property.

Property: For all integer $k \ge 3$, there are exactly two $n$ such that the number of people without medals are $k$.

* $[r]$ is the maximum integer that does not exceed $r$.


## 2007 — 1

**Record:** `jpn_2007_c7dc24`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_c7dc24.json.gz).

Let $n$ be a positive integer. Two people $P$, $Q$ play a game in which they call an integer $m$ ($1 \le m \le n$) alternately. $P$ calls the first number. They cannot call the numbers which are already called by themselves or by their opponent. The game is over when neither can call numbers. If the sum of the numbers that $A$ has called is divisible by $3$, $P$ wins, otherwise $Q$ wins. Find all $n$ which satisfy the condition below.
Condition: $P$ can win the game whatever $Q$ does.


## 2007 — 3

**Record:** `jpn_2007_d628f6`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_d628f6.json.gz).

Find all positive integer pairs $(m, n)$ that satisfy the following conditions.
$$
(1)\ m, n \leq 20
$$
(2) $m$ and $n$ are relatively prime.
$$
(3) \quad \frac{5}{7} < \frac{m}{n} < \frac{3}{4}
$$


## 2007 — 4

**Record:** `jpn_2007_da6e7a`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_da6e7a.json.gz).

$n$ is a 4-digit integer with ten's place nonzero, and if we take the first 2 digits and the last 2 digits as two 2-digit integers, their product is a divisor of $n$. Determine all $n$ with this property.


## 2008 — 7

**Record:** `jpn_2008_0160ba`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2008_0160ba.json.gz).

How many 3-digit numbers are there that can appear as the top three digits of a 6-digit number, which is a perfect square?


## 2008 — 4

**Record:** `jpn_2008_8c7570`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2008_8c7570.json.gz).

Suppose a positive integer has the property that the sum of the remainders when its factors are divided by $4$ equals $1000$. Determine all positive integers having this property.


## 2008 — 1

**Record:** `jpn_2008_a13f3b`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2008_a13f3b.json.gz).

A polynomial $P(x)$ with integer coefficients satisfies $P(n^2) = 0$ for some nonzero integer $n$. Show that $P(a^2) \neq 1$ must hold for any nonzero rational number $a$.


## 2008 — 6

**Record:** `jpn_2008_a26a53`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2008_a26a53.json.gz).

Suppose we denote by $n_{(10)}$ the decimal representation for a positive integer $n$. Suppose three distinct positive integers $a, b, c$ satisfy all of the following conditions:
* $c_{(10)}$ coincides with the number obtained by removing a 6 from $a_{(10)}$.
* $c_{(10)}$ coincides with the number obtained by removing a 6 from $b_{(10)}$.
* The number of digits for $a$ coincides with the number of digits for $b$, and $a$ is a multiple of $b$.
Determine the smallest possible value that $c$ can have satisfying these conditions.


## 2008 — 5

**Record:** `jpn_2008_ac9925`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2008_ac9925.json.gz).

Does there exist a positive integer $n$ satisfying the following condition?

Condition: For an arbitrary rational number $r$, there exist an integer $b$ and nonzero integers $a_1, a_2, \dots, a_n$ such that
$$
r = b + \frac{1}{a_1} + \dots + \frac{1}{a_n}
$$


## 2008 — 1

**Record:** `jpn_2008_f1202b`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2008_f1202b.json.gz).

Determine the maximum possible value for the least common multiple of 4 distinct single digit positive integers.


## 2009 — 3

**Record:** `jpn_2009_222056`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2009_222056.json.gz).

Let $k$ be an integer greater than or equal to $2$, and let $n_1$, $n_2$, $n_3$ be positive integers, and $a_1$, $a_2$, $a_3$ be integers greater than or equal to $1$ and less than or equal to $k-1$. Define
$$
b_i = a_i \sum_{j=0}^{n_i} k^j \quad (i = 1, 2, 3).
$$
Determine all possible combinations $(n_1, n_2, n_3)$ if $b_1 b_2 = b_3$.


## 2009 — 3

**Record:** `jpn_2009_8f1a5c`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2009_8f1a5c.json.gz).

Determine all the triples $(a, b, c)$ of positive integers which satisfy the following 2 identities. Distinguish two triples which are obtained by permuting the order of the same set of three numbers.
$$
ab + c = 13, \quad a + bc = 23.
$$


## 2009 — 1

**Record:** `jpn_2009_be6d0b`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2009_be6d0b.json.gz).

Determine all positive integers $n$ for which $8^n + n$ is divisible by $2^n + n$.


## 2010 — 10

**Record:** `jpn_2010_2a8898`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2010_2a8898.json.gz).

For a positive integer $n$, denote by $S(n)$ the sum of the digits of $n$. If $S(n) = 5$, what is the maximum possible value that $S(n^5)$ can take?


## 2010 — 2

**Record:** `jpn_2010_3b3a8d`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2010_3b3a8d.json.gz).

Let $k$ be a positive integer and $m$ an odd integer. Show that there exists a positive integer $n$ for which the number $n^n - m$ is divisible by $2^k$.


## 2010 — 7

**Record:** `jpn_2010_3f9b46`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2010_3f9b46.json.gz).

Consider an infinite sequence $a_1, a_2, a_3, \dots$ of positive integers. Suppose that the following 2 conditions are satisfied for an arbitrary positive integer $n$:
* $a_n$ is a multiple of $n$.
* $|a_n - a_{n+1}| \le 5$.
Find the maximum possible value that $a_1$ can take.


## 2012 — 9

**Record:** `jpn_2012_2146b7`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2012_2146b7.json.gz).

Players $A$ and $B$ wrote down two positive integers each on a black board. The product of the two numbers $A$ wrote is twice the sum of the two numbers $B$ wrote, and the product of the two numbers $B$ wrote is twice the sum of the two numbers $A$ wrote, and furthermore, the sum of the two numbers $A$ wrote is greater than or equal to the sum of the two numbers $B$ wrote. Determine all possible values for the sum of the two numbers $B$ wrote. Note that four numbers written down need not be distinct.


## 2012 — 4

**Record:** `jpn_2012_654103`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2012_654103.json.gz).

Let $A$ be a positive integer which is a multiple of $3$ but not of $9$. When we add to $A$ the product of all the digits of $A$, then we obtain a number which is a multiple of $9$. Find the smallest possible value for such a number $A$.


## 2012 — 5

**Record:** `jpn_2012_993c1a`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2012_993c1a.json.gz).

Let $k$ be a positive integer. Players $A$ and $B$ play a game according to the following rule: Initially, a chess piece is placed at the origin $(0, 0)$ of the $xy$-plane. The player $A$ will start the game followed by $B$ and repeat, each choosing a strategy among those specified by the following rules:
* Possible strategies for $A$: Choose a lattice point, which is not occupied by the chess piece and mark the point by a $\checkmark$.
(Here, by a lattice point we mean a point in the $xy$-plane whose $x$-coordinate and $y$-coordinate are both integers).
* Possible strategies for $B$: Repeat the process of moving the chess piece located at $(x, y)$ to either $(x+1, y)$ or $(x, y+1)$ $j$ times where $1 \le j \le k$. However, in each move of the process he is not allowed to move the chess piece into a lattice point marked by a $\checkmark$.
$A$ wins the game if $B$ gets into the situation where he cannot move the chess piece. Determine all possible values for $k$ for which $A$ can win the game after a finite number of steps no matter how $B$ chooses his strategies.


## 2012 — 3

**Record:** `jpn_2012_9e123c`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2012_9e123c.json.gz).

Let $p$ be a prime. Determine all positive integers $n$ for which the following condition is satisfied for all the integers $x$:
Condition: If $x^n - 1$ is divisible by $p$, then it is also divisible by $p^2$.


## 2012 — 5

**Record:** `jpn_2012_f00e16`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2012_f00e16.json.gz).

Determine all the positive integers $n$ for which the product of all positive factors equals $24^{240}$.


## 2013 — 1

**Record:** `jpn_2013_005966`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_005966.json.gz).

Suppose the least common multiple of three positive integers $x$, $y$, $z$ is $2100$. What is the minimum possible value that the sum $x + y + z$ can take?


## 2013 — 2

**Record:** `jpn_2013_1d4231`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_1d4231.json.gz).

Suppose two $20 \times 13$ rectangular grids consisting of $260$ small squares are given.
We insert into each square box of the two grids, numbers $1, 2, \ldots, 260$ in the following way:

* For the first grid, we start inserting numbers $1, 2, \ldots, 13$ into the boxes on the top row from left to right. Continue to insert numbers $14, 15, \ldots, 26$ into the boxes on the second row from left to right. Keep on going until you finish inserting numbers $248, 249, \ldots, 260$ from left to right into the boxes on the bottom row.

* For the second grid, we start inserting numbers $1, 2, \ldots, 20$ into the boxes on the right-most column from top to bottom. Continue to insert numbers $21, 22, \ldots, 40$ into the boxes on the second column from the right from top to bottom. Keep on doing until you finish inserting numbers $241, 242, \ldots, 260$ into the boxes on the left most column from top to bottom.

List all the positive integers which get inserted into the boxes located in the same position in the two grids in the two ways of distributing numbers described above.


## 2013 — 9

**Record:** `jpn_2013_35ed0b`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_35ed0b.json.gz).

Find all the factors $k$ of $10^{2013} - 1$, which satisfy $1 \le k \le 100$.


## 2013 — 2

**Record:** `jpn_2013_60648c`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_60648c.json.gz).

Suppose two $20 \times 13$ rectangular grids consisting of $260$ small squares are given. We insert into each square box of the two grids, numbers $1, 2, \ldots, 260$ in the following way:
* For the first grid, we start inserting numbers $1, 2, \ldots, 13$ into the boxes on the top row from left to right. Continue to insert numbers $14, 15, \ldots, 26$ into the boxes on the second row from left to right. Keep on going until you finish inserting numbers $248, 249, \ldots, 260$ from left to right into the boxes on the bottom row.
* For the second grid, we start inserting numbers $1, 2, \ldots, 20$ into the boxes on the right-most column from top to bottom. Continue to insert numbers $21, 22, \ldots, 40$ into the boxes on the second column from the right from top to bottom. Keep on doing until you finish inserting numbers $241, 242, \ldots, 260$ into the boxes on the left most column from top to bottom.

List all the positive integers which get inserted into the boxes located in the same position in the two grids in the two ways of distributing numbers described above.


## 2013 — 3

**Record:** `jpn_2013_6c42b8`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_6c42b8.json.gz).

Let $n$ be an integer greater than or equal to $2$. Find the smallest positive integer $m$ for which there exists a sequence $a_1, a_2, \dots, a_n$ of positive integers satisfying the following two conditions:
* $a_1 < a_2 < \dots < a_n = m$.
* All of the $n-1$ numbers $\frac{a_1^2 + a_2^2}{2}, \dots, \frac{a_{n-1}^2 + a_n^2}{2}$ are perfect squares.


## 2013 — 10

**Record:** `jpn_2013_798f65`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_798f65.json.gz).

There are 2013 cards numbered $0$, $1$, $2$, $\ldots$, $2012$. Initially, all the cards are placed with the face with a written number down. Then, we perform for each $i = 1, 2, \dots, 2013$ the following operation $i$ starting with $i = 1$ and with increasing order ending up with $i = 2013$:

Operation $i$: Flip each of the $i$ cards having the number $\left\lfloor \frac{2013j}{i} \right\rfloor$ for $j = 0, 1, \dots, i - 1$.

How many cards are with their faces up (showing their numbers) at the end of all the operations?

Here we denote by $[r]$ for each real number $r$ the greatest integer less than or equal to $r$.


## 2013 — 1

**Record:** `jpn_2013_7e2d7c`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_7e2d7c.json.gz).

Suppose the least common multiple of three positive integers $x$, $y$, $z$ is $2100$.
What is the minimum possible value that the sum $x + y + z$ can take?


## 2014 — 8

**Record:** `jpn_2014_1d9af9`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2014_1d9af9.json.gz).

Let $m$ be a positive integer of $1000$ digits, with the property that all of its digits are non-zero. For a positive integer $n$, consider $\left\lfloor \frac{m}{n} \right\rfloor$, where we define for any real number $r$, $\lfloor r \rfloor$ to be the largest integer less than or equal to $r$. Determine the largest possible number of digits which are $0$ for $\left\lfloor \frac{m}{n} \right\rfloor$, where $1 \le n \le m$.


## 2014 — 6

**Record:** `jpn_2014_74269a`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2014_74269a.json.gz).

There are two blackboards $A$ and $B$, and on each of these blackboards certain number of distinct integers greater than or equal to $2$ and less than or equal to $20$ are written in such a way that any pair of numbers one of which is chosen from $A$ and the other from $B$ are relatively prime. Determine the maximum possible value the product of the number of integers written on $A$ and the number of integers written on $B$ can take.


## 2014 — 2

**Record:** `jpn_2014_8f91d2`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2014_8f91d2.json.gz).

Suppose we assign one of positive integers $n$ satisfying $1 \le n \le 8$ to each of the 8 vertices of a regular octagon. How many ways of assigning these numbers are there, which satisfy the following 2 conditions?:
* assigned numbers are all distinct.
* any pair of numbers assigned to adjacent vertices are relatively prime.
Regard two assignments of 8 numbers to be distinct if one is obtained from the other by rotation or flipping of the octagon.


## 2014 — 3

**Record:** `jpn_2014_eeb196`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2014_eeb196.json.gz).

Find the value of
$$
\sum \frac{1}{d + \sqrt{10!}}
$$
where the sum is taken over all the positive factors $d$ of the number $10!$.


## 2015 — 5

**Record:** `jpn_2015_2c74e3`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2015_2c74e3.json.gz).

Let $a$ be a positive integer. Show the following assertion is valid for sufficiently large integer $n$:
From a grid of squares extending to $\pm\infty$ in both $x$- and $y$-directions, choose $n$ unit (i.e., $1 \times 1$) squares and color them black. Let $K$ be the number of $a \times a$ square blocks which contain exactly $a$ black unit squares. Then the maximum possible value $K$ can take is $a(n+1-a)$.
Here, by the statement "An assertion is valid for sufficiently large $n$", we mean that there exists a positive integer $N$ for which the assertion is valid for all $n \ge N$.


## 2015 — 7

**Record:** `jpn_2015_bd227a`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2015_bd227a.json.gz).

Let $l$ be a straight line lying on the $xy$-plane. For given $20 \times 15$ points $(m, n) : (m = 1, 2, \dots, 20, n = 1, 2, \dots, 15)$ on the $xy$-plane, there are $222$ straight lines parallel to the line $l$ ($l$ itself may be considered as one of those parallel lines) and going through at least one of these points. How many straight lines are there which go through at least one of these points and are perpendicular to $l$?


## 2015 — 4

**Record:** `jpn_2015_d092b4`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2015_d092b4.json.gz).

Suppose you want to distribute nine distinct integers greater than or equal to $1$ and less than or equal to $9$ into nine square boxes of a $3 \times 3$ grid in such a way that the sums of the numbers on each row and each column are all multiples of $3$. How many possible ways of distributing numbers are there to attain this goal? Regard two configurations, for which one can be obtained from rotating the other one or by flipping over the other one, to be distinct in counting the number of possible ways.


## 2019 — 6

**Record:** `jpn_2019_13b27b`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2019_13b27b.json.gz).

Some of the vertices of a regular $120$-gon are labeled by $*$. What is the maximal possible number of vertices labeled with $*$ if the following condition must be satisfied?

There exists no isosceles triangle with the angle at the top vertex of $18^\circ$ formed by $*$-labeled vertices of the $120$-gon.


## 2019 — 2

**Record:** `jpn_2019_1de558`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2019_1de558.json.gz).

Let $n$ be an odd integer greater than or equal to $3$. Suppose you play the following game using an $n \times n$ grid made up of $n^2$ $1 \times 1$ squares. The game consists of $n^2$ turns, and at each turn the following actions must be performed in the order specified:
* Choose one empty square and insert one positive integer greater than or equal to $1$ and less than or equal to $n^2$. Throughout the game, any integer can be used only once.
* You gain $1$ point if the sum of numbers written into the squares lying on the same row as the square you chose is a multiple of $n$, and the same rule applies for the column (you get $2$ points if both row sum and column sum are multiples of $n$.)

Find the maximum possible value for the total sum of the points you gain by the end of the game.


## 2019 — 2

**Record:** `jpn_2019_686a49`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2019_686a49.json.gz).

Call a positive integer a good number if its every digit is a prime number. Find all the good numbers having three digits and with the property that their squares are good numbers of five digits.


## 2019 — 7

**Record:** `jpn_2019_7a5927`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2019_7a5927.json.gz).

Suppose quadratic polynomials $P$, $Q$, $R$ with integer coefficients satisfy the following properties:
* $P(1) = P(2) = Q(3) = 0$.
* $P(x)^2 + Q(x)^2 = R(x)^2$ holds for any real number $x$.
* There exists no integer greater than or equal to $2$, which divides all of the numbers appearing as a coefficient of any of $P$, $Q$, $R$.
* The coefficients of the quadratic terms of $P$ and $Q$ are not $0$, and the coefficient of the quadratic term of $R$ is positive.
Find all possible forms of $R(x)$ satisfying the conditions above.


## 2019 — 5

**Record:** `jpn_2019_973fb8`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2019_973fb8.json.gz).

Find the smallest integer $n$ with the following property:
Remainders obtained when $n$ is divided by $97$, $100$, $103$ are $32$, $33$, $34$, respectively.


## 2019 — 1

**Record:** `jpn_2019_e8a872`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2019_e8a872.json.gz).

Find all the triplets $(x, y, z)$ of positive integers satisfying the following conditions:
$$
x + xy + xyz = 31, \quad x < y < z.
$$


## 2019 — 1

**Record:** `jpn_2019_eaa00f`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2019_eaa00f.json.gz).

Find all triplets $(a, b, c)$ of positive integers satisfying the following identity:
$$
a^2 + b + 3 = (b^2 - c^2)^2.
$$


## 2021 — 9

**Record:** `jpn_2021_aec1d9`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2021_aec1d9.json.gz).

Let $A$ be the number of cases such that each cell of a $2021 \times 2021$ table is filled with one of $1$, $2$, or $3$ in such a way that any $2 \times 2$ square in the table sums up to $8$. Answer the remainder after dividing $A$ by $100$.


## 2022 — 10

**Record:** `jpn_2022_60aa31`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2022_60aa31.json.gz).

Determine the number of ways to choose distinct $25$ integers from $1$ to $50$ such that for any two integers chosen, one is not a divisor of the other.


## 2022 — 4

**Record:** `jpn_2022_8b0446`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2022_8b0446.json.gz).

Determine all pairs of positive integers $(x, y)$ which satisfy $3^x - 8^y = 2xy + 1$.


## 2022 — 5

**Record:** `jpn_2022_a7e14f`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2022_a7e14f.json.gz).

How many pairs of integers $(m, n)$ are there with $1 \le m, n \le 2022$ satisfying the following condition?
For any positive integer $N$, there exists a nonnegative integer $k$ and an integer $d > N$ such that both $\frac{m-k^2}{d}$ and $\frac{n+2k}{d}$ are integers.


## 2022 — 11

**Record:** `jpn_2022_b3adee`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2022_b3adee.json.gz).

For each positive integer $n$, define $f(n)$ by
$$
  f(n) = \begin{cases}
    n^{100} & \text{(if digit sum of $n$ is even)}, \\
    -n^{100} & \text{(if digit sum of $n$ is odd)}.
  \end{cases}
$$
Let $S = f(1) + f(2) + \dots + f(10^{100} - 1)$, and determine the largest non-negative integer $m$ such that $S$ is divided by $5^m$. (You can use the fact without proof that $S$ is nonzero.)


## 2022 — 1

**Record:** `jpn_2022_ce8a09`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2022_ce8a09.json.gz).

Find the smallest four-digit integer divisible by three and greater than $2022$ such that there are exactly two types of numbers that appear in the digits.


## 2022 — 9

**Record:** `jpn_2022_e8d416`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2022_e8d416.json.gz).

How many permutations $(p_1, p_2, \dots, p_{1000})$ of $\{1, 2, \dots, 1000\}$ are there such that $p_i$ is a multiple of $i$ for any $1 \le i \le 999$?


## 2023 — 11

**Record:** `jpn_2023_b7080f`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2023_b7080f.json.gz).

Alice and Bob are playing a game using a blackboard. Initially, each of $2, 3, \dots, 50$ is written on the blackboard once. Also, a non-empty subset $S$ of $\{2, 3, \dots, 50\}$ is given. In the first turn, Alice erases all the elements of $S$ from the blackboard. After that, the two players, starting with Bob, take turns erasing one or more integers from the blackboard. However, they cannot erase integers that are relatively prime to all of the integers erased in the opponent's previous turn. The game ends when a player has no integers left to erase at the beginning of their turn, resulting in that player's loss and the other player's win.
How many sets $S$ are there such that Alice can always win, regardless of Bob's actions?


## 2024 — 12

**Record:** `jpn_2024_2726dd`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2024_2726dd.json.gz).

Find the number of tuples $(a_1, a_2, \dots, a_{2100})$ of integers between $0$ and $2099$ inclusive that satisfy the following condition:
There exists a tuple of integers $(b_1, b_2, \dots, b_{2100})$ such that for every integer $i$ from $1$ to $2100$,
$$
a_i \equiv \sum_{\substack{\gcd(j-i, 2100)=1 \\ 1 \le j \le 2100}} b_j \pmod{2100}
$$
holds.


## 2024 — 5

**Record:** `jpn_2024_48b428`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2024_48b428.json.gz).

Show that there are no positive integer solutions $(a, b, c, d, n)$ satisfying the equation $a^2 + b^2 + c^2 + d^2 - 4\sqrt{abcd} = 7 \cdot 2^{2n-1}$.


## 2024 — 2

**Record:** `jpn_2024_70520f`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2024_70520f.json.gz).

Positive integers such that all the digits are prime numbers are called excellent numbers. Determine all the three-digit positive integers $n$ such that $n + 2024$ and $n - 34$ are both excellent numbers. There exist exactly two such positive integers $n$.


## 2024 — 2

**Record:** `jpn_2024_9efea6`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2024_9efea6.json.gz).

Let $N$ denote the set of positive integers. Find all functions $f : N \to N$ such that the equation
$$
\operatorname{lcm}(m, f(m + f(n))) = \operatorname{lcm}(f(m), f(m) + n)
$$
holds for any positive integers $m$ and $n$. Here, for positive integers $x$ and $y$, $\operatorname{lcm}(x, y)$ denotes their least common multiple.


## 2024 — 7

**Record:** `jpn_2024_a26186`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2024_a26186.json.gz).

Determine the number of pairs $(p, a)$ of a prime number $p$ and an integer $a$ such that $p \ge 3$, $1 \le a \le 2024$, and the following condition is satisfied:
$a < p^4$ holds and $ap^4 + 2p^3 + 2p^2 + 1$ is a square number.


## 2024 — 1

**Record:** `jpn_2024_d9ab95`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2024_d9ab95.json.gz).

You are given that the following value is a rational number. Express it as an irreducible fraction.
$$
\sqrt{\frac{123! - 122!}{122! - 121!}}
$$


## 2024 — 5

**Record:** `jpn_2024_eb9ad6`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2024_eb9ad6.json.gz).

Find the smallest integer $n \ge 10$ such that
$$
\left[ \frac{n}{1} \right] \left[ \frac{n}{2} \right] \cdots \left[ \frac{n}{10} \right] = \binom{n}{10}
$$
Here denote by $[r]$ the largest integer less than or equal to $r$ for a real number $r$. For example, $[3.14] = 3$ and $[5] = 5$.


## 2025 — 4

**Record:** `jpn_2025_1ed68c`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2025_1ed68c.json.gz).

Determine how many integers between $1$ and $1000$ (inclusive) have the property that the remainders upon division by $2$, $3$, $4$, $5$, and $6$ are all distinct.


## 2025 — 2

**Record:** `jpn_2025_455cae`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2025_455cae.json.gz).

How many tuples of positive integers $(a, b, c, d)$ satisfy $abcd = 2025$, such that each of $ab$, $bc$, $cd$, and $da$ is a perfect square?


## 2025 — 10

**Record:** `jpn_2025_957b3e`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2025_957b3e.json.gz).

Let $S = \{0, 1, 2, \dots, 8\}$. How many functions $f : S \to S$ satisfy the following condition: For any elements $x, y, z \in S$, if $x+y-z$ is divisible by $9$, then $f(x)f(y) - f(f(z))$ is also divisible by $9$?


## 2025 — 6

**Record:** `jpn_2025_ae112c`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2025_ae112c.json.gz).

Let $a_1, a_2, \dots$ and $b_1, b_2, \dots$ be two sequences consisting of positive integers such that, for any positive integer $n$,
$$
(a_{n+1}, b_{n+1}) = \left( \frac{a_n}{2}, b_n + \frac{a_n}{2} \right) \text{ or } (a_{n+1}, b_{n+1}) = \left( a_n + \frac{b_n}{2}, \frac{b_n}{2} \right)
$$
holds. How many initial pairs $(a_1, b_1)$ with $1 \le a_1, b_1 \le 40$ are possible?


## 2025 — 4

**Record:** `jpn_2025_fd4cdd`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2025_fd4cdd.json.gz).

Determine all polynomials $f(x)$ with integer coefficients such that, for any integer $n \ge 2$, the following conditions hold:
$\bullet\ f(n) > 0.$
$\bullet\ f(n)$ divides $n^{f(n)} - 1$.



# KMO source statements

## 2006 — 6

**Record:** `kor_2006_38a9dc`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2006_38a9dc.json.gz).

A positive integer $N$ is said to be an "*n*-good number" if it satisfies the following two properties:
(Property 1) $N$ is divisible by at least $n$ distinct primes
(Property 2) There exist distinct positive divisors $1, x_2, \dots, x_n$ of $N$ such that
$$
1 + x_2 + \dots + x_n = N.
$$
Show that there exists an "*n*-good number" for each $n \ge 6$.


## 2006 — 2

**Record:** `kor_2006_96342c`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2006_96342c.json.gz).

For a positive integer $a$, let $S_a$ be the set of primes satisfying the following condition:
(condition) For any $p \in S_a$, there exists an odd integer $b$ such that $(2^{2^a})^b - 1$ is divisible by $p$.
For any positive integer $a$, prove that there exist infinitely many primes that are not contained in $S_a$.


## 2008 — 4

**Record:** `kor_2008_2c3894`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2008_2c3894.json.gz).

For a positive integer $m \ge 2$, define
$$
A_m := \{ m+1, 3m+2, 5m+3, 7m+4, 9m+5, \dots \}.
$$
(1) Prove that, for any given $m \ge 2$, there exists a positive integer $a$, $1 \le a < m$, such that either $2^a \in A_m$ or $2^a + 1 \in A_m$.

(2) Assume that, for some $m \ge 2$, there exist positive integers $a$ and $b$ for which $2^a \in A_m$ and $2^b + 1 \in A_m$. Let $a_0$ and $b_0$ be the smallest such $a$ and $b$, respectively, and find a relation between $a_0$ and $b_0$.


## 2008 — 2

**Record:** `kor_2008_ea6719`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2008_ea6719.json.gz).

Determine a polynomial $f(x)$ with integer coefficients which satisfies the following property: There are infinitely many relatively prime positive integers $a, b$ such that $a + b$ divides $f(a) + f(b)$.


## 2009 — 6

**Record:** `kor_2009_7d8389`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2009_7d8389.json.gz).

Find all pairs of positive integers $m$, $n$ satisfying the equation $3^m - 7^n = 2$.


## 2011 — 1

**Record:** `kor_2011_babdb4`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2011_babdb4.json.gz).

Prove that there are no positive integers $x, y, z$ such that
$$
x^2 y^4 - x^4 y^2 + 4x^2 y^2 z^2 + x^2 z^4 - y^2 z^4 = 0.
$$


## 2012 — 6

**Record:** `kor_2012_7f29e1`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2012_7f29e1.json.gz).

Let $M$ be the set of positive integers which is not divisible by any prime number greater than $3$. For arbitrary chosen subsets $A_1, A_2, A_3, \dots$ of $M$, prove that there exist two distinct positive integers $i$ and $j$ such that:
For each $x$ in $A_i$, $A_j$ has a divisor of $x$.


## 2013 — 5

**Record:** `kor_2013_090453`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2013_090453.json.gz).

Let $a$, $b$ be relatively prime positive integers and let $a_n$ and $b_n$ be integer sequences satisfying $(a + b\sqrt{2})^{2n} = a_n + b_n\sqrt{2}$. Find all primes $p$ such that there is a positive integer $n$ less than or equal to $p$ satisfying $b_n \equiv 0 \pmod{p}$.


## 2015 — 5

**Record:** `kor_2015_d64066`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2015_d64066.json.gz).

For a given positive integer $k$, define two sequences $\{a_n\}$ and $\{b_n\}$ as follows:
$$
\begin{aligned}
a_1 &= k, & a_2 &= k, & a_{n+2} &= a_n a_{n+1} \quad (n \ge 1) \\
b_1 &= 1, & b_2 &= k, & b_{n+2} &= \frac{b_{n+1}^3 + 1}{b_n} \quad (n \ge 1)
\end{aligned}
$$
For any positive integer $n$, show that $a_{2n}b_{n+3}$ is an integer.


## 2016 — Problem 3

**Record:** `kor_2016_3a86c0`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2016_3a86c0.json.gz).

Show that there are no rational numbers $x$ and $y$ such that
$$
x - \frac{1}{x} + y - \frac{1}{y} = 4.
$$


## 2024 — Problem 6

**Record:** `kor_2024_89b8c1`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2024_89b8c1.json.gz).

Show that there exists a positive integer $K$ satisfying the following: for any prime $p > K$, the number of integers $1 \le a \le p$ such that $a^{p-1} - 1$ is divisible by $p^2$ is less than or equal to $\frac{p}{2^{2024}}$.



# RMM source statements

## 2012 — Problem 1

**Record:** `rmm_2012_b79110`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2012_b79110.json.gz).

Given a finite group of boys and girls, a covering set of boys is a set of boys such that every girl knows at least one boy in that set; and a covering set of girls is a set of girls such that every boy knows at least one girl in that set. Prove that the number of covering sets of boys and the number of covering sets of girls have the same parity. (Acquaintance is assumed to be mutual.)


## 2012 — Problem 4

**Record:** `rmm_2012_d9fcef`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2012_d9fcef.json.gz).

Prove that there are infinitely many positive integer numbers $n$ such that $2^{2^{n}+1}+1$ is divisible by $n$, but $2^{n}+1$ is not.


## 2013 — 5.

**Record:** `usa_2013_de41b7`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2013_de41b7.json.gz).

Given an integer $k \ge 2$, set $a_1 = 1$ and, for every integer $n \ge 2$, let $a_n$ be the smallest $x > a_{n-1}$ such that

$$
x = 1 + \sum_{i=1}^{n-1} \lfloor \sqrt[k]{\frac{x}{a_i}} \rfloor.
$$

Prove that every prime occurs in the sequence $a_1, a_2, \dots$.


## 2015 — Problem 2.

**Record:** `rmm_2015_2cd14a`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2015_2cd14a.json.gz).

For an integer $n \geq 5$, two players play the following game on a regular $n$-gon. Initially, three consecutive vertices are chosen, and one counter is placed on each. A move consists of one player sliding one counter along any number of edges to another vertex of the $n$-gon without jumping over another counter. A move is legal if the area of the triangle formed by the counters is strictly greater after the move than before. The players take turns to make legal moves, and if a player cannot make a legal move, that player loses. For which values of $n$ does the player making the first move have a winning strategy?


## 2017 — Problem 2

**Record:** `rou_2017_ecd799`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2017_ecd799.json.gz).

Determine all positive integers $n$ satisfying the following condition: for every monic polynomial $P$ of degree at most $n$ with integer coefficients, there exists a positive integer $k \le n$, and $k+1$ distinct integers $x_1, x_2, \dots, x_{k+1}$ such that $P(x_1) + P(x_2) + \dots + P(x_k) = P(x_{k+1})$.

*Note.* A polynomial is *monic* if the coefficient of the highest power is one.


## 2019 — Problem 1

**Record:** `rmm_2019_0d3e45`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2019_0d3e45.json.gz).

Amy and Bob play the game. At the beginning, Amy writes down a positive integer on the board. Then the players take moves in turn, Bob moves first. On any move of his, Bob replaces the number $n$ on the blackboard with a number of the form $n-a^{2}$, where $a$ is a positive integer. On any move of hers, Amy replaces the number $n$ on the blackboard with a number of the form $n^{k}$, where $k$ is a positive integer. Bob wins if the number on the board becomes zero. Can Amy prevent Bob's win?


## 2019 — Problem 6

**Record:** `rmm_2019_39ca85`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2019_39ca85.json.gz).

Find all pairs of integers $(c, d)$, both greater than $1$, such that the following holds:
For any monic polynomial $Q$ of degree $d$ with integer coefficients and for any prime $p > c(2c+1)$, there exists a set $S$ of at most $\left(\frac{2c-1}{2c+1}\right)p$ integers, such that
$$
\bigcup_{s \in S} \{s, Q(s), Q(Q(s)), Q(Q(Q(s))), \ldots\}
$$
is a complete residue system modulo $p$ (i.e., intersects with every residue class modulo $p$).


## 2021 — Problem 3

**Record:** `rmm_2021_7ba909`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2021_7ba909.json.gz).

A number of 17 workers stand in a row. Every contiguous group of at least 2 workers is a brigade. The chief wants to assign each brigade a leader (which is a member of the brigade) so that each worker's number of assignments is divisible by 4. Prove that the number of such ways to assign the leaders is divisible by 17.


## 2021 — Problem 2

**Record:** `rmm_2021_d11caf`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2021_d11caf.json.gz).

Xenia and Sergey play the following game. Xenia thinks of a positive integer $N$ not exceeding $5000$. Then she fixes $20$ distinct positive integers $a_{1}, a_{2}, \ldots, a_{20}$ such that, for each $k=1,2, \ldots, 20$, the numbers $N$ and $a_{k}$ are congruent modulo $k$. By a move, Sergey tells Xenia a set $S$ of positive integers not exceeding $20$, and she tells him back the set $\{a_{k}: k \in S\}$ without spelling out which number corresponds to which index. How many moves does Sergey need to determine for sure the number Xenia thought of?


## 2024 — Problem 4.

**Record:** `rou_2024_e0aa00`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2024_e0aa00.json.gz).

Fix integers $a$ and $b$ greater than $1$. For any positive integer $n$, let $r_n$ be the (non-negative) remainder $b^n$ leaves upon division by $a^n$. Assume that there exists a positive integer $N$ such that $r_n < 2^n/n$ for all integers $n \ge N$. Prove that $a$ divides $b$.


## 2024 — Problem 6.

**Record:** `rou_2024_e309ed`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2024_e309ed.json.gz).

A polynomial $P$ with integer coefficients is *square-free* if it is not expressible in the form $P = Q^2R$, where $Q$ and $R$ are polynomials with integer coefficients and $Q$ is not constant. For a positive integer $n$, let $P_n$ be the set of polynomials of the form
$$
1 + a_1x + a_2x^2 + \dots + a_nx^n
$$
with $a_1, a_2, \dots, a_n \in \{0, 1\}$. Prove that there exists an integer $N$ so that, for all integers $n \ge N$, more than 99% of the polynomials in $P_n$ are square-free.


## 2024 — Problem 2.

**Record:** `rou_2024_eb35fe`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2024_eb35fe.json.gz).

Consider an odd prime $p$ and a positive integer $N < 50p$. Let $a_1, a_2, \dots, a_N$ be a list of positive integers less than $p$ such that any specific value occurs at most $\frac{51}{100}N$ times and $a_1 + a_2 + \dots + a_N$ is not divisible by $p$. Prove that there exists a permutation $b_1, b_2, \dots, b_N$ of the $a_i$ such that, for all $k = 1, 2, \dots, N$, the sum $b_1 + b_2 + \dots + b_k$ is not divisible by $p$.



# USAMO source statements

## 2006 — 3

**Record:** `usa_2006_2edd72`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2006_2edd72.json.gz).

For integral $m$, let $p(m)$ be the greatest prime divisor of $m$. By convention, we set $p(\pm 1) = 1$ and $p(0) = \infty$. Find all polynomials $f$ with integer coefficients such that the sequence $\{p(f(n^2)) - 2n\}_{n \ge 0}$ is bounded above. (In particular, this requires $f(n^2) \ne 0$ for $n \ge 0$.)


## 2006 — 5

**Record:** `usa_2006_ce5644`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2006_ce5644.json.gz).

A mathematical frog jumps along the number line. The frog starts at $1$, and jumps according to the following rule: if the frog is at integer $n$, then it can jump either to $n + 1$ or to $n + 2^{m_n+1}$ where $2^{m_n}$ is the largest power of $2$ that is a factor of $n$. Show that if $k \ge 2$ is a positive integer and $i$ is a nonnegative integer, then the minimum number of jumps needed to reach $2^i k$ is greater than the minimum number of jumps needed to reach $2^i$.


## 2006 — 1

**Record:** `usa_2006_da8d07`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2006_da8d07.json.gz).

Let $p$ be a prime number and let $s$ be an integer with $0 < s < p$. Prove that there exist integers $m$ and $n$ with $0 < m < n < p$ and
$$
\{\frac{sm}{p}\} < \{\frac{sn}{p}\} < \frac{s}{p}
$$
if and only if $s$ is not a divisor of $p-1$.
(For $x$ a real number, let $\lfloor x \rfloor$ denote the greatest integer less than or equal to $x$, and let $\{x\} = x - \lfloor x \rfloor$ denote the fractional part of $x$.)


## 2007 — 1

**Record:** `usa_2007_83a6e7`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2007_83a6e7.json.gz).

Let $n$ be a positive integer. Define a sequence by setting $a_1 = n$ and, for each $k > 1$, letting $a_k$ be the unique integer in the range $0 \le a_k \le k - 1$ for which $a_1 + a_2 + \cdots + a_k$ is divisible by $k$. For instance, when $n = 9$ the obtained sequence is $9, 1, 2, 0, 3, 3, 3, \dots$. Prove that for any $n$ the sequence $a_1, a_2, a_3, \dots$ eventually becomes constant.


## 2007 — 5

**Record:** `usa_2007_b62228`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2007_b62228.json.gz).

Prove that for every nonnegative integer $n$, the number $7^{7^n} + 1$ is the product of at least $2n+3$ (not necessarily distinct) primes.


## 2008 — 5

**Record:** `usa_2008_6039a6`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2008_6039a6.json.gz).

Three nonnegative real numbers $r_1$, $r_2$, $r_3$ are written on a blackboard. These numbers have the property that there exist integers $a_1$, $a_2$, $a_3$, not all zero, satisfying $a_1 r_1 + a_2 r_2 + a_3 r_3 = 0$. We are permitted to perform the following operation: find two numbers $x$, $y$ on the blackboard with $x \le y$, then erase $y$ and write $y-x$ in its place. Prove that after a finite number of such operations, we can end up with at least one $0$ on the blackboard.

(This problem was suggested by Kiran Kedlaya.)


## 2008 — 1

**Record:** `usa_2008_91e70b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2008_91e70b.json.gz).

Prove that for each positive integer $n$, there are pairwise relatively prime integers $k_0, k_1, \dots, k_n$, all strictly greater than 1, such that $k_0 k_1 \cdots k_n - 1$ is the product of two consecutive integers.


## 2009 — 2

**Record:** `usa_2009_ddbe0d`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2009_ddbe0d.json.gz).

Let $n$ be a positive integer. Determine the size of the largest subset of $\{-n, -n+1, \dots, n-1, n\}$ which does not contain three elements $a, b, c$ (not necessarily distinct) satisfying $a+b+c=0$.


## 2010 — 5

**Record:** `usa_2010_73d4a3`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2010_73d4a3.json.gz).

Let $q = \frac{3p-5}{2}$ where $p$ is an odd prime, and let
$$
S_q = \frac{1}{2 \cdot 3 \cdot 4} + \frac{1}{5 \cdot 6 \cdot 7} + \dots + \frac{1}{q(q+1)(q+2)}.
$$
Prove that if $\frac{1}{p} - 2S_q = \frac{m}{n}$ for integers $m$ and $n$, then $m-n$ is divisible by $p$.


## 2011 — 2

**Record:** `usa_2011_75d863`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2011_75d863.json.gz).

An integer is assigned to each vertex of a regular pentagon so that the sum of the five integers is $2011$. A turn of a solitaire game consists of subtracting an integer $m$ from each of the integers at two neighboring vertices and adding $2m$ to the opposite vertex, which is not adjacent to either of the first two vertices. (The amount $m$ and the vertices chosen can vary from turn to turn.) The game is won at a certain vertex if, after some number of turns, that vertex has the number $2011$ and the other four vertices have the number $0$. Prove that for any choice of the initial integers, there is exactly one vertex at which the game can be won.


## 2012 — 3

**Record:** `usa_2012_a825fc`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2012_a825fc.json.gz).

Determine which integers $n > 1$ have the property that there exists an infinite sequence $a_1, a_2, a_3, \dots$ of nonzero integers such that the equality
$$
a_k + 2a_{2k} + \dots + n a_{nk} = 0
$$
holds for every positive integer $k$.


## 2014 — 6.

**Record:** `usa_2014_952bd1`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2014_952bd1.json.gz).

Prove that there is a constant $c > 0$ with the following property: If $a, b, n$ are positive integers such that $\gcd(a + i, b + j) > 1$ for all $i, j \in \{0, 1, \dots, n\}$, then
$$
\min\{a, b\} > c^n \cdot n^{\frac{n}{2}}.
$$


## 2025 — USAMO 1

**Record:** `usa_2025_65d3dd`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_65d3dd.json.gz).

Let $k$ and $d$ be positive integers. Prove that there exists a positive integer $N$ such that for every odd integer $n > N$, the digits in the base-$2n$ representation of $n^k$ are all greater than $d$.


## 2025 — 5

**Record:** `usa_2025_e0957e`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_e0957e.json.gz).

Determine, with proof, all positive integers $k$ such that
$$
\frac{1}{n+1} \sum_{i=0}^{n} \binom{n}{i}^{k}
$$
is an integer for every positive integer $n$.



# VMO source statements

## 2001 — 2

**Record:** `vnm_2001_8275ea`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2001_8275ea.json.gz).

Let be given a positive integer $n$ and two coprime integers $a, b$ greater than $1$. Let $p, q$ be two odd divisors greater than $1$ of $a^{6n} + b^{6n}$. Find the remainder of the division of $p^{6n} + q^{6n}$ by $6 \cdot (12)^n$.


## 2003 — 5

**Record:** `vnm_2003_963d6a`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2003_963d6a.json.gz).

Find the greatest positive integer $n$ such that the system of equations
$$
(x+1)^2 + y_1^2 = (x+2)^2 + y_2^2 = \dots = (x+k)^2 + y_k^2 = \dots = (x+n)^2 + y_n^2
$$
has integral solution $(x, y_1, y_2, \dots, y_n)$.


## 2005 — Problem 5.

**Record:** `vnm_2005_ac7e15`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2005_ac7e15.json.gz).

Find all triples of natural numbers $(x, y, n)$ satisfying the relation
$$
\frac{x! + y!}{n!} = 3^n
$$
(with the convention $0! = 1$).


## 2006 — Problem 6

**Record:** `vnm_2006_fbb149`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2006_fbb149.json.gz).

Consider a set $S$ of 2006 distinct numbers. A subset $T$ of $S$ is called stubborn if for every $u, v$ (not necessarily distinct) in $T$, the number $u + v$ does not belong to $T$. Prove that

i) if $S$ is the set of 2006 first positive integers, then the number of elements of every stubborn subset $T$ of $S$ does not exceed 1003,

ii) if $S$ consists of 2006 arbitrary positive integers then there exists a stubborn subset $T$ of $S$ having 669 elements.


## 2008 — 6

**Record:** `vnm_2008_6bc7d0`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2008_6bc7d0.json.gz).

Denote by $M$ the set of the first $2008$ positive integers. The numbers in $M$ are colored blue, yellow and red such that each number is of one color and each color is used at least once. Consider the following sets:
$$
S_1 = \{(x, y, z) \in M^3 \mid x, y, z \text{ are of the same color and } (x + y + z) \equiv 0 \pmod{2008}\};
$$
$$
S_2 = \{(x, y, z) \in M^3 \mid x, y, z \text{ are of the three colors and } (x + y + z) \equiv 0 \pmod{2008}\}.
$$
Prove that $2|S_1| > |S_2|$.


## 2008 — 5

**Record:** `vnm_2008_e8616d`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2008_e8616d.json.gz).

Determine the number of positive integers that are multiple of $9$ with at most $2008$ decimal digits, and among these digits at least two are $9$.


## 2009 — Problem 4

**Record:** `vnm_2009_d06acd`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2009_d06acd.json.gz).

Given real numbers $a$, $b$, $c$ satisfying the condition: for each positive integer $n$, $a^n + b^n + c^n$ is an integer. Show that there exist integers $p$, $q$, $r$ such that $a$, $b$, $c$ are 3 solutions to the equation $x^3 + px^2 + qx + r = 0$.


## 2010 — 4

**Record:** `vnm_2010_8c54a3`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2010_8c54a3.json.gz).

Prove that for every positive integer $n$ the equation
$$
x^2 + 15y^2 = 4^n
$$
has at least $n$ non-negative integer solutions $(x, y)$.


## 2011 — 5

**Record:** `vnm_2011_0893a4`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2011_0893a4.json.gz).

A sequence of integers $(a_n)$ determined by
$$
a_0 = 1,\ a_1 = -1 \quad \text{and} \quad a_n = 6a_{n-1} + 5a_{n-2} \quad \text{for all } n \ge 2.
$$
Show that $a_{2012} - 2010$ is divisible by $2011$.


## 2012 — 6

**Record:** `vnm_2012_059cee`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_059cee.json.gz).

Let $a$, $b$ be two odd natural numbers. Suppose that $a$ is a divisor of $b^2 + 2$ and $b$ is a divisor of $a^2 + 2$. Prove that $a$ and $b$ belong to the sequence $(v_n)$ defined by
$$
v_1 = v_2 = 1 \quad \text{and} \quad v_n = 4v_{n-1} - v_{n-2} \quad \forall n \ge 3.
$$


## 2012 — Problem 6.

**Record:** `vnm_2012_736692`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_736692.json.gz).

Let $A$ be the set of positive integers that can be written in the form $2x^2 + 3y^2$ where $x, y$ are integers with $x^2 + y^2 \neq 0$. Prove that:

a) All numbers from $A$ are not perfect square.

b) The product of an odd number of numbers from $A$ is not a perfect square.


## 2012 — Problem 1.

**Record:** `vnm_2012_f162cc`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_f162cc.json.gz).

Find all integers $x, y$ such that
$$
x(x^{999} - 1) = (x - 1)y(y + 2).
$$


## 2013 — 4

**Record:** `vnm_2013_8efd6e`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2013_8efd6e.json.gz).

Several natural numbers are given on a line. We perform a transformation as follows: for every pair of consecutive integers on the line, write the sum of those two numbers in the middle of them. After 2013 such steps, how many times number 2013 are there on the line if

a) The given numbers are $1$ and $1000$?

b) The given numbers are $1, 2, 3, \ldots, 1000$ on the increasing order from the left to the right?


## 2014 — 7

**Record:** `vnm_2014_aef204`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2014_aef204.json.gz).

Find all sets of 2014 rational numbers not necessarily distinct such that: If an arbitrary number in the set is removed, one always can divide the remaining 2013 numbers into three sets such that each set has exactly 671 elements and the products of all elements in each set are equal.


## 2014 — 2

**Record:** `vnm_2014_dd4b83`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2014_dd4b83.json.gz).

Prove that for all positive integers $n$, the polynomial
$$
P(x) = (x^2 - 7x + 6)^{2n} + 13
$$
can not be written as a product of $(n+1)$ non-constant polynomials with integer coefficients.


## 2015 — 6

**Record:** `vnm_2015_380aa2`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2015_380aa2.json.gz).

For positive integers $a$, $n$; consider the following equation:
$$
a^2x + 6a y + 36z = n
$$
where $x$, $y$, $z$ are non-negative natural numbers.

a) Find all integers $a$ such that for all $n \ge 250$, the given equation always has natural roots $(x, y, z)$.

b) Given that $a > 1$ and $\gcd(a, 6) = 1$. Find the greatest value of $n$ in terms of $a$ such that the given equation doesn't have natural root $(x, y, z)$.


## 2015 — 3

**Record:** `vnm_2015_ef4208`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2015_ef4208.json.gz).

Given a positive integer $k$. Find the number of non-negative integers that do not exceed $10^k$ and satisfy the following conditions

i) $n$ is divisible by $3$,
ii) The digits of $n$ in decimal representation are in the set $\{2, 0, 1, 5\}$.


## 2015 — 5

**Record:** `vnm_2015_ff240f`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2015_ff240f.json.gz).

Let $f_n(x)$ be a sequence of polynomials, where $f_0(x) = 2$, $f_1(x) = 3x$, and
$$
f_n(x) = 3x f_{n-1}(x) + (1 - x - 2x^2) f_{n-2}(x)
$$
for all $n \ge 2$. Determine all positive integers $n$ such that $f_n(x)$ is divisible by $x^3 - x^2 + x$.


## 2021 — Problem 4.

**Record:** `vnm_2021_127c04`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2021_127c04.json.gz).

For each integer $n \ge 2$, let $s(n)$ denote the sum of all positive integers that are at most $n$ and not relatively prime to $n$.
a) Prove that $s(n) = \frac{n}{2}(n+1-\varphi(n))$, where $\varphi(n)$ is the number of positive integers that are at most $n$ and are relatively prime to $n$.
b) Prove that there does not exist an integer $n \ge 2$ such that
$$
s(n) = s(n + 2021).
$$


## 2022 — 5

**Record:** `vnm_2022_050178`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2022_050178.json.gz).

Consider 2 non-constant polynomials $P(x), Q(x)$, with non-negative coefficients. The coefficients of $P(x)$ is not larger than $2021$ and $Q(x)$ has at least one coefficient larger than $2021$. Assume that $P(2022) = Q(2022)$ and $P(x), Q(x)$ has a common rational root $\frac{p}{q} \neq 0$ for some $p, q \in \mathbb{Z}$, $(\gcd(p, q) = 1)$. Prove that
$$
|p| + n|q| \leq Q(n) - P(n), \forall n = 1, 2, \dots, 2021.
$$


## 2022 — 4

**Record:** `vnm_2022_ba1c51`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2022_ba1c51.json.gz).

For every pair of positive integers $n, m$ with $n < m$, denote $s(n, m)$ as the number of positive integers in the range $[n, m]$ that are coprime with $m$. Find all positive integers $m \ge 2$ such that $m$ satisfies these conditions

i) $\frac{s(n, m)}{m-n} \ge \frac{s(1, m)}{m}$ for all $n = 1, 2, \dots, m-1$.
ii) $2022^m + 1$ is divisible by $m^2$.


## 2023 — 2

**Record:** `vnm_2023_a8510a`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2023_a8510a.json.gz).

Let $a, b, c, \alpha, \beta$ be the given integers and the sequence $(u_n)$ is defined by $u_1 = \alpha, u_2 = \beta, u_{n+2} = a u_{n+1} + b u_n + c$ for all $n \ge 1$.

a) Prove that if $a = 3, b = -2, c = -1$ then there are infinitely many pairs of integers $(\alpha; \beta)$ so that $u_{2023} = 2^{2022}$.

b) Prove that there exists a positive integer $n_0$ such that exactly one of the following two statements is true:

i) There are infinitely many positive integers $m$, such that $u_{n_0}u_{n_0+1}\dots u_{n_0+m}$ is divisible by $7^{2023}$ or $17^{2023}$;

ii) There are infinitely many positive integers $k$ so that $u_{n_0}u_{n_0+1}\dots u_{n_0+k} - 1$ is divisible by 2023.


## 2024 — 7

**Record:** `vnm_2024_9e7ac6`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2024_9e7ac6.json.gz).

In the space, there is a convex polyhedron $D$ such that for every vertex of $D$, there are an even number of edges passing through that vertex. We choose a face $F$ of $D$. Then we assign each edge of $D$ a positive integer such that for all faces of $D$ different from $F$, the sum of the numbers assigned on the edges of that face is a positive integer divisible by 2024. Prove that the sum of the numbers assigned on the edges of $F$ is also a positive integer divisible by 2024.


