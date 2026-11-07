# vnm_2001_ec1af2

VMO | Vietnam | 2001 | First Day | 3

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [vnm_2001_ec1af2](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2001_ec1af2.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Vietnam
- Title: Vietnamese Mathematical Olympiad 2001
- Year: 2001
- Organization: MINISTRY OF EDUCATION AND TRAINING OF VIETNAM
- Place: Hanoi

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

1).
+ For $a = k\pi$ ($k \in \mathbb{Z}$), we have $x_n = k\pi \quad \forall n \in \mathbb{N}$, therefore $\lim_{n \to \infty} x_n = k\pi$.

+ For $a \neq k\pi$ ($k \in \mathbb{Z}$), consider the function $f(x) = x + \sin x$ defined on $\mathbb{R}$. We have $f'(x) = 1 + \cos x \ge 0 \quad \forall x \in \mathbb{R}$. It follows that:

i) If $a \in (2k\pi; (2k+1)\pi)$ the sequence $\{x_n\}$ is increasing and bounded above by $(2k+1)\pi$, and it is easy to see that $\lim_{n \to \infty} x_n = (2k+1)\pi$.

ii) If $a \in ((2k-1)\pi; 2k\pi)$ the sequence $\{x_n\}$ is decreasing and bounded below by $(2k-1)\pi$, and it is easy to see that $\lim_{n \to \infty} x_n = (2k-1)\pi$.

Thus, for every $a \in \mathbb{R}$, the sequence $\{x_n\}$ corresponding to $(a, 1)$ is convergent and $\lim_{n \to \infty} x_n = (2[a/2\pi]+\operatorname{sign}({a/2\pi}))\pi$.

2).
For $b > 2$, it is easy to show that there exists $a_0 \in (0; \pi)$ such that $2a_0 = b \cdot \sin a_0$ and the sequence $\{x_n\}$ corresponding to $(a = \pi - a_0, b)$ is a periodic sequence of period 2.
