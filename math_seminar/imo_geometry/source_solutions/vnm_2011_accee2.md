# vnm_2011_accee2

VMO | Vietnam | 2011 | First day of contest | 4

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [vnm_2011_accee2](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2011_accee2.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Vietnam
- Title: VIETNAMESE MATHEMATICAL OLYMPIAD IN 2011
- Year: 2011
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

To verify the claim, we will show that it is possible to cover the pentagon $ABCDE$ by 5 unit discs with center lying on the edges of the pentagon.

We have following remark:
**Remark:** It is possible to cover a triangle $XYZ$ with edges of length not exceeding $\sqrt{3}$ by 3 unit discs with centers at the vertices of the triangle.

**Proof:** Assuming the contrary, there exists a point $M$ belonging to triangle $XYZ$ but not lying in the unit discs with centers at the vertices of the triangle. Then we have $MX > 1$, $MY > 1$ and $MZ > 1$.

Clearly, among the angles $\widehat{XMY}$, $\widehat{YMZ}$ and $\widehat{ZMX}$ at least one is larger than $120^\circ$. Without loss of generality, assume that $\widehat{XMY} \ge 120^\circ$. Using the cosine theorem for triangle $XMY$, we obtain
$$
XY^2 = MX^2 + MY^2 - 2MX \cdot MY \cdot \cos \widehat{XMY} > 1 + 1 + 2 \cdot \frac{1}{2} = 3 \quad (\text{since } \cos \widehat{XMY} \le -\frac{1}{2}).
$$
Consequently $XY > \sqrt{3}$, contradicting the assumption. The contradiction yields the claim to be verified.

Since the triangles $ABC$, $ACD$ and $ADE$ have edges with length less than $\sqrt{3}$, according to the remark, they can be covered by the triples of unit discs $((A), (B), (C))$, $((A), (C), (D))$ and $((A), (D), (E))$. Hence the pentagon $ABCDE$ is covered by 5 unit discs with center at the vertices of the pentagon. According to Dirichlet's principle, among the 5 discs there exists one containing at least 403 of the chosen points. ■
