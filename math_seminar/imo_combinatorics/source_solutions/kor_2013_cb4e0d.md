# kor_2013_cb4e0d

KMO | South Korea | 2013 | The Second Day, March 24, 2013 | 6

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [kor_2013_cb4e0d](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2013_cb4e0d.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: South Korea
- Title: KOREAN MATHEMATICAL OLYMPIAD
- Subtitle: 26th Korean Mathematical Olympiad Final Round
- Year: 2013
- Organization: THE KOREAN MATHEMATICAL SOCIETY
- Publisher: THE KOREAN MATHEMATICAL SOCIETY
- Place: Seoul, Korea

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

We use an induction by the number $|D|$: Firstly, if $|D| = 0$, $f$ is identity and $A = B = C = \emptyset$. So it holds for $|D| = 0$.

Next, assume that it holds that for all bijections with $|D| < k$ for some positive integer $k$. Given $f$ with $|D_f| = k > 0$, there exists $i$ such that $f(i) > f(i+1)$. Define the function $g$ by
$$
g(j) = \begin{cases} f(i+1), & \text{if } j = i, \\ f(i), & \text{if } j = i+1, \\ f(j), & \text{otherwise.} \end{cases}
$$
We are able to define four set $(A_g, B_g, C_g, D_g)$ by the function $g$. Since $|D_g| = |D| - 1 = k - 1 < k$, by the induction hypothesis, we have
$$
|A_g| + 2|B_g| + |C_g| = |D_g|. \tag{5}
$$
Now, we divide five cases:

i. If $f(i+1) > i$ and $f(i) > i+1$, then we have
$$
(|A_f|, |B_f|, |C_f|, |D_f|) = (|A_g|, |B_g| + 1, |C_g| - 1, |D_g| + 1).
$$
ii. If $f(i+1) = i$ and $f(i) > i$, then the property
$$
|\{j \mid j < i \text{ and } i + 1 < f(j)\}| = |\{j \mid f(j) < i \text{ and } i + 1 < j\}|
$$
yields
$$
(|A_f|, |B_f|, |C_f|, |D_f|) = (|A_g| + 1, |B_g|, |C_g|, |D_g| + 1).
$$
iii. If $f(i+1) < i$ and $f(i) > i$, then we have
$$
(|A_f|, |B_f|, |C_f|, |D_f|) = (|A_g|, |B_g|, |C_g| + 1, |D_g| + 1)
$$
in the both of all cases $f^{-1}(i) < i$ and $f^{-1}(i) > i$.
iv. If $f(i+1) < i$ and $f(i) = i$, then the property
$$
|\{j \mid j < i \text{ and } i + 1 < f(j)\}| = |\{j \mid f(j) < i \text{ and } i + 1 < j\}| + 1
$$
yields
$$
(|A_f|, |B_f|, |C_f|, |D_f|) = (|A_g| - 1, |B_g| + 1, |C_g|, |D_g| + 1).
$$
v. If $f(i+1) < i$ and $f(i) < i$, then we have
$$
(|A_f|, |B_f|, |C_f|, |D_f|) = (|A_g|, |B_g| + 1, |C_g| - 1, |D_g| + 1).
$$
Due to (5), the results above all cases complete the proof. □

