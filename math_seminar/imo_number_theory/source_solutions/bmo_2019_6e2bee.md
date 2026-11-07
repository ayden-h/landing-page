# bmo_2019_6e2bee

BMO-SL | Balkan Mathematical Olympiad | 2019 | ALGEBRA | A1

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2019_6e2bee](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2019_6e2bee.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Balkan Mathematical Olympiad
- Title: 36th BALKAN MATHEMATICAL OLYMPIAD
- Subtitle: SHORTLIST OF SELECTED PROBLEMS
- Year: 2019
- Editors: Baltag, Valeriu; Costaș, Ana; Croitoru, Dorian; Guțu, Valeriu; Izbaş, Vladimir; Rusu, Galina; Sîrbu, Parascovia
- Organization: Balkan Mathematical Olympiad
- Publisher: Organizing Committee of BMO 2019
- Place: Chisinau, Republic of Moldova
- Series: Balkan Mathematical Olympiad
- Volume: 36
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Define $b_n = \frac{a_0+a_1+\dots+a_n}{n}$ for every positive integer $n$. According to condition, $b_n$ is a positive integer for every positive integer $n$.
Since $a_{n+1}$ is the smallest positive integer such that $\frac{a_0+a_1+\dots+a_n}{n+1}$ is a positive integer and
$$
\frac{a_0 + a_1 + \dots + a_n + b_n}{n+1} = \frac{a_0 + a_1 + \dots + a_n + \frac{a_0+a_1+\dots+a_n}{n}}{n+1} = \frac{a_0 + a_1 + \dots + a_n}{n} = b_n,
$$
which is a positive integer, we get $a_{n+1} \le b_n$ for every positive integer $n$.
Now from last result we have
$$
b_{n+1} = \frac{a_0 + a_1 + \dots + a_n + a_{n+1}}{n+1} \le \frac{a_0 + a_1 + \dots + a_n + b_n}{n+1} = b_n.
$$
Hence the infinite sequence of positive integers $b_1, b_2, \dots$ is non-increasing. So there exists a positive integer $T$ such that for all $n \ge T$ we have
$$
\begin{align*} b_{n+1} &= b_n \Rightarrow \frac{a_0 + a_1 + \dots + a_n + a_{n+1}}{n+1} = \frac{a_0 + a_1 + \dots + a_n}{n} &\Rightarrow \\ n(a_0 + a_1 + \dots + a_n + a_{n+1}) &= (n+1)(a_0 + a_1 + \dots + a_n) &\Rightarrow \\ na_{n+1} &= a_0 + a_1 + \dots + a_n &\Rightarrow a_{n+1} = \frac{a_0 + a_1 + \dots + a_n}{n} = b_n. \end{align*}
$$
Similarly we get $a_{n+2} = b_{n+1}$, which follows that $a_{n+2} = b_{n+1} = b_n = a_{n+1}$. Hence, taking $M = T+1$, we can state that $a_{n+1} = a_n$ for every $n \ge M$.
$\Box$
