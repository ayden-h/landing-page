# apm_2010_d1fcee

APMO | Asia Pacific Mathematics Olympiad (APMO) | 2010 |  | 5

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [apm_2010_d1fcee](https://mathnet.mit.edu/data_v2/full/asia-pacific-mathematics-olympiad-apmo/apm_2010_d1fcee.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Asia Pacific Mathematics Olympiad (APMO)
- Title: SOLUTIONS FOR 2010 APMO PROBLEMS
- Year: 2010
- Series: APMO Problems
- Language: English

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

It is clear that if $f$ is a constant function which satisfies the given equation, then the constant must be $0$. Conversely, $f(x)=0$ clearly satisfies the given equation, so, the identically $0$ function is a solution. In the sequel, we consider the case where $f$ is not a constant function.
Let $t \in \mathbf{R}$ and substitute $(x, y, z)=(t, 0,0)$ and $(x, y, z)=(0, t, 0)$ into the given functional equation. Then, we obtain, respectively,
$$
\begin{aligned}
& f(f(t)+2 f(0))=f(f(t)-f(0))+f(f(0))+2 f(0), \\
& f(f(t)+2 f(0))=f(f(0)-f(t))+f(f(0))+2 f(0),
\end{aligned}
$$
from which we conclude that $f(f(t)-f(0))=f(f(0)-f(t))$ holds for all $t \in \mathbf{R}$. Now, suppose for some pair $u_1, u_2$, $f\left(u_1\right)=f\left(u_2\right)$ is satisfied. Then by substituting $(x, y, z)=\left(s, 0, u_1\right)$ and $(x, y, z)=\left(s, 0, u_2\right)$ into the functional equation and comparing the resulting identities, we can easily conclude that
$$
\begin{equation*}
f\left(s u_1\right)=f\left(s u_2\right) \tag{*}
\end{equation*}
$$
holds for all $s \in \mathbf{R}$. Since $f$ is not a constant function there exists an $s_0$ such that $f\left(s_0\right)-f(0) \neq 0$. If we put $u_1=f\left(s_0\right)-f(0), u_2=-u_1$, then $f\left(u_1\right)=f\left(u_2\right)$, so we have by $(*)$
$$
f\left(s u_1\right)=f\left(s u_2\right)=f\left(-s u_1\right)
$$
for all $s \in \mathbf{R}$. Since $u_1 \neq 0$, we conclude that
$$
f(x)=f(-x)
$$
holds for all $x \in \mathbf{R}$.
Next, if $f(u)=f(0)$ for some $u \neq 0$, then by $(*)$, we have $f(s u)=f(s 0)=f(0)$ for all $s$, which implies that $f$ is a constant function, contradicting our assumption. Therefore, we must have $f(s) \neq f(0)$ whenever $s \neq 0$.
We will now show that if $f(x)=f(y)$ holds, then either $x=y$ or $x=-y$ must hold. Suppose on the contrary that $f\left(x_0\right)=f\left(y_0\right)$ holds for some pair of non-zero numbers $x_0, y_0$ for which $x_0 \neq y_0, x_0 \neq -y_0$. Since $f\left(-y_0\right)=f\left(y_0\right)$, we may assume, by replacing $y_0$ by $-y_0$ if necessary, that $x_0$ and $y_0$ have the same sign. In view of $(*)$, we see that $f\left(s x_0\right)=f\left(s y_0\right)$ holds for all $s$, and therefore, there exists some $r>0, r \neq 1$ such that
$$
f(x)=f(r x)
$$
holds for all $x$. Replacing $x$ by $r x$ and $y$ by $r y$ in the given functional equation, we obtain
$$
\begin{equation*}
f(f(r x)+f(r y)+f(z))=f(f(r x)-f(r y))+f\left(2 r^{2} x y+f(z)\right)+2 f(r(x-y) z) \tag{i}
\end{equation*}
$$
and replacing $x$ by $r^{2} x$ in the functional equation, we get
$$
\begin{equation*}
f\left(f\left(r^{2} x\right)+f(y)+f(z)\right)=f\left(f\left(r^{2} x\right)-f(y)\right)+f\left(2 r^{2} x y+f(z)\right)+2 f\left(\left(r^{2} x-y\right) z\right) \tag{ii}
\end{equation*}
$$
Since $f(r x)=f(x)$ holds for all $x \in \mathbf{R}$, we see that except for the last term on the right-hand side, all the corresponding terms appearing in the identities (i) and (ii) above are equal, and hence we conclude that
$$
\begin{equation*}
\left.f(r(x-y) z)=f\left(\left(r^{2} x-y\right) z\right)\right) \tag{iii}
\end{equation*}
$$
must hold for arbitrary choice of $x, y, z \in \mathbf{R}$. For arbitrarily fixed pair $u, v \in \mathbf{R}$, substitute $(x, y, z)=\left(\frac{v-u}{r^{2}-1}, \frac{v-r^{2} u}{r^{2}-1}, 1\right)$ into the identity (iii). Then we obtain $f(v)=f(r u)=f(u)$, since $x-y=u, r^{2} x-y=v, z=1$. But this implies that the function $f$ is a constant, contradicting our assumption. Thus we conclude that if $f(x)=f(y)$ then either $x=y$ or $x=-y$ must hold.
By substituting $z=0$ in the functional equation, we get
$$
f(f(x)+f(y)+f(0))=f(f(x)-f(y)+f(0))=f((f(x)-f(y))+f(2 x y+f(0))+2 f(0).
$$
Changing $y$ to $-y$ in the identity above and using the fact that $f(y)=f(-y)$, we see that all the terms except the second term on the right-hand side in the identity above remain the same. Thus we conclude that $f(2 x y+f(0))=f(-2 x y+f(0))$, from which we get either $2 x y+f(0)=-2 x y+f(0)$ or $2 x y+f(0)=2 x y-f(0)$ for all $x, y \in \mathbf{R}$. The first of these alternatives says that $4 x y=0$, which is impossible if $x y \neq 0$. Therefore the second alternative must be valid and we get that $f(0)=0$.
Finally, let us show that if $f$ satisfies the given functional equation and is not a constant function, then $f(x)=x^{2}$. Let $x=y$ in the functional equation, then since $f(0)=0$, we get
$$
f(2 f(x)+f(z))=f\left(2 x^{2}+f(z)\right)
$$
from which we conclude that either $2 f(x)+f(z)=2 x^{2}+f(z)$ or $2 f(x)+f(z)=-2 x^{2}-f(z)$ must hold. Suppose there exists $x_0$ for which $f\left(x_0\right) \neq x_0^{2}$, then from the second alternative, we see that $f(z)=-f\left(x_0\right)-x_0^{2}$ must hold for all $z$, which means that $f$ must be a constant function, contrary to our assumption. Therefore, the first alternative above must hold, and we have $f(x)=x^{2}$ for all $x$, establishing our claim.
It is easy to check that $f(x)=x^{2}$ does satisfy the given functional equation, so we conclude that $f(x)=0$ and $f(x)=x^{2}$ are the only functions that satisfy the requirement.
