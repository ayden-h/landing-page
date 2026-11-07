# kor_2006_db5ca5

KMO | South Korea | 2006 | Second Day | 5

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [kor_2006_db5ca5](https://mathnet.mit.edu/data_v2/full/south-korea/kor_2006_db5ca5.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: South Korea
- Title: THE 19TH KOREAN MATHEMATICAL OLYMPIAD
- Year: 2006
- Organization: KOREAN MATHEMATICAL OLYMPIAD COMMITTEE; THE KOREAN MATHEMATICAL SOCIETY
- Publisher: THE KOREAN MATHEMATICAL SOCIETY
- Place: Seoul, KOREA
- Series: Korean Mathematical Olympiad
- Volume: 19
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Suppose $\triangle ACE$ is equilateral, then $\triangle BDF$ is always equilateral, because three triangles $ACE$, $CDE$, $EFA$ are identical and shape of the hexagon $ABCDEF$ is invariable under the $120^\circ$ rotation around the center of $\triangle ACE$. That is, since $B \to D \to F$ is obtained from the $120^\circ$ rotation, $\triangle BDF$ is an equilateral triangle.

We now show that if three similar triangles $ABC$, $CDE$, $EFA$ are not of a isosceles triangle whose two same angles are $30^\circ$, the converse is true. First, let $\angle BAC = \angle DCE = \angle FEA = \alpha$, $\angle BCA = \angle DEC = \angle FAE = \beta$. Suppose that $\triangle BDF$ is equilateral. Let
$$
\begin{aligned}
\frac{AB}{AC} &= \frac{CD}{CE} = \frac{EF}{EA} = s \\
\frac{BC}{AC} &= \frac{DE}{CE} = \frac{FA}{EA} = t,
\end{aligned}
$$
$AC = a$, $CE = b$, $EA = c$. For $\triangle ABF$, we have
$$
\begin{aligned}
BF^2 &= AB^2 + FA^2 - 2AB \cdot FA \cdot \cos(\angle BAF) \\
&= (sa)^2 + (tc)^2 - 2stac \cdot \cos(\alpha + \beta + A) \\
&= s^2a^2 + t^2c^2 - 2stac[\cos(\alpha + \beta) \cos A - \sin(\alpha + \beta) \sin A].
\end{aligned}
$$

Similarly we have,
$$BD^2 = s^2b^2 + t^2a^2 - 2stab[\cos(\alpha + \beta) \cos C - \sin(\alpha + \beta) \sin C]$$
$$DF^2 = s^2b^2 + t^2a^2 - 2stab[\cos(\alpha + \beta) \cos C - \sin(\alpha + \beta) \sin C].$$
$\frac{1}{2}ac \sin A = \frac{1}{2}ab \sin C = \frac{1}{2}bc \sin E$ equals the area of $\triangle ACE$, and $BF^2 = BD^2 = DF^2$. Moreover, we have $2ac \cos A = a^2 + c^2 - b^2$, $2ab \cos C = a^2 + b^2 - c^2$, $2bc \cos E = b^2 + c^2 - a^2$. Let $\cos(\alpha+\beta) = K$, then we have
$$
\begin{aligned}
& s^2a^2 + t^2c^2 - stK(a^2 + c^2 - b^2) \\
&= s^2b^2 + t^2c^2 - stK(a^2 + b^2 - c^2) \\
&= s^2c^2 + t^2b^2 - stK(b^2 + c^2 - a^2)
\end{aligned}
$$
Now let
$$
s^2 - t^2 = x, \quad 2stK - s^2 = y, \quad t^2 - 2stK = z,
$$
then we have
$$
xa^2 + yb^2 + zc^2 = ya^2 + zb^2 + xc^2 = za^2 + xb^2 + yc^2 \quad (1)
$$
From the equations (1), suppose first that $x = y = z$, then we have $s = t$ and $K = \frac{1}{2}$; hence $\alpha + \beta = 60^\circ$. That is, three similar triangles $ABC$, $CDE$, $EFA$ are of a isosceles triangle whose two same angles are $30^\circ$. We exclude this case. Second, suppose $x, y, z$ are either all distinct or two of them are equal, then we get the equations $a = b = c$ by some calculations, which means that $\triangle ACE$ is equilateral. We conclude that $\triangle ACE$ is equilateral unless three similar triangles $ABC$, $CDE$, $EFA$ are of a isosceles triangle whose two same angles are $30^\circ$. $\square$
