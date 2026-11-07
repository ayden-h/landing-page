# bmo_2012_f7e2ed

BMO-SL | Balkan Mathematical Olympiad | 2012 | Algebra | A5

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2012_f7e2ed](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2012_f7e2ed.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Balkan Mathematical Olympiad
- Title: 29th Balkan Mathematical Olympiad
- Subtitle: Short-Listed Problems and Solutions
- Year: 2012
- Editors: Tekman, Okan; Bahadır, Seliim; Kadan, Fehmi Emre; Kurt, Süreyya Emre; Tekin, Ömer Faruk
- Place: Antalya, Turkey
- Series: Balkan Mathematical Olympiad
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Let $m_0$ be an integer at which $f$ achieves its maximum. Then $h(n) \geq f(m_0)g(n - m_0)$ for all $n \in \mathbb{Z}$ and
$$
\sum_{n \in \mathbb{Z}} h(n) \geq f(m_0) \sum_{n \in \mathbb{Z}} g(n - m_0) = f(m_0) \sum_{n \in \mathbb{Z}} g(n).
$$
Similarly, if $n_0$ is an integer at which $g$ achieves its maximum, then
$$
\sum_{n \in \mathbb{Z}} h(n) \geq g(n_0) \sum_{n \in \mathbb{Z}} f(n - n_0) = g(n_0) \sum_{n \in \mathbb{Z}} f(n).
$$
Combining these yields
$$
\sum_{n \in \mathbb{Z}} h(n) \geq (f(m_0))^{1/q} \left(\sum_{n \in \mathbb{Z}} g(n)\right)^{1/q} (g(n_0))^{1/p} \left(\sum_{n \in \mathbb{Z}} f(n)\right)^{1/p}.
$$
Since
$$
(f(m_0))^{1/q} \left(\sum_{n \in \mathbb{Z}} f(n)\right)^{1/p} = \left( (f(m_0))^{p-1} \sum_{n \in \mathbb{Z}} f(n) \right)^{1/p} \geq \left( \sum_{n \in \mathbb{Z}} (f(n))^p \right)^{1/p},
$$
and
$$
(g(n_0))^{1/p} \left(\sum_{n \in \mathbb{Z}} g(n)\right)^{1/q} \geq \left( \sum_{n \in \mathbb{Z}} (g(n))^q \right)^{1/q},
$$
the conclusion follows.

## Supplied solution 2

We apply H\"older's inequality to obtain
$$
\left(\sum_{k \in \mathbb{Z}} (f(k))^{q(p-1)}\right)^{1/q} \left(\sum_{k \in \mathbb{Z}} (g(n-k))^{p(q-1)}\right)^{1/p} \geq \sum_{k \in \mathbb{Z}} (f(k))^{p-1} (g(n-k))^{q-1}.
$$
Hence
$$
h(n) \left(\sum_{k \in \mathbb{Z}} (f(k))^p\right)^{1-1/p} \left(\sum_{k \in \mathbb{Z}} (g(k))^q\right)^{1-1/q} \geq \sum_{k \in \mathbb{Z}} (f(k))^p (g(n-k))^q.
$$
Summing over $n$ gives
$$
\left(\sum_{n \in \mathbb{Z}} h(n)\right) \left(\sum_{k \in \mathbb{Z}} (f(k))^p\right)^{1-1/p} \left(\sum_{k \in \mathbb{Z}} (g(k))^q\right)^{1-1/q} \geq \left(\sum_{k' \in \mathbb{Z}} (f(k'))^p\right) \left(\sum_{k' \in \mathbb{Z}} (g(k'))^q\right).
$$
The conclusion follows.
