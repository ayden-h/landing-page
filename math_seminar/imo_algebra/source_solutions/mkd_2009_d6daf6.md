# mkd_2009_d6daf6

BMO | North Macedonia | 2009 | III година | 3Б.

**Scope:** contest. **Review:** source text not independently verified.

**Source:** [mkd_2009_d6daf6](https://mathnet.mit.edu/data_v2/full/north-macedonia/mkd_2009_d6daf6.json.gz)

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

Не е тешко да се провери точноста на следното равенство
$$
\operatorname{ctg} \alpha - \operatorname{tg} \alpha = 2 \operatorname{ctg} 2\alpha. \qquad (1)
$$
Навистина
$$
\operatorname{ctg} \alpha - \operatorname{tg} \alpha = \frac{\cos \alpha}{\sin \alpha} - \frac{\sin \alpha}{\cos \alpha} = 2 \frac{\cos^2 \alpha - \sin^2 \alpha}{2 \cos \alpha \sin \alpha} = 2 \frac{\cos 2\alpha}{\sin 2\alpha} = 2 \operatorname{ctg} 2\alpha.
$$
Равенството (1) може да се трансформира во облик
$$
\operatorname{tg} \alpha = \operatorname{ctg} \alpha - 2 \operatorname{ctg} 2\alpha. \qquad (2)
$$
Сега
$$
2 \operatorname{tg} 2\alpha = 2 \operatorname{ctg} 2\alpha - 4 \operatorname{ctg} 4\alpha
$$
$$
2^2 \operatorname{tg} 2\alpha = 4 \operatorname{ctg} 4\alpha - 2^3 \operatorname{ctg} 2^3 \alpha
$$
$$
2^3 \operatorname{tg} 2\alpha = 2^3 \operatorname{ctg} 4\alpha - 2^4 \operatorname{ctg} 2^4 \alpha
$$
$$
2^n \operatorname{tg} 2\alpha = 2^n \operatorname{ctg} 2^n \alpha - 2^{n+1} \operatorname{ctg} 2^{n+1} \alpha
$$
Ако ги собереме претходните равенство (2) го добиваме бараното равенство
$$
\operatorname{tg} \alpha + 2 \operatorname{tg} 2\alpha + 2^2 \operatorname{tg} 2^2 \alpha + \dots + 2^n \operatorname{tg} 2^n \alpha = \operatorname{ctg} \alpha - 2^{\eta+1} \operatorname{ctg} 2^{\eta+1} \alpha.
$$
