# imo_2019_cd6d5a

IMO-SL | IMO | 2019 | Algebra | A2

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2019_cd6d5a](https://mathnet.mit.edu/data_v2/full/imo/imo_2019_cd6d5a.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: Shortlisted Problems
- Subtitle: with solutions
- Year: 2019
- Editors: Gardiner, Tony; Crane, Edward; Betts, Alexander; Cranch, James; Myers, Joseph; Aaronson, James; Carlotti, Andrew; Kós, Géza; Bogdanov, Ilya I.; Shotton, Jack
- Organization: 60th International Mathematical Olympiad
- Place: Bath, United Kingdom
- Series: International Mathematical Olympiad
- Volume: 60th
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

Checked rewritten solution: [A08](../reviewed_solutions/A08.md).

## Supplied solution 1

Let $P=\left\{i: u_{i}>0\right\}$ and $N=\left\{i: u_{i} \leqslant 0\right\}$ be the indices of positive and nonpositive elements in the sequence, and let $p=|P|$ and $n=|N|$ be the sizes of these sets; then $p+n=2019$. By the condition $\sum_{i=1}^{2019} u_{i}=0$ we have $0=\sum_{i=1}^{2019} u_{i}=\sum_{i \in P} u_{i}-\sum_{i \in N}|u_{i}|$, so
$$
\begin{equation*}
\sum_{i \in P} u_{i}=\sum_{i \in N}|u_{i}| . \tag{1}
\end{equation*}
$$
After this preparation, estimate the sum of squares of the positive and nonpositive elements as follows:
$$
\begin{align*}
& \sum_{i \in P} u_{i}^{2} \leqslant \sum_{i \in P} b u_{i}=b \sum_{i \in P} u_{i}=b \sum_{i \in N}|u_{i}| \leqslant b \sum_{i \in N}|a|=-n a b ;  \tag{2}\\
& \sum_{i \in N} u_{i}^{2} \leqslant \sum_{i \in N}|a| \cdot|u_{i}|=|a| \sum_{i \in N}|u_{i}|=|a| \sum_{i \in P} u_{i} \leqslant|a| \sum_{i \in P} b=-p a b . \tag{3}
\end{align*}
$$
The sum of these estimates is
$$
1=\sum_{i=1}^{2019} u_{i}^{2}=\sum_{i \in P} u_{i}^{2}+\sum_{i \in N} u_{i}^{2} \leqslant-(p+n) a b=-2019 a b ;
$$
that proves $a b \leqslant \frac{-1}{2019}$.

## Supplied solution 2

As in the previous solution we conclude that $a<0$ and $b>0$.
For every index $i$, the number $u_{i}$ is a convex combination of $a$ and $b$, so
$$
u_{i}=x_{i} a+y_{i} b \quad \text{with some weights} \ 0 \leqslant x_{i}, y_{i} \leqslant 1, \text{with} \ x_{i}+y_{i}=1 .$$
Let $X=\sum_{i=1}^{2019} x_{i}$ and $Y=\sum_{i=1}^{2019} y_{i}$. From $0=\sum_{i=1}^{2019} u_{i}=\sum_{i=1}^{2019}\left(x_{i} a+y_{i} b\right)=-|a| X+b Y$, we get
$$
\begin{equation*}
|a| X=b Y . \tag{4}
\end{equation*}
$$
From $\sum_{i=1}^{2019}\left(x_{i}+y_{i}\right)=2019$ we have
$$
\begin{equation*}
X+Y=2019 \tag{5}
\end{equation*}
$$
The system of linear equations $(4,5)$ has a unique solution:
$$
X=\frac{2019 b}{|a|+b}, \quad Y=\frac{2019|a|}{|a|+b}
$$
Now apply the following estimate to every $u_{i}^{2}$ in their sum:
$$
u_{i}^{2}=x_{i}^{2} a^{2}+2 x_{i} y_{i} a b+y_{i}^{2} b^{2} \leqslant x_{i} a^{2}+y_{i} b^{2}$$
we obtain that
$$
1=\sum_{i=1}^{2019} u_{i}^{2} \leqslant \sum_{i=1}^{2019}\left(x_{i} a^{2}+y_{i} b^{2}\right)=X a^{2}+Y b^{2}=\frac{2019 b}{|a|+b}|a|^{2}+\frac{2019|a|}{|a|+b} b^{2}=2019|a| b=-2019 a b
$$
Hence, $a b \leqslant \frac{-1}{2019}$.
