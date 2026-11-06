# rou_2018_a59bad

RMM | Romania | 2018 | First Day | 3

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [rou_2018_a59bad](https://mathnet.mit.edu/data_v2/full/romania/rou_2018_a59bad.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Romania
- Title: ROMANIAN MATHEMATICAL COMPETITIONS
- Year: 2018
- Organization: Romanian Mathematical Society
- Series: Romanian Mathematical Contests
- Volume: 25

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

For the checked rewritten exposition, see `../reviewed_solutions/W10.md`.

## Supplied solution 1

The answer is in the negative: Ann has a strategy allowing her to prevent Bob's victory.
We say that two unit grid-segments form a *low-left corner* (or *LL-corner*) if they share an endpoint which is the lowest point of one and the leftmost point of the other. An *up-right corner* (or *UR-corner*) is defined similarly. The common endpoint of two unit grid-segments at a corner is the *joint* of that corner.
Fix a vertical line on the grid and call it the *midline*; the unit grid-segments along the midline are called *middle segments*. The unit grid-segments lying to the left/right of the midline are called *left/right segments*. Partition all left segments into LL-corners, and all right segments into UR-corners.
We now describe Ann's strategy. Her first move consists in orienting some middle segment arbitrarily. Assume that at some stage, Bob orients some segment $s$. If $s$ is a middle segment, Ann orients any free middle segment arbitrarily. Otherwise, $s$ forms a corner in the partition with some other segment $t$. Then Ann orients $t$ so that the joint of the corner is either the source of both arrows, or the target of both. Notice that after any move of Ann's, each corner in the partition is either completely oriented or completely not oriented. This means that Ann can always make a required move.
Assume that Bob wins at some stage, i.e., an oriented cycle $C$ occurs. Let $X$ be the lowest of the leftmost points of $C$, and let $Y$ be the topmost of the rightmost points of $C$. If $X$ lies (strictly) to the left of the midline, then $X$ is the joint of some corner whose segments are both oriented. But, according to Ann's strategy, they are oriented so that they cannot occur in a cycle — a contradiction. Otherwise, $Y$ lies to the right of the midline, and a similar argument applies. Thus, Bob will never win, as desired.

