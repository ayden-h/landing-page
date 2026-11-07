---
title: "Olympiad Geometry: Worked Solutions"
author: "Ayden Bi"
date: "Research edition • 6 November 2026"
lang: en-US
---

# Reading this volume {.unnumbered}

Sixteen selected problems supply the checked core of this research edition. They are chosen to expose reusable mechanisms, not advertised as a statistically established list of the hardest problems. All are IMO shortlist problems; G10 also appeared as IMO 2017 Problem 4. The source archive contains many additional contests and team-selection records, with their verification status stated separately.

The notation $(ABC)$ means the circumcircle of three noncollinear points. Unless ordinary interior angles are explicitly used, angle equalities are modulo $180^\circ$. A second intersection and the circle it defines are assumed to exist as in the problem; coincident or tangent limiting configurations are not silently substituted for a stated distinct intersection. The diagrams in the companion volume are schematic illustrations of proved mechanisms, not additional hypotheses.

# G01. Two similarities sharing a secant

**Source:** IMO shortlist 2015, G1. **Record:** `imo_2015_29f541`.

**Problem.** In an acute triangle $ABC$ with orthocenter $H$, complete the parallelogram $ABGH$. On line $GH$ choose $I$ so that $AC$ passes through the midpoint of $HI$. Let $J\ne C$ be the other intersection of $AC$ with $(GCI)$. Prove $IJ=AH$.

**Solution.** Write $M=AC\cap GH$, so $MI=MH$. Since $BG\parallel AH\perp BC$ and $GH\parallel AB\perp CH$, the quadrilateral $BGCH$ is cyclic. Hence
$$\angle CGH=\angle CBH=\angle HAC.$$
Together with $BG\parallel AH$ and $GH\parallel AB$, this shows that the right triangles $CMH$ and $CGB$ are similar: their right angles are at $H$ and $B$, and the angle between $MC$ and $MH$ equals that between $GC$ and $GB$. Therefore $MH/MC=GB/GC$.

The secants $MCJ$ and $MIG$ of $(GCI)$ give similar triangles $MIJ$ and $MCG$, so $IJ/CG=MI/MC$. Combining the two ratios yields
$$\frac{IJ}{CG}=\frac{MI}{MC}=\frac{MH}{MC}=\frac{GB}{GC}=\frac{AH}{CG}.$$
Thus $IJ=AH$.

**Certificate.** The same intermediate ratio connects a secant similarity to an orthocenter similarity.

# G02. Reflect the two lines

**Source:** IMO shortlist 2015, G2. **Record:** `imo_2015_7c01e3`.

**Problem.** Triangle $ABC$ lies on a circle $\Omega$ with center $O$. A circle centered at $A$ cuts $BC$ at $D,E$ in the order $B,D,E,C$, and cuts the arcs $AB$ and $AC$ of $\Omega$ not containing the third vertex at $F,G$, respectively. Let $K\ne B$ be the intersection of $AB$ with $(BDF)$, and $L\ne C$ the intersection of $AC$ with $(CEG)$. If distinct lines $FK,GL$ meet at $X$, prove $A,X,O$ collinear.

**Solution.** The common chord $FG$ of the two original circles is perpendicular to their line of centers $AO$, so reflection in $AO$ exchanges $F$ and $G$. We prove that it also exchanges lines $FK$ and $GL$. Using directed angles, the three circles give
$$\begin{aligned}
\angle KFA
&=\angle DFG+\angle GFA-\angle DFK\\
&=\angle CEG+\angle GBA-\angle DBK\\
&=\angle CEG-\angle CBG\\
&=\angle CLG-\angle CAG=\angle AGL.
\end{aligned}$$
In the second line, $D,E,B,C$ are collinear; the circle centered at $A$ contains $D,E,F,G$, while $(BDF)$ contains $K$. The last line uses $(CEG)$ and $\Omega$. The angle equality is exactly the reflection criterion. Since the two lines are distinct, their intersection is fixed by the reflection and hence lies on $AO$.

**Certificate.** A concurrency conclusion on a symmetry axis can be proved by reflecting whole lines.

# G03. An angle condition is a distance locus

**Source:** IMO shortlist 2006, G1. **Record:** `imo_2006_e64448`.

**Problem.** Let $I$ be the incenter of $ABC$. An interior point $P$ satisfies $\angle PBA+\angle PCA=\angle PBC+\angle PCB$. Prove $AP\ge AI$, with equality only at $P=I$.

**Solution.** The four angles in the hypothesis sum to $B+C$. Thus $\angle PBC+\angle PCB=(B+C)/2$ and $\angle BPC=90^\circ+A/2=\angle BIC$. The points $B,C,I,P$ lie on one circle.

Let $T$ be the midpoint of the arc $BC$ not containing $A$ on $(ABC)$. Then $A,I,T$ are collinear in that order, and $TB=TC=TI$. For completeness, the first equality follows from the equal arcs, while in triangle $BIT$ the angles at $B$ and $I$ both equal $(A+B)/2$: use $\angle CBT=A/2$ and the incenter angle $\angle BIA=90^\circ+C/2$. Thus $T$ is the center of $(BCI)$.

The triangle inequality gives $AP+PT\ge AT=AI+IT$. As $PT=IT$, we obtain $AP\ge AI$. Equality requires $P$ to lie on segment $AT$. The circle has two intersections with this line; the nearer one to $A$ is $I$, and the other lies beyond $T$, outside the triangle. Therefore equality holds precisely at $I$.

**Certificate.** Identify the fixed-angle circle, then locate its center. An optimization becomes a one-line distance inequality.

# G04. Reflection completes a cyclicity proof

**Source:** IMO shortlist 2012, G2. **Record:** `imo_2012_758467`.

**Problem.** In cyclic quadrilateral $ABCD$, the diagonals meet at $E$. The extensions of $AD,BC$ beyond $A,B$ meet at $F$. Complete parallelogram $ECGD$, and reflect $E$ in $AD$ to obtain $H$. Prove $D,H,F,G$ concyclic.

**Solution.** Cyclicity gives similarities $EAB\sim EDC$ and $FAB\sim FCD$. Since $GD=EC$ and $GD\parallel EC$, we get
$$\frac{GD}{EB}=\frac{EC}{EB}=\frac{CD}{AB}=\frac{FD}{FB},
\qquad \angle FDG=\angle FBE.$$
Thus $FDG\sim FBE$, and $\angle FGD=\angle FEB$. In the ordinary interior angles of this configuration, reflection in $FD=AD$ gives $\angle FHD=\angle FED$. Since $B,E,D$ are collinear, $\angle FED=180^\circ-\angle FEB$. Consequently $\angle FHD+\angle FGD=180^\circ$, proving the required cyclicity.

**Certificate.** First obtain the angle needed at the unreflected point; reflection supplies the sign change automatically.

# G05. Reflected lines meet on the mirror

**Source:** IMO shortlist 2013, G2. **Record:** `imo_2013_22bd4a`.

**Problem.** Let $M,N$ be the midpoints of $AB,AC$, and $T$ the midpoint of the arc $BC$ not containing $A$ on $(ABC)$. The circle $(AMT)$ meets the perpendicular bisector of $AC$ at an interior point $X$ of $ABC$; similarly $(ANT)$ meets the perpendicular bisector of $AB$ at an interior point $Y$. If $K=MN\cap XY$, prove $KA=KT$.

**Solution.** We prove that reflection in the perpendicular bisector of $AT$ sends $M,N$ to $X,Y$. Use coordinates with $A=(0,0)$, the internal angle bisector as the positive horizontal axis, and
$$B=2u(c,s),\quad C=2v(c,-s),\quad c=\cos(A/2)>0,\ s=\sin(A/2)>0.$$
Here $u,v>0$, $M=(uc,us)$ and $N=(vc,-vs)$. Writing the equation of $(ABC)$ shows that its other horizontal intercept is $T=(t,0)$, where $t=(u+v)/c$.

The circle $(AMT)$ has equation $x^2+y^2-tx+(v/s)y=0$. The perpendicular bisector of $AC$ is $cx-sy=v$. Its two intersections with the circle are
$$X_0=(t-uc,us),\qquad X_1=(0,-v/s).$$
These are checked directly in both equations. The second point is outside the angle $BAC$, so the specified interior point is $X=X_0$. Similarly $Y=(t-vc,-vs)$. Thus $(x,y)\mapsto(t-x,y)$ exchanges $M,X$ and $N,Y$. It exchanges the two lines $MN$ and $XY$; their unique intersection lies on its fixed line $x=t/2$, the perpendicular bisector of $AT$. Hence $KA=KT$.

**Certificate.** A short coordinate calculation establishes the intended reflection and resolves which of two circle intersections is meant.

# G06. Double the cevians

**Source:** IMO shortlist 2014, G1. **Record:** `imo_2014_a0b822`.

**Problem.** In an acute triangle, choose $P,Q$ on $BC$ with $\angle PAB=C$ and $\angle QAC=B$. Extend $AP,AQ$ to $M,N$ so that $PM=PA$ and $QN=QA$. Show that $BM$ and $CN$ meet on $(ABC)$.

**Solution.** The triangles $ABP$ and $CAQ$ are similar, so
$$\frac{BP}{PM}=\frac{BP}{PA}=\frac{AQ}{QC}=\frac{NQ}{QC}.$$
Also $\angle BPM=B+C=\angle NQC$. Thus triangles $BPM$ and $NQC$ are similar by two sides and the included angle. Their remaining angles show that the intersection $S$ of $BM,CN$ satisfies $\angle BSC=B+C=180^\circ-A$. Equivalently, using directed angles, $\angle BSC=\angle BAC\pmod {180^\circ}$. Hence $A,B,S,C$ are concyclic. The same angle relation shows the two lines cannot be parallel, since $0<A<180^\circ$.

**Certificate.** The doubling construction preserves the side ratios needed for a second similarity.

# G07. Pack two similar triangles

**Source:** IMO shortlist 2014, G2. **Record:** `imo_2014_32e67b`.

**Problem.** Points $K,L,M$ on $BC,CA,AB$ have concurrent cevians $AK,BL,CM$. Prove that two of $ALM,BMK,CKL$ have inradii whose sum is at least the inradius $r$ of $ABC$.

**Solution.** First suppose the points are interior. Set $a=BK/KC$, $b=CL/LA$, $c=AM/MB$. Ceva gives $abc=1$. Around the cyclic list $a,b,c$ there is a transition from a value at least one to a value at most one. Relabel cyclically so $a\ge1\ge b$. Then $bc=1/a\le1$ and $ca=1/b\ge1$.

Through $M$, draw a parallel to $BC$ meeting $AC$ at $X$. The inequality $bc\le1$ is equivalent to $AM/AB\le AL/AC$, so $X$ lies on $AL$. Thus triangle $AMX$ lies inside $ALM$ and has inradius $(AM/AB)r$. Through $M$, draw a parallel to $AC$ meeting $BC$ at $Y$. The inequality $ca\ge1$ puts $Y$ on $BK$, so $BMY\subset BMK$ and its inradius is $(MB/AB)r$.

An inscribed disk in a contained triangle is a disk in the containing triangle, whose largest contained disk is its incircle. Consequently the inradii of $ALM,BMK$ have sum at least $(AM+MB)r/AB=r$. Boundary cases, if allowed, follow by continuity of triangle inradii, interpreting a degenerate triangle's inradius as zero.

**Certificate.** Ceva selects a favorable pair; homothety turns their sizes into complementary fractions.

# G08. Convert intersection ratios into half angles

**Source:** IMO shortlist 2016, G2. **Record:** `imo_2016_022acb`.

**Problem.** Let $I$ be the incenter, $M$ the midpoint of $BC$, and $D$ the foot from $I$ to $BC$. The perpendicular to $AI$ through $I$ meets $AB,AC$ at $F,E$. Let $X\ne A$ be the other common point of $(AEF)$ and $(ABC)$. Prove that $XD$ and $AM$ meet on $(ABC)$.

**Solution.** Let $Y\ne A$ be the other intersection of $AM$ with $(ABC)$. For a cyclic quadrilateral $PQRS$, if its diagonals meet at $U$, the area formula gives
$$\frac{QU}{US}=\frac{PQ\cdot QR}{PS\cdot SR},$$
with directed versions when necessary. Apply this to $ABYC$: since $BM=MC$, $BY/CY=AC/AB$. If $D'=XY\cap BC$, the corresponding formula for $XBYC$ gives
$$\frac{BD'}{D'C}=\frac{XB}{XC}\frac{AC}{AB}.$$
Angles in the two original circles show $XBF\sim XCE$, whence $XB/XC=BF/CE$. Put $\beta=B/2$, $\gamma=C/2$. Because $AI$ bisects $A$ and $EF\perp AI$, we have $FI=EI$. In triangles $BFI,CEI$, the sine rule gives
$$\frac{BF}{FI}=\frac{\sin\gamma}{\sin\beta},\qquad
\frac{CE}{EI}=\frac{\sin\beta}{\sin\gamma}.$$
Therefore
$$\frac{BD'}{D'C}=\frac{\sin2\beta}{\sin2\gamma}
\frac{\sin^2\gamma}{\sin^2\beta}
=\frac{\tan\gamma}{\tan\beta}=\frac{BD}{DC}.$$
The directed ratio is positive, so $D'$ lies inside $BC$; the ratio uniquely determines it. Hence $D'=D$, giving the required intersection $Y$.

**Certificate.** A chord-intersection ratio, one similarity, and a half-angle identity form a closed chain. No mixtilinear-circle facts are needed.

# G09. The hidden orthocenter of a pentagon

**Source:** IMO shortlist 2017, G1. **Record:** `imo_2017_e0103e`.

**Problem.** A convex pentagon $ABCDE$ satisfies $AB=BC=CD$, $\angle EAB=\angle BCD$, and $\angle EDC=\angle CBA$. Prove that $AC,BD$ and the perpendicular from $E$ to $BC$ concur.

**Solution.** Write the internal angles of the pentagon as $A,B,C,D,E$, so $A=C$ and $D=B$. Let $I$ be the intersection of the internal angle bisectors at $B,C$. Since $AB=BC$ and $BC=CD$, these bisectors are also the perpendicular bisectors of $AC,BD$. Thus $IA=IC$, $IB=ID$, $BI\perp AC$, and $CI\perp BD$.

The triangles $IAB,ICB,ICD$ are congruent by three sides. Hence $\angle IAB=C/2=A/2$ and $\angle IDC=B/2=D/2$. Thus $I$ also lies on the internal bisectors at $A,D$. Its equal distances to the five side lines, on the interior sides, show that $IE$ is the internal bisector at $E$ as well.

Let $H=AC\cap BD$. The first perpendicular relations say that $H$ is the orthocenter of triangle $BIC$, so $IH\perp BC$. It remains to put $E$ on $IH$. The angle sum gives $E=540^\circ-2B-2C$. In quadrilateral $ABIE$,
$$\angle BIE=360^\circ-C-B/2-E/2=90^\circ+B/2.$$
Since $\angle IBC=B/2$, this means $IE\perp BC$. Consequently $E,I,H$ are collinear, proving the concurrency.

**Audit note.** The extracted source contains an incorrect plus sign in its displayed pentagon angle sum. The correct sum is used above.

# G10. A half-turn creates the tangent

**Source:** IMO 2017, Problem 4; shortlist G2. **Record:** `imo_2017_bb6ddb`.

**Problem.** Points $R,S$ lie on $\Omega$, and $R'=2S-R$. Let $I$ lie on the smaller arc $RS$. The circle $\Gamma=(ISR')$ meets the tangent to $\Omega$ at $R$ twice; call the nearer intersection to $R$ point $A$. If $AI$ meets $\Omega$ again at $J$, prove $JR'$ tangent to $\Gamma$.

**Solution.** Let $A'=2S-A$. Thus $ARA'R'$ is a parallelogram. The two circles and the collinearity $A,I,J$ give
$$\angle JRS=\angle JIS=\angle AR'S.$$
As $R,S,R'$ are collinear, this implies $RJ\parallel AR'$, so $R,J,A'$ are collinear. Since $R'A'\parallel RA$ and $RA$ is tangent to $\Omega$,
$$\angle SR'A'=\angle SRA=\angle SJR.$$
Thus $S,J,A',R'$ lie on a circle. It follows that
$$\angle SR'J=\angle SA'J=\angle SA'R=\angle SAR'.$$
This is the tangent–chord criterion for line $JR'$ at the point $R'$ of $\Gamma$, as required. The designated nearer intersection is the one satisfying the stated ordinary configuration; the directed-angle argument avoids imposing an additional diagram order.

**Certificate.** Reflect the difficult point through the given midpoint. A tangent claim becomes a cyclic quadrilateral.

# G11. Two tangents encode a reflection

**Source:** IMO shortlist 2019, G1. **Record:** `imo_2019_be46cd`.

**Problem.** A circle through $A$ meets $AB,AC$ again at $D,E$ and crosses $BC$ at $F,G$ in that order. Tangents at $F$ to $(BDF)$ and at $G$ to $(CEG)$ meet at $T\ne A$. Prove $AT\parallel BC$.

**Solution.** The tangent–chord theorem and the first circle give, in directed form,
$$\angle(TF,BC)=\angle(BC,GA),\qquad
\angle(TG,BC)=\angle(BC,FA).$$
To make the resulting reflection explicit, scale coordinates so $F=(0,0)$, $G=(1,0)$, and $A=(u,v)$ with $v\ne0$. The first angle identity makes the direction of $FT$ proportional to $(1-u,v)$, and the second makes the direction of $GT$ proportional to $(-u,v)$. Their intersection is $T=(1-u,v)$. Hence $A$ and $T$ have the same nonzero height above $BC$; since they are distinct, $AT\parallel BC$.

**Certificate.** Two reversed angle relations identify a reflection in the perpendicular bisector of $FG$. The coordinate finish records the correct side of the line.

# G12. Close two circles around the target point

**Source:** IMO shortlist 2021, G1. **Record:** `imo_2021_18d688`.

**Problem.** In parallelogram $ABCD$, assume $AC=BC$. Take $P$ beyond $B$ on $AB$. Let $Q\ne D$ be the intersection of $PD$ with $(ACD)$, and $R\ne P$ the intersection of $PC$ with $(APQ)$. Prove $CD,AQ,BR$ concurrent.

**Solution.** We have $AC=BC=AD$, so $\angle ABC=\angle BAC=\angle ACD=\angle ADC$. Using $(APQR)$ and $(AQCD)$ gives
$$\angle CRA=\angle CBA\pmod {180^\circ}.$$
Thus $A,B,C,R$ lie on a circle. Set $X=AQ\cap CD$. Since $AB\parallel CD$, angles in $(APQR)$ give
$$\angle RQX=\angle RCX\pmod {180^\circ},$$
so $C,Q,R,X$ are concyclic. Now use these two new circles and the original one:
$$\angle XRC=\angle XQC=-\angle CQA=\angle ADC
=\angle BAC=-\angle CRB\pmod {180^\circ}.$$
It follows that $X,R,B$ are collinear, so $X$ is the desired concurrency point.

**Certificate.** Define the intended intersection first. Two auxiliary cyclicities force the last line through it.

# G13. A circle equation linearizes the ratio

**Source:** IMO shortlist 2015, G4. **Record:** `imo_2015_b11e64`.

**Problem.** In an acute triangle $ABC$, let $M$ be the midpoint of $AC$. A circle through $B,M$ meets $BA,BC$ again at $P,Q$. Complete parallelogram $BPTQ$, and assume $T\in(ABC)$. Determine $BT/BM$.

**Solution.** Put $B$ at the vector origin, write $A=\mathbf a$, $C=\mathbf c$, $P=p\mathbf a$, $Q=q\mathbf c$, so $M=(\mathbf a+\mathbf c)/2$ and $T=p\mathbf a+q\mathbf c$. Every circle through the origin has equation $|\mathbf x|^2=\mathbf u\cdot\mathbf x$ for a fixed vector $\mathbf u$.

For $(ABC)$, $\mathbf u\cdot\mathbf a=|\mathbf a|^2$ and $\mathbf u\cdot\mathbf c=|\mathbf c|^2$. Hence
$$BT^2=p|\mathbf a|^2+q|\mathbf c|^2.$$
For $(BPQM)$ the corresponding vector $\mathbf v$ satisfies $\mathbf v\cdot\mathbf a=p|\mathbf a|^2$ and $\mathbf v\cdot\mathbf c=q|\mathbf c|^2$. Therefore
$$BM^2=\tfrac12(p|\mathbf a|^2+q|\mathbf c|^2)=BT^2/2.$$
The only possible ratio is $\sqrt2$.

It is attainable with all intersections interior to the sides. Take $BA=BC=1$, $\cos B=3/8$, and $p,q=(55\pm\sqrt{385})/80$, both in $(0,1)$. Then $p+q=11/8$ and $pq=33/80$. Direct substitution gives $|M|^2=11/16=(p+q)/2$ and $|T|^2=(p+q)^2-2(1-3/8)pq=p+q$, exactly the two circle conditions. The isosceles triangle is acute. Thus the full answer is $\sqrt2$.

**Certificate.** The quadratic part of every circle equation is identical. Evaluating at a linear combination turns geometry into a linear identity.

# G14. Transfer a tangent through equal powers

**Source:** IMO shortlist 2015, G6. **Record:** `imo_2015_d499b1`.

**Problem.** An acute triangle $ABC$ has $AB>AC$, orthocenter $H$, base midpoint $M$, and altitude foot $F$ on $BC$. On its circumcircle $\Omega$, choose $Q,K$ so that $\angle AQH=\angle QKH=90^\circ$. Prove that $(KQH)$ and $(KFM)$ are tangent at $K$.

**Solution.** Let $A'$ be the antipode of $A$ on $\Omega$, and let $E$ be the reflection of $H$ in $BC$. The standard orthocenter reflection argument puts $E$ on $\Omega$: reflection changes $\angle BHC=180^\circ-A$ into the inscribed angle on the opposite side of $BC$. Also $BH\parallel CA'$ and $CH\parallel BA'$, so $BHCA'$ is a parallelogram and $H,M,A'$ are collinear. Since $AQ\perp HQ$ and $AQ\perp A'Q$ (the angle in a semicircle), $H,Q,A'$ are collinear. The lines $HA'$ and $HQ$ thus coincide.

Furthermore $EA'\parallel BC$, since $A'=2M-H$ and $E$ is the reflection of $H$ in $BC$. Hence $\angle HEA'=90^\circ$. The circles $\omega_1=(KQH)$ and $\omega_2=(EA'H)$ have diameters $HQ$ and $HA'$; their common tangent at $H$, denoted $t$, is perpendicular to $HM$.

Let $R=QK\cap A'E$. These lines are the radical axes of $\Omega$ with $\omega_1,\omega_2$. Therefore $R$ is on their mutual radical axis $t$. This intersection is finite: $A'E\parallel BC$, while $t\parallel BC$ would force $HM\perp BC$, contradicting $AB>AC$.

Since $\angle HKR=\angle HER=90^\circ$, points $H,K,E,R$ lie on the circle with diameter $HR$. Its center $S$, the midpoint of $HR$, satisfies $SK=SH=SE$. Thus $S$ lies on the perpendicular bisector of $HE$, which is $BC$. It also lies on $t$.

The circle $(HMF)$ has diameter $HM$, so its tangent at $H$ is again $t$. Directed powers along $BC$ give
$$\operatorname{Pow}_{(KFM)}(S)=\overline{SM}\,\overline{SF}
=\operatorname{Pow}_{(HMF)}(S)=SH^2=SK^2.$$
Since $K\in(KFM)$, this proves that $SK$ is tangent to $(KFM)$. Likewise $\operatorname{Pow}_{\omega_1}(S)=SH^2=SK^2$, so $SK$ is tangent to $\omega_1$ at $K$. The two distinct circles share this tangent, proving the claim.

**Certificate.** A radical center manufactures a point with three equal powers. Tangency follows from the equality between power and the square of a known secant distance. The definitions of $A',E$ and the collinearity argument are supplied here because the recovered source omitted that setup.

# G15. Equal segments turn spiral similarity into rotation

**Source:** IMO shortlist 2024, G1. **Record:** `imo_2024_a60b6c`.

**Problem.** A cyclic quadrilateral satisfies $AC<BD<AD$ and $\angle DBA<90^\circ$. On the side of $AD$ opposite $C$, choose $E$ with $DE\parallel AB$, $DE=AC$, and $F$ with $AF\parallel CD$, $AF=BD$. Prove that the perpendicular bisectors of $BC,EF$ meet on $(ABCD)$.

**Solution.** Cyclicity and the parallels give $\angle CAF=\angle EDB$ as directed angles, while $CA=DE$ and $AF=DB$. Thus $ACF$ and $DEB$ are congruent, so $CF=BE$. Put $P=BE\cap CF$. The same congruence gives
$$\angle CPB=\angle(CF,BE)=\angle(AF,DB)=\angle(DC,DB)=\angle CDB.$$
Consequently $P\in(ABCD)$, by the equal angles subtending $CB$.

Use the equal-segment center theorem proved in the companion theory volume: for two intersecting lines $BE,CF$, the direct similarity sending $B$ to $C$ and $E$ to $F$ has its center $T$ on $(PBC)$, allowing $T=P$. The proof solves $C-T=q(B-T)$ and $F-T=q(E-T)$ in complex coordinates and applies the cyclicity criterion, so it also covers coincident auxiliary intersections. Because $BE=CF$, the similarity has scale one, giving $TB=TC$ and $TE=TF$. Thus $T$ belongs to both perpendicular bisectors. Since $(PBC)=(ABCD)$, it is their common point on the required circle.

**Certificate.** Prove equality of two segments, then use the center of the direct similarity. Equal scale produces both perpendicular bisectors simultaneously.

# G16. Reflect a vertex in the incenter

**Source:** IMO shortlist 2024, G2. **Record:** `imo_2024_7db46b`.

**Problem.** A triangle has $AB<AC<BC$, incenter $I$, and incircle. The other tangent parallel to $AC$ meets the interior of $BC$ at $X$; the other tangent parallel to $AB$ meets it at $Y$. Let $P\ne A$ be the intersection of $AI$ with $(ABC)$, and let $K,L$ be the midpoints of $AB,AC$. Prove $\angle KIL+\angle YPX=180^\circ$.

**Solution.** Reflect $A$ in $I$ to get $A'$. The half-turn about $I$ preserves the incircle and sends $AB,AC$ to their other parallel tangents. Therefore $A'X\parallel AC$ and $A'Y\parallel AB$. Moreover $A,A',P$ are collinear. Angles in $(ABC)$ now give
$$\angle APB=\angle ACB=\angle A'XC,$$
which proves $B,P,A',X$ concyclic; similarly $C,P,A',Y$ are concyclic. The homothety with center $A$ and ratio two sends $K,I,L$ to $B,A',C$, so $\angle KIL=\angle BA'C$.

The two auxiliary circles give $\angle APX=\angle A'BC$ and $\angle YPA=\angle BCA'$. In the given order these add to $\angle YPX$. Hence
$$\angle KIL+\angle YPX=\angle BA'C+\angle A'BC+\angle BCA'=180^\circ.$$

**Certificate.** Reflecting a vertex in the incenter constructs both other parallel tangents at once. Doubling the midpoint triangle then reveals the ordinary triangle angle sum.

# Attribution and proof audit {.unnumbered}

The printed records resolve to `https://mathnet.mit.edu/data_v2/full/imo/RECORD.json.gz`. The complete ledger credits original booklets and their editors. The official IMO 2017 paper is at https://www.imo-official.org/assets/documents/problems/2017/2017_eng.pdf . The rewritten expositions repair omitted definitions in G14, the angle-sum sign in G09, and missing branches in the G05 transcription. These repairs are recorded separately from the untouched, explicitly labeled source-supplied texts. A geometric diagram is never used as evidence of an unstated collinearity or point order.
