# imo_2011_3bbde9

IMO-SL | IMO | 2011 | Combinatorics | C7

**Scope:** shortlist. **Review:** source text not independently verified.

**Source:** [imo_2011_3bbde9](https://mathnet.mit.edu/data_v2/full/imo/imo_2011_3bbde9.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: IMO
- Title: 52nd International Mathematical Olympiad
- Subtitle: Problem Shortlist with Solutions
- Year: 2011
- Editors: de Smit, Bart; Bogdanov, Ilya; Bosman, Johan; Brouwer, Andries; Dalla Torre, Gabriele; Kós, Géza; Lenstra, Hendrik; Leytem, Charles; van Luijk, Ronald; Reiher, Christian; Specht, Eckard; Sterk, Hans; Taelman, Lenny
- Organization: International Mathematical Olympiad
- Place: Amsterdam, The Netherlands
- Series: International Mathematical Olympiad
- Volume: 52nd

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 2

We present a different proof of the estimate which is the hard part of the problem. Let $S=35$, $H=17$, $m=39$; so the table size is $2011=S m+H(m-1)$, and the napkin size is $52=S+H$. Fix any positive integer $M$ and call a cell vicious if it contains a number distinct from $M$. We will prove that there are at least $H^{2}(m-1)+2 S H m$ vicious cells.

Firstly, we introduce some terminology. As in the previous solution, we number rows and columns and we use the same notions of small and big indices and lines; so, an index is small if it is congruent to one of the numbers $1,2, \ldots, S$ modulo $(S+H)$. The numbers $1,2, \ldots, S+H$ will be known as residues. For two residues $i$ and $j$, we say that a cell is of type $(i, j)$ if the index of its row is congruent to $i$ and the index of its column to $j$ modulo $(S+H)$. The number of vicious cells of this type is denoted by $v_{ij}$.

Let $s, s'$ be two variables ranging over small residues and let $h, h'$ be two variables ranging over big residues. A cell is said to be of class $A, B, C$, or $D$ if its type is of shape $(s, s')$, $(s, h)$, $(h, s)$, or $(h, h')$, respectively. The numbers of vicious cells belonging to these classes are denoted in this order by $a, b, c$, and $d$. Observe that each cell belongs to exactly one class.

**Claim 1.** We have
$$
m \leq \frac{a}{S^{2}}+\frac{b+c}{2 S H} . \tag{1}
$$
Proof. Consider an arbitrary small row $r$. Denote the numbers of vicious cells on $r$ belonging to the classes $A$ and $B$ by $\alpha$ and $\beta$, respectively. As in the previous solution, we obtain that $\alpha \geq S$ or $\beta \geq H$. So in each case we have $\frac{\alpha}{S}+\frac{\beta}{H} \geq 1$.

Performing this argument separately for each small row and adding up all the obtained inequalities, we get $\frac{a}{S}+\frac{b}{H} \geq m S$. Interchanging rows and columns we similarly get $\frac{a}{S}+\frac{c}{H} \geq m S$. Summing these inequalities and dividing by $2 S$ we get what we have claimed.

**Claim 2.** Fix two small residues $s, s'$ and two big residues $h, h'$. Then $2 m-1 \leq v_{s s'}+v_{s h'}+v_{h h'}$.

Proof. Each napkin covers exactly one cell of type $(s, s')$. Removing all napkins covering a vicious cell of this type, we get another collection of napkins, which covers each cell of type $(s, s')$ either $0$ or $M$ times depending on whether the cell is vicious or not. Hence $(m^{2}-v_{s s'}) M$ napkins are left and throughout the proof of Claim 2 we will consider only these remaining napkins. Now, using a red pen, write in each cell the number of napkins covering it. Notice that a cell containing a red number greater than $M$ is surely vicious.

We call two cells neighbors if they can be simultaneously covered by some napkin. So, each cell of type $(h, h')$ has not more than four neighbors of type $(s, s')$, while each cell of type $(s, h')$ has not more than two neighbors of each of the types $(s, s')$ and $(h, h')$. Therefore, each red number at a cell of type $(h, h')$ does not exceed $4 M$, while each red number at a cell of type $(s, h')$ does not exceed $2 M$.

Let $x, y$, and $z$ be the numbers of cells of type $(h, h')$ whose red number belongs to $(M, 2 M]$, $(2 M, 3 M]$, and $(3 M, 4 M]$, respectively. All these cells are vicious, hence $x+y+z \leq v_{h h'}$. The red numbers appearing in cells of type $(h, h')$ clearly sum up to $(m^{2}-v_{s s'}) M$. Bounding each of these numbers by a multiple of $M$ we get
$$
(m^{2}-v_{s s'}) M \leq ((m-1)^{2}-(x+y+z)) M+2 x M+3 y M+4 z M,
$$
i.e.
$$
2 m-1 \leq v_{s s'}+x+2 y+3 z \leq v_{s s'}+v_{h h'}+y+2 z .
$$
So, to prove the claim it suffices to prove that $y+2 z \leq v_{s h'}$.

For a cell $\delta$ of type $(h, h')$ and a cell $\beta$ of type $(s, h')$ we say that $\delta$ forces $\beta$ if there are more than $M$ napkins covering both of them. Since each red number in a cell of type $(s, h')$ does not exceed $2 M$, it cannot be forced by more than one cell.

On the other hand, if a red number in a $(h, h')$-cell belongs to $(2 M, 3 M]$, then it forces at least one of its neighbors of type $(s, h')$ (since the sum of red numbers in their cells is greater than $2 M$). Analogously, a $(h, h')$-cell with the red number in $(3 M, 4 M]$ forces both its neighbors of type $(s, h')$, since their red numbers do not exceed $2 M$. Therefore there are at least $y+2 z$ forced cells and clearly all of them are vicious, as desired.

**Claim 3.** We have
$$
2 m-1 \leq \frac{a}{S^{2}}+\frac{b+c}{2 S H}+\frac{d}{H^{2}} \tag{2}
$$
Proof. Averaging the previous result over all $S^{2} H^{2}$ possibilities for the quadruple $(s, s', h, h')$, we get $2 m-1 \leq \frac{a}{S^{2}}+\frac{b}{S H}+\frac{d}{H^{2}}$. Due to the symmetry between rows and columns, the same estimate holds with $b$ replaced by $c$. Averaging these two inequalities we arrive at our claim.

Now let us multiply (2) by $H^{2}$, multiply (1) by $(2 S H-H^{2})$ and add them; we get
$H^{2}(2 m-1)+(2 S H-H^{2}) m \leq a \cdot \frac{H^{2}+2 S H-H^{2}}{S^{2}}+(b+c) \frac{H^{2}+2 S H-H^{2}}{2 S H}+d=a \cdot \frac{2 H}{S}+b+c+d$.

The left-hand side is exactly $H^{2}(m-1)+2 S H m$, while the right-hand side does not exceed $a+b+c+d$ since $2 H \leq S$. Hence we come to the desired inequality.

1 additional supplied solution(s) require external figures; use the source link.
