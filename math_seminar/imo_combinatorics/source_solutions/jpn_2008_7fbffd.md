# jpn_2008_7fbffd

JMO | Japan | 2008 | First Stage | 10

**Scope:** pipeline_supplement. **Review:** source text not independently verified.

**Source:** [jpn_2008_7fbffd](https://mathnet.mit.edu/data_v2/full/japan/jpn_2008_7fbffd.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Japan
- Title: Japan Mathematical Olympiad
- Subtitle: The 18 Japanese Mathematical Olympiad: The First Round, The Final Round And The 6 Japanese Junior Mathematical Olympiad
- Year: 2008
- Organization: The Mathematical Olympiad Foundation of Japan
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

$[2^{251} + 2^{502} + 2^{1004} + 2^{2008}]$

Let us call the situation the [initial state] if every participating boy has a bouquet of flowers and every participating girl has a chocolate bar, and call the situation the [good state] if every participating boy has a chocolate bar and every participating girl has a bouquet of flowers.

Suppose the good state was attained for the first time after $d$ actions, then after $2d$ actions, the situation returns for the first time to the initial state. This is because the good state represents the situation in which the possessions of boys and girls are completely reversed from those in the initial state, and therefore, if we repeat once more the process of reversing the possessions of boys and girls completely, it is clear that the situation returns to the initial state. Furthermore, if for some $d' < 2d$ the situation returned to the initial state after $d'$ actions, then this would mean that after $|d-d'|$ actions the initial state and the good state were interchanged, and since $|d-d'| < d$, this is a contradiction. So, $2d$ is exactly the number of actions necessary to return to the initial state for the first time. Let us prove the following Lemma

**Lemma.** Suppose after $a$ actions the situation returns for the first time to the initial state. If the situation returns to the initial state after $b$ actions, then $b$ must be a multiple of $a$.

**Proof of Lemma** $b$ can be represented as $b = ma + k$ with a nonnegative integer $m$ and a number $k$ satisfying $0 \le k < a$. From the definition of $a$ it follows that the situation returns to the initial state after $ma$ actions. Consequently, after $b$ actions the situation is the same as the situation reached after $k$ actions from the initial state. If $k > 0$, then this would mean that the situation returns to the initial state in less than $a$ actions, and this contradicts the fact that $a$ was assumed to be the number of actions necessary to return for the first time to the initial state. Therefore, we must have $k = 0$, and this proves the Lemma.

From what we obtained above, we see that the situation returns to the initial state after the repetition of even multiples of $d$ actions, and goes into the good state after an odd multiples of $d$ actions. Furthermore, in view of the Lemma, we see that at no other time the initial state or the good state would be attained.

Since there are altogether $4016$ people participating, it is clear that after $4016$ actions, the situation returns to the initial state. Therefore, $2d$ must be a factor of $4016$, and this implies that $d$ must be one of the numbers

$1, 2, 4, 8, 251, 502, 1004, 2008$. We note that the good state can be reached also by going through $251$ actions if $d=1$, by $502$ actions if $d=2$, by $1004$ actions if $d=4$ and by $2008$ actions if $d=8$ respectively. By the Lemma, we see that there are no common seating arrangement among the seating arrangements corresponding to $251, 502, 1004, 2008$ as the number of actions necessary to get to the good state for the first time. Therefore, to obtain the possible number of seating arrangements to satisfy the requirement of the problem, it is enough to determine how many possible seating arrangements there are which produce the good state after $251, 502, 1004$ and $2008$ actions.

So, let $n \in \{251, 502, 1004, 2008\}$, and consider seating arrangements that will produce the good state after $n$ actions. Since the number $\frac{4016}{n}$ is an even integer, we see that if we decide the seating arrangement for some block consisting of $n$ consecutive chairs by deciding whether a boy or a girl sits in each of these $n$ chairs, then precisely $1$ seating arrangement for all the participants satisfying the requirement of the problem can be produced by putting alternately this arrangement of seating and the arrangement obtained by changing a boy by a girl and a girl by a boy in each chair to each of $\frac{4016}{n}$ distinct blocks of $n$ consecutive chairs. Therefore, there are $2^n$ seating arrangement satisfying the requirement for each $n$.

Consequently, the number of possible arrangements satisfying the requirement of the problem is

$$
2^{251} + 2^{502} + 2^{1004} + 2^{2008}
$$

