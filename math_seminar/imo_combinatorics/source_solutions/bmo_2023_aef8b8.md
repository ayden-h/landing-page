# bmo_2023_aef8b8

BMO-SL | Balkan Mathematical Olympiad | 2023 | Combinatorics | C1

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2023_aef8b8](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2023_aef8b8.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Balkan Mathematical Olympiad
- Title: Shortlisted Problems with Solutions
- Year: 2023
- Editors: Üçer, Melih; Bahadır, Selim; Kadan, Fehmi Emre; Yıldız, Mehmet Akif; İleri, Ahmet; Kaymak, Ozan
- Place: Antalya-Türkiye
- Series: BMO
- Volume: 2023

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

If on move $2y - 1$, Joe removes $1 \le a \le 2y - 1$ stones, then on move $2y$, Penny can remove either $2y - a$ or $2y + 1 - a$ stones (both of which are in the valid range). Thus Penny can ensure that the two moves remove either $2y$ or $2y + 1$ stones.

If on $k$ occasions, Penny chooses to ensure $2y + 1$ stones are removed then after move $2z$, there will be
$$
k + \sum_{y=1}^{z} 2y = z(z + 1) + k
$$
stones removed. Thus after move $2z$, Penny can ensure there are any number between $z(z + 1)$ and $z(z + 2)$ stones removed.

Setting $z = 69$ we see that after move $2 \cdot 69 = 138$, Penny can ensure $69 \cdot 70 \le 4860 \le 69 \cdot 71$ stones have been removed and so there are 140 stones remaining. Joe will leave between 1 and 139 stones which Penny can remove on her turn.

