# mkd_2008_8fbac0

BMO | North Macedonia | 2008 |  | 3

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [mkd_2008_8fbac0](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_8fbac0.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: North Macedonia
- Title: Macedonian Mathematical Competitions
- Year: 2008
- Editors: Maneva-Erakovic, Vesna; Malcheski, Risto; Markovski, Gjorgji; Markovski, Jasmina; Prangoski, Bojan; Cvetkovski, Zdravko; Petruschevski, Mirko; Malcheski, Aleksa
- Organization: MACEDONIAN MATHEMATICAL SOCIETY

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Denote $90n+1 = m$. We investigate the number of the lines modulo $4$ consecutively reducing different types of lines. The vertical and horizontal lines are $(m+5)+(m+1)=2(m+3)$ which is divisible by $4$. Moreover, every line which makes an acute angle to the axis $Ox$ (i.e. that line has a positive angular coefficient) corresponds to a unique line with an obtuse angle (consider the symmetry with respect to the line through the midpoints of $AB$ and $CD$). Therefore it is enough to prove that the lines with acute angles are an even number.

Every line which does not pass through the center $O$ of the rectangle corresponds to another line with the same angular coefficient (consider the symmetry with respect to $O$). Therefore it is enough to consider the lines through $O$.
Every line through $O$ has an angular coefficient $\frac{p}{q}$, where $(p,q)=1$, $p$ and $q$ are odd positive integers. (To see this, consider the two nearest, from the two sides, to $O$ points of the line).
If $p \ne 1$, $q \ne 1$, $p \le m$ and $q \le m$, the line with angular coefficient $\frac{p}{q}$ uniquely corresponds to the line with angular coefficient $\frac{q}{p}$. It remains to prove that the number of the remaining lines is even.

The last number is
$$
1+\frac{\varphi(m+2)}{2}+\frac{\varphi(m+4)}{2}-1=\frac{\varphi(m+2)+\varphi(m+4)}{2}
$$
because we have:
1) one line with $p=q=1$;
2) $\frac{\varphi(m+2)}{2}$ lines with angular coefficient $\frac{p}{m+2}$, $p \le m$ is odd and $(p,m+2)=1$;
3) $\frac{\varphi(m+4)}{2}-1$ lines with angular coefficient $\frac{p}{m+4}$, $p \le m$ is odd and $(p,m+4)=1$.
Now the assertion follows from the fact that the number $\varphi(m+2)+\varphi(m+4)=\varphi(90n+3)+\varphi(90n+5)$ is divisible by $4$.

