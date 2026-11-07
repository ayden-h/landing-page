# bmo_2023_0b3edf

BMO-SL | Balkan Mathematical Olympiad | 2023 | Geometry | G1

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [bmo_2023_0b3edf](https://mathnet.mit.edu/data_v2/full/balkan-mathematical-olympiad/bmo_2023_0b3edf.json.gz)

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

We will prove the following auxiliary result.
*Lemma.* Let $ABC$ be an arbitrary triangle, and $D$ be an arbitrary point on the segment $AB$. Denote by $O_1$ and $O_2$ the incenters of $\triangle ADC$ and $\triangle BDC$, respectively. If the circumcircle $\omega$ of $\triangle CO_1O_2$ intersects the sides $AC$ and $BC$ at points $P$ and $Q$, respectively, then
$$
CP - CQ = (AC - BC) + (BD - AD).
$$
*Proof.* Denote by $T$ and $K$ the orthogonal projections of $O_1$ over $AC$ and $CD$, respectively. Let $R$ be the second intersection point of $\omega$ with $CD$. Since $CO_1$ is an angle bisector it follows that $O_1P = O_1R$, thus $\triangle O_1TP \cong \triangle O_1KR$. Hence, $TP = KR$ and
$$
CP + CR = 2 \cdot CT(= 2 \cdot CK) = AC + CD - AD.
$$
Analogously, $CQ + CR = BC + CD - BD$ and taking the difference of the last two expressions, the result follows. $\square$

Now, applying the Lemma for $\triangle DBC$, we deduce that
$$
CQ - CP = (CD - BC) + (BX - DX).
$$
(G1-1)
Analogously, applying the Lemma for $\triangle ABD$, we derive
$$
AN - AM = (AD - AB) + (BX - DX).
$$
(G1-2)
Subtracting (G1-2) from (G1-1) and taking into account that $CD - BC = AD - AB$ we obtain $AM + CQ = AN + CP$, as desired.

**Remark.** The reverse statement also holds true, i.e., if for a convex quadrilateral $ABCD$ we have $AM + CQ = AN + CP$, then $ABCD$ is circumscribed.
