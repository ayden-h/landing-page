# esp_2013_8adf5f

IMO | Spain | 2013 |  | 6

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [esp_2013_8adf5f](https://mathnet.mit.edu/data_v2/full/spain/esp_2013_8adf5f.json.gz)

**Rights:** MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata.

- Source: Spain
- Title: OLIMPIADA MATEMÁTICA
- Subtitle: ACTIVIDADES 2013
- Year: 2013
- Authors: Alonso-Vega, María Gaspar; Díaz Barrero, José Luis
- Organization: REAL SOCIEDAD MATEMÁTICA ESPAÑOLA
- Publisher: REAL SOCIEDAD MATEMÁTICA ESPAÑOLA
- Language: Spanish

**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**

## Supplied solution 1

Antes de empezar, nótese que si $x + y = n$, y $\text{mcd}(x, y) = 1$, entonces $\text{mcd}(x, n) = \text{mcd}(y, n) = 1$, ya que si por ejemplo $\text{mcd}(x, n) = d > 1$, entonces $y = n - x$ es divisible por $d$, luego $\text{mcd}(x, y) \ge d$, contradicción. Recíprocamente, si una de entre $\text{mcd}(x, n) = 1$ o $\text{mcd}(y, n) = 1$ es cierta, entonces la otra también se cumple, siendo además $\text{mcd}(x, y) = 1$. Luego como el par es ordenado, $x$ puede tomar exactamente cualquiera de los valores enteros positivos menores que $n$ que son primos con $n$, y llamando $M_n$ y $N_n$ a los valores respectivos de $M$ y $N$, una vez fijado $n$, se tiene que $N_n = N_{n-1} + \varphi(n)$, donde $\varphi(n)$ denota a la función de Euler, es decir, al número de enteros positivos menores que $n$, y que son primos con $n$. Luego basta con demostrar que $M_3 = N_3 + 1$, y que para todo $n \ge 4$, $M_n - M_{n-1} = \varphi(n)$.

Nótese también que los $n+1$ puntos no necesitan estar equiespaciados sobre la circunferencia; la condición para que el etiquetado no sea bonito, es equivalente a que existan etiquetas $a < b < c < d$ con $a + d = b + c$, y tales que las etiquetas $a, d$ estén cada una en uno de los dos arcos delimitados por los puntos con etiquetas $b, c$, o equivalentemente que las etiquetas $b, c$ estén cada una en uno de los dos arcos delimitados por los puntos con etiquetas $a, d$. Nótese también que, para eliminar la posibilidad de tomar como distintos dos etiquetados que sean el mismo salvo una rotación, nos basta con definir los etiquetados recorriendo la circunferencia en el sentido de las agujas del reloj, empezando siempre por el punto con etiqueta 0, e ir enunciando sucesivamente las etiquetas que vayamos encontrando, y así será como lo hagamos en esta solución.

Sea un etiquetado bonito para un cierto $n$ dado. Entonces, eliminando la etiqueta $n$, nos queda un etiquetado bonito para $n-1$. En efecto, si no fuera así, existirían cuatro etiquetas $a < b < c < d$ con $a+d = b+c$, y tales que $a, d$ están cada una en uno de los dos arcos delimitados por los puntos con etiquetas $b, c$, y reponiendo la etiqueta $n$, la situación relativa de las etiquetas $a, b, c, d$ no ha cambiado, luego el etiquetado inicial no sería bonito. Recíprocamente, todo etiquetado bonito para $n$ se puede obtener de la siguiente manera: tomamos todos los etiquetados bonitos para $n-1$, y probamos para cada uno de ellos, todas las posiciones entre dos etiquetas distintas, en las que podemos insertar $n$, y para cada terna de etiquetas $a < b < c$ tales que $b+c-a = n$, comprobamos si $n, a$ están en el mismo arco delimitado por los puntos con etiquetas $b, c$. Si esto es así para todas tales ternas, hemos encontrado un etiquetado bonito, en caso contrario, $n$ no puede estar en esa posición para un etiquetado bonito. Cuando hayamos agotado todas las posiciones de $n$ en todos los etiquetados bonitos para $n-1$, habremos encontrado todos los etiquetados bonitos para $n$.

Nótese ahora que $N_3 = 3$ porque $(1,1)$ es el único par ordenado $(x,y)$ de enteros positivos coprimos tales que $x+y=2$, y $(1,2)$ y $(2,1)$ son los únicos pares ordenados tales que $x+y=3$. Al mismo tiempo, ningún etiquetado para $n=3$ puede ser de la forma $0, a, 3, b$, pues $a+b=1+2=3$, mientras que se comprueba fácilmente que $0, 1, 2, 3$, $0, 2, 1, 3$, $0, 3, 1, 2$ y $0, 3, 2, 1$, que son todos los posibles etiquetados de la forma $0, 3, a, b$ o $0, a, b, 3$, son todos bonitos. Luego $M_3 = 4 = 3+1 = N_3 + 1$, y nos basta con demostrar que, para todo $n \ge 4$, $M_n - M_{n-1} = \varphi(n)$.

Apoyándonos entonces en el estudio de los etiquetados bonitos para $n=4, 5, 6$ (que omitimos por brevedad en esta solución pero que el lector puede reproducir sin gran dificultad), formulamos la siguiente conjetura, que de ser probada, concluiría el problema: para $n-1$, existen $\varphi(n)$ etiquetados, que llamaremos *muy bonitos*, tales que $n$ puede ser introducido en exactamente dos posiciones distintas para formar un etiquetado bonito para $n$, y para todos los demás etiquetados bonitos para $n-1$, existe exactamente una posición en la que se puede insertar $n$ para formar un etiquetado bonito para $n$.

**Lema.** Sea $r \in \{1, 2, \dots, n-1\}$ tal que $r, n$ son coprimos. Entonces, asignando las etiquetas que dan los mismos restos al dividir entre $n$ que $0, r, 2r, 3r, \dots, (n-1)r$ y en este mismo orden, se obtiene un etiquetado muy bonito para $n-1$, donde $n$ puede ser insertado tanto antes, como después del 0, para obtener un etiquetado bonito para $n$, pero en ninguna otra posición.

**Demostración.** Por ser $r, n$ coprimos, claramente los restos al dividir $ur, vr$ entre $n$ son distintos cuando $u \neq v$, pues para que dos sean iguales, $n$ ha de dividir a $(u-v)r$, y al ser primo con $r$, ha de dividir a $u-v$, cuyo valor absoluto es no nulo y a lo sumo $n-1$, contradicción. Supongamos que el etiquetado así hallado no es bonito para $n-1$. Entonces, existen dos pares de etiquetas con igual suma, y tales que las cuerdas que unen sus correspondientes puntos se cortan dentro de la circunferencia. Comenzando desde 0, recorremos la circunferencia en el sentido de las agujas del reloj hasta encontrar la primera, que da el mismo resto al dividir entre $n$ que $tr$, y continuamos hasta encontrar las siguientes, que dan los mismos restos respectivamente que $ur, vr, wr$, con lo que los restos de $tr, vr$ han de sumar lo mismo que los restos de $ur, wr$, es decir, $r(t+v) \equiv r(u+w) \pmod{n}$. Pero como $n, r$ son coprimos, ha de ser $t+v \equiv u+w \pmod{n}$. Pero por la forma en la que se han asignado las etiquetas, es $t < u < v < w$, y al ser $t, u, v, w \in \{0, 1, 2, \dots, n-1\}$, es $0 < t+v < u+w < 2n$, y ha de ser $t+v \in \{0, 1, \dots, n-1\}$ y $u+w = t+v+n$. Pero entonces $0 < n-w = -t-(v-u) < 0$, contradicción. Luego en efecto el etiquetado $0, r, 2r, \dots, (n-1)r$ es bonito.

Supongamos que añadimos ahora, al etiquetado bonito para $n-1$ anterior, una etiqueta $n$ en alguna posición que no sea la primera o la última. Entonces, entre $r$ y $(n-1)r$ está el 0 y ninguna otra etiqueta, pero los restos módulo $n$ de $r$, $(n-1)r$ son positivos, menores que $n$, y al ser $r+(n-1)r \equiv 0 \pmod{n}$, han de sumar $n$, y el segmento que los une claramente corta al segmento que une las etiquetas $0, n$, y tal etiquetado nunca puede ser bonito. Supongamos que añadimos entonces $n$ en la última posición, es decir, consideremos el etiquetado $0, r, 2r, \dots, (n-1)r, n$. Si este etiquetado no es bonito, y como antes de añadir la etiqueta $n$ el etiquetado sí era bonito, entonces existen etiquetas $tr, ur, vr$ tales que $n+ur \equiv tr+vr \pmod{n}$ con $0 \le t < u < v \le n-1$, luego al ser $r$ coprimo con $n$, ha de ser $u \equiv t + v \pmod{n}$, y como $u < v$, y $t + v < 2n$, es $t + v = u + n$. Pero $n > v$ y $u > t$, contradicción, luego este etiquetado sí es bonito. De forma análoga, se comprueba que también es bonito el etiquetado $0, n, r, 2r, ..., (n-1)r$, pues si 0 no forma parte de las cuatro etiquetas, existen $1 \le u < v < w \le n-1$ tales que $n + vr \equiv ur + wr$, con llegada a una contradicción como en el caso anterior, mientras que si 0 sí es una de las etiquetas implicadas, se tendría que existen $1 \le v < w \le n-1$ tales que $0 + vr \equiv n + wr \pmod{n}$, con lo que $v \equiv w \pmod{n}$, claramente imposible.

Hemos demostrado entonces que el etiquetado $0, r, 2r, ..., (n-1)r$ es muy bonito para $n-1$ cuando $r$ es coprimo con $n$, luego existen exactamente $\varphi(n)$ tales etiquetados muy bonitos para $n-1$, cada uno de los cuales genera exactamente dos etiquetados muy bonitos para $n$.

Y ahora faltaría demostrar que el resto de etiquetados bonitos para $n - 1$, cada uno de ellos genera exactamente un etiquetado bonito para $n$.

Nota: Los etiquetados bonitos para $n = 4$ son
$$
\begin{array}{lll}
0, 1, 2, 3, 4; & 0, 2, 4, 1, 3; & 0, 3, 2, 1, 4; \\
0, 3, 1, 4, 2; & 0, 4, 1, 2, 3; & 0, 4, 3, 2, 1.
\end{array}
$$
Nótese que el primero, segundo, cuarto y sexto se corresponden a etiquetados muy bonitos con $r = 1, 2, 3, 4$ respectivamente (todos coprimos con 5). Todos provienen de etiquetados muy bonitos para $n = 3$, salvo el segundo y el cuarto, que provienen de los etiquetados bonitos pero no muy bonitos $0, 2, 1, 3$ y $0, 3, 1, 2$.

Para $n = 5$, los etiquetados bonitos son
$$
\begin{array}{llll}
0, 1, 2, 3, 4, 5; & 0, 2, 4, 1, 3, 5; & 0, 3, 1, 4, 2, 5; & 0, 3, 2, 5, 1, 4; \\
0, 4, 1, 5, 2, 3; & 0, 4, 3, 2, 1, 5; & 0, 5, 1, 2, 3, 4; & 0, 5, 2, 4, 1, 3; \\
& 0, 5, 3, 1, 4, 2; & 0, 5, 4, 3, 2, 1;
\end{array}
$$
Sólo son muy bonitos el primero y el último, para $r = 1, 5$ respectivamente, pues $2, 3, 4$ no son coprimos con 6. Los únicos que no provienen de etiquetas muy bonitos para $n = 4$ son el cuarto y el quinto.

