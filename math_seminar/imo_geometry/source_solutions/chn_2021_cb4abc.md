# chn_2021_cb4abc

China-TST | China | 2021 | Test III, Second Day | 6

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [chn_2021_cb4abc](https://mathnet.mit.edu/data_v2/full/china/chn_2021_cb4abc.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: China

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

We call $(x, y)$ an “$m$-integral point” if $x, y$ are integers and $m|x$, $m|y$. By a proper translation, we may assume that the unique interior $m$-integral point is at $(0, 0)$. Extend $AO$, $BO$, and $CO$ to meet the opposite sides at points $D$, $E$, and $F$, respectively. Denote
$$
p = \frac{OD}{AD} = \frac{S_{\triangle OBC}}{S_{\triangle ABC}}, \quad q = \frac{OE}{BE} = \frac{S_{\triangle OCA}}{S_{\triangle ABC}}, \quad r = \frac{OF}{CF} = \frac{S_{\triangle OAB}}{S_{\triangle ABC}}.
$$
Evidently, $p + q + r = 1$; assume $p \ge q \ge r > 0$ (so that $p \ge \frac{1}{3} \ge \frac{1}{m+2}$). Let $A'$, $B'$, and $D'$ be the respective symmetric points of $A$, $B$, and $D$ about $O$. On the line $AD$, let $UV$ be the intersection of the segments $AD$ and $D'A'$, namely, $U$ is $A$ or $D'$, $V$ is $D$ or $A'$, whichever is closer to $O$. Since $\triangle BUV \subseteq \triangle ABC$, except for $O$, there is no $m$-integral point in the interior of $\triangle BUV$ or in the interior of $UV$, and neither in the symmetric $\triangle B'UV$. Together, they imply that the parallelogram $BUB'V$

(centered at $O$) does not have interior $m$-integral points other than $O$. By Minkowski's theorem,
$$
4m^2 \geq S_{BUB'V} = 4S_{\Delta OBV} = 4S_{\Delta ABC} \times \min\{p, 1-p\} \times \frac{q}{q+r};
$$
$$
S_{\Delta ABC} \leq \frac{4m^2}{4 \min\{p, 1-p\}} \times \frac{q+r}{q} \leq \frac{2m^2}{\min\{p, 1-p\}}.
$$
If $p > \frac{m}{m+1}$, then
$$
\frac{OD}{OA'} = \frac{OD}{AO} = \frac{p}{1-p} > m,
$$
taking $OL = m \cdot OA'$ on segment $OD$, $L$ must be an $m$-integral point inside $\triangle ABC$, which is contradictory.
Therefore, $p \le \frac{m}{m+1}$, $\min\{p, 1-p\} \ge \frac{1}{m+2}$, and we deduce
$$
S_{\triangle ABC} \le 2m^2(m+2). \quad \square
