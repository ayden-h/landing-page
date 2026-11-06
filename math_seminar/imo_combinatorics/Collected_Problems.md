---
title: "Collected Olympiad Combinatorics Problems"
subtitle: "770 source statements • partial research corpus"
author: "Compiled for haohao; original sources credited in the ledger"
date: "5 November 2026"
lang: en-US
---

# Scope and attribution {.unnumbered}

This volume prints the 770 source statements included in the companion research package. It is **not a complete historical collection** and its source classifications and transcriptions have not all been independently verified. Mixed-domain candidates are included when the source tags indicate a combinatorial component. Problem numbers, years and contest labels can contain extraction errors.

These statements are reproduced from MathNet under its CC BY 4.0 fallback for records with no explicit original rights assertion in the recovered metadata. Records with an explicit rights assertion, detected external statement figures, or known out-of-scope classification are excluded here and retained as pointers in the complete catalog. This filtering does not establish that every remaining transcription is error-free or complete.

Source: [MathNet](https://mathnet.mit.edu/), by Shaden Alshammari, Kevin Wen, Abrar Zainal, Mark Hamilton, Navid Safaei, Sultan Albarakati, William T. Freeman and Antonio Torralba, ICLR 2026. [Dataset and rights statement](https://huggingface.co/datasets/ShadenA/MathNet). [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Original contest/source authors and booklet metadata are retained in the package's source ledger and individual problem files. Each entry links to its recovered source record.

Changes from the retrieved text: document grouping and typesetting; normalized contest labels where a discrepancy could be resolved. A few nonstandard TeX display commands may be normalized without changing the intended mathematics. Source prose is otherwise retained. Some entries are in their source language.

The separate **Worked Solutions** volume contains 26 reviewed, rewritten proofs. Files in `source_solutions/` contain additional supplied solutions with an explicit unreviewed label. Do not assume that an imported source proof has the same status as a reviewed case study.

Read **Coverage_Report.md** for exact counts, gaps, known defects and the distinction between competitions, shortlists, selection rounds and pipeline supplements.


# APMO


## 1989 — 4

**Record:** `apm_1989_ab9780`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1989_ab9780.json.gz).

Let $S$ be a set consisting of $m$ pairs $(a, b)$ of positive integers with the property that $1 \leq a < b \leq n$. Show that there are at least
$$
4m \frac{\left(m-\frac{n^{2}}{4}\right)}{3n}
$$
triples $(a, b, c)$ such that $(a, b), (a, c)$, and $(b, c)$ belong to $S$.



## 1990 — 4

**Record:** `apm_1990_c222d1`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1990_c222d1.json.gz).

A set of $1990$ persons is divided into non-intersecting subsets in such a way that
(a) no one in a subset knows all the others in the subset;
(b) among any three persons in a subset, there are always at least two who do not know each other; and
(c) for any two persons in a subset who do not know each other, there is exactly one person in the same subset knowing both of them.
(i) Prove that within each subset, every person has the same number of acquaintances.
(ii) Determine the maximum possible number of subsets.
Note: it is understood that if a person $A$ knows person $B$, then person $B$ will know person $A$; an acquaintance is someone who is known. Every person is assumed to know one's self.



## 1990 — 2

**Record:** `apm_1990_e66529`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1990_e66529.json.gz).

Let $a_{1}, a_{2}, \ldots, a_{n}$ be positive real numbers, and let $S_{k}$ be the sum of products of $a_{1}, a_{2}, \ldots, a_{n}$ taken $k$ at a time.
Show that
$$
S_{k} S_{n-k} \geq \binom{ n}{k}^{2} a_{1} a_{2} \ldots a_{n}, \quad \text{ for } \quad k=1,2, \ldots, n-1
$$



## 1991 — 2

**Record:** `apm_1991_b65647`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1991_b65647.json.gz).

Suppose there are 997 points given in a plane. If every two points are joined by a line segment with its midpoint coloured in red, show that there are at least 1991 red points in the plane. Can you find a special case with exactly 1991 red points?



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



## 1998 — 1

**Record:** `apm_1998_69a314`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1998_69a314.json.gz).

Let $F$ be the set of all $n$-tuples $(A_{1}, A_{2}, \ldots, A_{n})$ where each $A_{i}$, $i=1,2, \ldots, n$ is a subset of $\{1,2, \ldots, 1998\}$. Let $|A|$ denote the number of elements of the set $A$. Find the number
$$
\sum_{(A_{1}, A_{2}, \ldots, A_{n})} |A_{1} \cup A_{2} \cup \ldots \cup A_{n}|.
$$



## 1999 — 5

**Record:** `apm_1999_563b73`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_1999_563b73.json.gz).

Let $S$ be a set of $2n+1$ points in the plane such that no three are collinear and no four concyclic. A circle will be called good if it has 3 points of $S$ on its circumference, $n-1$ points in its interior and $n-1$ in its exterior. Prove that the number of good circles has the same parity as $n$.



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



## 2003 — 5

**Record:** `apm_2003_d3281e`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2003_d3281e.json.gz).

Given two positive integers $m$ and $n$, find the smallest positive integer $k$ such that among any $k$ people, either there are $2m$ of them who form $m$ pairs of mutually acquainted people or there are $2n$ of them forming $n$ pairs of mutually unacquainted people.



## 2004 — 1

**Record:** `apm_2004_1843da`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2004_1843da.json.gz).

Determine all finite nonempty sets $S$ of positive integers satisfying
$$
\frac{i+j}{(i, j)} \quad \text{is an element of } S \text{ for all } i, j \text{ in } S,
$$
where $(i, j)$ is the greatest common divisor of $i$ and $j$.



## 2004 — 3

**Record:** `apm_2004_f5148e`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2004_f5148e.json.gz).

Let a set $S$ of 2004 points in the plane be given, no three of which are collinear. Let $\mathcal{L}$ denote the set of all lines (extended indefinitely in both directions) determined by pairs of points from the set. Show that it is possible to colour the points of $S$ with at most two colours, such that for any points $p, q$ of $S$, the number of lines in $\mathcal{L}$ which separate $p$ from $q$ is odd if and only if $p$ and $q$ have the same colour.

Note: A line $\ell$ separates two points $p$ and $q$ if $p$ and $q$ lie on opposite sides of $\ell$ with neither point on $\ell$.



## 2005 — Problem 4

**Record:** `apm_2005_be8587`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2005_be8587.json.gz).

In a small town, there are $n \times n$ houses indexed by $(i, j)$ for $1 \leq i, j \leq n$ with $(1,1)$ being the house at the top left corner, where $i$ and $j$ are the row and column indices, respectively. At time $0$, a fire breaks out at the house indexed by $(1, c)$, where $c \leq \frac{n}{2}$. During each subsequent time interval $[t, t+1]$, the fire fighters defend a house which is not yet on fire while the fire spreads to all undefended neighbors of each house which was on fire at time $t$. Once a house is defended, it remains so all the time. The process ends when the fire can no longer spread. At most how many houses can be saved by the fire fighters? A house indexed by $(i, j)$ is a neighbor of a house indexed by $(k, \ell)$ if $|i-k|+|j-\ell|=1$.



## 2007 — Problem 5

**Record:** `apm_2007_1337e6`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2007_1337e6.json.gz).

A regular ($5 \times 5$)-array of lights is defective, so that toggling the switch for one light causes each adjacent light in the same row and in the same column as well as the light itself to change state, from on to off, or from off to on. Initially all the lights are switched off. After a certain number of toggles, exactly one light is switched on. Find all the possible positions of this light.



## 2007 — Problem 3

**Record:** `apm_2007_7a497c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2007_7a497c.json.gz).

Consider $n$ disks $C_{1}, C_{2}, \ldots, C_{n}$ in a plane such that for each $1 \leq i < n$, the center of $C_{i}$ is on the circumference of $C_{i+1}$, and the center of $C_{n}$ is on the circumference of $C_{1}$. Define the score of such an arrangement of $n$ disks to be the number of pairs $(i, j)$ for which $C_{i}$ properly contains $C_{j}$. Determine the maximum possible score.



## 2007 — Problem 1

**Record:** `apm_2007_ca2bc8`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2007_ca2bc8.json.gz).

Let $S$ be a set of 9 distinct integers all of whose prime factors are at most $3$. Prove that $S$ contains 3 distinct integers such that their product is a perfect cube.



## 2008 — Problem 2

**Record:** `apm_2008_44c90f`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2008_44c90f.json.gz).

Students in a class form groups each of which contains exactly three members such that any two distinct groups have at most one member in common. Prove that, when the class size is $46$, there is a set of $10$ students in which no group is properly contained.



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



## 2010 — 3

**Record:** `apm_2010_bde43c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2010_bde43c.json.gz).

Let $n$ be a positive integer. $n$ people take part in a certain party. For any pair of the participants, either the two are acquainted with each other or they are not. What is the maximum possible number of the pairs for which the two are not acquainted but have a common acquaintance among the participants?



## 2016 — 4

**Record:** `apm_2016_6dfebe`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2016_6dfebe.json.gz).

The country Dreamland consists of 2016 cities. The airline Starways wants to establish some one-way flights between pairs of cities in such a way that each city has exactly one flight out of it. Find the smallest positive integer $k$ such that no matter how Starways establishes its flights, the cities can always be partitioned into $k$ groups so that from any city it is not possible to reach another city in the same group by using at most 28 flights.



## 2018 — 3

**Record:** `mkd_2018_77a86a`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2018_77a86a.json.gz).

A collection of $n$ squares on the plane is called tri-connected if the following criteria are satisfied:
(i) All the squares are congruent
(ii) If two squares have a point $P$ in common, then $P$ is a vertex of each of the squares.
(iii) Each square touches exactly three other squares.
How many positive integers $n$ are there with $2018 \le n \le 3018$ such that there exists a collection of $n$ squares that is tri-connected?



## 2019 — 4

**Record:** `apm_2019_3a3563`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2019_3a3563.json.gz).

Consider a $2018 \times 2019$ board with integers in each unit square. Two unit squares are said to be neighbours if they share a common edge. In each turn, you choose some unit squares. Then for each chosen unit square the average of all its neighbours is calculated. Finally, after these calculations are done, the number in each chosen unit square is replaced by the corresponding average. Is it always possible to make the numbers in all squares become the same after finitely many turns?



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



## 2020 — 3

**Record:** `apm_2020_f3d3c1`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2020_f3d3c1.json.gz).

Determine all positive integers $k$ for which there exist a positive integer $m$ and a set $S$ of positive integers such that any integer $n>m$ can be written as a sum of distinct elements of $S$ in exactly $k$ ways.



## 2022 — 4

**Record:** `apm_2022_04f0c2`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2022_04f0c2.json.gz).

Let $n$ and $k$ be positive integers. Cathy is playing the following game. There are $n$ marbles and $k$ boxes, with the marbles labelled $1$ to $n$. Initially, all marbles are placed inside one box. Each turn, Cathy chooses a box and then moves the marbles with the smallest label, say $i$, to either any empty box or the box containing marble $i+1$. Cathy wins if at any point there is a box containing only marble $n$.
Determine all pairs of integers $(n, k)$ such that Cathy can win this game.



## 2023 — 4

**Record:** `apm_2023_44bc62`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2023_44bc62.json.gz).

Let $c>0$ be a given positive real and $\mathbb{R}_{>0}$ be the set of all positive reals. Find all functions $f: \mathbb{R}_{>0} \rightarrow \mathbb{R}_{>0}$ such that
$$
f((c+1) x+f(y))=f(x+2 y)+2 c x \quad \text{ for all } x, y \in \mathbb{R}_{>0} .
$$



## 2023 — 5

**Record:** `apm_2023_effff8`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2023_effff8.json.gz).

There are $n$ line segments on the plane, no three intersecting at a point, and each pair intersecting once in their respective interiors. Tony and his $2 n-1$ friends each stand at a distinct endpoint of a line segment. Tony wishes to send Christmas presents to each of his friends as follows:
First, he chooses an endpoint of each segment as a "sink". Then he places the present at the endpoint of the segment he is at. The present moves as follows:
- If it is on a line segment, it moves towards the sink.
- When it reaches an intersection of two segments, it changes the line segment it travels on and starts moving towards the new sink.
If the present reaches an endpoint, the friend on that endpoint can receive their present. Prove Tony can send presents to exactly $n$ of his $2 n-1$ friends.



## 2023 — 1

**Record:** `apm_2023_fb45d1`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2023_fb45d1.json.gz).

Let $n \geq 5$ be an integer. Consider $n$ squares with side lengths $1,2, \ldots, n$, respectively. The squares are arranged in the plane with their sides parallel to the $x$ and $y$ axes. Suppose that no two squares touch, except possibly at their vertices.
Show that it is possible to arrange these squares in a way such that every square touches exactly two other squares.



## 2024 — 4

**Record:** `apm_2024_299020`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2024_299020.json.gz).

Prove that for every positive integer $t$ there is a unique permutation $a_{0}, a_{1}, \ldots, a_{t-1}$ of $0,1, \ldots, t-1$ such that, for every $0 \leq i \leq t-1$, the binomial coefficient $\binom{t+i}{2 a_{i}}$ is odd and $2 a_{i} \neq t+i$.



## 2024 — 3

**Record:** `apm_2024_531576`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2024_531576.json.gz).

Let $n$ be a positive integer and $a_{1}, a_{2}, \ldots, a_{n}$ be positive real numbers. Prove that
$$
\sum_{i=1}^{n} \frac{1}{2^{i}}\left(\frac{2}{1+a_{i}}\right)^{2^{i}} \geq \frac{2}{1+a_{1} a_{2} \ldots a_{n}}-\frac{1}{2^{n}} .
$$



## 2024 — 2

**Record:** `apm_2024_91e126`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2024_91e126.json.gz).

Consider a $100 \times 100$ table, and identify the cell in row $a$ and column $b$, $1 \leq a, b \leq 100$, with the ordered pair $(a, b)$. Let $k$ be an integer such that $51 \leq k \leq 99$. A $k$-knight is a piece that moves one cell vertically or horizontally and $k$ cells to the other direction; that is, it moves from $(a, b)$ to $(c, d)$ such that $(|a-c|,|b-d|)$ is either $(1, k)$ or $(k, 1)$. The $k$-knight starts at cell $(1,1)$, and performs several moves. A sequence of moves is a sequence of cells $(x_{0}, y_{0})=(1,1)$, $(x_{1}, y_{1})$, $(x_{2}, y_{2}), \ldots, (x_{n}, y_{n})$ such that, for all $i=1,2, \ldots, n$, $1 \leq x_{i}, y_{i} \leq 100$ and the $k$-knight can move from $(x_{i-1}, y_{i-1})$ to $(x_{i}, y_{i})$. In this case, each cell $(x_{i}, y_{i})$ is said to be reachable. For each $k$, find $L(k)$, the number of reachable cells.
Answer: $L(k)=\left\{\begin{array}{ll}100^{2}-(2 k-100)^{2} & \text{ if } k \text{ is even } \\ \frac{100^{2}-(2 k-100)^{2}}{2} & \text{ if } k \text{ is odd }\end{array}\right.$.



## 2025 — 2

**Record:** `apm_2025_0453f0`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2025_0453f0.json.gz).

Let $\alpha$ and $\beta$ be positive real numbers. Emerald makes a trip in the coordinate plane, starting off from the origin $(0,0)$. Each minute she moves one unit up or one unit to the right, restricting herself to the region $|x-y|<2025$, in the coordinate plane. By the time she visits a point ( $x, y$ ) she writes down the integer $\lfloor x \alpha+y \beta\rfloor$ on it. It turns out that Emerald wrote each non-negative integer exactly once. Find all the possible pairs $(\alpha, \beta)$ for which such a trip would be possible.



## 2025 — 4

**Record:** `apm_2025_e1a993`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2025_e1a993.json.gz).

Let $n \geq 3$ be an integer. There are $n$ cells on a circle, and each cell is assigned either $0$ or $1$. There is a rooster on one of these cells, and it repeats the following operations:
- If the rooster is on a cell assigned $0$, it changes the assigned number to $1$ and moves to the next cell counterclockwise.
- If the rooster is on a cell assigned $1$, it changes the assigned number to $0$ and moves to the cell after the next cell counterclockwise.

Prove that the following statement holds true after sufficiently many operations:
If the rooster is on a cell $C$, then the rooster would go around the circle exactly three times, stopping again at $C$. Moreover, every cell would be assigned the same number as it was assigned right before the rooster went around the circle $3$ times.



# BMO


## 2004 — 4.

**Record:** `rou_2004_775bce`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2004_775bce.json.gz).

O mulţime finită de drepte, oricare trei neconcurente, partiţionează planul într-un număr de regiuni. Două regiuni se numesc "vecine" dacă frontierele lor au în comun mai mult decât un segment nedegenerat.

În fiecare regiune trebuie scris un număr întreg astfel încât:
(i) produsul numerelor scrise în oricare două regiuni vecine este strict mai mic decât suma lor;
(ii) pentru fiecare dintre dreptele date, suma numerelor scrise în regiunile aflate de aceeaşi parte a ei este egală cu $0$.

Demonstraţi că acesta este posibil dacă şi numai dacă nu toate dreptele sunt paralele.



## 2004 — Problema 3

**Record:** `rou_2004_a43add`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2004_a43add.json.gz).

Un grup este format din $n$ turişti. Oricum am alege 3 turişti, există 2 dintre ei care nu se cunosc. Pentru orice partiție a turiştilor în două autobuze putem găsi doi turişti care se cunosc şi sunt în acelaşi autobuz. Demonstrați că în grupul de turişti există un turist care are cel mult $\frac{2}{5} n$ cunoscuți.



## 2007 — 4

**Record:** `grc_2007_31776c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/greece/grc_2007_31776c.json.gz).

For a given positive integer $n > 2$, let $C_1$, $C_2$, $C_3$ be the boundaries of three convex $n$-gons in the plane such that the sets $C_1 \cap C_2$, $C_2 \cap C_3$, $C_3 \cap C_1$ are finite. Find the maximum number of points of the set $C_1 \cap C_2 \cap C_3$.



## 2008 — 3

**Record:** `mkd_2008_30218d`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_30218d.json.gz).

$2n$ ($n > 1$) points are given in the plane. Line $p$ lies in the plane and does not cross the given points. Prove that this line cuts no more than $n^2$ segments with end in the given points.



## 2008 — 3

**Record:** `mkd_2008_8fbac0`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_8fbac0.json.gz).

Let $n$ be a positive integer. The rectangle $ABCD$ with side lengths $AB = 90n + 1$ and $BC = 90n + 5$ is partitioned into unit squares with sides parallel to the sides of $ABCD$. Let $S$ be the set of all points which are vertices of these unit squares. Prove that the number of lines which pass through at least two points from $S$ is divisible by 4.



## 2008 — 4

**Record:** `mkd_2008_f3b3c2`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_f3b3c2.json.gz).

Let $1*2*3*4*5*6*7*8*9=0$ be a given equality. Is it possible to substitute some of the $*$ with $+$ and the others with $-$ to obtain a correct equality?



## 2009 — 3

**Record:** `bmo_2009_f956f2`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2009_f956f2.json.gz).

A $9 \times 12$ rectangle is divided into unit squares. The centers of all the unit squares, except the four corner squares and the eight squares adjacent (by side) to them, are colored red. Is it possible to numerate the red centers by $C_{1}, C_{2}, \ldots, C_{96}$ so that the following two conditions are fulfilled:
$1^{\circ}$ All segments $C_{1} C_{2}, C_{2} C_{3}, \ldots C_{95} C_{96}, C_{96} C_{1}$ have the length $\sqrt{13}$;
$2^{\circ}$ The poligonal line $C_{1} C_{2} \ldots C_{96} C_{1}$ is centrally symmetric?



## 2009 — 2АБ.

**Record:** `mkd_2009_24150b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_24150b.json.gz).

Провери ја точноста на равенството:
$$
\sum_{k=1}^{n} \frac{(-1)^{k+1}}{k} \binom{n}{k} = 1 + \frac{1}{2} + \frac{1}{3} + \dots + \frac{1}{n},
$$



## 2009 — 4А.

**Record:** `mkd_2009_5131ff`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_5131ff.json.gz).

Секоја точка од рамнината е обоена во една од две бои, сина или црвена. Да се докаже дека во таа рамнина постои рамностран триаголник чии темиња се обоени во една иста боја.



## 2009 — 3В.

**Record:** `mkd_2009_620603`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_620603.json.gz).

За даден број ќе велиме дека е “шарен” ако е запишан со еднаков број парни и непарни цифри. Да се определи бројот на сите четирицифрени “шарени” броеви запишани со различни цифри?



## 2009 — 3.

**Record:** `mkd_2009_895f98`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_895f98.json.gz).

Македонската математичка олимпијада се одржува во две соби означени со броеви $1$ и $2$. На почетокот сите натпреварувачи влегуваат во соба бр.$1$. Краен распоред на натпреварувачите по соби се добива на следниот начин: листа со имиња на неколку од натпреварувачите се чита на глас; кога едно име ќе биде прочитано, тој натпреварувач и сите негови познаници меѓу останатите натпреварувачи ја променуваат просторијата во која моментално се наоѓаат. Така на секоја листа имиња одговара по еден краен распоред на натпреварувачите по соби. Покажи дека вкупниот број на можни крајни распореди не е еднаков на $2009$. (познанство меѓу натпреварувачи е симетрична релација).



## 2009 — 3.

**Record:** `mkd_2009_c6e2af`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_c6e2af.json.gz).

The Macedonian mathematical Olympiad is held in two rooms labeled with the numbers $1$ and $2$. In the beginning all the contestants are in room $1$. The final schedule is obtained in the following manner: a list of names of some of the contestants is read; when a contestant's name is read, he and all of his friends change the room in which they are at the moment. So to every list of names corresponds a final schedule. Prove that the total number of possible schedules cannot be equal to $2009$. (Friendship is a symmetrical relation.)



## 2010 — Problem 3.

**Record:** `mkd_2010_b41ce7`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2010_b41ce7.json.gz).

A strip of width $w$ is the set of all points which lie on, or between, two parallel lines distance $w$ apart. Let $S$ be a set of $n$ ($n \ge 3$) points on the plane such that any three different points of $S$ can be covered by a strip of width $1$.
Prove that $S$ can be covered by a strip of width $2$.



## 2010 — Problem 3.

**Record:** `rou_2010_b512fc`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2010_b512fc.json.gz).

A strip of breadth $\ell$ is the set of those points in the plane, situated between or on two parallel lines at distance $\ell$ one from the other.
Consider a finite set $S$ of $n \geq 3$ (distinct) points in the plane, with the property that any three points of $S$ can be covered by a strip of breadth 1. Prove the set $S$ can be covered by a strip of breadth 2.



## 2011 — 3

**Record:** `mkd_2011_c1004b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2011_c1004b.json.gz).

Let $S$ be a finite set of positive integers which has the following property: if $x$ is a member of $S$, then so are all positive divisors of $x$. A non-empty subset $T$ of $S$ is a good if whenever $x, y \in T$ and $x < y$, the ratio $y/x$ is a power of a prime number. A non-empty subset $T$ of $S$ is bad if whenever $x, y \in T$ and $x < y$, the ratio $y/x$ is not a power of a prime number. We agree that a singleton subset of $S$ is both good and bad. Let $k$ be the largest possible size of a good subset of $S$. Prove that $k$ is also the smallest number of pairwise-disjoint bad subset whose union is $S$.



## 2012 — 3

**Record:** `mkd_2012_683110`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2012_683110.json.gz).

Let $n$ be a positive integer. Let $P_n = \{2^n, 2^{n-1} \cdot 3, 2^{n-2} \cdot 3^2, \dots, 3^n\}$. For each subset $X$ of $P_n$, we write $S_X$ for the sum of all elements of $X$, with the convention that $S_\emptyset = 0$ where $\emptyset$ is the empty set. Suppose that $y$ is a real number with $0 \le y \le 3^{n+1} - 2^{n+1}$.
Prove that there is a subset $Y$ of $P_n$ such that $0 \le y - S_Y < 2^n$.



## 2013 — 7

**Record:** `bmo_2013_654e0d`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2013_654e0d.json.gz).

Suppose that $k$ is a positive integer. A bijective map $f: \mathbb{Z} \to \mathbb{Z}$ is said to be $k$-jumpy if $|f(z) - z| \le k$ for all integers $z$.
Is it that case that for every $k$, each $k$-jumpy map is a composition of 1-jumpy maps?
*It is well known that this is the case when the support of the map is finite.*



## 2013 — 2

**Record:** `bmo_2013_84acf9`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2013_84acf9.json.gz).

Some squares of an $n \times n$ chessboard have been marked ($n \in \mathbb{N}^*$). Prove that if the number of marked squares is at least $n(\sqrt{n} + \frac{1}{2})$, then there exists a rectangle whose vertices are centers of marked squares.



## 2013 — 4

**Record:** `bmo_2013_a11bcd`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2013_a11bcd.json.gz).

A closed, non-self-intersecting broken line $L$ is drawn over a $(2n+1) \times (2n+1)$ chessboard in such a way that the set of $L$'s vertices coincides with the set of the vertices of the board's squares and every edge in $L$ is a side of some board square. All board squares lying in the interior of $L$ are coloured in red. Prove that the number of neighbouring pairs of red squares in every row of the board is even.



## 2013 — 5

**Record:** `bmo_2013_a923a3`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2013_a923a3.json.gz).

The cells of an $n \times n$ chessboard are coloured in several colours so that no $2 \times 2$ square contains four cells of the same colour. A proper path of length $m$ is a sequence $a_1, a_2, \dots, a_m$ of distinct cells in which the cells $a_i$ and $a_{i+1}$ have a common side and are coloured in different colours for all $1 \le i < m$. Show that there exists a proper path of length $n$.



## 2013 — Problem 4.

**Record:** `grc_2013_323f49`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/greece/grc_2013_323f49.json.gz).

In a mathematical competition some competitors are friends; friendship is always mutual, that is to say that is when $A$ is a friend of $B$, then also $B$ is a friend of $A$. We say that $n \ge 3$ different competitors $A_1, A_2, \dots, A_n$ form a weekly-friendly circle if $A_i$ is not a friend of $A_{i+1}$, for $1 \le i \le n$ ($A_{n+1} = A_1$), and there are no other pairs of non-friends among the components of this cycle.

The following property is satisfied:
For every competitor $C$, and every weekly-friendly cycle $\mathcal{A}$ of competitors not including $C$, the set of competitors $D$ in $\mathcal{A}$ which are not friends of $C$ has at most one element.

Prove that all competitors of this mathematical competition can be arranged into three rooms, such that every two competitors that are in the same rooms are friends.



## 2013 — Problem 4

**Record:** `rou_2013_306b97`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2013_306b97.json.gz).

In a mathematical competition some competitors are friends; friendship is always mutual, that is to say that when $A$ is a friend of $B$, then also $B$ is a friend of $A$. We say that $n \geq 3$ different competitors $A_{1}, A_{2}, \ldots, A_{n}$ form a weakly-friendly cycle if $A_{i}$ is not a friend of $A_{i+1}$, for $1 \leq i \leq n\left(A_{n+1}=A_{1}\right)$, and there are no other pairs of non-friends among the components of this cycle.
The following property is satisfied:
for every competitor $C$, and every weakly-friendly cycle $\mathcal{S}$ of competitors not including $C$, the set of competitors $D$ in $\mathcal{S}$ which are not friends of $C$ has at most one element.
Prove that all competitors of this mathematical competition can be arranged into three rooms, such that every two competitors that are in the same room are friends.

Problem:

La un concurs de matematică unii elevi participanţi sunt prieteni; prietenia este întotdeauna mutuală, adică dacă $A$ este prieten cu $B$ atunci şi $B$ este prieten cu $A$. Spunem că $n$ elevi diferiţi $(n \geq 3) A_{1}, A_{2}, \ldots, A_{n}$ formează un ciclu slab-prietenos dacă $A_{i}$ nu este prieten cu $A_{i+1}$, pentru $1 \leq i \leq n\left(A_{n+1}=A_{1}\right)$, şi nu mai există în acest ciclu alte perechi de neprieteni.
Presupunem că este satisfăcută următoarea proprietate:
pentru orice elev $C$, orice ciclu slab-prietenos $\mathcal{S}$ care nu-l conţine pe $C$ are cel mult un elev care nu este prieten cu $C$.
Să se arate că toţi elevii pot fi repartizaţi în trei camere, astfel încât oricare doi elevi din aceeaşi cameră sunt prieteni.



## 2014 — 4

**Record:** `mkd_2014_9ea0c9`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2014_9ea0c9.json.gz).

Let $n$ be a positive integer. A regular hexagon with side length $n$ is divided into equilateral triangles with side length $1$ by lines parallel to its sides.
Find the number of regular hexagons all of whose vertices are along the vertices of the equilateral triangles.



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



## 2015 — NT1.

**Record:** `bmo_2015_6abd41`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2015_6abd41.json.gz).

Let $n$ be a given even positive integer. First John writes the consecutive square numbers $1^2, 3^2, \dots, (2n-1)^2$ on the blackboard. Then he picks some three of them, say $a_1, a_2, a_3$, erases them and writes the number
$$
1 + \sum_{1 \le i < j \le 3} |a_i - a_j|
$$
on the blackboard. He continues this way replacing each time three of the numbers on the blackboard until only two numbers remain on it. Prove that the sum of the squares of the two remaining numbers is different from any of the numbers $1^2, 3^2, \dots, (2n-1)^2$ written initially on the blackboard.



## 2018 — 3

**Record:** `mkd_2018_3ac94a`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2018_3ac94a.json.gz).

Alice and Bob play the following game: They start with two non-empty piles of coins. Taking turns, with Alice playing first, each player chooses a pile with an even number of coins and moves half of this pile to the other pile. The game ends if a player cannot move, in which case the other player wins.
Determine all pairs $(a,b)$ of positive integers such that if initially the two piles have $a$ and $b$ coins respectively, then Bob has a winning strategy.



## 2019 — Problem 4.

**Record:** `grc_2019_037737`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/greece/grc_2019_037737.json.gz).

A grid consists of all points of the form $(m, n)$ where $m$ and $n$ are integers with $|m| \le 2019$, $|n| \le 2019$ and $|m| + |n| < 4038$. We call the points $(m, n)$ of the grid with either $|m| = 2019$ or $|n| = 2019$ the *boundary points*. The four lines $x = \pm 2019$ and $y = \pm 2019$ are called *boundary lines*. Two points in the grid are called *neighbours* if the distance between them is equal to 1.
Anna and Bob play a game on this grid.
Anna starts with a token at the point $(0, 0)$. They take turns, with Bob playing first.
1) On each of his turns, Bob deletes at most two boundary points on each boundary line.
2) On each of her turns, Anna makes exactly three *steps*, where a *step* consists of moving her token from its current point to any neighbouring point which has not been deleted.
As soon as Anna places her token on some boundary point which has not been deleted, the game is over and Anna wins.

Does Anna have a winning strategy?



## 2023 — Problem 3.

**Record:** `jbm_2023_78057b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/jbmo/jbm_2023_78057b.json.gz).

Alice and Bob play the following game on a $100 \times 100$ grid, taking turns, with Alice starting first. Initially the grid is empty. At their turn, they choose an integer from $1$ to $100^{2}$ that is not written yet in any of the cells and choose an empty cell, and place it in the chosen cell. When there is no empty cell left, Alice computes the sum of the numbers in each row, and her score is the maximum of these $100$ sums. Bob computes the sum of the numbers in each column, and his score is the maximum of these $100$ sums. Alice wins if her score is greater than Bob's score, Bob wins if his score is greater than Alice's score, otherwise no one wins.
Find if one of the players has a winning strategy, and if so which player has a winning strategy.



# BMO-SL


## 2010 — NT1

**Record:** `bmo_2010_2df1d0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2010_2df1d0.json.gz).

Is it possible to partition the set of all integer numbers into ordered triples in such a way that, for every triple $(a, b, c)$ the number
$$
|a^3 b + b^3 c + c^3 a|
$$
be a perfect square?



## 2010 — C1

**Record:** `bmo_2010_36a58c`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2010_36a58c.json.gz).

In a soccer tournament each team plays exactly one game with all others. The winner gets 3 points, the loser zero and each team gets 1 point in case of a draw.
It is known that $n$ teams ($n \ge 3$) took part in a tournament and the final classification is given by an arithmetical progression of points, the last team having only 1 point.
a) Prove that this is not possible in the Championship of the Republic of Moldova (with $n=12$).
b) Find all values of $n$ and all configurations when this is possible.



## 2010 — C4

**Record:** `bmo_2010_76e4e6`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2010_76e4e6.json.gz).

Integers are written in the cells of a table $2010 \times 2010$. Adding $1$ to all the numbers in a row or in a column is called a *move*. We say that the table is *equilibrium* if one can obtain after finitely many moves a table in which all the numbers are equal.

a) Find the largest positive integer $n$, for which there exists an equilibrium table containing the numbers $2^0, 2^1, \dots, 2^n$.

b) For this $n$, find the maximal number that may be contained in such a table.



## 2010 — C2

**Record:** `bmo_2010_82e1d0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2010_82e1d0.json.gz).

A grasshopper jumps on the plane from an integer point (point with all integer coordinates) to another integer point according to the following rules: His first jump is of length $\sqrt{98}$, his second jump is of length $\sqrt{149}$, his next jump is of length $\sqrt{98}$, and so on, alternatively. What is the least possible odd number of moves in which the grasshopper could return to his starting point?



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



## 2011 — C3

**Record:** `bmo_2011_2d432f`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2011_2d432f.json.gz).

Is it possible to partition the set of positive integer numbers into two classes, none of which contains an infinite arithmetic sequence (with a positive ratio)?
What if we require the extra condition that, in each class $C$ of the partition, the set of differences
$$
\{ \min \{ n : n \in C \text{ and } n > m \} - m : m \in C \}
$$
be bounded?



## 2012 — C1

**Record:** `bmo_2012_e19c1d`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2012_e19c1d.json.gz).

Suppose that $m$ is a positive integer. Let $P_m = \{2^m, 2^{m-1}3, 2^{m-2}3^2, \dots, 3^m\}$. If $X$ is a subset of $P_m$, we write $S_X$ for the sum of all elements of $X$, with the convention that $S_\emptyset = 0$ where $\emptyset$ is the empty set. Suppose that $y$ is a real number with $0 \le y \le 3^{m+1} - 2^{m+1}$. Prove that there is a subset $Y$ of $P_m$ such that $0 \le y - S_Y < 2^m$.



## 2014 — C2

**Record:** `bmo_2014_5daa9c`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_5daa9c.json.gz).

Let $M = \{1, 2, \dots, 2013\}$ and let $\Gamma$ be a circle. For every nonempty subset $\mathcal{A}$ of the set $M$, denote by $S(\mathcal{A})$ the sum of elements of the set $\mathcal{A}$, and define $S(\emptyset) = 0$ ($\emptyset$ is the empty set). Is it possible to join every subset $\mathcal{A}$ of $M$ with some point $A$ on the circle $\Gamma$ so that following conditions are fulfilled:
1. Different subsets are joined with different points;
2. All joined points are vertices of a regular polygon;
3. If $A_1, A_2, \dots, A_k$ are some of the joined points, $k > 2$, such that $A_1A_2 \dots A_k$ is a regular $k$-gon, then 2014 divides $S(\mathcal{A}_1) + S(\mathcal{A}_2) + \dots + S(\mathcal{A}_k)$?



## 2014 — A5

**Record:** `bmo_2014_64e0c9`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_64e0c9.json.gz).

Let $n \in \mathbb{N}$, $n > 2$, and suppose $a_1, a_2, \dots, a_{2n}$ is a permutation of the numbers $1, 2, \dots, 2n$ such that $a_1 < a_3 < \dots < a_{2n-1}$ and $a_2 > a_4 > \dots > a_{2n}$. Prove that
$$
(a_1 - a_2)^2 + (a_3 - a_4)^2 + \dots + (a_{2n-1} - a_{2n})^2 > n^3.
$$



## 2014 — C3

**Record:** `bmo_2014_96bc5b`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_96bc5b.json.gz).

Consider a lattice of side length $1$ equilateral triangles forming a regular hexagon of side length $n$. Show that the number of ways of simultaneously selecting six vertices of the lattice to form the vertices of a regular hexagon is a perfect square.



## 2014 — C1

**Record:** `bmo_2014_bde1ed`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2014_bde1ed.json.gz).

The International Mathematical Olympiad is being organized in Japan, where a folklore belief is that the number 4 brings bad luck. The opening ceremony takes place at the Grand Theatre where each row has the capacity of 55 seats. What is the maximum number of contestants that can be seated in a single row with the restriction that no two of them are 4 seats apart (so that bad luck during the competition is avoided)?



## 2015 — C2.

**Record:** `bmo_2015_5a0b4c`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2015_5a0b4c.json.gz).

Isaac and Jeremy play a game. Isaac tells Jeremy that he is thinking of some $2^n$ integers $k_1, \dots, k_{2^n}$, where $n$ is a positive integer. Jeremy asks questions of the form "is $k_i < k_j$?", to which Isaac answers truthfully. After $n2^{n-1}$ questions, Jeremy must state whether or not Isaac's numbers are all distinct. Show that Jeremy has no way of ensuring that his statement is correct. Jeremy's questions may depend on the answers he has already received, and are exactly determined by them.

[Slightly harder formulation: instead ask "Can Jeremy ensure that his statement is correct?"]



## 2015 — C1.

**Record:** `bmo_2015_9ee8d6`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2015_9ee8d6.json.gz).

We have $3366$ film critics who sent their preferences for the best actor and best actress for the Oscars. It turns out that for every integer $n \in \{1, 2, \dots, 100\}$ there is an actor or an actress who has been voted exactly $n$ times. Show that there are two critics which voted in exactly the same manner.



## 2015 — C3.

**Record:** `bmo_2015_e3a469`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2015_e3a469.json.gz).

A chessboard of size $1000 \times 1000$ is tiled with tiles of size $1 \times 10$. You do not know the tiling but wish to uncover it. In order to do so, you can choose some $N$ cells on the board, following which you will learn what the positions of the tiles that cover those cells are. What is the least $N$ such that you can make your choice so as to always be able to reconstruct the complete tiling?



## 2016 — C1.

**Record:** `bmo_2016_6d4fd5`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2016_6d4fd5.json.gz).

Let positive integers $K$ and $d$ be given. Prove that there exists a positive integer $n$ and a sequence of $K$ positive integers $b_1, b_2, \dots, b_K$ such that the number $n$ is a $d$-digit palindrome in all number bases $b_1, b_2, \dots, b_K$.



## 2016 — N5.

**Record:** `bmo_2016_715bc2`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2016_715bc2.json.gz).

A positive integer $n$ is *downhill* if its decimal representation $\overline{a_k a_{k-1} \dots a_0}$ satisfies $a_k \ge a_{k-1} \ge \dots \ge a_0$. A real-coefficient polynomial $P$ is *integer-valued* if $P(n)$ is an integer for all integer $n$, and *downhill-integer-valued* if $P(n)$ is an integer for all downhill positive integers $n$. Is it true that every downhill-integer-valued polynomial is also integer-valued?



## 2016 — C3.

**Record:** `bmo_2016_82a6cb`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2016_82a6cb.json.gz).

The plane is divided into unit squares by means of two sets of parallel lines. The unit squares are coloured in $1201$ colours so that no rectangle of perimeter $100$ contains two squares of the same colour. Show that no rectangle of size $1 \times 1201$ contains two squares of the same colour.



## 2016 — C2.

**Record:** `bmo_2016_bcac10`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2016_bcac10.json.gz).

There are $2016$ customers who entered a shop on a particular day. Every customer entered the shop exactly once (i.e. the customer entered the shop, stayed there for some time and then left the shop without returning back).
Find the maximal $k$ such that the following holds:
There are $k$ customers such that either all of them were in the shop at a specific time instance or no two of them were both in the shop at any time instance.



## 2017 — C1

**Record:** `bmo_2017_386ab9`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2017_386ab9.json.gz).

A grasshopper is sitting at an integer point in the Euclidean plane. Each second it jumps to another integer point in such a way that the jump vector is constant. A hunter that knows neither the starting point of the grasshopper nor the jump vector (but knows that the jump vector for each second is constant) wants to catch the grasshopper. Each second the hunter can choose one integer point in the plane and, if the grasshopper is there, he catches it. Can the hunter always catch the grasshopper in a finite amount of time?



## 2017 — C2

**Record:** `bmo_2017_3e2f81`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2017_3e2f81.json.gz).

Let $n$, $a$, $b$, $c$ be natural numbers. Every point on the coordinate plane with integer coordinates is colored in one of $n$ colors. Prove there exists $c$ triangles whose vertices are colored in the same color, which are pairwise congruent, and which have a side whose length is divisible by $a$ and a side whose length is divisible by $b$.



## 2017 — C3

**Record:** `bmo_2017_3f4864`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2017_3f4864.json.gz).

Let $n \ge 4$ points in the plane, no three of them are collinear. Prove that the number of parallelograms of area $1$, formed by these points, is at most $\frac{n^2-3n}{4}$.



## 2017 — C5

**Record:** `bmo_2017_5eecca`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2017_5eecca.json.gz).

We have $n$ students sitting at a round table. Initially each student is given one candy. At each step each student having candies either picks one of its candies and gives it to one of its neighbouring students, or distributes all of its candies to its neighbouring students in any way he wishes. A distribution of candies is called legal if it can be reached from the initial distribution via a sequence of steps.
Determine the number of legal distributions. (All the candies are identical.)



## 2017 — C6

**Record:** `bmo_2017_79742c`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2017_79742c.json.gz).

What is the least positive integer $k$ such that, in every convex $101$-gon, the sum of any $k$ diagonals is greater than or equal to the sum of the remaining diagonals?



## 2017 — A3

**Record:** `bmo_2017_7d83b0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2017_7d83b0.json.gz).

Find all the functions $f: \mathbb{N} \to \mathbb{N}$ such that:
$$
n + f(m) \mid f(n) + n f(m) \quad (1)
$$
for any $m, n \in \mathbb{N}$



## 2019 — C1

**Record:** `bmo_2019_17ff25`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2019_17ff25.json.gz).

100 couples are invited to a traditional Moldovan dance. The 200 people stand in a line, and then in a step, two of them (not necessarily adjacent) may swap positions. Find the least $C$ such that whatever the initial order, they can arrive at an ordering where everyone is dancing next to their partner in at most $C$ steps.



## 2019 — TN1

**Record:** `bmo_2019_404973`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2019_404973.json.gz).

Let $\mathbb{P}$ be the set of all prime numbers. Find all functions $f: \mathbb{P} \to \mathbb{P}$ such that
$$
f(p)^{f(q)} + q^p = f(q)^{f(p)} + p^q
$$
holds for all $p, q \in \mathbb{P}$.



## 2019 — C2

**Record:** `bmo_2019_52e757`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2019_52e757.json.gz).

Suppose that the numbers $\{1, 2, \dots, 25\}$ are written in some order in an $5 \times 5$ array. Find the maximal positive integer $k$, such that the following holds. There is always an $2 \times 2$ subarray whose numbers have a sum not less than $k$.

An $5 \times 5$ array must be completed with all numbers $\{1, 2, \dots, 25\}$, one number in each cell. Find the maximal positive integer $k$, such that for any completion of the array there is a $2 \times 2$ square (subarray), whose numbers have a sum not less than $k$.



## 2019 — C3

**Record:** `bmo_2019_840a04`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2019_840a04.json.gz).

Anna and Bob play a game on the set of all points of the form $(m, n)$ where $m, n$ are integers with $|m|, |n| \leq 2019$. Let us call the lines $x = \pm 2019$ and $y = \pm 2019$ the *boundary lines* of the game. The points of these lines are called the *boundary points*. The *neighbours* of point $(m, n)$ are the points $(m+1, n)$, $(m-1, n)$, $(m, n+1)$, $(m, n-1)$.

Anna starts with a token at the origin $(0, 0)$. With Bob playing first, they alternately perform the following steps: At his turn, Bob deletes two points on each boundary line. On her turn Anna makes a sequence of three moves of the token, where a *move* of the token consists of picking up the token from its current position and placing it in one of its neighbours.

To win the game Anna must place her token on a boundary point before it is deleted by Bob. Does Anna have a winning strategy?

[Note: At every turn except perhaps her last, Anna **must** make **exactly** three moves.]



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



## 2020 — C1

**Record:** `bmo_2020_dff0bd`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2020_dff0bd.json.gz).

Let $s \ge 2$ and $n \ge k \ge 2$ be integers, and let $\mathcal{A}$ be a subset of $\{1, 2, \dots, n\}^k$ of size at least $2sk^2n^{k-2}$ such that any two members of $\mathcal{A}$ share some entry. Prove that there are an integer $p \le k$ and $s+2$ members $A_1, A_2, \dots, A_{s+2}$ of $\mathcal{A}$ such that $A_i$ and $A_j$ share the $p$-th entry alone, whenever $i \ne j$.

Miroslav Mironov, Bulgaria



## 2021 — C5

**Record:** `bmo_2021_085336`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2021_085336.json.gz).

Angel has a warehouse, which initially contains $100$ piles of $100$ pieces of rubbish each. Each morning, Angel either clears every piece of rubbish from a single pile, or one piece of rubbish from each pile. However, every evening, a demon sneaks into the warehouse and adds one piece of rubbish to each non-empty pile, or creates a new pile with one piece. What is the first morning when Angel can guarantee to have cleared all the rubbish from the warehouse?

**Proposed by United Kingdom**



## 2021 — C4

**Record:** `bmo_2021_0a2e16`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2021_0a2e16.json.gz).

A sequence of $2n + 1$ non-negative integers $a_1, a_2, \dots, a_{2n+1}$ is given. There's also a sequence of $2n + 1$ consecutive cells enumerated from $1$ to $2n + 1$ from left to right, such that initially the number $a_i$ is written on the $i$-th cell, for $i = 1, 2, \dots, 2n + 1$. Starting from this initial position, we repeat the following sequence of steps, as long as it's possible:
*Step 1:* Add up the numbers written on all the cells, denote the sum as $s$.
*Step 2:* If $s$ is equal to $0$ or if it is larger than the current number of cells, the process terminates. Otherwise, remove the $s$-th cell, and shift all cells that are to the right of it one position to the left. Then go to Step 1.
Example: $(1, 0, 1, \underline{2}, 0) \to (1, \underline{0}, 1, 0) \to (1, \underline{1}, 0) \to (\underline{1}, 0) \to (0)$.
A sequence $a_1, a_2, \dots, a_{2n+1}$ of non-negative integers is called balanced, if at the end of this process there's exactly one cell left, and it's the cell that was initially enumerated by $(n+1)$, i.e. the cell that was initially in the middle.
Find the total number of balanced sequences as a function of $n$.



## 2021 — A4

**Record:** `bmo_2021_2fdefd`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2021_2fdefd.json.gz).

Let $f, g$ be functions from the positive integers to the integers. Vlad the impala is jumping around the integer grid. His initial position is $\mathbf{x}_0 = (0,0)$, and for every $n \ge 1$, his jump is
$$
\mathbf{x}_n - \mathbf{x}_{n-1} = (\pm f(n), \pm g(n)) \text{ or } (\pm g(n), \pm f(n)),
$$
with eight possibilities in total. Is it always possible that Vlad can choose his jumps to return to his initial location $(0,0)$ infinitely many times when
(a) $f, g$ are polynomials with integer coefficients?
(b) $f, g$ are any pair of functions from the positive integers to the integers?



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



## 2021 — C6

**Record:** `bmo_2021_c13570`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2021_c13570.json.gz).

There is a population $P$ of $10000$ bacteria, some of which are friends (friendship is mutual), so that each bacterion has at least one friend and if we wish to assign to each bacterion a coloured membrane so that no two friends have the same colour, then there is a way to do it with $2021$ colours, but not with $2020$ or less.

Two friends $A$ and $B$ can decide to *merge* in which case they become a single bacterion whose friends are precisely the union of friends of $A$ and $B$. (Merging is not allowed if $A$ and $B$ are not friends.) It turns out that no matter how we perform one merge or two consecutive merges, in the resulting population it would be possible to assign $2020$ colours or less so that no two friends have the same colour. Is it true that in any such population $P$ every bacterium has at least $2021$ friends?

**Proposed by Bulgaria**



## 2021 — C3

**Record:** `bmo_2021_c837cf`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2021_c837cf.json.gz).

In an exotic country, the National Bank issues coins that can take any value in the interval $[0, 1]$. Find the smallest constant $c > 0$ such that the following holds, no matter the situation in that country:
*Any citizen of the exotic country that has a finite number of coins, with a total value of no more than 1000, can split those coins into 100 boxes, such that the total value inside each box is at most c.*



## 2022 — C2.

**Record:** `bmo_2022_2d08c3`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2022_2d08c3.json.gz).

Alice is drawing a shape on a piece of paper. She starts by placing her pencil at the origin, and then draws line segments of length $1$, alternating between vertical and horizontal segments. Eventually, her pencil returns to the origin, forming a closed, non-self-intersecting shape. Show that the area of this shape is even if and only if its perimeter is a multiple of eight.



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



## 2022 — C4.

**Record:** `bmo_2022_8f10e3`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2022_8f10e3.json.gz).

Let $n \ge 3$ be an odd positive integer, and consider an $n \times n$ grid containing $n^2$ cells. Dionysus colours each cell either red or blue. A frog can hop directly between two cells if they have the same colour and share at least one vertex. Xanthias views the colouring, and wants to place frogs on $k$ of the cells so that any cell can be reached by a frog in a finite number of hops. Find the least value of $k$ such that Xanthias can always be successful regardless of the colouring chosen by Dionysus.



## 2022 — C1.

**Record:** `bmo_2022_9167c0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2022_9167c0.json.gz).

There are 100 positive integer numbers written on a board. At each step, Alex composes 50 fractions using each number written on the board exactly once, brings these fractions to their irreducible form, and then replaces the 100 numbers on the board with the new numerators and denominators to create 100 new numbers. Find the smallest positive integer $n$ such that regardless of the values of the initial 100 numbers, after $n$ steps Alex can arrange to have on the board only pairwise coprime numbers.



## 2022 — N4.

**Record:** `bmo_2022_977a4b`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2022_977a4b.json.gz).

A hare and a tortoise run in the same direction, at constant but different speeds, around the base of a tall square tower. They start together at the same vertex, and the run ends when both return to the initial vertex simultaneously for the first time. Suppose the hare runs with speed $1$, and the tortoise with speed less than $1$. For what rational numbers $x$ is it true that, if the tortoise runs with speed $x$, the fraction of the entire run for which the tortoise can see the hare is also $x$?



## 2022 — C3.

**Record:** `bmo_2022_9fea53`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2022_9fea53.json.gz).

Find the largest positive integer $k$ for which there exists a convex polyhedron $P$ with the following properties:
(a) $P$ has exactly $2022$ edges.
(b) The degrees of the vertices of $P$ don't differ by more than $1$.
(c) It is possible to colour the edges of $P$ with $k$ colours such that for every colour $c$, and every pair of vertices ($v_1$, $v_2$) of $P$, there is a monochromatic path between $v_1$ and $v_2$ in the colour $c$.



## 2023 — C3

**Record:** `bmo_2023_3cf7b2`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2023_3cf7b2.json.gz).

In a given community of people, each person has at least two friends within the community. Whenever some people from this community sit on a round table such that each adjacent pair of people are friends, it happens that no non-adjacent pair of people are friends. Prove that there exist two people in this community such that each has exactly two friends and they have at least one common friend.



## 2023 — C4

**Record:** `bmo_2023_4f2ba4`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2023_4f2ba4.json.gz).

Once upon a time there are $n$ pairs of princes and princesses who are in love with each other. One day a witch comes along and turns all the princes into frogs; the frogs can be distinguished by sight but the princesses cannot tell which frog corresponds to which prince. The witch tells the princesses that if any of them kisses the frog that corresponds to the prince that she loves then that frog will immediately transform back into a prince. If each princess can stand kissing at most $k$ frogs, what is the maximum number of princes they can be sure to save?

(The princesses may take turns kissing in any order, communicate with each other and vary their strategy for future kisses depending on information gained from past kisses.)



## 2023 — C2

**Record:** `bmo_2023_5e97b2`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2023_5e97b2.json.gz).

For an integer $n \ge 2$, the tuple $(1, 2, \dots, n)$ is written on a blackboard. On each turn, one can choose two numbers from the tuple such that their sum is a perfect square and swap them to obtain a new tuple. Find all integers $n \ge 2$ for which all permutations of $\{1, 2, \dots, n\}$ can appear on the blackboard in this way.



## 2023 — C1

**Record:** `bmo_2023_aef8b8`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2023_aef8b8.json.gz).

Joe and Penny play a game. Initially there are 5000 stones in a pile, and the two players remove stones from the pile by making a sequence of moves. On the $k$th move, any number of stones between 1 and $k$ inclusive may be removed. Joe makes the odd-numbered moves and Penny makes the even-numbered moves. The player who removes the very last stone is the winner. Who wins if both players play perfectly?



## 2023 — C5

**Record:** `bmo_2023_be5fcc`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2023_be5fcc.json.gz).

Find the greatest integer $k \le 2023$ for which, regardless of how Alice colors exactly $k$ numbers among $\{1, 2, \dots, 2023\}$ in red, Bob can color some of the remaining uncolored numbers in blue, such that the sum of the red numbers is the same as the sum of the blue ones.



## 2024 — C1.

**Record:** `bmo_2024_17dc50`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2024_17dc50.json.gz).

Let $n$, $k$ be positive integers. Julia and Florian play a game on a $2n \times 2n$ board. Julia has secretly tiled the entire board with invisible dominos. Florian now chooses $k$ cells. All dominos covering at least one of these cells then turn visible. Determine the minimal value of $k$ such that Florian has a strategy to always deduce the entire tiling.



## 2024 — C5.

**Record:** `bmo_2024_22c656`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2024_22c656.json.gz).

Let $n \ge 3$ be a natural number. Anna and Bob play the following game on the vertices of a regular $n$-gon: Anna places her token on a vertex of the $n$-gon. Afterwards Bob places his token on another vertex of the $n$-gon. Then, with Anna playing first, they move their tokens alternately as follows for $2n$ rounds: In Anna's turn on the $k$-th round, she moves her token $k$ positions clockwise or anticlockwise. In Bob's turn on the $k$-th round, he moves his token 1 position clockwise or anticlockwise.
If at the end of any person's turn the two tokens are on the same vertex, then Anna wins the game. Otherwise Bob wins. Decide for each value of $n$ which player has a winning strategy.



## 2024 — C3.

**Record:** `bmo_2024_37ccab`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2024_37ccab.json.gz).

Let $n \ge 3$. Alice and Bob play the following game: Alice chooses $k \in \{3, 4, \dots, n\}$ and draws a $3 \times k$ table, then he fills the $k$ cells of the first row with different numbers from $\{1, 2, \dots, n\}$. Then, Bob fills on the second row some of the cells (eventually none) with distinct numbers from $\{1, 2, \dots, n\}$, and the rest of them with $0$. Finally, on each cell of the third row we write the sum of the two cells above. Show that regardless how Alice plays, Bob can guarantee that on the third row he can obtain, in some order, the terms of a non-constant arithmetical progression.



## 2024 — C4.

**Record:** `bmo_2024_3c60be`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2024_3c60be.json.gz).

Prove that for every positive integer $k$ there exists an integer $n$ and distinct primes $p_1, p_2, \dots, p_k$ such that, if $A(n)$ denotes the number of integers in $\{1, 2, \dots, n\}$ which are relatively prime to $p_1p_2\dots p_k$, then
$$
\left| n \left(1 - \frac{1}{p_1}\right) \left(1 - \frac{1}{p_2}\right) \cdots \left(1 - \frac{1}{p_k}\right) - A(n) \right| > 2^{k-3}.
$$



## 2024 — C2.

**Record:** `bmo_2024_4b7efa`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2024_4b7efa.json.gz).

Let $n \ge 2$ and $S = \{1, 2, \dots, n^2\}$. For any function $f : S \to S$ let $\text{Fix}(f) = \{x \in S \mid f(x) = x\}$. Find the possible values of the expression
$$
|\text{Fix}(f)| + |\text{Im}(f)| + \max_{k \in S} |f^{-1}(k)|
$$
as $f$ ranges over all functions $f : S \to S$.



## 2025 — C6

**Record:** `bmo_2025_012c01`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_012c01.json.gz).

There are $n$ cities in a country, where $n \geq 100$ is a positive integer. Some pairs of cities are connected by (two-way) flights. For two cities $A$ and $B$, a path is a sequence of distinct cities $C_0, C_1, C_2, \ldots, C_k, C_{k+1}$, such that there are flights between $C_i$ and $C_{i+1}$ for every $0 \leq i \leq k$, with $C_0 = A$ and $C_{k+1} = B$.
A long path between $A$ and $B$ is defined as a path such that no other path has more vertices. Similarly, a short path is defined as a path with the fewest vertices. In particular, if $A$ and $B$ have a direct flight, that is the shortest path.
Assume that for any pair of cities $A$ and $B$ in the country, there exist a long path and a short path between them that have no cities in common (except $A$ and $B$). For a given $n$, find all possible numbers of flights in the country.



## 2025 — N3

**Record:** `bmo_2025_75a6a6`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_75a6a6.json.gz).

Given a positive integer $k$, a pair of positive integers $(a, b)$ is said to be $k$-nice if $a \mid b^k + 1$ and $b \mid a^k + 1$. For which positive integers $k$ are there infinitely many $k$-nice pairs?



## 2025 — C2

**Record:** `bmo_2025_8bfc7d`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_8bfc7d.json.gz).

A graph is *good* if its edges can be colored with 2 colors so that no cycle has two consecutive edges of the same color. What is the maximum number of edges in a *good* graph with 1000 vertices?



## 2025 — C4

**Record:** `bmo_2025_a483fd`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_a483fd.json.gz).

A social network has $2025$ users. Two different users are either friends or not friends. A user is considered *lonely* if they have no friends. Initially, there are no lonely users, and two users Alice and Bob are not friends. A user may swap all their friends, meaning if they were friends with someone before the swap, they are no longer friends, and vice versa. Must there exist a way to arrange the $2025$ users in a sequence so that if, one-by-one in that sequence, each user swaps their friends, no user is ever lonely at any point during the process?



## 2025 — C1

**Record:** `bmo_2025_b27827`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_b27827.json.gz).

Consider a table with $m$ rows and 22 columns. Each cell is filled with a number from the set $A = \{1, 2, 3, \dots, 2025\}$ (numbers may be repeated), such that for every pair of distinct numbers in $A$, there exists a row that contains exactly one of these two numbers. Find the minimum value of $m$.



## 2025 — C5

**Record:** `bmo_2025_d22b64`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2025_d22b64.json.gz).

Let $n$ and $m$ be positive integers with $n \ge 2$. There are $n$ piles having $a_1, \dots, a_n$ stones such that for each $1 \le i \le n$ we have $m \le a_i \le m \cdot i$ (so $a_1 = m$). Aida and Bob play the following game: on each round, Bob picks two non-empty piles (if possible) and he removes a number of stones from the pile with fewer stones (in the case of equality, he chooses randomly). Then Aida decides whether she removes the same number of stones from the other pile or she moves the stones Bob just removed to the other pile. If there is at most one non-empty pile, the game ends.
Find the smallest positive integer $k$ such that Aida can guarantee that at some point there will be at most $k$ stones, regardless of the sequence $a_1, \dots, a_n$ and of how Bob plays.



# CMO-China


## 2022 — 6

**Record:** `chn_2022_4f6805`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_4f6805.json.gz).

There are some direct one-way flights among $n \ge 8$ airports. Between any two airports $a$ and $b$, there is at most one direct one-way flight from $a$ to $b$ (it is possible to have direct one-way flights both from $a$ to $b$ and from $b$ to $a$). Suppose that, for any set $A$ consisting of some airports with $1 \le |A| \le n-1$, there are at least $4 \cdot \min\{|A|, n-|A|\}$ flights in total departing from the airports in $A$ and arriving at the airports not in $A$.
Prove that for any airport $x$, one can depart from $x$ and take no more than $\sqrt{2n}$ flights to return to $x$.



## 2022 — 3

**Record:** `chn_2022_aece1e`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_aece1e.json.gz).

Fix two positive integers $m$ and $n$. Fix a way to color the vertices of a regular $(2m+2n)$-gon so that $2m$ of them are black and the other $2n$ are white. Define the coloring distance $d(B, C)$ between two black points $B$ and $C$ to be the lesser of the numbers of white points on either side of the line $BC$; similarly, define the coloring distance $d(W, X)$ between two white points $W$ and $X$ to be the lesser of the numbers of black points on either side of the line $WX$.
A black pairing scheme $\mathcal{B}$ means to label the $2m$ black points as $B_1, \dots, B_m, C_1, \dots, C_m$, such that no two segments from $B_1C_1, \dots, B_mC_m$ intersect each other. For each such $\mathcal{B}$, put
$$
P(\mathcal{B}) = \sum_{i=1}^{m} d(B_i, C_i).
$$
A white pairing scheme $\mathcal{W}$ means to label the $2n$ white points as $W_1, \dots, W_n, X_1, \dots, X_n$, such that no two segments from $W_1X_1, \dots, W_nX_n$ intersect each other. For each such $\mathcal{W}$, put
$$
P(\mathcal{W}) = \sum_{i=1}^{n} d(W_i, X_i).
$$
Prove that, regardless of how the $2m+2n$ vertices are colored, we always have
$$
\max_{\mathcal{B}} P(\mathcal{B}) = \max_{\mathcal{W}} P(\mathcal{W}),
$$
where the maxima are taken over all possible black pairing schemes and all possible white pairing schemes, respectively.



## 2023 — 4

**Record:** `chn_2023_0ba7d6`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_0ba7d6.json.gz).

Let $a_1, a_2, \dots, a_{2023}$ be nonnegative real numbers such that $a_1 + a_2 + \dots + a_{2023} = 100$. Let $N$ denote the number of elements in the following set
$$
\{(i, j) \mid 1 \le i \le j \le 2023, a_i a_j \ge 1\}.
$$
Prove that $N \le 5050$, and determine the necessary and sufficient condition for $N = 5050$.



## 2023 — 6

**Record:** `chn_2023_422c39`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_422c39.json.gz).

A *state* refers to a way to place the numbers $1, 2, \ldots, 99$ on the vertices of a given regular $99$-gon, with exactly one number on each vertex and every number appearing exactly once. Two states are considered *equivalent* if one of them can be obtained from the other by rotating the regular $99$-gon (on the plane).

An *operation* is to first choose two adjacent vertices of the regular $99$-gon and then exchange the numbers on these two vertices. Determine the smallest positive integer $N$ such that, for any two states $\alpha$ and $\beta$, one may apply no more than $N$ operations to $\alpha$ to obtain a state that is equivalent to $\beta$.



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



# China-TST


## 2014 — 2

**Record:** `chn_2014_1d410b`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2014_1d410b.json.gz).

Let $A_1A_2\cdots A_{101}$ be a regular 101-gon, and color every vertex red or blue. Let $N$ be the number of obtuse triangles satisfying the following: The three vertices of the triangle must be vertices of the 101-gon, both the vertices with acute angles have the same color, and the vertex with obtuse angle have different color.

(1) Find the largest possible value of $N$.

(2) Find the number of ways to color the vertices such that maximum $N$ is achieved. (Two colorings are different if for some $A_i$ the colors are different on the two coloring schemes)



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



## 2021 — 1

**Record:** `chn_2021_376391`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_376391.json.gz).

Given a convex $n$-gon ($n \ge 5$) $\Omega: P_1P_2...P_n$, of which no three diagonals are concurrent inside $\Omega$. Prove that one can choose a point inside every quadrilateral $P_iP_jP_kP_l$ ($1 \le i < j < k < l \le n$) and not on any diagonal of $\Omega$, such that the $C_n^4$ points obtained are distinct and the segment connecting any two of them intersects with at least one diagonal of $\Omega$.
(Contributed by Leng Fusheng)



## 2021 — 1

**Record:** `chn_2021_4e9786`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_4e9786.json.gz).

Given integer $n \ge 2$. Find the least positive integer $m$, such that there are $n^2$ distinct positive real numbers $x_{i,j}$ ($1 \le i, j \le n$) satisfying the following conditions:
(1) For every $i, j$,
$$
x_{i,j} = \max\{x_{i,1}, x_{i,2}, \dots, x_{i,j}\} \text{ or}
$$
$$
x_{i,j} = \max\{x_{1,j}, x_{2,j}, \dots, x_{i,j}\};
$$
(2) For every $i$, there are at most $m$ indices $k$, with
$$
x_{i,k} = \max\{x_{i,1}, x_{i,2}, \dots, x_{i,k}\};
$$
(3) For every $j$, there are at most $m$ indices $k$, with
$$
x_{k,j} = \max\{x_{1,j}, x_{2,j}, \dots, x_{k,j}\}.
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



## 2021 — 2

**Record:** `chn_2021_85d786`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_85d786.json.gz).

Given $2021$ distinct positive integers $a_1, a_2, \dots, a_{2021}$. Define the sequence $\{a_n\}$ inductively as follows: for each integer $n \ge 2022$, $a_n$ is the smallest positive integer different from $a_1, a_2, \dots, a_{n-1}$ and not dividing the product $a_{n-1}a_{n-2}\dots a_{n-2021}$. Prove: there exists a positive integer $M$, such that all integers greater than or equal to $M$ appear in $\{a_n\}$.



## 2021 — 2

**Record:** `chn_2021_a11094`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_a11094.json.gz).

Given positive integers $n$ and $k$, $n > k^2 > 4$. In an $n \times n$ grid, any $k$ squares in distinct rows and distinct columns are called a $k$-set. Find the largest positive integer $N$ satisfying that: one can choose $N$ squares of the $n \times n$ grid and colour them in a certain way, such that for any coloured $k$-set, some two squares have the same colour, and some two squares have different colours.



## 2021 — 3

**Record:** `chn_2021_ab96ca`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_ab96ca.json.gz).

Let $S(k)$ denote the sum of all digits of $k$ in base 10. Find all integers $n \ge 2$ and rational numbers $\beta \in (0,1)$, such that there exist $n$ distinct positive integers $a_1, a_2, \dots, a_n$ that satisfy: for any subset $I \subseteq \{1, 2, \dots, n\}$ with two or more elements,
$$ S\left(\sum_{i \in I} a_i\right) = \beta \cdot \sum_{i \in I} S(a_i). $$



## 2021 — 6

**Record:** `chn_2021_cb4abc`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_cb4abc.json.gz).

Prove that there exists a constant $\lambda > 0$, such that: for any positive integer $m$, in the rectangular coordinates system, if all vertices of $\triangle ABC$ are integral points, and there is a unique interior (not on the side) integral point whose $x$ and $y$ coordinates are multiples of $m$, then the area of $\triangle ABC$ is less than $\lambda m^3$.

(Contributed by Wang Bin and Fu Yunhao)



## 2021 — 5

**Record:** `chn_2021_d4b623`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_d4b623.json.gz).

Let $n$ be a positive integer, $a_1, a_2, \dots, a_{2n+1}$ be $2n+1$ positive real numbers. For $k = 1, 2, \dots, 2n+1$, define
$$
b_k = \max_{0 \le m \le n} \left( \frac{1}{2m+1} \sum_{i=k-m}^{k+m} a_i \right),
$$
where the subscript of $a_i$ is taken modulo $2n+1$. Prove: the number of subscripts $k$ satisfying that $b_k \ge 1$ does not exceed $2 \sum_{i=1}^{2n+1} a_i$.



## 2021 — 2

**Record:** `chn_2021_e6f1e7`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_e6f1e7.json.gz).

Given positive integers $k$ and $n$ ($n \ge 2$), find the minimum constant $c$ satisfying this assertion: if $G$ is a simple $kn$-regular graph (the degree of each vertex is $kn$) with $m$ vertices, then each vertex can be coloured one of $n$ colours, such that the number of “mono edges” is at most $cm$. Here, a mono edge is an edge incident to two vertices of the same colour.



## 2021 — 5

**Record:** `chn_2021_fd4121`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2021_fd4121.json.gz).

Find the smallest real number $\alpha$, such that for any convex polygon $P$ of area $1$, there exists a point $M$ in the plane, such that the area of the convex hull of $P \cup Q$ is at most $\alpha$, where $Q$ is the central-symmetric figure of $P$ about $M$.
(Contributed by Qu Zhenhua and Wu Yuchi)



## 2022 — 1

**Record:** `chn_2022_01f5d7`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_01f5d7.json.gz).

On a screen formed by $n \times n$ ($n \ge 2$) squares, every square displays initially one of the three colors: red, yellow, and blue. Every second, the screen changes the color of each square following the rules below:
* for each square $A$ whose current color is red, if there is a yellow square sharing a side with this square, then $A$ turns yellow in the next second, otherwise, $A$ remains red;
* for each square $B$ whose current color is yellow, if there is a blue square sharing a side with this square, then $B$ turns blue in the next second, otherwise, $B$ remains yellow;
* for each square $C$ whose current color is blue, if there is a red square sharing a side with this square, then $C$ turns red in the next second, otherwise, $C$ remains blue.
Prove that if the screen does not change to a single color after $2n - 2$ seconds, then it will never change to a single color.



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



## 2022 — 2

**Record:** `chn_2022_4d5044`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_4d5044.json.gz).

Given a prime number $p$ and an infinite set $A \subset \mathbb{Z}$. Show that one can always find a subset $B$ of $A$, $B$ contains $2p-2$ elements, and for any $p$ distinct elements of $B$, their arithmetic mean does not belong to $A$.

(Contributed by Fu Yunhao)



## 2022 — 3

**Record:** `chn_2022_514503`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_514503.json.gz).

Find all functions $f: \mathbb{R} \to \mathbb{R}$ such that, for any real numbers $x, y$, the following two multisets are equal
$$
\{f(xf(y) + 1), f(yf(x) - 1)\} = \{xf(f(y)) - 1, yf(f(x)) + 1\}.
$$

*Remark: $\{a, b\} = \{c, d\}$ are equal as multisets if $a = c$ and $b = d$, or $a = d$ and $b = c$.*



## 2022 — 3

**Record:** `chn_2022_588922`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_588922.json.gz).

Given positive integers $a, b, c, p, q, r$, where $p, q, r \ge 2$. Let $Q = \{(x, y, z) \in \mathbb{Z}^3 \mid 0 \le x \le a, 0 \le y \le b, 0 \le z \le c\}$ be the game board.

Initially, put $M$ game pieces on $Q$ (no restriction on the number of pieces in each position). There are three types of legal moves:

(1) Remove $p$ pieces from $(x, y, z)$ and place one piece at $(x-1, y, z) \in Q$;

(2) Remove $q$ pieces from $(x, y, z)$ and place one piece at $(x, y-1, z) \in Q$;

(3) Remove $r$ pieces from $(x, y, z)$ and place one piece at $(x, y, z-1) \in Q$.

Find the minimum value of $M$, such that no matter how the $M$ game pieces are placed initially, one can always take a sequence of moves to get one piece placed at $(0, 0, 0)$.



## 2022 — 6

**Record:** `chn_2022_f8505c`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_f8505c.json.gz).

Let $m$ be a positive integer and $A$ be a finite set. Let $A_1, A_2, \dots, A_m$ be subsets of $A$ (not necessarily distinct). It is known that for any nonempty set $I \subseteq \{1, 2, \dots, m\}$,
$$
\left| \bigcup_{i \in I} A_i \right| \geq |I| + 1.
$$

Prove: the elements of $A$ can be coloured black or white, such that every of $A_1, A_2, \dots, A_m$ contains both black and white elements.



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



## 2023 — 6

**Record:** `chn_2023_e1b280`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_e1b280.json.gz).

Given a positive integer $n$, find the smallest positive integer $k$ with the following property: After coloring any $k$ unit squares black and the remaining squares white in a $2n \times 2n$ grid, it is always possible to make all squares black using a finite number of the following two operations:

(Operation 1) Select a $2 \times 2$ square that contains exactly 3 black squares and 1 white square, and change the color of the white square to black.

(Operation 2) Select a $2 \times 2$ square that contains exactly 2 black squares and 2 white squares, and change the color of all squares within the square (black squares become white, and white squares become black).

*Note*: The same $2 \times 2$ square can be operated on multiple times, and each square can change color multiple times.



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



## 2025 — Problem 10

**Record:** `chn_2025_d8572e`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_d8572e.json.gz).

Given an odd integer $n \ge 3$ and a regular $n$-gon with vertex set $V$, let $\mathcal{P}$ denote the set of all regular polygons with vertices in $V$. For example, if $n = 15$, then $\mathcal{P}$ includes 1 regular 15-gon, 3 regular pentagons, and 5 equilateral triangles.

Two players, Alice and Bob, play the following game. Initially, all points in $V$ are uncolored. Alice moves first, and they take turns coloring an uncolored point in $V$: Alice colors red, and Bob colors blue. The game ends when all points are colored. A polygon in $\mathcal{P}$ is called **red-dominated** if it has more red vertices than blue ones.

Find the largest integer $k$ such that, no matter how Bob plays, Alice can guarantee at least $k$ red-dominated polygons in $\mathcal{P}$ at the end.



# EGMO


## 2012 — Problem 2.

**Record:** `egm_2012_2d1fb4`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2012_2d1fb4.json.gz).

Let $n$ be a positive integer. Find the greatest possible integer $m$, in terms of $n$, with the following property: a table with $m$ rows and $n$ columns can be filled with real numbers in such a manner that for any two different rows $[a_{1}, a_{2}, \ldots, a_{n}]$ and $[b_{1}, b_{2}, \ldots, b_{n}]$ the following holds:
$$
\max \left(\left|a_{1}-b_{1}\right|,\left|a_{2}-b_{2}\right|, \ldots,\left|a_{n}-b_{n}\right|\right)=1
$$



## 2012 — Problem 6

**Record:** `egm_2012_5667e3`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2012_5667e3.json.gz).

There are infinitely many people registered on the social network Mugbook. Some pairs of (different) users are registered as friends, but each person has only finitely many friends. Every user has at least one friend. (Friendship is symmetric; that is, if $A$ is a friend of $B$, then $B$ is a friend of $A$.)

Each person is required to designate one of their friends as their best friend. If $A$ designates $B$ as her best friend, then (unfortunately) it does not follow that $B$ necessarily designates $A$ as her best friend. Someone designated as a best friend is called a 1-best friend. More generally, if $n>1$ is a positive integer, then a user is an $n$-best friend provided that they have been designated the best friend of someone who is an $(n-1)$-best friend. Someone who is a $k$-best friend for every positive integer $k$ is called popular.

a. Prove that every popular person is the best friend of a popular person.

b. Show that if people can have infinitely many friends, then it is possible that a popular person is not the best friend of a popular person.



## 2012 — Problem 8

**Record:** `egm_2012_684025`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2012_684025.json.gz).

A word is a finite sequence of letters from some alphabet. A word is repetitive if it is a concatenation of at least two identical subwords (for example, $a b a b a b$ and $a b c a b c$ are repetitive, but $a b a b a$ and $a a b b$ are not). Prove that if a word has the property that swapping any two adjacent letters makes the word repetitive, then all its letters are identical. (Note that one may swap two adjacent identical letters, leaving a word unchanged.)



## 2012 — Problem 4.

**Record:** `egm_2012_b764d7`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2012_b764d7.json.gz).

A set $A$ of integers is called sum-full if $A \subseteq A+A$, i.e. each element $a \in A$ is the sum of some pair of (not necessarily different) elements $b, c \in A$. A set $A$ of integers is said to be zero-sum-free if $0$ is the only integer that cannot be expressed as the sum of the elements of a finite nonempty subset of $A$.

Does there exist a sum-full zero-sum-free set of integers?



## 2012 — Problema 2

**Record:** `rou_2012_cf5e45`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2012_cf5e45.json.gz).

Fie $n$ un număr întreg strict pozitiv. Determinaţi cel mai mare număr întreg $m$ cu proprietatea că un tablou cu $m$ linii şi $n$ coloane poate fi umplut cu numere reale în aşa fel încât pentru oricare două linii diferite $[a_{1}, a_{2}, \ldots, a_{n}]$ si $[b_{1}, b_{2}, \ldots, b_{n}]$ următoarea relaţie este adevărată
$$
\max \left(\left|a_{1}-b_{1}\right|,\left|a_{2}-b_{2}\right|, \ldots,\left|a_{n}-b_{n}\right|\right)=1
$$



## 2012 — Problema 8

**Record:** `rou_2012_e2ccd4`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2012_e2ccd4.json.gz).

Un cuvânt este o secvenţă finită de litere dintr-un anume alfabet. Un cuvânt se zice repetitiv dacă este o concatenare de cel puţin două sub-cuvinte identice (de exemplu, $ababab$ şi $abcabc$ sunt repetitive, dar $ababa$ şi $aabb$ nu sunt). Demonstraţi că dacă un cuvânt are proprietatea că orice transpoziţie a două litere adiacente îl transformă într-un cuvânt repetitiv, atunci toate literele sale sunt identice. (O transpoziţie a două litere adiacente identice, care lasă cuvântul neschimbat, este şi ea a fi considerată.)



## 2012 — Problema 4

**Record:** `rou_2012_f18db0`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2012_f18db0.json.gz).

O mulţime $A$ de numere întregi se zice sumă-plină dacă $A \subseteq A+A$, adică orice element $a \in A$ este suma unei perechi (nu neapărat unice) de elemente (nu neapărat distincte) $b, c \in A$. O mulţime $A$ de numere întregi se zice liberă-de-sume-zero dacă $0$ este singurul număr întreg care nu poate fi exprimat ca suma elementelor unei submulţimi finite nevide a lui $A$.
Există oare o muļime sumă-plină liberă-de-sume-zero de numere întregi?



## 2012 — Problema 6

**Record:** `rou_2012_f9e615`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2012_f9e615.json.gz).

Un număr infinit de persoane sunt înregistrate ca useri pe reţeaua socială Mutrăbook. Unele perechi de useri (diferiţi) sunt înregistrate ca prieteni, dar fiecare persoană are cel mult un număr finit de prieteni. Fiecare user are cel puţin un prieten. (Relaţia de prietenie este simetrică; dacă $A$ este prieten cu $B$, atunci şi $B$ este prieten cu $A$.)

Fiecare persoană trebuie să-şi desemneze unul dintre prieteni ca fiind cel-mai-bun-prieten. Dacă $A$ îl desemnează pe $B$ ca cel-mai-bun-prieten, nu urmează (din păcate) în mod necesar că şi $B$ l-a desemnat pe $A$ ca cel-mai-bun-prieten. Cineva desemnat ca cel-mai-bun-prieten este numit 1-cel-mai-bun-prieten. În general, dacă $n>1$ este un număr întreg pozitiv, atunci un user este un $n$-cel-mai-bun-prieten dacă a fost desemnat ca cel-mai-bun-prieten de către cineva care este el însuşi un $(n-1)$-cel-mai-bun-prieten. O persoană care este un $k$-cel-mai-bun-prieten pentru toate numerele întregi pozitive $k$ este numită populară.

a. Demonstraţi că fiecare persoană populară este cel-mai-bun-prieten al (măcar) unei alte persoane populare.

b. Demonstraţi că dacă persoanele ar fi putut avea infinit de mulţi prieteni, atunci ar fi fost posibil ca o persoană populară să nu fi fost cel-mai-bun-prieten al niciunei alte persoane populare.



## 2013 — Problem 2.

**Record:** `egm_2013_35d4e6`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2013_35d4e6.json.gz).

Determine all integers $m$ for which the $m \times m$ square can be dissected into five rectangles, the side lengths of which are the integers $1,2,3, \ldots, 10$ in some order.



## 2013 — Problem 3.

**Record:** `egm_2013_6d183f`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2013_6d183f.json.gz).

Let $n$ be a positive integer.

a. Prove that there exists a set $S$ of $6 n$ pairwise different positive integers, such that the least common multiple of any two elements of $S$ is no larger than $32 n^{2}$.

b. Prove that every set $T$ of $6 n$ pairwise different positive integers contains two elements the least common multiple of which is larger than $9 n^{2}$.



## 2013 — Problem 6.

**Record:** `egm_2013_a2b3b6`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2013_a2b3b6.json.gz).

Snow White and the Seven Dwarves are living in their house in the forest. On each of 16 consecutive days, some of the dwarves worked in the diamond mine while the remaining dwarves collected berries in the forest. No dwarf performed both types of work on the same day. On any two different (not necessarily consecutive) days, at least three dwarves each performed both types of work. Further, on the first day, all seven dwarves worked in the diamond mine.

Prove that, on one of these 16 days, all seven dwarves were collecting berries.



## 2014 — 4.

**Record:** `egm_2014_0cc86d`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2014_0cc86d.json.gz).

Determine all integers $n \geq 2$ for which there exist integers $x_{1}, x_{2}, \ldots, x_{n-1}$ satisfying the condition that if $0 < i < n$, $0 < j < n$, $i \neq j$ and $n$ divides $2i + j$, then $x_{i} < x_{j}$.



## 2014 — 5.

**Record:** `egm_2014_8fdc8e`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2014_8fdc8e.json.gz).

Let $n$ be a positive integer. We have $n$ boxes where each box contains a nonnegative number of pebbles. In each move we are allowed to take two pebbles from a box we choose, throw away one of the pebbles and put the other pebble in another box we choose. An initial configuration of pebbles is called solvable if it is possible to reach a configuration with no empty box, in a finite (possibly zero) number of moves. Determine all initial configurations of pebbles which are not solvable, but become solvable when an additional pebble is added to a box, no matter which box is chosen.



## 2015 — 2

**Record:** `mkd_2015_b52719`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2015_b52719.json.gz).

A domino is a $2 \times 1$ or $1 \times 2$ tile. Determine in how many exactly $n^2$ dominoes can be placed without overlapping on a $2n \times 2n$ chessboard so that every $2 \times 2$ square contains at least two uncovered unit squares which lie in the same row or column.



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



## 2016 — Problem 3.

**Record:** `rou_2016_9a4499`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2016_9a4499.json.gz).

Let $m$ be a positive integer. Consider a $4m \times 4m$ array of square unit cells. Two different cells are *related* to each other if they are in either the same row or in the same column. No cell is related to itself. Some cells are colored blue, such that every cell is related to at least two blue cells. Determine the minimum number of blue cells.



## 2016 — Problem 5.

**Record:** `rou_2016_9aa109`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2016_9aa109.json.gz).

Let $k$ and $n$ be integers such that $k \ge 2$ and $k \le n \le 2k-1$. Place rectangular tiles, each of size $1 \times k$ or $k \times 1$, on an $n \times n$ chessboard so that each tile covers exactly $k$ cells, and no two tiles overlap. Do this until no further tile can be placed in this way. For each such $k$ and $n$, determine the minimum number of tiles that such an arrangement may contain.



## 2018 — Problem 3

**Record:** `egm_2018_c41bdb`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2018_c41bdb.json.gz).

The $n$ contestants of an EGMO are named $C_{1}, \ldots, C_{n}$. After the competition they queue in front of the restaurant according to the following rules.
- The Jury chooses the initial order of the contestants in the queue.
- Every minute, the Jury chooses an integer $i$ with $1 \leq i \leq n$.
- If contestant $C_{i}$ has at least $i$ other contestants in front of her, she pays one euro to the Jury and moves forward in the queue by exactly $i$ positions.
- If contestant $C_{i}$ has fewer than $i$ other contestants in front of her, the restaurant opens and the process ends.

a. Prove that the process cannot continue indefinitely, regardless of the Jury's choices.

b. Determine for every $n$ the maximum number of euros that the Jury can collect by cunningly choosing the initial order and the sequence of moves.

(Hungary)



## 2020 — Problem 4

**Record:** `egm_2020_d0be5e`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2020_d0be5e.json.gz).

A permutation of the integers $1,2, \ldots, m$ is called fresh if there exists no positive integer $k < m$ such that the first $k$ numbers in the permutation are $1,2, \ldots, k$ in some order. Let $f_{m}$ be the number of fresh permutations of the integers $1,2, \ldots, m$.

Prove that $f_{n} \geq n \cdot f_{n-1}$ for all $n \geq 3$.

For example, if $m=4$, then the permutation $(3,1,4,2)$ is fresh, whereas the permutation $(2,3,1,4)$ is not.



## 2023 — Problem 3

**Record:** `egm_2023_3c6e1c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2023_3c6e1c.json.gz).

Let $k$ be a positive integer. Lexi has a dictionary $\mathcal{D}$ consisting of some $k$-letter strings containing only the letters $A$ and $B$. Lexi would like to write either the letter $A$ or the letter $B$ in each cell of a $k \times k$ grid so that each column contains a string from $\mathcal{D}$ when read from top-to-bottom and each row contains a string from $\mathcal{D}$ when read from left-to-right.
What is the smallest integer $m$ such that if $\mathcal{D}$ contains at least $m$ different strings, then Lexi can fill her grid in this manner, no matter what strings are in $\mathcal{D}$ ?



## 2023 — Problem 5

**Record:** `egm_2023_fc0b21`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2023_fc0b21.json.gz).

We are given a positive integer $s \geqslant 2$. For each positive integer $k$, we define its twist $k^{\prime}$ as follows: write $k$ as $a s+b$, where $a, b$ are non-negative integers and $b<s$, then $k^{\prime}=b s+a$. For the positive integer $n$, consider the infinite sequence $d_{1}, d_{2}, \ldots$ where $d_{1}=n$ and $d_{i+1}$ is the twist of $d_{i}$ for each positive integer $i$.
Prove that this sequence contains 1 if and only if the remainder when $n$ is divided by $s^{2}-1$ is either 1 or $s$.



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



## 2025 — P2.

**Record:** `egm_2025_23b350`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2025_23b350.json.gz).

An infinite increasing sequence $a_{1} < a_{2} < a_{3} < \dots$ of positive integers is called central if for every positive integer $n$, the arithmetic mean of the first $a_{n}$ terms of the sequence is equal to $a_{n}$.  
Show that there exists an infinite sequence $b_{1}, b_{2}, b_{3}, \ldots$ of positive integers such that for every central sequence $a_{1}, a_{2}, a_{3}, \ldots$, there are infinitely many positive integers $n$ with $a_{n} = b_{n}$.



## 2025 — P6.

**Record:** `egm_2025_af59a0`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2025_af59a0.json.gz).

In each cell of a $2025 \times 2025$ board, a nonnegative real number is written in such a way that the sum of the numbers in each row is equal to $1$, and the sum of the numbers in each column is equal to $1$. Define $r_{i}$ to be the largest value in row $i$, and let $R = r_{1} + r_{2} + \dots + r_{2025}$. Similarly, define $c_{i}$ to be the largest value in column $i$, and let $C = c_{1} + c_{2} + \dots + c_{2025}$. What is the largest possible value of $\frac{R}{C}$?

What is the largest possible value of $\frac{R}{C}$?



## 2025 — P5.

**Record:** `egm_2025_b50ee2`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/european-girls-mathematical-olympiad-egmo/egm_2025_b50ee2.json.gz).

Let $n > 1$ be an integer. In a configuration of an $n \times n$ board, each of the $n^{2}$ cells contains an arrow, either pointing up, down, left, or right. Given a starting configuration, Turbo the snail starts in one of the cells of the board and travels from cell to cell. In each move, Turbo moves one square unit in the direction indicated by the arrow in her cell (possibly leaving the board). After each move, the arrows in all of the cells rotate $90^{\circ}$ counterclockwise. We call a cell good if, starting from that cell, Turbo visits each cell of the board exactly once, without leaving the board, and returns to her initial cell at the end. Determine, in terms of $n$, the maximum number of good cells over all possible starting configurations.



# IMO


## 1983 — 5.

**Record:** `esp_1983_4d889d`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_1983_4d889d.json.gz).

Decir si es posible elegir $1983$ enteros positivos distintos, todos menores o iguales que $10^{5}$, de forma que tres cualesquiera de ellos no sean términos consecutivos de una progresión aritmética. Justificar la respuesta.



## 1983 — 4.

**Record:** `esp_1983_f5c138`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_1983_f5c138.json.gz).

Sea $ABC$ un triángulo equilátero, y $\mathcal{E}$ el conjunto de todos los puntos contenidos en los tres segmentos $AB$, $BC$ y $CA$ (con $A$, $B$ y $C$ incluidos). Determinar si es cierto que para cada partición de $\mathcal{E}$ en dos conjuntos disjuntos, por lo menos uno de los dos conjuntos contiene los vértices de un triángulo rectángulo. Justificar la respuesta.



## 1984 — 3.

**Record:** `esp_1984_25d462`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_1984_25d462.json.gz).

Tenemos en el plano dos puntos diferentes, $A$ y $O$. Para cada punto $X$ del plano distinto de $O$, denotamos por $\alpha(X)$ la medida del ángulo entre $OA$ y $OX$, en radianes, y contado en sentido antihorario desde $OA$ $(0 \leq \alpha(X)<2\pi)$.

Sea $C(X)$ la circunferencia de centro $O$ y radio de longitud $OX + \frac{\alpha(X)}{OX}$. Tenemos un número finito de colores y coloreamos cada uno de los puntos del plano con ellos.

Demostrar que existe un punto $Y$ tal que $\alpha(Y)>0$ y tal que su color aparece sobre la circunferencia de $C(Y)$.



## 1984 — 5.

**Record:** `esp_1984_28162f`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_1984_28162f.json.gz).

Sea $d$ la suma de las longitudes de todas las diagonales de un polígono convexo plano de $n$ vértices $(n>3)$, y sea $p$ su perímetro. Demostrar que
$$
n-3<\frac{2d}{p}<\left[\frac{n}{2}\right]\left[\frac{n+1}{2}\right]-2
$$
siendo $[x]$ la parte entera de $x$.



## 1985 — 2.

**Record:** `esp_1985_31cbd9`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_1985_31cbd9.json.gz).

Sean $n$ y $k$ dos números naturales primos entre sí, con $0 < k < n$. Cada número del conjunto $\mathcal{M} = \{1, 2, \ldots, n-1\}$ se colorea o bien en azul, o bien en blanco. Se sabe que

1) Para cada $i \in \mathcal{M}$, los elementos $i$ y $n-i$ tienen el mismo color.

2) Para cada $i \in \mathcal{M}$, $i \neq k$, los elementos $i$ y $|i-k|$ tienen el mismo color.

Demostrar que todos los elementos de $\mathcal{M}$ tienen el mismo color.



## 1985 — 4.

**Record:** `esp_1985_417bfe`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_1985_417bfe.json.gz).

Sea $\mathcal{M}$ un conjunto de 1985 enteros positivos distintos, ninguno de los cuales tiene divisores primos mayores que 26. Demostrar que $\mathcal{M}$ contiene como mínimo un subconjunto de cuatro elementos distintos, cuyo producto es la cuarta potencia de un entero.



## 1985 — 3.

**Record:** `esp_1985_e6ffa9`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_1985_e6ffa9.json.gz).

Dado un polinomio $P(x)=a_{0}+a_{1} x+a_{2} x^{2}+\cdots+a_{k} x^{k}$ con coeficientes enteros, denotamos por $w(P)$ el número de coeficientes impares de $P$. Sea $Q_{i}(x)=(1+x)^{i}$, para $i=0,1, \ldots$ Demostrar que si $i_{1}, i_{2}, \ldots, i_{n}$ son enteros tales que $0 \leq i_{1}<i_{2}<\cdots<i_{n}$, entonces
$$
w\left(Q_{i_{1}}+Q_{i_{2}}+\cdots+Q_{i_{n}}\right) \geq w\left(Q_{i_{1}}\right)
$$



## 1986 — 6.

**Record:** `esp_1986_636219`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_1986_636219.json.gz).

Tenemos un conjunto finito de puntos del plano, cada uno con coordenadas enteras. Se pregunta si es posible colorear algunos puntos del conjunto en rojo y los restantes en blanco de forma que toda recta $L$ paralela a uno de los ejes de coordenadas contenga puntos rojos y blancos en cantidades cuya diferencia en valor absoluto sea 1 como máximo. Justificar la respuesta.



## 1986 — 3.

**Record:** `esp_1986_ae2a34`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_1986_ae2a34.json.gz).

A cada vértice de un pentágono le asignamos un número entero, de forma que la suma de los cinco enteros sea positiva. Si tres vértices consecutivos tienen números asignados $x, y, z$, respectivamente, y es $y<0$, entonces se permite hacer la siguiente operación: los números $x, y, z$ se sustituyen respectivamente por $x+y$, $-y$, $z+y$. Esta operación se puede hacer repetidamente mientras al menos uno de los cinco números sea negativo. Determinar si este proceso acaba necesariamente con un número finito de pasos.



## 1987 — 1.

**Record:** `esp_1987_575956`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_1987_575956.json.gz).

Sea $p_{n}(k)$ el número de permutaciones del conjunto $\{1,2, \ldots, n\}$, $n \geq 1$, que tienen exactamente $k$ puntos fijos. Demostrar que
$$
\sum_{k=0}^{n} k p_{n}(k) = n!
$$

(Nota: Una permutación $f$ de un conjunto $S$ es una aplicación biyectiva de $S$ sobre sí mismo. Un elemento $i$ de $S$ se llama punto fijo de la permutación $f$ si $f(i) = i$.)



## 1987 — 3.

**Record:** `esp_1987_ac6655`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_1987_ac6655.json.gz).

Sean $x_{1}, x_{2}, \ldots, x_{n}$, números reales que cumplen $x_{1}^{2}+x_{2}^{2}+\cdots+x_{n}^{2}=1$. Demostrar que para cada entero $k \geq 2$ existen enteros no todos nulos $a_{1}, a_{2}, \ldots, a_{n}$, tales que $\left|a_{i}\right| \leq k-1$ para todo $i$ y
$$
\left|a_{1} x_{1}+a_{2} x_{2}+\cdots+a_{n} x_{n}\right| \leq \frac{(k-1) \sqrt{n}}{k^{n}-1}
$$



## 2005 — 2

**Record:** `usa_2005_9b3d8f`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2005_9b3d8f.json.gz).

Let $a_1, a_2, \dots$ be a sequence of integers with infinitely many positive and infinitely many negative terms. Suppose that for each positive integer $n$, the numbers $a_1, a_2, \dots, a_n$ leave distinct remainders upon division by $n$. Prove that every integer occurs exactly once in the sequence.



## 2006 — 2

**Record:** `usa_2006_d819ea`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2006_d819ea.json.gz).

Let $\mathcal{P}$ be a regular 2006-gon. A diagonal of $\mathcal{P}$ is called *good segment* if its endpoints divide the boundary of $\mathcal{P}$ into two parts, each composed of an odd number of sides of $\mathcal{P}$. The sides of $\mathcal{P}$ are also called *good segment*.
Suppose $\mathcal{P}$ has been dissected into triangles by 2003 diagonals, no two of which have a common point in the interior of $\mathcal{P}$. Find the maximum number of isosceles triangles having two *good segments* that could appear in such a configuration.



## 2009 — 6

**Record:** `usa_2009_171772`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2009_171772.json.gz).

Let $a_1, a_2, \dots, a_n$ be distinct positive integers and let $M$ be a set of $n-1$ positive integers not containing $s = a_1 + a_2 + \dots + a_n$. A grasshopper is to jump along the real axis, starting at the point $0$ and making $n$ jumps to the right with lengths $a_1, a_2, \dots, a_n$ in some order. Prove that the order can be chosen in such a way that the grasshopper never lands on any point in $M$.

(The original version of this problem was suggested by Dmitry Khramtsov from Russian Federation.
The current version was strengthened by Christian Reiher from Germany.)



## 2009 — 5

**Record:** `usa_2009_ed888c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2009_ed888c.json.gz).

Determine all functions $f$ from the set of positive integers to the set of positive integers such that, for all positive integers $a$ and $b$, there exists a non-degenerate triangle with sides of lengths $a$, $f(b)$ and $f(b+f(a)-1)$.



## 2013 — 6

**Record:** `esp_2013_8adf5f`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_2013_8adf5f.json.gz).

Sea $n \ge 3$ un número entero. Se considera una circunferencia en la que se han marcado $n+1$ puntos igualmente espaciados. Cada punto se etiqueta con uno de los números $0, 1, \dots, n$ de manera que cada número se usa exactamente una vez. Dos distribuciones de etiquetas se consideran la misma si una se puede obtener de la otra por una rotación de la circunferencia. Una distribución de etiquetas se llama bonita si, para cualesquiera cuatro etiquetas $a < b < c < d$, con $a + d = b + c$, la cuerda que une los puntos etiquetados $a$ y $d$ no corta la cuerda que une los puntos etiquetados $b$ y $c$. Sea $M$ el número de distribuciones bonitas y $N$ el número de pares ordenados $(x, y)$ de enteros positivos tales que $x + y \le n$ y $\text{mcd}(x, y) = 1$. Demostrar que $M = N + 1$.



## 2013 — 2

**Record:** `esp_2013_93e99b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_2013_93e99b.json.gz).

Una configuración de $4027$ puntos del plano, de los cuales $2013$ son rojos y $2014$ azules, y no hay tres de ellos que sean colineales, se llama colombiana. Trazando algunas rectas, el plano queda dividido en varias regiones. Una colección de rectas es buena para una configuración colombiana si se cumplen las dos siguientes condiciones:
* ninguna recta pasa por ninguno de los puntos de la configuración;
* ninguna región contiene puntos de ambos colores.

Hallar el menor valor de $k$ tal que para cualquier configuración colombiana de $4027$ puntos hay una colección buena de $k$ rectas.



## 2014 — 1

**Record:** `esp_2014_460932`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_2014_460932.json.gz).

Sea $a_0 < a_1 < a_2 < \dots$ una sucesión infinita de números enteros positivos.
Demostrar que existe un único entero $n \ge 1$ tal que
$$
a_n < \frac{a_0 + a_1 + a_2 + \dots + a_n}{n} \le a_{n+1}.
$$



## 2014 — 5

**Record:** `esp_2014_b2ff75`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_2014_b2ff75.json.gz).

Para cada entero positivo $n$, el Banco de Ciudad del Cabo produce monedas de valor $\frac{1}{n}$. Dada una colección finita de tales monedas (no necesariamente de distintos valores) cuyo valor total no supera $99 + \frac{1}{2}$, demostrar que es posible separar esta colección en 100 o menos montones, de modo que el valor total de cada montón sea como máximo 1.



## 2014 — 6

**Record:** `esp_2014_c58f52`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_2014_c58f52.json.gz).

Un conjunto de rectas en el plano está en posición general si no hay dos que sean paralelas ni tres que pasen por el mismo punto. Un conjunto de rectas en posición general separa el plano en regiones, algunas de las cuales tienen área finita; a estas las llamamos sus regiones finitas. Demostrar que para cada $n$ suficientemente grande, en cualquier conjunto de $n$ rectas en posición general es posible colorear de azul al menos $\sqrt{n}$ de ellas de tal manera que ninguna de sus regiones finitas tenga todos los lados de su frontera azules.



## 2016 — 2

**Record:** `esp_2016_6b7306`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_2016_6b7306.json.gz).

Hallar todos los enteros positivos $n$ para los que en cada casilla de un tablero $n \times n$ se puede escribir una de las letras I, M y O de manera que:
* en cada fila y en cada columna, un tercio de las casillas tiene I, un tercio tiene M y un tercio tiene O; y
* en cualquier línea diagonal compuesta por un número de casillas divisible por 3, exactamente un tercio de las casillas tienen I, un tercio tiene M y un tercio tiene O.
**Nota:** Las filas y las columnas del tablero $n \times n$ se numeran desde 1 hasta $n$, en su orden natural. Así, cada casilla corresponde a un par de enteros positivos $(i, j)$ con $1 \le i, j \le n$. Para $n > 1$, el tablero tiene $4n - 2$ líneas diagonales de dos tipos. Una línea diagonal del primer tipo se compone de todas las casillas $(i, j)$ para las que $i + j$ es una constante, mientras que una línea diagonal del segundo tipo se compone de todas las casillas $(i, j)$ para las que $i - j$ es una constante.



## 2016 — 6

**Record:** `esp_2016_70968a`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/spain/esp_2016_70968a.json.gz).

Se tienen $n \ge 2$ segmentos en el plano tales que cada par de segmentos se intersecan en un punto interior a ambos, y no hay tres segmentos que tengan un punto en común. Mafalda debe elegir uno de los extremos de cada segmento y colocar sobre él una rana mirando hacia el otro extremo. Luego silbará $n - 1$ veces. En cada silbido, cada rana saltará inmediatamente hacia adelante hasta el siguiente punto de intersección sobre su segmento. Las ranas nunca cambian las direcciones de sus saltos. Mafalda quiere colocar las ranas de tal forma que nunca dos de ellas ocupen al mismo tiempo el mismo punto de intersección.

1. Demostrar que si $n$ es impar, Mafalda siempre puede lograr su objetivo.
2. Demostrar que si $n$ es par, Mafalda nunca logrará su objetivo.



# IMO-SL


## 2006 — N7

**Record:** `imo_2006_2a7e32`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_2a7e32.json.gz).

Prove that, for every positive integer $n$, there exists an integer $m$ such that $2^{m}+m$ is divisible by $n$.



## 2006 — C7

**Record:** `imo_2006_47470d`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_47470d.json.gz).

Consider a convex polyhedron without parallel edges and without an edge parallel to any face other than the two faces adjacent to it.
Call a pair of points of the polyhedron antipodal if there exist two parallel planes passing through these points and such that the polyhedron is contained between these planes.
Let $A$ be the number of antipodal pairs of vertices, and let $B$ be the number of antipodal pairs of midpoints of edges. Determine the difference $A-B$ in terms of the numbers of vertices, edges and faces.



## 2006 — C2

**Record:** `imo_2006_816c88`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_816c88.json.gz).

A diagonal of a regular 2006-gon is called odd if its endpoints divide the boundary into two parts, each composed of an odd number of sides. Sides are also regarded as odd diagonals.
Suppose the 2006-gon has been dissected into triangles by 2003 nonintersecting diagonals. Find the maximum possible number of isosceles triangles with two odd sides.
(Serbia)



## 2006 — C4

**Record:** `imo_2006_a3af5a`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_a3af5a.json.gz).

A cake has the form of an $n \times n$ square composed of $n^2$ unit squares. Strawberries lie on some of the unit squares so that each row or column contains exactly one strawberry; call this arrangement $\mathcal{A}$.
Let $\mathcal{B}$ be another such arrangement. Suppose that every grid rectangle with one vertex at the top left corner of the cake contains no fewer strawberries of arrangement $\mathcal{B}$ than of arrangement $\mathcal{A}$. Prove that arrangement $\mathcal{B}$ can be obtained from $\mathcal{A}$ by performing a number of switches, defined as follows:
A switch consists in selecting a grid rectangle with only two strawberries, situated at its top right corner and bottom left corner, and moving these two strawberries to the other two corners of that rectangle.



## 2006 — C5

**Record:** `imo_2006_b88369`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_b88369.json.gz).

An $(n, k)$-tournament is a contest with $n$ players held in $k$ rounds such that:
(i) Each player plays in each round, and every two players meet at most once.
(ii) If player $A$ meets player $B$ in round $i$, player $C$ meets player $D$ in round $i$, and player $A$ meets player $C$ in round $j$, then player $B$ meets player $D$ in round $j$.
Determine all pairs $(n, k)$ for which there exists an $(n, k)$-tournament.



## 2006 — C1

**Record:** `imo_2006_dccdc3`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_dccdc3.json.gz).

We have $n \geq 2$ lamps $L_{1}, \ldots, L_{n}$ in a row, each of them being either on or off. Every second we simultaneously modify the state of each lamp as follows:
- if the lamp $L_{i}$ and its neighbours (only one neighbour for $i=1$ or $i=n$, two neighbours for other $i$) are in the same state, then $L_{i}$ is switched off;
- otherwise, $L_{i}$ is switched on.
Initially all the lamps are off except the leftmost one which is on.

a. Prove that there are infinitely many integers $n$ for which all the lamps will eventually be off.

b. Prove that there are infinitely many integers $n$ for which the lamps will never be all off.



## 2006 — C3

**Record:** `imo_2006_f50971`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_f50971.json.gz).

Let $S$ be a finite set of points in the plane such that no three of them are on a line. For each convex polygon $P$ whose vertices are in $S$, let $a(P)$ be the number of vertices of $P$, and let $b(P)$ be the number of points of $S$ which are outside $P$. Prove that for every real number $x$
$$
\sum_{P} x^{a(P)}(1-x)^{b(P)}=1,
$$
where the sum is taken over all convex polygons with vertices in $S$.

NB. A line segment, a point and the empty set are considered as convex polygons of 2, 1 and 0 vertices, respectively.



## 2006 — C6

**Record:** `imo_2006_fa06e0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_fa06e0.json.gz).

A holey triangle is an upward equilateral triangle of side length $n$ with $n$ upward unit triangular holes cut out. A diamond is a $60^{\circ}$-$120^{\circ}$ unit rhombus. Prove that a holey triangle $T$ can be tiled with diamonds if and only if the following condition holds: Every upward equilateral triangle of side length $k$ in $T$ contains at most $k$ holes, for $1 \leq k \leq n$.
(Colombia)



## 2007 — C1

**Record:** `imo_2007_09542d`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_09542d.json.gz).

Let $n > 1$ be an integer. Find all sequences $a_{1}, a_{2}, \ldots, a_{n^{2}+n}$ satisfying the following conditions:
(a) $a_{i} \in \{0,1\}$ for all $1 \leq i \leq n^{2}+n$;
(b) $a_{i+1}+a_{i+2}+\ldots+a_{i+n} < a_{i+n+1}+a_{i+n+2}+\ldots+a_{i+2n}$ for all $0 \leq i \leq n^{2}-n$.



## 2007 — C3

**Record:** `imo_2007_104cb8`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_104cb8.json.gz).

Find all positive integers $n$, for which the numbers in the set $S=\{1,2, \ldots, n\}$ can be colored red and blue, with the following condition being satisfied: the set $S \times S \times S$ contains exactly $2007$ ordered triples $(x, y, z)$ such that (i) $x, y, z$ are of the same color and (ii) $x+y+z$ is divisible by $n$.



## 2007 — N1

**Record:** `imo_2007_16b745`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_16b745.json.gz).

Find all pairs $(k, n)$ of positive integers for which $7^{k}-3^{n}$ divides $k^{4}+n^{2}$.



## 2007 — N3

**Record:** `imo_2007_2b3b32`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_2b3b32.json.gz).

Let $X$ be a set of $10000$ integers, none of them is divisible by $47$. Prove that there exists a $2007$-element subset $Y$ of $X$ such that $a-b+c-d+e$ is not divisible by $47$ for any $a, b, c, d, e \in Y$.



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



## 2007 — C2

**Record:** `imo_2007_58d0fc`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_58d0fc.json.gz).

A unit square is dissected into $n>1$ rectangles such that their sides are parallel to the sides of the square. Any line, parallel to a side of the square and intersecting its interior, also intersects the interior of some rectangle. Prove that in this dissection, there exists a rectangle having no point on the boundary of the square.



## 2007 — C7

**Record:** `imo_2007_67267d`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_67267d.json.gz).

Let $\alpha < \frac{3 - \sqrt{5}}{2}$ be a positive real number. Prove that there exist positive integers $n$ and $p > \alpha \cdot 2^{n}$ for which one can select $2p$ pairwise distinct subsets $S_{1}, \ldots, S_{p}, T_{1}, \ldots, T_{p}$ of the set $\{1, 2, \ldots, n\}$ such that $S_{i} \cap T_{j} \neq \varnothing$ for all $1 \leq i, j \leq p$.



## 2007 — C5

**Record:** `imo_2007_be294f`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_be294f.json.gz).

In the Cartesian coordinate plane define the strip $S_{n}=\{(x, y) \mid n \leq x<n+1\}$ for every integer $n$. Assume that each strip $S_{n}$ is colored either red or blue, and let $a$ and $b$ be two distinct positive integers. Prove that there exists a rectangle with side lengths $a$ and $b$ such that its vertices have the same color.



## 2007 — C8

**Record:** `imo_2007_c1c48b`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_c1c48b.json.gz).

Given a convex $n$-gon $P$ in the plane. For every three vertices of $P$, consider the triangle determined by them. Call such a triangle good if all its sides are of unit length.
Prove that there are not more than $\frac{2}{3} n$ good triangles.



## 2007 — A2

**Record:** `imo_2007_d1b775`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_d1b775.json.gz).

Consider those functions $f: \mathbb{N} \rightarrow \mathbb{N}$ which satisfy the condition
$$
f(m+n) \geq f(m)+f(f(n))-1
$$
for all $m, n \in \mathbb{N}$. Find all possible values of $f(2007)$.

($\mathbb{N}$ denotes the set of all positive integers.)



## 2007 — N7

**Record:** `imo_2007_e1c86b`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_e1c86b.json.gz).

For a prime $p$ and a positive integer $n$, denote by $\nu_{p}(n)$ the exponent of $p$ in the prime factorization of $n!$. Given a positive integer $d$ and a finite set $\{p_{1}, \ldots, p_{k}\}$ of primes. Show that there are infinitely many positive integers $n$ such that $d \mid \nu_{p_{i}}(n)$ for all $1 \leq i \leq k$.



## 2007 — C4

**Record:** `imo_2007_e391ee`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_e391ee.json.gz).

Let $A_{0} = (a_{1}, \ldots, a_{n})$ be a finite sequence of real numbers. For each $k \geq 0$, from the sequence $A_{k} = (x_{1}, \ldots, x_{n})$ we construct a new sequence $A_{k+1}$ in the following way.
1. We choose a partition $\{1, \ldots, n\} = I \cup J$, where $I$ and $J$ are two disjoint sets, such that the expression
$$
\left|\sum_{i \in I} x_{i} - \sum_{j \in J} x_{j}\right|
$$
attains the smallest possible value. (We allow the sets $I$ or $J$ to be empty; in this case the corresponding sum is $0$.) If there are several such partitions, one is chosen arbitrarily.
2. We set $A_{k+1} = (y_{1}, \ldots, y_{n})$, where $y_{i} = x_{i} + 1$ if $i \in I$, and $y_{i} = x_{i} - 1$ if $i \in J$.
Prove that for some $k$, the sequence $A_{k}$ contains an element $x$ such that $|x| \geq n / 2$.



## 2007 — N4

**Record:** `imo_2007_f1ecad`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2007_f1ecad.json.gz).

For every integer $k \geq 2$, prove that $2^{3k}$ divides the number
$$
\binom{2^{k+1}}{2^{k}} - \binom{2^{k}}{2^{k-1}}
$$



## 2008 — C2

**Record:** `imo_2008_06a8f7`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_06a8f7.json.gz).

For every positive integer $n$ determine the number of permutations $(a_{1}, a_{2}, \ldots, a_{n})$ of the set $\{1,2, \ldots, n\}$ with the following property:
$$
2(a_{1}+a_{2}+\cdots+a_{k}) \quad \text{is divisible by} \ k \quad \text{for} \ k=1,2, \ldots, n.
$$



## 2008 — G5

**Record:** `imo_2008_384044`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_384044.json.gz).

Let $k$ and $n$ be integers with $0 \leq k \leq n-2$. Consider a set $L$ of $n$ lines in the plane such that no two of them are parallel and no three have a common point. Denote by $I$ the set of intersection points of lines in $L$. Let $O$ be a point in the plane not lying on any line of $L$.
A point $X \in I$ is colored red if the open line segment $O X$ intersects at most $k$ lines in $L$. Prove that $I$ contains at least $\frac{1}{2}(k+1)(k+2)$ red points.



## 2008 — N4

**Record:** `imo_2008_5311eb`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_5311eb.json.gz).

Let $n$ be a positive integer. Show that the numbers
$$
\binom{2^{n}-1}{0}, \quad\binom{2^{n}-1}{1}, \quad\binom{2^{n}-1}{2}, \quad \ldots, \quad\binom{2^{n}-1}{2^{n-1}-1}
$$
are congruent modulo $2^{n}$ to $1,3,5, \ldots, 2^{n}-1$ in some order.



## 2008 — C5

**Record:** `imo_2008_740617`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_740617.json.gz).

Let $S=\{x_{1}, x_{2}, \ldots, x_{k+\ell}\}$ be a $(k+\ell)$-element set of real numbers contained in the interval $[0,1]$; $k$ and $\ell$ are positive integers. A $k$-element subset $A \subset S$ is called nice if
$$
\left|\frac{1}{k} \sum_{x_{i} \in A} x_{i}-\frac{1}{\ell} \sum_{x_{j} \in S \backslash A} x_{j}\right| \leq \frac{k+\ell}{2 k \ell} .
$$
Prove that the number of nice subsets is at least $\frac{2}{k+\ell}\binom{k+\ell}{k}$.



## 2008 — A3

**Record:** `imo_2008_ac4e9a`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_ac4e9a.json.gz).

Let $S \subseteq \mathbb{R}$ be a set of real numbers. We say that a pair $(f, g)$ of functions from $S$ into $S$ is a Spanish Couple on $S$, if they satisfy the following conditions:
(i) Both functions are strictly increasing, i.e. $f(x) < f(y)$ and $g(x) < g(y)$ for all $x, y \in S$ with $x < y$;
(ii) The inequality $f(g(g(x))) < g(f(x))$ holds for all $x \in S$.
Decide whether there exists a Spanish Couple

a. on the set $S = \mathbb{N}$ of positive integers;
b. on the set $S = \{ a - 1 / b : a, b \in \mathbb{N} \}$.



## 2008 — C3

**Record:** `imo_2008_bdc772`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_bdc772.json.gz).

In the coordinate plane consider the set $S$ of all points with integer coordinates. For a positive integer $k$, two distinct points $A, B \in S$ will be called $k$-friends if there is a point $C \in S$ such that the area of the triangle $A B C$ is equal to $k$. A set $T \subset S$ will be called a $k$-clique if every two points in $T$ are $k$-friends. Find the least positive integer $k$ for which there exists a $k$-clique with more than 200 elements.



## 2008 — C1

**Record:** `imo_2008_edd8bc`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2008_edd8bc.json.gz).

In the plane we consider rectangles whose sides are parallel to the coordinate axes and have positive length. Such a rectangle will be called a box. Two boxes intersect if they have a common point in their interior or on their boundary.
Find the largest $n$ for which there exist $n$ boxes $B_{1}, \ldots, B_{n}$ such that $B_{i}$ and $B_{j}$ intersect if and only if $i \not \equiv j \pm 1(\bmod n)$.



## 2009 — C2

**Record:** `imo_2009_7c4eea`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2009_7c4eea.json.gz).

For any integer $n \geq 2$, let $N(n)$ be the maximal number of triples $(a_{i}, b_{i}, c_{i})$, $i=1, \ldots, N(n)$, consisting of nonnegative integers $a_{i}, b_{i}$ and $c_{i}$ such that the following two conditions are satisfied:
(1) $a_{i}+b_{i}+c_{i}=n$ for all $i=1, \ldots, N(n)$,
(2) If $i \neq j$, then $a_{i} \neq a_{j}, b_{i} \neq b_{j}$ and $c_{i} \neq c_{j}$.
Determine $N(n)$ for all $n \geq 2$.



## 2009 — C8

**Record:** `imo_2009_872455`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2009_872455.json.gz).

For any integer $n \geq 2$, we compute the integer $h(n)$ by applying the following procedure to its decimal representation. Let $r$ be the rightmost digit of $n$.
(1) If $r=0$, then the decimal representation of $h(n)$ results from the decimal representation of $n$ by removing this rightmost digit $0$.
(2) If $1 \leq r \leq 9$ we split the decimal representation of $n$ into a maximal right part $R$ that solely consists of digits not less than $r$ and into a left part $L$ that either is empty or ends with a digit strictly smaller than $r$. Then the decimal representation of $h(n)$ consists of the decimal representation of $L$, followed by two copies of the decimal representation of $R-1$. For instance, for the number $n=17,151,345,543$, we will have $L=17,151$, $R=345,543$ and $h(n)=17,151,345,542,345,542$.
Prove that, starting with an arbitrary integer $n \geq 2$, iterated application of $h$ produces the integer $1$ after finitely many steps.



## 2009 — N1

**Record:** `imo_2009_af95e8`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2009_af95e8.json.gz).

A social club has $n$ members. They have the membership numbers $1, 2, \ldots, n$, respectively. From time to time members send presents to other members, including items they have already received as presents from other members. In order to avoid the embarrassing situation that a member might receive a present that he or she has sent to other members, the club adds the following rule to its statutes at one of its annual general meetings:

"A member with membership number $a$ is permitted to send a present to a member with membership number $b$ if and only if $a(b-1)$ is a multiple of $n$."

Prove that, if each member follows this rule, none will receive a present from another member that he or she has already sent to other members.

Alternative formulation: Let $G$ be a directed graph with $n$ vertices $v_{1}, v_{2}, \ldots, v_{n}$, such that there is an edge going from $v_{a}$ to $v_{b}$ if and only if $a$ and $b$ are distinct and $a(b-1)$ is a multiple of $n$. Prove that this graph does not contain a directed cycle.



## 2009 — C6

**Record:** `imo_2009_c42d2f`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2009_c42d2f.json.gz).

On a $999 \times 999$ board a limp rook can move in the following way: From any square it can move to any of its adjacent squares, i.e. a square having a common side with it, and every move must be a turn, i.e. the directions of any two consecutive moves must be perpendicular. A nonintersecting route of the limp rook consists of a sequence of pairwise different squares that the limp rook can visit in that order by an admissible sequence of moves. Such a non-intersecting route is called cyclic, if the limp rook can, after reaching the last square of the route, move directly to the first square of the route and start over.
How many squares does the longest possible cyclic, non-intersecting route of a limp rook visit?



## 2009 — C4

**Record:** `imo_2009_c91ba6`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2009_c91ba6.json.gz).

For an integer $m \geq 1$, we consider partitions of a $2^{m} \times 2^{m}$ chessboard into rectangles consisting of cells of the chessboard, in which each of the $2^{m}$ cells along one diagonal forms a separate rectangle of side length 1. Determine the smallest possible sum of rectangle perimeters in such a partition.



## 2009 — N2

**Record:** `imo_2009_cf1420`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2009_cf1420.json.gz).

A positive integer $N$ is called balanced, if $N=1$ or if $N$ can be written as a product of an even number of not necessarily distinct primes. Given positive integers $a$ and $b$, consider the polynomial $P$ defined by $P(x)=(x+a)(x+b)$.

a. Prove that there exist distinct positive integers $a$ and $b$ such that all the numbers $P(1), P(2), \ldots, P(50)$ are balanced.

b. Prove that if $P(n)$ is balanced for all positive integers $n$, then $a=b$.



## 2009 — C1

**Record:** `imo_2009_de7766`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2009_de7766.json.gz).

Consider $2009$ cards, each having one gold side and one black side, lying in parallel on a long table. Initially all cards show their gold sides. Two players, standing by the same long side of the table, play a game with alternating moves. Each move consists of choosing a block of $50$ consecutive cards, the leftmost of which is showing gold, and turning them all over, so those which showed gold now show black and vice versa. The last player who can make a legal move wins.

a. Does the game necessarily end?

b. Does there exist a winning strategy for the starting player?



## 2009 — C5

**Record:** `imo_2009_fa6aa0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2009_fa6aa0.json.gz).

Five identical empty buckets of 2-liter capacity stand at the vertices of a regular pentagon. Cinderella and her wicked Stepmother go through a sequence of rounds: At the beginning of every round, the Stepmother takes one liter of water from the nearby river and distributes it arbitrarily over the five buckets. Then Cinderella chooses a pair of neighboring buckets, empties them into the river, and puts them back. Then the next round begins. The Stepmother's goal is to make one of these buckets overflow. Cinderella's goal is to prevent this. Can the wicked Stepmother enforce a bucket overflow?



## 2010 — A7

**Record:** `imo_2010_237f4c`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2010_237f4c.json.gz).

Let $a_{1}, \ldots, a_{r}$ be positive real numbers. For $n>r$, we inductively define
$$
a_{n}=\max _{1 \leq k \leq n-1}\left(a_{k}+a_{n-k}\right) \tag{1}
$$
Prove that there exist positive integers $\ell \leq r$ and $N$ such that $a_{n}=a_{n-\ell}+a_{\ell}$ for all $n \geq N$.



## 2010 — N6

**Record:** `imo_2010_3a2ab0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2010_3a2ab0.json.gz).

The rows and columns of a $2^{n} \times 2^{n}$ table are numbered from $0$ to $2^{n}-1$. The cells of the table have been colored with the following property being satisfied: for each $0 \leq i, j \leq 2^{n}-1$, the $j$th cell in the $i$th row and the $(i+j)$th cell in the $j$th row have the same color. (The indices of the cells in a row are considered modulo $2^{n}$.)

Prove that the maximal possible number of colors is $2^{n}$.

(Iran)



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



## 2010 — C2

**Record:** `imo_2010_c0ac83`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2010_c0ac83.json.gz).

On some planet, there are $2^{N}$ countries $(N \geq 4)$. Each country has a flag $N$ units wide and one unit high composed of $N$ fields of size $1 \times 1$, each field being either yellow or blue. No two countries have the same flag.

We say that a set of $N$ flags is diverse if these flags can be arranged into an $N \times N$ square so that all $N$ fields on its main diagonal will have the same color. Determine the smallest positive integer $M$ such that among any $M$ distinct flags, there exist $N$ flags forming a diverse set.



## 2010 — C7

**Record:** `imo_2010_c12e74`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2010_c12e74.json.gz).

Let $P_{1}, \ldots, P_{s}$ be arithmetic progressions of integers, the following conditions being satisfied:
(i) each integer belongs to at least one of them;
(ii) each progression contains a number which does not belong to other progressions.
Denote by $n$ the least common multiple of steps of these progressions; let $n=p_{1}^{\alpha_{1}} \ldots p_{k}^{\alpha_{k}}$ be its prime factorization. Prove that
$$
s \geq 1+\sum_{i=1}^{k} \alpha_{i}\left(p_{i}-1\right)
$$



## 2010 — C4

**Record:** `imo_2010_cb1492`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2010_cb1492.json.gz).

Six stacks $S_{1}, \ldots, S_{6}$ of coins are standing in a row. In the beginning every stack contains a single coin. There are two types of allowed moves:

Move 1: If stack $S_{k}$ with $1 \leq k \leq 5$ contains at least one coin, you may remove one coin from $S_{k}$ and add two coins to $S_{k+1}$.

Move 2: If stack $S_{k}$ with $1 \leq k \leq 4$ contains at least one coin, then you may remove one coin from $S_{k}$ and exchange stacks $S_{k+1}$ and $S_{k+2}$.

Decide whether it is possible to achieve by a sequence of such moves that the first five stacks are empty, whereas the sixth stack $S_{6}$ contains exactly $2010^{2010^{2010}}$ coins.



## 2010 — C5

**Record:** `imo_2010_f50853`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2010_f50853.json.gz).

$n \geq 4$ players participated in a tennis tournament. Any two players have played exactly one game, and there was no tie game. We call a company of four players bad if one player was defeated by the other three players, and each of these three players won a game and lost another game among themselves. Suppose that there is no bad company in this tournament. Let $w_{i}$ and $\ell_{i}$ be respectively the number of wins and losses of the $i$th player. Prove that
$$
\sum_{i=1}^{n}\left(w_{i}-\ell_{i}\right)^{3} \geq 0
$$



## 2011 — C6

**Record:** `imo_2011_1bfa71`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2011_1bfa71.json.gz).

Let $n$ be a positive integer and let $W = \ldots x_{-1} x_{0} x_{1} x_{2} \ldots$ be an infinite periodic word consisting of the letters $a$ and $b$. Suppose that the minimal period $N$ of $W$ is greater than $2^{n}$.

A finite nonempty word $U$ is said to appear in $W$ if there exist indices $k \leq \ell$ such that $U = x_{k} x_{k+1} \ldots x_{\ell}$. A finite word $U$ is called ubiquitous if the four words $U a$, $U b$, $a U$, and $b U$ all appear in $W$. Prove that there are at least $n$ ubiquitous finite nonempty words.



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



## 2011 — C7

**Record:** `imo_2011_3bbde9`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2011_3bbde9.json.gz).

On a square table of $2011$ by $2011$ cells we place a finite number of napkins that each cover a square of $52$ by $52$ cells. In each cell we write the number of napkins covering it, and we record the maximal number $k$ of cells that all contain the same nonzero number. Considering all possible napkin configurations, what is the largest value of $k$?



## 2011 — A2

**Record:** `imo_2011_5fba9c`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2011_5fba9c.json.gz).

Determine all sequences $\left(x_{1}, x_{2}, \ldots, x_{2011}\right)$ of positive integers such that for every positive integer $n$ there is an integer $a$ with
$$
x_{1}^{n}+2 x_{2}^{n}+\cdots+2011 x_{2011}^{n}=a^{n+1}+1 .
$$



## 2011 — C5

**Record:** `imo_2011_bc8c85`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2011_bc8c85.json.gz).

Let $m$ be a positive integer and consider a checkerboard consisting of $m$ by $m$ unit squares. At the midpoints of some of these unit squares there is an ant. At time 0, each ant starts moving with speed 1 parallel to some edge of the checkerboard. When two ants moving in opposite directions meet, they both turn $90^{\circ}$ clockwise and continue moving with speed 1. When more than two ants meet, or when two ants moving in perpendicular directions meet, the ants continue moving in the same direction as before they met. When an ant reaches one of the edges of the checkerboard, it falls off and will not re-appear.

Considering all possible starting positions, determine the latest possible moment at which the last ant falls off the checkerboard or prove that such a moment does not necessarily exist.



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



## 2012 — C1

**Record:** `imo_2012_21355f`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2012_21355f.json.gz).

Several positive integers are written in a row. Iteratively, Alice chooses two adjacent numbers $x$ and $y$ such that $x > y$ and $x$ is to the left of $y$, and replaces the pair $(x, y)$ by either $(y+1, x)$ or $(x-1, x)$. Prove that she can perform only finitely many such iterations.



## 2012 — C2

**Record:** `imo_2012_2dedb8`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2012_2dedb8.json.gz).

Let $n \geq 1$ be an integer. What is the maximum number of disjoint pairs of elements of the set $\{1,2, \ldots, n\}$ such that the sums of the different pairs are different integers not exceeding $n$?



## 2012 — N8

**Record:** `imo_2012_35e1cc`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2012_35e1cc.json.gz).

Prove that for every prime $p > 100$ and every integer $r$ there exist two integers $a$ and $b$ such that $p$ divides $a^{2} + b^{5} - r$.



## 2012 — C4

**Record:** `imo_2012_6b2e95`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2012_6b2e95.json.gz).

Players $A$ and $B$ play a game with $N \geq 2012$ coins and $2012$ boxes arranged around a circle. Initially $A$ distributes the coins among the boxes so that there is at least $1$ coin in each box. Then the two of them make moves in the order $B, A, B, A, \ldots$ by the following rules:
- On every move of his $B$ passes $1$ coin from every box to an adjacent box.
- On every move of hers $A$ chooses several coins that were not involved in $B$'s previous move and are in different boxes. She passes every chosen coin to an adjacent box.

Player $A$'s goal is to ensure at least $1$ coin in each box after every move of hers, regardless of how $B$ plays and how many moves are made. Find the least $N$ that enables her to succeed.



## 2012 — C5

**Record:** `imo_2012_ddfd08`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2012_ddfd08.json.gz).

The columns and the rows of a $3n \times 3n$ square board are numbered $1, 2, \ldots, 3n$. Every square $(x, y)$ with $1 \leq x, y \leq 3n$ is colored asparagus, byzantium or citrine according as the modulo $3$ remainder of $x+y$ is $0$, $1$ or $2$ respectively. One token colored asparagus, byzantium or citrine is placed on each square, so that there are $3n^{2}$ tokens of each color.

Suppose that one can permute the tokens so that each token is moved to a distance of at most $d$ from its original position, each asparagus token replaces a byzantium token, each byzantium token replaces a citrine token, and each citrine token replaces an asparagus token. Prove that it is possible to permute the tokens so that each token is moved to a distance of at most $d+2$ from its original position, and each square contains a token with the same color as the square.



## 2013 — C5

**Record:** `imo_2013_34622f`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_34622f.json.gz).

Let $r$ be a positive integer, and let $a_{0}, a_{1}, \ldots$ be an infinite sequence of real numbers. Assume that for all nonnegative integers $m$ and $s$ there exists a positive integer $n \in [m+1, m+r]$ such that
$$
a_{m}+a_{m+1}+\cdots+a_{m+s}=a_{n}+a_{n+1}+\cdots+a_{n+s}
$$
Prove that the sequence is periodic, i.e. there exists some $p \geqslant 1$ such that $a_{n+p}=a_{n}$ for all $n \geqslant 0$.



## 2013 — A2

**Record:** `imo_2013_34c239`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_34c239.json.gz).

Prove that in any set of $2000$ distinct real numbers there exist two pairs $a > b$ and $c > d$ with $a \neq c$ or $b \neq d$, such that
$$
\left|\frac{a-b}{c-d}-1\right|<\frac{1}{100000}
$$



## 2013 — A4

**Record:** `imo_2013_3eed83`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_3eed83.json.gz).

Let $n$ be a positive integer, and consider a sequence $a_{1}, a_{2}, \ldots, a_{n}$ of positive integers. Extend it periodically to an infinite sequence $a_{1}, a_{2}, \ldots$ by defining $a_{n+i}=a_{i}$ for all $i \geqslant 1$. If
$$
a_{1} \leqslant a_{2} \leqslant \cdots \leqslant a_{n} \leqslant a_{1}+n
$$
and
$$
a_{a_{i}} \leqslant n+i-1 \quad \text{ for } i=1,2, \ldots, n
$$
prove that
$$
a_{1}+\cdots+a_{n} \leqslant n^{2} .
$$



## 2013 — C1

**Record:** `imo_2013_4d15d8`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_4d15d8.json.gz).

Let $n$ be a positive integer. Find the smallest integer $k$ with the following property: Given any real numbers $a_{1}, \ldots, a_{d}$ such that $a_{1}+a_{2}+\cdots+a_{d}=n$ and $0 \leqslant a_{i} \leqslant 1$ for $i=1,2, \ldots, d$, it is possible to partition these numbers into $k$ groups (some of which may be empty) such that the sum of the numbers in each group is at most $1$.



## 2013 — C7

**Record:** `imo_2013_5a8513`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_5a8513.json.gz).

Let $n \geqslant 2$ be an integer. Consider all circular arrangements of the numbers $0,1, \ldots, n$; the $n+1$ rotations of an arrangement are considered to be equal. A circular arrangement is called beautiful if, for any four distinct numbers $0 \leqslant a, b, c, d \leqslant n$ with $a+c=b+d$, the chord joining numbers $a$ and $c$ does not intersect the chord joining numbers $b$ and $d$.
Let $M$ be the number of beautiful arrangements of $0,1, \ldots, n$. Let $N$ be the number of pairs ( $x, y$ ) of positive integers such that $x+y \leqslant n$ and $\operatorname{gcd}(x, y)=1$. Prove that
$$
M=N+1 .
$$



## 2013 — C8

**Record:** `imo_2013_5ee60e`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_5ee60e.json.gz).

Players $A$ and $B$ play a paintful game on the real line. Player $A$ has a pot of paint with four units of black ink. A quantity $p$ of this ink suffices to blacken a (closed) real interval of length $p$. In every round, player $A$ picks some positive integer $m$ and provides $1 / 2^{m}$ units of ink from the pot. Player $B$ then picks an integer $k$ and blackens the interval from $k / 2^{m}$ to $(k+1) / 2^{m}$ (some parts of this interval may have been blackened before). The goal of player $A$ is to reach a situation where the pot is empty and the interval $[0,1]$ is not completely blackened.
Decide whether there exists a strategy for player $A$ to win in a finite number of moves.



## 2013 — C3

**Record:** `imo_2013_7500b7`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_7500b7.json.gz).

A crazy physicist discovered a new kind of particle which he called an imon, after some of them mysteriously appeared in his lab. Some pairs of imons in the lab can be entangled, and each imon can participate in many entanglement relations. The physicist has found a way to perform the following two kinds of operations with these particles, one operation at a time.
(i) If some imon is entangled with an odd number of other imons in the lab, then the physicist can destroy it.
(ii) At any moment, he may double the whole family of imons in his lab by creating a copy $I^{\prime}$ of each imon $I$. During this procedure, the two copies $I^{\prime}$ and $J^{\prime}$ become entangled if and only if the original imons $I$ and $J$ are entangled, and each copy $I^{\prime}$ becomes entangled with its original imon $I$; no other entanglements occur or disappear at this moment.
Prove that the physicist may apply a sequence of such operations resulting in a family of imons, no two of which are entangled.



## 2013 — N7

**Record:** `imo_2013_a66da8`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_a66da8.json.gz).

Let $\nu$ be an irrational positive number, and let $m$ be a positive integer. A pair $(a, b)$ of positive integers is called good if
$$
a\lceil b \nu\rceil-b\lfloor a \nu\rfloor=m
$$
A good pair $(a, b)$ is called excellent if neither of the pairs $(a-b, b)$ and $(a, b-a)$ is good. (As usual, by $\lfloor x\rfloor$ and $\lceil x\rceil$ we denote the integer numbers such that $x-1<\lfloor x\rfloor \leqslant x$ and $x \leqslant\lceil x\rceil<x+1$.)
Prove that the number of excellent pairs is equal to the sum of the positive divisors of $m$.



## 2013 — A5

**Record:** `imo_2013_ca3c20`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_ca3c20.json.gz).

Let $\mathbb{Z}_{\geqslant 0}$ be the set of all nonnegative integers. Find all the functions $f: \mathbb{Z}_{\geqslant 0} \rightarrow \mathbb{Z}_{\geqslant 0}$ satisfying the relation
$$
f(f(f(n)))=f(n+1)+1
$$
for all $n \in \mathbb{Z}_{\geqslant 0}$.



## 2013 — A1

**Record:** `imo_2013_d960d1`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_d960d1.json.gz).

Let $n$ be a positive integer and let $a_{1}, \ldots, a_{n-1}$ be arbitrary real numbers. Define the sequences $u_{0}, \ldots, u_{n}$ and $v_{0}, \ldots, v_{n}$ inductively by $u_{0}=u_{1}=v_{0}=1$, and
$$
u_{k+1}=u_{k}+a_{k} u_{k-1}, \quad v_{k+1}=v_{k}+a_{n-k} v_{k-1} \quad \text{ for } k=1, \ldots, n-1 .$$
Prove that $u_{n}=v_{n}$.



## 2013 — C2

**Record:** `imo_2013_eb8b9e`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_eb8b9e.json.gz).

In the plane, 2013 red points and 2014 blue points are marked so that no three of the marked points are collinear. One needs to draw $k$ lines not passing through the marked points and dividing the plane into several regions. The goal is to do it in such a way that no region contains points of both colors.
Find the minimal value of $k$ such that the goal is attainable for every possible configuration of 4027 points.



## 2013 — C4

**Record:** `imo_2013_f9ba1b`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2013_f9ba1b.json.gz).

Let $n$ be a positive integer, and let $A$ be a subset of $\{1, \ldots, n\}$. An $A$-partition of $n$ into $k$ parts is a representation of $n$ as a sum $n=a_{1}+\cdots+a_{k}$, where the parts $a_{1}, \ldots, a_{k}$ belong to $A$ and are not necessarily distinct. The number of different parts in such a partition is the number of (distinct) elements in the set $\left\{a_{1}, a_{2}, \ldots, a_{k}\right\}$.
We say that an $A$-partition of $n$ into $k$ parts is optimal if there is no $A$-partition of $n$ into $r$ parts with $r<k$. Prove that any optimal $A$-partition of $n$ contains at most $\sqrt[3]{6 n}$ different parts.



## 2014 — C6

**Record:** `imo_2014_013ae9`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2014_013ae9.json.gz).

We are given an infinite deck of cards, each with a real number on it. For every real number $x$, there is exactly one card in the deck that has $x$ written on it. Now two players draw disjoint sets $A$ and $B$ of $100$ cards each from this deck. We would like to define a rule that declares one of them a winner. This rule should satisfy the following conditions:
1. The winner only depends on the relative order of the $200$ cards: if the cards are laid down in increasing order face down and we are told which card belongs to which player, but not what numbers are written on them, we can still decide the winner.
2. If we write the elements of both sets in increasing order as $A=\{a_{1}, a_{2}, \ldots, a_{100}\}$ and $B=\{b_{1}, b_{2}, \ldots, b_{100}\}$, and $a_{i}>b_{i}$ for all $i$, then $A$ beats $B$.
3. If three players draw three disjoint sets $A, B, C$ from the deck, $A$ beats $B$ and $B$ beats $C$, then $A$ also beats $C$.
How many ways are there to define such a rule? Here, we consider two rules as different if there exist two sets $A$ and $B$ such that $A$ beats $B$ according to one rule, but $B$ beats $A$ according to the other.



## 2014 — C8

**Record:** `imo_2014_09db9c`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2014_09db9c.json.gz).

A card deck consists of 1024 cards. On each card, a set of distinct decimal digits is written in such a way that no two of these sets coincide (thus, one of the cards is empty). Two players alternately take cards from the deck, one card per turn. After the deck is empty, each player checks if he can throw out one of his cards so that each of the ten digits occurs on an even number of his remaining cards. If one player can do this but the other one cannot, the one who can is the winner; otherwise a draw is declared.
Determine all possible first moves of the first player after which he has a winning strategy.



## 2014 — C3

**Record:** `imo_2014_44369f`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2014_44369f.json.gz).

Let $n \geqslant 2$ be an integer. Consider an $n \times n$ chessboard divided into $n^{2}$ unit squares. We call a configuration of $n$ rooks on this board happy if every row and every column contains exactly one rook. Find the greatest positive integer $k$ such that for every happy configuration of rooks, we can find a $k \times k$ square without a rook on any of its $k^{2}$ unit squares.



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



## 2014 — C5

**Record:** `imo_2014_d42980`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2014_d42980.json.gz).

Consider $n \geqslant 3$ lines in the plane such that no two lines are parallel and no three have a common point. These lines divide the plane into polygonal regions; let $\mathcal{F}$ be the set of regions having finite area. Prove that it is possible to colour $\lceil\sqrt{n / 2}\rceil$ of the lines blue in such a way that no region in $\mathcal{F}$ has a completely blue boundary. (For a real number $x,\lceil x\rceil$ denotes the least integer which is not smaller than $x$.)



## 2014 — N6

**Record:** `imo_2014_da4751`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2014_da4751.json.gz).

Let $a_{1} < a_{2} < \cdots < a_{n}$ be pairwise coprime positive integers with $a_{1}$ being prime and $a_{1} \geqslant n+2$. On the segment $I = [0, a_{1} a_{2} \cdots a_{n}]$ of the real line, mark all integers that are divisible by at least one of the numbers $a_{1}, \ldots, a_{n}$. These points split $I$ into a number of smaller segments. Prove that the sum of the squares of the lengths of these segments is divisible by $a_{1}$.



## 2014 — C7

**Record:** `imo_2014_fb1712`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2014_fb1712.json.gz).

Let $M$ be a set of $n \geqslant 4$ points in the plane, no three of which are collinear. Initially these points are connected with $n$ segments so that each point in $M$ is the endpoint of exactly two segments. Then, at each step, one may choose two segments $AB$ and $CD$ sharing a common interior point and replace them by the segments $AC$ and $BD$ if none of them is present at this moment. Prove that it is impossible to perform $n^{3} / 4$ or more such moves.



## 2015 — C1

**Record:** `imo_2015_0681fc`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2015_0681fc.json.gz).

In Lineland there are $n \geqslant 1$ towns, arranged along a road running from left to right. Each town has a left bulldozer (put to the left of the town and facing left) and a right bulldozer (put to the right of the town and facing right). The sizes of the $2n$ bulldozers are distinct. Every time when a right and a left bulldozer confront each other, the larger bulldozer pushes the smaller one off the road. On the other hand, the bulldozers are quite unprotected at their rears; so, if a bulldozer reaches the rear-end of another one, the first one pushes the second one off the road, regardless of their sizes.
Let $A$ and $B$ be two towns, with $B$ being to the right of $A$. We say that town $A$ can sweep town $B$ away if the right bulldozer of $A$ can move over to $B$ pushing off all bulldozers it meets. Similarly, $B$ can sweep $A$ away if the left bulldozer of $B$ can move to $A$ pushing off all bulldozers of all towns on its way.
Prove that there is exactly one town which cannot be swept away by any other one.



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



## 2015 — C7

**Record:** `imo_2015_552a15`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2015_552a15.json.gz).

In a company of people some pairs are enemies. A group of people is called unsociable if the number of members in the group is odd and at least $3$, and it is possible to arrange all its members around a round table so that every two neighbors are enemies. Given that there are at most $2015$ unsociable groups, prove that it is possible to partition the company into $11$ parts so that no two enemies are in the same part.



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



## 2015 — C2

**Record:** `imo_2015_ae4598`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2015_ae4598.json.gz).

Let $\mathcal{V}$ be a finite set of points in the plane. We say that $\mathcal{V}$ is balanced if for any two distinct points $A, B \in \mathcal{V}$, there exists a point $C \in \mathcal{V}$ such that $AC = BC$. We say that $\mathcal{V}$ is center-free if for any distinct points $A, B, C \in \mathcal{V}$, there does not exist a point $P \in \mathcal{V}$ such that $PA = PB = PC$.

a. Show that for all $n \geqslant 3$, there exists a balanced set consisting of $n$ points.

b. For which $n \geqslant 3$ does there exist a balanced, center-free set consisting of $n$ points?



## 2015 — C5

**Record:** `imo_2015_bab8ff`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2015_bab8ff.json.gz).

Consider an infinite sequence $a_{1}, a_{2}, \ldots$ of positive integers with $a_{i} \leqslant 2015$ for all $i \geqslant 1$. Suppose that for any two distinct indices $i$ and $j$ we have $i+a_{i} \neq j+a_{j}$.
Prove that there exist two positive integers $b$ and $N$ such that
$$
\left|\sum_{i=m+1}^{n}\left(a_{i}-b\right)\right| \leqslant 1007^{2}
$$
whenever $n>m \geqslant N$.



## 2015 — C6

**Record:** `imo_2015_f31319`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2015_f31319.json.gz).

Let $S$ be a nonempty set of positive integers. We say that a positive integer $n$ is clean if it has a unique representation as a sum of an odd number of distinct elements from $S$. Prove that there exist infinitely many positive integers that are not clean.
(U.S.A.)



## 2016 — C6

**Record:** `imo_2016_5fca7b`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2016_5fca7b.json.gz).

There are $n \geqslant 3$ islands in a city. Initially, the ferry company offers some routes between some pairs of islands so that it is impossible to divide the islands into two groups such that no two islands in different groups are connected by a ferry route.

After each year, the ferry company will close a ferry route between some two islands $X$ and $Y$. At the same time, in order to maintain its service, the company will open new routes according to the following rule: for any island which is connected by a ferry route to exactly one of $X$ and $Y$, a new route between this island and the other of $X$ and $Y$ is added.

Suppose at any moment, if we partition all islands into two nonempty groups in any way, then it is known that the ferry company will close a certain route connecting two islands from the two groups after some years. Prove that after some years there will be an island which is connected to all other islands by ferry routes.



## 2016 — C4

**Record:** `imo_2016_88479f`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2016_88479f.json.gz).

Find all positive integers $n$ for which we can fill in the entries of an $n \times n$ table with the following properties:
- each entry can be one of $I$, $M$ and $O$;
- in each row and each column, the letters $I$, $M$ and $O$ occur the same number of times; and
- in any diagonal whose number of entries is a multiple of three, the letters $I$, $M$ and $O$ occur the same number of times.



## 2016 — A3

**Record:** `imo_2016_b6b418`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2016_b6b418.json.gz).

Find all integers $n \geqslant 3$ with the following property: for all real numbers $a_{1}, a_{2}, \ldots, a_{n}$ and $b_{1}, b_{2}, \ldots, b_{n}$ satisfying $\left|a_{k}\right|+\left|b_{k}\right|=1$ for $1 \leqslant k \leqslant n$, there exist $x_{1}, x_{2}, \ldots, x_{n}$, each of which is either $-1$ or $1$, such that
$$
\left|\sum_{k=1}^{n} x_{k} a_{k}\right|+\left|\sum_{k=1}^{n} x_{k} b_{k}\right| \leqslant 1
$$



## 2016 — C7

**Record:** `imo_2016_f01bd2`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2016_f01bd2.json.gz).

Let $n \geqslant 2$ be an integer. In the plane, there are $n$ segments given in such a way that any two segments have an intersection point in the interior, and no three segments intersect at a single point. Jeff places a snail at one of the endpoints of each of the segments and claps his hands $n-1$ times. Each time when he claps his hands, all the snails move along their own segments and stay at the next intersection points until the next clap. Since there are $n-1$ intersection points on each segment, all snails will reach the furthest intersection points from their starting points after $n-1$ claps.

a) Prove that if $n$ is odd then Jeff can always place the snails so that no two of them ever occupy the same intersection point.

b) Prove that if $n$ is even then there must be a moment when some two snails occupy the same intersection point no matter how Jeff places the snails.



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



## 2017 — C2

**Record:** `imo_2017_7f8a8b`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2017_7f8a8b.json.gz).

Let $n$ be a positive integer. Define a chameleon to be any sequence of $3n$ letters, with exactly $n$ occurrences of each of the letters $a$, $b$, and $c$. Define a swap to be the transposition of two adjacent letters in a chameleon. Prove that for any chameleon $X$, there exists a chameleon $Y$ such that $X$ cannot be changed to $Y$ using fewer than $3n^{2}/2$ swaps.



## 2017 — G8

**Record:** `imo_2017_a6d9fd`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2017_a6d9fd.json.gz).

There are $2017$ mutually external circles drawn on a blackboard, such that no two are tangent and no three share a common tangent. A tangent segment is a line segment that is a common tangent to two circles, starting at one tangent point and ending at the other one. Luciano is drawing tangent segments on the blackboard, one at a time, so that no tangent segment intersects any other circles or previously drawn tangent segments. Luciano keeps drawing tangent segments until no more can be drawn. Find all possible numbers of tangent segments when he stops drawing.



## 2017 — C8

**Record:** `imo_2017_abff99`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2017_abff99.json.gz).

Let $n$ be a given positive integer. In the Cartesian plane, each lattice point with nonnegative coordinates initially contains a butterfly, and there are no other butterflies. The neighborhood of a lattice point $c$ consists of all lattice points within the axis-aligned $(2 n+1) \times (2 n+1)$ square centered at $c$, apart from $c$ itself. We call a butterfly lonely, crowded, or comfortable, depending on whether the number of butterflies in its neighborhood $N$ is respectively less than, greater than, or equal to half of the number of lattice points in $N$.

Every minute, all lonely butterflies fly away simultaneously. This process goes on for as long as there are any lonely butterflies. Assuming that the process eventually stops, determine the number of comfortable butterflies at the final state.

(Bulgaria)



## 2017 — C3

**Record:** `imo_2017_de14b7`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2017_de14b7.json.gz).

Sir Alex plays the following game on a row of 9 cells. Initially, all cells are empty. In each move, Sir Alex is allowed to perform exactly one of the following two operations:
(1) Choose any number of the form $2^{j}$, where $j$ is a non-negative integer, and put it into an empty cell.
(2) Choose two (not necessarily adjacent) cells with the same number in them; denote that number by $2^{j}$. Replace the number in one of the cells with $2^{j+1}$ and erase the number in the other cell.
At the end of the game, one cell contains the number $2^{n}$, where $n$ is a given positive integer, while the other cells are empty. Determine the maximum number of moves that Sir Alex could have made, in terms of $n$.



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



## 2018 — C6

**Record:** `imo_2018_556799`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2018_556799.json.gz).

Let $a$ and $b$ be distinct positive integers. The following infinite process takes place on an initially empty board.
(i) If there is at least a pair of equal numbers on the board, we choose such a pair and increase one of its components by $a$ and the other by $b$.
(ii) If no such pair exists, we write down two times the number $0$.
Prove that, no matter how we make the choices in (i), operation (ii) will be performed only finitely many times.



## 2018 — C5

**Record:** `imo_2018_b7dcfb`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2018_b7dcfb.json.gz).

Let $k$ be a positive integer. The organising committee of a tennis tournament is to schedule the matches for $2k$ players so that every two players play once, each day exactly one match is played, and each player arrives to the tournament site the day of his first match, and departs the day of his last match. For every day a player is present on the tournament, the committee has to pay 1 coin to the hotel. The organisers want to design the schedule so as to minimise the total cost of all players' stays. Determine this minimum cost.



## 2018 — C7

**Record:** `imo_2018_ee943a`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2018_ee943a.json.gz).

Consider 2018 pairwise crossing circles no three of which are concurrent. These circles subdivide the plane into regions bounded by circular edges that meet at vertices. Notice that there are an even number of vertices on each circle. Given the circle, alternately colour the vertices on that circle red and blue. In doing so for each circle, every vertex is coloured twice once for each of the two circles that cross at that point. If the two colourings agree at a vertex, then it is assigned that colour; otherwise, it becomes yellow. Show that, if some circle contains at least 2061 yellow points, then the vertices of some region are all yellow.



## 2018 — C2

**Record:** `imo_2018_eed763`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2018_eed763.json.gz).

Queenie and Horst play a game on a $20 \times 20$ chessboard. In the beginning the board is empty. In every turn, Horst places a black knight on an empty square in such a way that his new knight does not attack any previous knights. Then Queenie places a white queen on an empty square. The game gets finished when somebody cannot move.
Find the maximal positive $K$ such that, regardless of the strategy of Queenie, Horst can put at least $K$ knights on the board.



## 2018 — A6

**Record:** `imo_2018_f30e16`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2018_f30e16.json.gz).

Let $m, n \geqslant 2$ be integers. Let $f\left(x_{1}, \ldots, x_{n}\right)$ be a polynomial with real coefficients such that
$$
f\left(x_{1}, \ldots, x_{n}\right)=\left\lfloor\frac{x_{1}+\ldots+x_{n}}{m}\right\rfloor \text{ for every } x_{1}, \ldots, x_{n} \in\{0,1, \ldots, m-1\} .
$$
Prove that the total degree of $f$ is at least $n$.



## 2019 — N3

**Record:** `imo_2019_05dd86`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_05dd86.json.gz).

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



## 2019 — N7

**Record:** `imo_2019_152467`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_152467.json.gz).

Prove that there is a constant $c>0$ and infinitely many positive integers $n$ with the following property: there are infinitely many positive integers that cannot be expressed as the sum of fewer than $c n \log (n)$ pairwise coprime $n^{\text{th}}$ powers.



## 2019 — C3

**Record:** `imo_2019_26d060`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_26d060.json.gz).

Let $n$ be a positive integer. Harry has $n$ coins lined up on his desk, each showing heads or tails. He repeatedly does the following operation: if there are $k$ coins showing heads and $k>0$, then he flips the $k^{\text{th}}$ coin over; otherwise he stops the process. (For example, the process starting with $T H T$ would be $T H T \rightarrow H H T \rightarrow H T T \rightarrow T T T$, which takes three steps.)

Letting $C$ denote the initial configuration (a sequence of $n H$'s and $T$'s), write $\ell(C)$ for the number of steps needed before all coins show $T$. Show that this number $\ell(C)$ is finite, and determine its average value over all $2^{n}$ possible initial configurations $C$.



## 2019 — C4

**Record:** `imo_2019_335dd1`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_335dd1.json.gz).

On a flat plane in Camelot, King Arthur builds a labyrinth $\mathfrak{L}$ consisting of $n$ walls, each of which is an infinite straight line. No two walls are parallel, and no three walls have a common point. Merlin then paints one side of each wall entirely red and the other side entirely blue.
At the intersection of two walls there are four corners: two diagonally opposite corners where a red side and a blue side meet, one corner where two red sides meet, and one corner where two blue sides meet. At each such intersection, there is a two-way door connecting the two diagonally opposite corners at which sides of different colours meet.
After Merlin paints the walls, Morgana then places some knights in the labyrinth. The knights can walk through doors, but cannot walk through walls.
Let $k(\mathfrak{L})$ be the largest number $k$ such that, no matter how Merlin paints the labyrinth $\mathfrak{L}$, Morgana can always place at least $k$ knights such that no two of them can ever meet. For each $n$, what are all possible values for $k(\mathfrak{L})$, where $\mathfrak{L}$ is a labyrinth with $n$ walls?



## 2019 — C8

**Record:** `imo_2019_486790`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_486790.json.gz).

Alice has a map of Wonderland, a country consisting of $n \geqslant 2$ towns. For every pair of towns, there is a narrow road going from one town to the other. One day, all the roads are declared to be "one way" only. Alice has no information on the direction of the roads, but the King of Hearts has offered to help her. She is allowed to ask him a number of questions. For each question in turn, Alice chooses a pair of towns and the King of Hearts tells her the direction of the road connecting those two towns.

Alice wants to know whether there is at least one town in Wonderland with at most one outgoing road. Prove that she can always find out by asking at most $4 n$ questions.



## 2019 — C7

**Record:** `imo_2019_51a004`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_51a004.json.gz).

There are 60 empty boxes $B_{1}, \ldots, B_{60}$ in a row on a table and an unlimited supply of pebbles. Given a positive integer $n$, Alice and Bob play the following game.

In the first round, Alice takes $n$ pebbles and distributes them into the 60 boxes as she wishes. Each subsequent round consists of two steps:

a. Bob chooses an integer $k$ with $1 \leqslant k \leqslant 59$ and splits the boxes into the two groups $B_{1}, \ldots, B_{k}$ and $B_{k+1}, \ldots, B_{60}$.

b. Alice picks one of these two groups, adds one pebble to each box in that group, and removes one pebble from each box in the other group.

Bob wins if, at the end of any round, some box contains no pebbles. Find the smallest $n$ such that Alice can prevent Bob from winning.



## 2019 — G8

**Record:** `imo_2019_7bd8a9`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_7bd8a9.json.gz).

Let $\mathcal{L}$ be the set of all lines in the plane and let $f$ be a function that assigns to each line $\ell \in \mathcal{L}$ a point $f(\ell)$ on $\ell$. Suppose that for any point $X$, and for any three lines $\ell_{1}, \ell_{2}, \ell_{3}$ passing through $X$, the points $f\left(\ell_{1}\right), f\left(\ell_{2}\right), f\left(\ell_{3}\right)$ and $X$ lie on a circle.
Prove that there is a unique point $P$ such that $f(\ell)=P$ for any line $\ell$ passing through $P$.



## 2019 — A1

**Record:** `imo_2019_abb25c`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_abb25c.json.gz).

Let $\mathbb{Z}$ be the set of integers. Determine all functions $f: \mathbb{Z} \rightarrow \mathbb{Z}$ such that, for all integers $a$ and $b$,
$$
f(2a) + 2f(b) = f(f(a+b)).
$$



## 2019 — N5

**Record:** `imo_2019_aedde5`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_aedde5.json.gz).

Let $a$ be a positive integer. We say that a positive integer $b$ is $a$-good if $\binom{a n}{b}-1$ is divisible by $a n+1$ for all positive integers $n$ with $a n \geqslant b$. Suppose $b$ is a positive integer such that $b$ is $a$-good, but $b+2$ is not $a$-good. Prove that $b+1$ is prime.



## 2019 — C5

**Record:** `imo_2019_c92128`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_c92128.json.gz).

On a certain social network, there are $2019$ users, some pairs of which are friends, where friendship is a symmetric relation. Initially, there are $1010$ people with $1009$ friends each and $1009$ people with $1010$ friends each. However, the friendships are rather unstable, so events of the following kind may happen repeatedly, one at a time:

Let $A$, $B$, and $C$ be people such that $A$ is friends with both $B$ and $C$, but $B$ and $C$ are not friends; then $B$ and $C$ become friends, but $A$ is no longer friends with them.

Prove that, regardless of the initial friendships, there exists a sequence of such events after which each user is friends with at most one other user.



## 2019 — N6

**Record:** `imo_2019_ce6a78`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_ce6a78.json.gz).

Let $H=\{\lfloor i \sqrt{2}\rfloor: i \in \mathbb{Z}_{>0}\}=\{1,2,4,5,7, \ldots\}$, and let $n$ be a positive integer. Prove that there exists a constant $C$ such that, if $A \subset\{1,2, \ldots, n\}$ satisfies $|A| \geqslant C \sqrt{n}$, then there exist $a, b \in A$ such that $a-b \in H$. (Here $\mathbb{Z}_{>0}$ is the set of positive integers, and $\lfloor z\rfloor$ denotes the greatest integer less than or equal to $z$.)



## 2019 — C2

**Record:** `imo_2019_e753a3`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_e753a3.json.gz).

You are given a set of $n$ blocks, each weighing at least $1$; their total weight is $2n$. Prove that for every real number $r$ with $0 \leqslant r \leqslant 2n-2$ you can choose a subset of the blocks whose total weight is at least $r$ but at most $r+2$.



## 2019 — C1

**Record:** `imo_2019_f43f3b`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_f43f3b.json.gz).

The infinite sequence $a_{0}, a_{1}, a_{2}, \ldots$ of (not necessarily different) integers has the following properties: $0 \leqslant a_{i} \leqslant i$ for all integers $i \geqslant 0$, and
$$
\binom{k}{a_{0}}+\binom{k}{a_{1}}+\cdots+\binom{k}{a_{k}}=2^{k}
$$
for all integers $k \geqslant 0$.
Prove that all integers $N \geqslant 0$ occur in the sequence (that is, for all $N \geqslant 0$, there exists $i \geqslant 0$ with $a_{i}=N$ ).



## 2019 — C9

**Record:** `imo_2019_fa57ae`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_fa57ae.json.gz).

For any two different real numbers $x$ and $y$, we define $D(x, y)$ to be the unique integer $d$ satisfying $2^{d} \leqslant |x-y| < 2^{d+1}$. Given a set of reals $\mathcal{F}$, and an element $x \in \mathcal{F}$, we say that the scales of $x$ in $\mathcal{F}$ are the values of $D(x, y)$ for $y \in \mathcal{F}$ with $x \neq y$.
Let $k$ be a given positive integer. Suppose that each member $x$ of $\mathcal{F}$ has at most $k$ different scales in $\mathcal{F}$ (note that these scales may depend on $x$). What is the maximum possible size of $\mathcal{F}$?



## 2020 — C1

**Record:** `imo_2020_19e099`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2020_19e099.json.gz).

Let $n$ be a positive integer. Find the number of permutations $a_{1}, a_{2}, \ldots, a_{n}$ of the sequence $1,2, \ldots, n$ satisfying
$$
a_{1} \leqslant 2 a_{2} \leqslant 3 a_{3} \leqslant \ldots \leqslant n a_{n}
$$



## 2020 — A1

**Record:** `imo_2020_48d762`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2020_48d762.json.gz).

Version 1. Let $n$ be a positive integer, and set $N=2^{n}$. Determine the smallest real number $a_{n}$ such that, for all real $x$,
$$
\sqrt[N]{\frac{x^{2 N}+1}{2}} \leqslant a_{n}(x-1)^{2}+x .
$$

Version 2. For every positive integer $N$, determine the smallest real number $b_{N}$ such that, for all real $x$,
$$
\sqrt[N]{\frac{x^{2 N}+1}{2}} \leqslant b_{N}(x-1)^{2}+x
$$
(Ireland)



## 2020 — C7

**Record:** `imo_2020_9168c0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2020_9168c0.json.gz).

Consider any rectangular table having finitely many rows and columns, with a real number $a(r, c)$ in the cell in row $r$ and column $c$. A pair ($R, C$), where $R$ is a set of rows and $C$ a set of columns, is called a saddle pair if the following two conditions are satisfied:
(i) For each row $r'$, there is $r \in R$ such that $a(r, c) \geqslant a(r', c)$ for all $c \in C$;
(ii) For each column $c'$, there is $c \in C$ such that $a(r, c) \leqslant a(r, c')$ for all $r \in R$.
A saddle pair ($R, C$) is called a minimal pair if for each saddle pair ($R', C'$) with $R' \subseteq R$ and $C' \subseteq C$, we have $R' = R$ and $C' = C$.
Prove that any two minimal pairs contain the same number of rows.



## 2020 — C2

**Record:** `imo_2020_c1c2cc`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2020_c1c2cc.json.gz).

In a regular 100-gon, 41 vertices are colored black and the remaining 59 vertices are colored white. Prove that there exist 24 convex quadrilaterals $Q_{1}, \ldots, Q_{24}$ whose corners are vertices of the 100-gon, so that
- the quadrilaterals $Q_{1}, \ldots, Q_{24}$ are pairwise disjoint, and
- every quadrilateral $Q_{i}$ has three corners of one color and one corner of the other color.



## 2020 — C6

**Record:** `imo_2020_e10061`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2020_e10061.json.gz).

$4 n$ coins of weights $1, 2, 3, \ldots, 4 n$ are given. Each coin is colored in one of $n$ colors and there are four coins of each color. Show that all these coins can be partitioned into two sets with the same total weight, such that each set contains two coins of each color.
(Hungary)



## 2021 — N4

**Record:** `imo_2021_1c3cfc`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_1c3cfc.json.gz).

Alice is given a rational number $r>1$ and a line with two points $B \neq R$, where point $R$ contains a red bead and point $B$ contains a blue bead. Alice plays a solitaire game by performing a sequence of moves. In every move, she chooses a (not necessarily positive) integer $k$, and a bead to move. If that bead is placed at point $X$, and the other bead is placed at $Y$, then Alice moves the chosen bead to point $X^{\prime}$ with $\overrightarrow{Y X^{\prime}}=r^{k} \overrightarrow{Y X}$.

Alice's goal is to move the red bead to the point $B$. Find all rational numbers $r>1$ such that Alice can reach her goal in at most 2021 moves.



## 2021 — C8

**Record:** `imo_2021_4e49c6`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_4e49c6.json.gz).

Determine the largest $N$ for which there exists a table $T$ of integers with $N$ rows and 100 columns that has the following properties:
(i) Every row contains the numbers $1,2, \ldots, 100$ in some order.
(ii) For any two distinct rows $r$ and $s$, there is a column $c$ such that $|T(r, c)-T(s, c)| \geqslant 2$.
Here $T(r, c)$ means the number at the intersection of the row $r$ and the column $c$.



## 2021 — C1

**Record:** `imo_2021_5bfb5f`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_5bfb5f.json.gz).

Let $S$ be an infinite set of positive integers, such that there exist four pairwise distinct $a, b, c, d \in S$ with $\operatorname{gcd}(a, b) \neq \operatorname{gcd}(c, d)$. Prove that there exist three pairwise distinct $x, y, z \in S$ such that $\operatorname{gcd}(x, y)=\operatorname{gcd}(y, z) \neq \operatorname{gcd}(z, x)$.



## 2021 — N6

**Record:** `imo_2021_862aab`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_862aab.json.gz).

Determine all integers $n \geqslant 2$ with the following property: every $n$ pairwise distinct integers whose sum is not divisible by $n$ can be arranged in some order $a_{1}, a_{2}, \ldots, a_{n}$ so that $n$ divides $1 \cdot a_{1}+2 \cdot a_{2}+\cdots+n \cdot a_{n}$.



## 2021 — C3

**Record:** `imo_2021_a06079`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_a06079.json.gz).

A thimblerigger has 2021 thimbles numbered from 1 through 2021. The thimbles are arranged in a circle in arbitrary order. The thimblerigger performs a sequence of 2021 moves; in the $k^{\text{th}}$ move, he swaps the positions of the two thimbles adjacent to thimble $k$.
Prove that there exists a value of $k$ such that, in the $k^{\text{th}}$ move, the thimblerigger swaps some thimbles $a$ and $b$ such that $a < k < b$.



## 2021 — C4

**Record:** `imo_2021_a8deb3`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_a8deb3.json.gz).

The kingdom of Anisotropy consists of $n$ cities. For every two cities there exists exactly one direct one-way road between them. We say that a path from $X$ to $Y$ is a sequence of roads such that one can move from $X$ to $Y$ along this sequence without returning to an already visited city. A collection of paths is called diverse if no road belongs to two or more paths in the collection.
Let $A$ and $B$ be two distinct cities in Anisotropy. Let $N_{A B}$ denote the maximal number of paths in a diverse collection of paths from $A$ to $B$. Similarly, let $N_{B A}$ denote the maximal number of paths in a diverse collection of paths from $B$ to $A$. Prove that the equality $N_{A B}=N_{B A}$ holds if and only if the number of roads going out from $A$ is the same as the number of roads going out from $B$.



## 2021 — C6

**Record:** `imo_2021_b0420a`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_b0420a.json.gz).

A hunter and an invisible rabbit play a game on an infinite square grid. First the hunter fixes a colouring of the cells with finitely many colours. The rabbit then secretly chooses a cell to start in. Every minute, the rabbit reports the colour of its current cell to the hunter, and then secretly moves to an adjacent cell that it has not visited before (two cells are adjacent if they share a side). The hunter wins if after some finite time either
- the rabbit cannot move; or
- the hunter can determine the cell in which the rabbit started.
Decide whether there exists a winning strategy for the hunter.



## 2021 — C2

**Record:** `imo_2021_da9f3d`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_da9f3d.json.gz).

Let $n \geqslant 3$ be an integer. An integer $m \geqslant n+1$ is called $n$-colourful if, given infinitely many marbles in each of $n$ colours $C_{1}, C_{2}, \ldots, C_{n}$, it is possible to place $m$ of them around a circle so that in any group of $n+1$ consecutive marbles there is at least one marble of colour $C_{i}$ for each $i=1, \ldots, n$.
Prove that there are only finitely many positive integers which are not $n$-colourful. Find the largest among them.



## 2021 — A3

**Record:** `imo_2021_f2791d`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_f2791d.json.gz).

Given a positive integer $n$, find the smallest value of
$$
\left\lfloor\frac{a_{1}}{1}\right\rfloor+\left\lfloor\frac{a_{2}}{2}\right\rfloor+\cdots+\left\lfloor\frac{a_{n}}{n}\right\rfloor
$$
over all permutations $(a_{1}, a_{2}, \ldots, a_{n})$ of $(1,2, \ldots, n)$.



## 2021 — C7

**Record:** `imo_2021_fbb8aa`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2021_fbb8aa.json.gz).

Consider a checkered $3m \times 3m$ square, where $m$ is an integer greater than $1$. A frog sits on the lower left corner cell $S$ and wants to get to the upper right corner cell $F$. The frog can hop from any cell to either the next cell to the right or the next cell upwards.

Some cells can be sticky, and the frog gets trapped once it hops on such a cell. A set $X$ of cells is called blocking if the frog cannot reach $F$ from $S$ when all the cells of $X$ are sticky. A blocking set is minimal if it does not contain a smaller blocking set.

a. Prove that there exists a minimal blocking set containing at least $3m^{2} - 3m$ cells.

b. Prove that every minimal blocking set contains at most $3m^{2}$ cells.

Note. An example of a minimal blocking set for $m=2$ is shown below. Cells of the set $X$ are marked by letters $x$.

|   |   |   |   |   | $F$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $x$ | $x$ |   |   |   |   |
|   |   | $x$ |   |   |   |
|   |   |   | $x$ |   |   |
|   |   |   |   | $x$ |   |
| $S$ |   | $x$ |   |   |   |



## 2022 — A8.

**Record:** `imo_2022_1937c6`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2022_1937c6.json.gz).

For a positive integer $n$, an $n$-sequence is a sequence $(a_{0}, \ldots, a_{n})$ of non-negative integers satisfying the following condition: if $i$ and $j$ are non-negative integers with $i+j \leqslant n$, then $a_{i}+a_{j} \leqslant n$ and $a_{a_{i}+a_{j}}=a_{i+j}$.
Let $f(n)$ be the number of $n$-sequences. Prove that there exist positive real numbers $c_{1}, c_{2}$ and $\lambda$ such that
$$
c_{1} \lambda^{n}<f(n)<c_{2} \lambda^{n}
$$
for all positive integers $n$.



## 2022 — N8.

**Record:** `imo_2022_264ed6`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2022_264ed6.json.gz).

Prove that $5^{n}-3^{n}$ is not divisible by $2^{n}+65$ for any positive integer $n$.



## 2022 — C8.

**Record:** `imo_2022_34151b`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2022_34151b.json.gz).

Alice fills the fields of an $n \times n$ board with numbers from $1$ to $n^{2}$, each number being used exactly once. She then counts the total number of good paths on the board. A good path is a sequence of fields of arbitrary length (including $1$) such that:
(i) The first field in the sequence is one that is only adjacent to fields with larger numbers,
(ii) Each subsequent field in the sequence is adjacent to the previous field,
(iii) The numbers written on the fields in the sequence are in increasing order.

Two fields are considered adjacent if they share a common side. Find the smallest possible number of good paths Alice can obtain, as a function of $n$.



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



## 2022 — C6.

**Record:** `imo_2022_783196`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2022_783196.json.gz).

Let $n$ be a positive integer. We start with $n$ piles of pebbles, each initially containing a single pebble. One can perform moves of the following form: choose two piles, take an equal number of pebbles from each pile and form a new pile out of these pebbles. For each positive integer $n$, find the smallest number of non-empty piles that one can obtain by performing a finite sequence of moves of this form.



## 2022 — C2.

**Record:** `imo_2022_b034b8`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2022_b034b8.json.gz).

The Bank of Oslo issues coins made out of two types of metal: aluminium (denoted $A$) and copper (denoted $C$). Morgane has $n$ aluminium coins, and $n$ copper coins, and arranges her $2n$ coins in a row in some arbitrary initial order. Given a fixed positive integer $k \leqslant 2n$, she repeatedly performs the following operation: identify the largest subsequence containing the $k$-th coin from the left which consists of consecutive coins made of the same metal, and move all coins in that subsequence to the left end of the row. For example, if $n=4$ and $k=4$, the process starting from the configuration $A A C C C A C A$ would be
$$
A A C C C A C A \rightarrow C C C A A A C A \rightarrow A A A C C C C A \rightarrow C C C C A A A A \rightarrow \cdots .
$$
Find all pairs $(n, k)$ with $1 \leqslant k \leqslant 2n$ such that for every initial configuration, at some point of the process there will be at most one aluminium coin adjacent to a copper coin.



## 2022 — N5.

**Record:** `imo_2022_d417bb`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2022_d417bb.json.gz).

For each $1 \leqslant i \leqslant 9$ and $T \in \mathbb{N}$, define $d_{i}(T)$ to be the total number of times the digit $i$ appears when all the multiples of $1829$ between $1$ and $T$ inclusive are written out in base $10$.
Show that there are infinitely many $T \in \mathbb{N}$ such that there are precisely two distinct values among $d_{1}(T), d_{2}(T), \ldots, d_{9}(T)$.



## 2022 — C1.

**Record:** `imo_2022_e5b1cb`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2022_e5b1cb.json.gz).

A $\pm 1$-sequence is a sequence of $2022$ numbers $a_{1}, \ldots, a_{2022}$, each equal to either $+1$ or $-1$. Determine the largest $C$ so that, for any $\pm 1$-sequence, there exists an integer $k$ and indices $1 \leqslant t_{1}<\ldots<t_{k} \leqslant 2022$ so that $t_{i+1}-t_{i} \leqslant 2$ for all $i$, and
$$
\left|\sum_{i=1}^{k} a_{t_{i}}\right| \geqslant C.
$$



## 2023 — C4.

**Record:** `imo_2023_375cf9`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2023_375cf9.json.gz).

Let $n \geqslant 2$ be a positive integer. Paul has a $1 \times n^{2}$ rectangular strip consisting of $n^{2}$ unit squares, where the $i^{\text{th}}$ square is labelled with $i$ for all $1 \leqslant i \leqslant n^{2}$. He wishes to cut the strip into several pieces, where each piece consists of a number of consecutive unit squares, and then translate (without rotating or flipping) the pieces to obtain an $n \times n$ square satisfying the following property: if the unit square in the $i^{\text{th}}$ row and $j^{\text{th}}$ column is labelled with $a_{ij}$, then $a_{ij}-(i+j-1)$ is divisible by $n$.

Determine the smallest number of pieces Paul needs to make in order to accomplish this.



## 2023 — C7.

**Record:** `imo_2023_73cc8d`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2023_73cc8d.json.gz).

The Imomi archipelago consists of $n \geqslant 2$ islands. Between each pair of distinct islands is a unique ferry line that runs in both directions, and each ferry line is operated by one of $k$ companies. It is known that if any one of the $k$ companies closes all its ferry lines, then it becomes impossible for a traveller, no matter where the traveller starts at, to visit all the islands exactly once (in particular, not returning to the island the traveller started at).
Determine the maximal possible value of $k$ in terms of $n$.



## 2023 — A5.

**Record:** `imo_2023_76bf3b`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2023_76bf3b.json.gz).

Let $a_{1}, a_{2}, \ldots, a_{2023}$ be positive integers such that
- $a_{1}, a_{2}, \ldots, a_{2023}$ is a permutation of $1,2, \ldots, 2023$, and
- $\left|a_{1}-a_{2}\right|,\left|a_{2}-a_{3}\right|, \ldots,\left|a_{2022}-a_{2023}\right|$ is a permutation of $1,2, \ldots, 2022$.
Prove that $\max \left(a_{1}, a_{2023}\right) \geqslant 507$.



## 2023 — C5.

**Record:** `imo_2023_913777`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2023_913777.json.gz).

Elisa has 2023 treasure chests, all of which are unlocked and empty at first. Each day, Elisa adds a new gem to one of the unlocked chests of her choice, and afterwards, a fairy acts according to the following rules:
- if more than one chests are unlocked, it locks one of them, or
- if there is only one unlocked chest, it unlocks all the chests.
Given that this process goes on forever, prove that there is a constant $C$ with the following property: Elisa can ensure that the difference between the numbers of gems in any two chests never exceeds $C$, regardless of how the fairy chooses the chests to lock.



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



## 2024 — C2

**Record:** `imo_2024_0968d7`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2024_0968d7.json.gz).

Let $n$ be a positive integer. The integers $1, 2, 3, \ldots, n^{2}$ are to be written in the cells of an $n \times n$ board such that each integer is written in exactly one cell and each cell contains exactly one integer. For every integer $d$ with $d \mid n$, the $d$-division of the board is the division of the board into $(n / d)^{2}$ nonoverlapping sub-boards, each of size $d \times d$, such that each cell is contained in exactly one $d \times d$ sub-board.

We say that $n$ is a cool number if the integers can be written on the $n \times n$ board such that, for each integer $d$ with $d \mid n$ and $1 < d < n$, in the $d$-division of the board, the sum of the integers written in each $d \times d$ sub-board is not a multiple of $d$.

Determine all even cool numbers.



## 2024 — C5

**Record:** `imo_2024_1fd9d0`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2024_1fd9d0.json.gz).

Let $N$ be a positive integer. Geoff and Ceri play a game in which they start by writing the numbers $1, 2, \ldots, N$ on a board. They then take turns to make a move, starting with Geoff. Each move consists of choosing a pair of integers $(k, n)$, where $k \geqslant 0$ and $n$ is one of the integers on the board, and then erasing every integer $s$ on the board such that $2^{k} \mid n-s$. The game continues until the board is empty. The player who erases the last integer on the board loses.

Determine all values of $N$ for which Geoff can ensure that he wins, no matter how Ceri plays.

(Indonesia)



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



## 2024 — C8

**Record:** `imo_2024_34fef6`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2024_34fef6.json.gz).

Let $n$ be a positive integer. Given an $n \times n$ board, the unit cell in the top left corner is initially coloured black, and the other cells are coloured white. We then apply a series of colouring operations to the board. In each operation, we choose a $2 \times 2$ square with exactly one cell coloured black and we colour the remaining three cells of that $2 \times 2$ square black.

Determine all values of $n$ such that we can colour the whole board black.
(Peru)



## 2024 — N6

**Record:** `imo_2024_3f4e9a`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2024_3f4e9a.json.gz).

Let $n$ be a positive integer. We say that a polynomial $P$ with integer coefficients is $n$-good if there exists a polynomial $Q$ of degree 2 with integer coefficients such that $Q(k)(P(k)+Q(k))$ is never divisible by $n$ for any integer $k$.
Determine all integers $n$ such that every polynomial with integer coefficients is an $n$-good polynomial.



## 2024 — A2

**Record:** `imo_2024_5877d2`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2024_5877d2.json.gz).

Let $n$ be a positive integer. Find the minimum possible value of
$$
S = 2^{0} x_{0}^{2} + 2^{1} x_{1}^{2} + \cdots + 2^{n} x_{n}^{2}
$$
where $x_{0}, x_{1}, \ldots, x_{n}$ are nonnegative integers such that $x_{0} + x_{1} + \cdots + x_{n} = n$.



## 2024 — C1

**Record:** `imo_2024_657c6a`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2024_657c6a.json.gz).

Let $n$ be a positive integer. A class of $n$ students run $n$ races, in each of which they are ranked with no draws. A student is eligible for a rating $(a, b)$ for positive integers $a$ and $b$ if they come in the top $b$ places in at least $a$ of the races. Their final score is the maximum possible value of $a-b$ across all ratings for which they are eligible.
Find the maximum possible sum of all the scores of the $n$ students.



## 2024 — N7

**Record:** `imo_2024_7201b9`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2024_7201b9.json.gz).

Let $\mathbb{Z}_{>0}$ denote the set of positive integers. Let $f: \mathbb{Z}_{>0} \rightarrow \mathbb{Z}_{>0}$ be a function satisfying the following property: for $m, n \in \mathbb{Z}_{>0}$, the equation
$$
f(m n)^2 = f\left(m^2\right) f(f(n)) f(m f(n))
$$
holds if and only if $m$ and $n$ are coprime.
For each positive integer $n$, determine all the possible values of $f(n)$.



## 2024 — C4

**Record:** `imo_2024_7579e8`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2024_7579e8.json.gz).

On a board with $2024$ rows and $2023$ columns, Turbo the snail tries to move from the first row to the last row. On each attempt, he chooses to start on any cell in the first row, then moves one step at a time to an adjacent cell sharing a common side. He wins if he reaches any cell in the last row. However, there are $2022$ predetermined, hidden monsters in $2022$ of the cells, one in each row except the first and last rows, such that no two monsters share the same column. If Turbo unfortunately reaches a cell with a monster, his attempt ends and he is transported back to the first row to start a new attempt. The monsters do not move.
Suppose Turbo is allowed to take $n$ attempts. Determine the minimum value of $n$ for which he has a strategy that guarantees reaching the last row, regardless of the locations of the monsters.
(Hong Kong)

Comment. One of the main difficulties of solving this question is in determining the correct expression for $n$. Students may spend a long time attempting to prove bounds for the wrong value for $n$ before finding better strategies.
Students may incorrectly assume that Turbo is not allowed to backtrack to squares he has already visited within a single attempt. Fortunately, making this assumption does not change the answer to the problem, though it may make it slightly harder to find a winning strategy.



## 2024 — C6

**Record:** `imo_2024_91fd1f`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2024_91fd1f.json.gz).

Let $n$ and $T$ be positive integers. James has $4 n$ marbles with weights $1,2, \ldots, 4 n$. He places them on a balance scale, so that both sides have equal weight. Andrew may move a marble from one side of the scale to the other, so that the absolute difference in weights of the two sides remains at most $T$.
Find, in terms of $n$, the minimum positive integer $T$ such that Andrew may make a sequence of moves such that each marble ends up on the opposite side of the scale, regardless of how James initially placed the marbles.



## 2024 — C7

**Record:** `imo_2024_95e706`. **Category:** shortlist. [Source](https://mathnet.mit.edu/data_v2/full/imo/imo_2024_95e706.json.gz).

Let $N$ be a positive integer and let $a_{1}, a_{2}, \ldots$ be an infinite sequence of positive integers. Suppose that, for each $n > N$, $a_{n}$ is equal to the number of times $a_{n-1}$ appears in the list $a_{1}, a_{2}, \ldots, a_{n-1}$.
Prove that at least one of the sequences $a_{1}, a_{3}, a_{5}, \ldots$ and $a_{2}, a_{4}, a_{6}, \ldots$ is eventually periodic.



# IMO-TST


## Year unknown — Problem 2

**Record:** `usa_87d02d`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_87d02d.json.gz).

Let $f(n)$ be the minimal number of colors needed to properly color the directed edges of a tournament on $n$ vertices so that no two edges of the same color form a directed path of length $2$. Determine $f(n)$ for all $n \ge 1$.



## 2001 — 9

**Record:** `usa_2001_419b80`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2001_419b80.json.gz).

Let $A$ be a finite set of positive integers. Prove that there exists a finite set $B$ of positive integers such that $A \subseteq B$ and
$$
\prod_{x \in B} x = \sum_{x \in B} x^2.
$$



## 2001 — 4

**Record:** `usa_2001_77e185`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2001_77e185.json.gz).

There are 51 senators in a senate. The senate needs to be divided into $n$ committees so that each senator is on one committee. Each senator hates exactly three other senators. (If senator $A$ hates senator $B$, then senator $B$ does *not* necessarily hate senator $A$.) Find the smallest $n$ such that it is always possible to arrange the committees so that no senator hates another senator on his or her committee.



## 2001 — 3

**Record:** `usa_2001_8a88f8`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2001_8a88f8.json.gz).

Twenty-one girls and twenty-one boys took part in a mathematical competition. It turned out that

a. each contestant solved at most six problems, and

b. for each pair of a girl and a boy, there was at least one problem that was solved by both the girl and the boy.

Prove that there is a problem that was solved by at least three girls and at least three boys.



## 2001 — 4

**Record:** `usa_2001_9b2113`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2001_9b2113.json.gz).

Let $n$ be an odd integer greater than $1$ and let $c_1, c_2, \dots, c_n$ be integers. For each permutation $a = (a_1, a_2, \dots, a_n)$ of $\{1, 2, \dots, n\}$, define $S(a) = \sum_{i=1}^n c_i a_i$. Prove that there exist permutations $b$ and $c$, $b \neq c$, such that $n!$ divides $S(b) - S(c)$.



## 2001 — 2

**Record:** `usa_2001_a0d6f2`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2001_a0d6f2.json.gz).

Express
$$
\sum_{k=0}^{n} (-1)^k (n-k)!(n+k)!
$$
in closed form.



## 2001 — 3

**Record:** `usa_2001_e83e65`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2001_e83e65.json.gz).

For a set $S$, let $|S|$ denote the number of elements in $S$. Let $A$ be a set of positive integers with $|A| = 2001$. Prove that there exists a set $B$ such that
(i) $B \subseteq A$;
(ii) $|B| \geq 668$;
(iii) for any $u, v \in B$ (not necessarily distinct), $u + v \notin B$.



## 2001 — 3

**Record:** `vnm_2001_603cc9`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2001_603cc9.json.gz).

A club has $42$ participants. In each group of $31$ participants of this club, there is always an acquainted couple man - woman. Prove that in this club, we can select $12$ acquainted couples.



## 2001 — 5

**Record:** `vnm_2001_644f7b`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2001_644f7b.json.gz).

Let be given an integer $n > 1$ and an orthonormal system of coordinates $Oxyz$ in space. Let $T$ be the set of all points $P(x, y, z)$, the coordinates $x, y, z$ of which are integers satisfying the conditions $1 \le x, y, z \le n$. Colour some points in $T$ so that if the point $A(x_0, y_0, z_0)$ had been coloured then every point $B(x_1, y_1, z_1)$ with $x_1 \le x_0, y_1 \le y_0, z_1 \le z_0$ ($B \ne A$) could not be coloured. How many points at most can be coloured?



## 2001 — 6

**Record:** `vnm_2001_95fe00`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2001_95fe00.json.gz).

Let be given a sequence of positive integers $\{a_n\}$, $n = 1, 2, 3, \ldots$, satisfying the condition
$$
0 < a_{n+1} - a_n \le 2001
$$
for every $n = 1, 2, 3, \ldots$. Prove that there exists an infinite number of couples of positive integers $(p, q)$ such that $p < q$ and $a_p$ is a divisor of $a_q$.



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



## 2003 — 1

**Record:** `vnm_2003_5c9cad`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2003_5c9cad.json.gz).

Let be given four positive integers $m, n, p, q$, with $p < m$ and $q < n$. Take the four points $A(0; 0)$, $B(p; 0)$, $C(m; q)$ and $D(m; n)$ in the coordinate plane.

Consider the paths $f$ from $A$ to $D$ and the paths $g$ from $B$ to $C$ such that when going along $f$ or $g$, one goes only in the positive directions of the axes of coordinates and one can only change directions (from the positive direction of one axe of coordinate into the positive direction of the other axe of coordinate) at the points with integral coordinates.

Let $S$ be the number of couples $(f, g)$ such that $f$ and $g$ have no common point. Prove that
$$
S = C_{m+n}^{p} \cdot C_{m+q-p}^{q} - C_{m+q}^{p} \cdot C_{m+n-p}^{q}.
$$



## 2003 — 5

**Record:** `vnm_2003_767bbb`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2003_767bbb.json.gz).

Let $A$ be the set of all permutations $a = (a_1, a_2, ..., a_{2003})$ of $2003$ first positive integers such that each permutation satisfies the condition: there is no nonvoid proper subset $S$ of the set $\{1, 2, ..., 2003\}$ such that $\{a_k \mid k \in S\} = S$.

For each $a = (a_1, a_2, ..., a_{2003}) \in A$, put $d(a) = \sum_{k=1}^{2003} (a_k - k)^2$.

a. Find the least value of $d(a)$. Denote this least value by $d_0$.

b. Find all permutations $a \in A$ such that $d(a) = d_0$.



## 2004 — 4

**Record:** `usa_2004_8f5af1`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2004_8f5af1.json.gz).

Alice and Bob play a game on a $6$ by $6$ grid. On his or her turn, a player chooses a rational number not yet appearing in the grid and writes it in an empty square of the grid. Alice goes first and then the players alternate. When all squares have numbers written in them, in each row, the square with the greatest number in that row is colored black. Alice wins if she can then draw a line from the top of the grid to the bottom of the grid that stays in black squares, and Bob wins if she can't. (If two squares share a vertex, Alice can draw a line from one to the other that stays in those two squares.) Find, with proof, a winning strategy for one of the players.



## 2004 — 3

**Record:** `usa_2004_954202`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2004_954202.json.gz).

A $2004 \times 2004$ array of points is drawn. Find the largest integer $n$ such that it is possible to draw a convex $n$-sided polygon whose vertices lie on the points of the array.



## 2004 — 2

**Record:** `usa_2004_cbf0f1`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2004_cbf0f1.json.gz).

Let $n$ be a positive integer. Consider sequences $a_0, a_1, \dots, a_n$ such that $a_i \in \{1, 2, \dots, n\}$ for each $i$ and $a_n = a_0$.

a. Call such a sequence *good* if for all $i = 1, 2, \dots, n$, $a_i - a_{i-1} \not\equiv i \pmod n$. Suppose that $n$ is odd. Find the number of good sequences.

b. Call such a sequence *great* if for all $i = 1, 2, \dots, n$, $a_i - a_{i-1} \not\equiv i, 2i \pmod n$. Suppose that $n$ is an odd prime. Find the number of great sequences.



## 2006 — 1

**Record:** `usa_2006_6ff7ae`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2006_6ff7ae.json.gz).

A communications network consisting of some terminals is called a 3-connector if among any three terminals, some two of them can directly communicate with each other. A communications network contains a windmill with $n$ blades if there exist $n$ pairs of terminals $\{x_1, y_1\}, \dots, \{x_n, y_n\}$ such that each $x_i$ can directly communicate with the corresponding $y_i$ and there is a hub terminal that can directly communicate with each of the $2n$ terminals $x_1, y_1, \dots, x_n, y_n$. Determine the minimum value of $f(n)$, in terms of $n$, such that a 3-connector with $f(n)$ terminals always contains a windmill with $n$ blades.



## 2006 — 5

**Record:** `usa_2006_b160c2`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2006_b160c2.json.gz).

Let $n$ be a given integer with $n$ greater than $7$, and let $\mathcal{P}$ be a convex polygon with $n$ sides. Any set of $n-3$ diagonals of $\mathcal{P}$ that do not intersect in the interior of the polygon determine a triangulation of $\mathcal{P}$ into $n-2$ triangles. A triangle in the triangulation of $\mathcal{P}$ is an interior triangle if all of its sides are diagonals of $\mathcal{P}$.

Express, in terms of $n$, the number of triangulations of $\mathcal{P}$ with exactly two interior triangles, in closed form.



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



## 2008 — 5

**Record:** `usa_2008_cbf07d`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2008_cbf07d.json.gz).

Two sequences of integers, $a_1, a_2, a_3, \dots$ and $b_1, b_2, b_3, \dots$, satisfy the equation
$$
(a_n - a_{n-1})(a_n - a_{n-2}) + (b_n - b_{n-1})(b_n - b_{n-2}) = 0
$$
for each integer $n$ greater than $2$. Prove that there is a positive integer $k$ such that $a_k = a_{k+2008}$.



## 2008 — 3

**Record:** `usa_2008_de1133`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2008_de1133.json.gz).

For a pair $A = (x_1, y_1)$ and $B = (x_2, y_2)$ of points on the coordinate plane, let $d(A, B) = |x_1 - x_2| + |y_1 - y_2|$. We call a pair $(A, B)$ of (unordered) points *harmonic* if $1 < d(A, B) \le 2$. Determine the maximum number of harmonic pairs among 100 points on the plane.

(This problem was suggested by Zuming Feng and Oleg Golberg.)



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



## 2009 — 6

**Record:** `usa_2009_ef3309`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2009_ef3309.json.gz).

Let $N > M > 1$ be fixed integers. There are $N$ people playing in a chess tournament; each pair of players plays each other once, with no draws. It turns out that for each sequence of $M + 1$ distinct players $P_0, P_1, \dots, P_M$ such that $P_{i-1}$ beat $P_i$ for each $i = 1, \dots, M$, player $P_0$ also beat $P_M$. Prove that the players can be numbered $1, 2, \dots, N$ in such a way that, whenever $a \ge b + M - 1$, player $a$ beat player $b$.



## 2009 — 1

**Record:** `usa_2009_f1ac89`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2009_f1ac89.json.gz).

Let $m$ and $n$ be positive integers. Mr. Fat has a set $S$ containing every rectangular tile with integer side lengths and area a power of $2$. Mr. Fat also has a rectangle $R$ with dimensions $2^m \times 2^n$ and a $1 \times 1$ square removed from one of the corners. Mr. Fat wants to choose $m + n$ rectangles from $S$, with respective areas $2^0, 2^1, \dots, 2^{m+n-1}$, and then tile $R$ with the chosen rectangles. Prove that this can be done in at most $(m+n)!$ ways.



## 2010 — 5

**Record:** `ind_2010_051b62`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2010_051b62.json.gz).

Let $A = (a_{jk})$ be a $10 \times 10$ array of positive real numbers such that the sum of numbers in each row as well as in each column is $1$. Show that there exist $j < k$ and $l < m$ such that
$$
a_{jl}a_{km} + a_{jm}a_{kl} \geq \frac{1}{50}
$$



## 2010 — 10

**Record:** `sgp_2010_5727a3`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/singapore/sgp_2010_5727a3.json.gz).

Let $A$ be a set of positive integers and let $k$ be a positive integer. Set $A$ is said to be $k$-thin if there are $k$ positive integers $n_1, \dots, n_k$ so that for all $1 \le i < j \le k$ and all $a, a' \in A$, $n_i + a \ne n_j + a'$. Suppose that $A_r$ is a $k_r$-thin set for $1 \le r \le m$ and that $\cup_{r=1}^m A_r$ is the set of all positive integers. Show that
$$
\frac{1}{k_1} + \dots + \frac{1}{k_m} \ge 1.
$$



## 2010 — 6

**Record:** `sgp_2010_6c0264`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/singapore/sgp_2010_6c0264.json.gz).

Determine all finite sets $A$ of non-negative real numbers, containing at least four elements, and such that for all distinct $a, b, c, d \in A$, $ab + cd \in A$.



## 2010 — 8

**Record:** `sgp_2010_7e3a81`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/singapore/sgp_2010_7e3a81.json.gz).

Let $n$ be an integer $\ge 2$. Let $S$ be a set of triples of nonnegative integers $(a, b, c)$ such that $a + b + c = n$ and if $(a, b, c)$ and $(a', b', c')$ are distinct triples in $S$, then $a \ne a'$, $b \ne b'$ and $c \ne c'$. Find the maximum value of $|S|$.



## 2010 — 2

**Record:** `sgp_2010_c6cc18`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/singapore/sgp_2010_c6cc18.json.gz).

A subset $T$ of $\{7, 8, ..., 26\}$ does not contain three elements whose product is a perfect square. Determine the maximum number of elements in $T$.



## 2010 — 6

**Record:** `usa_2010_061aff`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2010_061aff.json.gz).

Let $T$ be a finite set of positive integers greater than $1$. A subset $S$ of $T$ is called *good*, if for every $t \in T$ there exists some $s \in S$ with $\gcd(s, t) > 1$. Prove that the number of good subsets of $T$ is odd.



## 2010 — 8

**Record:** `usa_2010_773ef5`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2010_773ef5.json.gz).

Let $m$, $n$ be positive integers with $m \ge n$, and let $S$ be the set of all ordered $n$-tuples $(a_1, a_2, \dots, a_n)$ of positive integers such that $a_1 + a_2 + \dots + a_n = m$. Show that
$$
\sum_{S} 1^{a_1} 2^{a_2} \cdots n^{a_n} = \binom{n}{n} n^m - \binom{n}{n-1} (n-1)^m + \cdots + (-1)^{n-2} \binom{n}{2} 2^m + \cdots + (-1)^{n-1} \binom{n}{1}.
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



## 2010 — Problem 5

**Record:** `vnm_2010_5c6598`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2010_5c6598.json.gz).

$n$ countries send delegates to an international Festival, each country send $k$ delegates ($n$ and $k$ are integers satisfying $n > k > 1$). The organizing committee of the Festival divides $nk$ delegates into $n$ discussion groups, each group consists of $k$ delegates. Show that one can choose $n$ delegates, in such a way that each group has one delegate be selected and each country has one delegate be selected.



## 2011 — 4

**Record:** `ind_2011_9fc5bb`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2011_9fc5bb.json.gz).

Let $(a_0, a_1, a_2, ...)$ and $(b_0, b_1, b_2, ...)$ be two infinite sequences of integers such that
$$
(a_n - a_{n-1})(a_n - a_{n-2}) + (b_n - b_{n-1})(b_n - b_{n-2}) = 0,
$$
for all integers $n \ge 2$. Prove that there exists a positive integer $K$ such that
$$
a_{K+2011} = a_{K+(2011)^{2011}}.
$$



## 2011 — 5

**Record:** `usa_2011_02c62b`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2011_02c62b.json.gz).

Let $c_n$ be a sequence which is defined recursively as follows: $c_0 = 1$, $c_{2n+1} = c_n$ for $n \ge 0$, and $c_{2n} = c_n + c_{n-2^e}$ for $n > 0$ where $e$ is the maximal nonnegative integer such that $2^e$ divides $n$. Prove that
$$
\sum_{i=0}^{2^n-1} c_i = \frac{1}{n+2} \binom{2n+2}{n+1}.
$$



## 2011 — 8

**Record:** `usa_2011_5c5516`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2011_5c5516.json.gz).

Let $n \ge 1$ be an integer, and let $S$ be a set of integer pairs $(a, b)$ with $1 \le a < b \le 2^n$. Assume $|S| > n \cdot 2^{n+1}$. Prove that there exist four integers $a < b < c < d$ such that $S$ contains all three pairs $(a, c)$, $(b, d)$ and $(a, d)$.



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



## 2011 — 6

**Record:** `vnm_2011_c8e35c`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2011_c8e35c.json.gz).

Let $n$ be an integer larger than $1$. There are $n$ students sitting at a round table, each is given a number of candies (some students may receive no candies) and the sum of the candies of all students is a multiple of $n$. The students transfer the candies to each other in the following way:

With the candies given at the beginning, if there is at least one student having more candies than the one sitting on his right, then an (arbitrary) student among such students transfers one candy to the student sitting on his right. With the candies that each student are having now, if there is at least one student having more candies than the one sitting on his right, then an (arbitrary) student among such students transfers one candy to the student sitting on his right. The process of candy transferring goes on this way.

Show that after a finite number of candy transfers, the students have the same number of candies.



## 2011 — 1

**Record:** `vnm_2011_f6e2ec`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2011_f6e2ec.json.gz).

1. At the point $(1, 1)$ of the coordinate plane $(Oxy)$, there is a cào cào. From that point the cào cào can only jump to other integral points by the rule: from the positive integral point $A$, the cào cào jumps to the positive integral point $B$ if the triangle $OAB$ has area equal to $\frac{1}{2}$.

1/ Find all points $(m, n)$ to which the cào cào can jump to after a finite number of jumps, starting from the point $(1, 1)$.

2/ Let $(m, n)$ be a positive integral point with property mentioned in 1/. Show that there exists a way, in which the cào cào can jump from point $(1, 1)$ to point $(m, n)$ with not more than $|m - n|$ jumps.



## 2012 — 8

**Record:** `ind_2012_2ce73f`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2012_2ce73f.json.gz).

Let $S$ be a nonempty set of primes satisfying the property that for each proper subset $P$ of $S$, all the prime factors of the number $\left(\prod_{p \in P} p\right) - 1$ are also in $S$. Determine all possible such sets $S$.



## 2012 — 9

**Record:** `ind_2012_f07169`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2012_f07169.json.gz).

Suppose $2n$ real numbers are placed in the cells of a $2 \times n$ grid such that the sum of the numbers in each of the $n$ columns is $1$. Prove that one can erase one of the two numbers in each column such that the sum of the remaining numbers in each of the rows does not exceed $\frac{n+1}{4}$.



## 2012 — 5

**Record:** `usa_2012_3b4732`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2012_3b4732.json.gz).

At a certain orphanage, every pair of orphans are either friends or enemies of each other. For every three of an orphan's friends, an even number of pairs of them are enemies. Prove that it's possible to assign each orphan two parents such that every pair of friends shares exactly one parent, but no pair of enemies does, and no three parents are in a love triangle (where each pair of them has a child).



## 2012 — 3

**Record:** `usa_2012_485e07`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2012_485e07.json.gz).

Prove that there exists a real constant $c$ such that for any pair $(x, y)$ of real numbers, there exist relatively prime integers $m$ and $n$ satisfying the relation
$$\sqrt{(x-m)^2 + (y-n)^2} < c \log(x^2 + y^2 + 2).$$
(This problem was suggested by Daniel Kane.)



## 2012 — 4

**Record:** `usa_2012_5521cf`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2012_5521cf.json.gz).

There are $2010$ students and $100$ classrooms in the Olympiad High School. At the beginning, each of the students is in one of the classrooms. Each minute, as long as not everyone is in the same classroom, somebody walks from one classroom into a different classroom with at least as many students in it (prior to his move). This process will terminate in $M$ minutes. Determine the maximum value of $M$.



## 2012 — 7

**Record:** `usa_2012_5abc60`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2012_5abc60.json.gz).

Determine all positive integers $n$, $n \ge 2$, such that the following statement is true:
If $(a_1, a_2, \ldots, a_n)$ is a sequence of positive integers with $a_1 + a_2 + \cdots + a_n = 2n - 1$, then there is a block of (at least two) consecutive terms in the sequence with their (arithmetic) mean being an integer.



## 2012 — 9.

**Record:** `usa_2012_af9e07`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2012_af9e07.json.gz).

Let $n$ be a positive integer. Suppose we are given $2^n + 1$ distinct sets, each containing finitely many objects. Place each set into one of two categories, the red sets and the blue sets, so that there is at least one set in each category. We define the *symmetric difference* of two sets as the set of objects belonging to exactly one of the two sets. Prove that there are at least $2^n$ different sets which can be obtained as the symmetric difference of a red set and a blue set.
(This problem was suggested by Max Alekseyev.)



## 2012 — 3.

**Record:** `usa_2012_e9f6ee`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2012_e9f6ee.json.gz).

Determine, with proof, whether or not there exist integers $a, b, c > 2010$ satisfying the equation
$$
a^3 + 2b^3 + 4c^3 = 6abc + 1.
$$



## 2012 — Bài 6

**Record:** `vnm_2012_1c51a9`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_1c51a9.json.gz).

Có 42 thí sinh tham gia Kì thi chọn đội tuyển Olympic Toán Quốc tế. Biết rằng mỗi thí sinh quen đúng 20 thí sinh khác. Chứng minh rằng có thể chia các thí sinh hoặc thành 2 nhóm hoặc thành 21 nhóm, sao cho trong mỗi cách chia số người của các nhóm bằng nhau và hai người bất kì trong cùng nhóm thì quen nhau.



## 2012 — Bài 2

**Record:** `vnm_2012_6d51b3`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_6d51b3.json.gz).

Trên một cánh đồng hình chữ nhật kích thước $m \times n$ ô vuông (gồm $m$ hàng và $n$ cột) người ta đặt máy tưới nước vào bên trong một số các ô vuông. Mỗi máy trong một ô vuông không chỉ tưới được ô vuông này và các ô vuông có cạnh chung với nó, mà còn tưới đến được các ô vuông cùng cột với nó và cách nó đúng một ô. Hãy tính số máy ít nhất để có thể tưới được toàn bộ cánh đồng trong hai trường hợp sau:

a) $m = 4,$

b) $m = 3.$



## 2012 — Bài 3

**Record:** `vnm_2012_f548c9`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_f548c9.json.gz).

Cho trước một số nguyên tố $p$ không nhỏ hơn $17$. Chứng minh rằng $t=3$ là số nguyên dương lớn nhất có tính chất: Với mọi bộ số nguyên $a, b, c, d$ sao cho $abc$ không chia hết cho $p$, nhưng $a+b+c$ chia hết cho $p$ thì luôn tồn tại $x, y, z \in \{0, 1, ..., \lfloor \frac{p}{t} \rfloor - 1\}$ để $ax+by+cz+d$ chia hết cho $p$. ($\lfloor \frac{p}{t} \rfloor$ kí hiệu số nguyên lớn nhất không vượt quá $\frac{p}{t}$).



## 2013 — 3

**Record:** `ind_2013_5ef73e`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2013_5ef73e.json.gz).

For a positive integer $n$, a sum-friendly odd partition of $n$ is a sequence $(a_1, a_2, \dots, a_k)$ of odd positive integers with $a_1 \le a_2 \le \dots \le a_k$ and $a_1 + a_2 + \dots + a_k = n$ such that for all positive integers $m \le n$, $m$ can be uniquely written as a subsum $m = a_{i_1} + a_{i_2} + \dots + a_{i_r}$. (Two subsums $a_{i_1} + a_{i_2} + \dots + a_{i_r}$, and $a_{j_1} + a_{j_2} + \dots + a_{j_s}$ with $i_1 < i_2 < \dots < i_r$ and $j_1 < j_2 < \dots < j_s$ are considered the same if $r = s$ and $a_{i_l} = a_{j_l}$ for $1 \le l \le r$.) For example, $(1, 1, 3, 3)$ is a sum-friendly odd partition of $8$. Find the number of sum-friendly odd partitions of $9999$.



## 2013 — 4

**Record:** `ind_2013_abf1b9`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2013_abf1b9.json.gz).

A marker is placed at the origin of an integer lattice. Calvin and Hobbes play the following game. Calvin starts the game and each of them takes turns alternatively. At each turn, one can choose two (not necessarily distinct) integers $a$, $b$, neither of which was chosen earlier by any player and move the marker by $a$ units in the horizontal direction and $b$ units in the vertical direction. Hobbes wins if the marker is back at the origin any time after the first move. Prove that Calvin can prevent Hobbes from winning.



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



## 2013 — 7.

**Record:** `usa_2013_88fa26`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2013_88fa26.json.gz).

In a table with $n$ rows and $2n$ columns where $n$ is a fixed positive integer, we write either zero or one into each cell so that each row has $n$ zeros and $n$ ones. For $1 \le k \le n$ and $1 \le i \le n$, we define $a_{k,i}$ so that the $i$th zero in the $k$th row is the $a_{k,i}^{th}$ column. Let $\mathcal{F}$ be the set of such tables with $a_{1,i} \ge a_{2,i} \ge \dots \ge a_{n,i}$ for every $i$ with $1 \le i \le n$. We associate another $n \times 2n$ table $f(C)$ from $C \in \mathcal{F}$ as follows: for the $k$th row of $f(C)$, we write $n$ ones in the columns $a_{n,k} - k + 1, a_{n-1,k} - k + 2, \dots, a_{1,k} - k + n$ (and we write zeros in the other cells in the row).

a. Show that $f(C) \in \mathcal{F}$.

b. Show that $f(f(f(f(f(C))))) = C$ for any $C \in \mathcal{F}$.



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



## 2014 — 3.

**Record:** `usa_2014_c1a41c`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2014_c1a41c.json.gz).

Let $n$ be an even positive integer, and let $G$ be an $n$-vertex graph with exactly $\frac{n^2}{4}$ edges, where there are no loops or multiple edges (each unordered pair of distinct vertices is joined by either 0 or 1 edge). An unordered pair of distinct vertices $\{x, y\}$ is said to be *amicable* if they have a common neighbor (there is a vertex $z$ such that $xz$ and $yz$ are both edges). Prove that $G$ has at least $2^{\binom{n/2}{2}}$ unordered pairs of vertices which are amicable.



## 2014 — 3.

**Record:** `usa_2014_d4dc03`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2014_d4dc03.json.gz).

Divide the plane into an infinite square grid by drawing all the lines $x = m$ and $y = n$ for integers $m$ and $n$. Next, if a square's upper-right corner has both coordinates even, color it black; otherwise, color it white (in this way, exactly $1/4$ of the squares are black and no two black squares are adjacent). Let $r$ and $s$ be odd integers, and let $(x, y)$ be a point in the interior of any white square such that $rx - sy$ is irrational. Shoot a laser out of this point with slope $r/s$; lasers pass through white squares and reflect off black squares. Prove that the path of this laser will form a closed loop.



## 2014 — 7.

**Record:** `usa_2014_e7d2f3`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2014_e7d2f3.json.gz).

A country has $n$ cities, labeled $1$, $2$, $3$, $\dots$, $n$. It wants to build exactly $n-1$ roads between certain pairs of cities so that every city is reachable from every other city via some sequence of roads. However, it is not permitted to put roads between pairs of cities that have labels differing by exactly $1$, and it is also not permitted to put a road between cities $1$ and $n$. Let $T_n$ be the total number of possible ways to build these roads.

a. For all odd $n$, prove that $T_n$ is divisible by $n$.

b. For all even $n$, prove that $T_n$ is divisible by $n/2$.



## 2015 — 1

**Record:** `vnm_2015_0c8e24`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2015_0c8e24.json.gz).

Let $\alpha$ be a positive root of the equation $x^2 + x = 5$. Suppose that $n$ is a positive integer and $c_0, c_1, \dots, c_n$ are nonnegative integers satisfying the condition
$$
c_0 + c_1\alpha + c_2\alpha^2 + \dots + c_n\alpha^n = 2015.
$$
a) Prove that $c_0 + c_1 + \dots + c_n \equiv 2 \pmod{3}$.
b) Find the minimum of $c_0 + c_1 + \dots + c_n$.



## 2016 — 4

**Record:** `ind_2016_85f4b8`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2016_85f4b8.json.gz).

Let $n$ be a natural number. We define sequences $a_i$ and $b_i$ as follows. We let $a_0 = 1$ and $b_0 = n$. For $i > 0$, we let
$$
(a_i, b_i) = \begin{cases} (2a_{i-1} + 1, b_{i-1} - a_{i-1} - 1) & \text{if } a_{i-1} < b_{i-1}, \\ (a_{i-1} - b_{i-1} - 1, 2b_{i-1} + 1) & \text{if } a_{i-1} > b_{i-1}, \\ (a_{i-1}, b_{i-1}) & \text{if } a_{i-1} = b_{i-1}. \end{cases}
$$
Given that $a_k = b_k$ for some natural number $k$, prove that $n + 3$ is a power of 2.



## 2016 — 5

**Record:** `ind_2016_9a166a`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2016_9a166a.json.gz).

Let $n$ be an odd natural number. We consider an $n$ by $n$ grid which is made up of $n^2$ unit squares and $2n(n+1)$ edges. We colour each of these edges either red or blue. If there are at most $n^2$ red edges, then show that there exists a unit square at least three of whose edges are blue.



## 2016 — 2

**Record:** `ind_2016_c1a286`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2016_c1a286.json.gz).

Let $n$ be a natural number. A sequence $x_1, x_2, \dots, x_{n^2}$ is called *n-*good if each $x_i$ is an element of $\{1, 2, \dots, n\}$ and the ordered pairs $(x_i, x_{i+1})$ are all different for $i = 1, 2, \dots, n^2$ (here we consider the subscripts modulo $n^2$). Two *n-*good sequences $x_1, x_2, \dots, x_{n^2}$ and $y_1, y_2, \dots, y_{n^2}$ are called *similar* if there exists an integer $k$ such that $y_i = x_{i+k}$ for all $i = 1, 2, \dots, n^2$ (again taking the subscripts modulo $n^2$). Suppose that there exists a non-trivial permutation $\sigma$ of $\{1, 2, \dots, n\}$ and an *n-*good sequence $x_1, x_2, \dots, x_{n^2}$ which is similar to $\sigma(x_1), \sigma(x_2), \dots, \sigma(x_{n^2})$. Show that $n \equiv 2 \pmod{4}$.



## 2017 — Problem 1

**Record:** `vnm_2017_71cd4a`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2017_71cd4a.json.gz).

There are $44$ distinct holes on a line and $2017$ ants. Each ant crawled up from a hole, then moved to another hole and crawled down. Denote $T$ as the set of time points that the ants crawled up or crawled down from some hole. Suppose that the speed of the ants are pairwise distinct and they did not change their own speed. Prove that if $|T| \le 45$ then there exist two ants did not meet.

Note that two ants met when there exists a time point such that they were at the same location on the line, including the holes.



## 2017 — Problem 5

**Record:** `vnm_2017_d99be9`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2017_d99be9.json.gz).

Given 2017 positive real numbers $a_1, a_2, \dots, a_{2017}$. For each positive integer $n > 2017$, let
$$
a_n = \max\{a_{i_1} a_{i_2} a_{i_3} \mid i_1 + i_2 + i_3 = n, 1 \le i_1 \le i_2 \le i_3 \le n-1\}.
$$
Prove there exists some positive integers $m \le 2017$ and $N > 4m$ such that $a_n a_{n-4m} = a_{n-2m}^2$ for every $n > N$.



## 2017 — Problem 6

**Record:** `vnm_2017_e0f625`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2017_e0f625.json.gz).

For a positive integer $n$, consider $a_1, a_2, \dots, a_{2n}$ as a permutation of the first $2n$ positive integers. A permutation is called "nice" if $a_i + a_{n+i} = 2n+1$, $i = 1, 2, 3, \dots, n$ and $a_i - a_{i+1}$ is not congruent to $a_j - a_{j+1}$ modulo $2n+1$ for all $1 \le i < j \le 2n$ (suppose that $a_{2n+1} = a_1$).

1. For $n = 6$, give an example of the nice permutation.
2. Prove that for all $n$, there always exist some nice permutation.



## 2018 — TSTST 6

**Record:** `usa_2018_259657`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2018_259657.json.gz).

Let $S = \{1, \dots, 100\}$, and for every positive integer $n$ define
$$
T_n = \{(a_1, \dots, a_n) \in S^n \mid a_1 + \dots + a_n \equiv 0 \pmod{100}\}.
$$
Determine which $n$ have the following property: if we color any 75 elements of $S$ red, then at least half of the $n$-tuples in $T_n$ have an even number of coordinates with red elements.



## 2018 — TSTST 7

**Record:** `usa_2018_5cd6f2`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2018_5cd6f2.json.gz).

Let $n$ be a positive integer. A frog starts on the number line at $0$. Suppose it makes a finite sequence of hops, subject to two conditions:
* The frog visits only points in $\{1, 2, \dots, 2^n - 1\}$, each at most once.
* The length of each hop is in $\{2^0, 2^1, 2^2, \dots\}$. (The hops may be either direction, left or right.)
Let $S$ be the sum of the (positive) lengths of all hops in the sequence. What is the maximum possible value of $S$?



## 2018 — TSTST 9

**Record:** `usa_2018_7ab8a8`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2018_7ab8a8.json.gz).

Show that there is an absolute constant $c < 1$ with the following property: whenever $\mathcal{P}$ is a polygon with area 1 in the plane, one can translate it by a distance of $\frac{1}{100}$ in some direction to obtain a polygon $\mathcal{Q}$, for which the intersection of the interiors of $\mathcal{P}$ and $\mathcal{Q}$ has total area at most $c$.



## 2018 — TSTST 2

**Record:** `usa_2018_9f41d2`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2018_9f41d2.json.gz).

In the nation of Onewaynia, certain pairs of cities are connected by one-way roads. Every road connects exactly two cities (roads are allowed to cross each other, e.g., via bridges), and each pair of cities has at most one road between them. Moreover, every city has exactly two roads leaving it and exactly two roads entering it.
We wish to close half the roads of Onewaynia in such a way that every city has exactly one road leaving it and exactly one road entering it. Show that the number of ways to do so is a power of 2 greater than 1 (i.e. of the form $2^n$ for some integer $n \ge 1$).



## 2018 — Problem 5

**Record:** `vnm_2018_027413`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2018_027413.json.gz).

Consider a rectangle board $ABCD$ of size $m \times n$ with $(m + 1) \times (n + 1)$ intersections. Some engineers want to build a route from $A$ which goes along the segments parallel to the sides of the board, passes through each intersection exactly once and finally turns back to $A$.

a. Prove that they can build the route if and only if either $m$ is odd or $n$ is odd.

b. With $m, n$ satisfying the condition in (a), find the least number of intersections at each there is a turn.



## 2018 — Problem 2

**Record:** `vnm_2018_e63671`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2018_e63671.json.gz).

Consider a positive integer $m$ and a rectangle board of size $m \times 2018$ which consists of $m$ rows and $2018$ columns. We write $0$ or $1$ into some cells of the board (only one number in a cell) and the rest are left empty. The board is *complete* if for an arbitrary binary sequence $S$ of length $2018$, we can always choose a row of the board to write some more $0$s, $1$s so that $2018$ numbers on that row (without any change in order) form the sequence $S$ (in case the board already had a row which is $S$, it is also complete). The board is *minimal* if it is complete and if we omit any row in the board, it is no longer complete.

a. If $0 \le k \le 2018$, prove that there exists a minimal $2^k \times 2018$ board such that there are exactly $k$ columns, each of which consists of both $0$ and $1$ (there are possibly some empty cells on those columns).

b. A minimal $m \times 2018$ board which has exactly $k$ columns, each of which consists of both $0$ and $1$, is given. Prove that $m \le 2^k$.



## 2019 — TST 5

**Record:** `usa_2019_213e85`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2019_213e85.json.gz).

Let $n$ be a positive integer. Tasty and Stacy are given a circular necklace with $3n$ sapphire beads and $3n$ turquoise beads, such that no three consecutive beads have the same color. They play a cooperative game where they alternate turns removing three consecutive beads, subject to the following conditions:
* Tasty must remove three consecutive beads which are turquoise, sapphire, and turquoise, in that order, on each of his turns.
* Stacy must remove three consecutive beads which are sapphire, turquoise, and sapphire, in that order, on each of her turns.
They win if all the beads are removed in $2n$ turns. Prove that if they can win with Tasty going first, they can also win with Stacy going first.



## 2019 — TST 4

**Record:** `usa_2019_272f92`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2019_272f92.json.gz).

We say a function $f: \mathbb{Z}_{\ge 0} \times \mathbb{Z}_{\ge 0} \to \mathbb{Z}$ is *great* if for any nonnegative integers $m$ and $n$,
$$
f(m+1, n+1)f(m, n) - f(m+1, n)f(m, n+1) = 1.
$$
If $A = (a_0, a_1, \dots)$ and $B = (b_0, b_1, \dots)$ are two sequences of integers, we write $A \sim B$ if there exists a great function $f$ satisfying $f(n, 0) = a_n$ and $f(0, n) = b_n$ for every nonnegative integer $n$ (in particular, $a_0 = b_0$).
Prove that if $A, B, C$, and $D$ are four sequences of integers satisfying $A \sim B, B \sim C$, and $C \sim D$, then $D \sim A$.



## 2019 — TSTST 3

**Record:** `usa_2019_2f0721`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2019_2f0721.json.gz).

On an infinite square grid we place finitely many cars, which each occupy a single cell and face in one of the four cardinal directions. Cars may never occupy the same cell. It is given that the cell immediately in front of each car is empty, and moreover no two cars face towards each other (no right-facing car is to the left of a left-facing car within a row, etc.). In a *move*, one chooses a car and shifts it one cell forward to a vacant cell. Prove that there exists an infinite sequence of valid moves using each car infinitely many times.



## 2019 — TST 3

**Record:** `usa_2019_5cb5ea`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2019_5cb5ea.json.gz).

A *snake of length* $k$ is an animal which occupies an ordered $k$-tuple $(s_1, \dots, s_k)$ of cells in an $n \times n$ grid of square unit cells. These cells must be pairwise distinct, and $s_i$ and $s_{i+1}$ must share a side for $i = 1, \dots, k-1$. If the snake is currently occupying $(s_1, \dots, s_k)$ and $s$ is an unoccupied cell sharing a side with $s_1$, the snake can *move* to occupy $(s, s_1, \dots, s_{k-1})$ instead. The snake has *turned around* if it occupied $(s_1, s_2, \dots, s_k)$ at the beginning, but after a finite number of moves occupies $(s_k, s_{k-1}, \dots, s_1)$ instead.
Determine whether there exists an integer $n > 1$ such that one can place some snake of length at least $0.9n^2$ in an $n \times n$ grid which can turn around.



## 2019 — TSTST 4

**Record:** `usa_2019_afbc19`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2019_afbc19.json.gz).

Consider coins with positive real denominations not exceeding $1$. Find the smallest $C > 0$ such that the following holds: if we are given any $100$ such coins with total value $50$, then we can always split them into two stacks of $50$ coins each such that the absolute difference between the total values of the two stacks is at most $C$.



## 2019 — TSTST 6

**Record:** `usa_2019_c48ff2`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2019_c48ff2.json.gz).

Suppose $P$ is a polynomial with integer coefficients such that for every positive integer $n$, the sum of the decimal digits of $|P(n)|$ is not a Fibonacci number. Must $P$ be constant?
(A *Fibonacci number* is an element of the sequence $F_0, F_1, \dots$ defined recursively by $F_0 = 0$, $F_1 = 1$, and $F_{k+2} = F_{k+1} + F_k$ for $k \ge 0$.)



## 2019 — TSTST 8

**Record:** `usa_2019_d4cda2`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2019_d4cda2.json.gz).

Let $S$ be a set of 16 points in the plane, no three collinear. Let $\chi(S)$ denote the number of ways to draw 8 line segments with endpoints in $S$, such that no two drawn segments intersect, even at endpoints. Find the smallest possible value of $\chi(S)$ across all such $S$.



## 2020 — TST 4

**Record:** `usa_2020_4ac916`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2020_4ac916.json.gz).

For a finite simple graph $G$, we define $G'$ to be the graph on the same vertex set as $G$, where for any two vertices $u \neq v$, the pair $\{u, v\}$ is an edge of $G'$ if and only if $u$ and $v$ have a common neighbor in $G$. Prove that if $G$ is a finite simple graph which is isomorphic to $(G')'$, then $G$ is also isomorphic to $G'$.

We say a vertex of a graph is *fatal* if it has degree at least 3, and some two of its neighbors are not adjacent.



## 2020 — TST 1

**Record:** `usa_2020_5d31dd`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2020_5d31dd.json.gz).

Choose positive integers $b_1, b_2, \dots$ satisfying
$$
1 = \frac{b_1}{1^2} > \frac{b_2}{2^2} > \frac{b_3}{3^2} > \frac{b_4}{4^2} > \dots
$$
and let $r$ denote the largest real number satisfying $\frac{b_n}{n^2} \ge r$ for all positive integers $n$. What are the possible values of $r$ across all possible choices of the sequence $(b_n)$?



## 2020 — TST 3

**Record:** `usa_2020_8ea9dc`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2020_8ea9dc.json.gz).

Let $\alpha \ge 1$ be a real number. Hephaestus and Poseidon play a turn-based game on an infinite grid of unit squares. Before the game starts, Poseidon chooses a finite number of cells to be *flooded*. Hephaestus is building a *levee*, which is a subset of unit edges of the grid (called *walls*) forming a connected, non-self-intersecting path or loop.
The game then begins with Hephaestus moving first. On each of Hephaestus's turns, he adds one or more walls to the levee, as long as the total length of the levee is at most $\alpha n$ after his nth turn. On each of Poseidon's turns, every cell which is adjacent to an already flooded cell and with no wall between them becomes flooded as well.
Hephaestus wins if the levee forms a closed loop such that all flooded cells are contained in the interior of the loop — hence stopping the flood and saving the world. For which $\alpha$ can Hephaestus guarantee victory in a finite number of turns no matter how Poseidon chooses the initial cells to flood?



## 2020 — TSTST 5

**Record:** `usa_2020_93693e`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2020_93693e.json.gz).

Let $\mathbb{N}^2$ denote the set of ordered pairs of positive integers. A finite subset $S$ of $\mathbb{N}^2$ is *stable* if whenever $(x, y)$ is in $S$, then so are all points $(x', y')$ of $\mathbb{N}^2$ with both $x' \le x$ and $y' \le y$.
Prove that if $S$ is a stable set, then among all stable subsets of $S$ (including the empty set and $S$ itself), at least half of them have an even number of elements.



## 2020 — TSTST 1

**Record:** `usa_2020_b23173`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2020_b23173.json.gz).

Let $a, b, c$ be fixed positive integers. There are $a+b+c$ ducks sitting in a circle, one behind the other. Each duck picks either *rock*, *paper*, or *scissors*, with $a$ ducks picking rock, $b$ ducks picking paper, and $c$ ducks picking scissors.
A *move* consists of an operation of one of the following three forms:
* If a duck picking rock sits behind a duck picking scissors, they switch places.
* If a duck picking paper sits behind a duck picking rock, they switch places.
* If a duck picking scissors sits behind a duck picking paper, they switch places.
Determine, in terms of $a, b$, and $c$, the maximum number of moves which could take place, over all possible initial configurations.



## 2020 — TSTST 9

**Record:** `usa_2020_fe77d1`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2020_fe77d1.json.gz).

Ten million fireflies are glowing in $\mathbb{R}^3$ at midnight. Some of the fireflies are friends, and friendship is always mutual. Every second, one firefly moves to a new position so that its distance from each one of its friends is the same as it was before moving. This is the only way that the fireflies ever change their positions. No two fireflies may ever occupy the same point.

Initially, no two fireflies, friends or not, are more than a meter away. Following some finite number of seconds, all fireflies find themselves at least ten million meters away from their original positions. Given this information, find the greatest possible number of friendships between the fireflies.

In general, we show that when $n \ge 70$, the answer is $f(n) = \lfloor \frac{n^2}{3} \rfloor$.



## 2021 — 2

**Record:** `vnm_2021_ae2abb`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2021_ae2abb.json.gz).

In a board of $2021 \times 2021$ grids, we pick $k$ unit squares such that every picked square shares at least one vertex with at most one other picked square. Determine the maximum of $k$.



## 2021 — Problem 6.

**Record:** `vnm_2021_ecd237`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2021_ecd237.json.gz).

Let $n \ge 3$ be a positive integer and $p$ be a prime number such that $p > 6^{n-1} - 2^n + 1$. Let $S$ be the set of $n$ positive integers with different residues modulo $p$. Show that there exists a positive integer $c$ such that there are exactly two ordered triples $(x, y, z) \in S^3$ with distinct elements, such that $x - y + z - c$ is divisible by $p$.



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



## 2022 — 3

**Record:** `chn_2022_64f1b5`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_64f1b5.json.gz).

Let $a, b, c, p, q, r$ be positive integers with $p, q, r \ge 2$. Denote
$$
Q = \{(x, y, z) \in \mathbb{Z}^3 \mid 0 \le x \le a, 0 \le y \le b, 0 \le z \le c\}.
$$
Initially, some stones are put at each point of $Q$, with total $M$ stones. Then one can perform the following three types of operations repeatedly:
(1) remove $p$ stones on $(x, y, z)$ and place a stone on $(x-1, y, z)$;
(2) remove $q$ stones on $(x, y, z)$ and place a stone on $(x, y-1, z)$;
(3) remove $r$ stones on $(x, y, z)$ and place a stone on $(x, y, z-1)$.
Find the smallest positive integer $M$ such that one can always perform a sequence of operations, to place a stone at $(0, 0, 0)$, no matter how the stones were distributed initially.



## 2022 — 5

**Record:** `chn_2022_78f104`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_78f104.json.gz).

Prove that there exist two positive real numbers $C$ and $\alpha > \frac{1}{2}$, such that, for any positive integer $n$, there is a subset $A$ of $\{1, 2, \dots, n\}$ with $|A| \ge Cn^\alpha$, such that the difference between any pair of different numbers in $A$ is not a perfect square.



## 2022 — 4

**Record:** `chn_2022_9e340b`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2022_9e340b.json.gz).

Find all positive integers $k$ such that there are finitely many triangles on the Descartes coordinate plane such that
(1) the center of mass of each triangle is an integral point;
(2) the intersection of any two triangles is either the empty set, a common vertex, or an edge joining two common vertices; and
(3) the union of these triangles is a square with side length $k$. (The vertices of the squares are not required to be integral points, and the edges are not required to be parallel to the coordinate axes.)



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



## 2022 — 2

**Record:** `vnm_2022_b14250`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2022_b14250.json.gz).

Given a convex polyhedron with 2022 faces. In 3 arbitrary faces, there are already numbers 26, 4 and 2022 (each face contains one number). One wants to fill in each other face a real number which is the arithmetic mean of every number in faces that share a common edge with that face. Prove that there is exactly one way to fill all the numbers in that polyhedron.



## 2022 — Problem 6

**Record:** `vnm_2022_b8b08c`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2022_b8b08c.json.gz).

Given a set $A = \{1, 2, \dots, 4044\}$. One colors 2022 numbers of them by white and the rest by black. For each $i \in A$, denote the weight of $i$ by sum of the amount of white numbers that are smaller than $i$ and the amount of black numbers that are larger than $i$. For every positive integer $m$, find all positive integers $k$ such that there exists a way to color the numbers which can get exactly $k$ numbers having weight $m$.



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



## 2023 — 2

**Record:** `chn_2023_a2bd30`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_a2bd30.json.gz).

A party is attended by $n$ people. Assume that there are at most $n$ pairs of friendships among them, and any two people shake hands at the party if and only if they have a common friend at the party.
Suppose $m$ is a positive integer satisfying $m \ge 3$ and $n \le m^3$. Prove that there exists a person $A$ such that the number of people $A$ has shaken hands with at this party does not exceed $(m-1)$ times the number of $A$'s friends.



## 2023 — 5

**Record:** `chn_2023_b8f301`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_b8f301.json.gz).

Suppose $P_1, \dots, P_n$ are $n$ points inside triangle $ABC$, such that any three points among $P_1, \dots, P_n, A, B, C$ are not collinear. Prove: It is possible to divide $\triangle ABC$ into a union of $2n+1$ smaller triangles such that each smaller triangle has its vertices among $P_1, \dots, P_n, A, B, C$, and the number of smaller triangles with vertices including at least one point among $A, B, C$ is no less than $n + \sqrt{n} + 1$.



## 2023 — 4

**Record:** `chn_2023_d02731`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_d02731.json.gz).

A nonempty set $A$ of integers is called a “beautiful set” if for any $a \in A$ and $k \in \{1, 2, \dots, 2023\}$, the set
$$
\{b \in A \mid \lfloor \frac{b}{3^k} \rfloor = \lfloor \frac{a}{3^k} \rfloor \}
$$
has exactly $2^k$ elements.
Prove that: if the intersection of an integer set $S$ and any beautiful set is not empty, then $S$ contains a beautiful set.

*Note:* Here $\lfloor x \rfloor$ represents the greatest integer not exceeding $x$.



## 2023 — 3

**Record:** `chn_2023_e54b7e`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2023_e54b7e.json.gz).

Find the largest positive integer $m$ such that there is a way to color some of the cells red in a $70 \times 70$ grid, satisfying the following two conditions:
(1) There do not exist two red cells such that the number of red cells in the row they belong to and the number of red cells in the column they belong to are the same;
(2) There are at least 2 rows each containing exactly $m$ red cells.



## 2023 — 1

**Record:** `ind_2023_001b9f`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2023_001b9f.json.gz).

In the fictional country of Mahishmati, there are $50$ cities, including a capital city. Some pairs of cities are connected by two-way flights. Given a city $A$, an ordered list of cities $C_1, \dots, C_{50}$ is called an *antitour* from $A$ if
* every city (including $A$) appears in the list exactly once, and
* for each $k \in \{1, 2, \dots, 50\}$, it is impossible to go from $A$ to $C_k$ by a sequence of exactly $k$ (not necessarily distinct) flights.

Baahubali notices that there is an antitour from $A$ for any city $A$. Further, he can take a sequence of flights, starting from the capital and passing through each city exactly once. Find the least possible total number of antitours from the capital city.



## 2023 — Problem 1

**Record:** `ind_2023_6854af`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2023_6854af.json.gz).

Find all $f: \mathbb{N} \to \mathbb{N}$ such that $f(x) + y$ and $f(y) + x$ have the same number of 1's in their binary representation for any $x, y \in \mathbb{N}$.



## 2023 — Problem 3

**Record:** `ind_2023_78c50a`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2023_78c50a.json.gz).

Prove that for all integers $k > 2$, there exists $k$ distinct positive integers $a_1, \dots, a_k$ such that
$$
\sum_{1 \le i < j \le k} \frac{1}{a_i a_j} = 1.
$$



## 2023 — Problem 2

**Record:** `ind_2023_b690b1`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2023_b690b1.json.gz).

In a school, every pair of students are either friends or strangers. A sequence of (not necessarily distinct) students $A_1, A_2, \dots, A_{2023}$ is called *mischievous* if

* Total number of friends of $A_1$ is odd.
* $A_i$ and $A_{i+1}$ are friends for $i = 1, 2, \dots, 2022$.
* Total number of friends of $A_{2023}$ is even.

Prove that the total number of *mischievous* sequences is even.



## 2023 — 3

**Record:** `usa_2023_103f73`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2023_103f73.json.gz).

Find all positive integers $n$ for which it is possible to color some cells of an infinite grid of unit squares red, such that each rectangle consisting of exactly $n$ cells (and whose edges lie along the lines of the grid) contains an odd number of red cells.



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



## 2023 — USA TST 2023/1

**Record:** `usa_2023_942b5a`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2023_942b5a.json.gz).

There are 2022 equally spaced points on a circular track $\gamma$ of circumference 2022. The points are labeled $A_1, A_2, \dots, A_{2022}$ in some order, each label used once. Initially, Bunbun the Bunny begins at $A_1$. She hops along $\gamma$ from $A_1$ to $A_2$, then from $A_2$ to $A_3$, until she reaches $A_{2022}$, after which she hops back to $A_1$. When hopping from $P$ to $Q$, she always hops along the shorter of the two arcs $\widehat{PQ}$ of $\gamma$; if $\widehat{PQ}$ is a diameter of $\gamma$, she moves along either semicircle.
Determine the maximal possible sum of the lengths of the 2022 arcs which Bunbun traveled, over all possible labellings of the 2022 points.



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



## 2023 — 4

**Record:** `usa_2023_d384cb`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2023_d384cb.json.gz).

Let $n \ge 3$ be an integer and let $K_n$ be the complete graph on $n$ vertices. Each edge of $K_n$ is colored either red, green, or blue. Let $A$ denote the number of triangles in $K_n$ with all edges of the same color, and let $B$ denote the number of triangles in $K_n$ with all edges of different colors. Prove that
$$
B \le 2A + \frac{n(n-1)}{3}.
$$



## 2023 — USA TST 2023/6

**Record:** `usa_2023_de1495`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2023_de1495.json.gz).

Fix a function $f: \mathbb{N} \to \mathbb{N}$ and for any $m, n \in \mathbb{N}$ define
$$
\Delta(m, n) = \underbrace{f(f(\dots f(m)\dots))}_{f(n) \text{ times}} - \underbrace{f(f(\dots f(n)\dots))}_{f(m) \text{ times}}.
$$
Suppose $\Delta(m, n) \neq 0$ for any distinct $m, n \in \mathbb{N}$. Show that $\Delta$ is unbounded, meaning that for any constant $C$ there exist $m, n \in \mathbb{N}$ with $|\Delta(m, n)| > C$.



## 2023 — 7

**Record:** `usa_2023_e8656c`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2023_e8656c.json.gz).

The Bank of Pittsburgh issues coins that have a heads side and a tails side. Vera has a row of $2023$ such coins alternately tails-up and heads-up, with the leftmost coin tails-up.

In a *move*, Vera may flip over one of the coins in the row, subject to the following rules:

* On the first move, Vera may flip over any of the $2023$ coins.
* On all subsequent moves, Vera may only flip over a coin adjacent to the coin she flipped on the previous move. (We do not consider a coin to be adjacent to itself.)

Determine the smallest possible number of moves Vera can make to reach a state in which every coin is heads-up.



## 2023 — 1

**Record:** `vnm_2023_3ebb4e`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2023_3ebb4e.json.gz).

A school has two classes $A$ and $B$ which have $m$ and $n$ students each. The students of the two classes sit in a circle. Each student is then given a number of candies equal to the number of consecutive students sitting to the left of him that are from his same class. After distributing the candies, the teacher decides to group the students such that in each group, all the students receive the same amount of candies, and any two students from two different groups should receive a different amount of candies.
a) What is the maximum number of students that a group can have?
b) Excluding the group where every student receives no candies, what is the maximum number of students that a group can have?



## 2023 — 6

**Record:** `vnm_2023_7638b1`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2023_7638b1.json.gz).

Let $n \ge 3$ be an integer and $S$ be a set of $n$ elements. Determine the largest integer $k_n$ such that: for each selection of $k_n$ 3-subsets of $S$, there exists a way to color elements of $S$ with two colors such that none of the chosen 3-subset is monochromatic.



## 2024 — 1

**Record:** `chn_2024_2a0411`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2024_2a0411.json.gz).

Let $\mathbb{N} = \{0,1,2,\dots\}$ be the set of all non-negative integers. For each $n \in \mathbb{N}$, define the Catalan number
$$
C_n = \frac{1}{n+1} \binom{2n}{n} = \frac{(2n)!}{n!(n+1)!}.
$$
Prove that for any positive integer $m$, we have
$$
\sum_{\substack{i,j,k \in \mathbb{N} \\ i+j+k=m}} C_{i+j}C_{i+k}C_{j+k} = \frac{3}{2m+3}C_{2m+1}.
$$



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



## 2024 — 4

**Record:** `chn_2024_7ed496`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2024_7ed496.json.gz).

Let $m > 1$ be an integer. It is known that there exists a prime number in the interval $[2m - \sqrt{m} + 1, 2m]$. Prove that among any $m$ pairwise distinct positive integers $a_1, a_2, \dots, a_m$, there exist two numbers $a_i$ and $a_j$ ($1 \le i, j \le m$) such that
$$
\frac{a_i}{(a_i, a_j)} \ge m,
$$
where $(a_i, a_j)$ denotes the greatest common divisor of the positive integers $a_i$ and $a_j$.



## 2024 — 2

**Record:** `chn_2024_cc0bb9`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2024_cc0bb9.json.gz).

For a positive integer $n$, a subset $S$ of $\{1,2,\dots,n\}$ is called an $n$-good set if for any elements $x,y$ in $S$ (they can be the same), if $x+y \le n$, then $x+y \in S$.
For a positive integer $n$, define $r_n$ as the smallest real number such that for any positive integer $m \le n$, there exists an $n$-good set with $m$ elements, whose sum of all elements does not exceed $m \cdot r_n$.
Prove that there exists a real number $\alpha$ such that for any positive integer $n$, we have $|r_n - \alpha n| < 2024$.



## 2024 — 2.

**Record:** `ind_2024_0dddaf`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2024_0dddaf.json.gz).

* $a^{2n} - a$ is divisible by $n$,
* $\sum_{k=1}^{n} k^{2024} a^{2k}$ is not divisible by $n$.
Prove that $n$ has a prime factor *smaller* than $2024$.



## 2024 — 1

**Record:** `ind_2024_804c67`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2024_804c67.json.gz).

A sleeping rabbit lies in the interior of a convex $2024$-gon. A hunter picks three vertices of the polygon and he lays a trap which covers the interior and the boundary of the triangular region determined by them. Determine the minimum number of times he needs to do this to guarantee that the rabbit will be trapped.



## 2024 — 2.

**Record:** `ind_2024_af0b04`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2024_af0b04.json.gz).

Let $x_1, x_2, \dots, x_{2024}$ be non-negative real numbers such that $x_1 \le x_2 \le \dots \le x_{2024}$, and $x_1^3 + x_2^3 + \dots + x_{2024}^3 = 2024$. Prove that
$$
\sum_{1 \le i < j \le 2024} (-1)^{i+j} x_i^2 x_j \ge -1012.
$$



## 2024 — 3

**Record:** `ind_2024_be9bfd`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2024_be9bfd.json.gz).

Let $P(x) \in \mathbb{Q}[x]$ be a polynomial with rational coefficients and degree $d \ge 2$. Prove there is no infinite sequence $a_0, a_1, \dots$ of rational numbers such that $P(a_i) = a_{i-1} + i$ for all $i \ge 1$.



## 2024 — 2.

**Record:** `ind_2024_d0a341`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2024_d0a341.json.gz).

There are $n \ge 3$ particles on a circle situated at the vertices of a regular $n$-gon. All these particles move on the circle with the same constant speed. One of the particles moves in the clockwise direction while all others move in the anti-clockwise direction. When particles collide, that is, they are all at the same point, they all reverse the direction of their motion and continue with the same speed as before.
Let $s$ be the smallest number of collisions after which all particles return to their original positions. Find $s$.



## 2024 — 3.

**Record:** `ind_2024_d6cfca`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2024_d6cfca.json.gz).

At an IMOTC party, all people have pairwise distinct ages. Some pairs of people are friends and friendship is mutual. Call a person *junior* if they are younger than all their friends, and *senior* if they are older than all their friends. A person with no friends is both *junior* and *senior*. A sequence of pairwise distinct people $A_1, \dots, A_m$ is called *photogenic* if:
* $A_1$ is junior,
* $A_m$ is senior, and
* $A_i$ and $A_{i+1}$ are friends, and $A_{i+1}$ is older than $A_i$ for all $1 \le i \le m-1$.
Let $k$ be a positive integer such that for every *photogenic* sequence $A_1, \dots, A_m$, $m$ is not divisible by $k$. Prove that the people at the party can be partitioned into $k$ groups so that no two people in the same group are friends.



## 2024 — 2

**Record:** `vnm_2024_befa2a`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2024_befa2a.json.gz).

In a garden, which is organized as a $2024 \times 2024$ board, we plant three types of flowers: roses, daisies, and orchids. We want to plant flowers such that the following conditions are satisfied:

(i) Each cell is planted with at most one type of flower. Some cells can be left blank and not planted.

(ii) For each planted cell $A$, there exist exactly $3$ other planted cells in the same column or row such that those $3$ cells are planted with flowers of different types from $A$'s.

(iii) Each flower is planted in at least $1$ cell.

What is the maximal number of the cells that can be planted with flowers?



## 2025 — Problem 1.

**Record:** `chn_2025_2bb7dd`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_2bb7dd.json.gz).

Find all positive integers $m$ such that there exists an infinite set $A$ of positive integers satisfying: for any $m$ distinct elements $a_1, a_2, \dots, a_m$ in $A$, both $a_1+a_2+\dots+a_m$ and $a_1a_2\cdots a_m$ are square-free.

*Note: A positive integer $n$ is called square-free if it is not divisible by the square of any prime number.*



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



## 2025 — Problem 11.

**Record:** `chn_2025_54b9d7`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_54b9d7.json.gz).

Let $n \ge 2$ be an integer. Two players, Alice and Bob, play the following game: Initially all $\binom{n}{2}$ edges of the complete graph $K_n$ are uncolored. They take turns coloring edges red, with Alice starting first. In each move, a player selects one or two uncolored edges to color red, with the constraint that after each move, no three vertices can have all three edges between them colored red. The game ends when no more edges can be colored.
Prove that there exists a real number $\varepsilon > 0$ such that for any integer $n \ge 2$, no matter how Bob plays, Alice can ensure that at the end of the game, the number of red edges does not exceed $\left(\frac{1}{4} - \varepsilon\right)n^2 + n$.



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



## 2025 — Problem 5.

**Record:** `chn_2025_f1f576`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/china/chn_2025_f1f576.json.gz).

Prove that there exist integers $x_1, x_2, \dots, x_{10}, y_1, y_2, \dots, y_{10}$ satisfying:
(1) For $i = 1, 2, \dots, 10$, $|x_i| \le 10^{10}$ and $|y_i| \le 10^{10}$;
(2) The point set in the plane
$$
X = \left\{ \left( \sum_{i=1}^{10} a_i x_i, \sum_{i=1}^{10} a_i y_i \right) \middle| a_1, a_2, \dots, a_{10} \in \{0, 1\} \right\}
$$
contains exactly 1024 distinct points;
(3) For any two parallel lines in the plane at distance 1, the strip region between them (including the lines) contains at most two points from $X$.



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



## 2025 — TSTST 1

**Record:** `usa_2025_061227`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_061227.json.gz).

In a group of people, some are friends (friendship is mutual) and each person $p$ has a list $f_1(p), f_2(p), \dots, f_{d(p)}(p)$ of their friends, where $d(p)$ is the number of friends $p$ has. Additionally, any two people are connected by a series of friendships. Each person also has a *water balloon*. The following game is played until someone ends up with more than one water balloon: on round $r$, each person $p$ throws the current water balloon they have to their friend $f_s(p)$ such that $d(p) \mid r - s$. Show that if the game never ends, then everyone has the same number of friends.



## 2025 — Problem 6

**Record:** `usa_2025_3e982f`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_3e982f.json.gz).

Two players, Alice and Bob, play a game on $n$ vertices labelled $1, 2, \dots, n$. Alice and Bob take turns adding edges $\{i, j\}$, with Alice going first. Both players are banned from creating a cycle, and the game ends after $n-1$ total turns.
Let the weight of the edge $\{i, j\}$ be $|i - j|$, and let $W$ be the total weight of all edges at the end of the game. If Alice plays to maximize $W$ and Bob plays to minimize $W$, what will $W$ be?



## 2025 — Problem 1

**Record:** `usa_2025_5085de`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_5085de.json.gz).

In a group of people, some are friends (friendship is mutual) and each person $p$ has a list $f_1(p), f_2(p), \dots, f_{d(p)}(p)$ of their friends, where $d(p)$ is the number of friends $p$ has. Additionally, any two people are connected by a series of friendships. Each person also has a *water balloon*. The following game is played until someone ends up with more than one water balloon: on round $r$, each person $p$ throws the current water balloon they have to their friend $f_s(p)$ such that $d(p) \mid r - s$. Show that if the game never ends, then everyone has the same number of friends.



## 2025 — 1

**Record:** `usa_2025_c87ac0`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_c87ac0.json.gz).

Let $n$ be a positive integer. Ana and Banana play a game. Banana thinks of a function $f: \mathbb{Z} \to \mathbb{Z}$ and a prime number $p$. He tells Ana that $f$ is nonconstant, $p < 100$, and $f(x+p) = f(x)$ for all integers $x$. Ana's goal is to determine the value of $p$. She writes down $n$ integers $x_1, \dots, x_n$. After seeing this list, Banana writes down $f(x_1), \dots, f(x_n)$ in order. Ana wins if she can determine the value of $p$ from this information. Find the smallest value of $n$ for which Ana has a winning strategy.



## 2025 — TST 1

**Record:** `usa_2025_d1cd24`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_d1cd24.json.gz).

Let $n$ be a positive integer. Ana and Banana play a game. Banana thinks of a function $f: \mathbb{Z} \to \mathbb{Z}$ and a prime number $p$. He tells Ana that $f$ is nonconstant, $p < 100$, and $f(x+p) = f(x)$ for all integers $x$. Ana's goal is to determine the value of $p$. She writes down $n$ integers $x_1, \dots, x_n$. After seeing this list, Banana writes down $f(x_1), \dots, f(x_n)$ in order. Ana wins if she can determine the value of $p$ from this information. Find the smallest value of $n$ for which Ana has a winning strategy.



## 2025 — 5

**Record:** `usa_2025_e105bb`. **Category:** selection. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_e105bb.json.gz).

A pond has $2025$ lily pads arranged in a circle. Two frogs, Alice and Bob, begin on different lily pads. A frog jump is a jump which travels $2$, $3$, or $5$ positions clockwise. Alice and Bob each make a series of frog jumps, and each frog ends on the same lily pad that it started from. Given that each lily pad is the destination of exactly one jump, prove that each frog completes exactly two laps around the pond (i.e. travels $4050$ positions in total).



# IMOTC


## 2023 — Problem 3

**Record:** `ind_2023_092f9b`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2023_092f9b.json.gz).

Prove that for all integers $k > 2$, there exists $k$ distinct positive integers $a_1, \dots, a_k$ such that
$$
\sum_{1 \le i < j \le k} \frac{1}{a_i a_j} = 1.
$$



## 2023 — Problem 1

**Record:** `ind_2023_407ed2`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2023_407ed2.json.gz).

The numbers $1$, $2$, $3$, $4$, $\ldots$, $39$ are written on a blackboard. In one step we are allowed to choose two numbers $a$ and $b$ on the blackboard such that $a$ divides $b$, and replace $a$ and $b$ by the single number $\frac{b}{a}$. This process is continued till no number on the board divides any other number. Let $S$ be the set of numbers which is left on the board at the end. What is the smallest possible value of $|S|$?



## 2023 — Problem 3

**Record:** `ind_2023_d9a3be`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/india/ind_2023_d9a3be.json.gz).

Let $n$ be any positive integer, and let $S(n)$ denote the number of permutations $\tau$ of $\{1, \dots, n\}$ such that $k^4 + (\tau(k))^4$ is prime for all $k = 1, \dots, n$. Show that $S(n)$ is always a square.



# IranMO


## 2015 — 4

**Record:** `irn_2015_4e48b5`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/iran/irn_2015_4e48b5.json.gz).

Let $n$ be a natural number. Determine the smallest natural number $k$ such that among any $k$ natural numbers, it is always possible to select an even number of them having a sum divisible by $n$.



## 2015 — 9

**Record:** `irn_2015_5e81d0`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/iran/irn_2015_5e81d0.json.gz).

Find the maximum number of rectangles with sides equal to $1$ and $2$ and parallel to the coordinate axes such that each two have an area equal to $1$ in common.



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



## 2015 — 1

**Record:** `irn_2015_acb8a8`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/iran/irn_2015_acb8a8.json.gz).

A local supermarket is responsible for the distribution of $100$ supply boxes. Each box is ought to contain $10$ kilograms of rice and $30$ eggs. It is known that a total of $1000$ kilograms of rice and $3000$ eggs are in these boxes, but in some of them the amount of either item is more or less than the amount required. In each step, supermarket workers can choose two arbitrary boxes and transfer any amount of rice or any number of eggs between them. At least how many steps are required so that, starting from any arbitrary initial condition, after these steps the amount of rice and the number of eggs in all these boxes is equal?



## 2015 — 11

**Record:** `irn_2015_c7ea96`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/iran/irn_2015_c7ea96.json.gz).

Permutation $(a_1, a_2, \dots, a_n)$ of the set $\{1, 2, \dots, n\}$ is called **messy** if for any three indices $1 \le i < j < k \le n$, $a_i + a_k - 2a_j$ is not divisible by $n$. Find all natural numbers $n \ge 3$ for which there exists a messy permutation of the set $\{1, 2, \dots, n\}$.



## 2015 — 5

**Record:** `irn_2015_f89b52`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/iran/irn_2015_f89b52.json.gz).

Consider an $n \times n$ array of points. For a subset $A$ of the edges of this array (i.e. the lattice edges), we denote by $V(A)$ the set of vertices of $A$ and by $J(A)$ the set of connected components of $A$. For each natural number $l$, prove that
$$
\frac{l}{2} \le \min_{|A| \ge l} (|V(A)| - |J(A)|) \le \frac{l}{2} + \sqrt{\frac{l}{2}} + 1.
$$
(For a set $X$, by $|X|$ we mean the number of elements of $X$).



# JMO


## 2006 — 6

**Record:** `jpn_2006_1f6f07`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2006_1f6f07.json.gz).

A $3 \times 3$ grid is given. We color each square by red or blue so that no red $2 \times 2$ square nor blue $2 \times 2$ square appears. How many such colorings are there?
We consider two colorings different even if they correspond by rotation and/or reversal.



## 2006 — 12

**Record:** `jpn_2006_2aa164`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2006_2aa164.json.gz).

Find the number of 20-tuple $(p_1, p_2, \dots, p_{10}, q_1, q_2, \dots, q_{10})$ of positive integers with $p_1 = q_{10} = 1$ and $p_i+1 < q_i - p_i$ for all $i = 1, 2, \dots, 9$.



## 2006 — 4

**Record:** `jpn_2006_9417a1`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2006_9417a1.json.gz).

$m, n, a, a', b$ and $b'$ are positive integers with $2 \le m \le n$, $a, a' \le m$, $b, b' \le n$ and $(a, b) \ne (a', b')$.
There is a rectangular town like a chessboard with $m$ avenues and $n$ streets. $\langle x, y \rangle$ represents the intersection of the $x$-th avenue from the west and the $y$-th street from the north. For which $(m, n, a, b, a', b')$ there exists a path from $\langle a, b \rangle$ to $\langle a', b' \rangle$ passing all the intersections exactly once?



## 2006 — 8

**Record:** `jpn_2006_a53c60`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2006_a53c60.json.gz).

Tomohiro and Akinori read mathematical books as follows. Akinori reads 2 pages a day. Tomohiro reads 3 pages a day. However, each of the two stop reading of that day if he reaches the end of a chapter.

There is a mathematical book which consists of 10 chapters and 120 pages. Find the smallest value of the difference between the number of days in which Akinori reads the book and that of Tomohiro. A new chapter always begins with a new page.



## 2006 — 3

**Record:** `jpn_2006_ef0ba3`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2006_ef0ba3.json.gz).

A $3 \times 4$ grid is given. Answer the number of possible cases to write a number among $1$, $2$, $3$ or $4$ in each square so that
* no number appears twice (or more) in the same row, and
* no number appears twice (or more) in the same column.



## 2006 — 10

**Record:** `jpn_2006_ff34be`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2006_ff34be.json.gz).

A dodecahedron and a vertex $X$ of the dodecahedron are given. An ant started from $X$, walked along the edges of the dodecahedron, passing each of the vertices of the dodecahedron except $X$ just once, and returned to $X$. How many such routes exist? We consider a route and its reversal to be different.



## 2007 — 5

**Record:** `jpn_2007_07e0bb`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_07e0bb.json.gz).

There is a grid of $5 \times 5$. And write the integers $1,2,\ldots,16$ in all the grids (each number can be written only once) in the upper left grid of $4 \times 4$ (♣). About the 4 rows, write the sum of four numbers that are written in each row at the right end of each row. Similarly, about the 4 columns, write the sum of four numbers that are written in each column at the lower end of each column. And nothing is written in the lower right grid. Find the maximum integer $m$ which satisfies the following condition.

Conditions: About step (♣), there exists a way of writing the numbers such that you can choose two numbers $a, b$ which $|a-b| \ge m$ hold from the right end column and also from the lower end row.



## 2007 — 4

**Record:** `jpn_2007_2549e4`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_2549e4.json.gz).

On a plane, the band with width $d$ is the set of all points whose distance from a line is less than or equal to $\frac{d}{2}$. There are four points $A$, $B$, $C$, $D$ on the plane. If you chose any three points among them, there exists a band with width $1$ containing them. Prove that there exists a band with width $\sqrt{2}$ containing all four points.



## 2007 — 12

**Record:** `jpn_2007_259143`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_259143.json.gz).

There is a village with a population of $2007$. This village has no name. You are God of this village and you want villagers to decide the name of this village. Every villager has one idea of the village's name.

Each villager can send a letter to each villager (including himself). And every villager can send any number of letters every day. Letters are collected in the evening and delivered at once the next morning every day. The villager who sends the letter can decide to whom the letter should be delivered. And each villager can send a letter to tell the idea of the name of the village to God only one time. This idea doesn't need to be the same as the idea which he and the other villagers had thought at first. And every villager's action is only writing a letter.

Every villager can be classified into an honest person or a liar. You and every villager don't know who is an honest person, and who is a liar. But you know that the number of liars is less than or equal to $T$, and there is one honest person at least in this village.

You can give instructions to every villager only once at noon of one day. An honest person necessarily follows the instruction, but you don't know if a liar follows the instruction. Find the maximum $T$ for which there exists an instruction which fulfills the conditions below.

* At last, every honest person sends a letter to God and every honest person sends the same idea of the village's name.
* If every honest person had thought the same idea of the name of the village at first, every honest person sends this idea to God.



## 2007 — 9

**Record:** `jpn_2007_406148`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_406148.json.gz).

We have a square grid of $19 \times 19$. We call a rectangle **good** if its edges are all along the border of small squares. What is the smallest $n$ with the following property?

Property: If $9$ small squares are removed from the grid, we can divide remaining area into $n$ or less number of good rectangles.



## 2007 — 8

**Record:** `jpn_2007_44d09d`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_44d09d.json.gz).

How many ways are there to cut a cube $S$ into tetrahedron $\{T_1, \dots, T_k\}$ with following properties?
(1) Every vertex of $T_1, \dots, T_k$ is one of the vertices of $S$.
(2) For every $i \neq j$, the intersection of $T_i$ and $T_j$ is a common face of them, a common edge of them, a common vertex of them or empty.



## 2007 — 1

**Record:** `jpn_2007_6677e6`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_6677e6.json.gz).

Let $n$ be a positive integer. Two people $P$, $Q$ play a game in which they call an integer $m$ ($1 \le m \le n$) alternately. $P$ calls the first number. They cannot call the numbers which are already called by themselves or by their opponent. The game is over when neither can call numbers. If the sum of the numbers that $A$ has called is divisible by $3$, $P$ wins, otherwise $Q$ wins. Find all $n$ which satisfy the condition below.

Condition: $P$ can win the game whatever $Q$ does.



## 2007 — 7

**Record:** `jpn_2007_7ed5b8`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_7ed5b8.json.gz).

In how many ways can $100$ be written as a sum of nonnegative powers of $3$? (We consider two ways same if they differ only in the order of numbers.)



## 2007 — 12

**Record:** `jpn_2007_96ded9`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_96ded9.json.gz).

There is a village with a population of $2007$. This village has no name. You are God of this village and you want villagers to decide the name of this village. Every villager has one idea of the village's name.

Each villager can send a letter to each villager (including himself). And every villager can send any number of letters every day. Letters are collected in the evening and delivered at once the next morning every day. The villager who sends the letter can decide to whom the letter should be delivered. And each villager can send a letter to tell the idea of the name of the village to God only one time. This idea doesn't need to be the same as the idea which he and the other villagers had thought at first. And every villager's action is only writing a letter.

Every villager can be classified into an honest person or a liar. You and every villager don't know who is an honest person, and who is a liar. But you know that the number of liars is less than or equal to $T$, and there is one honest person at least in this village.

You can give instructions to every villager only once at noon of one day. An honest person necessarily follows the instruction, but you don't know if a liar follows the instruction. Find the maximum $T$ for which there exists an instruction which fulfills the conditions below.

* At last, every honest person sends a letter to God and every honest person sends the same idea of the village's name.
* If every honest person had thought the same idea of the name of the village at first, every honest person sends this idea to God.



## 2007 — 5

**Record:** `jpn_2007_9c69b3`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_9c69b3.json.gz).

Let $[r]$ be the largest integer not exceeding real number $r$. For real positive numbers $x$, the set $A(x)$ is defined by
$$
A(x) = \{[nx] \mid n: \text{positive integer}\}.
$$
Find all irrational numbers $\alpha > 1$ satisfying the following condition.
Condition: If a positive real number $\beta$ satisfies $A(\alpha) \supset A(\beta)$, then $\frac{\beta}{\alpha}$ is an integer.



## 2007 — 10

**Record:** `jpn_2007_a14cf1`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_a14cf1.json.gz).

There are some cards with positive integers on them, and the sum of these integers is $2007$. For any integer $1 \le k \le 2006$ we can choose some cards so that the sum of the numbers written on those cards is $k$, and there is only one way (if cards with same number are considered to be the same) to do so for each $k$. How many kinds of such a set of cards are possible?



## 2007 — 1

**Record:** `jpn_2007_c7dc24`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_c7dc24.json.gz).

Let $n$ be a positive integer. Two people $P$, $Q$ play a game in which they call an integer $m$ ($1 \le m \le n$) alternately. $P$ calls the first number. They cannot call the numbers which are already called by themselves or by their opponent. The game is over when neither can call numbers. If the sum of the numbers that $A$ has called is divisible by $3$, $P$ wins, otherwise $Q$ wins. Find all $n$ which satisfy the condition below.
Condition: $P$ can win the game whatever $Q$ does.



## 2007 — 5

**Record:** `jpn_2007_ed31dc`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_ed31dc.json.gz).

3 rectangles are placed on a plane, and any 2 rectangles have their edges that are parallel to each other. They divide the plane into several parts. Determine the maximum possible number of such parts. (We consider the area that are contained in no rectangles as one part. For example, if we have only 1 rectangle, the plane is divided into 2 parts.)



## 2007 — 6

**Record:** `jpn_2007_f72375`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2007_f72375.json.gz).

We have 15 cards numbered $1$, $2$, $\dots$, $15$. How many ways are there to choose some (at least 1) cards so that all numbers on these cards are larger than or equal to the number of cards chosen?



## 2008 — 8

**Record:** `jpn_2008_1c7a4f`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2008_1c7a4f.json.gz).

8 coins are placed on a line from left to right.
In the sequel, we keep on repeating the following action:
Choose at random a coin showing a head and satisfying the following condition:
Condition: Either there is no coin on its right showing a tail, or there is no coin on its left showing a tail.
Suppose we keep on repeating this action until there remains no coin showing a head and satisfying the condition stated above. Determine the expectation of the number of coins showing a head when the actions end.



## 2008 — 10

**Record:** `jpn_2008_7fbffd`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2008_7fbffd.json.gz).

2008 boys and 2008 girls decided to get together and play the game of exchanging presents. Each participating boy was asked to bring a bouquet of flowers and each participating girl was asked to bring a bar of chocolate to the get-together. When all the participants showed up, they were lined up in some way and were seated in a circular arrangement with every one facing toward the interior of the circle. Then they were ordered to pass on simultaneously the presents they brought to the person sitting on their right in the circular arrangement. After the actions were repeated a certain number of times the situation was reached where every participating boy had in his possession a chocolate bar and every participating girl possessed a bouquet of flowers. How many possible arrangements of the chairs occupied by the boys are there?



## 2008 — 5

**Record:** `jpn_2008_945846`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2008_945846.json.gz).

Suppose there are 5 cards, each one of which has a distinct number from the set $\{2, 3, 4, 5, 6\}$ written on it. When these cards are placed in line from left to right randomly, what is the probability that for each $i$, $1 \leq i \leq 5$ the number written on the card placed on the $i$-th spot from the left is greater than or equal to $i$?



## 2008 — 12

**Record:** `jpn_2008_ade892`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2008_ade892.json.gz).

Suppose that the combination $(n; a_1, a_2, \dots, a_n)$ of positive integers satisfy the condition $a_1 + a_2 + \dots + a_n = 2008$. Let for each $k$ with $1 \le k \le n$, $A_k = a_1a_2\cdots a_k$. Determine the maximum possible value that the quantity $A_1 + A_2 + \dots + A_n$ can take.



## 2008 — 2

**Record:** `jpn_2008_cd2379`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2008_cd2379.json.gz).

There are $2008$ pieces each of red cards and white cards. These $4016$ cards are mixed and put on a pile. Then, each of the $2008$ participating players is dealt $2$ cards from the pile, and then all of the players are seated in a circular arrangement facing interior of the circle. At every turn of the game each player will perform the following act simultaneously:
If a player possesses at least one red card, he will pass one red card to the player sitting next to him on the left-side. If a player does not have any red card in his possession, then he will pass one white card to the player on his left.
Determine the maximum possible number of turns necessary to reach for the first time the situation where every player will have one each of red and white cards.



## 2008 — 3

**Record:** `jpn_2008_eec352`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2008_eec352.json.gz).

Currently circulating coins in Japanese currency come in 6 different denominations: 500 yen, 100 yen, 50 yen, 10 yen, 5 yen and 1 yen. Taro had 1 each of 1000 yen note, 100 yen coin, 10 yen coin and 1 yen coin. He made a certain purchase from a merchant and handed him all he had and received some change. Assume that Taro made the payment in such a way that he would not receive in the change any coins of the denominations same as what he had had to begin with, nor a 1000 yen note. Furthermore, he chose the method of the payment so that he would end up with the minimum possible number of coins when he received his change. Assume also that the merchant gave Taro the change with minimum possible number of coins. Count the case of no change as a possibility for the purchase price also. Under these conditions how many distinct purchase prices are possible?



## 2009 — 12

**Record:** `jpn_2009_0a1555`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2009_0a1555.json.gz).

A plane lying in the 3-dimensional space splits the space into 2 parts. We call one such part (excluding the plane) a **half space**. Let $S$ be a set consisting of 10 points in the space, no 4 among them lying on a same plane. Determine the number of subsets of $S$ which can be obtained as an intersection of $S$ with some half space.



## 2009 — 9

**Record:** `jpn_2009_4f9146`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2009_4f9146.json.gz).

10 language interpreters are invited to participate in an international mathematical contest. Each of the 10 interpreters is proficient in exactly 2 among the 5 following languages: Greek, Slovanian, Vietnamese, Spanish and German. Furthermore, the combinations of the 2 proficient languages among the 5 are all different for the interpreters. It is decided that the interpreters are distributed into 5 rooms, 2 people per room, in such a way that each pair of the interpreters assigned to the same room shares a common language of proficiency. How many different ways of distributing interpreters satisfy this requirement? Do not distinguish the two arrangements of room assignments in which all the five pairs occupying the same room are identical.



## 2009 — 5

**Record:** `jpn_2009_52732e`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2009_52732e.json.gz).

Determine all non-negative real-valued functions $f$ defined for non-negative real numbers, which satisfy
$$
f(x^2) + f(y) = f(x^2 + y + x f(4y))
$$
for every pair of non-negative real numbers $x$ and $y$.



## 2009 — 5

**Record:** `jpn_2009_981d39`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2009_981d39.json.gz).

Suppose there are $6$ red, $3$ blue and $3$ yellow balls. When you place all of these balls on a straight line, how many distinguishable ways of lining them up are there, in which no adjacent balls are of the same color? Assume that balls of the same color are non-distinguishable.



## 2009 — 2

**Record:** `jpn_2009_c83064`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2009_c83064.json.gz).

Let $N$ be a positive integer. Suppose some collection of integers are written on a blackboard satisfying the following properties.
* Every number $k$ written satisfies $1 \le k \le N$.
* Every $k$ with $1 \le k \le N$ is written at least once.
* The sum of all the numbers written is even.
Prove that by marking some of the numbers written by $\mathcal{O}$ and the rest by $\times$, it is possible to make the sum of those marked by $\mathcal{O}$ equal to the sum of those marked by $\times$.



## 2010 — 5

**Record:** `jpn_2010_04151c`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2010_04151c.json.gz).

Suppose a regular 2010-gon is given. How many combinations of 3 distinct vertices $A$, $B$, $C$ of this polygon are there for which all the inner angles of the triangle $ABC$ have integer-valued degrees (i.e., integral multiples of $1^\circ$)? Regard 2 triples as representing the same combination if one is a permutation of the other.



## 2010 — 1

**Record:** `jpn_2010_1e8d8f`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2010_1e8d8f.json.gz).

How many sextuples $(a, b, c, d, e, f)$ of positive integers are there for which conditions $a > b > c > d > e > f$ and $a+f = b+e = c+d = 22$ are satisfied?



## 2010 — 10

**Record:** `jpn_2010_2a8898`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2010_2a8898.json.gz).

For a positive integer $n$, denote by $S(n)$ the sum of the digits of $n$. If $S(n) = 5$, what is the maximum possible value that $S(n^5)$ can take?



## 2010 — 2

**Record:** `jpn_2010_3b3a8d`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2010_3b3a8d.json.gz).

Let $k$ be a positive integer and $m$ an odd integer. Show that there exists a positive integer $n$ for which the number $n^n - m$ is divisible by $2^k$.



## 2010 — 5

**Record:** `jpn_2010_3dd59d`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2010_3dd59d.json.gz).

Suppose for a convex 2010-gon, any 3 diagonals do not share a common point except for vertices. Let us consider a closed zig-zag line segments (abbr. by Z.Z.L.S.) which goes through each of the vertices of the 2010-gon once and only once. Determine the maximum possible number of the self-intersection points for such a closed Z.Z.L.S. Here, by a closed Z.Z.L.S. we mean contiguous line segments $P_1P_2\ldots P_nP_{n+1}$ for which $P_1 = P_{n+1}$ is satisfied.



## 2010 — 7

**Record:** `jpn_2010_3f9b46`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2010_3f9b46.json.gz).

Consider an infinite sequence $a_1, a_2, a_3, \dots$ of positive integers. Suppose that the following 2 conditions are satisfied for an arbitrary positive integer $n$:
* $a_n$ is a multiple of $n$.
* $|a_n - a_{n+1}| \le 5$.
Find the maximum possible value that $a_1$ can take.



## 2010 — 3

**Record:** `jpn_2010_5ba937`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2010_5ba937.json.gz).

Suppose there are $2010$ islands, and $2009$ bridges connecting some pair of these islands. Any pair of islands are either connected by one of the bridges or they are not. Also, any bridge connects two different islands. Furthermore, one can reach any island from any other island by crossing certain number of bridges. One day, each of the islands sent a letter to some island (possibility of sending the letter to itself was allowed). After the letters were delivered, the following facts came to light:
For islands $A$ and $B$ which are connected by a bridge, the addressee of the letter from $A$ and the addressee of the letter from $B$ are either connected by a bridge or else they are the same island.
Show that in this situation at least one of the following statements must be valid:
(1) There must be an island which sent its letter to itself.
(2) There is a pair of islands connected by a bridge, which exchanged letters.



## 2010 — 12

**Record:** `jpn_2010_61aff6`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2010_61aff6.json.gz).

Suppose there are $2010$ airports. Each airport has a number of direct flights to some of the other airports and the following conditions (1), (2) are known to be satisfied:
(1) For any pair of airports, say $A$ and $B$, one can go from $A$ to $B$, by making connections of several direct flights.
(2) If any one of the direct flights currently in operation is canceled, then the condition (1) will no longer be valid.
One day one of the direct flights in operation is canceled. How many possible ways are there for opening a new direct flight (which may be the same as the canceled one) in order to ensure that both of the conditions (1) and (2) above will be satisfied?
Note that even when there is a direct flight from airport $X$ to airport $Y$ it is not necessarily true that there is a direct flight from $Y$ to $X$.



## 2010 — 6

**Record:** `jpn_2010_869fd1`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2010_869fd1.json.gz).

Suppose there are 3 islands each for 3 different colors, red, blue and yellow. Try to build several bridges so as to satisfy the following conditions:
* For any pair of islands, they are either connected by a bridge or not connected by any bridge, and every bridge connects two distinct islands.
* For any pair of islands of a same color, there is no bridge connecting the pair, and furthermore, there is no island which is connected to both of the islands in the pair by bridges.
How many ways of building bridges to satisfy these conditions? Building no bridges will be counted as one possibility.



## 2010 — 2

**Record:** `jpn_2010_b192db`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2010_b192db.json.gz).

Find the average value of all those integers $n$ satisfying $0 \le n \le 10000$ for which the digit $1$ does not appear in their decimal expansions.



## 2010 — 9

**Record:** `jpn_2010_c054ab`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2010_c054ab.json.gz).

How many ways of lining up $2010$ white stones and $2010$ black stones along a horizontal straight line are there so as to satisfy the following condition?

* In the line-up there are odd number of pairs consisting of one white stone and one black stone with the white one lying on the right of the black one.



## 2011 — 7

**Record:** `jpn_2011_570513`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2011_570513.json.gz).

A square with side length $3$ is partitioned into a $3 \times 3$ grid with $9$ unit squares. In each of the $9$ unit squares a distinct positive integer greater than or equal to $1$ and less than or equal to $9$ is inserted. For each of the $3$ columns the second largest of the $3$ numbers appearing on that column is marked. How many possible arrangements of the $9$ integers are there if the second largest of the $3$ marked numbers is $5$?



## 2011 — 3

**Record:** `jpn_2011_7b87b7`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2011_7b87b7.json.gz).

Let $N$ be a positive integer. $N$ squares are lined up contiguously from left to right. Students A and B play a game according to the following rules:
(1) To start off, A will write 1 non-negative integer into each of the $N$ squares.
(2) The game ends when the following condition is achieved: For every $i$ satisfying $1 \le i \le N - 1$, the number in the $i$-th square from the left is less than or equal to the number in the $(i+1)$-th square from the left. The game continues as long as this condition is not achieved by repeating the following procedure:
(a) A designates 1 non-negative integer.
(b) B chooses one of the $N$ squares and replaces the number in that square by the number designated by A in (a).
Is it possible for B to end the game no matter how A plays?



## 2011 — 9

**Record:** `jpn_2011_8c8ec4`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2011_8c8ec4.json.gz).

Suppose $12$ boxes are lined up from left to right. We want to put a ball in each of these $12$ boxes. Balls are colored red, blue or yellow. How many distinct ways of putting balls into the $12$ boxes are there if the following condition is to be satisfied?

* Condition: For each ball placed in a box, at least $1$ of the balls in the adjacent boxes has the same color as its color.



## 2011 — 1

**Record:** `jpn_2011_9ace44`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2011_9ace44.json.gz).

How many quadruples $(a, b, c, d)$ of positive integers lying in between $1$ and $9$ ($1$ and $9$ inclusive) are there which satisfy $0 < b - a < c - b < d - c$?



## 2012 — 3

**Record:** `jpn_2012_365658`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2012_365658.json.gz).

Let $a, b, c, d, e, f, g, h, i$ be the distinct integers lying in between $1$ and $9$ (both $1$ and $9$ inclusive). Let $N$ be the maximum of the three numbers $a \times b \times c$, $d \times e \times f$ and $g \times h \times i$. Determine the minimum value the number $N$ can take.



## 2012 — 6

**Record:** `jpn_2012_592bd2`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2012_592bd2.json.gz).

A $2 \times 100$ square grid is given. Suppose we color each of the $200$ square boxes of the grid either red or blue. How many possible ways of coloring these boxes are there that satisfy the following conditions? Regard two patterns of colored boxes to be distinct if one of the patterns can be obtained from the other by rotating or flipping.

* There is at least one box colored red and at least one box colored blue.
* The region determined by all the red colored boxes forms a connected region and the same is true for blue colored boxes. (Here we consider $2$ boxes to be connected if they share a side).



## 2012 — 8

**Record:** `jpn_2012_70a429`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2012_70a429.json.gz).

How many possible ways of writing down a sequence of positive integers are there satisfying the following conditions?
Conditions: You start out with writing down the number $2012$ and end up with writing down the number $1$, and after writing down a number $n$ you follow with writing an integer less than or equal to $\sqrt{n}$.



## 2012 — 11

**Record:** `jpn_2012_8619cd`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2012_8619cd.json.gz).

Let $n$ be a positive integer and suppose a $2n \times 2n$ square grid is given. Suppose we color exactly $2n^2$ square boxes of the grid in such a way that the following condition is satisfied.

Condition: If a box is colored then none of the boxes which share only a vertex with that box is not colored.

How many ways of coloring $2n^2$ square boxes of the grid are there that satisfy the condition stated above? We regard two configurations of colored boxes to be distinct if one configuration can be transposed on the other by rotation or by flipping.



## 2012 — 5

**Record:** `jpn_2012_993c1a`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2012_993c1a.json.gz).

Let $k$ be a positive integer. Players $A$ and $B$ play a game according to the following rule: Initially, a chess piece is placed at the origin $(0, 0)$ of the $xy$-plane. The player $A$ will start the game followed by $B$ and repeat, each choosing a strategy among those specified by the following rules:
* Possible strategies for $A$: Choose a lattice point, which is not occupied by the chess piece and mark the point by a $\checkmark$.
(Here, by a lattice point we mean a point in the $xy$-plane whose $x$-coordinate and $y$-coordinate are both integers).
* Possible strategies for $B$: Repeat the process of moving the chess piece located at $(x, y)$ to either $(x+1, y)$ or $(x, y+1)$ $j$ times where $1 \le j \le k$. However, in each move of the process he is not allowed to move the chess piece into a lattice point marked by a $\checkmark$.
$A$ wins the game if $B$ gets into the situation where he cannot move the chess piece. Determine all possible values for $k$ for which $A$ can win the game after a finite number of steps no matter how $B$ chooses his strategies.



## 2012 — 5

**Record:** `jpn_2012_b3b037`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2012_b3b037.json.gz).

Given a piece on the origin in the coordinate plane. Two persons $A$, $B$ act as the following. First $A$ marks on a lattice point on which a piece isn't put. Then $B$ moves a piece put on the point $(x, y)$ to the point $(x + 1, y)$ or $(x, y + 1)$ $m$ times ($1 \leq m \leq k$). Note that we may not move the piece to unmarked point. If $A$ wins when $B$ can't move any pieces, then find all possible integers $k$ such that $A$ will win at finite action in regardless of how $B$ moves each piece.



## 2013 — 7

**Record:** `jpn_2013_050803`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_050803.json.gz).

How many 25-tuples $(x_1, x_2, \dots, x_{25})$ of non-negative integers are there which satisfy the following identity?
$$
x_1^2 + x_2^2 + \dots + x_{25}^2 = 2 + x_1x_2 + x_2x_3 + \dots + x_{24}x_{25}.
$$



## 2013 — 5

**Record:** `jpn_2013_348c1d`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_348c1d.json.gz).

Let $n$ be a positive integer. Points $P_1, P_2, \dots, P_{4n}$ are placed in a plane in such a way that no 3 points among them lie on any straight line. Furthermore, for each $i = 1, 2, \dots, 4n$ if we rotate the half-line $P_i P_{i-1}$ starting at $P_i$ around the point $P_i$ by $90^\circ$ clockwise, then the half line falls onto the half-line $P_i P_{i+1}$ starting at $P_i$. Determine the maximum possible number of the pairs $(i, j)$ for which the line segments $P_i P_{i+1}$ and $P_j P_{j+1}$ intersect at a point different from the end points of the line segments. Here we let $P_0 = P_{4n}, P_{4n+1} = P_1$ and assume that $1 \le i < j \le 4n$.



## 2013 — 1

**Record:** `jpn_2013_45e694`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_45e694.json.gz).

Let $n, k$ be positive integers satisfying $n \ge k$.
There is a group consisting of $n$ people. Each person of this group belongs to one and only one of $k$ clubs, called club $C_1, C_2, \dots, C_k$. Each club has at least one member belonging to it. Prove that it is possible to distribute $n^2$ pieces of cake to these $n$ people in such a way to satisfy all of the following conditions:
* Every one receives at least 1 piece of cake.
* For each $i$ $1 \le i \le k$, every member of the club $C_i$ receives $a_i$ pieces of cake.
* If $1 \le i < j \le k$, then $a_i > a_j$ is satisfied.



## 2013 — 11

**Record:** `jpn_2013_519e11`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_519e11.json.gz).

Let $n$ be a positive integer. By a lattice point in the $xyz$-space we mean a point $(k, l, m)$ where $k, l, m$ are integers. A line segment connecting two lattice points contained in the region $0 \le x, y, z \le n$ and distance 1 between them is called a lattice segment. We can assign a direction to each lattice segment (e.g., for a lattice segment with end points $A$ and $B$ assign one and only one of the directions $A \rightarrow B$, or $A \leftarrow B$). Call a square a lattice square if all of the four sides of the square are lattice segments. Let us say that two lattice squares are congruent if by rotation and a parallel displacement one can place one of the squares on top of the other square with further requirement that the directions of all four sides coincide. How many ways of assigning directions to lattice segments are there assuring that all the lattice squares are congruent?



## 2013 — 5

**Record:** `jpn_2013_6a6bc7`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_6a6bc7.json.gz).

Let $n$ be a positive integer. Points $P_1, P_2, \dots, P_{4n}$ are placed in a plane in such a way that no 3 points among them lie on any straight line. Furthermore, for each $i = 1, 2, \dots, 4n$ if we rotate the half-line $P_i P_{i-1}$ starting at $P_i$ around the point $P_i$ by $90^\circ$ clockwise, then the half line falls onto the half-line $P_i P_{i+1}$ starting at $P_i$. Determine the maximum possible number of the pairs $(i, j)$ for which the line segments $P_i P_{i+1}$ and $P_j P_{j+1}$ intersect at a point different from the end points of the line segments. Here we let $P_0 = P_{4n}, P_{4n+1} = P_1$ and assume that $1 \le i < j \le 4n$.



## 2013 — 10

**Record:** `jpn_2013_798f65`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_798f65.json.gz).

There are 2013 cards numbered $0$, $1$, $2$, $\ldots$, $2012$. Initially, all the cards are placed with the face with a written number down. Then, we perform for each $i = 1, 2, \dots, 2013$ the following operation $i$ starting with $i = 1$ and with increasing order ending up with $i = 2013$:

Operation $i$: Flip each of the $i$ cards having the number $\left\lfloor \frac{2013j}{i} \right\rfloor$ for $j = 0, 1, \dots, i - 1$.

How many cards are with their faces up (showing their numbers) at the end of all the operations?

Here we denote by $[r]$ for each real number $r$ the greatest integer less than or equal to $r$.



## 2013 — 12

**Record:** `jpn_2013_c38542`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_c38542.json.gz).

Let $a_1, a_2, \dots$ be an infinite sequence of distinct non-zero real numbers for which $\frac{a_{i+1}}{a_i} + \frac{a_{i+1}}{a_i}$ takes the same value lying in between 0 and 2 for each $i \ge 1$. Express in terms of $a_1, a_2, a_3$ the smallest number $c$ satisfying the following condition:
Condition: For any pair of positive integers $x, y$ with $x < y$,
$$
\frac{a_x a_{x+1} + a_{x+1} a_{x+2} + \dots + a_{y-1} a_y}{a_x a_y} \le c \quad \text{holds.}
$$



## 2013 — 6

**Record:** `jpn_2013_eb415f`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2013_eb415f.json.gz).

There are $24$ pieces each of two different kinds of cakes $A$ and $B$. All the cakes will be distributed among three people $X$, $Y$, $Z$. A method of distribution where a person may not receive any cake of a particular kind is allowed for consideration. How many different ways of distributing cakes are there in which there are no pairs of people ending up with the following situation?

One person in the pair receives $a$ pieces of $A$ and $b$ pieces of $B$, and the other person in the pair receives $a'$ pieces of $A$ and $b'$ pieces of $B$, where all of the conditions $a \le a'$, $b \le b'$ and $a+b < a'+b'$ are satisfied.



## 2014 — 7

**Record:** `jpn_2014_69b91c`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2014_69b91c.json.gz).

In a certain school, there is a committee consisting of 4 members. There are 4 sub-committees for this committee, and each committee member will be asked to chair a different sub-committee. Suppose each committee member has 2 sub-committees he prefers to chair. It is known that there are exactly 2 ways to assign sub-committees to members in such a way to satisfy the preferences of all the members. How many possible combinations of the preferences of all four members are there in this situation?



## 2014 — 6

**Record:** `jpn_2014_74269a`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2014_74269a.json.gz).

There are two blackboards $A$ and $B$, and on each of these blackboards certain number of distinct integers greater than or equal to $2$ and less than or equal to $20$ are written in such a way that any pair of numbers one of which is chosen from $A$ and the other from $B$ are relatively prime. Determine the maximum possible value the product of the number of integers written on $A$ and the number of integers written on $B$ can take.



## 2014 — 2

**Record:** `jpn_2014_8f91d2`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2014_8f91d2.json.gz).

Suppose we assign one of positive integers $n$ satisfying $1 \le n \le 8$ to each of the 8 vertices of a regular octagon. How many ways of assigning these numbers are there, which satisfy the following 2 conditions?:
* assigned numbers are all distinct.
* any pair of numbers assigned to adjacent vertices are relatively prime.
Regard two assignments of 8 numbers to be distinct if one is obtained from the other by rotation or flipping of the octagon.



## 2014 — 5

**Record:** `jpn_2014_a052c4`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2014_a052c4.json.gz).

Find the value of
$$
\sum 17C_a \cdot 17C_b \cdot 17C_c,
$$
where the sum is taken over all triples $(a, b, c)$ of non-negative integers satisfying $a+b+c=5$.



## 2014 — 3

**Record:** `jpn_2014_adb623`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2014_adb623.json.gz).

Let $n$ be a positive integer. For every pair of students enrolled in a certain school having $n$ students, either the pair are mutual friends or not mutual friends. Let $N$ be the smallest possible sum $a+b$ of positive integers $a$ and $b$ satisfying the following 2 conditions concerning students in this school:
(1) It is possible to divide students into $a$ teams in such a way that any pair of students belonging to a same team are mutual friends.
(2) It is possible to divide students into $b$ teams in such a way that any pair of students belonging to a same team are not mutual friends.
Assume that every student will belong to one and only one team when the students are divided to form teams to satisfy the conditions (1) and (2) above, and a team may consist of only one student, in which case this team is assumed to satisfy both of the conditions: that any pair of students in this team are mutual friends; are not mutual friends. Determine in terms of $n$ the maximum possible value that $N$ can take.



## 2014 — 11

**Record:** `jpn_2014_bd1bef`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2014_bd1bef.json.gz).

Consider an operation of putting an integer greater than or equal to $1$ and less than or equal to $6$ to each square in a grid of $6 \times 6$ squares. For a pair of integers $(i, j)$ with $1 \le i, j \le 6$, denote by $i \diamond j$ the integer put into the square located on $i$-th row and $j$-th column after an operation. How many different operations are there which satisfy the following 2 conditions?

* For every $i$ ($1 \le i \le 6$), $i \diamond i = i$ holds.
* For every choice of $i, j, k, \ell$ with $1 \le i, j, k, \ell \le 6$, $(i \diamond j) \diamond (k \diamond \ell) = i \diamond \ell$ holds.



## 2014 — 10

**Record:** `jpn_2014_f4f5dc`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2014_f4f5dc.json.gz).

For a grid of $55 \times 55$ squares, let us consider the following operation:

Operation: Choose a rectangular region consisting of a number of squares from the grid, and color the region either white or black.

Determine the smallest possible number of operations necessary to reach from the initial configuration, in which all the squares are colored white to the configuration satisfying the following conditions:
* the square at the upper left corner is colored black.
* every square sharing a side with a black-colored square is colored white.
* every square sharing a side with a white-colored square is colored black.



## 2015 — 5

**Record:** `jpn_2015_2c74e3`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2015_2c74e3.json.gz).

Let $a$ be a positive integer. Show the following assertion is valid for sufficiently large integer $n$:
From a grid of squares extending to $\pm\infty$ in both $x$- and $y$-directions, choose $n$ unit (i.e., $1 \times 1$) squares and color them black. Let $K$ be the number of $a \times a$ square blocks which contain exactly $a$ black unit squares. Then the maximum possible value $K$ can take is $a(n+1-a)$.
Here, by the statement "An assertion is valid for sufficiently large $n$", we mean that there exists a positive integer $N$ for which the assertion is valid for all $n \ge N$.



## 2015 — 9

**Record:** `jpn_2015_7ab8a2`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2015_7ab8a2.json.gz).

There are $4030$ numbers consisting of two of each number lying in between (and including) $1$ and $2015$. Suppose we line up these numbers from left to right. An ordered sequence of $2015$ numbers chosen from this line-up of $4030$ numbers and considered with the order inherited from the original line-up is called a *half-sequence*. What is the largest possible number of distinct half-sequences? Regard two half-sequences to be the same if they represent the same sequence of integers, even if they may come from different portions of the original line-up.



## 2015 — 7

**Record:** `jpn_2015_bd227a`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2015_bd227a.json.gz).

Let $l$ be a straight line lying on the $xy$-plane. For given $20 \times 15$ points $(m, n) : (m = 1, 2, \dots, 20, n = 1, 2, \dots, 15)$ on the $xy$-plane, there are $222$ straight lines parallel to the line $l$ ($l$ itself may be considered as one of those parallel lines) and going through at least one of these points. How many straight lines are there which go through at least one of these points and are perpendicular to $l$?



## 2015 — 4

**Record:** `jpn_2015_d092b4`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2015_d092b4.json.gz).

Suppose you want to distribute nine distinct integers greater than or equal to $1$ and less than or equal to $9$ into nine square boxes of a $3 \times 3$ grid in such a way that the sums of the numbers on each row and each column are all multiples of $3$. How many possible ways of distributing numbers are there to attain this goal? Regard two configurations, for which one can be obtained from rotating the other one or by flipping over the other one, to be distinct in counting the number of possible ways.



## 2019 — 3

**Record:** `jpn_2019_000cfe`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2019_000cfe.json.gz).

A $3 \times 3$ grid made up of $9$ $1 \times 1$ squares is given. Suppose you want to distribute $9$ distinct positive integers chosen from the integers greater than or equal to $1$ and less than or equal to $9$ into $9$ square boxes of the grid. How many distinct ways of distributing the $9$ numbers are there if for any pair of boxes sharing a side the difference of the numbers inserted must be $3$ or less? Even when the two configurations of the result of distribution coincide under a rotation or flipping over, regard the configurations distinct.



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



## 2019 — 9

**Record:** `jpn_2019_a2033b`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2019_a2033b.json.gz).

A $4 \times 4$ grid made up of $16$ $1 \times 1$ squares is given. Suppose we want to color each of the squares by using one of the four colors, red, blue, yellow or green. How many ways of painting all of the boxes are there if the following requirement must be met:
For any row and any column one of the following 3 conditions must be satisfied:
* all four squares must be colored by the same color.
* use two colors, each one to be used to color two squares.
* use all four colors, each one to be used to color one square.



## 2019 — 12

**Record:** `jpn_2019_e2fec2`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2019_e2fec2.json.gz).

Let $S = \{1, 2, \dots, 6\}$. Let $\mathcal{S}$ be the set of all subsets of $S$. How many mappings $F: \mathcal{S} \to \mathcal{S}$ are there that satisfy the following condition:
$$
F(F(A) \cup B) = A \cap F(B) \text{ for any pair of subsets of } S.
$$



## 2021 — 2

**Record:** `jpn_2021_5230d7`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2021_5230d7.json.gz).

Let $n > 1$ be an integer. Alice and Bob play the following game using an $n \times 2021$ grid. First, Alice colors each square either black or white. Bob places a piece in one of the squares in the top row and designates one square in the bottom row as the goal. Then, Alice repeatedly does the following operation $n-1$ times:
> If the piece is on a white square, she moves the piece to the square one below.
> Otherwise, she moves the piece to one left or right and then to one below.

Find the minimum possible value of $n$ such that Alice can always move the piece to the goal regardless of Bob's choice.



## 2021 — 5

**Record:** `jpn_2021_8a2d04`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2021_8a2d04.json.gz).

Let $n$ be a positive integer. Determine all integers $1 \le k \le 2n^2$ satisfying the following condition.

> There is a $2n \times 2n$ board. When $k$ distinct cells are chosen and colored black, while the other cells are colored white, the minimum number of the $2 \times 2$ squares which have both black and white cells is $2n-1$.



## 2021 — 9

**Record:** `jpn_2021_aec1d9`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2021_aec1d9.json.gz).

Let $A$ be the number of cases such that each cell of a $2021 \times 2021$ table is filled with one of $1$, $2$, or $3$ in such a way that any $2 \times 2$ square in the table sums up to $8$. Answer the remainder after dividing $A$ by $100$.



## 2021 — 4

**Record:** `jpn_2021_ce7bea`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2021_ce7bea.json.gz).

There are three distinct positive integers written on the blackboard. When real numbers $a$, $b$, $c$ are on the blackboard, consider the procedure that replaces those three numbers with $\frac{b+c}{2}$, $\frac{c+a}{2}$, $\frac{a+b}{2}$ at the same time. After this procedure is done $2021$ times, all three numbers on the blackboard are positive integers. Determine the minimum value of the sum of initial three positive integers on the blackboard.



## 2022 — 8

**Record:** `jpn_2022_135c78`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2022_135c78.json.gz).

Find the number of tuples of positive integers $(a_1, a_2, \dots, a_{2022})$ which satisfy $a_1 < a_2 < \dots < a_{2022}$ and
$$
a_1^2 - 6^2 \ge a_2^2 - 7^2 \ge \dots \ge a_{2022}^2 - 2027^2.
$$



## 2022 — 1

**Record:** `jpn_2022_269940`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2022_269940.json.gz).

Alex and Betty play a game with a row of consecutive $2022$ cells. At the start of the game, the name of Alex is written in the $1$st, $3$rd, ..., $2021$st cells from the left and the name of Betty is written in the $2$nd, $4$th, ..., $2022$nd cells from the left. Starting from Alex, two players do the following operation in turn.
Choose two cells with his or her own name which are not adjacent such that all cells between the two have the opponent's name. Then replace opponent's names with his or her own names for all cells between the chosen two.
The game ends when one player is not able to do the operation. Determine the largest positive integer $m$ satisfying the following condition.
No matter how Betty does the operations, Alex can play such that there are $m$ or more cells with Alex's name at the end of the game.



## 2022 — 10

**Record:** `jpn_2022_60aa31`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2022_60aa31.json.gz).

Determine the number of ways to choose distinct $25$ integers from $1$ to $50$ such that for any two integers chosen, one is not a divisor of the other.



## 2022 — 9

**Record:** `jpn_2022_e8d416`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2022_e8d416.json.gz).

How many permutations $(p_1, p_2, \dots, p_{1000})$ of $\{1, 2, \dots, 1000\}$ are there such that $p_i$ is a multiple of $i$ for any $1 \le i \le 999$?



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



## 2023 — 2

**Record:** `jpn_2023_87c2d1`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2023_87c2d1.json.gz).

Let us call a positive integer a *good number* if the digit $2$ appears more frequently than the digit $3$, and a *bad number* if the digit $3$ appears more frequently than the digit $2$. For example, $2023$ is a good number because the digit $2$ appears twice and the digit $3$ once, and $123$ is neither a good number nor a bad number because the digit $2$ appears once and the digit $3$ once.
Find the difference between the number of good numbers less than or equal to $2023$ and the number of bad numbers less than or equal to $2023$.



## 2023 — 9

**Record:** `jpn_2023_b42b43`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2023_b42b43.json.gz).

How many permutations $p_1, p_2, \dots, p_{2023}$ of $1, 2, \dots, 2023$ satisfy the equation
$$
p_1 + |p_2 - p_1| + |p_3 - p_2| + \dots + |p_{2023} - p_{2022}| + p_{2023} = 4048?
$$



## 2023 — 11

**Record:** `jpn_2023_b7080f`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2023_b7080f.json.gz).

Alice and Bob are playing a game using a blackboard. Initially, each of $2, 3, \dots, 50$ is written on the blackboard once. Also, a non-empty subset $S$ of $\{2, 3, \dots, 50\}$ is given. In the first turn, Alice erases all the elements of $S$ from the blackboard. After that, the two players, starting with Bob, take turns erasing one or more integers from the blackboard. However, they cannot erase integers that are relatively prime to all of the integers erased in the opponent's previous turn. The game ends when a player has no integers left to erase at the beginning of their turn, resulting in that player's loss and the other player's win.
How many sets $S$ are there such that Alice can always win, regardless of Bob's actions?



## 2023 — 5

**Record:** `jpn_2023_faa0e3`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2023_faa0e3.json.gz).

We denote $S = \{1, 2, \dots, 3000\}$. Find the maximum possible value of an integer $X$ that satisfies the following condition:
For any bijection $f: S \to S$, there exists a bijection $g: S \to S$ such that
$$
\sum_{k=1}^{3000} \left( \max\{f(f(k)), f(g(k)), g(f(k)), g(g(k))\} - \min\{f(f(k)), f(g(k)), g(f(k)), g(g(k))\} \right)
$$
is no less than $X$.



## 2024 — 3

**Record:** `jpn_2024_5e3413`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2024_5e3413.json.gz).

Let us call a point in the $xy$-plane a good point if each of its coordinates is an integer from $1$ to $2000$. Let us also call polyline $ABCD$ a Z-shaped polyline if four points $A(x_1, y_1)$, $B(x_2, y_2)$, $C(x_3, y_3)$, $D(x_4, y_4)$ satisfy all the following conditions:
* $A$, $B$, $C$, $D$ are good points.
* $x_1 < x_2$, $y_1 = y_2$.
* $x_2 > x_3$, $y_2 - x_2 = y_3 - x_3$.
* $x_3 < x_4$, $y_3 = y_4$.
Determine the smallest possible positive integer $n$ such that, there exist Z-shaped polylines $Z_1, Z_2, \dots, Z_n$ which satisfy the following condition:
Any good point $P$ lies on $Z_i$ for some $1 \le i \le n$.
Note that polyline $ABCD$ is the union sets of line segments (including both endpoints) $AB$, $BC$ and $CD$.



## 2024 — 4

**Record:** `jpn_2024_851b05`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2024_851b05.json.gz).

Let $0 \le n \le 5^5$ be an integer. Arrange $n$ black stones and $5^5-n$ white stones in a row, and repeat the following operation 5 times:
Divide the row of stones into groups of 5 stones from left to right. For each group, replace the 5 stones in the group with one stone of the color that appears more frequently among them.
Find the smallest possible value of $n$ for which the single remaining stone at the end is always black regardless of the initial arrangement of stones.



## 2024 — 10

**Record:** `jpn_2024_8d022e`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2024_8d022e.json.gz).

Consider filling each square of an $100 \times 100$ table with one of the letters J, M, or O. A $2 \times 2$ square of the table is called a **good block** if it satisfies one of the following conditions:
* The four squares have exactly one type of letter.
* The four squares have exactly two types of letters, and each letter appears twice.
* The four squares have exactly three types of letters, and the lower-left and upper-right squares have the same letter.
Find the number of ways of filling the 10000 squares of the table satisfying the following two conditions:
* Every $2 \times 2$ square of the table is a good block.
* Among pairs of two adjacent squares (sharing an edge) of the table, there are exactly 10000 pairs whose two squares have different letters. Here, two pairs where the order of squares is just swapped are considered as the same pair and are counted only once.
Note that we distinguish two ways of filling which can be obtained from each other by rotations or reflections.



## 2024 — 1

**Record:** `jpn_2024_e48072`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2024_e48072.json.gz).

Let $n \ge 2$ be an integer. Find all sets of real numbers $(a_1, a_2, \dots, a_n)$ such that $a_1 - 2a_2, a_2 - 2a_3, \dots, a_{n-1} - 2a_n, a_n - 2a_1$ is a permutation of $a_1, a_2, \dots, a_n$. Note that $a_1, a_2, \dots, a_n$ itself is also a permutation of $a_1, a_2, \dots, a_n$.



## 2025 — 3

**Record:** `jpn_2025_3422c1`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2025_3422c1.json.gz).

Let $n$ be a positive integer. Consider triples $(x_1, y_1, z_1)$, $(x_2, y_2, z_2)$, \dots, $(x_n, y_n, z_n)$ which consist of integers $1, 2, \dots, 100$ and satisfy the following condition:
For all infinite sequences $a_1, a_2, \dots$ which consist of integers $1, 2, \dots, 100$, there exist a positive integer $i$ and an integer $j$ with $1 \le j \le n$ such that $(a_i, a_{i+1}, a_{i+2}) = (x_j, y_j, z_j)$.
Determine the minimum possible value of $n$.



## 2025 — 7

**Record:** `jpn_2025_42febe`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2025_42febe.json.gz).

Alice plays a game using a board with 20 rows and 25 columns. Initially, no number is written in any of the $20 \times 25$ cells. The game proceeds in several turns, and on the $n$-th turn, the following operation is performed:
Choose a positive integer $k$ and $k$ empty cells $A_1, A_2, \dots, A_k$ such that for every integer $i$ with $1 \le i \le k-1$, the cell $A_{i+1}$ is adjacent to $A_i$ either to the right or above. Write the number $n$ in each of these $k$ cells.
The game ends when all cells on the board are filled with some numbers. When Alice plays optimally to minimize the number of turns until the game ends, how many different possible numberings of the board can be obtained when the game ends?
Note: Numberings that are identical under rotation or reflection are considered distinct and counted as different.



## 2025 — 10

**Record:** `jpn_2025_957b3e`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/japan/jpn_2025_957b3e.json.gz).

Let $S = \{0, 1, 2, \dots, 8\}$. How many functions $f : S \to S$ satisfy the following condition: For any elements $x, y, z \in S$, if $x+y-z$ is divisible by $9$, then $f(x)f(y) - f(f(z))$ is also divisible by $9$?



# KMO


## 2006 — 6

**Record:** `kor_2006_38a9dc`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2006_38a9dc.json.gz).

A positive integer $N$ is said to be an "*n*-good number" if it satisfies the following two properties:
(Property 1) $N$ is divisible by at least $n$ distinct primes
(Property 2) There exist distinct positive divisors $1, x_2, \dots, x_n$ of $N$ such that
$$
1 + x_2 + \dots + x_n = N.
$$
Show that there exists an "*n*-good number" for each $n \ge 6$.



## 2006 — 3

**Record:** `kor_2006_4bfe96`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2006_4bfe96.json.gz).

Three schools $A$, $B$ and $C$ participate in a chess tournament with five students from each school. Let $a_1, a_2, \dots, a_5; b_1, b_2, \dots, b_5; c_1, c_2, \dots, c_5$ be the list of the players from $A$, $B$, $C$ respectively. Let $P_A$, $P_B$, $P_C$ be the scores that schools $A$, $B$, $C$ make, respectively, when the tournament is over following the rules described below. Find the remainder of the number of possible triples $(P_A, P_B, P_C)$ when it is divided by $8$.

1. Players from each school have matches in order from the first one, and if a player is once defeated then he (or she) is eliminated from the tournament. The first match of the tournament is between the players $a_1$ and $b_1$.

2. When $x_i$ from school $X$ is defeated by $y_i$ from $Y$, if there are players left from the school $Z$ other than $X$, $Y$ then $y_i$ have another match with a player from $Z$, if there is no player left in $Z$ but there are players from $X$ then $y_j$ have a match with $x_{i+1}$. The tournament is over when no player is left in two schools.

3. School $X$ adds $10^{i-1}$ points to its score when $x_i$ from $X$ wins a match.



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



## 2008 — 6

**Record:** `kor_2008_d12348`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2008_d12348.json.gz).

There is an $n \times n$ chess board. Each of the $n^2$ small boxes can present a number from $0$ to $k$, for some positive integer $k$. In each row and column, there is a button and if we push the button in a row (or column), the number in each of the $n$ small boxes contained in that row (or column, respectively) increases by $1$ and the number $k$ is changed to $0$. We call this a "process". At first, the number $0$ was presented in every $n^2$ small box. But there were some processes and the numbers were changed. Show that every number in the $n^2$ small boxes can be changed to $0$ by taking at most $kn$ processes.



## 2009 — 5

**Record:** `kor_2009_03f95a`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2009_03f95a.json.gz).

Two players play a game on a $(m+1)$ by $m$ grid, which has $m+1$ horizontal lines, $m$ vertical lines, and hence $m(m+1)$ intersection points. One pebble is put on an intersection point. Two players alternatively move the pebble to an adjacent point along an edge, but they are not allowed to use edges used previously by either player. A player loses if he cannot move the pebble any more. Prove that there exists a winning strategy for the first player if the pebble was initially put on a point in the bottom horizontal line.



## 2009 — 3

**Record:** `kor_2009_89116d`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2009_89116d.json.gz).

In a table, there are $2009$ coins each with one side white and the other side black. At the beginning all coins are aligned in a row with all their white sides up except one with its black side up. In each step we choose a coin with black side up and flip the two adjacent coins. If we choose the outermost coin, then we flip just one adjacent coin. Find all positions of the black coin at the beginning from which we can reach the state where all coins have black sides up.



## 2010 — 5

**Record:** `kor_2010_1dc4be`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2010_1dc4be.json.gz).

Around a table $2n$ people are seated and $m$ cookies are distributed to them. These people can pass cookies under the following rules:

- One can only pass cookies to his/her neighbors.
- One can pass a cookie only if he or she eats one cookie.

Let $A$ be one of these people. Find the minimum $m$ such that no matter how $m$ cookies were distributed, there is a strategy to pass cookies so that $A$ has at least one cookie.



## 2010 — 3

**Record:** `kor_2010_8787ab`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2010_8787ab.json.gz).

When there is a link from a webpage $i$ to a webpage $j$, you can move from the webpage $i$ to the webpage $j$ directly. For $n \ge 2$, there are $n$ many webpages numbered from $1$ to $n$, and for all $i \in \{1, 2, \dots, n-1\}$, there is a link from the webpage $i$ to the webpage $(i+1)$.
Now you are allowed to add new links to the webpages so that new links can connect two webpages from $i$ to $j$ when $i < j$. Prove that there exist a way to add at most $3(n-1) \log_2(\log_2 n)$ many such new links so that for any two integers $1 \le i < j \le n$, you can move from the webpage $i$ to the webpage $j$ using at most 3 links.



## 2011 — 6

**Record:** `kor_2011_33308c`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2011_33308c.json.gz).

We are given a rectangular $m \times n$ chessboard with $m$ unit squares in each row and $n$ unit squares in each column. We are going to assign an integer to each unit square. A rectangle $R$ consisting of one or more unit squares is called a *shelf* if there is an integer $h$ satisfying the following two conditions:

1. The number in each unit square in $R$ is larger than $h$.
2. The number in a unit square out of $R$ sharing an edge or a point with $R$ is at most $h$.

(We assume that a shelf $R$ contains all interior unit squares in the rectangle.) What is the number of shelves if we assign integers to maximize the number of shelves?



## 2011 — 3

**Record:** `kor_2011_ea207d`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2011_ea207d.json.gz).

There were $n$ boys $a_1, a_2, \dots, a_n$ and $n$ girls $b_1, b_2, \dots, b_n$ in a party. No boys shook hand with each other and no girls shook hand with each other and for each $i \in \{1, 2, \dots, n\}$, $a_i$ did not shake his hand with $b_i$. We want to divide all $2n$ people into groups satisfying the following two conditions.
1. In each group, the number of boys is equal to the number of girls.
2. In each group, no two people shook hands with each other.
Let $m$ be the number of pairs $(a_i, b_j)$ where $a_i$ shook his hand with $b_j$. Prove that it is possible to make the number of groups less than or equal to $2$ or $\frac{2m}{n} + 1$.



## 2012 — 6

**Record:** `kor_2012_7f29e1`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2012_7f29e1.json.gz).

Let $M$ be the set of positive integers which is not divisible by any prime number greater than $3$. For arbitrary chosen subsets $A_1, A_2, A_3, \dots$ of $M$, prove that there exist two distinct positive integers $i$ and $j$ such that:
For each $x$ in $A_i$, $A_j$ has a divisor of $x$.



## 2012 — 3

**Record:** `kor_2012_e426b1`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2012_e426b1.json.gz).

Let $A_1, A_2, \dots, A_n$ be sets. For a subset $X$ of $\{1, 2, \dots, n\}$, let
$$
N(X) = \{i \in \{1, 2, \dots, n\} - X : A_i \cap A_j \neq \emptyset \text{ for all } j \in X\}.
$$
Prove that for every integer $3 \le m \le n - 2$, there exists a subset $X$ of $\{1, 2, \dots, n\}$ such that $|X| = m$ and $|N(X)| \neq 1$.



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



## 2013 — 6

**Record:** `kor_2013_cb4e0d`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2013_cb4e0d.json.gz).

Given an one-to-one correspondence $f : \{1, 2, \dots, n\} \to \{1, 2, \dots, n\}$ for some positive integer $n$, define four sets $A$, $B$, $C$, $D$ as follows:
$$
A = \{i \mid i > f(i)\}
$$
$$
B = \{(i, j) \mid i < j \le f(j) < f(i) \text{ or } f(j) < f(i) < i < j\}
$$
$$
C = \{(i, j) \mid i < j \le f(i) < f(j) \text{ or } f(i) < f(j) < i < j\}
$$
$$
D = \{(i, j) \mid i < j \text{ and } f(i) > f(j)\}
$$
Prove that $|A| + 2|B| + |C| = |D|$, where $|X|$ is the number of all elements in $X$.



## 2014 — Problem 6

**Record:** `kor_2014_2f8031`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2014_2f8031.json.gz).

A continent has a finite number of castles and each castle belongs to exactly one of the two countries $A$ and $B$. Each castle has one general. We say two castles are *neighboring* if there is a path between those two castles. We also say that a castle $P$ and a set of castles $Q$ is *neighboring* if $P$ is neighboring some castle in $Q$. Prove that the following two conditions are equivalent.
1. If some of the generals from the country $B$ move to some neighboring castles and attack, generals from the country $A$ can move to some neighboring castles so that at each castle from the country $A$, the number of generals from $A$ is greater than or equal to that of generals from $B$.
2. If $X$ is a set of castles from the country $A$, the number of generals from $A$ who are in $X$ or in castles neighboring $X$ is greater than or equal to the number of generals from $B$ who are in castles neighboring $X$.



## 2014 — Problem 3

**Record:** `kor_2014_ef7b46`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2014_ef7b46.json.gz).

$n$ students with different names are forming a circle and standing toward the center of the circle. Initially $n$ name tags of the students are distributed to them at random. The students repeat the following process:
[process] Every student having one's own name tag gets out of the circle, and the remaining students pass their name tags to the right.
Find the number of initial distributions of name tags such that some students still remain after 4 processes.



## 2016 — Problem 6

**Record:** `kor_2016_12c7ef`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2016_12c7ef.json.gz).

Let $U$ be a set of $m$ triangles. Prove that there exists a subset $W$ of $U$ satisfying the following conditions.

(i) The number of triangles in $W$ is at least $0.45m^{4/5}$.

(ii) There exist no 6 distinct points $A, B, C, D, E$, and $F$ such that $W$ contains 6 triangles $ABC, BCD, CDE, DEF, EFA$, and $FAB$.



## 2016 — Problem 2

**Record:** `kor_2016_3ddc3f`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2016_3ddc3f.json.gz).

Let $n$ and $k$ be integers satisfying $n \ge 2$ and $k \ge \frac{5}{2}n - 1$. Prove that in every choice of $k$ distinct points among all integer points $(x, y)$ with $1 \le x, y \le n$, there exists a circle going through at least four distinct chosen points.



## 2023 — 5

**Record:** `kor_2023_878c28`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2023_878c28.json.gz).

Let $n$ be a positive integer. There are $n$ boxes $B_1, B_2, \dots, B_n$ each of which contains some balls. One can perform the following moves.
Choose positive integers $i$ and $j$ with $1 \le i \le j \le n$, and add exactly one ball to each of the boxes $B_i, B_{i+1}, \dots, B_j$.
For positive integers $x_1, x_2, \dots, x_n$, let $f(x_1, x_2, \dots, x_n)$ be the minimum number of moves required to make the number of balls in each of boxes divisible by $3$, starting from $x_i$ balls in $B_i$ for each $i = 1, 2, \dots, n$. Find the maximum value of $f(x_1, x_2, \dots, x_n)$.
(If $3|x_i$ for $i = 1, 2, \dots, n$, then $f(x_1, x_2, \dots, x_n) = 0$)



## 2024 — Problem 2

**Record:** `kor_2024_10ef8b`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2024_10ef8b.json.gz).

Let $n (\ge 2)$ be a positive integer. Alice distributes $2n$ candies into $4n$ boxes $B_1, B_2, \dots, B_{4n}$. After checking the number of candies Alice puts in each box, Bob chooses $2n$ boxes $B_{k_1}, B_{k_2}, \dots, B_{k_{2n}}$ out of the $4n$ boxes satisfying the following, and then takes all candies in the chosen boxes.
$$
k_i - k_{i-1} \in \{1, 3\} \text{ for each } i = 1, 2, \dots, 2n, \text{ and } k_{2n} = 4n.\ (k_0 = 0)
$$
Alice gets all candies in the $2n$ boxes Bob did not choose. If Alice and Bob use their best strategies to take as many candies as possible, how many candies can Alice take?



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



## 2024 — Problem 6

**Record:** `kor_2024_89b8c1`. **Category:** pipeline supplement. [Source](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2024_89b8c1.json.gz).

Show that there exists a positive integer $K$ satisfying the following: for any prime $p > K$, the number of integers $1 \le a \le p$ such that $a^{p-1} - 1$ is divisible by $p^2$ is less than or equal to $\frac{p}{2^{2024}}$.



# RMM


## 2012 — Problem 5

**Record:** `rmm_2012_704e6f`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2012_704e6f.json.gz).

Given a positive integer number $n \geq 3$, colour each cell of an $n \times n$ square array one of $\left[(n+2)^{2} / 3\right]$ colours, each colour being used at least once. Prove that the cells of some $1 \times 3$ or $3 \times 1$ rectangular subarray have pairwise distinct colours.



## 2012 — Problem 1

**Record:** `rmm_2012_b79110`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2012_b79110.json.gz).

Given a finite group of boys and girls, a covering set of boys is a set of boys such that every girl knows at least one boy in that set; and a covering set of girls is a set of girls such that every boy knows at least one girl in that set. Prove that the number of covering sets of boys and the number of covering sets of girls have the same parity. (Acquaintance is assumed to be mutual.)



## 2013 — Problem 6

**Record:** `rmm_2013_3e4b91`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2013_3e4b91.json.gz).

$2n$ distinct tokens are placed at the vertices of a regular $2n$-gon, with one token placed at each vertex. A move consists of choosing an edge of the $2n$-gon and interchanging the two tokens at the endpoints of that edge. Suppose that after a finite number of moves, every pair of tokens have been interchanged exactly once. Prove that some edge has never been chosen.



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



## 2015 — Problem 6

**Record:** `rmm_2015_4db6ce`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2015_4db6ce.json.gz).

Given a positive integer $n$, determine the largest real number $\mu$ satisfying the following condition: for every $4n$-point configuration $C$ in an open unit square $U$, there exists an open rectangle in $U$, whose sides are parallel to those of $U$, which contains exactly one point of $C$, and has an area greater than or equal to $\mu$.



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



## 2015 — Problem 2

**Record:** `rou_2015_4f438f`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2015_4f438f.json.gz).

Two players play a game on a regular $n$-gon, where $n \ge 4$. Three counters start on consecutive vertices. In turn, each player slides one counter along any number of edges to another vertex of the polygon, without jumping over another counter, to strictly increase the area of the triangle formed by the counters. The loser is the first player who cannot make a legal move. For what $n$ does the first player have a winning strategy?

United Kingdom



## 2015 — Problem 6

**Record:** `rou_2015_eb480f`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2015_eb480f.json.gz).

Given a positive integer $n$, determine the largest real number $\mu$ satisfying the following condition: for every $4n$-point configuration $C$ in an open unit square $U$, there exists an open rectangle in $U$, whose sides are parallel to those of $U$, which contains exactly one point of $C$, and has an area greater than or equal to $\mu$.



## 2016 — Problem 6.

**Record:** `rou_2016_185273`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2016_185273.json.gz).

A set of $n$ points in Euclidean 3-dimensional space, no four of which are coplanar, is partitioned into two subsets $A$ and $B$. An $\mathcal{A}\mathcal{B}$-tree is a configuration of $n-1$ segments, each of which has an endpoint in $A$ and the other in $B$, and such that no segments form a closed polyline. An $\mathcal{A}\mathcal{B}$-tree is transformed into another as follows: choose three distinct segments $A_1B_1$, $B_1A_2$ and $A_2B_2$ in the $\mathcal{A}\mathcal{B}$-tree such that $A_1$ is in $A$ and $A_1B_1 + A_2B_2 > A_1B_2 + A_2B_1$, and remove the segment $A_1B_1$ to replace it by the segment $A_1B_2$. Given any $\mathcal{A}\mathcal{B}$-tree, prove that every sequence of successive transformations comes to an end (no further transformation is possible) after finitely many steps.
Russia



## 2016 — Problem 2.

**Record:** `rou_2016_dce07f`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2016_dce07f.json.gz).

Given positive integers $m$ and $n \ge m$, determine the largest number of dominoes ($1 \times 2$ or $2 \times 1$ rectangles) that can be placed on a rectangular board with $m$ rows and $2n$ columns consisting of unit cells ($1 \times 1$ squares) so that:
1) each domino covers exactly two adjacent cells of the board;
2) no two dominoes overlap;
3) no two form a $2 \times 2$ square;
4) the bottom row of the board is completely covered by $n$ dominoes.



## 2017 — Problem 5

**Record:** `rou_2017_a94581`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2017_a94581.json.gz).

Fix an integer $n \ge 2$. An $n \times n$ sieve is an $n \times n$ array with $n$ cells removed so that exactly one cell is removed from every row and every column. A stick is a $1 \times k$ or $k \times 1$ array for any positive integer $k$. For any sieve $A$, let $m(A)$ be the minimal number of sticks required to partition $A$. Find all possible values of $m(A)$, as $A$ varies over all possible $n \times n$ sieves.

Palmer Mebane, U.S.A., and Nikolai Beluhov, Bulgaria



## 2017 — Problem 3

**Record:** `rou_2017_f8413b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2017_f8413b.json.gz).

Let $n$ be an integer greater than $1$ and let $X$ be an $n$-element set. A non-empty collection of subsets $A_1, \dots, A_k$ of $X$ is *tight* if the union $A_1 \cup \dots \cup A_k$ is a proper subset of $X$ and no element of $X$ lies in exactly one of the $A_i$s. Find the largest cardinality of a collection of proper non-empty subsets of $X$, no non-empty subcollection of which is tight.



## 2018 — 5

**Record:** `rou_2018_53b77e`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2018_53b77e.json.gz).

Let $n$ be a positive integer and fix $2n$ distinct points on a circumference. Split these points into $n$ pairs and join the points in each pair by an arrow (i.e., an oriented line segment). The resulting configuration is good if no two arrows cross, and there are no arrows $\overrightarrow{AB}$ and $\overrightarrow{CD}$ such that $ABCD$ is a convex quadrangle oriented clockwise. Determine the number of good configurations.



## 2018 — 3

**Record:** `rou_2018_a59bad`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2018_a59bad.json.gz).

Ann and Bob play a game on an infinite checkered plane making moves in turn; Ann makes the first move. A move consists in orienting any unit grid-segment that has not been oriented before. If at some stage some oriented segments form an oriented cycle, Bob wins. Does Bob have a strategy that guarantees him to win?



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



## 2019 — Problem 4

**Record:** `rmm_2019_80fa3b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2019_80fa3b.json.gz).

Prove that for every positive integer $n$ there exists a (not necessarily convex) polygon with no three collinear vertices, which admits exactly $n$ different triangulations.
(A triangulation is a dissection of the polygon into triangles by interior diagonals which have no common interior points with each other nor with the sides of the polygon.)



## 2019 — Problem 3

**Record:** `rmm_2019_8e6703`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2019_8e6703.json.gz).

Given any positive real number $\varepsilon$, prove that, for all but finitely many positive integers $v$, any graph on $v$ vertices with at least $(1+\varepsilon) v$ edges has two distinct simple cycles of equal lengths.
(Recall that the notion of a simple cycle does not allow repetition of vertices in a cycle.)



## 2021 — Problem 4

**Record:** `rmm_2021_03b2ae`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2021_03b2ae.json.gz).

Consider an integer $n \geq 2$ and write the numbers $1,2, \ldots, n$ down on a board. A move consists in erasing any two numbers $a$ and $b$, and, for each $c$ in $\{a+b,|a-b|\}$, writing $c$ down on the board, unless $c$ is already there; if $c$ is already on the board, do nothing. For all integers $n \geq 2$, determine whether it is possible to be left with exactly two numbers on the board after a finite number of moves.



## 2021 — Problem 3

**Record:** `rmm_2021_7ba909`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2021_7ba909.json.gz).

A number of 17 workers stand in a row. Every contiguous group of at least 2 workers is a brigade. The chief wants to assign each brigade a leader (which is a member of the brigade) so that each worker's number of assignments is divisible by 4. Prove that the number of such ways to assign the leaders is divisible by 17.



## 2021 — Problem 2

**Record:** `rmm_2021_d11caf`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romanian-master-of-mathematics-rmm/rmm_2021_d11caf.json.gz).

Xenia and Sergey play the following game. Xenia thinks of a positive integer $N$ not exceeding $5000$. Then she fixes $20$ distinct positive integers $a_{1}, a_{2}, \ldots, a_{20}$ such that, for each $k=1,2, \ldots, 20$, the numbers $N$ and $a_{k}$ are congruent modulo $k$. By a move, Sergey tells Xenia a set $S$ of positive integers not exceeding $20$, and she tells him back the set $\{a_{k}: k \in S\}$ without spelling out which number corresponds to which index. How many moves does Sergey need to determine for sure the number Xenia thought of?



## 2023 — 6

**Record:** `rou_2023_0cea08`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2023_0cea08.json.gz).

Let $\Gamma$ be a connected graph on $r + g + b + 1$ vertices. The edges of $\Gamma$ bear three colours: red, green, and blue. It turns out that $\Gamma$ has a spanning tree with exactly $r$ red edges, a spanning tree with exactly $g$ green edges, and a spanning tree with exactly $b$ blue edges. Prove that $\Gamma$ has a spanning tree with exactly $r$ red edges, exactly $g$ green edges, and exactly $b$ blue edges.



## 2023 — 2

**Record:** `rou_2023_9c5b23`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2023_9c5b23.json.gz).

Fix an integer $n \ge 3$. Let $S$ be a set of $n$ points in the plane, no three of which are collinear. Given pairwise distinct points $A, B, C$ in $S$, the triangle $ABC$ is suitable for $AB$ if area $ABC \le$ area $ABX$ for all $X$ in $S$ different from $A$ and $B$. (Note that for a segment $AB$ there could be several suitable triangles.) A triangle is adequate if its vertices are all in $S$ and it is suitable for at least two of its sides. Prove that there are at least $\frac{1}{2}(n-1)$ adequate triangles.
Bulgaria, Alexadar Ivanov



## 2024 — Problem 3.

**Record:** `rou_2024_c3cc94`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2024_c3cc94.json.gz).

Given a positive integer $n$, a set $S$ is *n-admissible* if:
• each element of $S$ is an unordered triple of distinct integers in $\{1, 2, \dots, n\}$,
• $|S| = n-2$, and
• for each $1 \le k \le n-2$ and each choice of $k$ distinct $A_1, A_2, \dots, A_k \in S$,
$$
|A_1 \cup A_2 \cup \dots \cup A_k| \ge k + 2.
$$

Is it true that, for all $n > 3$ and for each $n$-admissible set $S$, there exist pairwise distinct points $P_1, \dots, P_n$ in the plane such that the angles of the triangle $P_iP_jP_k$ are all less than $61^\circ$ for any triple $\{i, j, k\}$ in $S$?



## 2024 — Problem 1.

**Record:** `rou_2024_d65b67`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/romania/rou_2024_d65b67.json.gz).

Let $n$ be a positive integer. Initially, a bishop is placed in each square of the top row of a $2^n \times 2^n$ chessboard; those bishops are numbered from 1 to $2^n$, from left to right. A jump is a simultaneous move made by all bishops such that the following conditions are satisfied:
* each bishop moves diagonally, in a straight line, some number of squares, and
* at the end of the jump, the bishops all stand in different squares of the same row.
Find the total number of permutations $\sigma$ of the numbers 1, 2, \ldots, $2^n$ with the following property: There exists a sequence of jumps such that all bishops end up on the bottom row arranged in the order $\sigma(1), \sigma(2), \ldots, \sigma(2^n)$, from left to right.



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



# USAMO


## 2006 — 3

**Record:** `usa_2006_2edd72`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2006_2edd72.json.gz).

For integral $m$, let $p(m)$ be the greatest prime divisor of $m$. By convention, we set $p(\pm 1) = 1$ and $p(0) = \infty$. Find all polynomials $f$ with integer coefficients such that the sequence $\{p(f(n^2)) - 2n\}_{n \ge 0}$ is bounded above. (In particular, this requires $f(n^2) \ne 0$ for $n \ge 0$.)



## 2006 — 2

**Record:** `usa_2006_9454b3`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2006_9454b3.json.gz).

For a given positive integer $k$ find, in terms of $k$, the minimum value of $N$ for which there is a set of $2k+1$ distinct positive integers that has sum greater than $N$ but every subset of size $k$ has sum at most $N/2$.



## 2006 — 5

**Record:** `usa_2006_ce5644`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2006_ce5644.json.gz).

A mathematical frog jumps along the number line. The frog starts at $1$, and jumps according to the following rule: if the frog is at integer $n$, then it can jump either to $n + 1$ or to $n + 2^{m_n+1}$ where $2^{m_n}$ is the largest power of $2$ that is a factor of $n$. Show that if $k \ge 2$ is a positive integer and $i$ is a nonnegative integer, then the minimum number of jumps needed to reach $2^i k$ is greater than the minimum number of jumps needed to reach $2^i$.



## 2007 — 1

**Record:** `usa_2007_83a6e7`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2007_83a6e7.json.gz).

Let $n$ be a positive integer. Define a sequence by setting $a_1 = n$ and, for each $k > 1$, letting $a_k$ be the unique integer in the range $0 \le a_k \le k - 1$ for which $a_1 + a_2 + \cdots + a_k$ is divisible by $k$. For instance, when $n = 9$ the obtained sequence is $9, 1, 2, 0, 3, 3, 3, \dots$. Prove that for any $n$ the sequence $a_1, a_2, a_3, \dots$ eventually becomes constant.



## 2007 — 3

**Record:** `usa_2007_92862a`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2007_92862a.json.gz).

Let $S$ be a set containing $n^2 + n - 1$ elements, for some positive integer $n$. Suppose that the $n$-element subsets of $S$ are partitioned into two classes. Prove that there are at least $n$ pairwise disjoint sets in the same class.



## 2007 — 3

**Record:** `usa_2007_9951a2`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2007_9951a2.json.gz).

Let $S$ be a set containing $n^2 + n - 1$ elements, for some positive integer $n$. Suppose that the $n$-element subsets of $S$ are partitioned into two classes. Prove that there are at least $n$ pairwise disjoint sets in the same class.



## 2007 — 5

**Record:** `usa_2007_b62228`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2007_b62228.json.gz).

Prove that for every nonnegative integer $n$, the number $7^{7^n} + 1$ is the product of at least $2n+3$ (not necessarily distinct) primes.



## 2008 — 4

**Record:** `usa_2008_2c2856`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2008_2c2856.json.gz).

Let $\mathcal{P}$ be a convex polygon with $n$ sides, $n \ge 3$. Any set of $n-3$ diagonals of $\mathcal{P}$ that do not intersect in the interior of the polygon determine a *triangulation* of $\mathcal{P}$ into $n-2$ triangles. If $\mathcal{P}$ is regular and there is a triangulation of $\mathcal{P}$ consisting of only isosceles triangles, find all the possible values of $n$.



## 2008 — 5

**Record:** `usa_2008_6039a6`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2008_6039a6.json.gz).

Three nonnegative real numbers $r_1$, $r_2$, $r_3$ are written on a blackboard. These numbers have the property that there exist integers $a_1$, $a_2$, $a_3$, not all zero, satisfying $a_1 r_1 + a_2 r_2 + a_3 r_3 = 0$. We are permitted to perform the following operation: find two numbers $x$, $y$ on the blackboard with $x \le y$, then erase $y$ and write $y-x$ in its place. Prove that after a finite number of such operations, we can end up with at least one $0$ on the blackboard.

(This problem was suggested by Kiran Kedlaya.)



## 2008 — 6

**Record:** `usa_2008_8434eb`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2008_8434eb.json.gz).

At a certain mathematical conference, every pair of mathematicians are either friends or strangers. At mealtime, every participant eats in one of two large dining rooms. Each mathematician insists upon eating in a room which contains an even number of his or her friends. Prove that the number of ways that the mathematicians may be split between the two rooms is a power of two (i.e., is of the form $2^k$ for some positive integer $k$).
(This problem was suggested by Sam Vandervelde.)



## 2008 — 3

**Record:** `usa_2008_fddb53`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2008_fddb53.json.gz).

Let $n$ be a positive integer. Denote by $S_n$ the set of points $(x, y)$ with integer coordinates such that
$$
|x| + \left\lfloor y + \frac{1}{2} \right\rfloor < n.
$$
A *path* is a sequence of distinct points $(x_1, y_1), (x_2, y_2), \dots, (x_\ell, y_\ell)$ in $S_n$ such that, for $i = 2, \dots, \ell$, the distance between $(x_i, y_i)$ and $(x_{i-1}, y_{i-1})$ is 1 (in other words, the points $(x_i, y_i)$ and $(x_{i-1}, y_{i-1})$ are neighbors in the lattice of points with integer coordinates).
Prove that the points in $S_n$ cannot be partitioned into fewer than $n$ paths (a partition of $S_n$ into $m$ paths is a set $\mathcal{P}$ of $m$ nonempty paths such that each point in $S_n$ appears in exactly one of the $m$ paths in $\mathcal{P}$).



## 2009 — 2

**Record:** `usa_2009_ddbe0d`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2009_ddbe0d.json.gz).

Let $n$ be a positive integer. Determine the size of the largest subset of $\{-n, -n+1, \dots, n-1, n\}$ which does not contain three elements $a, b, c$ (not necessarily distinct) satisfying $a+b+c=0$.



## 2010 — 2

**Record:** `usa_2010_30bc30`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2010_30bc30.json.gz).

There are $n$ students standing in a circle, one behind the other. The students have heights $h_1 < h_2 < \dots < h_n$. If a student with height $h_k$ is standing directly behind a student with height $h_{k-2}$ or less, the two students are permitted to switch places. Prove that it is not possible to make more than $\binom{n}{3}$ such switches before reaching a position in which no further switches are possible.

(This problem was suggested by Kiran Kedlaya, Travis Schedler, and David Speyer.)



## 2010 — 3

**Record:** `usa_2010_83c87b`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2010_83c87b.json.gz).

The 2010 positive numbers $a_1, a_2, \dots, a_{2010}$ satisfy the inequality $a_i a_j \le i + j$ for all distinct indices $i, j$. Determine, with proof, the largest possible value of the product $a_1 a_2 \cdots a_{2010}$.



## 2010 — 6

**Record:** `usa_2010_94fe39`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2010_94fe39.json.gz).

A blackboard contains 68 pairs of nonzero integers. Suppose that for each positive integer $k$ at most one of the pairs $(k, k)$ and $(-k, -k)$ is written on the blackboard. A student erases some of the 136 integers, subject to the condition that no two erased integers may add to 0. The student then scores one point for each of the 68 pairs in which at least one integer is erased. Determine, with proof, the largest number $N$ of points that the student can guarantee to score regardless of which 68 pairs have been written on the board.
(This problem was suggested by Gerhard Woeginger.)



## 2011 — 6

**Record:** `usa_2011_2951fb`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2011_2951fb.json.gz).

Let $A$ be a set with $|A| = 225$, meaning that $A$ has $225$ elements. Suppose further that there are eleven subsets $A_1, \dots, A_{11}$ of $A$ such that $|A_i| = 45$ for $1 \le i \le 11$ and $|A_i \cap A_j| = 9$ for $1 \le i < j \le 11$. Prove that $|A_1 \cup A_2 \cup \dots \cup A_{11}| \ge 165$, and give an example for which equality holds.



## 2011 — 2

**Record:** `usa_2011_75d863`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2011_75d863.json.gz).

An integer is assigned to each vertex of a regular pentagon so that the sum of the five integers is $2011$. A turn of a solitaire game consists of subtracting an integer $m$ from each of the integers at two neighboring vertices and adding $2m$ to the opposite vertex, which is not adjacent to either of the first two vertices. (The amount $m$ and the vertices chosen can vary from turn to turn.) The game is won at a certain vertex if, after some number of turns, that vertex has the number $2011$ and the other four vertices have the number $0$. Prove that for any choice of the initial integers, there is exactly one vertex at which the game can be won.



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



## 2012 — 2

**Record:** `usa_2012_9b4f1a`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2012_9b4f1a.json.gz).

A circle is divided into $432$ congruent arcs by $432$ points. The points are colored in four colors such that some $108$ points are colored Red, some $108$ points are colored Green, some $108$ points are colored Blue, and the remaining $108$ points are colored Yellow. Prove that one can choose three points of each color in such a way that the four triangles formed by the chosen points of the same color are congruent.



## 2013 — 2.

**Record:** `usa_2013_070dad`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2013_070dad.json.gz).

For a positive integer $n \ge 3$ plot $n$ equally spaced points around a circle. Label one of them $A$, and place a marker at $A$. One may move the marker forward in a clockwise direction to either the next point or the point after that. Hence there are a total of $2n$ distinct moves available; two from each point. Let $a_n$ count the number of ways to advance around the circle exactly twice, beginning and ending at $A$, without repeating a move. Prove that $a_{n-1} + a_n = 2^n$ for all $n \ge 4$.
(This problem was suggested by Sam Vandervelde.)



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



## 2014 — 4.

**Record:** `usa_2014_f6daba`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2014_f6daba.json.gz).

Let $k$ be a positive integer. Two players $A$ and $B$ play a game on an infinite grid of regular hexagons. Initially all the grid cells are empty. Then the players alternately take turns with $A$ moving first. In his move, $A$ may choose two adjacent hexagons in the grid which are empty and place a counter in both of them. In his move, $B$ may choose any counter on the board and remove it. If at any time there are $k$ consecutive grid cells in a line all of which contain a counter, $A$ wins. Find the minimum value of $k$ for which $A$ cannot win in a finite number of moves, or prove that no such minimum value exists.



## 2025 — USAMO 3

**Record:** `usa_2025_a5e142`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_a5e142.json.gz).

Alice the architect and Bob the builder play a game. First, Alice chooses two points $P$ and $Q$ in the plane and a subset $S$ of the plane, which are announced to Bob. Next, Bob marks infinitely many points in the plane, designating each a city. He may not place two cities within distance at most one unit of each other, and no three cities he places may be collinear. Finally, roads are constructed between the cities as follows: for each pair $A, B$ of cities, they are connected with a road along the line segment $AB$ if and only if the following condition holds:
For every city $C$ distinct from $A$ and $B$, there exists $R \in S$ such that $\triangle PQR$ is directly similar to either $\triangle ABC$ or $\triangle BAC$.

Alice wins the game if (i) the resulting roads allow for travel between any pair of cities via a finite sequence of roads and (ii) no two roads cross. Otherwise, Bob wins. Determine, with proof, which player has a winning strategy.



## 2025 — 5

**Record:** `usa_2025_e0957e`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_e0957e.json.gz).

Determine, with proof, all positive integers $k$ such that
$$
\frac{1}{n+1} \sum_{i=0}^{n} \binom{n}{i}^{k}
$$
is an integer for every positive integer $n$.



## 2025 — 6

**Record:** `usa_2025_e518f7`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/united-states/usa_2025_e518f7.json.gz).

Let $m$ and $n$ be positive integers with $m \ge n$. There are $m$ cupcakes of different flavors arranged around a circle and $n$ people who like cupcakes. Each person assigns a nonnegative real number score to each cupcake, depending on how much they like the cupcake. Suppose that for each person $P$, it is possible to partition the circle of $m$ cupcakes into $n$ groups of consecutive cupcakes so that the sum of $P$'s scores of the cupcakes in each group is at least 1. Prove that it is possible to distribute the $m$ cupcakes to the $n$ people so that each person $P$ receives cupcakes of total score at least 1 with respect to $P$.



# VMO


## 2001 — 6

**Record:** `vnm_2001_4665d8`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2001_4665d8.json.gz).

Let be given an integer $n \ge 1$. Consider a permutation $(a_1, a_2, ..., a_{2n})$ of the first $2n$ positive integers such that the numbers $|a_{i+1} - a_i|$ $(i = 1, 2, ..., 2n-1)$ are distinct each from others.
Prove that $a_1 - a_{2n} = n$ if and only if $1 \le a_{2k} \le n$ for every $k = 1, 2, ..., n$.



## 2002 — Problem 3

**Record:** `vnm_2002_ddb25c`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2002_ddb25c.json.gz).

Let be given two positive integers $m$, $n$ with $m < 2001$, $n < 2002$; and let be given $2001 \times 2002$ distinct real numbers. Put these numbers into the little squares of a rectangular board of size $2001 \times 2002$ (the board consists of $2001$ rows and $2002$ columns) so that each number is putting in a little square and each little square is filling with a number. We call a little square "bad" if the number put in it is less than at least $m$ numbers put in the same column as the considered little square and simultaneously this number is less than at least $n$ numbers put in the same row as the considered little square. For each such filling, let $s$ be the number of "bad" little squares. Find the least value of $s$.



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



## 2005 — Problem 3.

**Record:** `vnm_2005_05160d`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2005_05160d.json.gz).

In plane, let be given an octagon $A_1A_2A_3A_4A_5A_6A_7A_8$ such that no three of its diagonals are concurrent. Each point of intersection of every two diagonals of the octagon is called a cross.
Consider the convex quadrilaterals whose vertices are vertices of the given octagon. Each such quadrilateral is called a subquadrilateral.
Find the least positive integer $n$ such that one can colour $n$ crosses so that for every $i, k \in \{1, 2, 3, 4, 5, 6, 7, 8\}$ and $i \ne k$, if we denote by $s(i, k)$ the number of

subquadrilaterals admitting $A_i, A_k$ as vertices and admitting a coloured cross as the point of intersection of the diagonals then the values $s(i, k)$ are all equal.



## 2006 — Problem 6

**Record:** `vnm_2006_fbb149`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2006_fbb149.json.gz).

Consider a set $S$ of 2006 distinct numbers. A subset $T$ of $S$ is called stubborn if for every $u, v$ (not necessarily distinct) in $T$, the number $u + v$ does not belong to $T$. Prove that

i) if $S$ is the set of 2006 first positive integers, then the number of elements of every stubborn subset $T$ of $S$ does not exceed 1003,

ii) if $S$ consists of 2006 arbitrary positive integers then there exists a stubborn subset $T$ of $S$ having 669 elements.



## 2007 — 4

**Record:** `vnm_2007_eb910e`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2007_eb910e.json.gz).

Given a regular 2007-polygon. Find the smallest positive integer $k$ satisfying the following property: In every set of $k$ vertices there are 4 vertices which form a quadrilateral with 3 edges of the given 2007-polygon.



## 2008 — 5

**Record:** `vnm_2008_0c937e`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2008_0c937e.json.gz).

Let $n > 3$ be a positive integer and let $T$ denote the set of the first $n$ positive integers. A subset $S$ of $T$ is called a *scattered set* if $S$ has the following property: There exists a positive integer $c$, not exceeding $\frac{n}{2}$ such that $|s_1 - s_2| \neq c$ for any two numbers $s_1, s_2$ in $S$. What is the maximum number of elements of a scattered set?



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



## 2009 — Problem 5

**Record:** `vnm_2009_bd6666`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2009_bd6666.json.gz).

Given a positive integer $n$. Denote by $T$ the set of the first $2n$ positive integers. Find the number of subsets $S$ of $T$ with the property: in $S$ there do not exist numbers $a, b$ with $|a-b| \in \{1; n\}$.
(Note: The empty set is considered as satisfying the above property).



## 2010 — 5

**Record:** `vnm_2010_2bc522`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2010_2bc522.json.gz).

Given a positive integer $n$. Given a square table of sizes $3 \times 3$. One uses $n$ colors to paint the squares of the table in such a way, that each square is painted by one color. Two ways of painting is considered to be similar if they can be obtained from each other by rotating the table around its center. How many non-similar ways of painting are there?



## 2010 — 4

**Record:** `vnm_2010_8c54a3`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2010_8c54a3.json.gz).

Prove that for every positive integer $n$ the equation
$$
x^2 + 15y^2 = 4^n
$$
has at least $n$ non-negative integer solutions $(x, y)$.



## 2011 — 4

**Record:** `vnm_2011_accee2`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2011_accee2.json.gz).

Given a convex pentagon $ABCDE$, of which the length of each edge and of the diagonals $AC$, $AD$ does not exceed $\sqrt{3}$. Choose 2001 arbitrary distinct points in the interior of that pentagon. Show that there exists a unit disk with center lying on the edges of the pentagon, which contains at least 403 of the chosen points.



## 2012 — Problem 4.

**Record:** `vnm_2012_3fa159`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_3fa159.json.gz).

A sequence of $n$ real numbers ($n \ge 2$) is called *nearly increasing* if it contains an increasing subsequence of $n-1$ terms. How many nearly increasing sequences are there in the set of all permutations of $\{1,2,3,...,n\}$?



## 2012 — 1

**Record:** `vnm_2012_626786`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_626786.json.gz).

Given a sequence of real numbers $(x_n)$
$$
x_1 = 3 \quad \text{and} \quad x_n = \frac{n+2}{3n}(x_{n-1} + 2), \quad \forall n \ge 2.
$$
Prove that the sequence has a finite limit as $n \to \infty$ and calculate this limit.



## 2012 — Problem 6.

**Record:** `vnm_2012_736692`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_736692.json.gz).

Let $A$ be the set of positive integers that can be written in the form $2x^2 + 3y^2$ where $x, y$ are integers with $x^2 + y^2 \neq 0$. Prove that:

a) All numbers from $A$ are not perfect square.

b) The product of an odd number of numbers from $A$ is not a perfect square.



## 2012 — 5

**Record:** `vnm_2012_db0487`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_db0487.json.gz).

Calculate the number of the arrangements of 5 girls $G_1$, $G_2$, $G_3$, $G_4$ and $G_5$ and 12 boys in a row satisfying the following conditions:
1. The order of the girls from left to right is $G_1$, $G_2$, $G_3$, $G_4$ and $G_5$.
2. There are at least 3 boys between $G_1$ and $G_2$.
3. There are at least 1 boy and at most 4 boys between $G_4$ and $G_5$.



## 2012 — Problem 4.

**Record:** `vnm_2012_de8d74`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_de8d74.json.gz).

Let $M, N$ be two positive integers. We put a light on each unit square of the table $N \times N$ (each light is either on or off). Initially, all the lights are off. In each step, we choose either a column or a row and switch $M$ consecutive lights on the chosen column/row. Find the necessary and sufficient condition of $M, N$ such that we can switch on all the lights after finite steps.



## 2012 — Problem 7.

**Record:** `vnm_2012_e6adf8`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_e6adf8.json.gz).

Let $n$ be a positive integer. Given $2n$ positive real numbers $a_1, a_2, a_3, \dots, a_n$ and $b_1, b_2, b_3, \dots, b_n$ satisfying the following condition:
$$
a_1 > a_2 > a_3 > \dots > a_n \text{ and } b_1 > b_2 > b_3 > \dots > b_n.
$$
A partition of these $2n$ numbers into $n$ disjoint pairs $(a_i, b_j), 1 \le i \le n, 1 \le j \le n$ is called *regular* if the difference between two numbers of each pair is less than $2013$.

a. Suppose that there exists a regular partition for these numbers. Show that the partition $(a_1, b_1), (a_2, b_2), \dots, (a_n, b_n)$ is also regular.

b. Suppose that there exists a regular partition in which $i \neq j$ for each pair $(a_i, b_j)$.
Compute the least number of regular partitions in this case.



## 2012 — 4

**Record:** `vnm_2012_ed74b6`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2012_ed74b6.json.gz).

Given a positive integer $n$. There are $n$ boys and $n$ girls standing in a line. Give each person $X$ in the line a number of sweets which is exactly equal to the number of the pair $(a, b)$ such that $a$ and $b$ are of opposite sex of $X$ and $X$ is standing between $a$ and $b$. Prove that the total number of sweets of $n$ boys and $n$ girls does not exceed $\frac{1}{3}n(n^2 - 1)$.



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

**Record:** `vnm_2013_4017e2`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2013_4017e2.json.gz).

Let be given an alphabet consisting of $29$ characters. A sequence of characters is called word. For each positive integer $n$, let $X_n$ be the set all words with $n$ characters. Consider function $f: X_n \to X_2$ defined as follow: for each word from $X_n$, we erase any $n-2$ characters in this word to get a word from $X_2$. For each such function, let $V(f)$ be the set of all values of $f$. Find the minimal value of $|V(f)|$ in following cases:

a) $n=3$.

b) $n = 4$.



## 2013 — Problem 3.

**Record:** `vnm_2013_6fb2bd`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2013_6fb2bd.json.gz).

For each positive integer $n$, let $S_n = \{0,1,2,\ldots,2n+1\}$. Consider the function $f : (\mathbb{Z} \times S_n) \to [0;1]$ satisfying the following conditions:

i/ $f(x,0) = f(x,2n+1) = 0$ for all $x$ from integers.

ii/ $f(x-1,y)+f(x+1,y)+f(x,y-1)+f(x,y+1)=1$ for all $x,y \in \mathbb{Z}$ and $1 \le y \le 2n$.

Let $F$ be the set of all such functions.

1. Prove that $|F|$ is infinite.
2. For each function $f \in F$, let $v_f$ be the image set of $f$. Prove that $|v_f|$ is finite.
3. Find the maximum value of $|v_f|$ where $f \in F$.



## 2013 — 4

**Record:** `vnm_2013_8efd6e`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2013_8efd6e.json.gz).

Several natural numbers are given on a line. We perform a transformation as follows: for every pair of consecutive integers on the line, write the sum of those two numbers in the middle of them. After 2013 such steps, how many times number 2013 are there on the line if

a) The given numbers are $1$ and $1000$?

b) The given numbers are $1, 2, 3, \ldots, 1000$ on the increasing order from the left to the right?



## 2013 — Problem 5.

**Record:** `vnm_2013_986218`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2013_986218.json.gz).

The teacher has $2013$ candies of $11$ different types. She distributes the candies to her students such that no student obtains more than one candy of each type. She then asks each pair of students to write down on the board the number of candy types that they have in common. Let $M$ be the sum of written numbers.

a)
Find the minimum value of $M$.

b)
What happens if the teacher has only $9$ different types of candy?



## 2013 — Problem 3.

**Record:** `vnm_2013_a73731`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2013_a73731.json.gz).

Let be given a square $ABCD$ and $2009$ points inside the square such that no three points from these $2013$ points are collinear (including $4$ points $A$, $B$, $C$, $D$). We connect some points inside the square (as well as the vertices $A$, $B$, $C$, $D$) to partite the square into triangles. Each connecting segment is called edge. A path from the point to another point through edges is called a track-way.

Consider a partition of $2013$ above mentioned points into two sets $X$ and $Y$ such that $A, C \in X$ and $B, D \in Y$. Prove that: either there exists a track-way from $A$ to $C$ with all vertices only in $X$ or there exist a track-way from $B$ to $D$ with all vertices only in $Y$.



## 2013 — Problem 6.

**Record:** `vnm_2013_c284da`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2013_c284da.json.gz).

Given a $10 \times 10 \times 10$ box of $1000$ unit white cubes. An and Binh play a game with this box. An selects some bands of size $1 \times 1 \times 10$ such that any two chosen bands have no common points and then changes all cells on these bands to black. Binh then selects some unit cubes and asks An what color of these cells. What is the least number of cells Binh must choose in order to determine all black cells based on An's answer?



## 2013 — Problem 4.

**Record:** `vnm_2013_f344b9`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2013_f344b9.json.gz).

The diagonals of a convex pentagon cut together divide the pentagon into one small pentagon and 10 sub-triangles. Find the maximum number of triangles among these sub-triangles such that they have the same area.



## 2014 — 3

**Record:** `vnm_2014_a32c74`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2014_a32c74.json.gz).

Given a regular 103-sided polygon with 79 vertices are colored red and the remaining vertices are colored blue. Denote $A$ to be the number of pairs of adjacent red vertices and $B$ to be the number of pairs of adjacent blue vertices.

a) Find all possible values of $(A, B)$.

b) Determine the number of pairwise non-similar colorings of the polygon satisfying $B = 14$. Note that two ways of colorings are considered similar if one of them can be obtained from another with a rotation at the circumcircle of the polygon.



## 2014 — 7

**Record:** `vnm_2014_aef204`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2014_aef204.json.gz).

Find all sets of 2014 rational numbers not necessarily distinct such that: If an arbitrary number in the set is removed, one always can divide the remaining 2013 numbers into three sets such that each set has exactly 671 elements and the products of all elements in each set are equal.



## 2015 — 7

**Record:** `vnm_2015_5ce2b3`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2015_5ce2b3.json.gz).

There are $m$ girls and $n$ boys participating in a duet singing contest ($m, n \ge 2$). At the contest, there will be one show in each section. Each show includes some boy-girl duets where each boy-girl couple will sing no more than one song and each participant will sing at least one song. Two shows are considered different if there exists a boy-girl couple sings in exactly one of these two shows. The contest will end if and only if every possible shows are performed, and each show is performed exactly once.

a) A show is called depend on a participant $X$ if when we cancel all duets that $X$ performs, then there will be at least one participant is not allowed to sing any song in that show. Prove that among every show that depends on $X$, the number of shows with odd number of songs equal to the number of shows with even number of songs.

b) Prove that the organizers can arrange the shows such that the number of songs in two consecutive shows have different parities.



## 2015 — 7

**Record:** `vnm_2015_7ffead`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2015_7ffead.json.gz).

There are $m$ boys and $n$ girls took part in a festival of singing couples. Each day, there are couples sang songs in a presentation. Each couple had a boy and a girl. In a presentation, every one sang at least one song, and a boy sang a duet with a girl not more than one time. Two presentations were different if there was at least one couple sang in exactly one of these two presentations. The festival ended when every possible presentation taken and each presentation taken exactly one time.

a) A presentation was dependent on $X$ if in the case $X$ was excluded together with the songs he/she sang then there was also another child that did not sing any song. Prove that, the number of presentations depending on $X$ and has odd number of songs is equal to the number of presentations depending on $X$ and has even number of songs.

b) Prove that we can arrange all presentations in a sequence of days so that two consecutive presentations' song numbers have different parities.



## 2015 — 3

**Record:** `vnm_2015_ef4208`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2015_ef4208.json.gz).

Given a positive integer $k$. Find the number of non-negative integers that do not exceed $10^k$ and satisfy the following conditions

i) $n$ is divisible by $3$,
ii) The digits of $n$ in decimal representation are in the set $\{2, 0, 1, 5\}$.



## 2016 — 4

**Record:** `vnm_2016_c11c43`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2016_c11c43.json.gz).

A person wants to plant two different kinds of tree on a plot tabular grid size $m \times n$ (each square planted one tree). A planting way is called impressive if two following conditions are satisfied

i) The number of trees in each kind is equal.

ii) The difference between the number of two kinds of tree in each column and each row is at least $\frac{m}{2}$ and $\frac{n}{2}$ respectively.

a) Find an impressive planting way when $m = n = 2016$.

b) Prove that if there exists an impressive planting way then $m, n$ is divisible by 4.



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



## 2018 — 5

**Record:** `vnm_2018_dcf812`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2018_dcf812.json.gz).

For two positive integers $n$ and $d$, let $S_n(d)$ be the set of all ordered $d$-tuples $(x_1, x_2, \dots, x_d)$ that satisfy all the following conditions:

i) $x_i \in \{1, 2, \dots, n\}$ for every $i \in \{1, 2, \dots, d\}$;
ii) $x_i \neq x_{i+1}$ for every $i \in \{1, 2, \dots, d-1\}$;
iii) There do not exist indices $1 \le i < j < k < l \le d$ such that $x_i = x_k$ and $x_j = x_l$.

a) Compute $|S_3(5)|$.

b) Prove that $|S_n(d)| > 0$ if and only if $d \le 2n-1$.



## 2019 — 7

**Record:** `vnm_2019_e93538`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2019_e93538.json.gz).

There are several identical caro papers of size $5 \times 5$. Someone uses $n$ colors to fill in each paper such that two cells at the same position on two sides share the same color. Two papers are considered congruent if they can be stacked together in such a way that the pairs of squares at the same position have the same color. Prove that, by the definition of congruence, one can obtain at most
$$
\frac{1}{8}(n^{25} + 4n^{15} + n^{13} + 2n^{7})
$$
distinct colored caro papers.



## 2020 — 7

**Record:** `vnm_2020_1719a9`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2020_1719a9.json.gz).

Given a positive integer $n > 1$. Let $T$ be the set of all ordered triples $(x, y, z)$ where $x, y$ and $z$ are different positive integers and $1 \le x, y, z \le 2n$. A set $A$ containing ordered pairs $(u, v)$ is called 'connected' to $T$ if for all $(x, y, z) \in T$ then
$$
\{(x, y), (x, z), (y, z)\} \cap A \neq \emptyset.
$$
a) Find the number of elements of set $T$.
b) Prove that there exists a set connected to $T$ that has exactly $2n(n-1)$ elements.
c) Prove that every set that connected to $T$ has at least $2n(n-1)$ elements.



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



## 2022 — Problem 6

**Record:** `vnm_2022_a59d06`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2022_a59d06.json.gz).

There are 4 identical fair dices. Denote $x_i$ ($1 \leq x_i \leq 6$) be the number of dots on a face appearing on the $i$-th dice $1 \leq i \leq 4$.
a) Find the number of possible tuples $(x_1, x_2, x_3, x_4)$.
b) Find the probability that there exists a number $x_j$ such that $x_j$ is equal to the sum of the remaining numbers.
c) Find the probability that we can divide $x_1, x_2, x_3, x_4$ into 2 groups that have the same sum.



## 2023 — 6

**Record:** `vnm_2023_423ad5`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2023_423ad5.json.gz).

There are $n \ge 2$ classes organized $m \ge 1$ learning groups for students. Every class has students participating in at least one group. Every group has exactly $a$ classes that the students in this group participate in. For any two groups, there are no more than $b$ classes with students participating in both groups simultaneously.

a) Find $m$ when $n = 8, a = 4, b = 1$.

b) Prove that $n \ge 20$ when $m = 6, a = 10, b = 4$.

c) Find the minimum value of $n$ when $m = 20, a = 4, b = 1$.



## 2024 — 7

**Record:** `vnm_2024_9e7ac6`. **Category:** contest. [Source](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2024_9e7ac6.json.gz).

In the space, there is a convex polyhedron $D$ such that for every vertex of $D$, there are an even number of edges passing through that vertex. We choose a face $F$ of $D$. Then we assign each edge of $D$ a positive integer such that for all faces of $D$ different from $F$, the sum of the numbers assigned on the edges of that face is a positive integer divisible by 2024. Prove that the sum of the numbers assigned on the edges of $F$ is also a positive integer divisible by 2024.



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


