# mkd_2009_c6e2af

BMO | North Macedonia | 2009 |  | 3.

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [mkd_2009_c6e2af](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_c6e2af.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: North Macedonia
- Title: Натпревари по математика 2009
- Year: 2009
- Editors: Maneva-Erakovic, Vesna; Malcheski, Risto; Nastovski, Ljupco; Pachemska, Tatjna; Saneva, Katerina; Gegovska-Zajkova, Sonja; Miovska, Valentina; Brsakoska, Slagjana; Stojkovska, Irena; Hadzieva, Elena; Markovski, Gjorgji; Anova, Vesna; Gogovska, Valentina; Leschkovski, Delcho; Gacovska, Aneta; Trifunov, Zoran; Cvetkovski, Zdravko; Petruschevski, Mirko; Prangoski, Bojan; Jovchevski, Ilija; Samardziska, Simona; Dimovski, Pavel; Shoptrajanov, Martin; Misajlevski, Zoran; Sokoloski, Petar; Velinov, Daniel; Petrovski, Zlatko; Malcheski, Aleksa
- Organization: Macedonian Mathematical Society
- Publisher: Macedonian Mathematical Society
- Place: Skopje
- Language: Macedonian, English
- Isbn: 987-9989-646-07-2

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

We'll prove that the total number of possible schedules is an even number so it can't be equal to $2009$. It is enough to prove that there exists a list of names of some of the contestants such that all the contestants in room $1$ go to room $2$ (if this is possible then for every possible final schedule the reverse schedule is also possible, so all the final schedules can be paired).

We use induction on $n$, where $n$ is the number of contestants.

For $n=1$ the claim is obvious.

Let the claim is true for $n$ contestants. For $n+1$ contestants we have: for every $n$ among them there is a list of names such that all the contestants among those $n$ go from room $1$ to room $2$. If for any such list and the remaining $n+1$-th contestant moves to room $2$ then the claim is true. So let us assume that for every contestant there is so called his "good list" such that with it all other $n$ contestants move to room $2$ and he remains in room $1$. We will consider two cases:

i) $n$ is odd; then with the list formed of all $n+1$ "good lists", all contestants move to room $2$.

ii) $n$ is even; then among the $n+1$ contestants there exists at least one with even number of friends. We put his name first on the new formed list. After reading his name there are odd number of contestants in room $2$. After that we add the "good lists" of those contestants to the new list. Now the new list satisfies the condition.

