# jpn_2019_e2fec2

JMO | Japan | 2019 | PROBLEMS | 12

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2019_e2fec2](https://mathnet.mit.edu/data_v2/full/japan/jpn_2019_e2fec2.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Japan
- Title: The 29th Japanese Mathematical Olympiad
- Subtitle: The First Round, The Final Round
- Year: 2019
- Organization: The Mathematical Olympiad Foundation of Japan
- Publisher: The Mathematical Olympiad Foundation of Japan
- Series: Japan Mathematical Olympiad

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Let us fix $C \subset S$ and consider the situation where $F(\emptyset) = C$. If we let $A = \emptyset$ in the given identity, we get $F(C \cup B) = \emptyset$ for any set $B$ in $\mathfrak{S}$. So, if $D \supset C$ then we have $F(D) = \emptyset$. Therefore, if we let $A = C$, we get $F(B) = C \cap F(B)$, which implies that for any $B$ in $\mathfrak{S}$, $F(B) \subset C$ holds. Also, by letting $B = \emptyset$ in the given identity, we get $F(F(D)) = D \cap C$ for any set $D$ in $\mathfrak{S}$. If we substitute $D = F(A)$ in this identity, we obtain $F(F(F(A))) = F(A) \cap C = F(A)$. We also get from $F(F(A)) = A \cap C$, $F(F(F(A))) = F(A \cap C)$, and therefore, we have $F(A) = F(A \cap C)$ for any $A$. Thus, we conclude that the mapping $F: \mathfrak{S} \to \mathfrak{S}$ is determined completely by how the subsets of $C$ are mapped. Conversely, if for any pair of subsets $X, Y$ of $C$ condition
$$
(1) \qquad F(F(X) \cup Y) = X \cap F(Y)
$$
is satisfied, and for any $A \in \mathfrak{S}$ $F(A) = F(A \cap C) \subset C$, then by letting $X = A \cap C$ and $Y = B \cap C$, we get
$$
\begin{aligned}
F(F(A) \cup B) &= F((F(X) \cup B) \cap C) = F(F(X) \cup Y) \\
&= X \cap F(Y) = (A \cap C) \cap F(B) = A \cap F(B),
\end{aligned}
$$
which shows that the identity given for the problem is satisfied. Consequently, it is sufficient to consider the mapping $F: \mathfrak{S}_C \to \mathfrak{S}_C$ satisfying the condition (1), where by $\mathfrak{S}_C$ we mean the set of all subsets of $C$.
Now, if we consider such a mapping $F: \mathfrak{S}_C \to \mathfrak{S}_C$, then we have $F(F(X)) = X$ so that the mapping $F$ is bijective, and if we replace $X$ by $F(X)$ in (1), then we get
$$
(2) \qquad F(X \cup Y) = F(X) \cap F(Y).
$$
Conversely, if both $F(F(X)) = X$ and $F(X \cup Y) = F(X) \cap F(Y)$ are satisfied, then by replacing $X$ in (2) by $F(X)$, we get back the condition (1). So, from now on we consider mapping $F: \mathfrak{S}_C \to \mathfrak{S}_C$ satisfying the two conditions $F(F(X)) = X$ and $F(X \cup Y) = F(X) \cap F(Y)$.
Suppose now $X \subset Y$ is satisfied, then we get $F(X) \supset F(Y)$, since $F(Y) = F(X) \cap F(Y)$. By the injectivity of $F$, we get, in particular, that if $X \subset Y$ but $X \neq Y$, then we get $F(X) \supset F(Y)$ but $F(X) \neq F(Y)$. So, if we consider the process of transferring elements from $C \cap X^c$ to $X$ one element at every step starting with $X = \emptyset$, then the number of elements in the set $F(X)$ decreases strictly. Since we can repeat this process exactly $t$ times, where $t$ is the number of elements of $C$, every element $x \in C$, the number of elements in the set $F(\{x\})$ is larger than or equal to the number of elements in $C-1$. But since $F$ is injective, this number cannot be equal to the number of elements in $C$. Thus, we conclude that for each $x \in C$, the number of elements in the set $F(x)$ equals the number of elements of $C-1$.
Consequently, there must exist in $C$ exactly one element, which does not belong to $F(\{x\})$. Call this element $f(x)$. Then, the mapping $f: C \to C$ is injective since $F$ is and surjective since $C$ is a finite set.
Since $F(F(X)) = X$ for every $X$, by letting $X = \emptyset$, we get $F(C) = \emptyset$ and if we let $X = \{x\}$, $Y = \{f(x)\}$, then the left hand side becomes $\emptyset$, and therefore, we have $x \notin C \cap \{f(f(x))\}^c$, from which it follows that $f(f(x)) = x$ must be valid. When $X = \{x_1, \dots, x_k\}$, if we keep on applying (2), we get $F(X) = C \cap \{f(x_1), \dots, f(x_k)\}^c$, and conversely, $F$ defined by this formula satisfies the condition $F(F(X))$ and the property (2). Therefore, we can conclude that the number of functions $F$ satisfying $F(\emptyset) = C$ equals the number of functions $f: C \to C$ satisfying the property $f(f(x)) = x$.
The number of such functions $f: C \to C$ coincides with the number of ways of specifying pairs $x, y$ satisfying the property $f(x) = y$, $f(y) = x$ without repetition. In fact, for $z \in C$ left out of the pairing mentioned above, it is sufficient to let $f(z) = z$, and conversely, from every $f$ satisfying the property mentioned above, the pairing mentioned above can be achieved.
At this point, we just ignore the specification of $C$ and consider the way of counting the mappings $F$ satisfying the conditions stated above. Then, since it is not necessary to specify $C$ to start off, we can start off by forming some pairs of elements of $S$, and decide whether to make the remaining elements of $S$ to become elements of $C$ or not. To decide the number of ways of forming $k$ pairs of elements from the set containing $2k$ elements, we can line up $2k$ elements from left to right and among the elements having no partner, pick the one having the leftmost position and decide its partner and keep on doing the same until every one of $2k$ elements has a partner. Then, the number of ways this can be done is

$(2k-1)(2k-3)\dots 1$. Therefore, the answer we seek for the problem is
$$
\binom{6}{0} 2^6 + \binom{6}{2} 2^4 + \binom{6}{4} 3 \cdot 2^2 + \binom{6}{6} 5 \cdot 3 = 64 + 240 + 180 + 15 = 499
$$

