# mkd_2008_af4ffe

BMO | North Macedonia | 2008 | Regional competitions, 7th grade | 5

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [mkd_2008_af4ffe](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2008_af4ffe.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: North Macedonia
- Title: Macedonian Mathematical Competitions
- Year: 2008
- Editors: Maneva-Erakovic, Vesna; Malcheski, Risto; Markovski, Gjorgji; Markovski, Jasmina; Prangoski, Bojan; Cvetkovski, Zdravko; Petruschevski, Mirko; Malcheski, Aleksa
- Organization: MACEDONIAN MATHEMATICAL SOCIETY

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

We have $\overline{A_1A_2} = \overline{A_1T_1} + \overline{T_1A_2} + \overline{T_2A_2}$, $\overline{B_1B_2} = \overline{B_1T_1} + \overline{T_1B_2} + \overline{T_2B_2}$, $\overline{C_1C_2} = \overline{C_1T_1} + \overline{T_1C_2} + \overline{T_2C_2}$. If we sum the last three equalities we obtain
$$
\overline{A_1A_2} + \overline{B_1B_2} + \overline{C_1C_2} = 3\overline{T_1T_2} + (\overline{A_1T_1} + \overline{B_1T_1} + \overline{C_1T_1}) + (\overline{T_2A_2} + \overline{T_2B_2} + \overline{T_2C_2}) \dots(1)
$$
From the properties of medians and center of mass we have
$$
\overline{A_1T_1} = \frac{2}{3}(\overline{A_1B_1} + \frac{1}{2}\overline{B_1C_1}), \quad \overline{B_1T_1} = \frac{2}{3}(\overline{B_1C_1} + \frac{1}{2}\overline{C_1A_1}), \quad \overline{C_1T_1} = \frac{2}{3}(\overline{C_1A_1} + \frac{1}{2}\overline{A_1B_1})
$$
So we have
$$
\begin{aligned} \overline{A_1T_1} + \overline{B_1T_1} + \overline{C_1T_1} &= \frac{2}{3}(\overline{A_1B_1} + \frac{1}{2}\overline{B_1C_1}) + \frac{2}{3}(\overline{B_1C_1} + \frac{1}{2}\overline{C_1A_1}) + \frac{2}{3}(\overline{C_1A_1} + \frac{1}{2}\overline{A_1B_1}) = \\ &= \frac{1}{3}(\overline{A_1B_1} + \overline{B_1C_1} + \overline{C_1A_1}) + \frac{1}{3}(\overline{B_1C_1} + \overline{C_1A_1} + \overline{A_1B_1}) = \\ &= \frac{2}{3}\overline{A_1A_1} + \frac{1}{3}\overline{B_1B_1} = \frac{2}{3}\overline{o} + \frac{1}{3}\overline{o} = \overline{o} + \overline{\overline{o}} = \overline{\overline{o}}. \end{aligned}
$$
Similarly we have $\overline{A_2T_2} + \overline{B_2T_2} + \overline{C_2T_2} = \overline{o}$ from where we have that $\overline{T_2A_2} + \overline{T_2B_2} + \overline{T_2C_2} = \overline{o}$. Finally if we substitute in (1) we get
$$
\overline{A_1A_2} + \overline{B_1B_2} + \overline{C_1C_2} = 3\overline{T_1T_2} + \overline{o} + \overline{\overline{o}} = 3\overline{T_1T_2}.
$$
