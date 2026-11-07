# ind_2011_d8fd7b

IMO-TST | India | 2011 |  | 3

**Scope:** selection. **Review:** source text not independently verified.

**Source:** [ind_2011_d8fd7b](https://mathnet.mit.edu/data_v2/full/india/ind_2011_d8fd7b.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: India
- Title: Some problems used in Indian team selection for IMO-2011
- Year: 2011
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Let the circum-circle of $BCD$ be $\Gamma$ and let the circle with diameter $OD$ be $\Gamma'$. Let the mid-point of $OD$ be $O'$ (which is also the centre of $\Gamma'$). Now $OO'$ passes through $D$ and hence $\Gamma'$ and $\Gamma$ are tangent to each other at $D$. Hence there is a homothety with centre $D$ taking $\Gamma'$ to $\Gamma$, with ratio $2$. Since $\angle OMD = 90^\circ$, the point $M$ is on $\Gamma'$. Let the image of $M$ under the homothety be $D'$; it lies on $\Gamma$ and $M$ is the midpoint of $DD'$.

Consider the half-turn centred at $M$ taking $D$ to $D'$. This also takes $C$ to $E$ as $M$ is the mid-point of $CE$. Let $B'$ be the image of $B$ under this transformation. Since the half turn takes a line to another line parallel to it, the image of $BC$ is $B'E$; and $BC \parallel B'E$. Thus $AE \parallel BC \parallel B'E$. It follows that $A$, $B'$, $E$ are collinear. Observe that $A$, $B$ lie on the same side of $CE$. Since we have performed a rigid transformation preserving $C$, $E$, the images of $A$, $B$ must also lie on the same side of $CE$. This implies that $A$ and $B'$ lie on different sides of $CE$. Thus $E$ lies between $A$ and $B'$. Because of this, we have
$$
\begin{aligned}
AB' = AE + EB' &= AE + BC \quad (\text{half-turn takes } BC \text{ to } B'E) \\
&= AB.
\end{aligned}
$$
We also observe that the half-turn takes triangle $CD'B$ to $EDB'$. Therefore $\angle CD'B = \angle EDB'$. Thus we get
$$
\begin{aligned}
\angle BDB' = \angle BDE + \angle EDB' &= \angle BDE + \angle CD'B = \angle BDE + \angle CDB \\
&= \angle CDE = \angle CBA = 180^\circ - \angle BAB',
\end{aligned}
$$
since $BC \parallel AE$. This shows that $B$, $D$, $B'$, $A$ are concyclic. Since $AB = AB'$, they subtend equal angle at $D$. Thus $\angle ADB' = \angle BDA'$. Thus
$$
2\angle BDA = \angle BDA + \angle ADB' = \angle BDA + \angle ADE + \angle EDB'.
$$
But observe $\angle EDB' = \angle CD'B = \angle CDB$. Using this we obtain
$$
2\angle BDA = \angle BDA + \angle ADE + \angle CDB = \angle CDE.
$$
This completes the proof.
