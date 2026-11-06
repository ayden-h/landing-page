# jpn_2025_efabb8

JMO | Japan | 2025 | FIRST ROUND | 11

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2025_efabb8](https://mathnet.mit.edu/data_v2/full/japan/jpn_2025_efabb8.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Japan
- Title: The 35th Japanese Mathematical Olympiad
- Year: 2025
- Organization: The Mathematical Olympiad Foundation of Japan
- Publisher: The Mathematical Olympiad Foundation of Japan
- Series: Japan Mathematical Olympiad
- Volume: 35
- Issue: The First Round • The Final Round
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Let the initial configuration be called state $0$, and for each integer $n \ge 1$, let state $n$ denote the configuration after the $n$-th operation.

**Lemma 1.** There exists an assignment of every star into exactly one of groups $0$, $1$, or $2$ such that:
(1) Star $O$ is assigned to group $0$.
(2) For every flight $f$, the star $S_f$ belongs to the same group as the arrival star of $f$.
(3) For every flight $f$, if the departure star of $f$ lies in group $i$, then its arrival star lies in group $i + 1$ (where group $3$ is identified with group $0$).

**Proof of Lemma 1.** In state $0$, assign the five stars $O$, $A$, $B$, $C$, $D$ to groups $0$, $1$, $2$, $1$, $2$, respectively. Now assume inductively that every star in states $0$, $1$, ..., $n$ has already been assigned to a group satisfying conditions (1)-(3). To extend the assignment to state $n + 1$, proceed as follows:
* For each flight $f$ in state $n$, assign the new star $S_f$ to the same group as the arrival star of $f$. This guarantees condition (2) in the new state.
* To check condition (3), consider any flight $S_f \to S_{f'}$ that appears in state $n+1$. By construction this means the arrival star of $f$ coincides with the departure star of $f'$. If $S_f$ lies in group $i$, then its arrival star is in group $i$, so by the induction hypothesis the arrival star of $f'$ (hence $S_{f'}$) must lie in group $i+1$.
This completes the inductive step, and hence the proof. ■

Using Lemma 1, partition all stars into the three groups. For any star $S$, we define $g(S) \in \{0, 1, 2\}$ such that $S$ belongs to group $g(S)$. Moreover, we set $d_0 = 2$, $d_1 = 2$, $d_2 = 1$. For any integer $k$, define $d_k = d_r$, where $r$ is the remainder when $k$ is divided by $3$.

**Lemma 2.** For any star $S$, the number of outgoing flights from $S$ is $d_{g(S)}$.

**Proof of Lemma 2.** We argue by induction on $n$, where $S$ is a star in state $n$. The base $n=0$ holds by inspection. Assume the claim for state $k$, and let $f$ be any flight in state $k$, arriving at some star $T$. Then the number of flights departing from $S_f$ in state $k+1$ equals $d_{g(T)}$, which is the number of flights departing from $T$ in state $k$. Since $g(S_f) = g(T)$, this completes the induction. ■

**Lemma 3.** For each nonnegative integer $n$ and each integer $i$, all stars in state $n$ that lie in group $i$ have the same importance, say $v_{n,i}$.

**Proof of Lemma 3.** We proceed by induction on $n$. The claim is clear for $n=0$. Suppose it holds for $n=k$. Let $f$ be any flight in state $k$, departing from a star $T_1$ and arriving at a star $T_2$. Then we have
$$
\text{importance}(S_f) = v_{k,g(T_1)} + v_{k,g(T_2)} = v_{k,g(S_f)-1} + v_{k,g(S_f)}.
$$

From Lemma 3 we have the recurrence $v_{n+1,i} = v_{n,i-1} + v_{n,i}$. Let $V_n = \sum_{j=0}^{2} v_{n,j}$. Then, we have $V_{n+1} = 2V_n$ with $V_0 = 2$, so $V_n = 2^{n+1}$. Moreover, it follows that
$$
v_{n+1,i} = 2^{n+1} - v_{n,i+1},
$$
and therefore
$$
v_{n+3,i} = 2^{n+3} - 2^{n+2} + 2^{n+1} - v_{n,i+3} = 3 \cdot 2^{n+1} - v_{n,i}.
$$
Thus, we have
$$
\begin{aligned}
v_{100,2} &= (v_{100,2} + v_{97,2}) - (v_{97,2} + v_{94,2}) + (v_{94,2} + v_{91,2}) - \cdots + (v_{4,2} + v_{1,2}) - v_{1,2} \\
&= 3 \cdot 2^{98} - 3 \cdot 2^{95} + 3 \cdot 2^{92} - \cdots + 3 \cdot 2^2 - (v_{0,1} + v_{0,2}) \\
&= 3 \cdot \frac{2^{101} + 4}{9} - 2 \\
&= \frac{2^{101} - 2}{3}.
\end{aligned}
$$

Next, let $s_{n,i}$ be the number of stars in state $n$ lying in group $i$. Since each new star in state $n+1$ corresponds to a flight departing from a star in group $i-1$, Lemma 2 yields
$$
s_{n+1,i} = d_{i-1} s_{n,i-1}.
$$
In particular one finds
$$
s_{n+3,i} = d_{i-1} d_{i-2} d_{i-3} s_{n,i} = 4 s_{n,i}.
$$
With $s_{0,0} = 1$, $s_{0,1} = s_{0,2} = 2$, this gives
$$
s_{100,0} = s_{100,1} = 2^{67}, \quad s_{100,2} = 2^{68}.
$$
Finally, the total importance in state $100$ is
$$
\begin{aligned}
s_{100,0} \cdot v_{100,0} + s_{100,1} \cdot v_{100,1} + s_{100,2} \cdot v_{100,2} &= 2^{67}(v_{100,0} + v_{100,1} + 2v_{100,2}) \\
&= 2^{67}(V_{100} + v_{100,2}) \\
&= 2^{67} \left( 2^{101} + \frac{2^{101} - 2}{3} \right) \\
&= \frac{2^{68}(2^{102} - 1)}{3}.
\end{aligned}
$$

