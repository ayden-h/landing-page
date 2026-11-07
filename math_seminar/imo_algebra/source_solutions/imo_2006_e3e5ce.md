# imo_2006_e3e5ce

IMO-SL | IMO | 2006 | Algebra | A1

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2006_e3e5ce](https://mathnet.mit.edu/data_v2/full/imo/imo_2006_e3e5ce.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: Shortlisted Problems with Solutions
- Year: 2006
- Editors: Bauer, Andrej; Geretschläger, Robert; Kós, Géza; Kuczma, Marcin; Savchev, Svetoslav
- Organization: International Mathematical Olympiad
- Place: Slovenia
- Series: International Mathematical Olympiad
- Volume: 47
- Language: English

**Known source issue:** The negative two-cycle partner is -1-a, not 1-a. Corrected in A03.

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

Checked rewritten solution: [A03](../reviewed_solutions/A03.md).

## Supplied solution 1

First note that if $a_{0} \geq 0$, then all $a_{i} \geq 0$. For $a_{i} \geq 1$ we have (in view of $\left\langle a_{i}\right\rangle<1$ and $\left\lfloor a_{i}\right\rfloor>0$ )
$$
\left\lfloor a_{i+1}\right\rfloor \leq a_{i+1}=\left\lfloor a_{i}\right\rfloor \cdot\left\langle a_{i}\right\rangle<\left\lfloor a_{i}\right\rfloor
$$
the sequence $\left\lfloor a_{i}\right\rfloor$ is strictly decreasing as long as its terms are in $[1, \infty)$. Eventually there appears a number from the interval $[0,1)$ and all subsequent terms are $0$.

Now pass to the more interesting situation where $a_{0}<0$; then all $a_{i} \leq 0$. Suppose the sequence never hits $0$. Then we have $\left\lfloor a_{i}\right\rfloor \leq -1$ for all $i$, and so
$$
1+\left\lfloor a_{i+1}\right\rfloor>a_{i+1}=\left\lfloor a_{i}\right\rfloor \cdot\left\langle a_{i}\right\rangle>\left\lfloor a_{i}\right\rfloor
$$
this means that the sequence $\left\lfloor a_{i}\right\rfloor$ is nondecreasing. And since all its terms are integers from $(-\infty,-1]$, this sequence must be constant from some term on:
$$
\left\lfloor a_{i}\right\rfloor=c \quad \text{ for } \quad i \geq i_{0} ; \quad c \text{ a negative integer. }
$$
The defining formula becomes
$$
a_{i+1}=c \cdot\left\langle a_{i}\right\rangle=c\left(a_{i}-c\right)=c a_{i}-c^{2}
$$
Consider the sequence
$$
\begin{equation*}
b_{i}=a_{i}-\frac{c^{2}}{c-1} \tag{1}
\end{equation*}
$$
It satisfies the recursion rule
$$
b_{i+1}=a_{i+1}-\frac{c^{2}}{c-1}=c a_{i}-c^{2}-\frac{c^{2}}{c-1}=c b_{i}
$$
implying
$$
\begin{equation*}
b_{i}=c^{i-i_{0}} b_{i_{0}} \quad \text{ for } \quad i \geq i_{0} \tag{2}
\end{equation*}
$$
Since all the numbers $a_{i}$ (for $i \geq i_{0}$ ) lie in $[c, c+1)$, the sequence $\left(b_{i}\right)$ is bounded. The equation (2) can be satisfied only if either $b_{i_{0}}=0$ or $|c|=1$, i.e., $c=-1$.

In the first case, $b_{i}=0$ for all $i \geq i_{0}$, so that
$$
a_{i}=\frac{c^{2}}{c-1} \quad \text{ for } \quad i \geq i_{0} .
$$
In the second case, $c=-1$, equations (1) and (2) say that
$$
a_{i}=-\frac{1}{2}+(-1)^{i-i_{0}} b_{i_{0}}= \begin{cases}a_{i_{0}} & \text{ for } i=i_{0}, i_{0}+2, i_{0}+4, \ldots, \\ 1-a_{i_{0}} & \text{ for } i=i_{0}+1, i_{0}+3, i_{0}+5, \ldots .\end{cases}
$$
Summarising, we see that (from some point on) the sequence $\left(a_{i}\right)$ either is constant or takes alternately two values from the interval $(-1,0)$. The result follows.
