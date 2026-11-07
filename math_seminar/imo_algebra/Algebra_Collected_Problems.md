---
title: "Olympiad Algebra: Collected Problems"
author: "Ayden Bi"
date: "Research edition • 6 November 2026"
lang: en-US
---

# Scope and attribution {.unnumbered}

This volume contains sixteen restated problems from the checked core, followed by 716 source-provided statements. It is a partial collection. Source classifications, numbering and transcriptions are not all independently verified. Mixed-domain records may occur in other subject volumes. The corresponding proofs are in the separate worked volume and the individually labeled source-solution files.

The source statements are reproduced under MathNet's CC BY 4.0 fallback where recovered metadata contains no explicit original rights assertion. The complete package preserves original booklet credits and metadata. Figure-dependent statements and records with uncertain or explicit original rights remain source pointers. Original source wording is retained apart from logged typesetting compatibility repairs. The checked core is separately restated and corrected.

MathNet: Shaden Alshammari, Kevin Wen, Abrar Zainal, Mark Hamilton, Navid Safaei, Sultan Albarakati, William T. Freeman and Antonio Torralba, *MathNet: A Global Multimodal Benchmark for Mathematical Reasoning and Retrieval*, ICLR 2026. Sources: https://mathnet.mit.edu/ ; https://huggingface.co/datasets/ShadenA/MathNet ; https://creativecommons.org/licenses/by/4.0/ . Original source contributors are credited in the ledger and individual problem files.

Read Coverage_Report.md for exact counts, historical gaps, withheld records and the distinction between actual contests, shortlists and selection material. The author credit identifies this compiled edition and its authored expositions, not authorship of the historical problems.

# The sixteen checked-core problems

## A01. Remove the composition

**Source:** IMO 2019, Problem 1; shortlist A1. **Record:** `imo_2019_abb25c`.

Classify the integer-valued functions on the integers for which
$$f(2x)+2f(y)=f(f(x+y))\qquad(x,y\in\mathbb Z).$$

## A02. The exact cost of monotonicity

**Source:** IMO shortlist 2007, A1. **Record:** `imo_2007_524a29`.

Given real $a_1,\ldots,a_n$, set $M_i=\max_{j\le i}a_j$, $m_i=\min_{j\ge i}a_j$, and $d=\max_i(M_i-m_i)$. Prove that the least possible value of $\max_i|x_i-a_i|$, over nondecreasing real sequences $(x_i)$, is $d/2$.

## A03. A floor map eventually repeats

**Source:** IMO shortlist 2006, A1. **Record:** `imo_2006_e3e5ce`.

Starting from an arbitrary real $a_0$, iterate $a_{r+1}=\lfloor a_r\rfloor\{a_r\}$, where $\{x\}=x-\lfloor x\rfloor$. Prove that eventually $a_{r+2}=a_r$.

## A04. Cancel the exceptional coefficient

**Source:** IMO shortlist 2006, A2. **Record:** `imo_2006_e18476`.

Let $a_0=-1$ and, for $n\ge1$, let $\sum_{k=0}^n a_k/(n-k+1)=0$. Show that every $a_n$ with $n\ge1$ is positive.

## A05. Translate a quartic into a norm

**Source:** IMO shortlist 2010, A2. **Record:** `imo_2010_66cdab`.

Real $a,b,c,d$ have sum $6$ and sum of squares $12$. Prove
$$36\le4\sum a^3-\sum a^4\le48,$$
where both sums run over the four variables.

## A06. Reverse the coefficients, keep the answer

**Source:** IMO shortlist 2013, A1. **Record:** `imo_2013_d960d1`.

For real $a_1,\ldots,a_{n-1}$, define $u_0=u_1=1$ and $u_{k+1}=u_k+a_ku_{k-1}$. Define $v_0=v_1=1$ by the same recurrence with $a_1,\ldots,a_{n-1}$ reversed. Prove $u_n=v_n$.

## A07. A unique crossing

**Source:** IMO shortlist 2014, A1. **Record:** `imo_2014_6534d6`.

For strictly increasing positive integers $z_0,z_1,\ldots$, prove that exactly one $n\ge1$ satisfies
$$z_n<\frac{z_0+\cdots+z_n}{n}\le z_{n+1}.$$

## A08. An endpoint certificate for variance

**Source:** IMO shortlist 2019, A2. **Record:** `imo_2019_cd6d5a`.

Real numbers $u_1,\ldots,u_{2019}$ have sum zero and squared sum one. If $a$ and $b$ are their minimum and maximum, prove $ab\le-1/2019$.

## A09. Pair the cyclic ratios

**Source:** IMO shortlist 2020, A3. **Record:** `imo_2020_db020b`.

Positive $a,b,c,d$ satisfy $(a+c)(b+d)=ac+bd$. Determine the minimum of $a/b+b/c+c/d+d/a$.

## A10. Integer averages cannot rise too slowly

**Source:** IMO 2024, Problem 1; shortlist A1. **Record:** `imo_2024_071598`.

Find real $\alpha$ for which $n$ divides $\sum_{k=1}^n\lfloor k\alpha\rfloor$ for every positive integer $n$.

## A11. Pay for one unit at a time

**Source:** IMO shortlist 2024, A2. **Record:** `imo_2024_5877d2`.

Minimize $\sum_{i=0}^n2^i x_i^2$ over nonnegative integers with $\sum_{i=0}^n x_i=n$.

## A12. Choose the Jensen weights

**Source:** IMO shortlist 2009, A2. **Record:** `imo_2009_c42bed`.

Positive $a,b,c$ satisfy $1/a+1/b+1/c=a+b+c$. Prove $\sum_{\mathrm{cyc}}(2a+b+c)^{-2}\le3/16$.

## A13. A polynomial has a definite sign

**Source:** IMO shortlist 2017, A1. **Record:** `imo_2017_5b8561`.

Positive integers $a_i$ satisfy $\sum 1/a_i=k\in\mathbb Z_{>0}$ and $\prod a_i=M>1$. Show that $M(x+1)^k-\prod(x+a_i)$ has no positive real root.

## A14. A sharp quadratic majorant

**Source:** IMO shortlist 2020, A1, Version 1. **Record:** `imo_2020_48d762`.

For $N=2^n$ with $n\ge1$, find the least $c$ such that $((1+x^{2N})/2)^{1/N}\le x+c(x-1)^2$ for every real $x$.

## A15. The radical inequality and its sharp parameter

**Source:** IMO 2001, Problem 2. Official paper: [PDF](https://www.imo-official.org/assets/documents/problems/2001/2001_eng.pdf).

For positive $a,b,c$, prove $\sum_{\mathrm{cyc}}a/\sqrt{a^2+8bc}\ge1$.

## A16. Measure a union of rational-inequality intervals

**Source:** IMO 1988, Problem 4. Official paper: [PDF](https://www.imo-official.org/assets/documents/problems/1988/1988_eng.pdf).

Show that the real solution set of $\sum_{k=1}^{70} k/(x-k)\ge5/4$ is a disjoint union of intervals whose total length is $1988$; the poles are excluded from the domain.


# APMO source statements

## 1989 — 1

**Record:** `apm_1989_7c33be`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1989_7c33be.json.gz).

Let $x_{1}, x_{2}, \ldots, x_{n}$ be positive real numbers, and let
$$
S = x_{1} + x_{2} + \cdots + x_{n} .
$$
Prove that
$$
\left(1 + x_{1}\right)\left(1 + x_{2}\right) \cdots \left(1 + x_{n}\right) \leq 1 + S + \frac{S^{2}}{2!} + \frac{S^{3}}{3!} + \cdots + \frac{S^{n}}{n!} .
$$


## 1989 — 4

**Record:** `apm_1989_ab9780`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1989_ab9780.json.gz).

Let $S$ be a set consisting of $m$ pairs $(a, b)$ of positive integers with the property that $1 \leq a < b \leq n$. Show that there are at least
$$
4m \frac{\left(m-\frac{n^{2}}{4}\right)}{3n}
$$
triples $(a, b, c)$ such that $(a, b), (a, c)$, and $(b, c)$ belong to $S$.


## 1989 — 5

**Record:** `apm_1989_f42c63`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1989_f42c63.json.gz).

Determine all functions $f$ from the reals to the reals for which
(1) $f(x)$ is strictly increasing,
(2) $f(x)+g(x)=2x$ for all real $x$, where $g(x)$ is the composition inverse function to $f(x)$.
(Note: $f$ and $g$ are said to be composition inverses if $f(g(x))=x$ and $g(f(x))=x$ for all real $x$.)


## 1990 — 2

**Record:** `apm_1990_e66529`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1990_e66529.json.gz).

Let $a_{1}, a_{2}, \ldots, a_{n}$ be positive real numbers, and let $S_{k}$ be the sum of products of $a_{1}, a_{2}, \ldots, a_{n}$ taken $k$ at a time.
Show that
$$
S_{k} S_{n-k} \geq \binom{ n}{k}^{2} a_{1} a_{2} \ldots a_{n}, \quad \text{ for } \quad k=1,2, \ldots, n-1
$$


## 1991 — 3

**Record:** `apm_1991_cad7b7`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1991_cad7b7.json.gz).

Let $a_{1}, a_{2}, \ldots, a_{n}, b_{1}, b_{2}, \ldots, b_{n}$ be positive real numbers such that $a_{1}+a_{2}+\cdots+a_{n}=b_{1}+b_{2}+ \cdots+b_{n}$. Show that

$$
\frac{a_{1}^{2}}{a_{1}+b_{1}}+\frac{a_{2}^{2}}{a_{2}+b_{2}}+\cdots+\frac{a_{n}^{2}}{a_{n}+b_{n}} \geq \frac{a_{1}+a_{2}+\cdots+a_{n}}{2} .
$$


## 1992 — 4

**Record:** `apm_1992_0e43a2`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1992_0e43a2.json.gz).

Determine all pairs $(h, s)$ of positive integers with the following property: If one draws $h$ horizontal lines and another $s$ lines which satisfy
(i) they are not horizontal,
(ii) no two of them are parallel,
(iii) no three of the $h+s$ lines are concurrent,
then the number of regions formed by these $h+s$ lines is $1992$.

Answer: $(995,1),(176,10)$, and $(80,21)$.


## 1993 — 5

**Record:** `apm_1993_2c32ee`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1993_2c32ee.json.gz).

Let $P_{1}, P_{2}, \ldots, P_{1993}=P_{0}$ be distinct points in the $xy$-plane with the following properties:
(i) both coordinates of $P_{i}$ are integers, for $i=1,2, \ldots, 1993$;
(ii) there is no point other than $P_{i}$ and $P_{i+1}$ on the line segment joining $P_{i}$ with $P_{i+1}$ whose coordinates are both integers, for $i=0,1, \ldots, 1992$.
Prove that for some $i, 0 \leq i \leq 1992$, there exists a point $Q$ with coordinates ($q_{x}, q_{y}$) on the line segment joining $P_{i}$ with $P_{i+1}$ such that both $2q_{x}$ and $2q_{y}$ are odd integers.


## 1993 — 2

**Record:** `apm_1993_5590e4`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1993_5590e4.json.gz).

Find the total number of different integer values the function
$$
f(x) = [x] + [2x] + \left[\frac{5x}{3}\right] + [3x] + [4x]
$$
takes for real numbers $x$ with $0 \leq x \leq 100$.

Note: $[t]$ is the largest integer that does not exceed $t$.


## 1993 — 3

**Record:** `apm_1993_fd5e4d`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1993_fd5e4d.json.gz).

Let
$$
f(x) = a_{n} x^{n} + a_{n-1} x^{n-1} + \cdots + a_{0} \quad \text{and} \quad g(x) = c_{n+1} x^{n+1} + c_{n} x^{n} + \cdots + c_{0}
$$
be non-zero polynomials with real coefficients such that $g(x) = (x + r) f(x)$ for some real number $r$. If $a = \max \left(\left|a_{n}\right|, \ldots, \left|a_{0}\right|\right)$ and $c = \max \left(\left|c_{n+1}\right|, \ldots, \left|c_{0}\right|\right)$, prove that $\frac{a}{c} \leq n+1$.


## 1994 — 1

**Record:** `apm_1994_71c0bd`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1994_71c0bd.json.gz).

Let $f: \mathbb{R} \rightarrow \mathbb{R}$ be a function such that
(i) For all $x, y \in \mathbb{R}$,
$$
f(x)+f(y)+1 \geq f(x+y) \geq f(x)+f(y)
$$
(ii) For all $x \in [0,1)$, $f(0) \geq f(x)$,
(iii) $-f(-1)=f(1)=1$.
Find all such functions $f$.


## 1994 — 5

**Record:** `apm_1994_721e00`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1994_721e00.json.gz).

You are given three lists $A$, $B$, and $C$. List $A$ contains the numbers of the form $10^{k}$ in base 10, with $k$ any integer greater than or equal to $1$. Lists $B$ and $C$ contain the same numbers translated into base $2$ and $5$ respectively:

| $A$ | $B$ | $C$ |
| :--- | :--- | :--- |
| 10 | 1010 | 20 |
| 100 | 1100100 | 400 |
| 1000 | 1111101000 | 13000 |
| $\vdots$ | $\vdots$ | $\vdots$ |

Prove that for every integer $n>1$, there is exactly one number in exactly one of the lists $B$ or $C$ that has exactly $n$ digits.


## 1999 — 2

**Record:** `apm_1999_d63d04`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1999_d63d04.json.gz).

Let $a_{1}, a_{2}, \cdots$ be a sequence of real numbers satisfying $a_{i+j} \leq a_{i}+a_{j}$ for all $i, j=1,2, \cdots$. Prove that
$$
a_{1}+\frac{a_{2}}{2}+\frac{a_{3}}{3}+\cdots+\frac{a_{n}}{n} \geq a_{n}
$$
for each positive integer $n$.


## 2002 — 1

**Record:** `apm_2002_ee5012`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2002_ee5012.json.gz).

Let $a_{1}, a_{2}, a_{3}, \ldots, a_{n}$ be a sequence of non-negative integers, where $n$ is a positive integer. Let
$$
A_{n} = \frac{a_{1} + a_{2} + \cdots + a_{n}}{n}
$$
Prove that
$$
a_{1}! a_{2}! \ldots a_{n}! \geq \left( \left\lfloor A_{n} \right\rfloor ! \right)^{n}
$$
where $\left\lfloor A_{n} \right\rfloor$ is the greatest integer less than or equal to $A_{n}$, and $a! = 1 \times 2 \times \cdots \times a$ for $a \geq 1$ (and $0! = 1$). When does equality hold?


## 2003 — 4

**Record:** `apm_2003_7dec2d`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2003_7dec2d.json.gz).

Let $a$, $b$, $c$ be the sides of a triangle, with $a + b + c = 1$, and let $n \geq 2$ be an integer. Show that
$$
\sqrt[n]{a^{n} + b^{n}} + \sqrt[n]{b^{n} + c^{n}} + \sqrt[n]{c^{n} + a^{n}} < 1 + \frac{\sqrt[n]{2}}{2}
$$


## 2003 — 1

**Record:** `apm_2003_e72335`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2003_e72335.json.gz).

Let $a, b, c, d, e, f$ be real numbers such that the polynomial
$$
p(x) = x^{8} - 4x^{7} + 7x^{6} + a x^{5} + b x^{4} + c x^{3} + d x^{2} + e x + f
$$
factorises into eight linear factors $x - x_{i}$, with $x_{i} > 0$ for $i = 1, 2, \ldots, 8$. Determine all possible values of $f$.


## 2004 — 1

**Record:** `apm_2004_1843da`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2004_1843da.json.gz).

Determine all finite nonempty sets $S$ of positive integers satisfying
$$
\frac{i+j}{(i, j)} \quad \text{is an element of } S \text{ for all } i, j \text{ in } S,
$$
where $(i, j)$ is the greatest common divisor of $i$ and $j$.


## 2005 — Problem 2

**Record:** `apm_2005_00a9c6`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2005_00a9c6.json.gz).

Let $a$, $b$ and $c$ be positive real numbers such that $a b c = 8$. Prove that
$$
\frac{a^{2}}{\sqrt{\left(1+a^{3}\right)\left(1+b^{3}\right)}} + \frac{b^{2}}{\sqrt{\left(1+b^{3}\right)\left(1+c^{3}\right)}} + \frac{c^{2}}{\sqrt{\left(1+c^{3}\right)\left(1+a^{3}\right)}} \geq \frac{4}{3}
$$


## 2005 — Problem 1

**Record:** `apm_2005_f8ae2c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2005_f8ae2c.json.gz).

Prove that for every irrational real number $a$, there are irrational real numbers $b$ and $b^{\prime}$ so that $a+b$ and $a b^{\prime}$ are both rational while $a b$ and $a+b^{\prime}$ are both irrational.


## 2008 — Problem 5

**Record:** `apm_2008_eadb1c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2008_eadb1c.json.gz).

Let $a$, $b$, $c$ be integers satisfying $0 < a < c - 1$ and $1 < b < c$. For each $k$, $0 \leq k \leq a$, let $r_{k}$, $0 \leq r_{k} < c$, be the remainder of $k b$ when divided by $c$. Prove that the two sets $\{r_{0}, r_{1}, r_{2}, \ldots, r_{a}\}$ and $\{0, 1, 2, \ldots, a\}$ are different.


## 2008 — Problem 4

**Record:** `apm_2008_ec38c0`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2008_ec38c0.json.gz).

Consider the function $f: \mathbb{N}_0 \rightarrow \mathbb{N}_0$, where $\mathbb{N}_0$ is the set of all non-negative integers, defined by the following conditions:
(i) $f(0)=0$,
(ii) $f(2 n)=2 f(n)$ and
(iii) $f(2 n+1)=n+2 f(n)$ for all $n \geq 0$.

a. Determine the three sets $L:=\{n \mid f(n)<f(n+1)\}$, $E:=\{n \mid f(n)=f(n+1)\}$, and $G:=\{n \mid f(n)>f(n+1)\}$.

b. For each $k \geq 0$, find a formula for $a_k:=\max \left\{f(n): 0 \leq n \leq 2^k\right\}$ in terms of $k$.


## 2009 — Problem 1

**Record:** `apm_2009_dd163e`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2009_dd163e.json.gz).

Consider the following operation on positive real numbers written on a blackboard:
Choose a number $r$ written on the blackboard, erase that number, and then write a pair of positive real numbers $a$ and $b$ satisfying the condition $2 r^{2}=a b$ on the board.
Assume that you start out with just one positive real number $r$ on the blackboard, and apply this operation $k^{2}-1$ times to end up with $k^{2}$ positive real numbers, not necessarily distinct. Show that there exists a number on the board which does not exceed $k r$.


## 2010 — 5

**Record:** `apm_2010_d1fcee`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2010_d1fcee.json.gz).

Find all functions $f$ from the set $\{\mathbf{R}\}$ of real numbers into $\{\mathbf{R}\}$ which satisfy for all $x, y, z \in \{\mathbf{R}\}$ the identity
$$
f(f(x)+f(y)+f(z))=f(f(x)-f(y))+f(2 x y+f(z))+2 f(x z-y z)
$$


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


## 2016 — 5

**Record:** `apm_2016_e3d4e1`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2016_e3d4e1.json.gz).

Find all functions $f: \mathbb{R}^{+} \rightarrow \mathbb{R}^{+}$ such that
$$
(z+1) f(x+y) = f(x f(z) + y) + f(y f(z) + x)
$$
for all positive real numbers $x$, $y$, $z$.


## 2018 — 5

**Record:** `mkd_2018_b1584d`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2018_b1584d.json.gz).

Find all polynomials $P(x)$ with integer coefficients such that for all real numbers $s$ and $t$, if $P(s)$ and $P(t)$ are both integers, then $P(st)$ is also an integer.


## 2018 — 2

**Record:** `mkd_2018_ea8ca8`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2018_ea8ca8.json.gz).

Let $f(x)$ and $g(x)$ be given by
$$
f(x) = \frac{1}{x} + \frac{1}{x-2} + \dots + \frac{1}{x-2018}
$$
and
$$
g(x) = \frac{1}{x-1} + \frac{1}{x-3} + \dots + \frac{1}{x-2017}.
$$
Prove that
$$
|f(x) - g(x)| > 2
$$
for any non-integer real number $x$ satisfying $0 < x < 2018$.


## 2020 — 4

**Record:** `apm_2020_2b1cf6`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2020_2b1cf6.json.gz).

Let $\mathbb{Z}$ denote the set of all integers. Find all polynomials $P(x)$ with integer coefficients that satisfy the following property:
For any infinite sequence $a_{1}, a_{2}, \ldots$ of integers in which each integer in $\mathbb{Z}$ appears exactly once, there exist indices $i<j$ and an integer $k$ such that $a_{i}+a_{i+1}+\cdots+a_{j}=P(k)$.


## 2020 — 2

**Record:** `apm_2020_9793f2`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2020_9793f2.json.gz).

Show that $r=2$ is the largest real number $r$ which satisfies the following condition:
If a sequence $a_{1}, a_{2}, \ldots$ of positive integers fulfills the inequalities
$$
a_{n} \leq a_{n+2} \leq \sqrt{a_{n}^{2}+r a_{n+1}}
$$
for every positive integer $n$, then there exists a positive integer $M$ such that $a_{n+2}=a_{n}$ for every $n \geq M$.


## 2022 — 5

**Record:** `apm_2022_1b0270`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2022_1b0270.json.gz).

Let $a, b, c, d$ be real numbers such that $a^{2}+b^{2}+c^{2}+d^{2}=1$. Determine the minimum value of $(a-b)(b-c)(c-d)(d-a)$ and determine all values of $(a, b, c, d)$ such that the minimum value is achieved.


## 2022 — 3

**Record:** `apm_2022_a90b58`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2022_a90b58.json.gz).

Find all positive integers $k<202$ for which there exists a positive integer $n$ such that
$$
\left\{\frac{n}{202}\right\}+\left\{\frac{2 n}{202}\right\}+\cdots+\left\{\frac{k n}{202}\right\}=\frac{k}{2}
$$
where $\{x\}$ denote the fractional part of $x$.
Note: $\{x\}$ denotes the real number $k$ with $0 \leq k<1$ such that $x-k$ is an integer.


## 2023 — 4

**Record:** `apm_2023_44bc62`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2023_44bc62.json.gz).

Let $c>0$ be a given positive real and $\mathbb{R}_{>0}$ be the set of all positive reals. Find all functions $f: \mathbb{R}_{>0} \rightarrow \mathbb{R}_{>0}$ such that
$$
f((c+1) x+f(y))=f(x+2 y)+2 c x \quad \text{ for all } x, y \in \mathbb{R}_{>0} .
$$


## 2024 — 3

**Record:** `apm_2024_531576`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2024_531576.json.gz).

Let $n$ be a positive integer and $a_{1}, a_{2}, \ldots, a_{n}$ be positive real numbers. Prove that
$$
\sum_{i=1}^{n} \frac{1}{2^{i}}\left(\frac{2}{1+a_{i}}\right)^{2^{i}} \geq \frac{2}{1+a_{1} a_{2} \ldots a_{n}}-\frac{1}{2^{n}} .
$$


## 2025 — 2

**Record:** `apm_2025_0453f0`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2025_0453f0.json.gz).

Let $\alpha$ and $\beta$ be positive real numbers. Emerald makes a trip in the coordinate plane, starting off from the origin $(0,0)$. Each minute she moves one unit up or one unit to the right, restricting herself to the region $|x-y|<2025$, in the coordinate plane. By the time she visits a point ( $x, y$ ) she writes down the integer $\lfloor x \alpha+y \beta\rfloor$ on it. It turns out that Emerald wrote each non-negative integer exactly once. Find all the possible pairs $(\alpha, \beta)$ for which such a trip would be possible.


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

## 2004 — 1.

**Record:** `rou_2004_382714`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2004_382714.json.gz).

Şirul de numere reale $a_{0}, a_{1}, \ldots, a_{n}, \ldots$ satisface relaţia
$$
a_{m+n} + a_{m-n} - m + n - 1 = \frac{1}{2}\left(a_{2m} + a_{2n}\right)
$$
pentru orice numere naturale $m$ şi $n$, $m \geq n$.
Dacă $a_{1} = 3$, aflaţi $a_{2004}$.


## 2004 — Problema 2

**Record:** `rou_2004_97964e`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2004_97964e.json.gz).

Pentru orice număr natural nenul $n$, suma $1+\frac{1}{2}+\ldots+\frac{1}{n}$ se scrie sub forma $\frac{p_{n}}{q_{n}}$ unde $p_{n}$ şi $q_{n}$ sunt numere naturale prime între ele.

a. Arătați că $p_{67}$ nu se divide cu 3.

b. Determinați toate numerele naturale nenule $n$, pentru care $p_{n}$ este divizibil cu 3.


## 2007 — 3

**Record:** `grc_2007_ef47a3`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/greece/grc_2007_ef47a3.json.gz).

Find all positive integers $n$ such that there is a permutation $\sigma$ of the set $\{1,2,...,n\}$ for which $\sqrt{\sigma(1)+\sigma(2)+\dots+\sigma(n)}$ is a rational number.

*: A permutation of the set $\{1,2,...,n\}$ is a one-to-one function of this set to itself.*


## 2008 — 4

**Record:** `mkd_2008_0174ff`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_0174ff.json.gz).

Mile imagined a number and said: "If I multiply the number by two and add this product to the half of the number I will get a number that is for 26 bigger than the third of the imagined number." What number did Mile imagine?


## 2008 — 1

**Record:** `mkd_2008_017711`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_017711.json.gz).

In the right triangle $\lg \frac{a-b}{2} = \frac{1}{2}(\lg a + \lg b - \lg 2)$, where $a > b$, $a, b$ are the sides of the triangle. Find the angles of the triangle.


## 2008 — 2

**Record:** `mkd_2008_059cbe`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_059cbe.json.gz).

Prove that for every real root $x$ of $x^2 + p x + q = 0$, where $p, q \in \mathbb{R}$ and $a > 0$ we have $x \ge \frac{4q - (p + a)^2}{4a}$.


## 2008 — 3. (B)

**Record:** `mkd_2008_06715b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_06715b.json.gz).

Solve the system:
$$
\begin{cases}
x(y+z) = 35 \\
y(z+x) = 32 \\
z(x+y) = 27
\end{cases}
$$


## 2008 — 5

**Record:** `mkd_2008_06a626`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_06a626.json.gz).

Four boys Andrej, Bojan, Vasko and Goce are collecting post stamps. Andrej has as many post stamps as Bojan and Vasko have together. Goce has five times less post stamps than Andrej, and Bojan has four times more post stamps than Vasko. If they together have 5016 post stamps, how many post stamps each of the four boys has?


## 2008 — 2

**Record:** `mkd_2008_178502`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_178502.json.gz).

Maja went to the bookstore to buy two books. The price of the first book was $65\%$ and the price of the other $57.5\%$ from the money that Maja had with her. She needed additional $45$ denars to buy the two books. How much money did Maja have with her?


## 2008 — 2

**Record:** `mkd_2008_2127bc`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_2127bc.json.gz).

Let $x + y + z = a$ and $\frac{1}{x} + \frac{1}{y} + \frac{1}{z} = \frac{1}{a}$, for $x, y, z, a \in \mathbb{R}$. Prove that at least one of $x, y, z$ is equal to $a$.


## 2008 — 1

**Record:** `mkd_2008_24232c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_24232c.json.gz).

For which values of $x$ and $y$, the difference of $\frac{2x+15}{8}$ and $1\frac{1}{3} \cdot (y-1)$ will be 3 times smaller than $2 \cdot (5-2y)$ and $\frac{x+5}{2}$ will be for $0.125$ bigger than $3y$?


## 2008 — 3

**Record:** `mkd_2008_251f69`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_251f69.json.gz).

The difference of two complementary angles $\alpha$ and $\beta$ is $20^\circ 52'$. Determine $\alpha$ and $\beta$.


## 2008 — 4

**Record:** `mkd_2008_290b9f`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_290b9f.json.gz).

Ilina ate $\frac{1}{5}$ plus three of the candies from the bag. From the remaining candies she ate $\frac{1}{5}$ plus five the next day. The third day she ate the remaining 15 candies. How many candies were there in the bag in the beginning?


## 2008 — 2

**Record:** `mkd_2008_2b2e13`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_2b2e13.json.gz).

a) Find the smallest positive integer which multiplied by $2520$ gives a square of a positive integer.

b) Prove that the sum of two consecutive odd integers is divisible with $4$.


## 2008 — 5

**Record:** `mkd_2008_2d37d3`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_2d37d3.json.gz).

One rectangle has side lengths $a$ cm and $b$ cm. If the side with length $a$ cm is enlarged by $b$ cm and the side with length $b$ cm is enlarged by $a$ cm then the resulting square has area of $100\,\mathrm{cm}^2$. Determine the rectangle that satisfies this condition with smallest area if its side lengths are positive integers.


## 2008 — 3

**Record:** `mkd_2008_30218d`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_30218d.json.gz).

$2n$ ($n > 1$) points are given in the plane. Line $p$ lies in the plane and does not cross the given points. Prove that this line cuts no more than $n^2$ segments with end in the given points.


## 2008 — 3

**Record:** `mkd_2008_3ec66c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_3ec66c.json.gz).

Let $n$ be a positive integer. Does $(2n-3)(2n-1)(2n+1)(2n+3)+16$ equal the square of a positive integer? Does the number $2005 \times 2007 \times 2009 \times 2011 + 16$ equal the square of a positive integer?


## 2008 — 1

**Record:** `mkd_2008_487682`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_487682.json.gz).

Find the number by which the sum of the numbers $54863$ and $30608$ has to be decreased in order to obtain their difference?


## 2008 — 4

**Record:** `mkd_2008_523d54`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_523d54.json.gz).

Let $c$ be a positive integer. The sequence $a_1, a_2, \dots, a_n, \dots$ is defined by $a_1 = c$, and $a_{n+1} = a_n^2 + a_n + c^3$, for every positive integer $n$. Find all values of $c$ for which there exist some integers $k \ge 1$ and $m \ge 2$, such that $a_k^2 + c^3$ is the $m$th power of some positive integer.


## 2008 — 1. (AB)

**Record:** `mkd_2008_52dd2b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_52dd2b.json.gz).

Find $(x+y)^2$, if $\frac{2}{x} - \frac{2}{y} = 1$ and $y-x=1$.


## 2008 — 2

**Record:** `mkd_2008_53b43c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_53b43c.json.gz).

If one of the sides of a square is increased two times and the other one is increased by $22\text{ mm}$, then the new rectangle has a perimeter that is $2000\text{ mm}$ greater than the perimeter of the square. What is the side length of the square?


## 2008 — 4. (AB)

**Record:** `mkd_2008_5808cf`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_5808cf.json.gz).

Prove that if $2a_m = a_n$, then $a_{2m-n}$ is a perfect square, where $a_n = 1+2+...+n$, for every $n \in \mathbb{N}$.


## 2008 — 3

**Record:** `mkd_2008_5d913f`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_5d913f.json.gz).

One school has less than $400$ students in $6$th grade. They are divided in several classes. Six of them have equal number of students and together they have more than $150$ students. In the remaining classes there are $15\%$ more students than in these six classes together. How many students of $6$th grade are there in the school?


## 2008 — 3. (B)

**Record:** `mkd_2008_5f4949`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_5f4949.json.gz).

Prove that if $n$ is an odd natural number, then $n^3 + 3n^2 - n - 3$ is divisible by 48.


## 2008 — 1. (A)

**Record:** `mkd_2008_60b4d0`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_60b4d0.json.gz).

The sequence $49$, $4489$, $444889$, ... is given so that the number $48$ is put in the middle of the preceding term. Prove that every term in the sequence is perfect square.


## 2008 — 2

**Record:** `mkd_2008_63a31b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_63a31b.json.gz).

a)
$$
1\frac{5}{8} + \left(1\frac{1}{2} + \left(\left(1\frac{1}{2} - \frac{1}{6}\right) \cdot \left(\frac{1}{3} + \frac{1}{4}\right) + 1\right)\right) : \frac{2}{3}
$$

b)
$$
0,6 : \frac{1\frac{1}{2} + 0,5 \cdot 2\frac{1}{2} - 0,25}{15 - 0,5}
$$


## 2008 — 2

**Record:** `mkd_2008_640265`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_640265.json.gz).

One student was multiplying two numbers. During the multiplication he switched the last digit of the first number, which was $4$, with $1$. So he obtained $525$ as a result instead of $600$. Which numbers did the student multiply?


## 2008 — 1

**Record:** `mkd_2008_6b0e94`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_6b0e94.json.gz).

Stefan, Filip and Nikola went on an excursion. They took with them $222$ denars. Stefan spent $\frac{1}{3}$ of his money, Filip spent $\frac{1}{5}$ of his and Nikola spent $\frac{7}{15}$ of his. On the end of the excursion they had equal amount of money. How much money did each of them take for the excursion?


## 2008 — 3

**Record:** `mkd_2008_6f2f5a`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_6f2f5a.json.gz).

Find all the real functions $f: \mathbb{R} \to \mathbb{R}$ such that
$$
f(x^2 - y^2) = (x - y)[f(x) + f(y)]
$$


## 2008 — 1

**Record:** `mkd_2008_7ac7f5`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_7ac7f5.json.gz).

The ratios $\frac{3a5b}{36}$ and $\frac{4c7d}{45}$ are positive integers, where $a, b, c, d$ are digits. Order all numbers of this kind by size.


## 2008 — 2

**Record:** `mkd_2008_8d0ad8`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_8d0ad8.json.gz).

Does there exist a sequence $a_1, a_2, \ldots, a_n, \ldots$ of positive real numbers satisfying both of the following conditions:

$\sum_{i=1}^{n} a_i \le n^2$, for every positive integer $n$;

$\sum_{i=1}^{n} \frac{1}{a_i} \le 2008$, for every positive integer $n$?


## 2008 — 4

**Record:** `mkd_2008_9477b5`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_9477b5.json.gz).

The book that Marko reads has $242$ pages. The first day he has read $22$ pages. During the second day he has read $4$ pages more than the first and the same during the third day. How many days will Marko need to finish the book if he reads two pages more than the third day each day from the fourth day onward?


## 2008 — 3

**Record:** `mkd_2008_97b838`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_97b838.json.gz).

The teacher ordered 20 students from one class in a row and gave 800 candies to them. Every student had to calculate the ratio $\frac{x}{x+2k-1}$, where $x$ is the number of candies that he got and $k$ is the number of his position in the row, counting from left to right. After calculating they all got the same result. How many candies were given to the student that was twelfth in the row?


## 2008 — 4. (B)

**Record:** `mkd_2008_9e3d8c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_9e3d8c.json.gz).

Solve the equation $\log_{3x+4}(2x+1)^2 + \log_{2x+1}(6x^2 + 11x + 4) = 4$.


## 2008 — 2. (B)

**Record:** `mkd_2008_a4fb7b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_a4fb7b.json.gz).

Solve the equation $\frac{x-1}{x} + \frac{x-2}{x} + \dots + \frac{1}{x} = \frac{3x-20}{4}$ in $\mathbb{N}$.


## 2008 — 1. (B)

**Record:** `mkd_2008_acffae`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_acffae.json.gz).

Find the value of $y$ so that $\sqrt{y^2 + 2y + 1}$, $\frac{y^2 + 3y - 1}{3}$, $y-1$ are consecutive terms in the arithmetic progression.


## 2008 — 3

**Record:** `mkd_2008_af1550`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_af1550.json.gz).

In the first barrel there is $5$ hl and $25$ l wine. In the second barrel there is $3$ times more wine than in the first one and in the third there is $1$ hl and $75$ l less wine than in the first one. How much wine is there in each of the barrels?


## 2008 — 3. (A)

**Record:** `mkd_2008_af49f5`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_af49f5.json.gz).

The roots of the quadratic equation $x^2 + p x + q = 0$ are integers. Find the numbers $p$ and $q$ and the roots of the equation, if $p + q = 198$.


## 2008 — 2

**Record:** `mkd_2008_afd3e2`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_afd3e2.json.gz).

A passenger wanted to know the speed of the bus in which he was traveling, so he looked through the window and saw on a road sign (denoting the distance from the town from where he started his traveling) two-digit number. After one hour drive he saw on another road sign a three-digit number written with the same two digits as one hour before but in opposite order and a zero between them. The passenger evaluated the speed of the bus and fell asleep. Two hours later he woke up and saw on a road sign three-digit number with first and last digit same as the number two hours ago but different middle digit. If we know that the bus had constant speed determine the speed and the numbers which the passenger saw on the road signs.


## 2008 — 4

**Record:** `mkd_2008_bdf736`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_bdf736.json.gz).

From the digits $3$, $7$, $1$, $9$, $0$ and $4$ Mila formed the biggest and the smallest six-digit number using each digit exactly once in each of the two numbers. Then she reduced their difference $9$ times. Which number did she get?


## 2008 — 4

**Record:** `mkd_2008_bfdaf7`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_bfdaf7.json.gz).

Find all triples of positive integers $(x, y, z)$ such that
$$
xyz + xy + yz + zx + x + y + z = 243.
$$


## 2008 — 4. (A)

**Record:** `mkd_2008_c8a845`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_c8a845.json.gz).

Solve the system
$$
\begin{cases}
x^{\log y} + \sqrt{y^{\log x}} = 110 \\
xy = 1000
\end{cases}
$$


## 2008 — 1

**Record:** `mkd_2008_c9c363`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_c9c363.json.gz).

In a school there are $32$ classes. Six of them have $29$ students each, eight of them have $30$ students each, two of them have $31$ students each and the rest have $32$ students each. How many students are there in the school?


## 2008 — 3. (AB)

**Record:** `mkd_2008_cb8870`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_cb8870.json.gz).

Prove that if $\left|\frac{a+b}{2}\right| + \left|\frac{a-b}{2}\right| < c$, for $a, b, c \in \mathbb{R}$, then $|a| < c$ and $|b| < c$.


## 2008 — 3

**Record:** `mkd_2008_d603eb`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_d603eb.json.gz).

There were 25 birds on two branches. After a while 5 birds from the first branch flew over to the second and after a while longer 7 birds from the second flew away. In that moment on the first branch there were twice as many birds than on the second. How many birds were there on each of the two branches in the beginning?


## 2008 — 3. (B)

**Record:** `mkd_2008_d79f9b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_d79f9b.json.gz).

In a square shaped area on the ground with side length $12\text{ m}$ a cylindrical hole is dug with diameter $8\text{ m}$. The dug soil is equally allotted on the square shaped area, outside of the hole, and then is pressed as much as was before the digging. How deep should be the dug in order the hole to be deep?


## 2008 — 1

**Record:** `mkd_2008_d9d0d9`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_d9d0d9.json.gz).

During three hours a driver with a car has driven $180\,km$. During the first hour he has driven $0.375$ from the whole distance and during the second hour he has driven $0.9$ from the distance that he had driven during the first hour. What distance has the driver driven during the third hour?


## 2008 — 3

**Record:** `mkd_2008_ddaaeb`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_ddaaeb.json.gz).

a) Calculate $(-3ab + a^2 - 1) - (-4a^2 + 5ab - 7) + 2(a - 2b)(a + b)$

b) If $A = 7x^2$ and $B = -2y$ calculate $(A+B)^2$ and $(A+B)(A-B)$.


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


## 2008 — 4

**Record:** `mkd_2008_f3b3c2`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_f3b3c2.json.gz).

Let $1*2*3*4*5*6*7*8*9=0$ be a given equality. Is it possible to substitute some of the $*$ with $+$ and the others with $-$ to obtain a correct equality?


## 2008 — 1

**Record:** `mkd_2008_f95407`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_f95407.json.gz).

Determine the sum of all odd 3-digit numbers whose product of digits is equal to $140$.


## 2008 — 4

**Record:** `mkd_2008_fbf396`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_fbf396.json.gz).

Find all three digit numbers equal to the sum of the factorials of their digits.


## 2008 — 4. (A)

**Record:** `mkd_2008_fd5b30`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_fd5b30.json.gz).

Prove that if $(x+\sqrt{x^2+1}) \cdot (y+\sqrt{y^2+1}) = 1$ then $x+y=0$.


## 2009 — 4

**Record:** `grc_2009_78d09d`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/greece/grc_2009_78d09d.json.gz).

Let $\mathbb{N}^* = \{1,2,3,...\}$ be the set of positive integers. Find all functions $f: \mathbb{N}^* \rightarrow \mathbb{N}^*$ such that
$$
f(f(m)^2 + 2f(n)^2) = m^2 + 2n^2, \text{ for all } m, n \in \mathbb{N}^*.
$$


## 2009 — 2АБ.

**Record:** `mkd_2009_24150b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_24150b.json.gz).

Провери ја точноста на равенството:
$$
\sum_{k=1}^{n} \frac{(-1)^{k+1}}{k} \binom{n}{k} = 1 + \frac{1}{2} + \frac{1}{3} + \dots + \frac{1}{n},
$$


## 2009 — 3А.

**Record:** `mkd_2009_44ad67`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_44ad67.json.gz).

Реши ја равенката $\left(\frac{x^3 + x}{3}\right)^3 + \frac{x^3 + x}{3} = 3x$.


## 2009 — 1Б.

**Record:** `mkd_2009_4eac92`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_4eac92.json.gz).

Определи ги комплексните броеви $z$ за кои
$$
|z| = \frac{1}{|z|} = |z - 1|.
$$


## 2009 — 2АБ.

**Record:** `mkd_2009_5450be`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_5450be.json.gz).

За бројот $a$, е исполнето равенството $a + \frac{1}{a} = 1$. Пресметaj ја вредноста на $a^5 + \frac{1}{a^5}$.


## 2009 — 3А.

**Record:** `mkd_2009_573297`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_573297.json.gz).

Дадени се 21 плочка во облик на квадратче, со иста димензија. На четири плочки е запишан бројот 1; на две плочки е запишан бројот 2; на седум плочки е запишан бројот 3; на 8 плочки е запишан бројот 4. Користејќи 20 од тие плочки, Димитар формирал правоаголник со димензии 4 на 5. За формираниот правоаголник збирот на броевите во секоја редица е иста, и збирот на броевите во секоја колона е иста. Кој број стои на неискористената плочка?


## 2009 — 1А.

**Record:** `mkd_2009_5f7681`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_5f7681.json.gz).

Определи ги сите природни броеви $n$ за кои бројот $z = \left(\frac{3+i}{2-i}\right)^n$ е реален.


## 2009 — 4.

**Record:** `mkd_2009_9519f9`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_9519f9.json.gz).

Нека $a, b, c$ се позитивни реални броеви за кои важи $ab + bc + ca = 1/3$. Да се докаже неравенството
$$
\frac{a}{a^2 - bc + 1} + \frac{b}{b^2 - ca + 1} + \frac{c}{c^2 - ab + 1} \ge \frac{1}{a + b + c}
$$


## 2009 — 1Б.

**Record:** `mkd_2009_a0c7fc`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_a0c7fc.json.gz).

Нека $a$ и $b$ се природни броеви. Докажи дека $a^2 + ab + b^2$ е делител на бројот $(a+b)^6 - a^6$.


## 2009 — 3Б.

**Record:** `mkd_2009_d6daf6`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_d6daf6.json.gz).

Да се провери точноста на равенството
$$
\operatorname{tg} \alpha + 2 \operatorname{tg} 2\alpha + 2^2 \operatorname{tg} 2^2 \alpha + \dots + 2^n \operatorname{tg} 2^n \alpha = \operatorname{ctg} \alpha - 2^{\eta+1} \operatorname{ctg} 2^{\eta+1} \alpha.
$$


## 2009 — 1Б.

**Record:** `mkd_2009_db9b38`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_db9b38.json.gz).

Реши ја равенката
$$
4^{\log_{10} x} - 32 + x^{\log_{10} 4} = 0.
$$


## 2009 — 3Б.

**Record:** `mkd_2009_dc4f50`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_dc4f50.json.gz).

Реши го системот равенки
$$
\begin{cases}
x + y = z \\
x^2 + y^2 = z \\
x^3 + y^3 = z
\end{cases}
$$


## 2009 — 4Б.

**Record:** `mkd_2009_e8804f`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_e8804f.json.gz).

Дадена е функцијата $f: \mathbb{R} \rightarrow \mathbb{R}$ таква што
$$
f(x+1)+f(x-1)=\sqrt{2}f(x).
$$
Докажи дека $f$ е периодична функција.


## 2009 — 1А.

**Record:** `mkd_2009_eb1908`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_eb1908.json.gz).

Определи ги сите цели броеви $x$, за кои $\log_2(x^2 - 4x - 1)$ е исто така цел број.


## 2009 — 3Б.

**Record:** `mkd_2009_ee8242`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_ee8242.json.gz).

Во равенството $25!=15\ 511 \times 10\ 043\ 330\ \text{у}85\ 984\ z00\ 000$ определи ги цифрите $x,y$ и $z$ за да тоа е точно.


## 2009 — 1АБ.

**Record:** `mkd_2009_f6a112`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_f6a112.json.gz).

Аритметичката прогресија се состои од цели броеви. Збирот на првите $n$ членови на прогресијата е степен на бројот 2. Докажи дека и $n$ е степен на бројот 2.


## 2010 — Problem 1.

**Record:** `mkd_2010_92c748`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2010_92c748.json.gz).

Let $a$, $b$, $c$ be positive real numbers. Prove that
$$
\frac{a^2 b (b-c)}{a+b} + \frac{b^2 c (c-a)}{b+c} + \frac{c^2 a (a-b)}{c+a} \geq 0.
$$


## 2011 — 4

**Record:** `mkd_2011_246059`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2011_246059.json.gz).

Find all functions $f: \mathbb{R} \to \mathbb{R}$ such that:
$$
f(x + y f(x)) = f(f(x)) + x f(y)
$$


## 2011 — 2

**Record:** `mkd_2011_3de3d8`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2011_3de3d8.json.gz).

Given real numbers $x, y, z$ such that $x + y + z = 0$, show that
$$
\frac{x(x+2)}{2x^2+1} + \frac{y(y+2)}{2y^2+1} + \frac{z(z+2)}{2z^2+1} \ge 0.
$$
When does equality hold?


## 2012 — 3

**Record:** `mkd_2012_683110`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2012_683110.json.gz).

Let $n$ be a positive integer. Let $P_n = \{2^n, 2^{n-1} \cdot 3, 2^{n-2} \cdot 3^2, \dots, 3^n\}$. For each subset $X$ of $P_n$, we write $S_X$ for the sum of all elements of $X$, with the convention that $S_\emptyset = 0$ where $\emptyset$ is the empty set. Suppose that $y$ is a real number with $0 \le y \le 3^{n+1} - 2^{n+1}$.
Prove that there is a subset $Y$ of $P_n$ such that $0 \le y - S_Y < 2^n$.


## 2012 — 2

**Record:** `mkd_2012_857951`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2012_857951.json.gz).

$$
\sum_{\text{cyc}} (x+y)\sqrt{(z+x)(z+y)} \ge 4(xy+yz+zx)
$$
for all positive real numbers $x$, $y$, $z$.


## 2012 — 4

**Record:** `mkd_2012_f9bf27`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2012_f9bf27.json.gz).

Let $\mathbb{Z}^+$ be the set of all positive integers. Find all functions $f: \mathbb{Z}^+ \to \mathbb{Z}^+$ such that $f(n!) = f(n)!$, and $m-n$ divides $f(m)-f(n)$ for all distinct positive integers $m$ and $n$.


## 2013 — 7

**Record:** `bmo_2013_654e0d`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2013_654e0d.json.gz).

Suppose that $k$ is a positive integer. A bijective map $f: \mathbb{Z} \to \mathbb{Z}$ is said to be $k$-jumpy if $|f(z) - z| \le k$ for all integers $z$.
Is it that case that for every $k$, each $k$-jumpy map is a composition of 1-jumpy maps?
*It is well known that this is the case when the support of the map is finite.*


## 2013 — 2

**Record:** `bmo_2013_84acf9`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2013_84acf9.json.gz).

Some squares of an $n \times n$ chessboard have been marked ($n \in \mathbb{N}^*$). Prove that if the number of marked squares is at least $n(\sqrt{n} + \frac{1}{2})$, then there exists a rectangle whose vertices are centers of marked squares.


## 2013 — Problem 3

**Record:** `rou_2013_b362ad`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2013_b362ad.json.gz).

Let $S$ be the set of positive real numbers. Find all functions $f: S^{3} \rightarrow S$ such that, for all positive real numbers $x, y, z$ and $k$, the following three conditions are satisfied:
(a) $x f(x, y, z)=z f(z, y, x)$,
(b) $f\left(x, y k, k^{2} z\right)=k f(x, y, z)$,
(c) $f(1, k, k+1)=k+1$.

Problem:
Fie $S$ mulţimea numerelor reale strict pozitive. Să se găsească toate funcţiile $f: S^{3} \rightarrow S$ care satisfac condiţiile
(a) $x f(x, y, z)=z f(z, y, x)$,
(b) $f\left(x, y k, k^{2} z\right)=k f(x, y, z)$,
(c) $f(1, k, k+1)=k+1$.
pentru orice numere reale strict pozitive $x, y, z$ şi $k$.


## 2014 — 1

**Record:** `mkd_2014_3acc00`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2014_3acc00.json.gz).

Let $x$, $y$ and $z$ be positive real numbers such that $xy + yz + zx = 3xyz$. Prove that
$$
x^2 y + y^2 z + z^2 x \geq 2(x + y + z) - 3
$$


## 2014 — 4

**Record:** `mkd_2014_9ea0c9`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2014_9ea0c9.json.gz).

Let $n$ be a positive integer. A regular hexagon with side length $n$ is divided into equilateral triangles with side length $1$ by lines parallel to its sides.
Find the number of regular hexagons all of whose vertices are along the vertices of the equilateral triangles.


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


## 2015 — NT1.

**Record:** `bmo_2015_6abd41`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2015_6abd41.json.gz).

Let $n$ be a given even positive integer. First John writes the consecutive square numbers $1^2, 3^2, \dots, (2n-1)^2$ on the blackboard. Then he picks some three of them, say $a_1, a_2, a_3$, erases them and writes the number
$$
1 + \sum_{1 \le i < j \le 3} |a_i - a_j|
$$
on the blackboard. He continues this way replacing each time three of the numbers on the blackboard until only two numbers remain on it. Prove that the sum of the squares of the two remaining numbers is different from any of the numbers $1^2, 3^2, \dots, (2n-1)^2$ written initially on the blackboard.


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


## 2018 — 2

**Record:** `mkd_2018_881ec5`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2018_881ec5.json.gz).

Let $q$ be a positive rational number. Two ants are initially at the same point $X$ in the plane. In the $n$-th minute ($n=1,2,3,\ldots$) each of them chooses whether to walk due north, east, south or west and then walks the distance of $q^n$ meter. After a whole number of minutes, they are at the same point in the plane (not necessarily $X$), but have not taken exactly the same route within that time. Determine all possible values of $q$.



# BMO-SL source statements

## 2010 — NT1

**Record:** `bmo_2010_2df1d0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2010_2df1d0.json.gz).

Is it possible to partition the set of all integer numbers into ordered triples in such a way that, for every triple $(a, b, c)$ the number
$$
|a^3 b + b^3 c + c^3 a|
$$
be a perfect square?


## 2010 — C4

**Record:** `bmo_2010_76e4e6`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2010_76e4e6.json.gz).

Integers are written in the cells of a table $2010 \times 2010$. Adding $1$ to all the numbers in a row or in a column is called a *move*. We say that the table is *equilibrium* if one can obtain after finitely many moves a table in which all the numbers are equal.

a) Find the largest positive integer $n$, for which there exists an equilibrium table containing the numbers $2^0, 2^1, \dots, 2^n$.

b) For this $n$, find the maximal number that may be contained in such a table.


## 2010 — A4

**Record:** `bmo_2010_897051`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2010_897051.json.gz).

Let $n > 2$ be a positive integer. Consider all numbers $S$ of the form
$$
S = a_1 a_2 + a_2 a_3 + \dots + a_{k-1} a_k,
$$
with $k > 1$, and $a_i$ being positive integers such that $a_1 + a_2 + \dots + a_k = n$. Determine all numbers that can be represented in the given form.


## 2010 — C5

**Record:** `bmo_2010_8eb8ae`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2010_8eb8ae.json.gz).

A train consists of $2010$ wagons containing gold coins, all of the same shape. Any two coins have equal weight provided that they are in the same wagon, and differ in weight if they are in different ones. The weight of a coin is one of the positive reals $m_1 < m_2 < \dots < m_{2010}$. Each wagon is marked by a label with one of the numbers $m_1, m_2, \dots, m_{2010}$ (the numbers on different labels are different).
A controller has a pair of scales (allowing only to compare masses) at his disposal. During each measurement he can use an arbitrary number of coins from any of the wagons. The controller has the task to establish: if all labels show rightly the common weight of the coins in a wagon or if there exists at least one wrong label. What is the least number of measurements that the controller has to perform to accomplish his task?


## 2010 — A2

**Record:** `bmo_2010_ced32c`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2010_ced32c.json.gz).

Let the sequence $(a_n)_{n \in N^*}$ be given with $a_1 = 2$ and $a_{n+1} = a_n^2 - a_n + 1$. Find the minimum real number $L$ such that for every $k \in N^*$
$$
\sum_{i=1}^{k} \frac{1}{a_i} < L.
$$


## 2012 — A3

**Record:** `bmo_2012_3242cc`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2012_3242cc.json.gz).

Determine the maximum possible number of distinct real roots of a polynomial $P(x)$ of degree $2012$ with real coefficients satisfying the condition
$$
P(a)^3 + P(b)^3 + P(c)^3 \geq 3P(a)P(b)P(c)
$$
for all real numbers $a, b, c$ with $a + b + c = 0$.


## 2012 — N1

**Record:** `bmo_2012_46d8dc`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2012_46d8dc.json.gz).

A sequence $(a_n)_{n=1}^\infty$ of positive integers satisfies the condition $a_{n+1} = a_n + \tau(n)$ for all positive integers $n$ where $\tau(n)$ is the number of positive integer divisors of $n$. Determine whether two consecutive terms of this sequence can be perfect squares.


## 2012 — N2

**Record:** `bmo_2012_907bbf`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2012_907bbf.json.gz).

Let the sequences $(a_n)_{n=1}^\infty$ and $(b_n)_{n=1}^\infty$ satisfy $a_0 = b_0 = 1$, $a_n = 9a_{n-1} - 2b_{n-1}$ and $b_n = 2a_{n-1} + 4b_{n-1}$ for all positive integers $n$. Let $c_n = a_n + b_n$ for all positive integers $n$. Prove that there do not exist positive integers $k, r, m$ such that $c_r^2 = c_k c_m$.


## 2012 — A5

**Record:** `bmo_2012_f7e2ed`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2012_f7e2ed.json.gz).

Let $N$ be a nonnegative integer and let $f, g: \mathbb{Z} \to [0, \infty)$ be functions such that $f(n) = g(n) = 0$ for all $|n| \geq N$ where $\mathbb{Z}$ is the set of all integers. Define $h: \mathbb{Z} \to [0, \infty)$ by
$$
h(n) = \max \{f(k)g(n-k) : k \in \mathbb{Z}\}
$$
for all $n \in \mathbb{Z}$. Prove that
$$
\sum_{n \in \mathbb{Z}} h(n) \geq \left( \sum_{n \in \mathbb{Z}} (f(n))^p \right)^{1/p} \left( \sum_{n \in \mathbb{Z}} (g(n))^q \right)^{1/q}
$$
for all positive real numbers $p$ and $q$ satisfying $1/p + 1/q = 1$.


## 2014 — A6

**Record:** `bmo_2014_2198db`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_2198db.json.gz).

The sequence $a_0, a_1, \dots$ is defined by the initial conditions $a_0 = 1$, $a_1 = 6$ and the recursion $a_{n+1} = 4a_n - a_{n-1} + 2$ for $n > 1$. Prove that $a_{2^k-1}$ has at least three prime factors for every positive integer $k > 3$.


## 2014 — A5

**Record:** `bmo_2014_64e0c9`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_64e0c9.json.gz).

Let $n \in \mathbb{N}$, $n > 2$, and suppose $a_1, a_2, \dots, a_{2n}$ is a permutation of the numbers $1, 2, \dots, 2n$ such that $a_1 < a_3 < \dots < a_{2n-1}$ and $a_2 > a_4 > \dots > a_{2n}$. Prove that
$$
(a_1 - a_2)^2 + (a_3 - a_4)^2 + \dots + (a_{2n-1} - a_{2n})^2 > n^3.
$$


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


## 2014 — C3

**Record:** `bmo_2014_96bc5b`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_96bc5b.json.gz).

Consider a lattice of side length $1$ equilateral triangles forming a regular hexagon of side length $n$. Show that the number of ways of simultaneously selecting six vertices of the lattice to form the vertices of a regular hexagon is a perfect square.


## 2014 — A3

**Record:** `bmo_2014_96ebbd`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_96ebbd.json.gz).

The sequence $a_1, a_2, a_3, \dots$ is defined by $a_1 = a_2 = 1$, $a_{2n+1} = 2a_{2n} - a_n$ and $a_{2n+2} = 2a_{2n+1}$ for $n \in \mathbb{N}$. Prove that if $n > 3$ and $n - 3$ is divisible by 8 then $a_n$ is divisible by 5.


## 2014 — A4

**Record:** `bmo_2014_9b9d0d`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_9b9d0d.json.gz).

Let $m_1$, $m_2$, $m_3$, $n_1$, $n_2$ and $n_3$ be positive real numbers such that
$$
(m_1 - n_1)(m_2 - n_2)(m_3 - n_3) = m_1 m_2 m_3 - n_1 n_2 n_3.
$$
Prove that
$$
(m_1 + n_1)(m_2 + n_2)(m_3 + n_3) \geq 8m_1 m_2 m_3.
$$


## 2014 — N5

**Record:** `bmo_2014_ff005c`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_ff005c.json.gz).

Let $a, b, c, p, q, r$ be positive integers such that $a^p + b^q + c^r = a^q + b^r + c^p = a^r + b^p + c^q$.
Prove that $a = b = c$ or $p = q = r$.


## 2015 — A6.

**Record:** `bmo_2015_61b7e3`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2015_61b7e3.json.gz).

For a polynomial $P \in \mathbb{R}[x]$, let $f(P) = n$ if $n$ is the smallest positive integer such that
$$
(\forall x \in \mathbb{R}) \underbrace{(P(P(\dots P(x))\dots))}_{n} > 0,
$$
and $f(P) = 0$ if such an integer $n$ does not exist. Does there exist a polynomial $P \in \mathbb{R}[x]$ of degree $2014^{2015}$ such that $f(P) = 2015$?


## 2015 — A5.

**Record:** `bmo_2015_81c11b`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2015_81c11b.json.gz).

Let $m$, $n$ be positive integers and $a$, $b$ be positive real numbers different from $1$. Suppose that $m > n$ and $\frac{a^{m+1}-1}{a^m-1} = \frac{b^{n+1}-1}{b^n-1} = c$. Show that $a^m c^n > b^n c^m$.


## 2015 — A4.

**Record:** `bmo_2015_b72311`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2015_b72311.json.gz).

Find all functions $f : \mathbb{R}^+ \to \mathbb{R}^+$ such that
$$
(x + y)f(2yf(x) + f(y)) = x^3 f(yf(x)), \quad \forall x, y \in \mathbb{R}^+.
$$


## 2015 — A2.

**Record:** `bmo_2015_c975a8`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2015_c975a8.json.gz).

Let $a$, $b$ and $c$ be the sides of a triangle and $r$, $R$ and $s$ be the inradius, the circumradius and the semiperimeter of the triangle respectively. Prove that
$$
\frac{1}{a+b} + \frac{1}{a+c} + \frac{1}{b+c} \le \frac{r}{16Rs} + \frac{s}{16Rr} + \frac{11}{8s}
$$


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


## 2017 — A1

**Record:** `bmo_2017_dd66f1`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2017_dd66f1.json.gz).

Let $a$, $b$, $c$ be positive real numbers such that $abc = 1$. Prove that
$$
\frac{1}{a^5+b^5+c^2} + \frac{1}{b^5+c^5+a^2} + \frac{1}{c^5+a^5+b^2} \le 1
$$


## 2017 — A4

**Record:** `bmo_2017_f27d27`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2017_f27d27.json.gz).

Let $M = \{(a,b,c) \in \mathbb{R}^3: 0 < a, b, c < \frac{1}{2} \text{ with } a+b+c=1\}$ and $f: M \to \mathbb{R}$ given as
$$
f(a, b, c) = 4\left(\frac{1}{a} + \frac{1}{b} + \frac{1}{c}\right) - \frac{1}{abc}
$$
Find the best (real) bounds $\alpha$ and $\beta$ such that
$$
f(M) = \{f(a, b, c) : (a, b, c) \in M\} \subseteq [\alpha, \beta]
$$
and determine whether any of them is achievable.


## 2019 — A4

**Record:** `bmo_2019_1bd440`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2019_1bd440.json.gz).

Let $a_{ij}$, $i = 1, 2, \dots, m$ and $j = 1, 2, \dots, n$, be positive real numbers. Prove that
$$
\sum_{i=1}^{m} \left( \sum_{j=1}^{n} \frac{1}{a_{ij}} \right)^{-1} \le \left( \sum_{j=1}^{n} \left( \sum_{i=1}^{m} a_{ij} \right)^{-1} \right)^{-1}.
$$
When does the equality hold?


## 2019 — TN1

**Record:** `bmo_2019_404973`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2019_404973.json.gz).

Let $\mathbb{P}$ be the set of all prime numbers. Find all functions $f: \mathbb{P} \to \mathbb{P}$ such that
$$
f(p)^{f(q)} + q^p = f(q)^{f(p)} + p^q
$$
holds for all $p, q \in \mathbb{P}$.


## 2019 — A3

**Record:** `bmo_2019_6827dd`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2019_6827dd.json.gz).

Let $a, b, c$ be real numbers such that $0 \le a \le b \le c$. Prove that if
$$
a + b + c = ab + bc + ca > 0,
$$
then $\sqrt{bc}(a + 1) \ge 2$. When does the equality hold?


## 2019 — A1

**Record:** `bmo_2019_6e2bee`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2019_6e2bee.json.gz).

Let $a_0$ be an arbitrary positive integer. Let $\{a_n\}$ be an infinite sequence of positive integers such that for every positive integer $n$ the term $a_n$ is the smallest positive integer such that $a_0 + a_1 + \dots + a_n$ is divisible by $n$. Prove that there is a positive integer $N$ such that $a_{n+1} = a_n$ for all $n \ge N$.

Let $a_0$ be an arbitrary positive integer. Consider the infinite sequence $(a_n)_{n \ge 1}$, defined inductively as follows: given $a_0, a_1, \dots, a_{n-1}$ define the term $a_n$ as the smallest positive integer such that $a_0 + a_1 + \dots + a_n$ is divisible by $n$. Prove that there exists a positive integer $M$ such that $a_{n+1} = a_n$ for all $n \ge M$.


## 2019 — C4

**Record:** `bmo_2019_dd840b`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2019_dd840b.json.gz).

A town-planner has built an isolated city whose road network consists of $2N$ roundabouts, each connecting exactly three roads. A series of tunnels and bridges ensure that all roads in the town meet only at roundabouts. All roads are two-way, and each roundabout is oriented clockwise.
Vlad has recently passed his driving test, and is nervous about roundabouts. He starts driving from his house, and always takes the first exit at each roundabout he encounters. It turns out his journey includes every road in the town in both directions before he arrives back at the starting point in the starting direction. For what values of $N$ is this possible?


## 2020 — C4

**Record:** `bmo_2020_2d224f`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2020_2d224f.json.gz).

A strategical video game consists of a map of finitely many towns. In each town there are $k$ directions, labelled from 1 through $k$. One of the towns is designated as initial, and one – as terminal. Starting from the initial town the hero of the game makes a finite sequence of moves. At each move the hero selects a direction from the current town. This determines the next town he visits and a certain positive amount of points he receives.

Two strategical video games are equivalent if for every sequence of directions the hero can reach the terminal town from the initial in one game, he can do so in the other game, and, in addition, he accumulates the same amount of points in both games.

For his birthday John receives two strategical video games – one with $N$ towns and one with $M$ towns. He claims they are equivalent. Marry is convinced they are not. Marry is right. Prove that she can provide a sequence of at most $N + M$ directions that shows the two games are indeed not equivalent.

Stefan Gerdjikov, Bulgaria


## 2020 — N2

**Record:** `bmo_2020_327627`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2020_327627.json.gz).

A number of $N$ children are at a party, and they sit in a circle to play a game of Pass the Parcel. Because the host has no other form of entertainment, the parcel has infinitely many layers. On turn $i$, starting with $i = 1$, the following two things happen in order:
(1) The parcel is passed $i^2$ positions clockwise; and
(2) The child currently holding the parcel unwraps a layer and claims the prize inside. For what values of $N$ will every child receive a prize?


## 2021 — A4

**Record:** `bmo_2021_2fdefd`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2021_2fdefd.json.gz).

Let $f, g$ be functions from the positive integers to the integers. Vlad the impala is jumping around the integer grid. His initial position is $\mathbf{x}_0 = (0,0)$, and for every $n \ge 1$, his jump is
$$
\mathbf{x}_n - \mathbf{x}_{n-1} = (\pm f(n), \pm g(n)) \text{ or } (\pm g(n), \pm f(n)),
$$
with eight possibilities in total. Is it always possible that Vlad can choose his jumps to return to his initial location $(0,0)$ infinitely many times when
(a) $f, g$ are polynomials with integer coefficients?
(b) $f, g$ are any pair of functions from the positive integers to the integers?


## 2022 — A5.

**Record:** `bmo_2022_34f8be`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2022_34f8be.json.gz).

Find all functions $f: (0, \infty) \to (0, \infty)$ such that
$$
f(yf(x)^3 + x) = x^3 f(y) + f(x)
$$
for all $x, y > 0$.


## 2022 — C5.

**Record:** `bmo_2022_36e10e`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2022_36e10e.json.gz).

A cube of side length $2021$ is given. In how many ways can we place a $1 \times 1 \times 1$ cubelet on the border of this cube in such a way that the newly formed solid can be completely filled using $k \times 1 \times 1$, $1 \times k \times 1$ and $1 \times 1 \times k$ cuboids, for some $k \in \mathbb{N} \setminus \{1\}$?


## 2022 — N2.

**Record:** `bmo_2022_380ffa`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2022_380ffa.json.gz).

Let $a$, $b$, $n$ be positive integers such that:
(i) $a^{2021} \mid n$ and $b^{2021} \mid n$
(ii) $2022 \mid a - b$ and $a > b$.
Prove that there is a subset of the divisors of the number $n$ having sum of elements divisible by $2022$ but not by $2022^2$.


## 2022 — A2.

**Record:** `bmo_2022_4d73ec`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2022_4d73ec.json.gz).

Let $k > 1$ be a real number, $n \ge 3$ be an integer, and $x_1 \ge x_2 \ge x_3 \ge \dots \ge x_n > 0$ be real numbers. Prove the inequality:
$$
\frac{x_1 + kx_2}{x_2 + x_3} + \frac{x_2 + kx_3}{x_3 + x_4} + \dots + \frac{x_{n-1} + kx_n}{x_n + x_1} + \frac{x_n + kx_1}{x_1 + x_2} \ge \frac{n(k+1)}{2}.
$$


## 2022 — N4.

**Record:** `bmo_2022_977a4b`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2022_977a4b.json.gz).

A hare and a tortoise run in the same direction, at constant but different speeds, around the base of a tall square tower. They start together at the same vertex, and the run ends when both return to the initial vertex simultaneously for the first time. Suppose the hare runs with speed $1$, and the tortoise with speed less than $1$. For what rational numbers $x$ is it true that, if the tortoise runs with speed $x$, the fraction of the entire run for which the tortoise can see the hare is also $x$?


## 2023 — A1

**Record:** `bmo_2023_0ab85a`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2023_0ab85a.json.gz).

Find all functions $f: \mathbb{R} \to \mathbb{R}$ such that for all $x, y \in \mathbb{R}$,
$$
x f(x + f(y)) = (y - x) f(f(x)).
$$


## 2023 — A4

**Record:** `bmo_2023_2ac979`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2023_2ac979.json.gz).

Prove that there exists a real number $c < 3/4$ such that for each sequence $\{x_i\}_{i=1}^\infty$ satisfying $0 \le x_i \le 1$ for all $i$, there are infinitely many pairs $(m, n)$ with $m > n$ such that
$$
|x_m - x_n| \le \frac{c}{m}.
$$


## 2023 — A3

**Record:** `bmo_2023_423d32`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2023_423d32.json.gz).

Find all functions $f: \mathbb{R} \to \mathbb{R}$ such that for all real numbers $x$ and $y$,
$$
f(xy + f(x^2)) = x f(x + y).
$$


## 2023 — A6

**Record:** `bmo_2023_a23af0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2023_a23af0.json.gz).

Let $\mathbb{R}_{>0}$ be the set of all positive real numbers. Find all functions $f: \mathbb{R}_{>0} \to \mathbb{R}_{>0}$ such that for all positive real numbers $x$ and $y$,
$$
f(x^{2023} + f(x)f(y)) = x^{2023} + yf(x).
$$


## 2023 — A2

**Record:** `bmo_2023_bc3f7d`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2023_bc3f7d.json.gz).

Let $a$, $b$, $c$, $d$ be non-negative real numbers such that
$$
\frac{1}{a+3} + \frac{1}{b+3} + \frac{1}{c+3} + \frac{1}{d+3} = 1.
$$
Prove that there is a permutation $(x_1, x_2, x_3, x_4)$ of the sequence $(a, b, c, d)$ such that
$$
x_1x_2 + x_2x_3 + x_3x_4 + x_4x_1 \ge 4.
$$


## 2023 — A5

**Record:** `bmo_2023_bfc001`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2023_bfc001.json.gz).

Are there polynomials $P$ and $Q$ with real coefficients such that $P(P(x)) \cdot Q(Q(x))$ has exactly $2023$ distinct real roots and $P(Q(x)) \cdot Q(P(x))$ has exactly $2024$ distinct real roots?


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


## 2024 — A3.

**Record:** `bmo_2024_3cdd5b`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2024_3cdd5b.json.gz).

Find all triples $(a, b, c)$ of positive real numbers that satisfy the system:
$$
\begin{aligned}
11bc - 36b - 15c &= abc \\
12ca - 10c - 28a &= abc \\
13ab - 21a - 6b &= abc.
\end{aligned}
$$


## 2024 — C2.

**Record:** `bmo_2024_4b7efa`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2024_4b7efa.json.gz).

Let $n \ge 2$ and $S = \{1, 2, \dots, n^2\}$. For any function $f : S \to S$ let $\text{Fix}(f) = \{x \in S \mid f(x) = x\}$. Find the possible values of the expression
$$
|\text{Fix}(f)| + |\text{Im}(f)| + \max_{k \in S} |f^{-1}(k)|
$$
as $f$ ranges over all functions $f : S \to S$.


## 2024 — N1.

**Record:** `bmo_2024_54aaec`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2024_54aaec.json.gz).

Let $n$ be a fixed natural number and
$$
S_n = \{\overline{c_n c_{n-1} \dots c_1}_{(10)} \mid c_1, \dots, c_{n-1}, c_n \in \{1, 2, 3, 4\}\}.
$$
Are there distinct numbers $x$ and $y$, $x, y \in S_n$, such that $4^n \mid x - y$?


## 2024 — A6.

**Record:** `bmo_2024_7b3222`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2024_7b3222.json.gz).

Let $\mathbb{R}^+ = (0, \infty)$ be the set of all positive real numbers. Find all functions $f : \mathbb{R}^+ \to \mathbb{R}^+$ and polynomials $g(x)$ with non-negative coefficients and $g(0) = 0$ that satisfy the equality:
$$
f(f(x) + g(y)) = f(x - y) + 2y
$$
for all positive real numbers $x > y$.


## 2024 — A2.

**Record:** `bmo_2024_c7a652`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2024_c7a652.json.gz).

Prove that there is a positive integer number $n$ such that the decimal representation of the number:
$$
\sum_{k=1}^{\lfloor \frac{n}{3} \rfloor} \binom{n}{3k} 8^k
$$
ends in 2023 digits 8.


## 2025 — A5

**Record:** `bmo_2025_3bfb9a`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_3bfb9a.json.gz).

Find all functions $f: \mathbb{R} \to \mathbb{R}$ such that
$$
f(x + y f(x)) + y = x y + f(x + y)
$$
for all real numbers $x, y$.


## 2025 — A4

**Record:** `bmo_2025_4bc606`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_4bc606.json.gz).

Prove that the inequality
$$
\left(\frac{a^2 + b^2}{a + b}\right)^3 + \left(\frac{b^2 + c^2}{b + c}\right)^3 + \left(\frac{c^2 + a^2}{c + a}\right)^3 \ge a^3 + b^3 + c^3
$$
holds for all $a, b, c > 0$.


## 2025 — N6

**Record:** `bmo_2025_613b0e`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_613b0e.json.gz).

Find all polynomials $P(x)$ with integer coefficients such that there exists a positive integer $N$ such that for all positive integers $n > N$ we have $P(n) > 0$ and
$$
n + P(n) \mid n^{P(n)} + P(n)^n.
$$


## 2025 — A2

**Record:** `bmo_2025_6e83a7`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_6e83a7.json.gz).

Determine all natural numbers $n$ such that the inequality
$$
x^n + 2x + 1 \ge 4x^2
$$
holds for every $x > 0$.


## 2025 — N5

**Record:** `bmo_2025_7480b3`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_7480b3.json.gz).

Let $k > 2$ be a given positive integer. Find all positive integers $d$, for which there exists a polynomial $P(x)$ with integer coefficients such that $\deg P(x) = d$ and $11^k \mid 2025^n + P(n)$ for all positive integers $n > k$.


## 2025 — A1

**Record:** `bmo_2025_79faf0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_79faf0.json.gz).

Determine all real polynomials $P(x)$ such that
$$
P^2(x) + P^2(y) + P^2(x + y) = 2P(x^2 + xy + y^2)
$$
for every $x, y \in \mathbb{R}$.


## 2025 — A3

**Record:** `bmo_2025_9242c4`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_9242c4.json.gz).

Let $f: \mathbb{R}^+ \to \mathbb{R}^+$ be a non-constant function. Prove that there exist $a, b \in \mathbb{R}^+$ such that
$$
f(a) + f(b) > 2f(\sqrt{ab}).
$$


## 2025 — N2

**Record:** `bmo_2025_b9b8f0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_b9b8f0.json.gz).

A positive integer $n > 1$ is called good if there exists some permutation of the numbers $1, 2, 3, \dots, n$, denoted by $(a_1, a_2, a_3, \dots, a_n)$ such that $a_i$ and $a_{i+1}$ have different parities for every $1 \le i \le n-1$; and for every $1 \le k \le n$, the sum $a_1 + a_2 + \dots + a_k$ is a quadratic residue modulo $n$. Prove that there exist infinitely many good numbers, as well as infinitely many numbers which are not good.
*Remark: Here an integer $x$ is considered a quadratic residue modulo $n$ if there exists an integer $y$ such that $x \equiv y^2 \pmod{n}$.*


## 2025 — A6

**Record:** `bmo_2025_ce73f9`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_ce73f9.json.gz).

For all $a$, $b$, $c$ positive real numbers with $a^2b + a^2c + b^2a + b^2c + c^2a + c^2b = 1$, show that
$$
\frac{ab + bc + ca}{1 + 2abc} \le \frac{(a + b + c)^2}{4}.
$$


## 2025 — A7

**Record:** `bmo_2025_ea349a`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_ea349a.json.gz).

Let $x_1, x_2, x_3$ and $x_4$ be positive real numbers. Prove the inequality:
$$
\frac{x_1 + 3x_2}{x_2 + x_3} + \frac{x_2 + 3x_3}{x_3 + x_4} + \frac{x_3 + 3x_4}{x_4 + x_1} + \frac{x_4 + 3x_1}{x_1 + x_2} \ge 8.
$$



# CMO-China source statements

## 2022 — 6

**Record:** `chn_2022_4f6805`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_4f6805.json.gz).

There are some direct one-way flights among $n \ge 8$ airports. Between any two airports $a$ and $b$, there is at most one direct one-way flight from $a$ to $b$ (it is possible to have direct one-way flights both from $a$ to $b$ and from $b$ to $a$). Suppose that, for any set $A$ consisting of some airports with $1 \le |A| \le n-1$, there are at least $4 \cdot \min\{|A|, n-|A|\}$ flights in total departing from the airports in $A$ and arriving at the airports not in $A$.
Prove that for any airport $x$, one can depart from $x$ and take no more than $\sqrt{2n}$ flights to return to $x$.


## 2023 — 4

**Record:** `chn_2023_0ba7d6`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_0ba7d6.json.gz).

Let $a_1, a_2, \dots, a_{2023}$ be nonnegative real numbers such that $a_1 + a_2 + \dots + a_{2023} = 100$. Let $N$ denote the number of elements in the following set
$$
\{(i, j) \mid 1 \le i \le j \le 2023, a_i a_j \ge 1\}.
$$
Prove that $N \le 5050$, and determine the necessary and sufficient condition for $N = 5050$.


## 2023 — 2

**Record:** `chn_2023_364475`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_364475.json.gz).

Determine the largest real number $C$ such that
$$
\sum_{i=1}^{n} \sum_{j=1}^{n} (n - |i - j|) x_i x_j \ge C \sum_{i=1}^{n} x_i^2
$$
holds for every positive integer $n$ and any real numbers $x_1, x_2, \dots, x_n$.


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


## 2024 — 1

**Record:** `chn_2024_9e1916`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2024_9e1916.json.gz).

Fix an irrational number $\alpha > 1$ and a positive integer $L$ such that $L > \frac{\alpha^2}{\alpha - 1}$.
Given an integer $x_1 > L$, define a sequence $\{x_n\}$ as follows: for every integer $n \ge 1$,
$$
x_{n+1} = \begin{cases} \lfloor \alpha x_n \rfloor, & \text{if } x_n \le L, \\ \lfloor \frac{x_n}{\alpha} \rfloor, & \text{if } x_n > L. \end{cases}
$$
Here, $\lfloor u \rfloor$ denotes the largest integer that is less than or equal to $u$.
(1) Prove that the sequence $\{x_n\}$ is eventually periodic, i.e., there exist positive integers $T$ and $N$ such that for any integer $n > N$, we have $x_{n+T} = x_n$.
(2) Prove that the smallest integer $T$ satisfying (1) is an odd integer that is independent of $x_1$.



# China-TST source statements

## 2014 — 3

**Record:** `chn_2014_1a3af5`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2014_1a3af5.json.gz).

Show that there are no 2-tuples $(x, y)$ of positive integers satisfying the equation
$$
(x+1)(x+2)\cdots(x+2014) = (y+1)(y+2)\cdots(y+4028).
$$


## 2014 — 2

**Record:** `chn_2014_1d410b`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2014_1d410b.json.gz).

Let $A_1A_2\cdots A_{101}$ be a regular 101-gon, and color every vertex red or blue. Let $N$ be the number of obtuse triangles satisfying the following: The three vertices of the triangle must be vertices of the 101-gon, both the vertices with acute angles have the same color, and the vertex with obtuse angle have different color.

(1) Find the largest possible value of $N$.

(2) Find the number of ways to color the vertices such that maximum $N$ is achieved. (Two colorings are different if for some $A_i$ the colors are different on the two coloring schemes)


## 2014 — 5

**Record:** `chn_2014_4de9b3`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2014_4de9b3.json.gz).

Let $n$ be a given integer which is greater than $1$. Find the greatest constant $\lambda(n)$ such that for any non-zero complex $z_1, z_2, \dots, z_n$, we have
$$
\sum_{k=1}^{n} |z_k|^2 \geq \lambda(n) \min_{1 \leq k \leq n} \{|z_{k+1} - z_k|^2\},
$$
where $z_{n+1} = z_1$.


## 2014 — 4

**Record:** `chn_2014_c8fce5`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2014_c8fce5.json.gz).

Let $k$ be a fixed odd integer, $k > 3$. Prove: There exist infinitely many positive integers $n$, such that there are two positive integers $d_1, d_2$ satisfying $d_1, d_2$ each dividing $\frac{n^2+1}{2}$, and $d_1 + d_2 = n + k$.


## 2021 — 3

**Record:** `chn_2021_0b68e6`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_0b68e6.json.gz).

Find the largest constant $C > 0$, such that for any integer $n \ge 2$, one can find real numbers $x_1, x_2, \dots, x_n \in [-1, 1]$ satisfying
$$
\prod_{1 \le i < j \le n} (x_i - x_j) \ge C^{\frac{n(n-1)}{2}}.
$$


## 2021 — 4

**Record:** `chn_2021_0faf8c`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_0faf8c.json.gz).

For a positive integer $n$, let $\varphi(n)$ represent the number of positive integers not exceeding $n$ and relatively prime to $n$. Find all functions $f:\mathbb{N}_+ \to \mathbb{N}_+$ satisfying that for any positive integers $m, n$ with $m \ge n$,
$$f(m\varphi(n^3)) = f(m)\varphi(n^3).$$


## 2021 — 3

**Record:** `chn_2021_36327e`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_36327e.json.gz).

Given positive integers $a$, $b$, $c$ which are pairwise coprime. Let $f(n)$ represent the number of nonnegative integer solutions $(x, y, z)$ of the equation $a x + b y + c z = n$. Prove: there exist real constants $\alpha$, $\beta$, $\gamma$, such that for every nonnegative real number $n$,
$$
|f(n) - (\alpha n^2 + \beta n + \gamma)| < \frac{a+b+c}{12}.
$$


## 2021 — 1

**Record:** `chn_2021_584851`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_584851.json.gz).

Let $m, n$ be positive integers, $a_{ij}$ ($1 \le i \le m, 1 \le j \le n$) be nonnegative real numbers such that for any $i, j$, the inequalities
$$
a_{i,1} \ge a_{i,2} \ge \dots \ge a_{i,n}, \quad a_{1,j} \ge a_{2,j} \ge \dots \ge a_{m,j}
$$
hold. For $i = 1, 2, \dots, m$ and $j = 1, 2, \dots, n$, define
$$
X_{i,j} = a_{1,j} + \dots + a_{i-1,j} + a_{i,j} + a_{i,j-1} + \dots + a_{i,1},
$$
$$
Y_{i,j} = a_{i,j} + a_{i+1,j} + \dots + a_{m,j} + a_{i,j+1} + \dots + a_{i,n}.
$$
Prove that
$$
\prod_{i=1}^{m} \prod_{j=1}^{n} X_{i,j} \ge \prod_{i=1}^{m} \prod_{j=1}^{n} Y_{i,j}.
$$


## 2021 — 4

**Record:** `chn_2021_8156cd`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_8156cd.json.gz).

For each positive integer $N$, let $\tau(N)$ be the number of positive factors of $N$; $\omega(N)$ be the number of distinct prime factors of $N$; $\Omega(N)$ be the number of prime factors (counts multiplicities) of $N$. Prove: for each positive integer $n$,
$$
\sum_{m=1}^{n} 5^{\omega(m)} \le \sum_{k=1}^{n} \lfloor \frac{n}{k} \rfloor \tau(k)^2 \le \sum_{m=1}^{n} 5^{\Omega(m)}.
$$

Here, $\lfloor x \rfloor$ is the largest integer not exceeding $x$.


## 2021 — 3

**Record:** `chn_2021_ab96ca`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_ab96ca.json.gz).

Let $S(k)$ denote the sum of all digits of $k$ in base 10. Find all integers $n \ge 2$ and rational numbers $\beta \in (0,1)$, such that there exist $n$ distinct positive integers $a_1, a_2, \dots, a_n$ that satisfy: for any subset $I \subseteq \{1, 2, \dots, n\}$ with two or more elements,
$$ S\left(\sum_{i \in I} a_i\right) = \beta \cdot \sum_{i \in I} S(a_i). $$


## 2021 — 5

**Record:** `chn_2021_b54346`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_b54346.json.gz).

Find all functions $f : \mathbb{R} \to \mathbb{R}$ such that for any $x, y \in \mathbb{R}$,
$$ f(xf(y) + y^{2021}) = yf(x) + (f(y))^{2021}. $$
(Contributed by Fu Yunhao)


## 2021 — 5

**Record:** `chn_2021_d4b623`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_d4b623.json.gz).

Let $n$ be a positive integer, $a_1, a_2, \dots, a_{2n+1}$ be $2n+1$ positive real numbers. For $k = 1, 2, \dots, 2n+1$, define
$$
b_k = \max_{0 \le m \le n} \left( \frac{1}{2m+1} \sum_{i=k-m}^{k+m} a_i \right),
$$
where the subscript of $a_i$ is taken modulo $2n+1$. Prove: the number of subscripts $k$ satisfying that $b_k \ge 1$ does not exceed $2 \sum_{i=1}^{2n+1} a_i$.


## 2021 — 4

**Record:** `chn_2021_d6fcbc`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_d6fcbc.json.gz).

For real numbers $x_1, x_2, \dots, x_{60} \in [-1, 1]$, find the maximum of
$$
\sum_{i=1}^{60} x_i^2 (x_{i+1} - x_{i-1}),
$$
where $x_0 = x_{60}, x_{61} = x_1$.


## 2021 — 2

**Record:** `chn_2021_e6f1e7`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_e6f1e7.json.gz).

Given positive integers $k$ and $n$ ($n \ge 2$), find the minimum constant $c$ satisfying this assertion: if $G$ is a simple $kn$-regular graph (the degree of each vertex is $kn$) with $m$ vertices, then each vertex can be coloured one of $n$ colours, such that the number of “mono edges” is at most $cm$. Here, a mono edge is an edge incident to two vertices of the same colour.


## 2022 — 5

**Record:** `chn_2022_1913d8`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_1913d8.json.gz).

Let $n$ be a positive integer. Let $x_1, x_2, \dots, x_{2n}$ be $2n$ nonnegative real numbers such that $x_1 + x_2 + \dots + x_{2n} = 4$. Prove that there exist nonnegative integers $p, q$ such that $q \le n - 1$, and that
$$
\sum_{i=1}^{q} x_{p+2i-1} \le 1, \quad \sum_{i=q+1}^{n-1} x_{p+2i} \le 1.
$$

*Remark 1 : the subscripts are understood modulo $2n$, i.e. if $k \equiv \ell \pmod{2n}$, then $x_k = x_\ell$.*
*Remark 2 : If $q = 0$, then the first sum is considered as 0; if $q = n - 1$, then the second sum is considered as 0.*


## 2022 — 6

**Record:** `chn_2022_43fc7f`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_43fc7f.json.gz).

Given a positive integer $n$, let $D$ denote the set of all positive divisors of $n$. Let $A$ and $B$ be subsets of $D$ satisfying: for any $a \in A$ and $b \in B$, we have $a \nmid b$ and $b \nmid a$. Prove that
$$
\sqrt{|A|} + \sqrt{|B|} \le \sqrt{|D|}.
$$


## 2022 — 3

**Record:** `chn_2022_514503`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_514503.json.gz).

Find all functions $f: \mathbb{R} \to \mathbb{R}$ such that, for any real numbers $x, y$, the following two multisets are equal
$$
\{f(xf(y) + 1), f(yf(x) - 1)\} = \{xf(f(y)) - 1, yf(f(x)) + 1\}.
$$

*Remark: $\{a, b\} = \{c, d\}$ are equal as multisets if $a = c$ and $b = d$, or $a = d$ and $b = c$.*


## 2023 — 2

**Record:** `chn_2023_200f9d`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_200f9d.json.gz).

Let $a$, $b$, and $d$ be integers satisfying $d \ge 0$, $|a| \ge 2$, and $b \ge (|a| + 1)^{d+1}$. Suppose $f(x)$ is a real-coefficient polynomial of degree $d$, and for each positive integer $n$, let $r_n$ denote the remainder of $\lfloor f(n)a^n \rfloor$ modulo $b$.

*Proof:* If the sequence $r_n$ is ultimately periodic, then $f(x)$ is a rational-coefficient polynomial.

*Note 1:* For every real number $x$, $\lfloor x \rfloor$ denotes the largest integer that is not greater than $x$.

*Note 2:* A sequence $a_n$ is called *ultimately periodic* if there exist positive integers $n_0$ and $T$ such that for every integer $n \ge n_0$, we have $a_{n+T} = a_n$.


## 2023 — 4

**Record:** `chn_2023_2f8df9`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_2f8df9.json.gz).

Find all functions $f : \mathbb{Z} \to \mathbb{Z}$ that satisfy the following equation for any integers $a, b, c$:
$$
2f(a^2 + b^2 + c^2) - 2f(ab + bc + ca) = (f(a - b))^2 + (f(b - c))^2 + (f(c - a))^2.
$$


## 2023 — 3

**Record:** `chn_2023_4f8fa4`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_4f8fa4.json.gz).

Given an integer $n \ge 2$. Find the minimum real number $\lambda$ such that for any real numbers $a_1, a_2, \dots, a_n$, and $b$, the following inequality holds:
$$
\lambda \sum_{i=1}^{n} \sqrt{|a_i - b|} + \sqrt{n \left| \sum_{i=1}^{n} a_i \right|} \ge \sum_{i=1}^{n} \sqrt{|a_i|}.
$$


## 2023 — 5

**Record:** `chn_2023_56850c`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_56850c.json.gz).

Does there exist a sequence of pairwise distinct integers $a_1, a_2, \dots$ that satisfies both of the following conditions?

a. For all positive integers $k$, we have $a_{k^2} > 0$ and $a_{k^2+k} < 0$.

b. For all positive integers $n$, we have $|a_{n+1} - a_n| \le 2023\sqrt{n}$.


## 2023 — 1

**Record:** `chn_2023_8e18d4`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_8e18d4.json.gz).

Does there exist an irrational number $x$ such that there are at most finitely many positive integers $n$ satisfying
$$
\{kx\} \geq \frac{1}{n+1}
$$
for every $k \in \{1, \dots, n\}$?

Note: Here, for a positive real number $y$, $\{y\}$ denotes the fractional part of $y$.


## 2023 — 6

**Record:** `chn_2023_a44cf5`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_a44cf5.json.gz).

Find the largest real number $\lambda$ with the following property: for any 100th-order doubly stochastic matrix, it is always possible to select 150 elements from it and change the remaining 9850 elements to zero, such that the resulting matrix has row sums and column sums not less than $\lambda$.

Note: An "$n$th-order doubly stochastic matrix" is an $n \times n$ square matrix in which all elements are non-negative real numbers, and the sum of each row and the sum of each column are both equal to 1.


## 2025 — Problem 1

**Record:** `chn_2025_05f740`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_05f740.json.gz).

Prove that the real-coefficient polynomial in $x, y, z$,
$$
x^{4}(x - y)(x - z) + y^{4}(y - z)(y - x) + z^{4}(z - x)(z - y),
$$
cannot be expressed as a finite sum of squares of real-coefficient polynomials in $x, y, z$.


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


## 2025 — Problem 5

**Record:** `chn_2025_2add97`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_2add97.json.gz).

There are $2025$ people and $66$ given colors. Each person has $66$ balls, one of each color, with a total weight of $1$ for all $66$ balls.
Find the smallest real number $C$ such that, no matter how the balls are weighted, one can always select exactly one ball from each person so that for every color, the total weight of the selected balls of that color does not exceed $C$.


## 2025 — Problem 9

**Record:** `chn_2025_53da42`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_53da42.json.gz).

A finite point set $P = \{(x_i, y_i) \mid i = 1, 2, \dots, n\}$ in the plane is called **sparse** if for any $1 \le i < j \le n$,
$$
|x_i - x_j| \cdot |y_i - y_j| \ge 1.
$$
(1) Let $\{Q_1, Q_2, Q_3\}$ be a sparse set where no $Q_i$ lies inside the axis-aligned rectangle with the other two points as diagonal vertices. Prove that the area of triangle $Q_1Q_2Q_3$ is at least $\frac{\sqrt{5}}{2}$.

(2) Let $P$ be a sparse set with no three collinear points, all lying inside an axis-aligned square of side length $a$. Prove that the number of points in $P$ does not exceed
$$
\frac{a^2}{\sqrt{5}} + 2a + 1.
$$


## 2025 — Problem 11

**Record:** `chn_2025_73d79f`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_73d79f.json.gz).

Given a positive integer $n \ge 4$, prove that the equation
$$
(2^x - 1)(5^x - 1) = y^n
$$
has no positive integer solutions $(x, y)$.


## 2025 — Problem 12

**Record:** `chn_2025_82eea5`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_82eea5.json.gz).

Let $P(x)$ and $Q(x)$ be non-constant real polynomials such that for every positive integer $m$, there exists a positive integer $n$ with $P(m) = Q(n)$.
(1) Prove that if $\deg(Q)$ divides $\deg(P)$, then there exists a real polynomial $h(x)$ such that $P(x) = Q(h(x))$.
(2) Prove that $\deg(Q)$ divides $\deg(P)$.



# EGMO source statements

## 2012 — Problem 4.

**Record:** `egm_2012_b764d7`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2012_b764d7.json.gz).

A set $A$ of integers is called sum-full if $A \subseteq A+A$, i.e. each element $a \in A$ is the sum of some pair of (not necessarily different) elements $b, c \in A$. A set $A$ of integers is said to be zero-sum-free if $0$ is the only integer that cannot be expressed as the sum of the elements of a finite nonempty subset of $A$.

Does there exist a sum-full zero-sum-free set of integers?


## 2013 — Problem 4.

**Record:** `egm_2013_34529d`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2013_34529d.json.gz).

Find all positive integers $a$ and $b$ for which there are three consecutive integers at which the polynomial
$$
P(n)=\frac{n^{5}+a}{b}
$$
takes integer values.


## 2013 — Problem 2.

**Record:** `egm_2013_35d4e6`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2013_35d4e6.json.gz).

Determine all integers $m$ for which the $m \times m$ square can be dissected into five rectangles, the side lengths of which are the integers $1,2,3, \ldots, 10$ in some order.


## 2014 — 6.

**Record:** `egm_2014_2a820b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2014_2a820b.json.gz).

Determine all functions $f: \mathbb{R} \rightarrow \mathbb{R}$ satisfying the condition
$$
f\left(y^{2}+2 x f(y)+f(x)^{2}\right)=(y+f(x))(x+f(y))
$$
for all real numbers $x$ and $y$.


## 2014 — 1.

**Record:** `egm_2014_971b39`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2014_971b39.json.gz).

Determine all real constants $t$ such that whenever $a, b, c$ are the lengths of the sides of a triangle, then so are $a^{2}+b c t$, $b^{2}+c a t$, $c^{2}+a b t$.


## 2014 — 1.

**Record:** `fra_2014_41466c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/france/fra_2014_41466c.json.gz).

Déterminer tous les nombres réels $t$ tels que si $a, b, c$ sont les longueurs des côtés d'un triangle, alors il en est de même pour $a^{2}+b c t, b^{2}+c a t, c^{2}+a b t$.


## 2016 — Problem 1.

**Record:** `rou_2016_5548b4`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2016_5548b4.json.gz).

Let $n$ be an odd positive integer, and let $x_1, x_2, \dots, x_n$ be non-negative real numbers. Show that $\min_{k=1,\dots,n} (x_k^2 + x_{k+1}^2) \le \max_{k=1,\dots,n} (2x_k x_{k+1})$, where $x_{n+1} = x_1$.


## 2020 — Problem 2

**Record:** `egm_2020_0b3206`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2020_0b3206.json.gz).

Find all lists $\left(x_{1}, x_{2}, \ldots, x_{2020}\right)$ of non-negative real numbers such that the following three conditions are all satisfied:
(i) $x_{1} \leq x_{2} \leq \ldots \leq x_{2020}$;
(ii) $x_{2020} \leq x_{1}+1$;
(iii) there is a permutation $\left(y_{1}, y_{2}, \ldots, y_{2020}\right)$ of $\left(x_{1}, x_{2}, \ldots, x_{2020}\right)$ such that
$$
\sum_{i=1}^{2020}\left(\left(x_{i}+1\right)\left(y_{i}+1\right)\right)^{2}=8 \sum_{i=1}^{2020} x_{i}^{3}
$$
A permutation of a list is a list of the same length, with the same entries, but the entries are allowed to be in any order. For example, $(2,1,2)$ is a permutation of $(1,2,2)$, and they are both permutations of $(2,2,1)$. Note that any list is a permutation of itself.


## 2020 — Problem 6

**Record:** `egm_2020_2eb0ec`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2020_2eb0ec.json.gz).

Let $m > 1$ be an integer. A sequence $a_{1}, a_{2}, a_{3}, \ldots$ is defined by $a_{1} = a_{2} = 1$, $a_{3} = 4$, and for all $n \geq 4$,
$$
a_{n} = m\left(a_{n-1} + a_{n-2}\right) - a_{n-3}.
$$
Determine all integers $m$ such that every term of the sequence is a square.


## 2024 — Problem 4

**Record:** `egm_2024_10a8ce`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2024_10a8ce.json.gz).

For a sequence $a_{1} < a_{2} < \cdots < a_{n}$ of integers, a pair $(a_{i}, a_{j})$ with $1 \leq i < j \leq n$ is called interesting if there exists a pair $(a_{k}, a_{l})$ of integers with $1 \leq k < l \leq n$ such that
$$
\frac{a_{l} - a_{k}}{a_{j} - a_{i}} = 2
$$
For each $n \geq 3$, find the largest possible number of interesting pairs in a sequence of length $n$.


## 2024 — Problem 1

**Record:** `egm_2024_86f588`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2024_86f588.json.gz).

Two different integers $u$ and $v$ are written on a board. We perform a sequence of steps. At each step we do one of the following two operations:

(i) If $a$ and $b$ are different integers on the board, then we can write $a+b$ on the board, if it is not already there.

(ii) If $a, b$ and $c$ are three different integers on the board, and if an integer $x$ satisfies $a x^{2}+b x+c=0$, then we can write $x$ on the board, if it is not already there.

Determine all pairs of starting numbers $(u, v)$ from which any integer can eventually be written on the board after a finite sequence of steps.


## 2024 — Problem 6

**Record:** `egm_2024_c245c8`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2024_c245c8.json.gz).

Find all positive integers $d$ for which there exists a degree $d$ polynomial $P$ with real coefficients such that there are at most $d$ different values among $P(0), P(1), \ldots, P\left(d^{2}-d\right)$.


## 2025 — P2.

**Record:** `egm_2025_23b350`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2025_23b350.json.gz).

An infinite increasing sequence $a_{1} < a_{2} < a_{3} < \dots$ of positive integers is called central if for every positive integer $n$, the arithmetic mean of the first $a_{n}$ terms of the sequence is equal to $a_{n}$.  
Show that there exists an infinite sequence $b_{1}, b_{2}, b_{3}, \ldots$ of positive integers such that for every central sequence $a_{1}, a_{2}, a_{3}, \ldots$, there are infinitely many positive integers $n$ with $a_{n} = b_{n}$.


## 2025 — P6.

**Record:** `egm_2025_af59a0`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2025_af59a0.json.gz).

In each cell of a $2025 \times 2025$ board, a nonnegative real number is written in such a way that the sum of the numbers in each row is equal to $1$, and the sum of the numbers in each column is equal to $1$. Define $r_{i}$ to be the largest value in row $i$, and let $R = r_{1} + r_{2} + \dots + r_{2025}$. Similarly, define $c_{i}$ to be the largest value in column $i$, and let $C = c_{1} + c_{2} + \dots + c_{2025}$. What is the largest possible value of $\frac{R}{C}$?

What is the largest possible value of $\frac{R}{C}$?



# IMO source statements

## 1983 — 1.

**Record:** `esp_1983_a103e1`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_1983_a103e1.json.gz).

Hallar todas las funciones $f$ definida en el conjunto de los números reales, que toman valores reales positivos y que satisfacen las condiciones

1) $\quad f(x f(y))=y f(x)$ para todo $x, y$ positivos,

2) $\quad f(x) \rightarrow 0$ si $x \rightarrow \infty$.


## 1984 — 3.

**Record:** `esp_1984_25d462`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_1984_25d462.json.gz).

Tenemos en el plano dos puntos diferentes, $A$ y $O$. Para cada punto $X$ del plano distinto de $O$, denotamos por $\alpha(X)$ la medida del ángulo entre $OA$ y $OX$, en radianes, y contado en sentido antihorario desde $OA$ $(0 \leq \alpha(X)<2\pi)$.

Sea $C(X)$ la circunferencia de centro $O$ y radio de longitud $OX + \frac{\alpha(X)}{OX}$. Tenemos un número finito de colores y coloreamos cada uno de los puntos del plano con ellos.

Demostrar que existe un punto $Y$ tal que $\alpha(Y)>0$ y tal que su color aparece sobre la circunferencia de $C(Y)$.


## 1985 — 3.

**Record:** `esp_1985_e6ffa9`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_1985_e6ffa9.json.gz).

Dado un polinomio $P(x)=a_{0}+a_{1} x+a_{2} x^{2}+\cdots+a_{k} x^{k}$ con coeficientes enteros, denotamos por $w(P)$ el número de coeficientes impares de $P$. Sea $Q_{i}(x)=(1+x)^{i}$, para $i=0,1, \ldots$ Demostrar que si $i_{1}, i_{2}, \ldots, i_{n}$ son enteros tales que $0 \leq i_{1}<i_{2}<\cdots<i_{n}$, entonces
$$
w\left(Q_{i_{1}}+Q_{i_{2}}+\cdots+Q_{i_{n}}\right) \geq w\left(Q_{i_{1}}\right)
$$


## 1986 — 5.

**Record:** `esp_1986_293a65`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_1986_293a65.json.gz).

Hallar todas las funciones $f$ definidas en el conjunto de los números reales no negativos y que toman valores reales no negativos, tales que

1) $\quad f(x f(y)) f(y)=f(x+y)$ para todo $x, y \geq 0$,

2) $\quad f(2)=0$,

3) $\quad f(x) \neq 0$ para $0 \leq x<2$.


## 1987 — 3.

**Record:** `esp_1987_ac6655`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_1987_ac6655.json.gz).

Sean $x_{1}, x_{2}, \ldots, x_{n}$, números reales que cumplen $x_{1}^{2}+x_{2}^{2}+\cdots+x_{n}^{2}=1$. Demostrar que para cada entero $k \geq 2$ existen enteros no todos nulos $a_{1}, a_{2}, \ldots, a_{n}$, tales que $\left|a_{i}\right| \leq k-1$ para todo $i$ y
$$
\left|a_{1} x_{1}+a_{2} x_{2}+\cdots+a_{n} x_{n}\right| \leq \frac{(k-1) \sqrt{n}}{k^{n}-1}
$$


## 2005 — 3

**Record:** `usa_2005_329553`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2005_329553.json.gz).

$$
\frac{x^5 - x^2}{x^5 + y^2 + z^2} + \frac{y^5 - y^2}{y^5 + z^2 + x^2} + \frac{z^5 - z^2}{z^5 + x^2 + y^2} \ge 0.
$$


## 2006 — 5

**Record:** `usa_2006_0b18ef`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2006_0b18ef.json.gz).

Let $P(x)$ be a polynomial of degree $n > 1$ with integer coefficients and let $k$ be a positive integer. Consider the polynomial
$$
Q(x) = \underbrace{P(P(\dots(P(x)\dots)))}_{k \text{ P's}}
$$
Prove that there are at most $n$ integers $t$ such that $Q(t) = t$.


## 2008 — 4

**Record:** `usa_2008_b4961a`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2008_b4961a.json.gz).

Determine all functions $f : (0, \infty) \to (0, \infty)$ such that
$$
\frac{(f(p))^2 + (f(q))^2}{f(r^2) + f(s^2)} = \frac{p^2 + q^2}{r^2 + s^2}
$$
for all positive real numbers $p$, $q$, $r$, $s$ satisfying $pq = rs$.


## 2009 — 5

**Record:** `usa_2009_ed888c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2009_ed888c.json.gz).

Determine all functions $f$ from the set of positive integers to the set of positive integers such that, for all positive integers $a$ and $b$, there exists a non-degenerate triangle with sides of lengths $a$, $f(b)$ and $f(b+f(a)-1)$.


## 2014 — 1

**Record:** `esp_2014_460932`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_2014_460932.json.gz).

Sea $a_0 < a_1 < a_2 < \dots$ una sucesión infinita de números enteros positivos.
Demostrar que existe un único entero $n \ge 1$ tal que
$$
a_n < \frac{a_0 + a_1 + a_2 + \dots + a_n}{n} \le a_{n+1}.
$$


## 2014 — Exercice 8

**Record:** `fra_2014_55d6e2`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/france/fra_2014_55d6e2.json.gz).

Déterminer toutes les fonctions $f: \mathbb{R}_{+}^{*} \longmapsto \mathbb{R}_{+}^{*}$ telles que
$$
f\left(\frac{y}{f(x+1)}\right)+f\left(\frac{x+1}{x f(y)}\right)=f(y)
$$
pour tous $x, y \in \mathbb{R}_{+}^{*}$.


## 2014 — Exercice 10

**Record:** `fra_2014_8e92eb`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/france/fra_2014_8e92eb.json.gz).

Déterminer tous les polynômes $P$ à coefficients entiers pour lesquels l'ensemble $P(\mathbb{N})$ contient une suite géométrique infinie de raison $a$ avec $a \notin\{-1,0,1\}$ et de premier terme non nul.



# IMO-SL source statements

## 2006 — A3

**Record:** `imo_2006_272963`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_272963.json.gz).

The sequence $c_{0}, c_{1}, \ldots, c_{n}, \ldots$ is defined by $c_{0}=1$, $c_{1}=0$ and $c_{n+2}=c_{n+1}+c_{n}$ for $n \geq 0$. Consider the set $S$ of ordered pairs $(x, y)$ for which there is a finite set $J$ of positive integers such that $x=\sum_{j \in J} c_{j}$, $y=\sum_{j \in J} c_{j-1}$. Prove that there exist real numbers $\alpha$, $\beta$ and $m$, $M$ with the following property: An ordered pair of nonnegative integers $(x, y)$ satisfies the inequality
$$
m<\alpha x+\beta y<M
$$
if and only if $(x, y) \in S$.

N. B. A sum over the elements of the empty set is assumed to be $0$.


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


## 2006 — C7

**Record:** `imo_2006_47470d`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_47470d.json.gz).

Consider a convex polyhedron without parallel edges and without an edge parallel to any face other than the two faces adjacent to it.
Call a pair of points of the polyhedron antipodal if there exist two parallel planes passing through these points and such that the polyhedron is contained between these planes.
Let $A$ be the number of antipodal pairs of vertices, and let $B$ be the number of antipodal pairs of midpoints of edges. Determine the difference $A-B$ in terms of the numbers of vertices, edges and faces.


## 2006 — A6

**Record:** `imo_2006_778dd2`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_778dd2.json.gz).

Determine the smallest number $M$ such that the inequality
$$
\left|a b\left(a^{2}-b^{2}\right)+b c\left(b^{2}-c^{2}\right)+c a\left(c^{2}-a^{2}\right)\right| \leq M\left(a^{2}+b^{2}+c^{2}\right)^{2}
$$
holds for all real numbers $a, b, c$.


## 2006 — A5

**Record:** `imo_2006_b08bab`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_b08bab.json.gz).

Let $a, b, c$ be the sides of a triangle. Prove that
$$
\frac{\sqrt{b+c-a}}{\sqrt{b}+\sqrt{c}-\sqrt{a}}+\frac{\sqrt{c+a-b}}{\sqrt{c}+\sqrt{a}-\sqrt{b}}+\frac{\sqrt{a+b-c}}{\sqrt{a}+\sqrt{b}-\sqrt{c}} \leq 3 .
$$


## 2006 — C5

**Record:** `imo_2006_b88369`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_b88369.json.gz).

An $(n, k)$-tournament is a contest with $n$ players held in $k$ rounds such that:
(i) Each player plays in each round, and every two players meet at most once.
(ii) If player $A$ meets player $B$ in round $i$, player $C$ meets player $D$ in round $i$, and player $A$ meets player $C$ in round $j$, then player $B$ meets player $D$ in round $j$.
Determine all pairs $(n, k)$ for which there exists an $(n, k)$-tournament.


## 2006 — N4

**Record:** `imo_2006_bf7806`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_bf7806.json.gz).

Let $P$ be a polynomial of degree $n>1$ with integer coefficients and let $k$ be any positive integer. Consider the polynomial $Q(x)=P(P(\ldots P(P(x)) \ldots))$, with $k$ pairs of parentheses. Prove that $Q$ has no more than $n$ integer fixed points, i.e. integers satisfying the equation $Q(x)=x$.
(Romania)


## 2006 — C1

**Record:** `imo_2006_dccdc3`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_dccdc3.json.gz).

We have $n \geq 2$ lamps $L_{1}, \ldots, L_{n}$ in a row, each of them being either on or off. Every second we simultaneously modify the state of each lamp as follows:
- if the lamp $L_{i}$ and its neighbours (only one neighbour for $i=1$ or $i=n$, two neighbours for other $i$) are in the same state, then $L_{i}$ is switched off;
- otherwise, $L_{i}$ is switched on.
Initially all the lamps are off except the leftmost one which is on.

a. Prove that there are infinitely many integers $n$ for which all the lamps will eventually be off.

b. Prove that there are infinitely many integers $n$ for which the lamps will never be all off.


## 2006 — A2

**Record:** `imo_2006_e18476`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_e18476.json.gz).

The sequence of real numbers $a_{0}, a_{1}, a_{2}, \ldots$ is defined recursively by
$$
a_{0}=-1, \quad \sum_{k=0}^{n} \frac{a_{n-k}}{k+1}=0 \quad \text{ for } \quad n \geq 1
$$
Show that $a_{n}>0$ for $n \geq 1$.


## 2006 — A1

**Record:** `imo_2006_e3e5ce`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_e3e5ce.json.gz).

**Source issue:** The negative two-cycle partner is -1-a, not 1-a. Corrected in A03.

A sequence of real numbers $a_{0}, a_{1}, a_{2}, \ldots$ is defined by the formula
$$
a_{i+1}=\left\lfloor a_{i}\right\rfloor \cdot\left\langle a_{i}\right\rangle \quad \text{ for } \quad i \geq 0
$$
here $a_{0}$ is an arbitrary real number, $\left\lfloor a_{i}\right\rfloor$ denotes the greatest integer not exceeding $a_{i}$, and $\left\langle a_{i}\right\rangle=a_{i}-\left\lfloor a_{i}\right\rfloor$. Prove that $a_{i}=a_{i+2}$ for $i$ sufficiently large.


## 2006 — A4

**Record:** `imo_2006_e510c0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_e510c0.json.gz).

Prove the inequality
$$
\sum_{i<j} \frac{a_{i} a_{j}}{a_{i}+a_{j}} \leq \frac{n}{2\left(a_{1}+a_{2}+\cdots+a_{n}\right)} \sum_{i<j} a_{i} a_{j}
$$
for positive real numbers $a_{1}, a_{2}, \ldots, a_{n}$.


## 2006 — C3

**Record:** `imo_2006_f50971`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_f50971.json.gz).

Let $S$ be a finite set of points in the plane such that no three of them are on a line. For each convex polygon $P$ whose vertices are in $S$, let $a(P)$ be the number of vertices of $P$, and let $b(P)$ be the number of points of $S$ which are outside $P$. Prove that for every real number $x$
$$
\sum_{P} x^{a(P)}(1-x)^{b(P)}=1,
$$
where the sum is taken over all convex polygons with vertices in $S$.

NB. A line segment, a point and the empty set are considered as convex polygons of 2, 1 and 0 vertices, respectively.


## 2006 — N3

**Record:** `imo_2006_ffa2b8`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_ffa2b8.json.gz).

The sequence $f(1), f(2), f(3), \ldots$ is defined by
$$
f(n)=\frac{1}{n}\left(\left\lfloor\frac{n}{1}\right\rfloor+\left\lfloor\frac{n}{2}\right\rfloor+\cdots+\left\lfloor\frac{n}{n}\right\rfloor\right),
$$
where $\lfloor x\rfloor$ denotes the integer part of $x$.

a. Prove that $f(n+1)>f(n)$ infinitely often.

b. Prove that $f(n+1)<f(n)$ infinitely often.


## 2007 — C1

**Record:** `imo_2007_09542d`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_09542d.json.gz).

Let $n > 1$ be an integer. Find all sequences $a_{1}, a_{2}, \ldots, a_{n^{2}+n}$ satisfying the following conditions:
(a) $a_{i} \in \{0,1\}$ for all $1 \leq i \leq n^{2}+n$;
(b) $a_{i+1}+a_{i+2}+\ldots+a_{i+n} < a_{i+n+1}+a_{i+n+2}+\ldots+a_{i+2n}$ for all $0 \leq i \leq n^{2}-n$.


## 2007 — N1

**Record:** `imo_2007_16b745`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_16b745.json.gz).

Find all pairs $(k, n)$ of positive integers for which $7^{k}-3^{n}$ divides $k^{4}+n^{2}$.


## 2007 — A1

**Record:** `imo_2007_524a29`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_524a29.json.gz).

Given a sequence $a_{1}, a_{2}, \ldots, a_{n}$ of real numbers. For each $i$ ($1 \leq i \leq n$) define
$$
d_{i}=\max \{a_{j}: 1 \leq j \leq i\}-\min \{a_{j}: i \leq j \leq n\}
$$
and let
$$
d=\max \{d_{i}: 1 \leq i \leq n\} .
$$

a. Prove that for arbitrary real numbers $x_{1} \leq x_{2} \leq \ldots \leq x_{n}$,
$$
\max \{\left|x_{i}-a_{i}\right|: 1 \leq i \leq n\} \geq \frac{d}{2} . \tag{1}
$$

b. Show that there exists a sequence $x_{1} \leq x_{2} \leq \ldots \leq x_{n}$ of real numbers such that we have equality in (1).


## 2007 — A2

**Record:** `imo_2007_d1b775`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_d1b775.json.gz).

Consider those functions $f: \mathbb{N} \rightarrow \mathbb{N}$ which satisfy the condition
$$
f(m+n) \geq f(m)+f(f(n))-1
$$
for all $m, n \in \mathbb{N}$. Find all possible values of $f(2007)$.

($\mathbb{N}$ denotes the set of all positive integers.)


## 2007 — N4

**Record:** `imo_2007_f1ecad`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_f1ecad.json.gz).

For every integer $k \geq 2$, prove that $2^{3k}$ divides the number
$$
\binom{2^{k+1}}{2^{k}} - \binom{2^{k}}{2^{k-1}}
$$


## 2008 — N3

**Record:** `imo_2008_032bdc`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_032bdc.json.gz).

Let $a_{0}, a_{1}, a_{2}, \ldots$ be a sequence of positive integers such that the greatest common divisor of any two consecutive terms is greater than the preceding term; in symbols, $\operatorname{gcd}\left(a_{i}, a_{i+1}\right)>a_{i-1}$. Prove that $a_{n} \geq 2^{n}$ for all $n \geq 0$.


## 2008 — A4

**Record:** `imo_2008_4e4b33`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_4e4b33.json.gz).

For an integer $m$, denote by $t(m)$ the unique number in $\{1,2,3\}$ such that $m+t(m)$ is a multiple of $3$. A function $f: \mathbb{Z} \rightarrow \mathbb{Z}$ satisfies $f(-1)=0$, $f(0)=1$, $f(1)=-1$ and
$$
f\left(2^{n}+m\right)=f\left(2^{n}-t(m)\right)-f(m) \quad \text{ for all integers } m, n \geq 0 \text{ with } 2^{n}>m.
$$

Prove that $f(3p) \geq 0$ holds for all integers $p \geq 0$.


## 2008 — A5

**Record:** `imo_2008_62a5e7`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_62a5e7.json.gz).

Let $a$, $b$, $c$, $d$ be positive real numbers such that
$$
a b c d = 1 \quad \text{ and } \quad a + b + c + d > \frac{a}{b} + \frac{b}{c} + \frac{c}{d} + \frac{d}{a}
$$
Prove that
$$
a + b + c + d < \frac{b}{a} + \frac{c}{b} + \frac{d}{c} + \frac{a}{d}
$$


## 2008 — A6

**Record:** `imo_2008_96b2a5`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_96b2a5.json.gz).

Let $f: \mathbb{R} \rightarrow \mathbb{N}$ be a function which satisfies
$$
f\left(x+\frac{1}{f(y)}\right)=f\left(y+\frac{1}{f(x)}\right) \quad \text{ for all } x, y \in \mathbb{R}
$$
Prove that there is a positive integer which is not a value of $f$.


## 2008 — A7

**Record:** `imo_2008_a5a178`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_a5a178.json.gz).

Prove that for any four positive real numbers $a$, $b$, $c$, $d$ the inequality
$$
\frac{(a-b)(a-c)}{a+b+c}+\frac{(b-c)(b-d)}{b+c+d}+\frac{(c-d)(c-a)}{c+d+a}+\frac{(d-a)(d-b)}{d+a+b} \geq 0
$$
holds. Determine all cases of equality.


## 2008 — A3

**Record:** `imo_2008_ac4e9a`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_ac4e9a.json.gz).

Let $S \subseteq \mathbb{R}$ be a set of real numbers. We say that a pair $(f, g)$ of functions from $S$ into $S$ is a Spanish Couple on $S$, if they satisfy the following conditions:
(i) Both functions are strictly increasing, i.e. $f(x) < f(y)$ and $g(x) < g(y)$ for all $x, y \in S$ with $x < y$;
(ii) The inequality $f(g(g(x))) < g(f(x))$ holds for all $x \in S$.
Decide whether there exists a Spanish Couple

a. on the set $S = \mathbb{N}$ of positive integers;
b. on the set $S = \{ a - 1 / b : a, b \in \mathbb{N} \}$.


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


## 2009 — C2

**Record:** `imo_2009_7c4eea`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2009_7c4eea.json.gz).

For any integer $n \geq 2$, let $N(n)$ be the maximal number of triples $(a_{i}, b_{i}, c_{i})$, $i=1, \ldots, N(n)$, consisting of nonnegative integers $a_{i}, b_{i}$ and $c_{i}$ such that the following two conditions are satisfied:
(1) $a_{i}+b_{i}+c_{i}=n$ for all $i=1, \ldots, N(n)$,
(2) If $i \neq j$, then $a_{i} \neq a_{j}, b_{i} \neq b_{j}$ and $c_{i} \neq c_{j}$.
Determine $N(n)$ for all $n \geq 2$.


## 2009 — A2

**Record:** `imo_2009_c42bed`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2009_c42bed.json.gz).

Let $a$, $b$, $c$ be positive real numbers such that $\frac{1}{a} + \frac{1}{b} + \frac{1}{c} = a + b + c$. Prove that
$$
\frac{1}{(2a + b + c)^2} + \frac{1}{(2b + c + a)^2} + \frac{1}{(2c + a + b)^2} \leq \frac{3}{16}
$$


## 2009 — C4

**Record:** `imo_2009_c91ba6`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2009_c91ba6.json.gz).

For an integer $m \geq 1$, we consider partitions of a $2^{m} \times 2^{m}$ chessboard into rectangles consisting of cells of the chessboard, in which each of the $2^{m}$ cells along one diagonal forms a separate rectangle of side length 1. Determine the smallest possible sum of rectangle perimeters in such a partition.


## 2010 — A5

**Record:** `imo_2010_18587d`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2010_18587d.json.gz).

Denote by $\mathbb{Q}^{+}$ the set of all positive rational numbers. Determine all functions $f: \mathbb{Q}^{+} \rightarrow \mathbb{Q}^{+}$ which satisfy the following equation for all $x, y \in \mathbb{Q}^{+}$:
$$
f\left(f(x)^{2} y\right)=x^{3} f(x y)
$$


## 2010 — A7

**Record:** `imo_2010_237f4c`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2010_237f4c.json.gz).

Let $a_{1}, \ldots, a_{r}$ be positive real numbers. For $n>r$, we inductively define
$$
a_{n}=\max _{1 \leq k \leq n-1}\left(a_{k}+a_{n-k}\right) \tag{1}
$$
Prove that there exist positive integers $\ell \leq r$ and $N$ such that $a_{n}=a_{n-\ell}+a_{\ell}$ for all $n \geq N$.


## 2010 — A8

**Record:** `imo_2010_3205ec`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2010_3205ec.json.gz).

Given six positive numbers $a, b, c, d, e, f$ such that $a < b < c < d < e < f$. Let $a + c + e = S$ and $b + d + f = T$. Prove that
$$
2 S T > \sqrt{3(S + T)(S(b d + b f + d f) + T(a c + a e + c e))}
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


## 2010 — A2

**Record:** `imo_2010_66cdab`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2010_66cdab.json.gz).

Let the real numbers $a, b, c, d$ satisfy the relations $a+b+c+d=6$ and $a^{2}+b^{2}+c^{2}+d^{2}=12$. Prove that
$$
36 \leq 4\left(a^{3}+b^{3}+c^{3}+d^{3}\right)-\left(a^{4}+b^{4}+c^{4}+d^{4}\right) \leq 48
$$


## 2010 — N5

**Record:** `imo_2010_970d18`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2010_970d18.json.gz).

Let $\mathbb{N}$ be the set of all positive integers. Find all functions $f: \mathbb{N} \rightarrow \mathbb{N}$ such that the number $(f(m)+n)(m+f(n))$ is a square for all $m, n \in \mathbb{N}$.
(U.S.A.)


## 2010 — A4

**Record:** `imo_2010_abf386`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2010_abf386.json.gz).

A sequence $x_{1}, x_{2}, \ldots$ is defined by $x_{1}=1$ and $x_{2k}=-x_{k}$, $x_{2k-1}=(-1)^{k+1} x_{k}$ for all $k \geq 1$. Prove that $x_{1}+x_{2}+\cdots+x_{n} \geq 0$ for all $n \geq 1$.


## 2010 — N4

**Record:** `imo_2010_ae862f`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2010_ae862f.json.gz).

Let $a, b$ be integers, and let $P(x) = a x^{3} + b x$. For any positive integer $n$ we say that the pair $(a, b)$ is $n$-good if $n \mid P(m) - P(k)$ implies $n \mid m - k$ for all integers $m, k$. We say that $(a, b)$ is very good if $(a, b)$ is $n$-good for infinitely many positive integers $n$.

a. Find a pair $(a, b)$ which is $51$-good, but not very good.

b. Show that all $2010$-good pairs are very good.

(Turkey)


## 2010 — A6

**Record:** `imo_2010_c795de`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2010_c795de.json.gz).

Suppose that $f$ and $g$ are two functions defined on the set of positive integers and taking positive integer values. Suppose also that the equations $f(g(n))=f(n)+1$ and $g(f(n))= g(n)+1$ hold for all positive integers. Prove that $f(n)=g(n)$ for all positive integer $n$.


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


## 2011 — A2

**Record:** `imo_2011_5fba9c`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2011_5fba9c.json.gz).

Determine all sequences $\left(x_{1}, x_{2}, \ldots, x_{2011}\right)$ of positive integers such that for every positive integer $n$ there is an integer $a$ with
$$
x_{1}^{n}+2 x_{2}^{n}+\cdots+2011 x_{2011}^{n}=a^{n+1}+1 .
$$


## 2011 — N6

**Record:** `imo_2011_b111da`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2011_b111da.json.gz).

Let $P(x)$ and $Q(x)$ be two polynomials with integer coefficients such that no nonconstant polynomial with rational coefficients divides both $P(x)$ and $Q(x)$. Suppose that for every positive integer $n$ the integers $P(n)$ and $Q(n)$ are positive, and $2^{Q(n)}-1$ divides $3^{P(n)}-1$. Prove that $Q(x)$ is a constant polynomial.


## 2011 — A4

**Record:** `imo_2011_d1d467`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2011_d1d467.json.gz).

Determine all pairs $(f, g)$ of functions from the set of positive integers to itself that satisfy
$$
f^{g(n)+1}(n) + g^{f(n)}(n) = f(n+1) - g(n+1) + 1
$$
for every positive integer $n$. Here, $f^{k}(n)$ means $\underbrace{f(f(\ldots f}_{k}(n) \ldots))$.


## 2011 — N3

**Record:** `imo_2011_f26960`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2011_f26960.json.gz).

Let $n \geq 1$ be an odd integer. Determine all functions $f$ from the set of integers to itself such that for all integers $x$ and $y$ the difference $f(x)-f(y)$ divides $x^{n}-y^{n}$.


## 2012 — C3

**Record:** `imo_2012_16a6fb`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2012_16a6fb.json.gz).

In a $999 \times 999$ square table some cells are white and the remaining ones are red. Let $T$ be the number of triples $(C_{1}, C_{2}, C_{3})$ of cells, the first two in the same row and the last two in the same column, with $C_{1}$ and $C_{3}$ white and $C_{2}$ red. Find the maximum value $T$ can attain.


## 2012 — C2

**Record:** `imo_2012_2dedb8`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2012_2dedb8.json.gz).

Let $n \geq 1$ be an integer. What is the maximum number of disjoint pairs of elements of the set $\{1,2, \ldots, n\}$ such that the sums of the different pairs are different integers not exceeding $n$?


## 2012 — N8

**Record:** `imo_2012_35e1cc`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2012_35e1cc.json.gz).

Prove that for every prime $p > 100$ and every integer $r$ there exist two integers $a$ and $b$ such that $p$ divides $a^{2} + b^{5} - r$.


## 2013 — C5

**Record:** `imo_2013_34622f`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_34622f.json.gz).

Let $r$ be a positive integer, and let $a_{0}, a_{1}, \ldots$ be an infinite sequence of real numbers. Assume that for all nonnegative integers $m$ and $s$ there exists a positive integer $n \in [m+1, m+r]$ such that
$$
a_{m}+a_{m+1}+\cdots+a_{m+s}=a_{n}+a_{n+1}+\cdots+a_{n+s}
$$
Prove that the sequence is periodic, i.e. there exists some $p \geqslant 1$ such that $a_{n+p}=a_{n}$ for all $n \geqslant 0$.


## 2013 — C1

**Record:** `imo_2013_4d15d8`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_4d15d8.json.gz).

Let $n$ be a positive integer. Find the smallest integer $k$ with the following property: Given any real numbers $a_{1}, \ldots, a_{d}$ such that $a_{1}+a_{2}+\cdots+a_{d}=n$ and $0 \leqslant a_{i} \leqslant 1$ for $i=1,2, \ldots, d$, it is possible to partition these numbers into $k$ groups (some of which may be empty) such that the sum of the numbers in each group is at most $1$.


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


## 2013 — A6

**Record:** `imo_2013_b1d43a`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_b1d43a.json.gz).

Let $m \neq 0$ be an integer. Find all polynomials $P(x)$ with real coefficients such that
$$
\left(x^{3}-m x^{2}+1\right) P(x+1)+\left(x^{3}+m x^{2}+1\right) P(x-1)=2\left(x^{3}-m x+1\right) P(x)
$$
for all real numbers $x$.


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


## 2013 — A1

**Record:** `imo_2013_d960d1`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_d960d1.json.gz).

**Source issue:** The recovered statement omits v_1=1 in one initialization. Supplied explicitly in A06.

Let $n$ be a positive integer and let $a_{1}, \ldots, a_{n-1}$ be arbitrary real numbers. Define the sequences $u_{0}, \ldots, u_{n}$ and $v_{0}, \ldots, v_{n}$ inductively by $u_{0}=u_{1}=v_{0}=1$, and
$$
u_{k+1}=u_{k}+a_{k} u_{k-1}, \quad v_{k+1}=v_{k}+a_{n-k} v_{k-1} \quad \text{ for } k=1, \ldots, n-1 .$$
Prove that $u_{n}=v_{n}$.


## 2014 — C8

**Record:** `imo_2014_09db9c`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2014_09db9c.json.gz).

A card deck consists of 1024 cards. On each card, a set of distinct decimal digits is written in such a way that no two of these sets coincide (thus, one of the cards is empty). Two players alternately take cards from the deck, one card per turn. After the deck is empty, each player checks if he can throw out one of his cards so that each of the ten digits occurs on an even number of his remaining cards. If one player can do this but the other one cannot, the one who can is the winner; otherwise a draw is declared.
Determine all possible first moves of the first player after which he has a winning strategy.


## 2014 — A3

**Record:** `imo_2014_4fbd86`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2014_4fbd86.json.gz).

For a sequence $x_{1}, x_{2}, \ldots, x_{n}$ of real numbers, we define its price as
$$
\max_{1 \leqslant i \leqslant n}\left|x_{1}+\cdots+x_{i}\right| .
$$
Given $n$ real numbers, Dave and George want to arrange them into a sequence with a low price. Diligent Dave checks all possible ways and finds the minimum possible price $D$. Greedy George, on the other hand, chooses $x_{1}$ such that $\left|x_{1}\right|$ is as small as possible; among the remaining numbers, he chooses $x_{2}$ such that $\left|x_{1}+x_{2}\right|$ is as small as possible, and so on. Thus, in the $i^{\text {th }}$ step he chooses $x_{i}$ among the remaining numbers so as to minimise the value of $\left|x_{1}+x_{2}+\cdots+x_{i}\right|$. In each step, if several numbers provide the same value, George chooses one at random. Finally he gets a sequence with price $G$.
Find the least possible constant $c$ such that for every positive integer $n$, for every collection of $n$ real numbers, and for every possible sequence that George might obtain, the resulting values satisfy the inequality $G \leqslant c D$.


## 2014 — A1

**Record:** `imo_2014_6534d6`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2014_6534d6.json.gz).

Let $z_{0} < z_{1} < z_{2} < \cdots$ be an infinite sequence of positive integers. Prove that there exists a unique integer $n \geqslant 1$ such that
$$
z_{n} < \frac{z_{0} + z_{1} + \cdots + z_{n}}{n} \leqslant z_{n+1} .
$$


## 2014 — N6

**Record:** `imo_2014_da4751`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2014_da4751.json.gz).

Let $a_{1} < a_{2} < \cdots < a_{n}$ be pairwise coprime positive integers with $a_{1}$ being prime and $a_{1} \geqslant n+2$. On the segment $I = [0, a_{1} a_{2} \cdots a_{n}]$ of the real line, mark all integers that are divisible by at least one of the numbers $a_{1}, \ldots, a_{n}$. These points split $I$ into a number of smaller segments. Prove that the sum of the squares of the lengths of these segments is divisible by $a_{1}$.


## 2015 — A3

**Record:** `imo_2015_0b0e39`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2015_0b0e39.json.gz).

Let $n$ be a fixed positive integer. Find the maximum possible value of
$$
\sum_{1 \leqslant r<s \leqslant 2 n}(s-r-n) x_{r} x_{s}
$$
where $-1 \leqslant x_{i} \leqslant 1$ for all $i=1,2, \ldots, 2 n$.


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


## 2015 — A6

**Record:** `imo_2015_8f5283`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2015_8f5283.json.gz).

Let $n$ be a fixed integer with $n \geqslant 2$. We say that two polynomials $P$ and $Q$ with real coefficients are block-similar if for each $i \in\{1,2, \ldots, n\}$ the sequences
$$
\begin{aligned}
& P(2015 i), P(2015 i-1), \ldots, P(2015 i-2014) \quad \text{ and } \\
& Q(2015 i), Q(2015 i-1), \ldots, Q(2015 i-2014)
\end{aligned}
$$
are permutations of each other.

a. Prove that there exist distinct block-similar polynomials of degree $n+1$.

b. Prove that there do not exist distinct block-similar polynomials of degree $n$.


## 2015 — C5

**Record:** `imo_2015_bab8ff`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2015_bab8ff.json.gz).

Consider an infinite sequence $a_{1}, a_{2}, \ldots$ of positive integers with $a_{i} \leqslant 2015$ for all $i \geqslant 1$. Suppose that for any two distinct indices $i$ and $j$ we have $i+a_{i} \neq j+a_{j}$.
Prove that there exist two positive integers $b$ and $N$ such that
$$
\left|\sum_{i=m+1}^{n}\left(a_{i}-b\right)\right| \leqslant 1007^{2}
$$
whenever $n>m \geqslant N$.


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


## 2016 — A3

**Record:** `imo_2016_b6b418`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2016_b6b418.json.gz).

Find all integers $n \geqslant 3$ with the following property: for all real numbers $a_{1}, a_{2}, \ldots, a_{n}$ and $b_{1}, b_{2}, \ldots, b_{n}$ satisfying $\left|a_{k}\right|+\left|b_{k}\right|=1$ for $1 \leqslant k \leqslant n$, there exist $x_{1}, x_{2}, \ldots, x_{n}$, each of which is either $-1$ or $1$, such that
$$
\left|\sum_{k=1}^{n} x_{k} a_{k}\right|+\left|\sum_{k=1}^{n} x_{k} b_{k}\right| \leqslant 1
$$


## 2016 — A8

**Record:** `imo_2016_d18840`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2016_d18840.json.gz).

Determine the largest real number $a$ such that for all $n \geqslant 1$ and for all real numbers $x_{0}, x_{1}, \ldots, x_{n}$ satisfying $0=x_{0}<x_{1}<x_{2}<\cdots<x_{n}$, we have
$$
\frac{1}{x_{1}-x_{0}}+\frac{1}{x_{2}-x_{1}}+\cdots+\frac{1}{x_{n}-x_{n-1}} \geqslant a\left(\frac{2}{x_{1}}+\frac{3}{x_{2}}+\cdots+\frac{n+1}{x_{n}}\right)
$$


## 2016 — N8

**Record:** `imo_2016_fa5aef`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2016_fa5aef.json.gz).

Find all polynomials $P(x)$ of odd degree $d$ and with integer coefficients satisfying the following property: for each positive integer $n$, there exist $n$ positive integers $x_{1}, x_{2}, \ldots, x_{n}$ such that $\frac{1}{2}<\frac{P\left(x_{i}\right)}{P\left(x_{j}\right)}<2$ and $\frac{P\left(x_{i}\right)}{P\left(x_{j}\right)}$ is the $d$-th power of a rational number for every pair of indices $i$ and $j$ with $1 \leqslant i, j \leqslant n$.


## 2017 — A5

**Record:** `imo_2017_38c1ed`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2017_38c1ed.json.gz).

An integer $n \geqslant 3$ is given. We call an $n$-tuple of real numbers $(x_{1}, x_{2}, \ldots, x_{n})$ Shiny if for each permutation $y_{1}, y_{2}, \ldots, y_{n}$ of these numbers we have
$$
\sum_{i=1}^{n-1} y_{i} y_{i+1} = y_{1} y_{2} + y_{2} y_{3} + y_{3} y_{4} + \cdots + y_{n-1} y_{n} \geqslant -1.
$$
Find the largest constant $K = K(n)$ such that
$$
\sum_{1 \leqslant i < j \leqslant n} x_{i} x_{j} \geqslant K
$$
holds for every Shiny $n$-tuple $(x_{1}, x_{2}, \ldots, x_{n})$.


## 2017 — C7

**Record:** `imo_2017_403e3f`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2017_403e3f.json.gz).

For any finite sets $X$ and $Y$ of positive integers, denote by $f_{X}(k)$ the $k^{	ext{th}}$ smallest positive integer not in $X$, and let
$$
X * Y = X \cup \{ f_{X}(y) : y \in Y \} .
$$
Let $A$ be a set of $a > 0$ positive integers, and let $B$ be a set of $b > 0$ positive integers. Prove that if $A * B = B * A$, then
$$
\underbrace{A *(A * \cdots *(A *(A * A)) \ldots)}_{A \text{ appears } b \text{ times }} = \underbrace{B *(B * \cdots *(B *(B * B)) \ldots)}_{B \text{ appears } a \text{ times }} . \tag{U.S.A.}
$$


## 2017 — A1

**Record:** `imo_2017_5b8561`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2017_5b8561.json.gz).

Let $a_{1}, a_{2}, \ldots, a_{n}, k$, and $M$ be positive integers such that
$$
\frac{1}{a_{1}}+\frac{1}{a_{2}}+\cdots+\frac{1}{a_{n}}=k \quad \text{ and } \quad a_{1} a_{2} \ldots a_{n}=M .
$$
If $M>1$, prove that the polynomial
$$
P(x)=M(x+1)^{k}-\left(x+a_{1}\right)\left(x+a_{2}\right) \cdots\left(x+a_{n}\right)
$$
has no positive roots.


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


## 2018 — C4

**Record:** `imo_2018_55614a`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2018_55614a.json.gz).

An anti-Pascal pyramid is a finite set of numbers, placed in a triangle-shaped array so that the first row of the array contains one number, the second row contains two numbers, the third row contains three numbers and so on; and, except for the numbers in the bottom row, each number equals the absolute value of the difference of the two numbers below it. For instance, the triangle below is an anti-Pascal pyramid with four rows, in which every integer from 1 to $1+2+3+4=10$ occurs exactly once:
$$
\begin{aligned}
& 4 \\
& 2\ 6 \\
& 5\ 7\ 1 \\
& 8\ 3\ 10\ 9 .
\end{aligned}
$$
Is it possible to form an anti-Pascal pyramid with 2018 rows, using every integer from 1 to $1+2+\cdots+2018$ exactly once?


## 2018 — C5

**Record:** `imo_2018_b7dcfb`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2018_b7dcfb.json.gz).

Let $k$ be a positive integer. The organising committee of a tennis tournament is to schedule the matches for $2k$ players so that every two players play once, each day exactly one match is played, and each player arrives to the tournament site the day of his first match, and departs the day of his last match. For every day a player is present on the tournament, the committee has to pay 1 coin to the hotel. The organisers want to design the schedule so as to minimise the total cost of all players' stays. Determine this minimum cost.


## 2018 — A5

**Record:** `imo_2018_d26063`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2018_d26063.json.gz).

Determine all functions $f:(0, \infty) \rightarrow \mathbb{R}$ satisfying
$$
\left(x+\frac{1}{x}\right) f(y)=f(x y)+f\left(\frac{y}{x}\right)
$$
for all $x, y>0$.


## 2018 — A6

**Record:** `imo_2018_f30e16`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2018_f30e16.json.gz).

Let $m, n \geqslant 2$ be integers. Let $f\left(x_{1}, \ldots, x_{n}\right)$ be a polynomial with real coefficients such that
$$
f\left(x_{1}, \ldots, x_{n}\right)=\left\lfloor\frac{x_{1}+\ldots+x_{n}}{m}\right\rfloor \text{ for every } x_{1}, \ldots, x_{n} \in\{0,1, \ldots, m-1\} .
$$
Prove that the total degree of $f$ is at least $n$.


## 2019 — N3

**Record:** `imo_2019_05dd86`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_05dd86.json.gz).

**Source issue:** Zero-polynomial convention would trivialize the closure condition; the substantive nonconstant version is made explicit in N10.

We say that a set $S$ of integers is rootiful if, for any positive integer $n$ and any $a_{0}, a_{1}, \ldots, a_{n} \in S$, all integer roots of the polynomial $a_{0}+a_{1} x+\cdots+a_{n} x^{n}$ are also in $S$. Find all rootiful sets of integers that contain all numbers of the form $2^{a}-2^{b}$ for positive integers $a$ and $b$.


## 2019 — A3

**Record:** `imo_2019_070c84`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_070c84.json.gz).

Let $n \geqslant 3$ be a positive integer and let $(a_{1}, a_{2}, \ldots, a_{n})$ be a strictly increasing sequence of $n$ positive real numbers with sum equal to $2$. Let $X$ be a subset of $\{1,2, \ldots, n\}$ such that the value of
$$
\left|1-\sum_{i \in X} a_{i}\right|
$$
is minimised. Prove that there exists a strictly increasing sequence of $n$ positive real numbers $(b_{1}, b_{2}, \ldots, b_{n})$ with sum equal to $2$ such that
$$
\sum_{i \in X} b_{i}=1
$$


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


## 2019 — A1

**Record:** `imo_2019_abb25c`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_abb25c.json.gz).

Let $\mathbb{Z}$ be the set of integers. Determine all functions $f: \mathbb{Z} \rightarrow \mathbb{Z}$ such that, for all integers $a$ and $b$,
$$
f(2a) + 2f(b) = f(f(a+b)).
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


## 2019 — A6

**Record:** `imo_2019_c89fae`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_c89fae.json.gz).

A polynomial $P(x, y, z)$ in three variables with real coefficients satisfies the identities
$$
P(x, y, z) = P(x, y, x y - z) = P(x, z x - y, z) = P(y z - x, y, z)
$$
Prove that there exists a polynomial $F(t)$ in one variable such that
$$
P(x, y, z) = F\left(x^{2} + y^{2} + z^{2} - x y z\right)
$$


## 2019 — N8

**Record:** `imo_2019_ca3568`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_ca3568.json.gz).

Let $a$ and $b$ be two positive integers. Prove that the integer
$$
a^{2} + \left\lceil \frac{4 a^{2}}{b} \right\rceil
$$
is not a square. (Here $\lceil z\rceil$ denotes the least integer greater than or equal to $z$.)


## 2019 — A2

**Record:** `imo_2019_cd6d5a`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_cd6d5a.json.gz).

Let $u_{1}, u_{2}, \ldots, u_{2019}$ be real numbers satisfying
$$
u_{1}+u_{2}+\cdots+u_{2019}=0 \quad \text{and} \quad u_{1}^{2}+u_{2}^{2}+\cdots+u_{2019}^{2}=1 .$$
Let $a=\min \left(u_{1}, u_{2}, \ldots, u_{2019}\right)$ and $b=\max \left(u_{1}, u_{2}, \ldots, u_{2019}\right)$. Prove that
$$
a b \leqslant-\frac{1}{2019}$$


## 2019 — N6

**Record:** `imo_2019_ce6a78`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_ce6a78.json.gz).

Let $H=\{\lfloor i \sqrt{2}\rfloor: i \in \mathbb{Z}_{>0}\}=\{1,2,4,5,7, \ldots\}$, and let $n$ be a positive integer. Prove that there exists a constant $C$ such that, if $A \subset\{1,2, \ldots, n\}$ satisfies $|A| \geqslant C \sqrt{n}$, then there exist $a, b \in A$ such that $a-b \in H$. (Here $\mathbb{Z}_{>0}$ is the set of positive integers, and $\lfloor z\rfloor$ denotes the greatest integer less than or equal to $z$.)


## 2019 — A4

**Record:** `imo_2019_db517d`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_db517d.json.gz).

Let $n \geqslant 2$ be a positive integer and $a_{1}, a_{2}, \ldots, a_{n}$ be real numbers such that
$$
a_{1}+a_{2}+\cdots+a_{n}=0 .
$$
Define the set $A$ by
$$
A=\left\{(i, j)\left|1 \leqslant i<j \leqslant n,\left|a_{i}-a_{j}\right| \geqslant 1\right\} .\right.
$$
Prove that, if $A$ is not empty, then
$$
\sum_{(i, j) \in A} a_{i} a_{j}<0 .
$$


## 2019 — A5

**Record:** `imo_2019_ef79a1`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_ef79a1.json.gz).

Let $x_{1}, x_{2}, \ldots, x_{n}$ be different real numbers. Prove that
$$
\sum_{1 \leqslant i \leqslant n} \prod_{j \neq i} \frac{1-x_{i} x_{j}}{x_{i}-x_{j}}= \begin{cases}0, & \text{ if } n \text{ is even } \\ 1, & \text{ if } n \text{ is odd }\end{cases}
$$


## 2020 — C1

**Record:** `imo_2020_19e099`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2020_19e099.json.gz).

Let $n$ be a positive integer. Find the number of permutations $a_{1}, a_{2}, \ldots, a_{n}$ of the sequence $1,2, \ldots, n$ satisfying
$$
a_{1} \leqslant 2 a_{2} \leqslant 3 a_{3} \leqslant \ldots \leqslant n a_{n}
$$


## 2020 — A7

**Record:** `imo_2020_20c7b8`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2020_20c7b8.json.gz).

Let $n$ and $k$ be positive integers. Prove that for $a_{1}, \ldots, a_{n} \in [1,2^{k}]$ one has
$$
\sum_{i=1}^{n} \frac{a_{i}}{\sqrt{a_{1}^{2}+\ldots+a_{i}^{2}}} \leqslant 4 \sqrt{k n}
$$


## 2020 — A4

**Record:** `imo_2020_43ccfa`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2020_43ccfa.json.gz).

Let $a$, $b$, $c$, $d$ be four real numbers such that $a \geqslant b \geqslant c \geqslant d > 0$ and $a + b + c + d = 1$. Prove that
$$
(a + 2b + 3c + 4d) a^{a} b^{b} c^{c} d^{d} < 1
$$


## 2020 — A1

**Record:** `imo_2020_48d762`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2020_48d762.json.gz).

**Source issue:** The checked A14 proves Version 1 only; an imported Version 2 comparison also repeats the wrong sign label.

Version 1. Let $n$ be a positive integer, and set $N=2^{n}$. Determine the smallest real number $a_{n}$ such that, for all real $x$,
$$
\sqrt[N]{\frac{x^{2 N}+1}{2}} \leqslant a_{n}(x-1)^{2}+x .
$$

Version 2. For every positive integer $N$, determine the smallest real number $b_{N}$ such that, for all real $x$,
$$
\sqrt[N]{\frac{x^{2 N}+1}{2}} \leqslant b_{N}(x-1)^{2}+x
$$
(Ireland)


## 2020 — A2

**Record:** `imo_2020_55a2c0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2020_55a2c0.json.gz).

Let $\mathcal{A}$ denote the set of all polynomials in three variables $x, y, z$ with integer coefficients. Let $\mathcal{B}$ denote the subset of $\mathcal{A}$ formed by all polynomials which can be expressed as
$$
(x+y+z) P(x, y, z)+(x y+y z+z x) Q(x, y, z)+x y z R(x, y, z)
$$
with $P, Q, R \in \mathcal{A}$. Find the smallest non-negative integer $n$ such that $x^{i} y^{j} z^{k} \in \mathcal{B}$ for all nonnegative integers $i, j, k$ satisfying $i+j+k \geqslant n$.
(Venezuela)


## 2020 — A8

**Record:** `imo_2020_839f00`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2020_839f00.json.gz).

Let $\mathbb{R}^{+}$ be the set of positive real numbers. Determine all functions $f: \mathbb{R}^{+} \rightarrow \mathbb{R}^{+}$ such that, for all positive real numbers $x$ and $y$,
$$
f(x+f(xy))+y=f(x)f(y)+1
$$


## 2020 — A5

**Record:** `imo_2020_b69121`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2020_b69121.json.gz).

A magician intends to perform the following trick. She announces a positive integer $n$, along with $2n$ real numbers $x_{1} < \ldots < x_{2n}$, to the audience. A member of the audience then secretly chooses a polynomial $P(x)$ of degree $n$ with real coefficients, computes the $2n$ values $P(x_{1}), \ldots, P(x_{2n})$, and writes down these $2n$ values on the blackboard in non-decreasing order. After that the magician announces the secret polynomial to the audience.
Can the magician find a strategy to perform such a trick?
(Luxembourg)


## 2020 — A3

**Record:** `imo_2020_db020b`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2020_db020b.json.gz).

Suppose that $a, b, c, d$ are positive real numbers satisfying $(a+c)(b+d)=a c+b d$. Find the smallest possible value of
$$
S=\frac{a}{b}+\frac{b}{c}+\frac{c}{d}+\frac{d}{a}
$$
(Israel)


## 2021 — A2

**Record:** `imo_2021_18d4a8`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_18d4a8.json.gz).

For every integer $n \geqslant 1$ consider the $n \times n$ table with entry $\left\lfloor\frac{ij}{n+1}\right\rfloor$ at the intersection of row $i$ and column $j$, for every $i=1, \ldots, n$ and $j=1, \ldots, n$. Determine all integers $n \geqslant 1$ for which the sum of the $n^{2}$ entries in the table is equal to $\frac{1}{4} n^{2}(n-1)$.


## 2021 — N4

**Record:** `imo_2021_1c3cfc`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_1c3cfc.json.gz).

Alice is given a rational number $r>1$ and a line with two points $B \neq R$, where point $R$ contains a red bead and point $B$ contains a blue bead. Alice plays a solitaire game by performing a sequence of moves. In every move, she chooses a (not necessarily positive) integer $k$, and a bead to move. If that bead is placed at point $X$, and the other bead is placed at $Y$, then Alice moves the chosen bead to point $X^{\prime}$ with $\overrightarrow{Y X^{\prime}}=r^{k} \overrightarrow{Y X}$.

Alice's goal is to move the red bead to the point $B$. Find all rational numbers $r>1$ such that Alice can reach her goal in at most 2021 moves.


## 2021 — A7

**Record:** `imo_2021_3f3928`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_3f3928.json.gz).

Let $n \geqslant 1$ be an integer, and let $x_{0}, x_{1}, \ldots, x_{n+1}$ be $n+2$ non-negative real numbers that satisfy $x_{i} x_{i+1}-x_{i-1}^{2} \geqslant 1$ for all $i=1,2, \ldots, n$. Show that
$$
x_{0}+x_{1}+\cdots+x_{n}+x_{n+1}>\left(\frac{2 n}{3}\right)^{3 / 2}
$$


## 2021 — C8

**Record:** `imo_2021_4e49c6`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_4e49c6.json.gz).

Determine the largest $N$ for which there exists a table $T$ of integers with $N$ rows and 100 columns that has the following properties:
(i) Every row contains the numbers $1,2, \ldots, 100$ in some order.
(ii) For any two distinct rows $r$ and $s$, there is a column $c$ such that $|T(r, c)-T(s, c)| \geqslant 2$.
Here $T(r, c)$ means the number at the intersection of the row $r$ and the column $c$.


## 2021 — A8

**Record:** `imo_2021_51a6a7`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_51a6a7.json.gz).

Determine all functions $f: \mathbb{R} \rightarrow \mathbb{R}$ that satisfy
$$
(f(a)-f(b))(f(b)-f(c))(f(c)-f(a))=f\left(a b^{2}+b c^{2}+c a^{2}\right)-f\left(a^{2} b+b^{2} c+c^{2} a\right)
$$
for all real numbers $a, b, c$.


## 2021 — G3

**Record:** `imo_2021_96bcae`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_96bcae.json.gz).

Version 1. Let $n$ be a fixed positive integer, and let $S$ be the set of points $(x, y)$ on the Cartesian plane such that both coordinates $x$ and $y$ are nonnegative integers smaller than $2n$ (thus $|S| = 4n^2$). Assume that $\mathcal{F}$ is a set consisting of $n^2$ quadrilaterals such that all their vertices lie in $S$, and each point in $S$ is a vertex of exactly one of the quadrilaterals in $\mathcal{F}$.
Determine the largest possible sum of areas of all $n^2$ quadrilaterals in $\mathcal{F}$.

Version 2. Let $n$ be a fixed positive integer, and let $S$ be the set of points $(x, y)$ on the Cartesian plane such that both coordinates $x$ and $y$ are nonnegative integers smaller than $2n$ (thus $|S| = 4n^2$). Assume that $\mathcal{F}$ is a set of polygons such that all vertices of polygons in $\mathcal{F}$ lie in $S$, and each point in $S$ is a vertex of exactly one of the polygons in $\mathcal{F}$.
Determine the largest possible sum of areas of all polygons in $\mathcal{F}$.


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


## 2021 — A3

**Record:** `imo_2021_f2791d`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_f2791d.json.gz).

Given a positive integer $n$, find the smallest value of
$$
\left\lfloor\frac{a_{1}}{1}\right\rfloor+\left\lfloor\frac{a_{2}}{2}\right\rfloor+\cdots+\left\lfloor\frac{a_{n}}{n}\right\rfloor
$$
over all permutations $(a_{1}, a_{2}, \ldots, a_{n})$ of $(1,2, \ldots, n)$.


## 2021 — A5

**Record:** `imo_2021_f5cc52`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_f5cc52.json.gz).

Let $n \geqslant 2$ be an integer, and let $a_{1}, a_{2}, \ldots, a_{n}$ be positive real numbers such that $a_{1}+a_{2}+\cdots+a_{n}=1$. Prove that
$$
\sum_{k=1}^{n} \frac{a_{k}}{1-a_{k}}\left(a_{1}+a_{2}+\cdots+a_{k-1}\right)^{2}<\frac{1}{3} .
$$


## 2022 — A8.

**Record:** `imo_2022_1937c6`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2022_1937c6.json.gz).

For a positive integer $n$, an $n$-sequence is a sequence $(a_{0}, \ldots, a_{n})$ of non-negative integers satisfying the following condition: if $i$ and $j$ are non-negative integers with $i+j \leqslant n$, then $a_{i}+a_{j} \leqslant n$ and $a_{a_{i}+a_{j}}=a_{i+j}$.
Let $f(n)$ be the number of $n$-sequences. Prove that there exist positive real numbers $c_{1}, c_{2}$ and $\lambda$ such that
$$
c_{1} \lambda^{n}<f(n)<c_{2} \lambda^{n}
$$
for all positive integers $n$.


## 2022 — C7.

**Record:** `imo_2022_4008eb`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2022_4008eb.json.gz).

Lucy starts by writing $s$ integer-valued 2022-tuples on a blackboard. After doing that, she can take any two (not necessarily distinct) tuples $\mathbf{v} = (v_1, \ldots, v_{2022})$ and $\mathbf{w} = (w_1, \ldots, w_{2022})$ that she has already written, and apply one of the following operations to obtain a new tuple:
$$
\begin{aligned}
& \mathbf{v} + \mathbf{w} = (v_1 + w_1, \ldots, v_{2022} + w_{2022}) \\
& \mathbf{v} \vee \mathbf{w} = (\max(v_1, w_1), \ldots, \max(v_{2022}, w_{2022}))
\end{aligned}
$$
and then write this tuple on the blackboard.
It turns out that, in this way, Lucy can write any integer-valued 2022-tuple on the blackboard after finitely many steps. What is the smallest possible number $s$ of tuples that she initially wrote?


## 2022 — A2.

**Record:** `imo_2022_57242c`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2022_57242c.json.gz).

Let $k \geqslant 2$ be an integer. Find the smallest integer $n \geqslant k+1$ with the property that there exists a set of $n$ distinct real numbers such that each of its elements can be written as a sum of $k$ other distinct elements of the set.


## 2022 — C9.

**Record:** `imo_2022_70d092`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2022_70d092.json.gz).

Let $\mathbb{Z}_{\geqslant 0}$ be the set of non-negative integers, and let $f: \mathbb{Z}_{\geqslant 0} \times \mathbb{Z}_{\geqslant 0} \rightarrow \mathbb{Z}_{\geqslant 0}$ be a bijection such that whenever $f\left(x_{1}, y_{1}\right)>f\left(x_{2}, y_{2}\right)$, we have $f\left(x_{1}+1, y_{1}\right)>f\left(x_{2}+1, y_{2}\right)$ and $f\left(x_{1}, y_{1}+1\right)>f\left(x_{2}, y_{2}+1\right)$.
Let $N$ be the number of pairs of integers $(x, y)$, with $0 \leqslant x, y<100$, such that $f(x, y)$ is odd. Find the smallest and largest possible value of $N$.


## 2023 — N5.

**Record:** `imo_2023_1ffb42`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2023_1ffb42.json.gz).

Let $a_{1} < a_{2} < a_{3} < \cdots$ be positive integers such that $a_{k+1}$ divides $2(a_{1} + a_{2} + \cdots + a_{k})$ for every $k \geqslant 1$. Suppose that for infinitely many primes $p$, there exists $k$ such that $p$ divides $a_{k}$. Prove that for every positive integer $n$, there exists $k$ such that $n$ divides $a_{k}$.


## 2023 — N8.

**Record:** `imo_2023_3c0851`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2023_3c0851.json.gz).

Let $\mathbb{Z}_{>0}$ be the set of positive integers. Determine all functions $f: \mathbb{Z}_{>0} \rightarrow \mathbb{Z}_{>0}$ such that
$$
f^{b f(a)}(a+1) = (a+1) f(b)
$$
holds for all $a, b \in \mathbb{Z}_{>0}$, where $f^{k}(n) = f(f(\cdots f(n) \cdots))$ denotes the composition of $f$ with itself $k$ times.


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


## 2023 — A5.

**Record:** `imo_2023_76bf3b`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2023_76bf3b.json.gz).

Let $a_{1}, a_{2}, \ldots, a_{2023}$ be positive integers such that
- $a_{1}, a_{2}, \ldots, a_{2023}$ is a permutation of $1,2, \ldots, 2023$, and
- $\left|a_{1}-a_{2}\right|,\left|a_{2}-a_{3}\right|, \ldots,\left|a_{2022}-a_{2023}\right|$ is a permutation of $1,2, \ldots, 2022$.
Prove that $\max \left(a_{1}, a_{2023}\right) \geqslant 507$.


## 2023 — A3.

**Record:** `imo_2023_7a9af0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2023_7a9af0.json.gz).

Let $x_{1}, x_{2}, \ldots, x_{2023}$ be distinct real positive numbers such that
$$
a_{n}=\sqrt{\left(x_{1}+x_{2}+\cdots+x_{n}\right)\left(\frac{1}{x_{1}}+\frac{1}{x_{2}}+\cdots+\frac{1}{x_{n}}\right)}
$$
is an integer for every $n=1,2, \ldots, 2023$. Prove that $a_{2023} \geqslant 3034$.


## 2023 — A4.

**Record:** `imo_2023_7d3fd0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2023_7d3fd0.json.gz).

Let $\mathbb{R}_{>0}$ be the set of positive real numbers. Determine all functions $f: \mathbb{R}_{>0} \rightarrow \mathbb{R}_{>0}$ such that
$$
x(f(x)+f(y)) \geqslant (f(f(x))+y) f(y)
$$
for every $x, y \in \mathbb{R}_{>0}$.


## 2023 — A1.

**Record:** `imo_2023_b2d73c`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2023_b2d73c.json.gz).

Professor Oak is feeding his 100 Pokémon. Each Pokémon has a bowl whose capacity is a positive real number of kilograms. These capacities are known to Professor Oak. The total capacity of all the bowls is 100 kilograms. Professor Oak distributes 100 kilograms of food in such a way that each Pokémon receives a non-negative integer number of kilograms of food (which may be larger than the capacity of their bowl). The dissatisfaction level of a Pokémon who received $N$ kilograms of food and whose bowl has a capacity of $C$ kilograms is equal to $|N-C|$.
Find the smallest real number $D$ such that, regardless of the capacities of the bowls, Professor Oak can distribute the food in a way that the sum of the dissatisfaction levels over all the 100 Pokémon is at most $D$.


## 2023 — A6.

**Record:** `imo_2023_d4d6f3`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2023_d4d6f3.json.gz).

Let $k \geqslant 2$ be an integer. Determine all sequences of positive integers $a_{1}, a_{2}, \ldots$ for which there exists a monic polynomial $P$ of degree $k$ with non-negative integer coefficients such that
$$
P\left(a_{n}\right)=a_{n+1} a_{n+2} \cdots a_{n+k}
$$
for every integer $n \geqslant 1$.


## 2023 — A7.

**Record:** `imo_2023_f7b402`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2023_f7b402.json.gz).

Let $N$ be a positive integer. Prove that there exist three permutations $a_{1}, a_{2}, \ldots, a_{N}$; $b_{1}, b_{2}, \ldots, b_{N}$; and $c_{1}, c_{2}, \ldots, c_{N}$ of $1,2, \ldots, N$ such that
$$
\left|\sqrt{a_{k}}+\sqrt{b_{k}}+\sqrt{c_{k}}-2 \sqrt{N}\right|<2023
$$
for every $k=1,2, \ldots, N$.


## 2024 — A1

**Record:** `imo_2024_071598`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2024_071598.json.gz).

Determine all real numbers $\alpha$ such that the number
$$
\lfloor\alpha\rfloor+\lfloor 2 \alpha\rfloor+\cdots+\lfloor n \alpha\rfloor
$$
is a multiple of $n$ for every positive integer $n$. (Here $\lfloor z\rfloor$ denotes the greatest integer less than or equal to $z$.)


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


## 2024 — C7

**Record:** `imo_2024_95e706`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2024_95e706.json.gz).

Let $N$ be a positive integer and let $a_{1}, a_{2}, \ldots$ be an infinite sequence of positive integers. Suppose that, for each $n > N$, $a_{n}$ is equal to the number of times $a_{n-1}$ appears in the list $a_{1}, a_{2}, \ldots, a_{n-1}$.
Prove that at least one of the sequences $a_{1}, a_{3}, a_{5}, \ldots$ and $a_{2}, a_{4}, a_{6}, \ldots$ is eventually periodic.



# IMO-TST source statements

## 2001 — 4

**Record:** `usa_2001_02fd39`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2001_02fd39.json.gz).

Let $P$ be a point in the plane of triangle $ABC$ such that the segments $PA$, $PB$, and $PC$ are the sides of an obtuse triangle. Assume that in this triangle the obtuse angle opposes the side congruent to $PA$. Prove that $\angle BAC$ is acute.


## 2001 — 7

**Record:** `usa_2001_154ed9`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2001_154ed9.json.gz).

Let $ABCD$ be a convex quadrilateral such that $\angle ABC = \angle ADC = 135^\circ$ and
$$
AC^2 \cdot BD^2 = 2AB \cdot BC \cdot CD \cdot DA.
$$
Prove that the diagonals of quadrilateral $ABCD$ are perpendicular.


## 2001 — 1

**Record:** `usa_2001_2e5455`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2001_2e5455.json.gz).

Let $\{a_n\}_{n \ge 0}$ be a sequence of real numbers such that $a_{n+1} \ge a_n^2 + \frac{1}{5}$ for all $n \ge 0$. Prove that $\sqrt{a_{n+5}} \ge a_{n-5}^2$ for all $n \ge 5$.


## 2001 — 9

**Record:** `usa_2001_419b80`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2001_419b80.json.gz).

Let $A$ be a finite set of positive integers. Prove that there exists a finite set $B$ of positive integers such that $A \subseteq B$ and
$$
\prod_{x \in B} x = \sum_{x \in B} x^2.
$$


## 2001 — 3

**Record:** `usa_2001_8e6431`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2001_8e6431.json.gz).

Let $a, b$, and $c$ be nonnegative real numbers such that
$$
a^2 + b^2 + c^2 + abc = 4.
$$
Prove that
$$
0 \le ab + bc + ca - abc \le 2.
$$


## 2001 — 2

**Record:** `usa_2001_a0d6f2`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2001_a0d6f2.json.gz).

Express
$$
\sum_{k=0}^{n} (-1)^k (n-k)!(n+k)!
$$
in closed form.


## 2001 — 8

**Record:** `usa_2001_a49c5f`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2001_a49c5f.json.gz).

Find all pairs of nonnegative integers $(m, n)$ such that
$$
(m + n - 5)^2 = 9mn.
$$


## 2001 — 6

**Record:** `usa_2001_d8e944`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2001_d8e944.json.gz).

Let $a, b, c$ be positive real numbers such that
$$
a + b + c \ge abc.
$$
Prove that at least two of the inequalities
$$
\frac{2}{a} + \frac{3}{b} + \frac{6}{c} \ge 6, \quad \frac{2}{c} + \frac{3}{a} + \frac{6}{b} \ge 6,
$$
are true.


## 2001 — 4

**Record:** `vnm_2001_4fda7f`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2001_4fda7f.json.gz).

The positive real numbers $a$, $b$, $c$ satisfy the condition:
$$
21ab + 2bc + 8ca \le 12.
$$
Find the least value of the expression:
$$
P(a, b, c) = \frac{1}{a} + \frac{2}{b} + \frac{3}{c}.
$$


## 2001 — 1

**Record:** `vnm_2001_ff5434`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2001_ff5434.json.gz).

The sequence of integers $\{a_n\}$, $n = 0, 1, 2, \ldots$, is defined by:
$a_0 = 1$ and $a_n = a_{n-1} + a_{\lceil n/3 \rceil}$ for every $n = 1, 2, 3, \ldots$.
Prove that for every prime number $p \le 13$, there exists an infinite number of natural numbers $k$ such that $a_k$ is divisible by $p$.
([x] denotes the integral part of x).


## 2002 — Problem 4

**Record:** `vnm_2002_aea91a`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2002_aea91a.json.gz).

Let be given an integer $n \ge 2$ and a rectangular board of size $n \times 2n$ ($n$ rows, $2n$ columns). One labels randomly $n^2$ little squares of the board. Prove that for every integer $k$ such that $1 < k \le \lfloor n/2 \rfloor + 1$, there always exist $k$ rows of the board so that the rectangular board of size $k \times 2n$ formed by these $k$ rows has no less than
$$
\frac{k!(n - 2k + 2)}{(n - k + 1)(n - k + 2)\dots(n - 1)}
$$
columns containing only labelled little squares.

($[a]$ denotes the greatest integer not exceeding $a$)


## 2002 — Problem 2

**Record:** `vnm_2002_ba609d`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2002_ba609d.json.gz).

A positive integer $N_0$ is written on the board. Two persons, $A$ and $B$, play the following game: $A$ erases $N_0$ and writes a number $N_1 \in \{N_0 - 1; [N_0/3]\}$. Then $B$ erases $N_1$ and writes a number $N_2 \in \{N_1 - 1; [N_1/3]\}$. At his turn, $A$ erases $N_2$ and so on. They continue to play until on the board appears the number $0$; the player who writes first the number $0$ is considered as the winner and the other player is considered lost.

Determine whether the player $A$ or the player $B$ has a strategy to guarantee his win when:
$$
1/\ N_0 = 120 ?
$$
$$
2/\ N_0 = (3^{2002} - 1)/2 ?
$$
$$
3/\ N_0 = (3^{2002} + 1)/2 ?
$$


## 2003 — 3

**Record:** `vnm_2003_23ab5b`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2003_23ab5b.json.gz).

Let $f: N \times Z \to N$ be a given function satisfying simultaneously the following conditions:
i/ $f(0, 0) = 5^{2003}$, $f(0, n) = 0$ for every integer $n \neq 0$;
ii/ $f(m, n) = f(m - 1, n) - 2\left[\frac{f(m - 1, n)}{2}\right] + \left[\frac{f(m - 1, n - 1)}{2}\right] + \left[\frac{f(m - 1, n + 1)}{2}\right]$ for every natural number $m > 0$ and for every integer $n$.
Prove that there exists natural number $M$ such that
$f(M, n) = 1$ for all integers $n$ such that $|n| \le (5^{2003} - 1)/2$
and $f(M, n) = 0$ for all integers $n$ such that $|n| > (5^{2003} - 1)/2$.


## 2003 — 5

**Record:** `vnm_2003_767bbb`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2003_767bbb.json.gz).

Let $A$ be the set of all permutations $a = (a_1, a_2, ..., a_{2003})$ of $2003$ first positive integers such that each permutation satisfies the condition: there is no nonvoid proper subset $S$ of the set $\{1, 2, ..., 2003\}$ such that $\{a_k \mid k \in S\} = S$.

For each $a = (a_1, a_2, ..., a_{2003}) \in A$, put $d(a) = \sum_{k=1}^{2003} (a_k - k)^2$.

a. Find the least value of $d(a)$. Denote this least value by $d_0$.

b. Find all permutations $a \in A$ such that $d(a) = d_0$.


## 2004 — 5

**Record:** `usa_2004_0c6223`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2004_0c6223.json.gz).

Let $a$, $b$ and $c$ be positive real numbers. Prove that
$$
(a^5 - a^2 + 3)(b^5 - b^2 + 3)(c^5 - c^2 + 3) \geq (a + b + c)^3.
$$


## 2004 — 3

**Record:** `usa_2004_6ca0a8`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2004_6ca0a8.json.gz).

For what real values of $k > 0$ is it possible to dissect a $1 \times k$ rectangle into two similar, but noncongruent, polygons?


## 2004 — 2

**Record:** `usa_2004_7153d3`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2004_7153d3.json.gz).

Suppose $a_1, \dots, a_n$ are integers whose greatest common divisor is $1$. Let $S$ be a set of integers with the following properties.

a. For $i = 1, \dots, n$, $a_i \in S$.

b. For $i, j = 1, \dots, n$ (not necessarily distinct), $a_i - a_j \in S$.

c. For any integers $x, y \in S$, if $x + y \in S$, then $x - y \in S$.

Prove that $S$ must be equal to the set of all integers.


## 2004 — 1

**Record:** `usa_2004_92e118`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2004_92e118.json.gz).

Let $a_1, a_2, \dots, a_n, b_1, b_2, \dots, b_n$ be real numbers such that
$$
(a_1^2 + a_2^2 + \cdots + a_n^2 - 1)(b_1^2 + b_2^2 + \cdots + b_n^2 - 1) 
> (a_1b_1 + a_2b_2 + \cdots + a_nb_n - 1)^2.
$$
Show that $a_1^2 + a_2^2 + \cdots + a_n^2 > 1$ and $b_1^2 + b_2^2 + \cdots + b_n^2 > 1$.


## 2004 — 2

**Record:** `usa_2004_cbf0f1`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2004_cbf0f1.json.gz).

Let $n$ be a positive integer. Consider sequences $a_0, a_1, \dots, a_n$ such that $a_i \in \{1, 2, \dots, n\}$ for each $i$ and $a_n = a_0$.

a. Call such a sequence *good* if for all $i = 1, 2, \dots, n$, $a_i - a_{i-1} \not\equiv i \pmod n$. Suppose that $n$ is odd. Find the number of good sequences.

b. Call such a sequence *great* if for all $i = 1, 2, \dots, n$, $a_i - a_{i-1} \not\equiv i, 2i \pmod n$. Suppose that $n$ is an odd prime. Find the number of great sequences.


## 2004 — 6

**Record:** `usa_2004_e0c776`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2004_e0c776.json.gz).

Let $\mathbb{N}_0^+$ and $\mathbb{Q}$ be the set of nonnegative integers and rational numbers, respectively. Define the function $f : \mathbb{N}_0^+ \to \mathbb{Q}$ by $f(0) = 0$ and
$$f(3n + k) = -\frac{3f(n)}{2} + k, \quad \text{for } k = 0, 1, 2.$$ 
Prove that $f$ is one-to-one, and determine its range.


## 2006 — 3

**Record:** `usa_2006_1da087`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2006_1da087.json.gz).

Find the least real number $k$ with the following property: if the real numbers $x$, $y$, and $z$ are not all positive, then
$$
k(x^2 - x + 1)(y^2 - y + 1)(z^2 - z + 1) \geq (xyz)^2 - xyz + 1.
$$


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


## 2007 — 2

**Record:** `usa_2007_f12e75`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2007_f12e75.json.gz).

Let $n$ be a positive integer and let $a_1 \le a_2 \le \dots \le a_n$ and $b_1 \le b_2 \le \dots \le b_n$ be two nondecreasing sequences of real numbers such that
$$
a_1 + \dots + a_i \le b_1 + \dots + b_i \quad \text{for every } i = 1, \dots, n-1
$$
and
$$
a_1 + \dots + a_n = b_1 + \dots + b_n.
$$

Suppose that for any real number $m$, the number of pairs $(i, j)$ with $a_i - a_j = m$ equals the number of pairs $(k, \ell)$ with $b_k - b_\ell = m$. Prove that $a_i = b_i$ for $i = 1, \dots, n$.

**Note:** It is important to interpret the condition that for any real number $m$, the number of pairs $(i, j)$ with $a_i - a_j = m$ equals the number of pairs $(k, \ell)$ with $b_k - b_\ell = m$. It means that we have two identical multi-sets (a multi-set is a set that allows repeated elements)


## 2008 — 1

**Record:** `usa_2008_4ddab6`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2008_4ddab6.json.gz).

There is a set of $n$ coins with distinct integer weights $w_1, w_2, \dots, w_n$. It is known that if any coin with weight $w_k$, $1 \le k \le n$, is removed from the set, the remaining coins can be split into two groups of the same weight. (The number of coins in the two groups can be different.) Find all $n$ for which such a set of coins exists.
(This problem was suggested by Gregory Galperin.)


## 2008 — 6

**Record:** `usa_2008_7bcea0`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2008_7bcea0.json.gz).

Let $n$ be a positive integer not divisible by the cube of a prime. Given an integer-coefficient polynomial $f(x)$, define its *signature modulo* $n$ to be the (ordered) sequence $f(1), \dots, f(n)$ modulo $n$. Of the $n^n$ such $n$-term sequences of integers modulo $n$, how many are the signature of some polynomial $f(x)$?


## 2008 — 5

**Record:** `usa_2008_cbf07d`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2008_cbf07d.json.gz).

Two sequences of integers, $a_1, a_2, a_3, \dots$ and $b_1, b_2, b_3, \dots$, satisfy the equation
$$
(a_n - a_{n-1})(a_n - a_{n-2}) + (b_n - b_{n-1})(b_n - b_{n-2}) = 0
$$
for each integer $n$ greater than $2$. Prove that there is a positive integer $k$ such that $a_k = a_{k+2008}$.


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


## 2009 — 1

**Record:** `usa_2009_f1ac89`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2009_f1ac89.json.gz).

Let $m$ and $n$ be positive integers. Mr. Fat has a set $S$ containing every rectangular tile with integer side lengths and area a power of $2$. Mr. Fat also has a rectangle $R$ with dimensions $2^m \times 2^n$ and a $1 \times 1$ square removed from one of the corners. Mr. Fat wants to choose $m + n$ rectangles from $S$, with respective areas $2^0, 2^1, \dots, 2^{m+n-1}$, and then tile $R$ with the chosen rectangles. Prove that this can be done in at most $(m+n)!$ ways.


## 2010 — 5

**Record:** `ind_2010_051b62`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2010_051b62.json.gz).

Let $A = (a_{jk})$ be a $10 \times 10$ array of positive real numbers such that the sum of numbers in each row as well as in each column is $1$. Show that there exist $j < k$ and $l < m$ such that
$$
a_{jl}a_{km} + a_{jm}a_{kl} \geq \frac{1}{50}
$$


## 2010 — 6

**Record:** `sgp_2010_6c0264`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/singapore/sgp_2010_6c0264.json.gz).

Determine all finite sets $A$ of non-negative real numbers, containing at least four elements, and such that for all distinct $a, b, c, d \in A$, $ab + cd \in A$.


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


## 2010 — Problem 4

**Record:** `vnm_2010_bd2edd`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2010_bd2edd.json.gz).

Let $a$, $b$, $c$ be positive numbers satisfying:
$$
\frac{1}{a} + \frac{1}{b} + \frac{1}{c} \le 16(a + b + c).
$$
Show that
$$
\frac{1}{(a + b + \sqrt{2(a + c)})^3} + \frac{1}{(b + c + \sqrt{2(b + a)})^3} + \frac{1}{(c + a + \sqrt{2(c + b)})^3} \le \frac{8}{9}.
$$
When does the equality occur?


## 2011 — 3

**Record:** `usa_2011_8b387a`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2011_8b387a.json.gz).

Let $p$ be a prime. We say that a sequence of integers $\{z_n\}_{n=0}^{\infty}$ is a $p$-pod if for each $e \ge 0$, there is an $N \ge 0$ such that whenever $m \ge N$, $p^e$ divides the sum
$$
\sum_{k=0}^{m} (-1)^k \binom{m}{k} z_k.
$$

Prove that if both sequences $\{x_n\}_{n=0}^{\infty}$ and $\{y_n\}_{n=0}^{\infty}$ are $p$-pods, then the sequence $\{x_n y_n\}_{n=0}^{\infty}$ is a $p$-pod.


## 2011 — 9

**Record:** `usa_2011_c4196c`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2011_c4196c.json.gz).

Determine whether or not there exist two different sets $A$, $B$, each consisting of at most $2011^2$ positive integers, such that every $x$ with $0 < x < 1$ satisfies the following inequality:
$$
\left| \sum_{a \in A} x^a - \sum_{b \in B} x^b \right| < (1-x)^{2011}.
$$


## 2011 — 6

**Record:** `usa_2011_ff9f97`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2011_ff9f97.json.gz).

A polynomial $P(x)$ is called *nice* if $P(0) = 1$ and the nonzero coefficients of $P(x)$ alternate between $1$ and $-1$ when written in order. Suppose $P(x)$ is nice, and let $m$ and $n$ be two relatively prime positive integers. Show that
$$
Q(x) = P(x^n) \cdot \frac{(x^{mn} - 1)(x - 1)}{(x^m - 1)(x^n - 1)}
$$
is nice as well.


## 2011 — 4

**Record:** `vnm_2011_36c22e`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2011_36c22e.json.gz).

$$
a_0 = 1, a_1 = 3 \text{ and } a_{n+2} = 1 + \left\lfloor \frac{a_{n+1}^2}{a_n} \right\rfloor \text{ for all } n \ge 0.
$$

Show that $a_{n+2} \cdot a_n - a_{n+1}^2 = 2^n$ for all integers $n$.


## 2011 — 3

**Record:** `vnm_2011_8717a7`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2011_8717a7.json.gz).

Given an integer $n \ge 3$. Consider $n$ real numbers $x_1, x_2, \dots, x_n$ satisfying at the same time the following conditions:

i/  $x_1 \ge x_2 \ge \dots \ge x_n$;
ii/  $\sum_{i=1}^{n} x_i = 0$;
iii/  $\sum_{i=1}^{n} x_i^2 = n(n-1)$.

Find the maximum and the minimum values of the sum $S = x_1 + x_2$.


## 2011 — 1

**Record:** `vnm_2011_f6e2ec`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2011_f6e2ec.json.gz).

1. At the point $(1, 1)$ of the coordinate plane $(Oxy)$, there is a cào cào. From that point the cào cào can only jump to other integral points by the rule: from the positive integral point $A$, the cào cào jumps to the positive integral point $B$ if the triangle $OAB$ has area equal to $\frac{1}{2}$.

1/ Find all points $(m, n)$ to which the cào cào can jump to after a finite number of jumps, starting from the point $(1, 1)$.

2/ Let $(m, n)$ be a positive integral point with property mentioned in 1/. Show that there exists a way, in which the cào cào can jump from point $(1, 1)$ to point $(m, n)$ with not more than $|m - n|$ jumps.


## 2012 — 9

**Record:** `ind_2012_f07169`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2012_f07169.json.gz).

Suppose $2n$ real numbers are placed in the cells of a $2 \times n$ grid such that the sum of the numbers in each of the $n$ columns is $1$. Prove that one can erase one of the two numbers in each column such that the sum of the remaining numbers in each of the rows does not exceed $\frac{n+1}{4}$.


## 2012 — 3

**Record:** `usa_2012_485e07`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2012_485e07.json.gz).

Prove that there exists a real constant $c$ such that for any pair $(x, y)$ of real numbers, there exist relatively prime integers $m$ and $n$ satisfying the relation
$$\sqrt{(x-m)^2 + (y-n)^2} < c \log(x^2 + y^2 + 2).$$
(This problem was suggested by Daniel Kane.)


## 2012 — 1

**Record:** `usa_2012_5176bd`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2012_5176bd.json.gz).

Find all real-valued functions $f$ defined on pairs of real numbers, having the following property: for all real numbers $a, b, c$, the median of $f(a, b)$, $f(b, c)$, $f(c, a)$ equals the median of $a, b, c$. (The median of three real numbers, not necessarily distinct, is the number that is in the middle when the three numbers are arranged in non-decreasing order.)


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


## 2012 — 6

**Record:** `usa_2012_8acacb`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2012_8acacb.json.gz).

Let $a$, $b$, $c$ be real numbers in the interval $[0, 1]$ with $a + b$, $b + c$, $c + a \ge 1$. Prove that
$$
1 \le (1-a)^2 + (1-b)^2 + (1-c)^2 + \frac{2\sqrt{2abc}}{\sqrt{a^2+b^2+c^2}}.
$$


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


## 2012 — Bài 4

**Record:** `vnm_2012_1add92`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_1add92.json.gz).

Cho dãy số $x_1, x_2, \ldots$ được xác định như sau: $x_1 = 1$, $x_2 = 2011$, $x_{n+2} = 4022x_{n+1} - x_n$ với mọi $n \ge 1$.
Chứng minh rằng $\frac{x_{2012} + 1}{2012}$ là số chính phương.


## 2012 — Bài 5

**Record:** `vnm_2012_cbc884`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_cbc884.json.gz).

Chứng minh rằng $c = 10\sqrt{24}$ là số thực dương lớn nhất có tính chất: Nếu $a_1, a_2, \ldots, a_{17}$ là 17 số thực dương thỏa mãn đồng thời
$$
\text{hai điều kiện } \sum_{i=1}^{17} a_i^2 = 24, \quad \sum_{i=1}^{17} a_i^3 + \sum_{i=1}^{17} a_i < c
$$
thì với mọi $1 \le i < j < k \le 17$ ta có $a_i, a_j, a_k$ là độ dài ba cạnh của một tam giác.


## 2012 — Bài 3

**Record:** `vnm_2012_f548c9`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_f548c9.json.gz).

Cho trước một số nguyên tố $p$ không nhỏ hơn $17$. Chứng minh rằng $t=3$ là số nguyên dương lớn nhất có tính chất: Với mọi bộ số nguyên $a, b, c, d$ sao cho $abc$ không chia hết cho $p$, nhưng $a+b+c$ chia hết cho $p$ thì luôn tồn tại $x, y, z \in \{0, 1, ..., \lfloor \frac{p}{t} \rfloor - 1\}$ để $ax+by+cz+d$ chia hết cho $p$. ($\lfloor \frac{p}{t} \rfloor$ kí hiệu số nguyên lớn nhất không vượt quá $\frac{p}{t}$).


## 2013 — 1.

**Record:** `usa_2013_2d2e1e`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2013_2d2e1e.json.gz).

A social club has $2k + 1$ members, each of whom is fluent in the same $k$ languages. Any pair of members always talk to each other in only one language. Suppose that there were no three members such that they use only one language among them. Let $A$ be the number of three-member subsets such that the three distinct pairs among them use different languages. Find the maximum possible value of $A$.


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


## 2013 — 9.

**Record:** `usa_2013_f4a0e2`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2013_f4a0e2.json.gz).

Given a set $S$ of $n$ variables, a binary operation $\times$ on $S$ is called *simple* if it satisfies $(x \times y) \times z = x \times (y \times z)$ for all $x, y, z \in S$ and $x \times y \in \{x, y\}$ for all $x, y \in S$. Given a simple operation $\times$ on $S$, any string of elements in $S$ can be reduced to a single element, such as $xyz \rightarrow x \times (y \times z)$. A string of variables in $S$ is called *full* if it contains each variable in $S$ at least once, and two strings are *equivalent* if they evaluate to the same variable regardless of which simple $\times$ is chosen. For example, $xxx$, $xx$, and $x$ are equivalent, but these are only full if $n = 1$. Suppose $T$ is a set of strings such that any full string is equivalent to exactly one element of $T$. Determine the number of elements of $T$.
(This problem was suggested by John Berman.)


## 2014 — 6.

**Record:** `usa_2014_19553f`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2014_19553f.json.gz).

Let $\mathbb{N}$ be the set of positive integers. Find all functions $f : \mathbb{N} \to \mathbb{N}$ that satisfy the equation
$$
f^{abc-a}(abc) + f^{abc-b}(abc) + f^{abc-c}(abc) = a + b + c
$$
for all $a, b, c \ge 2$.
(Here $f^1(n) = f(n)$ and $f^k(n) = f(f^{k-1}(n))$ for every integer $k$ greater than 1.)


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


## 2014 — 4.

**Record:** `usa_2014_9ebb86`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2014_9ebb86.json.gz).

Let $n$ be a positive even integer, and let $c_1, c_2, \dots, c_{n-1}$ be real numbers satisfying
$$
\sum_{i=1}^{n-1} |c_i - 1| < 1.
$$
Prove that
$$
2x^n - c_{n-1}x^{n-1} + c_{n-2}x^{n-2} - \dots - c_1x + 2
$$
has no real roots.


## 2014 — 3.

**Record:** `usa_2014_c1a41c`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2014_c1a41c.json.gz).

Let $n$ be an even positive integer, and let $G$ be an $n$-vertex graph with exactly $\frac{n^2}{4}$ edges, where there are no loops or multiple edges (each unordered pair of distinct vertices is joined by either 0 or 1 edge). An unordered pair of distinct vertices $\{x, y\}$ is said to be *amicable* if they have a common neighbor (there is a vertex $z$ such that $xz$ and $yz$ are both edges). Prove that $G$ has at least $2^{\binom{n/2}{2}}$ unordered pairs of vertices which are amicable.


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


## 2015 — 1

**Record:** `vnm_2015_0c8e24`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2015_0c8e24.json.gz).

Let $\alpha$ be a positive root of the equation $x^2 + x = 5$. Suppose that $n$ is a positive integer and $c_0, c_1, \dots, c_n$ are nonnegative integers satisfying the condition
$$
c_0 + c_1\alpha + c_2\alpha^2 + \dots + c_n\alpha^n = 2015.
$$
a) Prove that $c_0 + c_1 + \dots + c_n \equiv 2 \pmod{3}$.
b) Find the minimum of $c_0 + c_1 + \dots + c_n$.


## 2015 — 6

**Record:** `vnm_2015_7c4b9d`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2015_7c4b9d.json.gz).

Find the smallest positive integer $n$ such that there exist $n$ real numbers $a_1, a_2, \dots, a_n$ satisfying the following conditions:
i) $a_1 + \dots + a_n > 0$;
ii) $a_1^3 + \dots + a_n^3 < 0$; and
iii) $a_1^5 + \dots + a_n^5 > 0$.


## 2016 — 4

**Record:** `ind_2016_85f4b8`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2016_85f4b8.json.gz).

Let $n$ be a natural number. We define sequences $a_i$ and $b_i$ as follows. We let $a_0 = 1$ and $b_0 = n$. For $i > 0$, we let
$$
(a_i, b_i) = \begin{cases} (2a_{i-1} + 1, b_{i-1} - a_{i-1} - 1) & \text{if } a_{i-1} < b_{i-1}, \\ (a_{i-1} - b_{i-1} - 1, 2b_{i-1} + 1) & \text{if } a_{i-1} > b_{i-1}, \\ (a_{i-1}, b_{i-1}) & \text{if } a_{i-1} = b_{i-1}. \end{cases}
$$
Given that $a_k = b_k$ for some natural number $k$, prove that $n + 3$ is a power of 2.


## 2016 — 2

**Record:** `ind_2016_c1a286`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2016_c1a286.json.gz).

Let $n$ be a natural number. A sequence $x_1, x_2, \dots, x_{n^2}$ is called *n-*good if each $x_i$ is an element of $\{1, 2, \dots, n\}$ and the ordered pairs $(x_i, x_{i+1})$ are all different for $i = 1, 2, \dots, n^2$ (here we consider the subscripts modulo $n^2$). Two *n-*good sequences $x_1, x_2, \dots, x_{n^2}$ and $y_1, y_2, \dots, y_{n^2}$ are called *similar* if there exists an integer $k$ such that $y_i = x_{i+k}$ for all $i = 1, 2, \dots, n^2$ (again taking the subscripts modulo $n^2$). Suppose that there exists a non-trivial permutation $\sigma$ of $\{1, 2, \dots, n\}$ and an *n-*good sequence $x_1, x_2, \dots, x_{n^2}$ which is similar to $\sigma(x_1), \sigma(x_2), \dots, \sigma(x_{n^2})$. Show that $n \equiv 2 \pmod{4}$.


## 2017 — Problem 5

**Record:** `vnm_2017_d99be9`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2017_d99be9.json.gz).

Given 2017 positive real numbers $a_1, a_2, \dots, a_{2017}$. For each positive integer $n > 2017$, let
$$
a_n = \max\{a_{i_1} a_{i_2} a_{i_3} \mid i_1 + i_2 + i_3 = n, 1 \le i_1 \le i_2 \le i_3 \le n-1\}.
$$
Prove there exists some positive integers $m \le 2017$ and $N > 4m$ such that $a_n a_{n-4m} = a_{n-2m}^2$ for every $n > N$.


## 2018 — TSTST 1

**Record:** `usa_2018_1d04a5`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2018_1d04a5.json.gz).

As usual, let $\mathbb{Z}[x]$ denote the set of single-variable polynomials in $x$ with integer coefficients.
Find all functions $\theta : \mathbb{Z}[x] \to \mathbb{Z}$ such that for any polynomials $p, q \in \mathbb{Z}[x]$,
* $\theta(p + 1) = \theta(p) + 1$, and
* if $\theta(p) \neq 0$ then $\theta(p)$ divides $\theta(p \cdot q)$.


## 2018 — TSTST 6

**Record:** `usa_2018_259657`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2018_259657.json.gz).

Let $S = \{1, \dots, 100\}$, and for every positive integer $n$ define
$$
T_n = \{(a_1, \dots, a_n) \in S^n \mid a_1 + \dots + a_n \equiv 0 \pmod{100}\}.
$$
Determine which $n$ have the following property: if we color any 75 elements of $S$ red, then at least half of the $n$-tuples in $T_n$ have an even number of coordinates with red elements.


## 2018 — TSTST 4

**Record:** `usa_2018_5b516b`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2018_5b516b.json.gz).

For an integer $n > 0$, denote by $\mathcal{F}(n)$ the set of integers $m > 0$ for which the polynomial $p(x) = x^2 + mx + n$ has an integer root.

a. Let $S$ denote the set of integers $n > 0$ for which $\mathcal{F}(n)$ contains two consecutive integers. Show that $S$ is infinite but
$$
\sum_{n \in S} \frac{1}{n} \le 1.
$$

b. Prove that there are infinitely many positive integers $n$ such that $\mathcal{F}(n)$ contains three consecutive integers.


## 2018 — TSTST 7

**Record:** `usa_2018_5cd6f2`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2018_5cd6f2.json.gz).

Let $n$ be a positive integer. A frog starts on the number line at $0$. Suppose it makes a finite sequence of hops, subject to two conditions:
* The frog visits only points in $\{1, 2, \dots, 2^n - 1\}$, each at most once.
* The length of each hop is in $\{2^0, 2^1, 2^2, \dots\}$. (The hops may be either direction, left or right.)
Let $S$ be the sum of the (positive) lengths of all hops in the sequence. What is the maximum possible value of $S$?


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


## 2019 — TSTST 4

**Record:** `usa_2019_afbc19`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2019_afbc19.json.gz).

Consider coins with positive real denominations not exceeding $1$. Find the smallest $C > 0$ such that the following holds: if we are given any $100$ such coins with total value $50$, then we can always split them into two stacks of $50$ coins each such that the absolute difference between the total values of the two stacks is at most $C$.


## 2019 — TSTST 6

**Record:** `usa_2019_c48ff2`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2019_c48ff2.json.gz).

Suppose $P$ is a polynomial with integer coefficients such that for every positive integer $n$, the sum of the decimal digits of $|P(n)|$ is not a Fibonacci number. Must $P$ be constant?
(A *Fibonacci number* is an element of the sequence $F_0, F_1, \dots$ defined recursively by $F_0 = 0$, $F_1 = 1$, and $F_{k+2} = F_{k+1} + F_k$ for $k \ge 0$.)


## 2019 — TSTST 1

**Record:** `usa_2019_f27ccd`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2019_f27ccd.json.gz).

Find all binary operations $\diamond$: $\mathbb{R}_{>0} \times \mathbb{R}_{>0} \to \mathbb{R}_{>0}$ (meaning $\diamond$ takes pairs of positive real numbers to positive real numbers) such that for any real numbers $a, b, c > 0$,
* the equation $a \diamond (b \diamond c) = (a \diamond b) \cdot c$ holds; and
* if $a \ge 1$ then $a \diamond a \ge 1$.


## 2020 — TST 1

**Record:** `usa_2020_5d31dd`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2020_5d31dd.json.gz).

Choose positive integers $b_1, b_2, \dots$ satisfying
$$
1 = \frac{b_1}{1^2} > \frac{b_2}{2^2} > \frac{b_3}{3^2} > \frac{b_4}{4^2} > \dots
$$
and let $r$ denote the largest real number satisfying $\frac{b_n}{n^2} \ge r$ for all positive integers $n$. What are the possible values of $r$ across all possible choices of the sequence $(b_n)$?


## 2020 — TSTST 3

**Record:** `usa_2020_992de5`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2020_992de5.json.gz).

We say a nondegenerate triangle whose angles have measures $\theta_1, \theta_2, \theta_3$ is *quirky* if there exists integers $r_1, r_2, r_3$, not all zero, such that
$$
r_1\theta_1 + r_2\theta_2 + r_3\theta_3 = 0.
$$
Find all integers $n \ge 3$ for which a triangle with side lengths $n-1, n, n+1$ is quirky.


## 2020 — TSTST 7

**Record:** `usa_2020_dc53c4`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2020_dc53c4.json.gz).

Find all nonconstant polynomials $P(z)$ with complex coefficients for which all complex roots of the polynomials $P(z)$ and $P(z) - 1$ have absolute value $1$.


## 2021 — TST 1

**Record:** `usa_2021_c4710d`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2021_c4710d.json.gz).

Determine all integers $s \ge 4$ for which there exist positive integers $a, b, c, d$ such that $s = a+b+c+d$ and $s$ divides $abc + abd + acd + bcd$.


## 2021 — 1

**Record:** `vnm_2021_862c74`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2021_862c74.json.gz).

Define the sequence $(a_n)$ as $a_1 = 1$, $a_{2n} = a_n$ and $a_{2n+1} = a_n + 1$ for all positive integers $n$.

a) Find all positive integers $n$ such that $a_{kn} = a_n$ for all integers $1 \le k \le n$.

b) Prove that there are infinitely many positive integers $m$ such that $a_{km} \ge a_m$ for all positive integers $k$.


## 2021 — 4

**Record:** `vnm_2021_dfb9b1`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2021_dfb9b1.json.gz).

Let $a$, $b$ and $c$ be non-negative real numbers such that
$$
2(a^2 + b^2 + c^2) + 3(ab + bc + ca) = 5(a + b + c).
$$
Prove that $4(a^2 + b^2 + c^2) + 2(ab + bc + ca) + 7abc \le 25$.


## 2022 — 4

**Record:** `chn_2022_252cd5`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_252cd5.json.gz).

Given a positive integer $n$, find all $n$-tuples of real numbers $(x_1, x_2, \dots, x_n)$ such that
$$
f(x_1, x_2, \dots, x_n) = \sum_{k_1=0}^{2} \sum_{k_2=0}^{2} \cdots \sum_{k_n=0}^{2} \left| k_1 x_1 + k_2 x_2 + \cdots + k_n x_n - 1 \right|
$$
attains its minimum.


## 2022 — 6

**Record:** `chn_2022_3e5903`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_3e5903.json.gz).

Let $m$ and $n$ be two positive integers with $m \ge n \ge 2022$. Let $a_1, a_2, \dots, a_n, b_1, b_2, \dots, b_n$ be $2n$ real numbers. Prove that the numbers of ordered pairs $(i, j)$ ($1 \le i, j \le n$) such that
$$
|a_i + b_j - ij| \le m
$$
is less than or equal to $3n\sqrt{m \log n}$.


## 2022 — 3

**Record:** `chn_2022_bec0c9`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_bec0c9.json.gz).

Let $a_1, a_2, \dots, a_n$ be $n$ positive integers that are not divisible one another, i.e. for any $i \neq j$, $a_i$ is not divisible by $a_j$. Show that
$$
a_1 + a_2 + \dots + a_n \geq 1.1n^2 - 2n.
$$


## 2022 — Problem 5

**Record:** `vnm_2022_841202`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2022_841202.json.gz).

A fractional number $x$ is called ‘pretty’ if it has finite expression in base $b$ numeral system where $b$ is a positive integer in $[2; 2022]$. Prove that there exists finite positive integers $n \ge 4$ such that with every $m$ in $\left(\frac{2n}{3}, n\right)$, there is at least one pretty number among two numbers $\frac{m}{n-m}$ and $\frac{n-m}{m}$.


## 2022 — 2

**Record:** `vnm_2022_b14250`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2022_b14250.json.gz).

Given a convex polyhedron with 2022 faces. In 3 arbitrary faces, there are already numbers 26, 4 and 2022 (each face contains one number). One wants to fill in each other face a real number which is the arithmetic mean of every number in faces that share a common edge with that face. Prove that there is exactly one way to fill all the numbers in that polyhedron.


## 2022 — 1

**Record:** `vnm_2022_b974b3`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2022_b974b3.json.gz).

Given a real number $\alpha$ and consider function $\varphi(x) = x^2 e^{\alpha x}$ for all real numbers $x$. Find all functions $f: \mathbb{R} \to \mathbb{R}$ that satisfy
$$
f(\varphi(x) + f(y)) = y + \varphi(f(x))
$$
for all real numbers $x, y$.


## 2023 — 5

**Record:** `chn_2023_0510b2`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_0510b2.json.gz).

Given a positive integer $n$ and $n^3$ integers $a_{ijk} \in \{1, -1\}$ ($1 \le i, j, k \le n$). Prove that there exist
$$
x_1, \dots, x_n, y_1, \dots, y_n, z_1, \dots, z_n \in \{1, -1\},
$$
such that the following inequality holds
$$
\left| \sum_{i=1}^{n} \sum_{j=1}^{n} \sum_{k=1}^{n} a_{ijk} x_i y_j z_k \right| > \frac{n^2}{3}
$$


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


## 2023 — 6

**Record:** `chn_2023_8eb30f`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_8eb30f.json.gz).

(1) Prove: on the complex plane, for each line passing through the origin except for the real axis, there is at most one point $z$ such that $\frac{1+z^{23}}{z^{64}}$ is a real number.

(2) Prove: for any complex number $a \ne 0$ and any real number $\theta$, the equation
$$
1 + z^{23} + a z^{64} = 0
$$
has at least one root in the set
$$
S_{\theta} = \{z \in \mathbb{C} \mid \mathrm{Re}(z \cdot e^{-i\theta}) \ge |z| \cdot \cos \frac{\pi}{20}\}.
$$


## 2023 — 4

**Record:** `chn_2023_d02731`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_d02731.json.gz).

A nonempty set $A$ of integers is called a “beautiful set” if for any $a \in A$ and $k \in \{1, 2, \dots, 2023\}$, the set
$$
\{b \in A \mid \lfloor \frac{b}{3^k} \rfloor = \lfloor \frac{a}{3^k} \rfloor \}
$$
has exactly $2^k$ elements.
Prove that: if the intersection of an integer set $S$ and any beautiful set is not empty, then $S$ contains a beautiful set.

*Note:* Here $\lfloor x \rfloor$ represents the greatest integer not exceeding $x$.


## 2023 — 2

**Record:** `ind_2023_438140`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2023_438140.json.gz).

Let $g: \mathbb{N} \to \mathbb{N}$ be a bijective function and suppose that $f: \mathbb{N} \to \mathbb{N}$ is a function such that:
• For all naturals $x$, $f^{2023}(x) = x$
• For all naturals $x, y$ such that $x \mid y$, we have $f(x) \mid g(y)$.
Prove that $f(x) = x$.


## 2023 — Problem 1

**Record:** `ind_2023_6854af`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2023_6854af.json.gz).

Find all $f: \mathbb{N} \to \mathbb{N}$ such that $f(x) + y$ and $f(y) + x$ have the same number of 1's in their binary representation for any $x, y \in \mathbb{N}$.


## 2023 — Problem 3

**Record:** `ind_2023_78c50a`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2023_78c50a.json.gz).

Prove that for all integers $k > 2$, there exists $k$ distinct positive integers $a_1, \dots, a_k$ such that
$$
\sum_{1 \le i < j \le k} \frac{1}{a_i a_j} = 1.
$$


## 2023 — USA TST 2023/3

**Record:** `usa_2023_4eb572`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2023_4eb572.json.gz).

Consider pairs $(f, g)$ of functions from the set of nonnegative integers to itself such that
* $f(0) \ge f(1) \ge f(2) \ge \dots \ge f(300) \ge 0$;
* $f(0) + f(1) + f(2) + \dots + f(300) \le 300$;
* for any 20 nonnegative integers $n_1, n_2, \dots, n_{20}$, not necessarily distinct, we have
$$
g(n_1 + n_2 + \dots + n_{20}) \le f(n_1) + f(n_2) + \dots + f(n_{20}).
$$
Determine the maximum possible value of $g(0) + g(1) + \dots + g(6000)$ over all such pairs of functions.


## 2023 — USA TST 2023/5

**Record:** `usa_2023_9d8847`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2023_9d8847.json.gz).

Let $m$ and $n$ be fixed positive integers. Tsvety and Freyja play a game on an infinite grid of unit square cells. Tsvety has secretly written a real number inside of each cell so that the sum of the numbers within every rectangle of size either $m \times n$ or $n \times m$ is zero. Freyja wants to learn all of these numbers.

One by one, Freyja asks Tsvety about some cell in the grid, and Tsvety truthfully reveals what number is written in it. Freyja wins if, at any point, Freyja can simultaneously deduce the number written in every cell of the entire infinite grid. (If this never occurs, Freyja has lost the game and Tsvety wins.)

In terms of $m$ and $n$, find the smallest number of questions that Freyja must ask to win, or show that no finite number of questions can suffice.


## 2023 — 2

**Record:** `usa_2023_ca255f`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2023_ca255f.json.gz).

Let $n \ge m \ge 1$ be integers. Prove that
$$
\sum_{k=m}^{n} \left( \frac{1}{k^2} + \frac{1}{k^3} \right) \ge m \cdot \left( \sum_{k=m}^{n} \frac{1}{k^2} \right)^2 .
$$


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


## 2023 — USA TST 2023/6

**Record:** `usa_2023_de1495`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2023_de1495.json.gz).

Fix a function $f: \mathbb{N} \to \mathbb{N}$ and for any $m, n \in \mathbb{N}$ define
$$
\Delta(m, n) = \underbrace{f(f(\dots f(m)\dots))}_{f(n) \text{ times}} - \underbrace{f(f(\dots f(n)\dots))}_{f(m) \text{ times}}.
$$
Suppose $\Delta(m, n) \neq 0$ for any distinct $m, n \in \mathbb{N}$. Show that $\Delta$ is unbounded, meaning that for any constant $C$ there exist $m, n \in \mathbb{N}$ with $|\Delta(m, n)| > C$.


## 2023 — 2

**Record:** `vnm_2023_5e265b`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2023_5e265b.json.gz).

Given three functions
$$
P(x) = (x^2 - 1)^{2023}, Q(x) = (2x + 1)^{14}, R(x) = \left(2x + 1 + \frac{2}{x}\right)^{34}.
$$
Initially, we pick a set $S$ containing two of these functions, and we perform some operations on it. Allowed operations include:
* Take two functions $p, q \in S$ and add one of $p+q, p-q$, or $pq$ to $S$.
* Take a function $p \in S$ and add $p^k$ to $S$ for $k$ is an arbitrary positive integer.
* Take a function $p \in S$ and choose a real number $t$, and add to $S$ one of the function $p+t, p-t, pt$.
Show that no matter how we pick $S$ in the beginning, there is no way we can perform finitely many operations on $S$ that would eventually yield the third function not in $S$.


## 2023 — 4

**Record:** `vnm_2023_77dbf4`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2023_77dbf4.json.gz).

Given are two coprime positive integers $a, b$ with $b$ odd and $a > 2$. The sequence $(x_n)$ is defined by $x_0 = 2$, $x_1 = a$ and $x_{n+2} = a x_{n+1} + b x_n$ for $n \ge 1$. Prove that

a) If $a$ is even then there do not exist positive integers $m, n, p$ such that $\frac{x_m}{x_n x_p}$ is a positive integer.

b) If $a$ is odd then there do not exist positive integers $m, n, p$ such that $mnp$ is even and $\frac{x_m}{x_n x_p}$ is a perfect square.


## 2024 — 3

**Record:** `chn_2024_420fd0`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2024_420fd0.json.gz).

Given an integer $n > 1$, let the real number $x > 1$ satisfy
$$
x^{101} - n x^{100} + n x - 1 = 0.
$$
Prove that for any real numbers $0 < a < b < 1$, there exists a positive integer $m$ such that
$$
a < \{x^m\} < b.
$$
Here $\{t\} = t - \lfloor t \rfloor$ denotes the fractional part of the real number $t$.


## 2024 — 3

**Record:** `chn_2024_44289a`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2024_44289a.json.gz).

Given an integer $n \ge 3$. Let $\frac{n(n-1)}{2}$ non-negative real numbers $x_{i,j}$ ($1 \le i < j \le n$) satisfy: for any $1 \le i < j < k \le n$, we have $x_{i,j} + x_{j,k} \le x_{i,k}$. Prove that:
$$
\left\lfloor \frac{n^2}{4} \right\rfloor \cdot \sum_{1 \le i < j \le n} x_{i,j}^4 \ge \left( \sum_{1 \le i < j \le n} x_{i,j}^2 \right)^2 .
$$


## 2024 — 6

**Record:** `chn_2024_7afa57`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2024_7afa57.json.gz).

Given positive integers $m, n$ and non-negative real numbers $a_0, a_1, \dots, a_m, b_0, b_1, \dots, b_n$. Define
$$
c_k = \max_{i+j=k} a_i b_j \quad (k = 0, 1, \dots, m+n).
$$
Prove that:
$$
\frac{c_0 + c_1 + \dots + c_{m+n}}{m+n+1} \ge \frac{a_0 + a_1 + \dots + a_m}{m+1} \cdot \frac{b_0 + b_1 + \dots + b_n}{n+1}.
$$


## 2024 — 2

**Record:** `chn_2024_cc0bb9`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2024_cc0bb9.json.gz).

For a positive integer $n$, a subset $S$ of $\{1,2,\dots,n\}$ is called an $n$-good set if for any elements $x,y$ in $S$ (they can be the same), if $x+y \le n$, then $x+y \in S$.
For a positive integer $n$, define $r_n$ as the smallest real number such that for any positive integer $m \le n$, there exists an $n$-good set with $m$ elements, whose sum of all elements does not exceed $m \cdot r_n$.
Prove that there exists a real number $\alpha$ such that for any positive integer $n$, we have $|r_n - \alpha n| < 2024$.


## 2024 — 3

**Record:** `ind_2024_147f67`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2024_147f67.json.gz).

Find all functions $f : \mathbb{R} \to \mathbb{R}$ such that for all real numbers $a, b, c$, we have
$$
f(a + b + c)f(ab + bc + ca) - f(a)f(b)f(c) = f(a + b)f(b + c)f(c + a).
$$


## 2024 — 1

**Record:** `ind_2024_5998d9`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2024_5998d9.json.gz).

Let $r > 0$ be a real number. We call a monic polynomial with complex coefficients $r$-good if all of its roots have absolute value at most $r$. We call a monic polynomial with complex coefficients *primordial* if all of its coefficients have absolute value at most 1.

a. Prove that any 1-good polynomial has a primordial multiple.

b. If $r > 1$, prove that there exists an $r$-good polynomial that does not have a primordial multiple.


## 2024 — 1.

**Record:** `ind_2024_8f9865`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2024_8f9865.json.gz).

Let $n$ be a positive integer. Let $s: \mathbb{N} \to \{1, \dots, n\}$ be a function such that $n$ divides $m - s(m)$ for all positive integers $m$. Let $a_0, a_1, a_2, \dots$ be a sequence such that $a_0 = 0$ and
$$
a_k = a_{k-1} + s(k) \text{ for all } k \ge 1.
$$
Find all $n$ for which this sequence contains all the residues modulo $(n+1)^2$.


## 2024 — 2.

**Record:** `ind_2024_af0b04`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2024_af0b04.json.gz).

Let $x_1, x_2, \dots, x_{2024}$ be non-negative real numbers such that $x_1 \le x_2 \le \dots \le x_{2024}$, and $x_1^3 + x_2^3 + \dots + x_{2024}^3 = 2024$. Prove that
$$
\sum_{1 \le i < j \le 2024} (-1)^{i+j} x_i^2 x_j \ge -1012.
$$


## 2024 — 3

**Record:** `ind_2024_be9bfd`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2024_be9bfd.json.gz).

Let $P(x) \in \mathbb{Q}[x]$ be a polynomial with rational coefficients and degree $d \ge 2$. Prove there is no infinite sequence $a_0, a_1, \dots$ of rational numbers such that $P(a_i) = a_{i-1} + i$ for all $i \ge 1$.


## 2025 — Problem 10.

**Record:** `chn_2025_4d380b`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_4d380b.json.gz).

For a finite non-empty set $A$ of real numbers, let $\max(A)$ denote its maximum element, and define:
$$
P(A) = \sum_{\substack{B \subseteq A \\ |B| \text{ odd}}} m(B), \quad Q(A) = \sum_{\substack{\emptyset \neq B \subseteq A \\ |B| \text{ even}}} m(B),
$$
where $m(B)$ is the median of finite non-empty set $B$: if $B = \{b_1, b_2, \dots, b_n\}$ ($b_1 < b_2 < \dots < b_n$), then $m(B) = \frac{1}{2}(b_{\lfloor \frac{n+1}{2} \rfloor} + b_{\lceil \frac{n+1}{2} \rceil})$.
Find the smallest real number $c$ such that for any set $A$ of 2025 distinct positive real numbers,
$$
P(A) - Q(A) \leq c \cdot \max(A).
$$


## 2025 — Problem 2.

**Record:** `chn_2025_5ae358`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_5ae358.json.gz).

Let $p_1, p_2, \dots, p_{2025}$ be real numbers, and let $\{a_n^{(1)}\}_{n \ge 0}$, $\{a_n^{(2)}\}_{n \ge 0}$, $\dots$, $\{a_n^{(2025)}\}_{n \ge 0}$ be $2025$ real sequences satisfying:
(1) $a_0^{(i)}$ ($1 \le i \le 2025$) are all zero;
(2) $a_1^{(i)}$ ($1 \le i \le 2025$) are **not** all zero;
(3) For $i = 1, 2, \dots, 2025$ and any positive integer $n$,
$$
a_{n-1}^{(i)} + a_n^{(i)} + a_{n+1}^{(i)} = p_i \cdot a_n^{(i+1)},
$$
where $a_n^{(2026)} = a_n^{(1)}$.
Prove that there exists a positive real number $r$ and infinitely many positive integers $n$ such that
$$
\max \{|a_n^{(1)}|, |a_n^{(2)}|, \dots, |a_n^{(2025)}|\} > r.
$$


## 2025 — Problem 6.

**Record:** `chn_2025_9cc0fb`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_9cc0fb.json.gz).

Find the smallest real number $M$ such that there exist complex numbers $a, b, c, d$ with $|a| = |b| = |c| = |d| = 1$ satisfying: for any complex number $z$ with $|z| = 1$,
$$
|az^3 + bz^2 + cz + d| \le M.
$$


## 2025 — Problem 3.

**Record:** `chn_2025_d18489`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_d18489.json.gz).

Given nonzero real numbers $\lambda_1, \lambda_2, \dots, \lambda_{2025}$ and a real number $d$. Let $X$ be a finite set of real numbers. Define the sets:
$$
A = \{(x_1, \dots, x_{2025}) \in X^{2025} \mid \lambda_1 x_1 + \dots + \lambda_{2025} x_{2025} = d\};
$$
$$
B = \{(x_1, \dots, x_{2024}) \in X^{2024} \mid x_1 + \dots + x_{1012} = x_{1013} + \dots + x_{2024}\};
$$
$$
C = \{(x_1, \dots, x_{2026}) \in X^{2026} \mid x_1 + \dots + x_{1013} = x_{1014} + \dots + x_{2026}\};
$$
where $X^n$ denotes the set of all ordered tuples $(x_1, \dots, x_n)$ with $x_i \in X$ ($i = 1, \dots, n$).
Prove: $|A|^2 \le |B| \cdot |C|$, where $|Y|$ denotes the number of elements in the finite set $Y$.


## 2025 — Problem 12.

**Record:** `chn_2025_e6abc2`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_e6abc2.json.gz).

Find all functions $f : \mathbb{Z} \to \mathbb{Z}$ satisfying:
(1) For any positive integer $M$, there exists an integer $k$ with $|f(k)| \ge M$;
(2) For any integers $m, n$,
$$2f(m)f(n) - f(m - n) - 1$$ is a perfect square.


## 2025 — Problem 8

**Record:** `usa_2025_24dab7`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_24dab7.json.gz).

Find all polynomials $f$ with integer coefficients such that for all positive integers $n$, $n$ divides $\underbrace{f(f(\dots(f(0))\dots))}_{n+1 \text{ f's}} -1$.


## 2025 — Problem 2

**Record:** `usa_2025_990fe9`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_990fe9.json.gz).

Let $f: \mathbb{R} \to \mathbb{Z}$ be a function satisfying
$$
f(x - y) - 2f(x) + f(x + y) \geq -1
$$
for all $x, y \in \mathbb{R}$. Find all possible values of the set $\{f(x) \mid x \in \mathbb{R}\}$.


## 2025 — TSTST 2

**Record:** `usa_2025_a11fb3`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_a11fb3.json.gz).

Let $f: \mathbb{R} \to \mathbb{Z}$ be a function satisfying
$$
f(x - y) - 2f(x) + f(x + y) \geq -1
$$
for all $x, y \in \mathbb{R}$. Find all possible values of the set $\{f(x) \mid x \in \mathbb{R}\}$.


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


## 2025 — 2

**Record:** `usa_2025_c14ae8`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_c14ae8.json.gz).

Let $a_1, a_2, \dots$ and $b_1, b_2, \dots$ be sequences of real numbers for which $a_1 > b_1$ and
$$
a_{n+1} = a_n^2 - 2b_n
$$
$$
b_{n+1} = b_n^2 - 2a_n
$$
for all positive integers $n$. Prove that $a_1, a_2, \dots$ is eventually increasing (that is, there exists a positive integer $N$ for which $a_k < a_{k+1}$ for all $k > N$).


## 2025 — Problem 7

**Record:** `usa_2025_d9378d`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_d9378d.json.gz).

For a positive real number $c$, the sequence $a_1, a_2, \dots$ of real numbers is defined as follows. Let $a_1 = c$, and for $n \ge 2$, let
$$
a_n = \sum_{i=1}^{n-1} (a_i)^{n-i+1}.
$$
Find all positive real numbers $c$ such that $a_i > a_{i+1}$ for all positive integers $i$.



# IMOTC source statements

## 2023 — Problem 3

**Record:** `ind_2023_092f9b`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2023_092f9b.json.gz).

Prove that for all integers $k > 2$, there exists $k$ distinct positive integers $a_1, \dots, a_k$ such that
$$
\sum_{1 \le i < j \le k} \frac{1}{a_i a_j} = 1.
$$



# IranMO source statements

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


## 2015 — 8

**Record:** `irn_2015_80e073`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/iran/irn_2015_80e073.json.gz).

For each nonnegative integer $n$, polynomial $K_n(x_1, x_2, ..., x_n)$ is defined recursively as follows,
$$
\begin{array}{l}
K_0 = 1 \\
K_1(x_1) = x_1 \\
K_n(x_1, \dots, x_n) = x_n K_{n-1}(x_1, \dots, x_{n-1}) + (x_n^2 + x_{n-1}^2) K_{n-2}(x_1, \dots, x_{n-2}).
\end{array}
$$
Prove that $K_n(x_1, x_2, ..., x_{n-1}, x_n) = K_n(x_n, x_{n-1}, ..., x_2, x_1)$.


## 2015 — 5

**Record:** `irn_2015_8e5525`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/iran/irn_2015_8e5525.json.gz).

A non-empty set $S$ of positive real numbers is called **powerful** if for any two distinct elements of it like $a$ and $b$, at least one of the numbers $a^b$ or $b^a$ is an element of $S$.

a) Present an example of a powerful set having four elements.

b) Prove that a finite powerful set cannot have more than four elements.



# JMO source statements

## 2006 — 5

**Record:** `jpn_2006_02674c`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2006_02674c.json.gz).

Answer the maximum value of $A$ for which, for every positive $x_1, x_2, x_3, y_1, y_2, y_3, z_1, z_2$ and $z_3$, the inequality
$$
(x_1^3 + x_2^3 + x_3^3 + 1)(y_1^3 + y_2^3 + y_3^3 + 1)(z_1^3 + z_2^3 + z_3^3 + 1) 
\geq A(x_1 + y_1 + z_1)(x_2 + y_2 + z_2)(x_3 + y_3 + z_3)
$$
holds.
For the maximum value of $A$, establish the cases of equality.


## 2006 — 3

**Record:** `jpn_2006_3a7b23`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2006_3a7b23.json.gz).

Find every $f : \mathbb{R} \to \mathbb{R}$ such that for any $x$ and $y$,
$$
f(x)^2 + 2y f(x) + f(y) = f(y + f(x)).
$$


## 2006 — 1

**Record:** `jpn_2006_85d536`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2006_85d536.json.gz).

$n$ is a positive 3-digit number, and its hundred's place and its one's place are not $0$. Make a new number by exchanging the hundred's place and the one's place of $n$, and call it $m$. Answer the maximum value of $n - m$.


## 2006 — 2

**Record:** `jpn_2006_966084`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2006_966084.json.gz).

Find every integer $k$ that satisfies the following condition.
There are infinitely many triplet $(a, b, c)$ of integers such that $(a^2 - k)(b^2 - k) = c^2 - k$.


## 2006 — 5

**Record:** `jpn_2006_a460fb`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2006_a460fb.json.gz).

Find all real numbers $x$, $y$ and $z$ such that all the following equations hold.
$$
x^2 - 3y - z = -8
$$
$$
y^2 - 5z - x = -12
$$
$$
z^2 - x - y = 6
$$


## 2006 — 8

**Record:** `jpn_2006_a53c60`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2006_a53c60.json.gz).

Tomohiro and Akinori read mathematical books as follows. Akinori reads 2 pages a day. Tomohiro reads 3 pages a day. However, each of the two stop reading of that day if he reaches the end of a chapter.

There is a mathematical book which consists of 10 chapters and 120 pages. Find the smallest value of the difference between the number of days in which Akinori reads the book and that of Tomohiro. A new chapter always begins with a new page.


## 2006 — 4

**Record:** `jpn_2006_e5e5b8`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2006_e5e5b8.json.gz).

Find three distinct positive integers which minimize their sum under the condition that any two of them add up to a perfect square.


## 2007 — 5

**Record:** `jpn_2007_07e0bb`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_07e0bb.json.gz).

There is a grid of $5 \times 5$. And write the integers $1,2,\ldots,16$ in all the grids (each number can be written only once) in the upper left grid of $4 \times 4$ (♣). About the 4 rows, write the sum of four numbers that are written in each row at the right end of each row. Similarly, about the 4 columns, write the sum of four numbers that are written in each column at the lower end of each column. And nothing is written in the lower right grid. Find the maximum integer $m$ which satisfies the following condition.

Conditions: About step (♣), there exists a way of writing the numbers such that you can choose two numbers $a, b$ which $|a-b| \ge m$ hold from the right end column and also from the lower end row.


## 2007 — 4

**Record:** `jpn_2007_4de1ef`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_4de1ef.json.gz).

Find one of the polynomials $f(x, y, z)$ whose degree is $3$, with real coefficients, that satisfy the following conditions.
• $f(x, y, z) + x$ is divisible by $y + z$
• $f(x, y, z) + y$ is divisible by $z + x$
• $f(x, y, z) + z$ is divisible by $x + y$
A polynomial $P(x, y, z)$ is divisible by a polynomial $Q(x, y, z)$ means that there exists a polynomial $R(x, y, z)$ that satisfies $P(x, y, z) = Q(x, y, z)R(x, y, z)$.


## 2007 — 2

**Record:** `jpn_2007_6b2668`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_6b2668.json.gz).

Determine ten's place of $11^{12^{13}}$. ($12^{13}$th power of $11$, not $13$th power of $11^{12}$.)


## 2007 — 5

**Record:** `jpn_2007_9c69b3`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_9c69b3.json.gz).

Let $[r]$ be the largest integer not exceeding real number $r$. For real positive numbers $x$, the set $A(x)$ is defined by
$$
A(x) = \{[nx] \mid n: \text{positive integer}\}.
$$
Find all irrational numbers $\alpha > 1$ satisfying the following condition.
Condition: If a positive real number $\beta$ satisfies $A(\alpha) \supset A(\beta)$, then $\frac{\beta}{\alpha}$ is an integer.


## 2007 — 11

**Record:** `jpn_2007_b2e5f1`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_b2e5f1.json.gz).

In a mathematical competition, gold medals are given to $\lfloor \frac{n}{a} \rfloor$ people, silver medals to $\lfloor \frac{n}{b} \rfloor$ and bronze medals to $\lfloor \frac{n}{c} \rfloor$ ($a \ge b \ge c$ are integer constants and $n$ is the number of participants). No one gets two or more medals. Determine all triplets $(a, b, c)$ with the following property.

Property: For all integer $k \ge 3$, there are exactly two $n$ such that the number of people without medals are $k$.

* $[r]$ is the maximum integer that does not exceed $r$.


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


## 2007 — 6

**Record:** `jpn_2007_f72375`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_f72375.json.gz).

We have 15 cards numbered $1$, $2$, $\dots$, $15$. How many ways are there to choose some (at least 1) cards so that all numbers on these cards are larger than or equal to the number of cards chosen?


## 2008 — 7

**Record:** `jpn_2008_0160ba`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2008_0160ba.json.gz).

How many 3-digit numbers are there that can appear as the top three digits of a 6-digit number, which is a perfect square?


## 2008 — 4

**Record:** `jpn_2008_49ef98`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2008_49ef98.json.gz).

Determine all the real-valued functions $f$ defined on the real line, which satisfies for all real numbers $x$ and $y$
$$
f(x+y)f(f(x)-y) = xf(x) - yf(y).
$$


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


## 2008 — 12

**Record:** `jpn_2008_ade892`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2008_ade892.json.gz).

Suppose that the combination $(n; a_1, a_2, \dots, a_n)$ of positive integers satisfy the condition $a_1 + a_2 + \dots + a_n = 2008$. Let for each $k$ with $1 \le k \le n$, $A_k = a_1a_2\cdots a_k$. Determine the maximum possible value that the quantity $A_1 + A_2 + \dots + A_n$ can take.


## 2008 — 9

**Record:** `jpn_2008_babc4b`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2008_babc4b.json.gz).

Suppose $2008$ real numbers $x_1, x_2, \dots, x_{2008}$ are given and suppose that $|x_1| = 999$ and $|x_n| = |x_{n-1} + 1|$ for all $n$ with $2 \le n \le 2008$ are satisfied. Determine the smallest possible value that $x_1 + x_2 + \dots + x_{2008}$ can have under these conditions.


## 2008 — 3

**Record:** `jpn_2008_eec352`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2008_eec352.json.gz).

Currently circulating coins in Japanese currency come in 6 different denominations: 500 yen, 100 yen, 50 yen, 10 yen, 5 yen and 1 yen. Taro had 1 each of 1000 yen note, 100 yen coin, 10 yen coin and 1 yen coin. He made a certain purchase from a merchant and handed him all he had and received some change. Assume that Taro made the payment in such a way that he would not receive in the change any coins of the denominations same as what he had had to begin with, nor a 1000 yen note. Furthermore, he chose the method of the payment so that he would end up with the minimum possible number of coins when he received his change. Assume also that the merchant gave Taro the change with minimum possible number of coins. Count the case of no change as a possibility for the purchase price also. Under these conditions how many distinct purchase prices are possible?


## 2009 — 11

**Record:** `jpn_2009_02108c`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2009_02108c.json.gz).

For a real number $r$, let $[r]$ represent the largest integer less than or equal to $r$. Determine the sum of all real numbers $x$ which satisfy the equation
$$
[x] + [2x] + [3x] + [4x] + [5x] + [6x] + [7x] + [8x] + [9x] = 44x.
$$


## 2009 — 8

**Record:** `jpn_2009_0c4c51`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2009_0c4c51.json.gz).

Both $f(x)$ and $g(x)$ are polynomials with real coefficients, and are not identically zero. Suppose that they satisfy the following functional equation:
$$
f(x^3) + g(x) = f(x) + x^5g(x)
$$
Give an example of such a function $f(x)$ with the smallest possible degree.


## 2009 — 3

**Record:** `jpn_2009_222056`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2009_222056.json.gz).

Let $k$ be an integer greater than or equal to $2$, and let $n_1$, $n_2$, $n_3$ be positive integers, and $a_1$, $a_2$, $a_3$ be integers greater than or equal to $1$ and less than or equal to $k-1$. Define
$$
b_i = a_i \sum_{j=0}^{n_i} k^j \quad (i = 1, 2, 3).
$$
Determine all possible combinations $(n_1, n_2, n_3)$ if $b_1 b_2 = b_3$.


## 2009 — 10

**Record:** `jpn_2009_39c357`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2009_39c357.json.gz).

Compute the value of
$$
\frac{\sum_{n=1}^{99} (\sqrt{10 + \sqrt{n}})}{\sum_{n=1}^{99} (\sqrt{10 - \sqrt{n}})}
$$


## 2009 — 5

**Record:** `jpn_2009_52732e`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2009_52732e.json.gz).

Determine all non-negative real-valued functions $f$ defined for non-negative real numbers, which satisfy
$$
f(x^2) + f(y) = f(x^2 + y + x f(4y))
$$
for every pair of non-negative real numbers $x$ and $y$.


## 2009 — 3

**Record:** `jpn_2009_8f1a5c`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2009_8f1a5c.json.gz).

Determine all the triples $(a, b, c)$ of positive integers which satisfy the following 2 identities. Distinguish two triples which are obtained by permuting the order of the same set of three numbers.
$$
ab + c = 13, \quad a + bc = 23.
$$


## 2009 — 1

**Record:** `jpn_2009_902407`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2009_902407.json.gz).

Determine the number which can be represented in the form $n^2 + 4n$ for some positive integer $n$ and for which the absolute value of its difference from the number $10000$ is the smallest.


## 2009 — 1

**Record:** `jpn_2009_be6d0b`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2009_be6d0b.json.gz).

Determine all positive integers $n$ for which $8^n + n$ is divisible by $2^n + n$.


## 2009 — 2

**Record:** `jpn_2009_c83064`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2009_c83064.json.gz).

Let $N$ be a positive integer. Suppose some collection of integers are written on a blackboard satisfying the following properties.
* Every number $k$ written satisfies $1 \le k \le N$.
* Every $k$ with $1 \le k \le N$ is written at least once.
* The sum of all the numbers written is even.
Prove that by marking some of the numbers written by $\mathcal{O}$ and the rest by $\times$, it is possible to make the sum of those marked by $\mathcal{O}$ equal to the sum of those marked by $\times$.


## 2009 — 7

**Record:** `jpn_2009_de56c9`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2009_de56c9.json.gz).

Suppose the real numbers $x_1, x_2, x_3, x_4, x_5$ satisfy the following set of five equations:
$$
\begin{cases}
x_1x_2 + x_1x_3 + x_1x_4 + x_1x_5 = -1 \\
x_2x_1 + x_2x_3 + x_2x_4 + x_2x_5 = -1 \\
x_3x_1 + x_3x_2 + x_3x_4 + x_3x_5 = -1 \\
x_4x_1 + x_4x_2 + x_4x_3 + x_4x_5 = -1 \\
x_5x_1 + x_5x_2 + x_5x_3 + x_5x_4 = -1
\end{cases}
$$
Determine all the possible values that the number $x_1$ can take.


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


## 2011 — 1

**Record:** `jpn_2011_9ace44`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2011_9ace44.json.gz).

How many quadruples $(a, b, c, d)$ of positive integers lying in between $1$ and $9$ ($1$ and $9$ inclusive) are there which satisfy $0 < b - a < c - b < d - c$?


## 2012 — 10

**Record:** `jpn_2012_01d81d`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2012_01d81d.json.gz).

For a real number $r$ denote by $[r]$ the greatest integer less than or equal to $r$. How many positive integers $n$ are there for which
$$
\lfloor \frac{1000000}{n} \rfloor - \lfloor \frac{1000000}{n+1} \rfloor = 1
$$
is satisfied?


## 2012 — 9

**Record:** `jpn_2012_2146b7`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2012_2146b7.json.gz).

Players $A$ and $B$ wrote down two positive integers each on a black board. The product of the two numbers $A$ wrote is twice the sum of the two numbers $B$ wrote, and the product of the two numbers $B$ wrote is twice the sum of the two numbers $A$ wrote, and furthermore, the sum of the two numbers $A$ wrote is greater than or equal to the sum of the two numbers $B$ wrote. Determine all possible values for the sum of the two numbers $B$ wrote. Note that four numbers written down need not be distinct.


## 2012 — 3

**Record:** `jpn_2012_365658`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2012_365658.json.gz).

Let $a, b, c, d, e, f, g, h, i$ be the distinct integers lying in between $1$ and $9$ (both $1$ and $9$ inclusive). Let $N$ be the maximum of the three numbers $a \times b \times c$, $d \times e \times f$ and $g \times h \times i$. Determine the minimum value the number $N$ can take.


## 2012 — 2

**Record:** `jpn_2012_3f1a68`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2012_3f1a68.json.gz).

Find all functions $f : \mathbb{R} \to \mathbb{R}$ such that
$$
f(f(x+y)f(x-y)) = x^2 - y f(y)
$$
for all $x, y \in \mathbb{R}$.


## 2012 — 4

**Record:** `jpn_2012_654103`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2012_654103.json.gz).

Let $A$ be a positive integer which is a multiple of $3$ but not of $9$. When we add to $A$ the product of all the digits of $A$, then we obtain a number which is a multiple of $9$. Find the smallest possible value for such a number $A$.


## 2012 — 8

**Record:** `jpn_2012_70a429`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2012_70a429.json.gz).

How many possible ways of writing down a sequence of positive integers are there satisfying the following conditions?
Conditions: You start out with writing down the number $2012$ and end up with writing down the number $1$, and after writing down a number $n$ you follow with writing an integer less than or equal to $\sqrt{n}$.


## 2012 — 2

**Record:** `jpn_2012_7f3ce5`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2012_7f3ce5.json.gz).

Determine all the real valued functions $f$ defined on the real line for which the following identity is satisfied for every pair of real numbers $x, y$:
$$
f(f(x+y)f(x-y)) = x^2 - y f(y).
$$


## 2013 — 4

**Record:** `jpn_2013_001a20`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_001a20.json.gz).

Let for $k$, $0 \le k \le 9$, $a_k$ be the coefficient of the $x^k$-term in the polynomial $(x+1)^3(x+2)^3(x+3)^3$. Find the value of $a_2 + a_4 + a_6 + a_8$.


## 2013 — 7

**Record:** `jpn_2013_050803`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_050803.json.gz).

How many 25-tuples $(x_1, x_2, \dots, x_{25})$ of non-negative integers are there which satisfy the following identity?
$$
x_1^2 + x_2^2 + \dots + x_{25}^2 = 2 + x_1x_2 + x_2x_3 + \dots + x_{24}x_{25}.
$$


## 2013 — 2

**Record:** `jpn_2013_1d4231`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_1d4231.json.gz).

Suppose two $20 \times 13$ rectangular grids consisting of $260$ small squares are given.
We insert into each square box of the two grids, numbers $1, 2, \ldots, 260$ in the following way:

* For the first grid, we start inserting numbers $1, 2, \ldots, 13$ into the boxes on the top row from left to right. Continue to insert numbers $14, 15, \ldots, 26$ into the boxes on the second row from left to right. Keep on going until you finish inserting numbers $248, 249, \ldots, 260$ from left to right into the boxes on the bottom row.

* For the second grid, we start inserting numbers $1, 2, \ldots, 20$ into the boxes on the right-most column from top to bottom. Continue to insert numbers $21, 22, \ldots, 40$ into the boxes on the second column from the right from top to bottom. Keep on doing until you finish inserting numbers $241, 242, \ldots, 260$ into the boxes on the left most column from top to bottom.

List all the positive integers which get inserted into the boxes located in the same position in the two grids in the two ways of distributing numbers described above.


## 2013 — 1

**Record:** `jpn_2013_45e694`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_45e694.json.gz).

Let $n, k$ be positive integers satisfying $n \ge k$.
There is a group consisting of $n$ people. Each person of this group belongs to one and only one of $k$ clubs, called club $C_1, C_2, \dots, C_k$. Each club has at least one member belonging to it. Prove that it is possible to distribute $n^2$ pieces of cake to these $n$ people in such a way to satisfy all of the following conditions:
* Every one receives at least 1 piece of cake.
* For each $i$ $1 \le i \le k$, every member of the club $C_i$ receives $a_i$ pieces of cake.
* If $1 \le i < j \le k$, then $a_i > a_j$ is satisfied.


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


## 2013 — 2

**Record:** `jpn_2013_b3ca6b`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_b3ca6b.json.gz).

Determine all real-valued functions $f$ defined on the set of all integers and satisfying the following identity for an arbitrary pair $m, n$ of integers:
$$
f(m) + f(n) = f(mn) + f(m + n + mn).
$$


## 2013 — 12

**Record:** `jpn_2013_c38542`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_c38542.json.gz).

Let $a_1, a_2, \dots$ be an infinite sequence of distinct non-zero real numbers for which $\frac{a_{i+1}}{a_i} + \frac{a_{i+1}}{a_i}$ takes the same value lying in between 0 and 2 for each $i \ge 1$. Express in terms of $a_1, a_2, a_3$ the smallest number $c$ satisfying the following condition:
Condition: For any pair of positive integers $x, y$ with $x < y$,
$$
\frac{a_x a_{x+1} + a_{x+1} a_{x+2} + \dots + a_{y-1} a_y}{a_x a_y} \le c \quad \text{holds.}
$$


## 2014 — 8

**Record:** `jpn_2014_1d9af9`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2014_1d9af9.json.gz).

Let $m$ be a positive integer of $1000$ digits, with the property that all of its digits are non-zero. For a positive integer $n$, consider $\left\lfloor \frac{m}{n} \right\rfloor$, where we define for any real number $r$, $\lfloor r \rfloor$ to be the largest integer less than or equal to $r$. Determine the largest possible number of digits which are $0$ for $\left\lfloor \frac{m}{n} \right\rfloor$, where $1 \le n \le m$.


## 2014 — 6

**Record:** `jpn_2014_74269a`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2014_74269a.json.gz).

There are two blackboards $A$ and $B$, and on each of these blackboards certain number of distinct integers greater than or equal to $2$ and less than or equal to $20$ are written in such a way that any pair of numbers one of which is chosen from $A$ and the other from $B$ are relatively prime. Determine the maximum possible value the product of the number of integers written on $A$ and the number of integers written on $B$ can take.


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


## 2021 — 5

**Record:** `jpn_2021_8a2d04`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2021_8a2d04.json.gz).

Let $n$ be a positive integer. Determine all integers $1 \le k \le 2n^2$ satisfying the following condition.

> There is a $2n \times 2n$ board. When $k$ distinct cells are chosen and colored black, while the other cells are colored white, the minimum number of the $2 \times 2$ squares which have both black and white cells is $2n-1$.


## 2021 — 4

**Record:** `jpn_2021_ce7bea`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2021_ce7bea.json.gz).

There are three distinct positive integers written on the blackboard. When real numbers $a$, $b$, $c$ are on the blackboard, consider the procedure that replaces those three numbers with $\frac{b+c}{2}$, $\frac{c+a}{2}$, $\frac{a+b}{2}$ at the same time. After this procedure is done $2021$ times, all three numbers on the blackboard are positive integers. Determine the minimum value of the sum of initial three positive integers on the blackboard.


## 2022 — 8

**Record:** `jpn_2022_135c78`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2022_135c78.json.gz).

Find the number of tuples of positive integers $(a_1, a_2, \dots, a_{2022})$ which satisfy $a_1 < a_2 < \dots < a_{2022}$ and
$$
a_1^2 - 6^2 \ge a_2^2 - 7^2 \ge \dots \ge a_{2022}^2 - 2027^2.
$$


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


## 2022 — 2

**Record:** `jpn_2022_e889ae`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2022_e889ae.json.gz).

Let $N$ be the set of positive integers. Determine all functions $f : N \to N$ such that, for all positive integers $m$ and $n$,
$$
f^{f(n)}(m) + mn = f(m)f(n).
$$
Note that $f^k(n) = \underbrace{f(f(\cdots f(n)\cdots))}_{k \text{ times}}$.


## 2023 — 3

**Record:** `jpn_2023_4980a0`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2023_4980a0.json.gz).

Let $c$ be a non-negative integer. Find all sequences of positive integers $\{a_n\}_{n \ge 1}$ such that for any positive integer $n$, the following condition holds:
There are exactly $a_n$ positive integers $i$ satisfying $a_i \le a_{n+1} + c$.


## 2023 — 12

**Record:** `jpn_2023_648f4e`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2023_648f4e.json.gz).

Let $A$ be a set of functions defined for integers from $1$ to $2023$ and taking integer values from $1$ to $2023$. Suppose that $A$ satisfies the following two conditions:
* For any function $f$ belonging to $A$ and any integers $x$ and $y$ with $1 \le x < y \le 2023$, we have $f(x) \ge f(y)$.
* For any functions $f$ and $g$ belonging to $A$ and any integer $x$ from $1$ to $2023$, we have $f(g(x)) = g(f(g(x)))$.
In this case, find the maximum possible number of elements of $A$.


## 2023 — 5

**Record:** `jpn_2023_faa0e3`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2023_faa0e3.json.gz).

We denote $S = \{1, 2, \dots, 3000\}$. Find the maximum possible value of an integer $X$ that satisfies the following condition:
For any bijection $f: S \to S$, there exists a bijection $g: S \to S$ such that
$$
\sum_{k=1}^{3000} \left( \max\{f(f(k)), f(g(k)), g(f(k)), g(g(k))\} - \min\{f(f(k)), f(g(k)), g(f(k)), g(g(k))\} \right)
$$
is no less than $X$.


## 2024 — 11

**Record:** `jpn_2024_5a6712`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2024_5a6712.json.gz).

Let $N$ be the set of positive integers. A function $f: N \to N$ satisfies $f(34) = 2024$, and for any positive integers $a, b, c$, there exists a triangle with side lengths $a+f(b)$, $b+f(c)$, $c+f(a)$. Find the smallest possible value of $f(100) + f(101) + \dots + f(199)$ under these conditions. Note that three points lying on the same line do not form a triangle.


## 2024 — 2

**Record:** `jpn_2024_70520f`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2024_70520f.json.gz).

Positive integers such that all the digits are prime numbers are called excellent numbers. Determine all the three-digit positive integers $n$ such that $n + 2024$ and $n - 34$ are both excellent numbers. There exist exactly two such positive integers $n$.


## 2024 — 8

**Record:** `jpn_2024_714449`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2024_714449.json.gz).

Let $N_0$ be the set of nonnegative integers and $\mathbb{Z}$ be the set of integers. Find the number of possible tuples $(f(0), f(1), \dots, f(2024))$ for $f: N_0 \to \mathbb{Z}$ satisfying
$$
f(m+n)^2 = f(m|f(n)|) + f(n^2)
$$
for any $m, n \in N_0$.


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


## 2024 — 1

**Record:** `jpn_2024_e48072`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2024_e48072.json.gz).

Let $n \ge 2$ be an integer. Find all sets of real numbers $(a_1, a_2, \dots, a_n)$ such that $a_1 - 2a_2, a_2 - 2a_3, \dots, a_{n-1} - 2a_n, a_n - 2a_1$ is a permutation of $a_1, a_2, \dots, a_n$. Note that $a_1, a_2, \dots, a_n$ itself is also a permutation of $a_1, a_2, \dots, a_n$.


## 2024 — 5

**Record:** `jpn_2024_eb9ad6`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2024_eb9ad6.json.gz).

Find the smallest integer $n \ge 10$ such that
$$
\left[ \frac{n}{1} \right] \left[ \frac{n}{2} \right] \cdots \left[ \frac{n}{10} \right] = \binom{n}{10}
$$
Here denote by $[r]$ the largest integer less than or equal to $r$ for a real number $r$. For example, $[3.14] = 3$ and $[5] = 5$.


## 2025 — 8

**Record:** `jpn_2025_4c49c4`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2025_4c49c4.json.gz).

For an integer $n \ge 3$, a sequence of integers $a_1, a_2, \dots, a_n$ is called a **beautiful sequence** if the following conditions are all satisfied.
* $0 = a_1 < a_2 < \dots < a_n$.
* There exists an integer $i$ such that $1 \le i \le n$ and $a_i = 2025$.
* For all integers $i, j, k$ with $1 \le i < j < k \le n$, the inequality $\frac{a_i + a_k}{2} \le a_j$ holds.
Let $N$ be the maximum possible length of a beautiful sequence. For beautiful sequences $a_1, a_2, \dots, a_N$ of length $N$, determine the minimum possible value of $a_N$.
Here, the length of a sequence of integers $x_1, x_2, \dots, x_l$ is $l$.


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


## 2025 — 1

**Record:** `jpn_2025_b183a2`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2025_b183a2.json.gz).

Let $n \ge 2$ be an integer. Suppose that real numbers $a_1, a_2, \dots, a_{2n}$ satisfy $|a_k - a_{n+k}| \ge 1$ for every integer $k$ such that $1 \le k \le n$. Find the minimum possible value of
$$
(a_1 - a_2)^2 + (a_2 - a_3)^2 + \dots + (a_{2n-1} - a_{2n})^2 + (a_{2n} - a_1)^2.
$$


## 2025 — 4

**Record:** `jpn_2025_fd4cdd`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2025_fd4cdd.json.gz).

Determine all polynomials $f(x)$ with integer coefficients such that, for any integer $n \ge 2$, the following conditions hold:
$\bullet\ f(n) > 0.$
$\bullet\ f(n)$ divides $n^{f(n)} - 1$.



# KMO source statements

## 2006 — 4

**Record:** `kor_2006_673008`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2006_673008.json.gz).

For three mutually distinct real numbers $a_1$, $a_2$, $a_3$, define three real numbers $b_1$, $b_2$, $b_3$ as follows:
$$
b_j = \left( 1 + \frac{a_j a_i}{a_j - a_i} \right) \left( 1 + \frac{a_j a_k}{a_j - a_k} \right), \quad \{i, j, k\} = \{1, 2, 3\}.
$$
Prove the inequality
$$
1 + |a_1 b_1 + a_2 b_2 + a_3 b_3| \le (1 + |a_1|)(1 + |a_2|)(1 + |a_3|).
$$
When does the equality hold?


## 2007 — 6

**Record:** `kor_2007_5b3a67`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2007_5b3a67.json.gz).

Let $f: \mathbb{N} \to \mathbb{N}$ be a function satisfying
$$
k f(n) \le f(kn) \le k f(n) + k - 1
$$
for every $k, n \in \mathbb{N}$, where $\mathbb{N}$ is the set of all positive integers.
(1) Show that, for every $a, b \in \mathbb{N}$,
$$
f(a) + f(b) \le f(a + b) \le f(a) + f(b) + 1.
$$
(2) Show that, if $f$ satisfies
$$
f(2007n) \le 2007 f(n) + 2005
$$
for every $n \in \mathbb{N}$, then there exists $c \in \mathbb{N}$ such that $f(2007c) = 2007 f(c)$.


## 2008 — 2

**Record:** `kor_2008_ea6719`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2008_ea6719.json.gz).

Determine a polynomial $f(x)$ with integer coefficients which satisfies the following property: There are infinitely many relatively prime positive integers $a, b$ such that $a + b$ divides $f(a) + f(b)$.


## 2008 — 3

**Record:** `kor_2008_f70401`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2008_f70401.json.gz).

Find all functions $f: \mathbb{R}^+ \to \mathbb{R}$ satisfying
(i) $f(1) = 2008$,
(ii) $|f(x)| \le x^2 + 1004^2$, and
$$
(iii) \quad f\left(x + y + \frac{1}{x} + \frac{1}{y}\right) = f\left(x + \frac{1}{y}\right) + f\left(y + \frac{1}{x}\right)
$$
for all $x, y > 0$, where $\mathbb{R}$ is the set of all real numbers and $\mathbb{R}^+$ is the set of all positive real numbers.


## 2009 — 1

**Record:** `kor_2009_bab5c4`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2009_bab5c4.json.gz).

Let $a$, $b$ and $c$ be the sides of a triangle, and we set
$$
A = \frac{a^2 + bc}{b+c} + \frac{b^2 + ca}{c+a} + \frac{c^2 + ab}{a+b}
$$
$$
B = \frac{1}{\sqrt{(a+b-c)(b+c-a)}} + \frac{1}{\sqrt{(b+c-a)(c+a-b)}} + \frac{1}{\sqrt{(c+a-b)(a+b-c)}}
$$
Prove that $AB \ge 9$.


## 2011 — 6

**Record:** `kor_2011_33308c`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2011_33308c.json.gz).

We are given a rectangular $m \times n$ chessboard with $m$ unit squares in each row and $n$ unit squares in each column. We are going to assign an integer to each unit square. A rectangle $R$ consisting of one or more unit squares is called a *shelf* if there is an integer $h$ satisfying the following two conditions:

1. The number in each unit square in $R$ is larger than $h$.
2. The number in a unit square out of $R$ sharing an edge or a point with $R$ is at most $h$.

(We assume that a shelf $R$ contains all interior unit squares in the rectangle.) What is the number of shelves if we assign integers to maximize the number of shelves?


## 2011 — 1

**Record:** `kor_2011_babdb4`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2011_babdb4.json.gz).

Prove that there are no positive integers $x, y, z$ such that
$$
x^2 y^4 - x^4 y^2 + 4x^2 y^2 z^2 + x^2 z^4 - y^2 z^4 = 0.
$$


## 2011 — 4

**Record:** `kor_2011_d3f64b`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2011_d3f64b.json.gz).

Find the maximum value of
$$
\frac{1}{a^2 - 4a + 9} + \frac{1}{b^2 - 4b + 9} + \frac{1}{c^2 - 4c + 9}
$$
where $a$, $b$, $c$ are non-negative real numbers satisfying $a + b + c = 1$.


## 2013 — 5

**Record:** `kor_2013_090453`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2013_090453.json.gz).

Let $a$, $b$ be relatively prime positive integers and let $a_n$ and $b_n$ be integer sequences satisfying $(a + b\sqrt{2})^{2n} = a_n + b_n\sqrt{2}$. Find all primes $p$ such that there is a positive integer $n$ less than or equal to $p$ satisfying $b_n \equiv 0 \pmod{p}$.


## 2013 — 3

**Record:** `kor_2013_3747e5`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2013_3747e5.json.gz).

Given a positive integer $n \ge 2$, define the set $T$ by
$$
T = \{ (i, j) : 1 \le i < j \le n \text{ and } i \ne j \}.
$$
For nonnegative real numbers $x_1, x_2, \dots, x_n$ satisfying $x_1 + x_2 + \dots + x_n = 1$, find the maximum (as a function of $n$) of
$$
\sum_{(i,j) \in T} x_i x_j.
$$


## 2013 — 2

**Record:** `kor_2013_c1caf4`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2013_c1caf4.json.gz).

Find all functions $f : \mathbb{R} \to [0, \infty)$ such that, for all real $a, b, c, d$ that satisfy $ab + bc + cd = 0$, the following equality holds:
$$
f(a - b) + f(c - d) = f(a) + f(b + c) + f(d)
$$
(Here $\mathbb{R}$ is the set of real numbers and $[0, \infty)$ is the set of nonnegative real numbers.)


## 2014 — Problem 1

**Record:** `kor_2014_f7ac50`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2014_f7ac50.json.gz).

Let $x$, $y$, $z$ be positive real numbers satisfying $x + y + z = 1$. Prove that
$$
\frac{(1 + xy + yz + zx)(1 + 3x^3 + 3y^3 + 3z^3)}{9(x + y)(y + z)(z + x)} \ge \left( \frac{x\sqrt{1+x}}{\sqrt[4]{3+9x^2}} + \frac{y\sqrt{1+y}}{\sqrt[4]{3+9y^2}} + \frac{z\sqrt{1+z}}{\sqrt[4]{3+9z^2}} \right)^2
$$


## 2015 — 1

**Record:** `kor_2015_4c6641`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2015_4c6641.json.gz).

Find all functions $f : \mathbb{R} \to \mathbb{R}$ such that for all $x, y \in \mathbb{R}$
$$
f(x^{2015} + f(y)^{2015}) = f(x)^{2015} + y^{2015}.
$$


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


## 2016 — Problem 4

**Record:** `kor_2016_713232`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2016_713232.json.gz).

Find the maximum value of $(x^2 - yz)(y^2 - zx)(z^2 - xy)$ given that $x, y, z$ are real numbers satisfying $x^2 + y^2 + z^2 = 1$.


## 2023 — 6

**Record:** `kor_2023_57d25e`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2023_57d25e.json.gz).

For an integer $n \ge 3$ and real numbers $a_1, \dots, a_n$ and $b_1, \dots, b_n$, show the following inequality.
$$
\sum_{i=1}^{n} a_i (b_i - b_{i+3}) \le \frac{3n}{8} \sum_{i=1}^{n} \left[ (a_i - a_{i+1})^2 + (b_i - b_{i+1})^2 \right] \\
(a_{n+1} = a_1 \text{ and } b_{n+1} = b_1 \text{ for } i = 1, 2, 3)
$$


## 2023 — 2

**Record:** `kor_2023_5952ef`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2023_5952ef.json.gz).

Let $\mathbb{R}^+$ be the set of positive real numbers. Let $f : \mathbb{R}^+ \to \mathbb{R}^+$ be a function satisfying the following.
For each positive real number $x$, there exists $y \in \mathbb{R}$ such that
$$
(x + f(y))(y + f(x)) \leq 4,
$$
and the number of such $y$'s is finite.
Prove that $f(x) > f(y)$ for every pair of positive real numbers $x$ and $y$ with $x < y$.


## 2024 — Problem 5

**Record:** `kor_2024_6e49fd`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2024_6e49fd.json.gz).

Let $n (\ge 4)$ be a positive integer, and $a_1, a_2, \dots, a_n$ be distinct positive integers less than or equal to $n$. Determine the maximum value of
$$
\sum_{i=1}^{n} |a_i - a_{i+1} + a_{i+2} - a_{i+3}|.
$$
($a_{n+i} = a_i$ for $i = 1, 2, 3$)


## 2024 — Problem 3

**Record:** `kor_2024_7a75e8`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2024_7a75e8.json.gz).

Find the smallest positive real number $p (\le 1)$ such that the inequality
$$
\sum_{i=1}^{2024} x_i (y_{2025-i} - y_{2024-i}) \ge 1 - p
$$
holds for all real numbers $0 \le x_1 \le x_2 \le \dots \le x_{2024} \le 1$ and $0 = y_0 \le y_1 \le y_2 \le \dots \le y_{2024} \le 1$ satisfying
$$
\sum_{i=1}^{2024} x_i = \sum_{i=1}^{2024} y_i = 2024p.
$$



# RMM source statements

## 2013 — 5.

**Record:** `usa_2013_de41b7`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2013_de41b7.json.gz).

Given an integer $k \ge 2$, set $a_1 = 1$ and, for every integer $n \ge 2$, let $a_n$ be the smallest $x > a_{n-1}$ such that

$$
x = 1 + \sum_{i=1}^{n-1} \lfloor \sqrt[k]{\frac{x}{a_i}} \rfloor.
$$

Prove that every prime occurs in the sequence $a_1, a_2, \dots$.


## 2015 — Problem 3.

**Record:** `rmm_2015_d7c58c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2015_d7c58c.json.gz).

A finite list of rational numbers is written on a blackboard. In an operation, we choose any two numbers $a, b$, erase them, and write down one of the numbers
$$
a+b,\ a-b,\ b-a,\ a \times b,\ a / b\ (\text{ if } b \neq 0),\ b / a\ (\text{ if } a \neq 0).
$$
Prove that, for every integer $n>100$, there are only finitely many integers $k \geq 0$, such that, starting from the list
$$
k+1,\ k+2,\ \ldots,\ k+n
$$
it is possible to obtain, after $n-1$ operations, the value $n!$.


## 2016 — Problem 4.

**Record:** `rou_2016_e666aa`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2016_e666aa.json.gz).

Let $x$ and $y$ be positive real numbers such that $x + y^{2016} \ge 1$. Prove that $x^{2016} + y > 1 - 1/100$.


## 2017 — Problem 4

**Record:** `rou_2017_6a40eb`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2017_6a40eb.json.gz).

In the Cartesian plane, let $\gamma_1$ and $\gamma_2$ be the graphs of the quadratic functions $f_1(x) = p_1x^2+q_1x+r_1$ and $f_2(x) = p_2x^2+q_2x+r_2$, where $p_1 > 0 > p_2$. The graphs $\gamma_1$ and $\gamma_2$ cross at distinct points $A$ and $B$. The four tangents to $\gamma_1$ and $\gamma_2$ at $A$ and $B$ form a convex quadrangle which has an inscribed circle. Prove that the graphs $\gamma_1$ and $\gamma_2$ have the same axis of symmetry.


## 2017 — Problem 2

**Record:** `rou_2017_ecd799`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2017_ecd799.json.gz).

Determine all positive integers $n$ satisfying the following condition: for every monic polynomial $P$ of degree at most $n$ with integer coefficients, there exists a positive integer $k \le n$, and $k+1$ distinct integers $x_1, x_2, \dots, x_{k+1}$ such that $P(x_1) + P(x_2) + \dots + P(x_k) = P(x_{k+1})$.

*Note.* A polynomial is *monic* if the coefficient of the highest power is one.


## 2019 — Problem 6

**Record:** `rmm_2019_39ca85`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2019_39ca85.json.gz).

Find all pairs of integers $(c, d)$, both greater than $1$, such that the following holds:
For any monic polynomial $Q$ of degree $d$ with integer coefficients and for any prime $p > c(2c+1)$, there exists a set $S$ of at most $\left(\frac{2c-1}{2c+1}\right)p$ integers, such that
$$
\bigcup_{s \in S} \{s, Q(s), Q(Q(s)), Q(Q(Q(s))), \ldots\}
$$
is a complete residue system modulo $p$ (i.e., intersects with every residue class modulo $p$).


## 2021 — Problem 4

**Record:** `rmm_2021_03b2ae`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2021_03b2ae.json.gz).

Consider an integer $n \geq 2$ and write the numbers $1,2, \ldots, n$ down on a board. A move consists in erasing any two numbers $a$ and $b$, and, for each $c$ in $\{a+b,|a-b|\}$, writing $c$ down on the board, unless $c$ is already there; if $c$ is already on the board, do nothing. For all integers $n \geq 2$, determine whether it is possible to be left with exactly two numbers on the board after a finite number of moves.


## 2021 — Problem 3

**Record:** `rmm_2021_7ba909`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2021_7ba909.json.gz).

A number of 17 workers stand in a row. Every contiguous group of at least 2 workers is a brigade. The chief wants to assign each brigade a leader (which is a member of the brigade) so that each worker's number of assignments is divisible by 4. Prove that the number of such ways to assign the leaders is divisible by 17.


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



# USAMO source statements

## 2006 — 4

**Record:** `usa_2006_0a860b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2006_0a860b.json.gz).

Find all positive integers $n$ such that there are $k \ge 2$ positive rational numbers $a_1, a_2, \dots, a_k$ satisfying $a_1 + a_2 + \dots + a_k = a_1 \cdot a_2 \dots a_k = n$.


## 2006 — 3

**Record:** `usa_2006_2edd72`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2006_2edd72.json.gz).

For integral $m$, let $p(m)$ be the greatest prime divisor of $m$. By convention, we set $p(\pm 1) = 1$ and $p(0) = \infty$. Find all polynomials $f$ with integer coefficients such that the sequence $\{p(f(n^2)) - 2n\}_{n \ge 0}$ is bounded above. (In particular, this requires $f(n^2) \ne 0$ for $n \ge 0$.)


## 2006 — 2

**Record:** `usa_2006_9454b3`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2006_9454b3.json.gz).

For a given positive integer $k$ find, in terms of $k$, the minimum value of $N$ for which there is a set of $2k+1$ distinct positive integers that has sum greater than $N$ but every subset of size $k$ has sum at most $N/2$.


## 2007 — 1

**Record:** `usa_2007_83a6e7`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2007_83a6e7.json.gz).

Let $n$ be a positive integer. Define a sequence by setting $a_1 = n$ and, for each $k > 1$, letting $a_k$ be the unique integer in the range $0 \le a_k \le k - 1$ for which $a_1 + a_2 + \cdots + a_k$ is divisible by $k$. For instance, when $n = 9$ the obtained sequence is $9, 1, 2, 0, 3, 3, 3, \dots$. Prove that for any $n$ the sequence $a_1, a_2, a_3, \dots$ eventually becomes constant.


## 2007 — 5

**Record:** `usa_2007_b62228`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2007_b62228.json.gz).

Prove that for every nonnegative integer $n$, the number $7^{7^n} + 1$ is the product of at least $2n+3$ (not necessarily distinct) primes.


## 2008 — 6

**Record:** `usa_2008_8434eb`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2008_8434eb.json.gz).

At a certain mathematical conference, every pair of mathematicians are either friends or strangers. At mealtime, every participant eats in one of two large dining rooms. Each mathematician insists upon eating in a room which contains an even number of his or her friends. Prove that the number of ways that the mathematicians may be split between the two rooms is a power of two (i.e., is of the form $2^k$ for some positive integer $k$).
(This problem was suggested by Sam Vandervelde.)


## 2008 — 1

**Record:** `usa_2008_91e70b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2008_91e70b.json.gz).

Prove that for each positive integer $n$, there are pairwise relatively prime integers $k_0, k_1, \dots, k_n$, all strictly greater than 1, such that $k_0 k_1 \cdots k_n - 1$ is the product of two consecutive integers.


## 2010 — 5

**Record:** `usa_2010_73d4a3`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2010_73d4a3.json.gz).

Let $q = \frac{3p-5}{2}$ where $p$ is an odd prime, and let
$$
S_q = \frac{1}{2 \cdot 3 \cdot 4} + \frac{1}{5 \cdot 6 \cdot 7} + \dots + \frac{1}{q(q+1)(q+2)}.
$$
Prove that if $\frac{1}{p} - 2S_q = \frac{m}{n}$ for integers $m$ and $n$, then $m-n$ is divisible by $p$.


## 2010 — 3

**Record:** `usa_2010_83c87b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2010_83c87b.json.gz).

The 2010 positive numbers $a_1, a_2, \dots, a_{2010}$ satisfy the inequality $a_i a_j \le i + j$ for all distinct indices $i, j$. Determine, with proof, the largest possible value of the product $a_1 a_2 \cdots a_{2010}$.


## 2012 — 6.

**Record:** `usa_2012_06c2de`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2012_06c2de.json.gz).

For integer $n \ge 2$, let $x_1, x_2, \dots, x_n$ be real numbers satisfying
$$
x_1 + x_2 + \dots + x_n = 0, \quad \text{and} \quad x_1^2 + x_2^2 + \dots + x_n^2 = 1.
$$
For each subset $A \subseteq \{1, 2, \dots, n\}$, define
$$
S_A = \sum_{i \in A} x_i.
$$
(If $A$ is the empty set, then $S_A = 0$.)
Prove that for any positive number $\lambda$, the number of sets $A$ satisfying $S_A \ge \lambda$ is at most $\frac{2^{n-3}}{\lambda^2}$.
For what choices of $x_1, x_2, \dots, x_n, \lambda$ does equality hold?


## 2012 — 1

**Record:** `usa_2012_25ac44`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2012_25ac44.json.gz).

Find all integers $n \ge 3$ such that among any $n$ positive real numbers $a_1, a_2, \ldots, a_n$ with
$$ \max(a_1, a_2, \ldots, a_n) \le n \cdot \min(a_1, a_2, \ldots, a_n), $$
there exist three that are the side lengths of an acute triangle.


## 2013 — 3.

**Record:** `usa_2013_a35b16`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2013_a35b16.json.gz).

Let $n$ be a positive integer. There are $\frac{n(n+1)}{2}$ marks, each with a black side and a white side, arranged into an equilateral triangle, with the biggest row containing $n$ marks. Initially, each mark has the black side up. An *operation* is to choose a line parallel to one of the sides of the triangle, and flipping all the marks on that line. A configuration is called *admissible* if it can be obtained from the initial configuration by performing a finite number of operations. For each admissible configuration $C$, let $f(C)$ denote the smallest number of operations required to obtain $C$ from the initial configuration. Find the maximum value of $f(C)$, where $C$ varies over all admissible configurations.
(This problem was suggested by Warut Suksompong.)


## 2014 — 6.

**Record:** `usa_2014_952bd1`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2014_952bd1.json.gz).

Prove that there is a constant $c > 0$ with the following property: If $a, b, n$ are positive integers such that $\gcd(a + i, b + j) > 1$ for all $i, j \in \{0, 1, \dots, n\}$, then
$$
\min\{a, b\} > c^n \cdot n^{\frac{n}{2}}.
$$


## 2014 — 1.

**Record:** `usa_2014_e6bd00`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2014_e6bd00.json.gz).

Let $a$, $b$, $c$, $d$ be real numbers such that $b - d \ge 5$ and all zeros $x_1$, $x_2$, $x_3$, and $x_4$ of the polynomial $P(x) = x^4 + a x^3 + b x^2 + c x + d$ are real. Find the smallest value the product $(x_1^2 + 1)(x_2^2 + 1)(x_3^2 + 1)(x_4^2 + 1)$ can take.


## 2014 — 3.

**Record:** `usa_2014_eef9b1`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2014_eef9b1.json.gz).

Prove that there exists an infinite set of points
$$
\dots, P_{-3}, P_{-2}, P_{-1}, P_0, P_1, P_2, P_3, \dots
$$
in the plane with the following property: For any three distinct integers $a, b$ and $c$, points $P_a, P_b$ and $P_c$ are collinear if and only if $a + b + c = 2014$.


## 2025 — USAMO 1

**Record:** `usa_2025_65d3dd`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_65d3dd.json.gz).

Let $k$ and $d$ be positive integers. Prove that there exists a positive integer $N$ such that for every odd integer $n > N$, the digits in the base-$2n$ representation of $n^k$ are all greater than $d$.


## 2025 — USAMO 2

**Record:** `usa_2025_7a0fcb`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_7a0fcb.json.gz).

Let $n$ and $k$ be positive integers with $k < n$. Let $P(x)$ be a polynomial of degree $n$ with real coefficients, nonzero constant term, and no repeated roots. Suppose that for any real numbers $a_0, a_1, \dots, a_k$ such that the polynomial $a_kx^k + \dots + a_1x + a_0$ divides $P(x)$, the product $a_0a_1\dots a_k$ is zero. Prove that $P(x)$ has a nonreal root.


## 2025 — 5

**Record:** `usa_2025_e0957e`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_e0957e.json.gz).

Determine, with proof, all positive integers $k$ such that
$$
\frac{1}{n+1} \sum_{i=0}^{n} \binom{n}{i}^{k}
$$
is an integer for every positive integer $n$.



# VMO source statements

## 2001 — 4

**Record:** `vnm_2001_3e4085`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2001_3e4085.json.gz).

Let $x$, $y$, $z$ be positive real numbers satisfying the following conditions:
$$
\frac{1}{\sqrt{2}} \leq z < \frac{1}{2} \min \{x\sqrt{2},\ y\sqrt{3}\}, \\
 x + z\sqrt{3} \geq \sqrt{6}, \\
 y\sqrt{3} + z\sqrt{10} \geq 2\sqrt{5}.
$$
Find the greatest value of the expression:
$$
P(x, y, z) = \frac{1}{x^2} + \frac{2}{y^2} + \frac{3}{z^2}
$$


## 2001 — 5

**Record:** `vnm_2001_45a2d4`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2001_45a2d4.json.gz).

Consider the function $g(x) = \frac{2x}{1+x^2}$. Find all function $f(x)$ defined and continuous on the interval $(-1; 1)$ which satisfy the condition:
$$
(1 - x^2)f(g(x)) = (1 + x^2)^2 f(x)
$$
for every $x \in (-1; 1)$.


## 2001 — 6

**Record:** `vnm_2001_4665d8`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2001_4665d8.json.gz).

Let be given an integer $n \ge 1$. Consider a permutation $(a_1, a_2, ..., a_{2n})$ of the first $2n$ positive integers such that the numbers $|a_{i+1} - a_i|$ $(i = 1, 2, ..., 2n-1)$ are distinct each from others.
Prove that $a_1 - a_{2n} = n$ if and only if $1 \le a_{2k} \le n$ for every $k = 1, 2, ..., n$.


## 2001 — 3

**Record:** `vnm_2001_ec1af2`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2001_ec1af2.json.gz).

For every couple of real numbers $(a, b)$, consider the sequence of numbers $\{x_n\}$, $n = 0, 1, 2, \dots$, defined by:
$$
x_0 = a \quad \text{and} \quad x_{n+1} = x_n + b \sin x_n \quad \text{for every } n = 0, 1, 2, \dots
$$
Prove that:
1) for every real number $a$, the sequence $\{x_n\}$ corresponding to $(a, b)$ has a finite limit when $n$ tends to infinity. Find this limit.
2) for every number $b > 2$, there exists a real number $a$ such that the sequence $\{x_n\}$ corresponding to $(a, b)$ does not have a finite limit when $n$ tends to infinity.


## 2003 — 3

**Record:** `vnm_2003_16d22f`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2003_16d22f.json.gz).

Find all polynomials $P(x)$ with real coefficients, satisfying the relation
$$
(x^3 + 3x^2 + 3x + 2)P(x - 1) = (x^3 - 3x^2 + 3x - 2)P(x)
$$
for every real number $x$.


## 2003 — 10

**Record:** `vnm_2003_6ad236`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2003_6ad236.json.gz).

For each integer $n > 1$, denote by $s_n$ the number of permutations $(a_1, a_2, ..., a_n)$ of $n$ first positive integers such that each permutation satisfies the condition:
$$
1 \le |a_k - k| \le 2 \quad \text{for every } k = 1, 2, ..., n.
$$
Prove that: $1.75 \cdot s_{n-1} < s_n < 2 \cdot s_{n-1}$ for all integers $n > 6$.


## 2003 — 8

**Record:** `vnm_2003_98ada4`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2003_98ada4.json.gz).

Let $F$ be the set of all functions $f: \mathbb{R}^+ \to \mathbb{R}^+$ satisfying the condition
$f(3x) \geq f(f(2x)) + x$ for every real positive number $x$.
Find the greatest real number $\alpha$ such that for all $f \in F$, we have
$$
f(x) \geq \alpha x
$$
for every real positive number $x$.


## 2003 — 4

**Record:** `vnm_2003_c7a079`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2003_c7a079.json.gz).

Let be given two polynomials
$$
P(x) = 4x^3 - 2x^2 - 15x + 9
$$
and
$$ Q(x) = 12x^3 + 6x^2 - 7x + 1. $$
1/ Prove that each of these polynomials has three distinct real roots.
2/ Let $\alpha$ and $\beta$ be respectively the greatest roots of $P(x)$ and $Q(x)$. Prove that $\alpha^2 + 3\beta^2 = 4$.


## 2003 — 7

**Record:** `vnm_2003_e66438`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2003_e66438.json.gz).

Let be given a real number $\alpha \neq 0$. Consider the sequence of real numbers $\{x_n\}$, $n = 1, 2, 3, \dots$, defined by:
$$
x_1 = 0 \quad \text{and} \quad x_{n+1}(x_n + \alpha) = \alpha + 1 \quad \text{for every } n = 1, 2, 3, \dots
$$
1/ Find the general term of the sequence $\{x_n\}$.
2/ Prove that the sequence $\{x_n\}$ has a finite limit when $n \to +\infty$. Find this limit.


## 2005 — Problem 1.

**Record:** `vnm_2005_a1981f`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2005_a1981f.json.gz).

Find the least value and the greatest value of the expression
$$
P = x + y
$$
where $x, y$ are real numbers satisfying the condition
$$
x - 3\sqrt{x + 1} = 3\sqrt{y + 2} - y.
$$


## 2005 — Problem 4.

**Record:** `vnm_2005_fb9b22`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2005_fb9b22.json.gz).

Find all functions $f$ defined on $\mathbb{R}$, taking values in $\mathbb{R}$ so that
$$
f(f(x - y)) = f(x)f(y) - f(x) + f(y) - xy
$$
for all real numbers $x, y$.


## 2006 — Problem 4

**Record:** `vnm_2006_6a3ccf`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2006_6a3ccf.json.gz).

Consider the function
$$
f(x) = -x + \sqrt{(x + a)(x + b)}
$$
where $a$ and $b$ are two given distinct positive real numbers.
Prove that for every real number $s$ belonging to the interval $(0,1)$ there exists a unique real number $\alpha$ such that
$$
f(\alpha) = \left( \frac{a^s + b^s}{2} \right)^{\frac{1}{s}}
$$


## 2006 — Problem 1

**Record:** `vnm_2006_dbb88d`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2006_dbb88d.json.gz).

Solve the following system of equations
$$
\begin{cases}
\sqrt{x^2 - 2x + 6} \log_3 (6-y) = x \\
\sqrt{y^2 - 2y + 6} \log_3 (6-z) = y \\
\sqrt{z^2 - 2z + 6} \log_3 (6-x) = z.
\end{cases}
$$


## 2006 — Problem 5

**Record:** `vnm_2006_e20b07`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2006_e20b07.json.gz).

Find all polynomials $P(x)$ with real coefficients satisfying the condition
$$
P(x^2) + x(3P(x) + P(-x)) = (P(x))^2 + 2x^2
$$
for all real numbers $x$.


## 2007 — 5

**Record:** `vnm_2007_42542b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2007_42542b.json.gz).

Let $b$ be a positive real number. Find all functions $f: \mathbb{R} \to \mathbb{R}$ satisfying
$$
f(x+y) = f(x) \cdot 3^{b^y} + f(y)^{-1} + b^x (3^{b^y} + f(y)^{-1} - b^y) \quad \forall x, y \in \mathbb{R}.
$$


## 2007 — 1

**Record:** `vnm_2007_6e5b26`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2007_6e5b26.json.gz).

Solve the equation system
$$
\begin{cases} 1 - \frac{12}{y+3x} = \frac{2}{\sqrt{x}} \\ 1 + \frac{12}{y+3x} = \frac{6}{\sqrt{x}} \end{cases}
$$


## 2007 — 7

**Record:** `vnm_2007_d94bb0`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2007_d94bb0.json.gz).

Let $a > 2$ be a real number and $f_n(x) = a^{10} x^{n+10} + x^n + \dots + x + 1$ ($n = 1, 2, \dots$). Prove that for every positive integer $n$ the equation $f_n(x) = a$ has exactly a real root $x_n \in (0; +\infty)$. Prove that the sequence $(x_n)$ has a finite limit when $n \to +\infty$.


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


## 2009 — Problem 1

**Record:** `vnm_2009_84ddc1`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2009_84ddc1.json.gz).

Solve the following system of equations:
$$
\begin{cases}
\frac{1}{\sqrt{1+2x^2}} + \frac{1}{\sqrt{1+2y^2}} = \frac{2}{\sqrt{1+2xy}} \\
\sqrt{x(1-2x)} + \sqrt{y(1-2y)} = \frac{2}{9}
\end{cases}
$$


## 2009 — Problem 4

**Record:** `vnm_2009_d06acd`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2009_d06acd.json.gz).

Given real numbers $a$, $b$, $c$ satisfying the condition: for each positive integer $n$, $a^n + b^n + c^n$ is an integer. Show that there exist integers $p$, $q$, $r$ such that $a$, $b$, $c$ are 3 solutions to the equation $x^3 + px^2 + qx + r = 0$.


## 2009 — Problem 2

**Record:** `vnm_2009_f1d3f0`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2009_f1d3f0.json.gz).

A sequence of real numbers $(x_n)$ is given by
$$
x_1 = \frac{1}{2} \quad \text{and} \quad x_n = \frac{\sqrt{x_{n-1}^2 + 4x_{n-1}} + x_{n-1}}{2} \quad \text{for all } n \ge 2.
$$
For each non-negative integer $n$, let
$$
y_n = \sum_{i=1}^{n} \frac{1}{x_i^2}.
$$
Show that the sequence $(y_n)$ has a finite limit when $n \to \infty$. Find this limit.


## 2010 — 5

**Record:** `vnm_2010_2bc522`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2010_2bc522.json.gz).

Given a positive integer $n$. Given a square table of sizes $3 \times 3$. One uses $n$ colors to paint the squares of the table in such a way, that each square is painted by one color. Two ways of painting is considered to be similar if they can be obtained from each other by rotating the table around its center. How many non-similar ways of painting are there?


## 2010 — 1

**Record:** `vnm_2010_eaed62`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2010_eaed62.json.gz).

Solve the following system of equations:
$$
\begin{cases} x^4 - y^4 = 240 \\ x^3 - 2y^3 = 3(x^2 - 4y^2) - 4(x - 8y). \end{cases}
$$


## 2010 — 2

**Record:** `vnm_2010_fe3e68`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2010_fe3e68.json.gz).

The sequence of real numbers $(a_n)$ is defined by
$$
a_1 = 5 \quad \text{and} \quad a_n = \sqrt[n]{a_{n-1}^{n-1} + 2^{n-1} + 2 \cdot 3^{n-1}} \quad \text{for all } n \ge 2.
$$
Prove that the sequence $(a_n)$ is decreasing.


## 2011 — 5

**Record:** `vnm_2011_0893a4`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2011_0893a4.json.gz).

A sequence of integers $(a_n)$ determined by
$$
a_0 = 1,\ a_1 = -1 \quad \text{and} \quad a_n = 6a_{n-1} + 5a_{n-2} \quad \text{for all } n \ge 2.
$$
Show that $a_{2012} - 2010$ is divisible by $2011$.


## 2011 — 1

**Record:** `vnm_2011_0e3af4`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2011_0e3af4.json.gz).

Given a positive integer $n$. Show that for any positive real number $x$, we have the inequality:
$$
\frac{x^n (x^{n+1} + 1)}{x^n + 1} \le \left( \frac{x+1}{2} \right)^{2n+1}
$$
When does the equality take place?


## 2011 — 2

**Record:** `vnm_2011_231420`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2011_231420.json.gz).

Given a sequence of real numbers ($x_n$):
$$
x_1 = 1 \quad \text{and} \quad x_n = \frac{2n}{(n-1)^2} \sum_{i=1}^{n-1} x_i \quad \text{for all } n \ge 2.
$$
For each positive integer $n$, let $y_n = x_{n+1} - x_n$.
Show that the sequence ($y_n$) has finite limit as $n \to +\infty$.


## 2011 — 7

**Record:** `vnm_2011_90414d`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2011_90414d.json.gz).

Let $n$ be a positive integer. Show that the polynomial
$$
P(x, y) = x^n + x y + y^n
$$
can not be written in the form
$$
P(x, y) = G(x, y) \cdot H(x, y),
$$
where $G(x, y)$ and $H(x, y)$ are non-constant polynomials with real coefficients.


## 2012 — 6

**Record:** `vnm_2012_059cee`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_059cee.json.gz).

Let $a$, $b$ be two odd natural numbers. Suppose that $a$ is a divisor of $b^2 + 2$ and $b$ is a divisor of $a^2 + 2$. Prove that $a$ and $b$ belong to the sequence $(v_n)$ defined by
$$
v_1 = v_2 = 1 \quad \text{and} \quad v_n = 4v_{n-1} - v_{n-2} \quad \forall n \ge 3.
$$


## 2012 — 2

**Record:** `vnm_2012_07ba94`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_07ba94.json.gz).

Given two arithmetic progressions $(a_n)$, $(b_n)$ and an integer $m > 2$. Consider $m$ quadratics $P_k(x) = x^2 + a_k x + b_k$, $k = 1, 2, \dots, m$. Suppose that neither $P_1(x)$ nor $P_m(x)$ has a real root. Prove that none of the given quadratics contains a real root.


## 2012 — Problem 3.

**Record:** `vnm_2012_0e70a3`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_0e70a3.json.gz).

Let be given two positive real numbers $a_0$ and $a_1$. The sequence $(a_n)$ is defined by
$$
a_{n+2} = 1 + \frac{a_{n+1}}{a_n}, \quad n = 0,1,2,\ldots
$$
Prove that $|a_{2012} - 2| < 10^{-200}$.


## 2012 — Problem 1.

**Record:** `vnm_2012_5dec98`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_5dec98.json.gz).

The equation $x^3 + 2x - 1 = 0$ has only one real root $r$. Note that $0.4 < r < 0.5$.

a. Prove that $\sum_{k=0}^{\infty} r^{3k+1} = \frac{1}{2}$.

b. Suppose that $(a_k)$ be a strictly increasing sequence of positive integral numbers such that $\sum_{k=0}^{\infty} r^{a_k} = \frac{1}{2}$. Prove that $a_k = k+1$ for all $k = 0, 1, 2, \ldots$


## 2012 — 1

**Record:** `vnm_2012_626786`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_626786.json.gz).

Given a sequence of real numbers $(x_n)$
$$
x_1 = 3 \quad \text{and} \quad x_n = \frac{n+2}{3n}(x_{n-1} + 2), \quad \forall n \ge 2.
$$
Prove that the sequence has a finite limit as $n \to \infty$ and calculate this limit.


## 2012 — 7

**Record:** `vnm_2012_960dde`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_960dde.json.gz).

Find all functions $f: \mathbb{R} \to \mathbb{R}$ satisfying all of the following conditions:
1. $f$ is a bijective function.
2. $f$ is an increasing function.
3. $f(f(x)) = f(x) + 12x, \forall x \in \mathbb{R}$.


## 2012 — Problem 1.

**Record:** `vnm_2012_9808c9`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_9808c9.json.gz).

Let $a, b, c \ge 2$ be real numbers, satisfying the condition $a + b + c = \frac{1}{a} + \frac{1}{b} + \frac{1}{c} + 8$. Prove that we have the inequality
$$
3(ab + bc + ca) \le 81 \le (a + b + c)^2.
$$


## 2012 — Problem 5.

**Record:** `vnm_2012_99501a`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_99501a.json.gz).

Let $a, b, c$ be positive real numbers. It is known that the system of equations
$$
\begin{cases} a^2x + b^2y + c^2z = 1 \\ xy + yz + zx = 1 \end{cases} \quad \text{(where $a, b, c$ are parameters)}
$$
has only one solution $(x, y, z)$. Prove that $a, b, c$ are the sides of a certain triangle.


## 2012 — Problem 2.

**Record:** `vnm_2012_d89ec3`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_d89ec3.json.gz).

Let $a$, $b$ be two positive real numbers and $n$ be an integer greater than $1$. Prove that for all positive real number $x$ satisfying $x^n \leq a x + b$, we have
$$
x < n^{-1/2} \sqrt{a} + n^{1/2} \sqrt{b}.
$$


## 2012 — Problem 2.

**Record:** `vnm_2012_e9f5a2`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_e9f5a2.json.gz).

Let $a > 0$ and the sequence $(x_n)$ is defined by
$$ x_1 = a, $$
$$ x_{n+1} = x_n + \frac{\sqrt{x_n}}{n^2}, \forall n \ge 1. $$
Prove that $(x_n)$ has a finite limit when $n$ tends to infinity.


## 2013 — Problem 1.

**Record:** `vnm_2013_1b2564`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2013_1b2564.json.gz).

Let be given an integer $n \ge 4$ and $x_1, x_2, x_3, \dots, x_n$ be nonnegative real numbers.
a) Prove that we have inequality
$$
\left(\sum_{i=1}^{n} x_i\right)^2 \ge \min\left\{\frac{n}{3}, \frac{8}{3}\right\} \sum_{i=1}^{n} x_i (x_{i+1} + x_{i+2} + x_{i+3})
$$
where $x_{n+1} = x_1$, $x_{n+2} = x_2$, $x_{n+3} = x_3$.
b) When does the equality hold?


## 2013 — Problem 3.

**Record:** `vnm_2013_6fb2bd`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2013_6fb2bd.json.gz).

For each positive integer $n$, let $S_n = \{0,1,2,\ldots,2n+1\}$. Consider the function $f : (\mathbb{Z} \times S_n) \to [0;1]$ satisfying the following conditions:

i/ $f(x,0) = f(x,2n+1) = 0$ for all $x$ from integers.

ii/ $f(x-1,y)+f(x+1,y)+f(x,y-1)+f(x,y+1)=1$ for all $x,y \in \mathbb{Z}$ and $1 \le y \le 2n$.

Let $F$ be the set of all such functions.

1. Prove that $|F|$ is infinite.
2. For each function $f \in F$, let $v_f$ be the image set of $f$. Prove that $|v_f|$ is finite.
3. Find the maximum value of $|v_f|$ where $f \in F$.


## 2013 — Problem 5.

**Record:** `vnm_2013_986218`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2013_986218.json.gz).

The teacher has $2013$ candies of $11$ different types. She distributes the candies to her students such that no student obtains more than one candy of each type. She then asks each pair of students to write down on the board the number of candy types that they have in common. Let $M$ be the sum of written numbers.

a)
Find the minimum value of $M$.

b)
What happens if the teacher has only $9$ different types of candy?


## 2014 — 2

**Record:** `vnm_2014_025c24`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2014_025c24.json.gz).

Let $a_1, a_2, \dots, a_{14}$ be some positive real numbers. Prove that
$$
\frac{a_1}{a_2+a_3} + \frac{a_2}{a_3+a_4} + \dots + \frac{a_{14}}{a_1+a_2} \ge \frac{a_1}{a_{14}+a_1} + \frac{a_2}{a_1+a_2} + \dots + \frac{a_{14}}{a_{13}+a_{14}}.
$$
When does the equality occur?


## 2014 — 6

**Record:** `vnm_2014_0630eb`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2014_0630eb.json.gz).

Let $x$, $y$ and $z$ be positive real numbers. Find the maximum value of the following expression
$$
\frac{x^3 y^4 z^3}{(x^4 + y^4)(xy + z^2)^3} + \frac{y^3 z^4 x^3}{(y^4 + z^4)(yz + x^2)^3} + \frac{z^3 x^4 y^3}{(z^4 + x^4)(zx + y^2)^3}
$$


## 2014 — 1

**Record:** `vnm_2014_60c13b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2014_60c13b.json.gz).

Let $(a_n)$ be the sequence such that $a_1 = \frac{3}{2}$ and
$$
a_{n+1} = a_n - \frac{3n+2}{2n(n+1)(2n+1)},\ n \ge 1.
$$
Find the limit $\lim_{n \to +\infty} a_n$.


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


## 2014 — 1

**Record:** `vnm_2014_ec195b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2014_ec195b.json.gz).

Let $(x_n)$, $(y_n)$ be two positive sequences defined by $x_1 = 1$, $y_1 = \sqrt{3}$ and
$$
\begin{cases} x_{n+1}y_{n+1} - x_n = 0 \\ x_{n+1}^2 + y_n = 2 \end{cases}
$$
for all positive integers $n$. Prove that these sequences are convergent and find their limits.


## 2015 — 2

**Record:** `vnm_2015_855e2c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2015_855e2c.json.gz).

Let $a$, $b$ and $c$ be non-negative real numbers. Prove that
$$
3(a^2 + b^2 + c^2) \ge (a+b+c)(\sqrt{ab} + \sqrt{bc} + \sqrt{ca}) + (a-b)^2 + (b-c)^2 + (c-a)^2 \ge (a+b+c)^2.
$$


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


## 2016 — 2

**Record:** `vnm_2016_afd01e`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2016_afd01e.json.gz).

a) Let $(a_n)$ be a sequence defined by $a_n = \ln(2n^2 + 1) - \ln(n^2 + n + 1)$ for all positive integers $n$. Prove that there are finite values of $n$ such that $\{a_n\} < \frac{1}{2}$.

b) Let $(b_n)$ be a sequence defined by $b_n = \ln(2n^2 + 1) + \ln(n^2 + n + 1)$ for all positive integers $n$. Prove that there are infinite values of $n$ such that $\{b_n\} < \frac{1}{2016}$.


## 2016 — 1

**Record:** `vnm_2016_baa520`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2016_baa520.json.gz).

Solve the system of equations
$$
\begin{cases} 6x - y + z^2 = 3 \\ x^2 - y^2 - 2z = -1 \\ 6x^2 - 3y^2 - z - 2z^2 = 0 \end{cases} \quad (x, y, z \in \mathbb{R})
$$


## 2016 — 5

**Record:** `vnm_2016_d8c35c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2016_d8c35c.json.gz).

Find all real numbers $a$ such that there exists a function $f: \mathbb{R} \rightarrow \mathbb{R}$ satisfying the following conditions

i) $f(1) = 2016$;
ii) $f(x + y + f(y)) = f(x) + ay$ for all real numbers $x, y$.


## 2018 — 4

**Record:** `vnm_2018_949f1a`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2018_949f1a.json.gz).

On the Cartesian plane, let $C$ be the graph of the function $y = \sqrt[3]{x^2}$. A line $d$ varies on the plane such that $d$ always cuts $C$ at three distinct points with $x$-coordinates $x_1, x_2$ and $x_3$.

a. Prove that the following value is a constant:
$$
\sqrt[3]{\frac{x_1 x_2}{x_3^2}} + \sqrt[3]{\frac{x_2 x_3}{x_1^2}} + \sqrt[3]{\frac{x_3 x_1}{x_2^2}}
$$

b. Show that:
$$
\sqrt[3]{\frac{x_1^2}{x_2 x_3}} + \sqrt[3]{\frac{x_2^2}{x_3 x_1}} + \sqrt[3]{\frac{x_3^2}{x_1 x_2}} < -\frac{15}{4}
$$


## 2018 — 3

**Record:** `vnm_2018_b1f4be`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2018_b1f4be.json.gz).

An investor has two rectangular lands, each of size $120 \times 100$.

a. On the first land, she wants to build a house with a rectangular base of size $25 \times 35$ and nine circular flower pots with diameter $5$ outside the house. Prove that for all positions of the flower pots, the remaining land is still sufficient to build the desired house.

b. On the second land, she wants to construct a polygonal fish pond such that the distance from an arbitrary point on the land, outside the pond, to the nearest pond edge is not over $5$. Prove that the perimeter of the pond is not smaller than $440 - 20\sqrt{2}$.


## 2018 — Problem 3

**Record:** `vnm_2018_da4108`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2018_da4108.json.gz).

A farmer has 2 rectangle lands of size $120 \text{ m} \times 100 \text{ m}$.

a. On the first land, there are 9 circle gardens of diameter $5 \text{ m}$. Prove that regardless to the position of gardens, he always can builds a rectangle garden of size $25 \text{ m} \times 35 \text{ m}$.

b. On the second land, he builds a convex polygon lake such that the shortest distance from any point on the boundary of the land to the lake is at most $5$ m. Prove that the perimeter of the lake is at least $440 - 20\sqrt{2}$ m.


## 2019 — 7

**Record:** `vnm_2019_e93538`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2019_e93538.json.gz).

There are several identical caro papers of size $5 \times 5$. Someone uses $n$ colors to fill in each paper such that two cells at the same position on two sides share the same color. Two papers are considered congruent if they can be stacked together in such a way that the pairs of squares at the same position have the same color. Prove that, by the definition of congruence, one can obtain at most
$$
\frac{1}{8}(n^{25} + 4n^{15} + n^{13} + 2n^{7})
$$
distinct colored caro papers.


## 2021 — 6

**Record:** `vnm_2021_384922`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2021_384922.json.gz).

A student divides $30$ marbles into $5$ boxes labelled $1, 2, 3, 4, 5$ (there may be a box without marble).

a. How many ways are there to divide marbles into boxes (two ways are different if there is a box with different number of marbles)?

b. After dividing, this student paints those marbles by a number of colors (each marble have one color, one color can be painted for many marbles), such that there does not exist $2$ marbles in the same box, having a mutual color and from any $2$ boxes, it is impossible to choose $8$ marbles painted in $4$ colors. Prove that for every division, the student must use at least $10$ colors to paint the marbles.

c. Find a division so that the student can use exactly $10$ colors to paint the marbles that satisfies the conditions in question b).


## 2021 — 1

**Record:** `vnm_2021_6a7ac6`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2021_6a7ac6.json.gz).

Consider the real sequence $(x_n)$ such that $x_1 \in (0, \frac{1}{2})$ and
$$
x_{n+1} = 3x_n^2 - 2n x_n^3, \quad \forall n \ge 1.
$$

a) Prove that $\lim_{n \to \infty} x_n = 0$.

b) For each $n \ge 1$, let $y_n = x_1 + 2x_2 + \dots + n x_n$. Prove that $(y_n)$ converges.


## 2021 — 5

**Record:** `vnm_2021_7572d1`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2021_7572d1.json.gz).

Consider the polynomial $P(x) = a_{21}x^{21} + a_{20}x^{20} + \cdots + a_1x + a_0$ with coefficients that are in the interval $[1011, 2021]$. Given that $P(x)$ has an integer root and there exists a positive real number $c$ such that $|a_{k+2} - a_k| \le c$ for all $k \in \{0, 1, \dots, 19\}$.

a) Prove that $P(x)$ has a unique integer root.

b) Prove that $\sum_{k=0}^{10} (a_{2k+1} - a_{2k})^2 \le 440c^2$.


## 2021 — 2

**Record:** `vnm_2021_a8fb9e`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2021_a8fb9e.json.gz).

Find all functions $f: \mathbb{R} \to \mathbb{R}$ such that
$$
f(x)f(y) = f(xy - 1) + x f(y) + y f(x), \quad \forall x, y \in \mathbb{R}.
$$


## 2022 — 5

**Record:** `vnm_2022_050178`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2022_050178.json.gz).

Consider 2 non-constant polynomials $P(x), Q(x)$, with non-negative coefficients. The coefficients of $P(x)$ is not larger than $2021$ and $Q(x)$ has at least one coefficient larger than $2021$. Assume that $P(2022) = Q(2022)$ and $P(x), Q(x)$ has a common rational root $\frac{p}{q} \neq 0$ for some $p, q \in \mathbb{Z}$, $(\gcd(p, q) = 1)$. Prove that
$$
|p| + n|q| \leq Q(n) - P(n), \forall n = 1, 2, \dots, 2021.
$$


## 2022 — 2

**Record:** `vnm_2022_22ba21`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2022_22ba21.json.gz).

Find all functions $f: \mathbb{R}^+ \to \mathbb{R}^+$ such that
$$
f\left(\frac{f(x)}{x} + y\right) = 1 + f(y), \forall x, y > 0.
$$


## 2022 — 1

**Record:** `vnm_2022_f42fa4`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2022_f42fa4.json.gz).

Let $a$ be a non-negative real number and a sequence $(u_n)$ defined as
$$
u_1 = 6, u_{n+1} = \frac{2n + a}{n} + \sqrt{\frac{n+a}{n}}u_n + 4$$
for all positive integers $n$.
a) For $a = 0$, prove that $(u_n)$ has a finite limit and find its value.
b) For $a \ge 0$, prove that $(u_n)$ has a finite limit.


## 2023 — 3

**Record:** `vnm_2023_3e5eba`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2023_3e5eba.json.gz).

Find the maximum value of the positive real number $k$ such that the inequality
$$
\frac{1}{kab + c^2} + \frac{1}{kbc + a^2} + \frac{1}{kca + b^2} \ge \frac{k+3}{a^2 + b^2 + c^2}
$$
holds for all positive real numbers $a, b, c$ such that $a^2 + b^2 + c^2 = 2(ab + bc + ca)$.


## 2023 — 6

**Record:** `vnm_2023_423ad5`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2023_423ad5.json.gz).

There are $n \ge 2$ classes organized $m \ge 1$ learning groups for students. Every class has students participating in at least one group. Every group has exactly $a$ classes that the students in this group participate in. For any two groups, there are no more than $b$ classes with students participating in both groups simultaneously.

a) Find $m$ when $n = 8, a = 4, b = 1$.

b) Prove that $n \ge 20$ when $m = 6, a = 10, b = 4$.

c) Find the minimum value of $n$ when $m = 20, a = 4, b = 1$.


## 2023 — 7

**Record:** `vnm_2023_938036`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2023_938036.json.gz).

Let $ABC$ be a scalene triangle with orthocenter $H$ and circumcenter $O$. Incircle $(I)$ of the $ABC$ is tangent to the sides $BC, CA, AB$ at $M, N, P$ respectively. Denote $\Omega_A$ to be the circle passing through point $A$, external tangent to $(I)$ at $A'$ and cut again $AB, AC$ at $A_b, A_c$ respectively. The circles $\Omega_B, \Omega_C$ and points $B', B_a, B_c, C', C_a, C_b$ are defined similarly.

a) Prove that $B_cC_b + C_aA_c + A_bB_a \ge NP + PM + MN$.

b) Suppose $A', B', C'$ lie on $AM, BN, CP$ respectively. Denote $K$ as the circumcenter of the triangle formed by lines $A_bA_c, B_cB_a, C_aC_b$. Prove $OH$ is parallel to $IK$.


## 2023 — 5

**Record:** `vnm_2023_9ad037`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2023_9ad037.json.gz).

Consider functions $f: \mathbb{R} \to \mathbb{R}$ and $g: \mathbb{R} \to \mathbb{R}$ satisfying $f(0) = 2022$ and
$$
f(x + g(y)) = x f(y) + (2023 - y) f(x) + g(x), \quad \forall x, y \in \mathbb{R}.
$$
a) Prove that $f$ is surjective and $g$ is injective.
b) Find all functions $f, g$ satisfying the given conditions.


## 2023 — 2

**Record:** `vnm_2023_a8510a`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2023_a8510a.json.gz).

Let $a, b, c, \alpha, \beta$ be the given integers and the sequence $(u_n)$ is defined by $u_1 = \alpha, u_2 = \beta, u_{n+2} = a u_{n+1} + b u_n + c$ for all $n \ge 1$.

a) Prove that if $a = 3, b = -2, c = -1$ then there are infinitely many pairs of integers $(\alpha; \beta)$ so that $u_{2023} = 2^{2022}$.

b) Prove that there exists a positive integer $n_0$ such that exactly one of the following two statements is true:

i) There are infinitely many positive integers $m$, such that $u_{n_0}u_{n_0+1}\dots u_{n_0+m}$ is divisible by $7^{2023}$ or $17^{2023}$;

ii) There are infinitely many positive integers $k$ so that $u_{n_0}u_{n_0+1}\dots u_{n_0+k} - 1$ is divisible by 2023.


## 2024 — 5

**Record:** `vnm_2024_b86eb8`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2024_b86eb8.json.gz).

For each polynomial $P(x)$, define
$$
P_1(x) = P(x), \forall x \in \mathbb{R},
$$
$$
P_2(x) = P(P_1(x)), \forall x \in \mathbb{R},
$$
$$
P_{2024}(x) = P(P_{2023}(x)), \forall x \in \mathbb{R}.
$$
Let $a > 2$ be a real number. Is there a polynomial $P$ with real coefficients such that for all $t \in (-a, a)$, the equation $P_{2024}(x) = t$ has $2^{2024}$ distinct real roots?


