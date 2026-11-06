# vnm_2015_7ffead

VMO | Vietnam | 2015 | Day II - Jan 09, 2015 | 7

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [vnm_2015_7ffead](https://mathnet.mit.edu/data_v2/full/vietnam/vnm_2015_7ffead.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Vietnam
- Title: Vietnam Mathematical Olympiad 2015
- Subtitle: Problems and Solutions
- Year: 2015
- Editors: Hai, Nguyen Minh; Hung, Tran Quang; Huong, Hoang Que
- Organization: Center for Educational Research and Applications (CERA), Vietnam National University - Hanoi
- Place: Hanoi
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

We denote the boys by the integers from $1$ to $m$ and girls by the integers from $1$ to $n$. Each presentation is presented by a table of $m$ rows (corresponding to $m$ girls) and $n$ columns (corresponding to $n$ boys). Each cell takes a label $0$ or $1$ as shown in the following:

* Cell in $i$-th row and $j$-th column takes label $1$ if $i$-th boy sang duet with $j$-th girl in that presentation.
* Cell in $i$-th row and $j$-th column takes label $0$ otherwise.

A table is called "good" if each row and each column contains at least one cell which takes label $1$.
A "good" table is equivalent to a possible presentation.

Let consider a child denoted by $X$. Without losing generality, we assume that $X$ is a girl. The presentation depends on $X$ if and only if on its corresponding table there is at least one column which has exactly one cell which takes label $1$ and this cell lies on the row corresponding to $X$. That column is called the depending on $X$ column.

We need to prove that among the tables depending on $X$ the number of tables which has odd number of $1$ label cells is equal to the number of even ones.

Let consider a table with $k$ columns depending on $X$. Of course, $k < n$. Because, if $k = n$ then all the cells on $X$ row take label $1$ while the remaining cells of the table take the label $0$. Hence $n \ge 2$, this implies that there exists a girl that had not sung any song in that presentation. This is contradiction to the condition of validity of $X$.

For $k < n$ we exclude $k$ depending on $X$ columns from the table and the table loses exactly $k$ $1$ label cells. The $n-k$ remaining cells on $X$ row can have label $0$ or $1$ because every remaining column has at least one cell label $1$ not belonging to $X$. In consequence, if we continue excluding $X$ row, the table is still "good".

Such that, the number of "good" tables and depending on $X$ is $2^{n-k}$ multiplied by the number of "good" $(m-1) \times (n-k)$ tables. If we choose an arbitrary cell on row $X$ and change its label $0$ to $1$ or $1$ to $0$, we change the parity of number of $1$ label cells on the table. This leads to the isomorphism between the tables of even number of $1$ label cells and the tables of odd number of $1$ label cells. This fact does make the proof of our problem.

Next, we denote $f(m, n)$ and $g(m, n)$ be the number of "good" $m \times n$ tables with even and odd number of $1$ label cells. Consider an arbitrary girl, denoted by $X$. Let consider the following cases:

* If exists a column that depends on $X$ then in the above part the number of odd number $1$ label cells equals to the number of even $1$ label cells. Denote this quantity by $h(m, n)$.
* If there does not exist any column depends on $X$ then if we exclude the row corresponding to $X$ then we have a $(m-1) \times n$ "good" table.

The numbers of cases where row $X$ has odd and even cells labelling $1$ are defined as following,
$$
O = \sum_{a \equiv 1 \pmod{2}} C_n^a
$$
$$
E = \sum_{a \equiv 0 \pmod{2}, a > 0} C_n^a.
$$
We can easily prove that, $O = E + 1$ and the following recursive formulas,
$$
\begin{cases}
f(m,n) = h(m,n) + O \cdot g(m-1,n) + E \cdot f(m-1,n) \\
g(m,n) = h(m,n) + O \cdot f(m-1,n) + E \cdot g(m-1,n).
\end{cases}
$$
Consequently,
$$
\begin{aligned}
f(m,n) - g(m,n) &= (L-C)(g(m-1,n) - f(m-1,n)) \\
&= g(m-1,n) - f(m-1,n) = \dots \\
&= (-1)^{m+n-4}(f(2,2) - g(2,2)) \\
&= (-1)^{m+n-4}(3-4) = (-1)^{m+n-3}.
\end{aligned}
$$

This implies that the numbers of two types of representations differ not exceeding $1$ so that the arrangement as shown in the problem is always possible.

