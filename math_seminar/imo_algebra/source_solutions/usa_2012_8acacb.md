# usa_2012_8acacb

IMO-TST | United States | 2012 | TSTST 2012 Problems | 6

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [usa_2012_8acacb](https://mathnet.mit.edu/data_v2/full/united-states/usa_2012_8acacb.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: United States
- Title: USA and International Mathematical Olympiads 2011-2012
- Editors: Feng, Zuming; Sun, Yi

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

We may assume without loss of generality that $a \ge b \ge c$. Noting that $(1-b)^2 + (1-c)^2 = (b+c-1)^2 - 2bc + 1$, we may transform the right hand side of the desired inequality into
$$
(1-a)^2 + (1-b)^2 + (1-c)^2 + \frac{2\sqrt{2abc}}{\sqrt{a^2 + b^2 + c^2}} = \frac{2\sqrt{2abc}}{\sqrt{a^2 + b^2 + c^2}} - 2bc + (1-a)^2 + (b+c-1)^2 + 1.
$$
Rearranging, it suffices to show that
$$
\frac{2bc(\sqrt{a^2 + b^2 + c^2} - \sqrt{2a})}{\sqrt{a^2 + b^2 + c^2}} \le (1-a)^2 + (b+c-1)^2, \quad (19)
$$
which after rationalizing the numerator is equivalent to
$$
\frac{2bc(b^2 + c^2 - a^2)}{\sqrt{a^2 + b^2 + c^2} (\sqrt{2}a + \sqrt{a^2 + b^2 + c^2})} \le (1-a)^2 + (b+c-1)^2. \quad (20)
$$
If $b^2 + c^2 - a^2 \le 0$, then (20) is clearly true. We may therefore assume that $b^2 + c^2 - a^2 > 0$. To simplify (20), we want to produce the term $b^2 + c^2 - a^2$ from the right-hand side of (20). By the RMS-AM inequality, we have
$$
(1-a)^2 + (b+c-1)^2 \ge \frac{[(1-a) + (b+c-1)]^2}{2} = \frac{(b+c-a)^2}{2}. \quad (21)
$$
By our assumption that $a \ge b \ge c$, we obtain
$$
b^2 + c^2 - a^2 - (b + c - a)^2 = 2(ab + ac - bc - a^2) = -2(a - b)(a - c) \le 0,
$$
hence
$$
\frac{(b+c-a)^2}{2} \ge \frac{b^2+c^2-a^2}{2} \ge 0. \quad (22)
$$
Together, (21) and (22) show that
$$
(1-a)^2 + (b+c-1)^2 \ge \frac{b^2+c^2-a^2}{2}. \quad (23)
$$
On the other hand, the ordering $a \ge b \ge c \ge 0$ implies $a^2 \ge bc$, so $a \ge \sqrt{bc}$. Hence by the AM-GM inequality, we have
$$
\sqrt{a^2 + b^2 + c^2} (\sqrt{2a} + \sqrt{a^2 + b^2 + c^2}) \ge \sqrt{bc + 2bc} (\sqrt{2bc} + \sqrt{bc + 2bc}) = (3 + \sqrt{6})bc > 4bc. \quad (24)
$$
Dividing both sides of (24) by the left hand side and combining it with (23), we find that
$$
(1-a)^2 + (b+c-1)^2 \ge \frac{b^2+c^2-a^2}{2} \cdot \frac{4bc}{\sqrt{a^2 + b^2 + c^2} (\sqrt{2a} + \sqrt{a^2 + b^2 + c^2})},
$$
which is the desired (20).
