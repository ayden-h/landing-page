# AIME Geometry Worked Solutions

New exposition after source consultation. Each entry records its source review and verification; see the coverage and provenance reports for their precise scope.

## 1983 AIME Problem 4: The interior corner of a circular notch

Points A and C lie on a circle of radius √50. Point B lies inside it, AB=6, BC=2, and ∠ABC=90°. Find the squared distance from B to the circle center.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1983_AIME_Problems/Problem_4) · MAA AMC.

### Solution

Choose B=(0,0), A=(0,6), C=(2,0), and center O=(u,v). The two radius equations are u²+(v-6)²=50 and (u-2)²+v²=50. Subtraction gives u=3v-8; substitution gives (v-1)(v-5)=0. The centers are (-5,1) and (7,5), with OB²=26 and 74. Since B is inside the radius-√50 circle, only 26 is admissible.

**Answer:** 026.

**Methods:** coordinate geometry, circle equations.

**Verification:** Both center candidates satisfy the two radius equations; only squared distance 26 is less than 50.

**Source comparison:** All seven entries inspected. Coordinate, cosine, and right-triangle methods agree. Index 6 explicitly relies on guessed integer lengths from the drawing and is not a proof. The interior-location condition selects the correct circle center.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Two perpendicular notch segments locate an interior point relative to a circle.

## 1983 AIME Problem 11: A square base and an extended ridge

A solid has square base ABCD of side s and upper edge EF of length 2s, parallel to AB. Its faces are ABCD, ADE, BCF, ABFE, and DCEF; AE=DE=BF=CF=s. For s=6√2, find its volume.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1983_AIME_Problems/Problem_11) · MAA AMC.

### Solution

The two equal-edge triangles put the ridge over the line through the midpoints of AD and BC. Its overhang beyond each end of the square is s/2. A lateral edge therefore has horizontal displacement components s/2,s/2, giving height h=√(s²-s²/4-s²/4)=s/√2=6. Extend the solid to the triangular prism with ridge length 2s, base width s, and height h. Its volume is s²h. The two added end pyramids each have rectangular base area s²/2 and height h, hence combined volume s²h/3. The required volume is 2s²h/3=288.

**Answer:** 288.

**Methods:** solid geometry, volume decomposition.

**Verification:** The independent horizontal-section area at height z is s²(1-z²/h²); integration gives 2s²h/3=288.

**Source comparison:** All four alternatives read: prism subtraction, completion to a regular tetrahedron, horizontal-section integration, and a less explicit prism-plus-pyramids decomposition. The geometric ridge orientation must be retained from the diagram in a standalone restatement.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A square-based solid is measured by prism and pyramid decomposition.

## 1983 AIME Problem 12: A diameter with reversed chord digits

A circle has a two-digit integer diameter AB. A perpendicular chord CD has length obtained by reversing those digits. Their intersection H has positive rational distance from the center O. Find AB.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1983_AIME_Problems/Problem_12) · MAA AMC.

### Solution

Write AB=10a+b and CD=10b+a. The perpendicular diameter bisects the chord, so (2 OH)²=(10a+b)²-(10b+a)²=99(a+b)(a-b). Positivity gives a>b. A rational square root of an integer is integral; therefore this product is a square. Its factor 11 forces 11|(a+b)(a-b). Since 0<a-b≤9 and a+b≤18, we get a+b=11. Now 99·11(a-b)=33²(a-b), so a-b is a positive square. With a+b=11 and digits at most 9, the odd difference is at most 7; its only square possibility is 1. Thus a=6,b=5 and AB=65.

**Answer:** 065.

**Methods:** digit constraints, perfect squares, circle chords.

**Verification:** 65²-56²=1089=33², so OH=33/2 is positive rational. Independent exact check passed: Exhaust all90 digit pairs and test the squared chord-distance difference.

**Source comparison:** Both alternatives use the right-triangle or power-of-point identity followed by the prime 11. The bound on the digit difference is needed to rule out square 9 after a+b=11.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory. The reversed-digit chord condition imposes a perfect-square constraint from a right triangle.

## 1983 AIME Problem 14: Equal chords through an intersection

Two circles of radii 8 and 6 have centers 12 units apart and intersect at P. A line through P meets the first again at Q and the second again at R, with P between Q,R and QP=PR. Find QP².

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1983_AIME_Problems/Problem_14) · MAA AMC.

### Solution

Take P as the vector origin and write Q=-tu, R=tu for a unit vector u and t>0. Let A,B be the center vectors, with |A|²=64, |B|²=36, and |B-A|²=144. Comparing the equal-radius equations at P,Q and P,R gives A·u=-t/2 and B·u=t/2. Hence S=A+B is perpendicular to u, while D=B-A has D·u=t. Now |S|²=2(64+36)-144=56 and S·D=36-64=-28. In the plane, the squared projection of D perpendicular to S is t²=|D|²-(S·D)²/|S|²=144-784/56=130.

**Answer:** 130.

**Methods:** vectors, circle chords, orthogonal projections.

**Verification:** The projection computation gives 130 exactly and a positive projection length; reversing u selects the prescribed Q,P,R order.

**Source comparison:** All ten entries inspected. Reflection and midpoint methods justify the configuration. Several alternatives use the special collinearity of the second endpoint with the centers without first proving it. Index 8 misprints the smaller circle equation, and index 9 writes 2x² instead of (2x)². The projection proof requires neither collinearity guess.

**Archived entries inspected:** 10 of 10. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Equal collinear chords impose projection constraints on the two circle centers.

## 1983 AIME Problem 15: A unique chord with prescribed bisector

In a circle of radius 5, chord BC has length 6 and bisects chord AD. B lies on the minor arc AD. No other chord from A is bisected by BC. Express the sine of the minor central angle AOB as m/n in lowest terms and find mn.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1983_AIME_Problems/Problem_15) · MAA AMC.

### Solution

Set O=(0,0), B=(3,4), C=(-3,4), and A=(u,v). A chord from A has midpoint on BC exactly when its other endpoint has y-coordinate 8-v. Midpoints of two circle points lie in the disk, so such midpoints on the line y=4 automatically lie on segment BC. The uniqueness hypothesis thus makes the horizontal line y=8-v tangent to the circle. Since -5≤v≤5, only 8-v=5 is possible, giving v=3 and u=±4. The minor-arc condition with B=(3,4) selects A=(4,3), D=(0,5). Therefore sin∠AOB=|4·4-3·3|/25=7/25, and mn=175.

**Answer:** 175.

**Methods:** locus, tangency, coordinate geometry.

**Verification:** The chord endpoints A=(4,3),D=(0,5) have midpoint(2,4) on BC; tangency ensures uniqueness, and the determinant gives the reduced sine 7/25.

**Source comparison:** All eight archived entries read, including the separate uniqueness continuation at index 4. The midpoint-circle and parallel-line loci are valid. The uniqueness-to-tangency step must justify that a second line-circle intersection would still give a midpoint on the chord segment; convexity of the disk supplies this in the new proof.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A unique bisected chord forces tangency of a midpoint locus and determines a central angle.

## 1984 AIME Problem 3: Three parallel-line triangles

Point P lies inside triangle ABC. For each side, the two lines through P parallel to the other sides cut off a triangle with vertex P and base on that side. These three triangles have areas 4,9,49. Find the area of ABC.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1984_AIME_Problems/Problem_3) · MAA AMC.

### Solution

Let K be the area of ABC and let λ₁,λ₂,λ₃ be the scale factors of the three similar triangles. Their altitudes relative to the corresponding sides equal the distances from P to those sides. Hence λᵢ is also the area ratio of the triangle formed by P and that whole side to ABC. Those three larger triangles partition ABC, so λ₁+λ₂+λ₃=1. Since the given smaller areas are λᵢ²K, we obtain (2+3+7)/√K=1 and K=144.

**Answer:** 144.

**Methods:** similarity, area ratios, barycentric coordinates.

**Verification:** The scale factors 1/6,1/4,7/12 sum to 1 and their squared multiples of 144 are 4,9,49.

**Source comparison:** All four alternatives use similarity and additive base lengths. Index 1 assumes an arbitrary base-to-height ratio without explicitly justifying an area-preserving affine normalization. The area-ratio proof works for every nondegenerate shape.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Three parallel-line triangles have scale factors whose sum is1.

## 1984 AIME Problem 6: Balancing three equal disks

Three disks of radius 3 have centers(14,92),(17,76),(19,84). A line through(17,76) divides their total area equally between its two sides. Find the absolute value of its slope.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1984_AIME_Problems/Problem_6) · MAA AMC.

### Solution

Translate(17,76) to the origin. The other centers are U=(-3,16), V=(2,8); the disk at the origin is automatically bisected. A disk cut by a line has signed area imbalance that is a strictly increasing odd function of its signed center distance while the distance lies between-3 and 3. The two disks cannot lie wholly on opposite sides: for a unit normal(nₓ,nᵧ), U·n≤-3 implies 16nᵧ≤3nₓ-3≤0, whence V·n≤2<3. Reversing the normal covers the other orientation. Thus balance requires both disks to be cut and their signed distances to be opposite, forcing the line through(U+V)/2=(-1/2,12). Its slope is-24. Conversely this line exchanges the two equal disks by a half-turn about their midpoint and bisects their total area. The answer is 24.

**Answer:** 024.

**Methods:** central symmetry, area bisection, signed distance.

**Verification:** The balanced line has equation 24x+y=0 in translated coordinates; center distances are±56/√577, strictly less than 3, and its slope is-24.

**Source comparison:** All five alternatives inspected. Midpoint symmetry proves existence. Several assert uniqueness without excluding a line separating two entire disks; the given radius is needed for that exclusion. Index 0 says the radius never matters, which is false for sufficiently small radii. Index 1 rejects a geometric case solely because its slope is not an integer, which is not a proof.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Equal-disk area balance is controlled by signed distances from a line through a fixed center.

## 1984 AIME Problem 9: Volume from two face areas

In tetrahedron ABCD, AB=3, areas[ABC]=15 and[ABD]=12, and the dihedral angle between those faces is 30°. Find the volume.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1984_AIME_Problems/Problem_9) · MAA AMC.

### Solution

The perpendicular distance fromD to lineAB within its face is 2·12/3=8. Rotating that perpendicular through the 30° dihedral angle shows that the distance fromD to planeABC is 8sin30°=4. Hence the volume is[ABC]·4/3=20. The feet of the face altitudes need not coincide onAB.

**Answer:** 020.

**Methods:** dihedral angle, tetrahedron volume.

**Verification:** The general formula 2[ABC][ABD]sinθ/(3 AB) gives 2·15·12·(1/2)/9=20.

**Source comparison:** All four alternatives give 20, but indices 0 and 2 simply assume isosceles or right faces; index 1 treats two distinct altitude feet as one. Such normalizations require a shear-invariance justification. The perpendicular-distance argument avoids any shape assumption.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Two face areas and their dihedral angle determine a tetrahedron height.

## 1985 AIME Problem 2: Rotating a right triangle about either leg

Rotating a right triangle about one leg produces a cone of volume 800π; rotating it about the other produces volume 1920π. Find its hypotenuse.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1985_AIME_Problems/Problem_2) · MAA AMC.

### Solution

Let the legs be a,b with ab²/3=800 and a²b/3=1920. Dividing gives a/b=12/5, so write a=12t,b=5t. The first equation is 100t³=800, hence t=2. The legs are 24 and 10, and their hypotenuse is√(24²+10²)=26.

**Answer:** 026.

**Methods:** cone volume, similarity, Pythagorean triples.

**Verification:** The two volumes are 24·100π/3=800π and 10·576π/3=1920π.

**Source comparison:** All three alternatives correctly translate the rotations into cone equations and recover the scaled 5-12-13 triangle.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Two rotations of a right triangle relate its legs through cone volumes.

## 1985 AIME Problem 4: A square formed by four sloping lines

In the unit square with vertices(0,0),(1,0),(1,1),(0,1), draw the lines joining these vertices respectively to (1,1-1/n),(1/n,1),(0,1/n),(1-1/n,0), where n≥2 is an integer. The central square has area 1/1985. Find n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1985_AIME_Problems/Problem_4) · MAA AMC.

### Solution

Put t=1-1/n. Two opposite boundary lines of the central square are y=tx and y=tx+1/n. The other pair is perpendicular to them by the construction. Thus the central side length is their separation, (1/n)/√(1+t²)=1/√(n²+(n-1)²). Equating its squared value to 1/1985 gives 2n²-2n+1=1985, or n(n-1)=992=32·31. The positive integer solution is n=32.

**Answer:** 032.

**Methods:** coordinate geometry, parallel-line distance, area.

**Verification:** For n=32, n²+(n-1)²=1024+961=1985; the other quadratic root is-31.

**Source comparison:** All three alternatives read. They derive the same square-width formula through a parallelogram or similar triangles. The standalone coordinate construction supplies the missing diagram unambiguously.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Distances between two pairs of parallel lines determine a central square area.

## 1985 AIME Problem 6: Areas around concurrent cevians

Cevians AD,BE,CF meet at an interior point P of triangle ABC, with D∈BC,E∈CA,F∈AB. The areas[APF],[BPF],[BPD],[CPE] are 40,30,35,84 respectively. Find[ABC].

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1985_AIME_Problems/Problem_6) · MAA AMC.

### Solution

Let $x=[APE]$ and $y=[CPD]$. Equal-altitude ratios on $AB$ give
$$\frac{AF}{FB}=\frac{40}{30}=\frac{[ACF]}{[BCF]}=\frac{x+124}{y+65},$$
so $4y=3x+112$. Equal-altitude ratios on $BC$ give
$$\frac{CD}{DB}=\frac{y}{35}=\frac{[ACD]}{[ABD]}=\frac{x+y+84}{105},$$
so $2y=x+84$. Solving yields $x=56$, $y=70$. Adding all six regions gives $40+30+35+84+56+70=315$.

**Answer:** 315.

**Methods:** area ratios, concurrent cevians.

**Verification:** The positive pair(56,70) satisfies both independent ratios:180/135=4/3 and 70/35=210/105=2. Labels agree in the principal and alternate transcriptions. Independent exact check passed: Construct rational coordinates realizing all givens; determinant areas verify the unknown regions.

**Source comparison:** All four primary alternatives read, with the alternate archive consulted to recover the omitted area labels. Index 0 has the consistent area-ratio proof. Index 1 is only a mass-points outline. Index 2 reverses a ratio and obtains incorrect individual areas 105,21, whose sum accidentally agrees. Index 3 mixes point labels and misfactors its quadratic; the correct factorization of 10r²-12r-16 is (r-2)(10r+8).

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Areas of triangles formed by concurrent cevians determine shared-base ratios.

## 1985 AIME Problem 9: Three chord lengths and a doubled angle

Chords of lengths 2,3,4 in one circle subtend minor central angles α,β,α+β, with α+β<π. If cosα=m/n in lowest terms, find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1985_AIME_Problems/Problem_9) · MAA AMC.

### Solution

Place successive arcs of anglesα andβ on the circle. Their endpoints form a triangle with side lengths 2,3,4, and the angle opposite side 2 isα/2 by the inscribed-angle theorem. The cosine rule gives cos(α/2)=(3²+4²-2²)/(2·3·4)=7/8. Therefore cosα=2(7/8)²-1=17/32, so m+n=49.

**Answer:** 049.

**Methods:** circle chords, inscribed angles, cosine rule.

**Verification:** The double-angle calculation gives 34/64=17/32, already reduced and positive.

**Source comparison:** All three alternatives correctly use a2-3-4 triangle or direct half-angle equations. Parallelism of the original chords is immaterial because chord lengths depend only on their central angles.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Chord angles assemble a triangle with sides2,3,4, allowing a cosine calculation.

## 1985 AIME Problem 11: An ellipse tangent to the axis

An ellipse has foci(9,20) and (49,55) and is tangent to the x-axis. Find the length of its major axis.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1985_AIME_Problems/Problem_11) · MAA AMC.

### Solution

Let L be the constant sum of focal distances, equal to the major-axis length. Reflect the second focus to F₂′=(49,-55). For any X on the x-axis, XF₁+XF₂=XF₁+XF₂′≥F₁F₂′, with equality at the unique crossing of the segmentF₁F₂′ with the axis. Tangency forces L to be this minimum: a smaller level misses the axis, while a larger level contains an axis point in the ellipse interior and hence is cut by the axis. Thus L=√(40²+75²)=85.

**Answer:** 085.

**Methods:** ellipse, reflection, shortest path.

**Verification:** The reflected segment crosses at x=59/3; its two focal distances sum to 85, greater than the distance between the foci.

**Source comparison:** Both primary alternatives read. Reflection gives a short complete proof. The calculus alternative treats the focal-sum function along the axis as if its derivative were the ellipse slope; its intended minimization can be repaired, but the reflection proof makes the needed tangent/minimum relation explicit.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. An ellipse tangent to a line gives a shortest broken path between two foci.

## 1985 AIME Problem 15: A hexagonal cut through a cube

Cut three 12×12 squares along segments joining midpoints of adjacent sides, producing three isosceles right triangles and three pentagons. Attach these pieces alternately around a regular hexagon, along their sides of length 6√2, and fold them into the convex polyhedron specified by this net. Find its volume.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1985_AIME_Problems/Problem_15) · MAA AMC.

### Solution

Consider the cube 0≤x,y,z≤12 cut by the plane x+y+z=18. The section is a regular hexagon whose vertices are the six permutations of (0,6,12); its side length is 6√2. On each coordinate-zero face, the part below the plane is a12-square with a midpoint corner triangle removed, while on each coordinate-12 face it is precisely that triangle. These are the alternating pentagons and triangles of the given net, so the desired polyhedron is this half-cube. Central reflection(x,y,z)↦(12-x,12-y,12-z) interchanges the two parts. Their volumes are equal, giving 12³/2=864.

**Answer:** 864.

**Methods:** polyhedron nets, central symmetry, volume.

**Verification:** The six section vertices are coplanar at coordinate sum 18 and adjacent distances are 6√2. The cube reflection is volume preserving and swaps the two half-spaces.

**Source comparison:** Both primary entries and the alternate archive were read. The first identifies two copies as a cube; the second subtracts small tetrahedra from a larger one. The coordinate half-cube construction explicitly verifies the face shapes and alternating net rather than relying solely on the omitted image.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The folded net is identified with one half of a cube cut by a central hexagonal section.

## 1986 AIME Problem 9: Equal parallel sections of a triangle

A triangle has side lengths 425,450,510. Through an interior point, draw the full segments inside the triangle parallel to its three sides. All three segments have common length d. Find d.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1986_AIME_Problems/Problem_9) · MAA AMC.

### Solution

Let λA,λB,λC be the ratios[ PBC ]/[ABC],[ PCA ]/[ABC],[ PAB ]/[ABC]; they sum to 1. The segment throughP parallel toBC has length BC·(1-λA), by similarity using its distance fromBC. Therefore d/450=1-λA, d/510=1-λB, and d/425=1-λC. Adding yields d(1/450+1/510+1/425)=2, so d=306. The resulting three λ-values are positive, consistent with an interior point.

**Answer:** 306.

**Methods:** barycentric coordinates, similarity, parallel sections.

**Verification:** The ratios 306/450=17/25,306/510=3/5,306/425=18/25 sum to 2; their complementary positive values sum to 1.

**Source comparison:** All six archived text alternatives read; no linked video was viewed. Similarity, mass points, and area decompositions give the same reciprocal-sum formula. Index 3 drops a square in an intermediate display; its intended cancellation is valid. The barycentric argument avoids extensive diagram labels.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Parallel section lengths are affine functions of barycentric coordinates.

## 1986 AIME Problem 14: A box from distances to a body diagonal

For a rectangular box, the distances from a body diagonal to the six edges it does not meet take the three values 2√5,30/√13,15/√10. Find the box volume.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1986_AIME_Problems/Problem_14) · MAA AMC.

### Solution

For edges parallel to a side of lengtha, project perpendicular to that direction. The body diagonal projects to a diagonal of a b-by-c rectangle, and the relevant edge projects to a different corner. Its distance is bc/√(b²+c²); the perpendicular feet lie within both segments. Thus the reciprocals of the three squared distances are the pairwise sums of 1/a²,1/b²,1/c². They are 45/900,13/900,40/900. Half the appropriate sums minus the remaining value give the three individual reciprocals 36/900,9/900,4/900. Hence the side lengths are 5,10,15 in some order, and volume 750.

**Answer:** 750.

**Methods:** skew-line distances, orthogonal projection, reciprocal substitution.

**Verification:** For sides $5,10,15$, the face-diagonal altitudes are $50/\sqrt{125}=2\sqrt5$, $150/\sqrt{325}=30/\sqrt{13}$, and $75/\sqrt{250}=15/\sqrt{10}$.

**Source comparison:** The sole archived solution correctly projects to face diagonals and solves a reciprocal-square linear system. Guessing a1:2:3 ratio from the radicals is not needed.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Projecting skew lines gives reciprocal-square equations for a box’s edge lengths.

## 1986 AIME Problem 15: The angle between medians of a right triangle

Triangle ABC is right-angled at C and has hypotenuse 60. Its medians from A and B lie on y=x+3 and y=2x+4. Find its area.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1986_AIME_Problems/Problem_15) · MAA AMC.

### Solution

The acute angle θ between the median lines has tanθ=|(2-1)/(1+2)|=1/3. In coordinates C=(0,0),A=(a,0),B=(0,b), direction vectors for those medians are (-a,b/2) and (a/2,-b). Their determinant has magnitude 3 ab/4 and their dot product magnitude(a²+b²)/2. Thus tanθ=3 ab/[2(a²+b²)]. Since a²+b²=60², the area ab/2=(60²/3)tanθ=400.

**Answer:** 400.

**Methods:** medians, vectors, angle between lines.

**Verification:** The general identity area=(hypotenuse²/3)tanθ yields 3600/9=400;1/3≤3/4, so the prescribed median angle is feasible for a right triangle.

**Source comparison:** All four alternatives read. The first three give valid tangent or coordinate methods. Index 3 swaps sine and cosine at the start, later switches back, and changes vertex/median labels; its long computation is not a reliable standalone proof. The vector determinant/dot-product formula is direct.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The angle between two medians of a right triangle determines its area relative to the hypotenuse.

## 1987 AIME Problem 2: Maximum distance between two spheres

One point lies on the sphere centered at (-2,-10,5) with radius 19; another lies on the sphere centered at (12,8,-16) with radius 87. Find their largest possible separation.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1987_AIME_Problems/Problem_2) · MAA AMC.

### Solution

The center distance is√(14²+18²+21²)=31. The triangle inequality bounds the point distance by 19+31+87=137. Choose both points on the center line, on the outward sides opposite the other center. Their separation is exactly this sum, proving the maximum 137.

**Answer:** 137.

**Methods:** distance, triangle inequality, attainment.

**Verification:** 14²+18²+21²=961=31²; collinear outward points attain 137 even though one sphere surrounds the other.

**Source comparison:** The sole alternative gives the center-distance calculation and the sum of radii. The outward collinear construction supplies the explicit equality case.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The triangle inequality and collinear extreme points maximize separation of two spheres.

## 1987 AIME Problem 4: A region bounded by absolute values

Find the area enclosed by|x-60|+|y|=|x|/4.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1987_AIME_Problems/Problem_4) · MAA AMC.

### Solution

A point on the graph must satisfy|x-60|≤|x|/4. Negative x is impossible, and for x≥0 the inequality gives 48≤x≤80. The upper boundary is y=5x/4-60 for 48≤x≤60 and y=60-3x/4 for 60≤x≤80; the lower boundary is its reflection across the x-axis. Thus the vertices are (48,0),(60,15),(80,0),(60,-15), giving area(80-48)·30/2=480.

**Answer:** 480.

**Methods:** absolute values, coordinate area.

**Verification:** All four vertices satisfy the equation and the two triangular halves each have area 240.

**Source comparison:** Both alternatives correctly identify the quadrilateral. Index 0 calls the symmetry a y-axis symmetry instead of x-axis symmetry; index 1 drops an x from one intermediate equation.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. Absolute-value branches form a quadrilateral whose area is determined by its intercepts.

## 1987 AIME Problem 6: Four equal regions in a rectangle

In rectangle ABCD, X,Y lie in order on AB and W,Z in order from D to C on DC. Interior points P,Q with PQ∥AB form four equal-area regions via XP,WP,PQ,YQ,ZQ. Suppose XY=YB+BC+CZ=ZW=WD+DA+AX. Given BC=19 and PQ=87, find AB.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1987_AIME_Problems/Problem_6) · MAA AMC.

### Solution

Set XY=ZW=t. The two central trapezoids with bases t and 87 have equal area, hence equal heights. Their heights sum to 19, so each is 19/2 and its area is 19(t+87)/4. This is a quarter of the rectangle, giving AB=t+87. The four equal boundary portions total the rectangle perimeter, so 4t=2 AB+38, or 2t=AB+19. Solving gives t=106 and AB=193.

**Answer:** 193.

**Methods:** trapezoid areas, perimeter partition.

**Verification:** The perimeter is 424=4·106, and each central trapezoid has area 19·193/4, exactly one quarter of the rectangle.

**Source comparison:** All three alternatives read. The principal area/perimeter method is complete. Index 2 has a factor-of-two error in its opening relation and several missing parentheses; the two-invariant solution avoids those displays. The point ordering and five internal segments were restored from the source relationships.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Equal trapezoid areas and equal perimeter portions determine a rectangle’s length.

## 1987 AIME Problem 9: Three equal angles at an interior point

Triangle $ABC$ is right-angled at $B$. An interior point $P$ satisfies $PA=10$, $PB=6$, and $\angle APB=\angle BPC=\angle CPA$. Find $PC$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1987_AIME_Problems/Problem_9) · MAA AMC.

### Solution

The three angles sum to $360^\circ$, so each is $120^\circ$. Put $PC=t$. The cosine rule gives $AB^2=10^2+6^2+10\cdot6=196$, $BC^2=t^2+6t+36$, and $AC^2=t^2+10t+100$. Since $AC^2=AB^2+BC^2$, cancellation leaves $10t+100=6t+232$, hence $t=33$.

**Answer:** 033.

**Methods:** cosine rule, Fermat point, right triangles.

**Verification:** At t=33, BC²=1323 and AC²=1519, and 196+1323=1519.

**Source comparison:** The sole alternative correctly uses the three 120-degree cosine laws followed by the right-triangle relation.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Three120-degree angles and a right-triangle identity determine the remaining distance.

## 1987 AIME Problem 15: Two orientations of an inscribed square

Triangle ABC is right-angled at C. One inscribed square has a vertex at C, sides along CA and CB, and its opposite vertex on AB; its area is 441. A second has one side on AB and its other two vertices on CA and CB; its area is 440. Find AC+CB.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1987_AIME_Problems/Problem_15) · MAA AMC.

### Solution

Let the legs be a,b, their sum s, product p, and hypotenuse c. The first square has side ab/(a+b), so p=21s. For the second square, similarity at heightq above the hypotenuse gives q=c(1-q/h), where h=p/c; hence q=pc/(c²+p). Using q²=440 and c²=s²-2p gives 440=441(s²-42s)/(s-21)². Rearrangement yields(s-21)²=441². Since s>0 and p=21s implies s>42, we take s-21=441, so s=462.

**Answer:** 462.

**Methods:** inscribed squares, similarity, symmetric variables.

**Verification:** At s=462,p=9702,c²=194040, the first side is 21 and the second squared side p²c²/(c²+p)² is 440; the leg quadratic has positive roots. Independent exact check passed: Verify both square-area equations with exact rational symmetric data.

**Source comparison:** All four alternatives reviewed. The ratio and symmetric-sum approaches give 462. The source figures were replaced by the two explicit square orientations; these are essential because different inscribed-square placements need not have the same area.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Two differently oriented inscribed squares determine symmetric functions of a right triangle’s legs.

## 1988 AIME Problem 7: An altitude from a known angle tangent

In triangle ABC, tan∠A=22/7. The altitude from A meets the interior of BC and divides BC into segments 3 and 17. Find the triangle’s area.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1988_AIME_Problems/Problem_7) · MAA AMC.

### Solution

Let the altitude be h>0. The two angles at A have tangents 3/h and 17/h. Thus tan∠A=20h/(h²-51)=22/7. Rearranging gives 11h²-70h-561=(h-11)(11h+51)=0. The positive solution is h=11, so the area is (3+17)·11/2=110.

**Answer:** 110.

**Methods:** altitude, tangent addition, triangle area.

**Verification:** For h=11,20h/(h²-51)=220/70=22/7 and the base length is 20.

**Source comparison:** The sole alternative correctly uses tangent addition and rejects the negative height. The interior-foot condition is retained explicitly in the restatement.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. An altitude splits a vertex angle into two angles whose tangents determine the height.

## 1988 AIME Problem 10: Interior diagonals of a polyhedron

A convex polyhedron has 12 square, 8 regular hexagonal and 6 regular octagonal faces, one of each at every vertex. Count vertex-pair segments lying in its interior.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1988_AIME_Problems/Problem_10) · MAA AMC.

### Solution

Counting square corners gives $V=12\cdot4=48$. Three edges meet at every vertex, hence $E=3V/2=72$. A k-gon has $k(k-3)/2$ diagonals, so face diagonals total $12\cdot2+8\cdot9+6\cdot20=216$. In a convex polyhedron, every vertex-pair segment is an edge, a face diagonal, or an interior diagonal; a face diagonal belongs to only one face. Therefore the answer is $\binom{48}{2}-72-216=840$.

**Answer:** 840.

**Methods:** incidence, combinatorial geometry.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 5 archived solution entries. Alternatives count face incidences, permissible endpoints, face diagonals or use Euler’s formula.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Vertex-pair incidences count interior diagonals after excluding edges and face diagonals.

## 1988 AIME Problem 11: Mean lines pass through a centroid

A line is a mean line for complex points w₁,…,w₅ if it contains z₁,…,z₅ with Σ(zₖ-wₖ)=0. For w=(32+170i,-7+64i,-9+200i,1+27i,-14+43i), find the slope of the mean line whose y-intercept is 3.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1988_AIME_Problems/Problem_11) · MAA AMC.

### Solution

A mean line must contain the average of its points zₖ, which equals the average of the wₖ. Conversely any line through that average works by choosing all zₖ equal to it. Here the average is (3/5,504/5). The line through this point and (0,3) has slope(504/5-3)/(3/5)=163.

**Answer:** 163.

**Methods:** centroids, affine geometry, complex coordinates.

**Verification:** At x=3/5, the line y=163x+3 has y=504/5, and choosing five identical centroid points satisfies the sum condition.

**Source comparison:** All three alternatives give 163. The centroid characterization in index 2 is shortest; the new proof includes its converse, ensuring existence as well as the necessary slope. Index 1 calls Cartesian components polar coordinates.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The affine closure of a line identifies every mean line as a line through the centroid.

## 1988 AIME Problem 12: Three equal terminal pieces of cevians

Cevians AD,BE,CF of triangle ABC meet at an interior point P. Suppose PD=PE=PF=3, while AP=a,BP=b,CP=c and a+b+c=43. Find abc.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1988_AIME_Problems/Problem_12) · MAA AMC.

### Solution

Triangles PBC and ABC share their base, and their altitude ratio is PD/AD=3/(a+3). The analogous ratios for the other two sides sum to 1 because PBC,PCA,PAB partition ABC. Therefore 3/(a+3)+3/(b+3)+3/(c+3)=1. Clear denominators and cancel the common 3(ab+bc+ca) terms. The result is abc=9(a+b+c)+54=9·43+54=441.

**Answer:** 441.

**Methods:** concurrent cevians, area ratios, symmetric identities.

**Verification:** The general identity for equal terminal length d is abc=d²(a+b+c)+2d³; d=3 and sum 43 give 441.

**Source comparison:** All four alternatives read. Area ratios, mass points, and a Gergonne/Ceva identity yield the same cubic relation. The proof only needs the sum of the three barycentric area ratios, not a separate theorem citation. Missing figure labels were reconstructed from the explicit ratios.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Concurrent-cevian area ratios give a symmetric cubic identity for three segment lengths.

## 1988 AIME Problem 14: Reflecting a rectangular hyperbola

Reflect the curve xy=1 in the line y=2x. Write its equation as 12x²+bxy+cy²+d=0. Find bc.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1988_AIME_Problems/Problem_14) · MAA AMC.

### Solution

A unit vector along the reflecting line is u=(1,2)/√5. Reflection is v↦2(v·u)u-v, with matrix(1/5)[[-3,4],[4,3]]. Since reflection is its own inverse, a point(x,y) on the reflected curve corresponds to ((-3x+4y)/5,(4x+3y)/5) on the original. Their product is 1, so-12x²+7 xy+12y²=25. In the requested normalization, b=-7,c=-12, and bc=84.

**Answer:** 084.

**Methods:** reflection matrices, conics, coordinate transformations.

**Verification:** The reflection matrix squares to the identity and fixes(1,2). Expanding the transformed coordinate product gives the stated normalized coefficients.

**Source comparison:** All four alternatives read. The coordinate reflection method is complete. Index 2 writes an incorrect principal-arctangent equality for the doubled angle and misprints 3/5 as 5/5 once; its intended matrix and final equation are correct. Index 3 proposes a point-fitting calculation without carrying it out.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A reflection matrix transforms a rectangular hyperbola’s quadratic equation.

## 1989 AIME Problem 2: Polygons from circle points

Ten points lie on a circle. Count convex polygons with at least three vertices selected from those points.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1989_AIME_Problems/Problem_2) · MAA AMC.

### Solution

Every subset of at least three points gives exactly one convex polygon, by taking its points in circular order. Remove subsets of sizes 0,1,2 from all subsets: $2^{10}-1-10-\binom{10}{2}=968$.

**Answer:** 968.

**Methods:** bijection, subsets.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Choosing subsets of ten points on a circle counts convex polygons.

## 1989 AIME Problem 6: The first possible moving rendezvous

A and B are 100 units apart. Allie leaves A at speed 8 along a ray making a 60° angle with AB. Billie leaves B simultaneously at speed 7 along a chosen straight ray. What distance has Allie traveled at their earliest possible meeting?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1989_AIME_Problems/Problem_6) · MAA AMC.

### Solution

Set $A=(0,0)$ and $B=(100,0)$. After time $t>0$, Allie is at $(4t,4\sqrt3t)$. Billie can reach this point in the same time precisely when its distance from $B$ is $7t$. Squaring gives $(100-4t)^2+48t^2=49t^2$, or $3t^2-160t+2000=0$. Its roots are $20$ and $100/3$, and each determines a valid ray from $B$. The earlier meeting occurs at $t=20$, when Allie has traveled $8\cdot20=160$.

**Answer:** 160.

**Methods:** relative motion, law of cosines, quadratic equations.

**Verification:** At $t=20$ the displacement from $B$ is $(-20,80\sqrt3)$, whose squared length is $19600=(7\cdot20)^2$.

**Source comparison:** All four alternatives read. The coordinate quadratic retains both possible meeting times. Several geometric alternatives choose an orientation that yields the earlier branch without discussing the second; index 0 also writes two proportional quadratic expressions as literally equal.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. An earliest meeting of two constant-speed travelers is a quadratic distance equation.

## 1989 AIME Problem 10: Cotangents expressed through area

A triangle has side lengths a,b,c opposite angles α,β,γ, and a²+b²=1989c². Find cotγ/(cotα+cotβ).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1989_AIME_Problems/Problem_10) · MAA AMC.

### Solution

Let K>0 be its area. The cosine law and K=ab sinγ/2 give cotγ=(a²+b²−c²)/(4K). Applying the same formula to α and β and adding gives cotα+cotβ=c²/(2K). Hence the requested quotient is (a²+b²−c²)/(2c²)=1988/2=994. These identities also hold when an angle is obtuse.

**Answer:** 994.

**Methods:** cotangent, triangle area, law of cosines.

**Verification:** The denominator c²/(2K) is strictly positive, so the quotient is defined for every admissible triangle.

**Source comparison:** All eight alternatives read. Indices 5 and 7 assume a right triangle without establishing that the quotient is invariant, so their specialization is insufficient by itself. Altitude approaches need directed projections in obtuse cases; the area identities avoid that issue.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The law of cosines and area formulas simplify a quotient of cotangents.

## 1989 AIME Problem 12: Opposite-edge midpoints in a tetrahedron

A tetrahedron has AB=41, AC=7, AD=18, BC=36, BD=27, and CD=13. If M and N are the midpoints of AB and CD, find MN².

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1989_AIME_Problems/Problem_12) · MAA AMC.

### Solution

Apollonius’s identity in triangles ABC and ABD gives CM²=(2·7²+2·36²−41²)/4=1009/4 and DM²=(2·18²+2·27²−41²)/4=425/4. Apply it again in triangle CMD, whose median MN goes to the midpoint of CD: MN²=(2CM²+2DM²−CD²)/4=(717−169)/4=137.

**Answer:** 137.

**Methods:** Apollonius theorem, tetrahedra, midpoint distance.

**Verification:** Equivalently, 4MN²=AC²+AD²+BC²+BD²−AB²−CD²=548.

**Source comparison:** The single archived alternative is valid. Repeated median identities give the distance without constructing spatial coordinates.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Apollonius identities determine the distance between opposite-edge midpoints of a tetrahedron.

## 1989 AIME Problem 15: Area ratios force a right angle

In triangle ABC, cevians AD,BE,CF meet at an interior point P, with D∈BC,E∈CA,F∈AB. Given AP=6, BP=9, PD=6, PE=3, and CF=20, find the area of ABC.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1989_AIME_Problems/Problem_15) · MAA AMC.

### Solution

The area fractions of PBC and PCA in ABC are PD/AD=1/2 and PE/BE=1/4. Therefore PAB also has area fraction 1/4, so PF/CF=1/4, giving PF=5 and CP=15. The equal areas of PAB and PAC imply BD=DC, so PD is a median of triangle PBC. Apollonius gives BD²=(BP²+CP²)/2−PD²=(81+225)/2−36=117. Since BP²+PD²=117, triangle BPD is right at P. Points A,P,D are collinear, so AP⊥BP and [APB]=6·9/2=27. Its area fraction is 1/4, hence [ABC]=108.

**Answer:** 108.

**Methods:** concurrent cevians, area coordinates, median identity, right-angle detection.

**Verification:** The derived values CP=15,PF=5 satisfy CF=20, and the median computation proves the perpendicularity used in the final area calculation.

**Source comparison:** All nine alternatives read. Index 0 mislabels the right angle as being at B rather than P. Index 2 mixes several segment labels and lengths; index 3 writes CF/PF=3 instead of 4; index 8 names triangles inconsistent with its cosine-law lengths. The area-fraction and median argument supplies a complete short proof.

**Archived entries inspected:** 9 of 9. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Concurrent-cevian area ratios and a median identity force a right angle.

## 1990 AIME Problem 3: A largest regular-polygon side count

Regular polygons with r and s sides satisfy r≥s≥3, and each interior angle of the r-gon is 59/58 times each interior angle of the s-gon. Find the largest possible s.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1990_AIME_Problems/Problem_3) · MAA AMC.

### Solution

Using the interior-angle formula gives 58(r−2)/r=59(s−2)/s, hence r=116s/(118−s). Positivity of r and s forces s<118, so s≤117. For s=117, the formula gives r=116·117, an integer exceeding s. Thus the bound is attained and the answer is 117.

**Answer:** 117.

**Methods:** regular polygons, rational constraints, attainability.

**Verification:** At s=117,r=13572, the rearranged angle-ratio equation holds exactly.

**Source comparison:** All three alternatives read. Indices 0 and 2 prove the bound and exhibit an integer solution. Index 1 splits divisibility into cases that are not exhaustive and invokes the contest answer range; those arguments are unnecessary.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory. Regular-polygon angle ratios lead to an integer bound on the number of sides.

## 1990 AIME Problem 7: An angle bisector from unit vectors

Triangle PQR has P=(−8,5), Q=(−15,−19), and R=(1,−7). Its internal bisector at P has equation ax+2y+c=0. Find a+c.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1990_AIME_Problems/Problem_7) · MAA AMC.

### Solution

The vectors PQ=(−7,−24) and PR=(9,−12) have lengths 25 and 15. The sum of their unit vectors, (−7/25,−24/25)+(3/5,−4/5)=(8/25,−44/25), points along the internal bisector: its projections on the two unit side vectors are equal, and it lies between them. Thus the bisector has direction (2,−11), giving normal (11,2). Passing through P yields 11x+2y+78=0, so a+c=89.

**Answer:** 089.

**Methods:** angle bisectors, unit vectors, coordinate geometry.

**Verification:** The line passes through P, and its direction is a positive multiple of the sum of the two unit side vectors.

**Source comparison:** All six entries read. Entry 0 is only an introductory fragment; later entries complete angle-bisector, isosceles, incenter, or trigonometric methods. The half-angle method requires careful angle branches. Summing unit direction vectors yields the internal bisector directly.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Unit vectors along two sides give the direction of their internal angle bisector.

## 1990 AIME Problem 12: Sum of dodecagon chords

For a regular 12-gon of circumradius 12, write the sum of all side and diagonal lengths as a+b√2+c√3+d√6. Find a+b+c+d.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1990_AIME_Problems/Problem_12) · MAA AMC.

### Solution

For circular separation $j=1,\ldots,5$, there are 12 chords of length $24\sin(15j^\circ)$; there are six diameters of length 24. The five shorter lengths are $6(\sqrt6-\sqrt2),12,12\sqrt2,12\sqrt3,6(\sqrt6+\sqrt2)$. Thus the total is $288+144\sqrt2+144\sqrt3+144\sqrt6$, whose coefficient sum is $720$. The diameter class has six rather than twelve members because the two directions reach the same endpoint.

**Answer:** 720.

**Methods:** orbit size, chord counting.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 4 archived solution entries. Alternatives evaluate the same six chord classes using trigonometry, cosine law or complex coordinates.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Chord lengths are grouped by cyclic vertex separation and counted with their multiplicities.

## 1990 AIME Problem 14: A tetrahedron folded from a rectangle

A 12√3 by 13√3 rectangle ABCD has diagonal intersection P. Remove triangle ABP, identify edges AP and BP, and fold along CP and DP to form a tetrahedron. Find its volume.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1990_AIME_Problems/Problem_14) · MAA AMC.

### Solution

After A and B are identified as X, the base XCD has sides 13√3,13√3,12√3. Its altitude is √399 and area K=18√133. The three distances PX,PC,PD are all half the original diagonal, namely √939/2. The perpendicular projection of P onto the base is therefore its circumcenter. The base circumradius is R=(13√3)²(12√3)/(4K)=169√3/(2√133). If h is the tetrahedron height, h²=939/4−R²=9801/133, so h=99/√133. The volume is Kh/3=594.

**Answer:** 594.

**Methods:** folded nets, tetrahedron volume, circumradius, equal lateral edges.

**Verification:** The height square is positive, and (18√133)(99/√133)/3=594.

**Source comparison:** All three alternatives read. The synthetic circumcenter method is complete and avoids dihedral-angle bookkeeping. Index 1 inconsistently names its base vertices but its distance equations are correct. The third uses a different face as base and reaches the same volume.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Folding a rectangle fixes all six tetrahedron edges, so base circumradius determines its height.

## 1991 AIME Problem 2: Parallel slices of a rectangle

In a 4 by 3 rectangle ABCD, divide AB and CB into 168 equal parts starting at A and C, and join corresponding interior division points. Repeat on AD and CD, then include diagonal AC. Find the total length of the resulting 335 parallel segments.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1991_AIME_Problems/Problem_2) · MAA AMC.

### Solution

The diagonal has length 5. By similarity, the 167 interior segments on either side have lengths 5j/168 for j=1,…,167. Hence their total, including the diagonal once, is 5+(10/168)(167·168/2)=5+835=840.

**Answer:** 840.

**Methods:** similar triangles, arithmetic sums, parallel segments.

**Verification:** There are 2·167+1=335 segments, and each pair of complementary slice lengths sums to 5.

**Source comparison:** All three alternatives read. Index 0 mixes the summation endpoints and subtraction of the diagonal, obtaining the right total through inconsistent displayed arithmetic. The other two give valid direct summation or pairing arguments.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Similar right triangles produce an arithmetic sequence of parallel segment lengths.

## 1991 AIME Problem 11: Twelve disks in the depicted regular ring

In the rotationally symmetric arrangement shown in the original problem, twelve congruent disks form a ring covering a circle of radius 1. Neighboring disks are externally tangent at points of that circle. Their total area is π(a−b√c), with c squarefree. Find a+b+c.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1991_AIME_Problems/Problem_11) · MAA AMC.

### Solution

The disk centers form a regular dodecagon. Each point of tangency is the midpoint of a side, so the dodecagon has apothem 1 and side length twice the disk radius r. A right triangle from the center to a vertex and an adjacent side midpoint has angle 15° at the center, giving r=tan 15°=2−√3. The total disk area is 12πr²=π(84−48√3). Therefore a+b+c=84+48+3=135.

**Answer:** 135.

**Methods:** regular polygons, tangent circles, half-angle geometry.

**Verification:** For the regular arrangement r=tan(π/12), adjacent center distance is 2r, and the twelve covered arcs each have central angle 30°.

**Source comparison:** The sole alternative uses the regular dodecagon depicted in the original figure. That regularity is essential: the prose alone, without the pictured rotational symmetry, permits alternating distances of disk centers from the origin and does not uniquely determine the radius. The restatement explicitly preserves the figure’s symmetry assumption.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The regular ring depicted in the diagram gives a circumscribed dodecagon and a 15-degree tangent.

## 1991 AIME Problem 12: A reflected vertex locates a rhombus center

A rhombus PQRS is inscribed in rectangle ABCD, with P,Q,R,S in the interiors of AB,BC,CD,DA respectively. Given PB=15, BQ=20, PR=30, and QS=40, the rectangle’s perimeter is m/n in lowest terms. Find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1991_AIME_Problems/Problem_12) · MAA AMC.

### Solution

Set B=(0,0), P=(−15,0), and Q=(0,20). Let O be the rhombus center. Since the diagonals bisect each other, OP=15 and OQ=20. The point B has those same distances to P and Q, so the other intersection O of the two circles is the reflection of B across PQ. The line PQ is 4x−3y+60=0, and reflecting (0,0) in it gives O=(−96/5,72/5). The rhombus center is also the rectangle center: PR has endpoints on its horizontal sides, while QS has endpoints on its vertical sides. Thus the rectangle dimensions are 192/5 and 144/5. Its perimeter is 672/5, so m+n=677.

**Answer:** 677.

**Methods:** rhombus diagonals, reflection, coordinate geometry.

**Verification:** The reflected center has OP=15,OQ=20 and lies inside the resulting rectangle; the reflected vertices R,S lie in the required side interiors.

**Source comparison:** All eight entries read, including a diagram-only entry. Index 1 rejects an extraneous algebraic branch by incorrectly saying everything becomes squares; the actual issue is failure of the prescribed diagonal lengths. Index 6 omits that branch. Several later entries have mislabeled segments. Reflection of B across PQ determines the correct center uniquely.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The rhombus center is a reflected rectangle vertex, fixing the rectangle dimensions.

## 1991 AIME Problem 14: Three Ptolemy equations for a hexagon

A cyclic hexagon ABCDEF has AB=31 and all its other sides equal to 81. Find AC+AD+AE.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1991_AIME_Problems/Problem_14) · MAA AMC.

### Solution

Equal chords subtend equal minor arcs, and the five equal sides must use those minor arcs, so reflection symmetry gives x=AC=BF, y=AD=BE=CF, and z=AE=BD=DF. Ptolemy’s theorem in ABCD, ACDF, and ADEF gives respectively xz=81y+31·81, y²=xz+81², and z²=81y+81². The first two yield y²−81y−9072=0, whose positive root is y=144. Then z²=81·225, so z=135, and x=81(144+31)/135=105. The requested sum is 105+144+135=384.

**Answer:** 384.

**Methods:** cyclic polygons, Ptolemy theorem, symmetry.

**Verification:** The values satisfy $105\cdot135=81\cdot144+31\cdot81$, $144^2=105\cdot135+81^2$, and $135^2=81\cdot144+81^2$.

**Source comparison:** The single alternative correctly uses three Ptolemy identities. The repeated diagonal lengths rely on the equal-arc symmetry, which is stated explicitly in the new proof.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Three Ptolemy identities determine the distinct diagonal lengths of a cyclic hexagon.

## 1992 AIME Problem 7: A tetrahedron from two face areas

Faces ABC and BCD of a tetrahedron meet at a dihedral angle of 30°. Their areas are 120 and 80, and BC=10. Find the tetrahedron’s volume.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1992_AIME_Problems/Problem_7) · MAA AMC.

### Solution

The perpendicular distance from D to line BC within face BCD is 2·80/10=16. Its component perpendicular to plane ABC is 16sin30°=8. Taking ABC as base, the tetrahedron volume is 120·8/3=320.

**Answer:** 320.

**Methods:** dihedral angles, tetrahedron volume, altitude projection.

**Verification:** The general formula is V=2K₁K₂ sinθ/(3e) for face areas K₁,K₂ sharing an edge of length e; substitution gives 320.

**Source comparison:** The sole alternative correctly projects the face altitude through the dihedral angle. This works whether its foot lies on the segment BC or its extension.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The dihedral angle converts an altitude within one face into the tetrahedron height.

## 1992 AIME Problem 9: A base point equidistant from trapezoid legs

Trapezoid ABCD has AB∥CD, AB=92, BC=50, CD=19, and AD=70. A circle centered at P on AB is tangent to BC and AD. Write AP=m/n in lowest terms. Find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1992_AIME_Problems/Problem_9) · MAA AMC.

### Solution

Let h be the trapezoid height, r the circle radius, and AP=x. The distance from P to line AD is x sin∠DAB=xh/70, while its distance to line BC is (92−x)h/50. These distances are equal, so x/70=(92−x)/50. Therefore 120x=6440, giving x=161/3 and m+n=164.

**Answer:** 164.

**Methods:** distance to a line, trapezoids, tangent circles.

**Verification:** AP:PB=(161/3):(115/3)=7:5=AD:BC, with P strictly inside AB.

**Source comparison:** All six alternatives read. The common height cancels, so computing it is unnecessary. Index 4 names a degenerate triangle PBA where PDA is intended. The angle-bisector approaches require the extension and similarity argument; direct distances are shorter.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Equal distances from a base point to the trapezoid legs give a segment-length ratio.

## 1992 AIME Problem 10: A square outside two semicircles

Let A consist of nonzero complex z such that the real and imaginary parts of both z/40 and 40/conj(z) lie in [0,1]. Find the integer nearest the area of A.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1992_AIME_Problems/Problem_10) · MAA AMC.

### Solution

Write z=x+iy. The first condition gives 0≤x,y≤40. The second gives x²+y²≥40x and x²+y²≥40y, so the region is the square outside the circles centered at (20,0) and (0,20), both of radius 20. Within the square these are two semicircles, each of area 200π. Their overlap consists of two 90° circular segments, with total area 2(100π−200)=200π−400. Their union therefore has area 200π+400. The required area is 1600−(200π+400)=1200−200π≈571.681, whose nearest integer is 572.

**Answer:** 572.

**Methods:** complex inequalities, circle intersections, area inclusion-exclusion.

**Verification:** Using 3.14159<π<3.14160 puts the exact area between 571.680 and 571.682, safely rounding to 572.

**Source comparison:** The sole alternative obtains the correct final area but calls 200π+400 the overlap; it is actually the union area. The true overlap is 200π−400. Distinguishing those regions fixes the exposition.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Complex-coordinate inequalities describe a square with two semicircular regions removed.

## 1992 AIME Problem 11: The order of two successive reflections

Reflect a line through the origin first in the line making angle π/70 with the positive x-axis, then in the line making angle π/54. Starting with y=(19/92)x, find the least positive number of repetitions that restores the original line.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1992_AIME_Problems/Problem_11) · MAA AMC.

### Solution

Reflection in a line of angle α sends a direction θ to 2α−θ modulo π. The two reflections therefore send θ to θ+2(π/54−π/70)=θ+8π/945. After m repetitions the original unoriented line returns exactly when 8mπ/945 is an integer multiple of π. Since gcd(8,945)=1, this occurs precisely when 945 divides m. The least positive value is 945.

**Answer:** 945.

**Methods:** composition of reflections, rotation order, modular arithmetic.

**Verification:** 945 repetitions rotate by 8π; coprimality excludes every smaller positive repetition count.

**Source comparison:** The single alternative correctly treats lines as directions modulo π rather than 2π. The initial slope is irrelevant because every line through the origin has the same return order.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory. Composing reflections gives a rational-angle rotation whose order on unoriented lines is computed modulo pi.

## 1992 AIME Problem 13: Maximum area on an Apollonius circle

Triangle ABC has AB=9 and BC:AC=40:41. Find its largest possible area.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1992_AIME_Problems/Problem_13) · MAA AMC.

### Solution

Place B=(0,0), A=(9,0), and C=(x,y). The side ratio gives 1681(x²+y²)=1600((x−9)²+y²). Completing the square yields (x+1600/9)²+y²=(1640/9)². Thus C lies on a circle of radius 1640/9, and its greatest possible distance from line AB is that radius, attained directly above or below the circle’s center. The maximum area is (9/2)(1640/9)=820.

**Answer:** 820.

**Methods:** Apollonius circles, maximum triangle area, completing the square.

**Verification:** The highest locus point has nonzero altitude and satisfies the exact squared-distance ratio 1600:1681.

**Source comparison:** All five alternatives read. Coordinate and Heron/AM-GM methods are valid when attainment is checked. Index 0 contains a 1600-versus-1600/81 simplification typo; index 4 duplicates a prefactor in its final line. The locus circle both bounds and attains the altitude.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A fixed side ratio gives an Apollonius circle whose radius maximizes the altitude.

## 1992 AIME Problem 14: A universal product identity for cevian ratios

Cevians AA′,BB′,CC′ of triangle ABC meet at an interior point O, with A′,B′,C′ on the opposite sides. If AO/OA′+BO/OB′+CO/OC′=92, find the product of these three ratios.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1992_AIME_Problems/Problem_14) · MAA AMC.

### Solution

Set x=AO/OA′, y=BO/OB′, z=CO/OC′. The area fraction [OBC]/[ABC] equals OA′/AA′=1/(1+x), and the analogous fractions sum to 1. Thus 1/(1+x)+1/(1+y)+1/(1+z)=1. Clearing denominators gives xy+xz+yz+2(x+y+z)+3=xyz+xy+xz+yz+x+y+z+1. Therefore xyz=x+y+z+2=94.

**Answer:** 094.

**Methods:** barycentric areas, concurrent cevians, symmetric identities.

**Verification:** The denominator factors are positive because O is interior, and the exact identity xyz=x+y+z+2 follows without assumptions about triangle shape.

**Source comparison:** All four alternatives read. The area-coordinate and mass-point proofs are complete. Index 2 arbitrarily sets two barycentric coordinates equal without proving invariance, so that specialization alone is insufficient. Clearing the universal area identity supplies the needed invariant.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Barycentric area fractions imply a symmetric identity among concurrent-cevian ratios.

## 1993 AIME Problem 2: A forty-day spiral of square distances

A traveler goes east, north, west, south in a repeating four-day cycle. On day n he travels n²/2 miles. How far is he from his starting point after 40 days?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1993_AIME_Problems/Problem_2) · MAA AMC.

### Solution

Group the days into ten blocks indexed by $j=0,\ldots,9$. The east-minus-west displacement in block $j$ is $((4j+1)^2-(4j+3)^2)/2=-8j-4$. The north-minus-south displacement is $((4j+2)^2-(4j+4)^2)/2=-8j-6$. Summing with $\sum_{j=0}^9j=45$ gives total displacement $(-400,-420)$. Its length is $\sqrt{400^2+420^2}=20\sqrt{20^2+21^2}=580$.

**Answer:** 580.

**Methods:** vector displacement, difference of squares, arithmetic sums.

**Verification:** The component magnitudes 400 and 420 form the scaled 20–21–29 right triangle.

**Source comparison:** The sole alternative correctly groups days into four-day blocks. Its initial prose calls an entire block the first day and briefly drops a factor 1/2, but the displayed block sums and final result are correct.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Alternating directional square distances sum to two perpendicular displacement components.

## 1993 AIME Problem 10: Uniform vertex face incidences

A convex polyhedron has 32 triangular or pentagonal faces. At each vertex, T triangles and P pentagons meet. Determine 100P+10T+V.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1993_AIME_Problems/Problem_10) · MAA AMC.

### Solution

Let t,p be the face counts. Incidence counting gives $3t=TV$, $5p=PV$, so $V(5T+3P)=15(t+p)=480$. Every vertex has degree $T+P$, hence Euler gives $V(T+P-2)=60$. Eliminating V yields $5T+3P=8(T+P-2)$, or $3T+5P=16$. Its only nonnegative integer solution is $T=P=2$. Therefore $V=60/(4-2)=30$, and the answer is $200+20+30=250$.

**Answer:** 250.

**Methods:** Euler formula, double counting.

**Verification:** Independent exact check passed: Exhausted the integer incidence equations; no regular-face assumption. Result [(30, 2, 2)]. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 4 archived solution entries. The incidence-based alternative is sound and avoids unwarranted regularity or visual uniqueness assumptions.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Euler’s formula and face-vertex incidences constrain a convex polyhedron’s local face counts.

## 1993 AIME Problem 12: Undoing random midpoint choices

Inside the triangle with vertices (0,0),(0,420),(560,0), a point undergoes six midpoint moves toward arbitrarily selected vertices and ends at (14,92). Determine the sum of its starting coordinates.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1993_AIME_Problems/Problem_12) · MAA AMC.

### Solution

Undoing the affine recurrence gives $x_1=64(14)-560J$ and $y_1=64(92)-420K$, where J and K are integers encoding choices of the two nonzero vertices. Because the start is interior, $0<x_1<560$ and $0<y_1<420$. These inequalities force $J=1,K=14$, so $(x_1,y_1)=(336,8)$. The two binary encodings 1 and 14 have disjoint 1-bits, so they correspond to valid vertex choices; the remaining bits correspond to the origin. Also $336/560+8/420<1$, confirming the start is interior. The coordinate sum is $344$.

**Answer:** 344.

**Methods:** binary coding, affine state.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 2 archived solution entries. Both sources reverse the affine midpoint process, either stepwise or through binary weights.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Six midpoint choices encode the starting coordinates through binary place values.

## 1993 AIME Problem 13: When a moving line of sight clears a building

Jenny and Kenny walk in the same direction at 1 and 3 feet per second on parallel paths 200 feet apart. A circular building of diameter 100 is centered midway between the paths. When it first blocks their view they are 200 feet apart. If visibility returns after t seconds, find numerator plus denominator of t in lowest terms.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1993_AIME_Problems/Problem_13) · MAA AMC.

### Solution

At first blockage they are abreast, since their separation equals the distance between the paths. Put the building center at the origin and their positions at (−50,100) and (−50,−100). At time t they are J=(−50+t,100), K=(−50+3t,−100), and their joining line is 100x+ty=200t−5000. Its distance from the origin is |200t−5000|/√(10000+t²). Tangency occurs when this equals 50; squaring and simplifying gives t(15t−800)=0. For 0<t<160/3 the line’s distance is less than 50, and the intersected circle lies between the paths, so the segment is blocked. Visibility returns at t=160/3; the requested sum is 163.

**Answer:** 163.

**Methods:** distance to a line, moving geometry, tangency, visibility interval.

**Verification:** The squared distance minus 2500 has numerator 2500t(15t−800), establishing the sign throughout the blockage interval.

**Source comparison:** All four alternatives read. Coordinate, angle-bisector, similarity, and area methods agree. The new proof checks the interval between the two tangencies and confirms that line intersection corresponds to segment blockage, not merely an intersection outside the walkers.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The line of sight becomes tangent to a circle at the endpoints of a visibility interval.

## 1993 AIME Problem 14: The least perimeter of an unstuck inscribed rectangle

A rectangle inscribed in a 6 by 8 rectangle has one vertex on each side. Call it unstuck if a nonzero sufficiently small rotation about its center keeps it inside the larger rectangle. The least possible perimeter is √N. Find N.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1993_AIME_Problems/Problem_14) · MAA AMC.

### Solution

Center the outer rectangle at the origin with sides x=±4,y=±3. The inscribed rectangle has the same center, so write adjacent vertices A=(4,u), B=(v,3), with opposites −A,−B. Equal diagonals give v²−u²=7. A small positive rotation changes A’s x-coordinate initially by −u times the angle and B’s y-coordinate by v times the angle. Thus an allowed rotation in either direction requires uv≤0. Reflecting if necessary, write u=y≥0,v=−x≤0, where x²=y²+7. If p,q are its side lengths, then p²+q²=4|A|²=64+4y² and pq=2 det(A,B)=24+2 xy. Its perimeter squared is 4(p+q)²=448+16y²+16 xy≥448. Equality occurs at y=0,x=√7. This rectangle is unstuck: a small positive rotation moves its right-hand vertex inward to x=4cosθ<4 and its upper vertex downward, while the other coordinates remain strictly inside their bounds. Hence N=448.

**Answer:** 448.

**Methods:** inscribed rectangles, rotation feasibility, perimeter optimization, coordinate geometry.

**Verification:** At equality p²+q²=64 and pq=24, so the perimeter squared is 4(64+48)=448; an explicit small rotation preserves containment.

**Source comparison:** Both alternatives read. The first gives a geometric deformation argument; the second asserts a minimum-diagonal principle without proving it. The coordinate sign condition and exact squared-perimeter identity establish a global bound and verify that equality is genuinely unstuck.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The unstuck rotation condition restricts contact-point signs, yielding a sharp perimeter bound.

## 1993 AIME Problem 15: Two incircle contacts on an altitude

Triangle ABC has AB=1995, AC=1994, and BC=1993. Its altitude CH meets AB at H. The incircles of ACH and BCH touch CH at R and S. Write RS=m/n in lowest terms and find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1993_AIME_Problems/Problem_15) · MAA AMC.

### Solution

The altitude foot lies inside AB. Subtracting AC²=AH²+CH² and BC²=BH²+CH² gives (AH−BH)·1995=1994²−1993²=3987. In a right triangle the contact distance from the right-angle vertex equals the inradius, half the sum of its legs minus its hypotenuse. Hence HR=(AH+CH−1994)/2 and HS=(BH+CH−1993)/2. Their difference has absolute value (3987/1995−1)/2=1992/3990=332/665. Thus m+n=997.

**Answer:** 997.

**Methods:** right-triangle inradius, altitude projections, tangent lengths.

**Verification:** AH=(1995+3987/1995)/2 lies between 0 and 1995, justifying the two interior right triangles; gcd(332,665)=1.

**Source comparison:** The single entry and its appended generalizations were read. The general formula |b−a|(a+b−c)/(2c) is valid when the altitude foot lies on the base segment; the appended claim for every triangle omits that hypothesis and can fail for an exterior foot.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Right-triangle inradii and altitude-foot projections determine a tangency-point separation.

## 1994 AIME Problem 2: A square between internally tangent circles

A circle of diameter PQ=10 is internally tangent at P to a circle of radius 20. A square ABCD has A,B on the larger circle, while CD is tangent to the smaller circle at Q and the smaller circle lies outside the square. If AB=m+√n, find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1994_AIME_Problems/Problem_2) · MAA AMC.

### Solution

Put the large-circle center at (0,0), P=(0,20), and Q=(0,10). The line CD is y=10, and the square extends away from the small circle, downward. If its side is s, then AB is a horizontal chord at height 10−s, with endpoints (±s/2,10−s). The circle equation gives s²/4+(10−s)²=400, or s²−16s−240=0. Its only positive root is s=8+√304, so m+n=312.

**Answer:** 312.

**Methods:** circle chords, tangent square, quadratic equations.

**Verification:** The negative quadratic root is impossible for a side length, and the positive root places both chord endpoints exactly on the radius-20 circle.

**Source comparison:** The sole alternative correctly uses the half-chord and center offset. The coordinate restatement of the configuration explains the orientation imposed by the smaller circle being outside the square.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A centered square chord and the circle radius give a quadratic for the square side.

## 1994 AIME Problem 6: Small triangles in three line families

For every integer k from −10 to 10, draw y=k, y=√3x+2k and y=−√3x+2k. Count equilateral triangles of side 2/√3 whose edges lie on the lines.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1994_AIME_Problems/Problem_6) · MAA AMC.

### Solution

Choose line indices a,b,c in the horizontal, positive-slope and negative-slope families. The sloped lines meet at height b+c, so the triangle’s altitude is $|a-b-c|$ and its side is $2|a-b-c|/\sqrt3$. Thus count triples with $a-b-c=\pm1$. For a fixed sum $s=b+c$, there are $21-|s|$ pairs when $|s|\le20$. The +1 case requires $-11\le s\le9$ and contributes $21^2-(66+45)=330$. Symmetry gives 330 for −1. Each triangle has a unique three-line description, so the answer is $660$.

**Answer:** 660.

**Methods:** lattice counting, combinatorial geometry.

**Verification:** Independent exact check passed: Enumerated all 21³ triples of line indices with unit altitude. Result 660. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 3 archived solution entries. Alternatives use hexagon area, missing horizontal lines or an enclosing triangle.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Three families of parallel lines produce a triangular-grid counting problem.

## 1994 AIME Problem 7: Lines with only integral circle intersections

Count real pairs (a,b) for which ax+by=1 and x²+y²=50 have at least one common point and every common point has integral coordinates.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1994_AIME_Problems/Problem_7) · MAA AMC.

### Solution

The circle’s integral points are $(\pm1,\pm7),(\pm7,\pm1),(\pm5,\pm5)$, twelve in all. A qualifying line is either tangent at one of these twelve points or a secant through two of them. There are $\binom{12}{2}$ secants, but the six antipodal pairs give lines through the origin, which cannot have equation $ax+by=1$. All other secants and all tangents have unique normalized equations of that form. Hence the answer is $66-6+12=72$.

**Answer:** 072.

**Methods:** geometric pairs, exceptional fibers.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The finite lattice-point model determines all tangent and secant possibilities; antipodal pairs require a separate exclusion.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry, number_theory. Integer points on a circle determine allowable secant and tangent lines.

## 1994 AIME Problem 8: An equilateral triangle from two heights

The points (0,0),(a,11),(b,37) form an equilateral triangle. Find ab.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1994_AIME_Problems/Problem_8) · MAA AMC.

### Solution

One vector from the origin is obtained from the other by a rotation of ±60°. For the +60° orientation, b=a/2−11√3/2 and 37=√3a/2+11/2. Thus a=21√3 and b=5√3, giving ab=315. The −60° orientation is the reflection of this configuration across the y-axis, changing both signs and preserving the product.

**Answer:** 315.

**Methods:** equilateral triangles, rotation matrices, orientation.

**Verification:** For a=21√3,b=5√3, all three squared side lengths equal 1444; changing both signs preserves them.

**Source comparison:** All four alternatives read. Index 1 switches perpendicular-vector signs inconsistently; index 2 misprints the final value of a; index 3 has a malformed initial equality and chooses positive roots without discussing reflection. The two rotation orientations exhaust the possibilities.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A 60-degree rotation relates the coordinates of an equilateral triangle.

## 1994 AIME Problem 10: A prime-cube projection in an integer right triangle

Triangle ABC is right at C and has integer side lengths. The altitude from C meets AB at D with BD=29³. If cosB=m/n in lowest terms, find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1994_AIME_Problems/Problem_10) · MAA AMC.

### Solution

Similarity gives BC²=AB·BD=29³AB. Integer prime valuations imply 29² divides BC, so write BC=29²x and AB=29x² for a positive integer x. Pythagoras yields AC²=(29x)²(x²−29²). Since an integer square divisible by (29x)² has its root divisible by 29x, put AC=29 xy with y a positive integer. Then (x−y)(x+y)=29². Both factors are positive; their only nondegenerate pair is 1,841, since 29,29 would give y=0. Thus x=421, and cosB=BC/AB=29/421. The requested sum is 450.

**Answer:** 450.

**Methods:** integer right triangles, prime valuations, difference of squares, projection theorem.

**Verification:** The resulting sides are 29·421·420, 29²·421, and 29·421²; the projection BC²/AB equals 29³.

**Source comparison:** All three alternatives read. Index 0 supplies the valid integer-side reduction. Index 1 treats the altitude as an integer without proof and invokes the answer range to discard factor pairs. Index 2 assumes an integral parametrization prematurely. The divisibility argument justifies every integer variable.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory. A right-triangle projection and integer side lengths lead to a prime-square factorization.

## 1994 AIME Problem 12: The finest square grid within a fence budget

A fenced 24 by 52 meter rectangle is partitioned completely into congruent axis-parallel square plots using at most 1994 meters of additional internal fence. Find the largest possible number of plots.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1994_AIME_Problems/Problem_12) · MAA AMC.

### Solution

If the square side is s, the integer grid dimensions u=24/s and v=52/s satisfy 13u=6v. Thus u=6t,v=13t for a positive integer t. Internal fence length is 52(u−1)+24(v−1)=624t−76. The budget gives 624t≤2070, so t≤3. The maximum occurs at t=3, producing uv=78t²=702 plots and requiring 1796 meters of fence.

**Answer:** 702.

**Methods:** rectangular grids, integer ratios, resource optimization.

**Verification:** The maximizing grid is $18$ by $39$, with side $4/3$. Its fence length is $17\cdot52+38\cdot24=1796$ meters, below the budget of $1994$. The next value $t=4$ requires $2420$ meters.

**Source comparison:** Both alternatives read. Index 0 correctly counts internal grid lines. Index 1 uses plus signs where boundary exclusions require minus signs and gives a dimensionally incorrect fence formula; it happens to find the right grid size.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory. Integral grid dimensions and a fence-length budget bound the square subdivision scale.

## 1994 AIME Problem 14: Unfolding a beam between two finite mirrors

Two equal-length mirror segments BA and BC meet at angle β=1.994°. A beam first reflects at C, making angle α=19.94° with BC and then traveling into the angle toward BA. It continues reflecting until it leaves the segments. Count all reflections, including the one at C.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1994_AIME_Problems/Problem_14) · MAA AMC.

### Solution

Scale the mirror lengths to 1 and place B at the center of the unit circle, C on it. Unfold each reflection by reflecting the next mirror instead of bending the ray. The beam becomes a straight chord starting at C, making angle α with the inward radial direction. Its other intersection with the unit circle subtends central angle 180°−2α=140.12° from C. The successive unfolded mirrors are unit radial segments separated by β. Thus after the initial reflection, the ray meets exactly those radial segments with kβ≤140.12°, namely k=1,…,70, since 70β=139.58° and 71β=141.574°. Including C gives 71 reflections.

**Answer:** 071.

**Methods:** reflection unfolding, finite mirrors, chord geometry.

**Verification:** The final allowable radial angle is 139.58°, strictly below the exit angle 140.12°, and the next is strictly above it.

**Source comparison:** The sole alternative and its diagram program were read to recover that β is angle ABC and α is measured relative to BC, rather than its normal. The program uses illustrative angles different from the problem data. The source phrase “inside or at B” should describe intersection within the finite mirror radius; the unit-circle chord gives that precise criterion.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Unfolding reflections turns the beam into a chord crossing equally angled radial segments.

## 1994 AIME Problem 15: Fold points as an intersection of diameter disks

For P on triangular paper ABC, fold each vertex onto P, producing the perpendicular-bisector creases restricted to the paper. Call P a fold point if these creases do not intersect. Given AB=36, AC=72, and ∠B=90°, the fold-point region has area qπ−r√s with s squarefree. Find q+r+s.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1994_AIME_Problems/Problem_15) · MAA AMC.

### Solution

Set B=(0,0), A=(a,0), C=(0,b), where a=36 and b=36√3. For interior P=(x,y), the intersection of its A- and B-creases is (a/2,(x²+y²−ax)/(2y)). Since P lies in the rectangle [0,a]×[0,b], this intersection lies on the paper exactly when x²+y²≥ax. Similarly the B- and C-creases meet on the paper exactly when x²+y²≥by. The A- and C-creases meet outside the paper because P is inside the circle with diameter AC: their circumcenter lies across AC from P. Thus, apart from boundary points of zero area, the allowed region is the lens inside both diameter disks AB and BC. Their radii are 18 and 18√3, and their centers are 36 apart. The common chord subtends angles 120° and 60° at the two centers, respectively. The lens area is 18²(π/3−√3/4)+(18√3)²(π/6−√3/4)=270π−324√3. Therefore q+r+s=597.

**Answer:** 597.

**Methods:** paper folding, perpendicular bisectors, circle lenses, locus geometry.

**Verification:** The two diameter circles meet at B and the altitude foot from B to AC; their lens lies inside ABC. The sector areas total 270π and the subtracted triangular areas total 324√3. Independent exact check passed: Exact rational crease-intersection tests at every interior point of a1/20 grid in a3–4–5 triangle.

**Source comparison:** The sole alternative gives the correct lens but asserts that circumcenters outside their small triangles are automatically outside the paper. That implication needs justification. The coordinate intersection test establishes necessity and sufficiency for this right-triangle configuration, with boundary distinctions irrelevant to area.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Intersections of perpendicular-bisector creases characterize a lens bounded by diameter circles.

## 1995 AIME Problem 1: Five shrinking squares with quarter overlaps

Start with a unit square. Each successive square has half the previous side length and is centered at its outward corner, with parallel sides; at every stage use the corner away from the earlier squares. For the first five squares, write their union area as m/n in lowest terms. Find m−n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1995_AIME_Problems/Problem_1) · MAA AMC.

### Solution

Each new square overlaps the preceding one in a quarter of its own area. It does not overlap an earlier square: along either coordinate direction, the nearest edge of the square two stages later already lies beyond the earlier square’s outer edge. Thus the union area is 1+(3/4)(1/4+1/16+1/64+1/256)=1+255/1024=1279/1024. The numerator is odd and the denominator a power of two, so the fraction is reduced and m−n=255.

**Answer:** 255.

**Methods:** geometric series, overlapping squares, union area.

**Verification:** The successive added areas are 3/16,3/64,3/256,3/1024, totaling 255/1024.

**Source comparison:** The single alternative correctly subtracts adjacent overlaps but leaves the absence of nonadjacent overlaps implicit. The outward-corner construction in the restatement expresses the original perpendicular-bisector conditions without a figure.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Successively halved squares overlap in quarter-squares, giving a telescoping area sum.

## 1995 AIME Problem 4: A common tangent chord of three tangent circles

Circles of radii 3 and 6 are externally tangent and internally tangent to a circle of radius 9. A common external tangent to the smaller circles cuts a chord from the larger circle. Find the square of its length.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1995_AIME_Problems/Problem_4) · MAA AMC.

### Solution

Let the three centers be O₃,O₆,O₉. Internal tangency gives O₃O₉=6 and O₆O₉=3, while external tangency gives O₃O₆=9. Equality in the triangle inequality places O₉ between the other centers, one third of the way from O₆ to O₃. Signed distance to a fixed line is affine, and both smaller centers lie on the same side of their common external tangent. Thus the large center’s distance to it is (2·6+3)/3=5. A radius-9 circle cut at distance 5 from its center has chord squared 4(9²−5²)=224.

**Answer:** 224.

**Methods:** tangent circles, affine distances, chord length.

**Verification:** The interpolated distance 5 is less than radius 9, and the half-chord has squared length 56.

**Source comparison:** Both alternatives correctly interpolate the distance from the large center to the common tangent. The new proof explains why the three centers are collinear, using equality in the triangle inequality.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Distances to a common tangent interpolate along three collinear circle centers.

## 1995 AIME Problem 9: An isosceles triangle with a tripled angle

In isosceles triangle ABC, AB=AC and altitude AM=11. A point D on AM satisfies AD=10 and ∠BDC=3∠BAC. If the triangle’s perimeter is a+√b, find a+b.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1995_AIME_Problems/Problem_9) · MAA AMC.

### Solution

Let θ=∠CAM. Symmetry gives ∠CDM=3θ, and DM=1. Thus tan 3θ/tanθ=(CM/1)/(CM/11)=11. Since 0<3θ<90°, all tangents and denominators are valid. Writing u=tanθ>0, the triple-angle identity gives (3−u²)/(1−3u²)=11, so u²=1/4. Therefore CM=11/2 and AC=11√5/2. The perimeter is 2 CM+2 AC=11+√605, yielding a+b=616.

**Answer:** 616.

**Methods:** angle multiplication, isosceles symmetry, tangent triple angle.

**Verification:** For u=1/2, tan 3θ=(3u−u³)/(1−3u²)=11/2, exactly the required CM/DM.

**Source comparison:** All five alternatives read. The tangent identity is shortest, while complex arguments require quadrant verification. The geometric angle bound 3θ<90° prevents spurious branches introduced by tangent periodicity. The longer synthetic construction reaches the same lengths.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. An altitude and a tripled apex angle lead to a tangent triple-angle equation.

## 1995 AIME Problem 11: A self-similar cut prism

An integer-sided rectangular prism has sorted sides $a\le b\le c$ with $b=1995$. A face-parallel cut produces a smaller similar prism. Count possible triples $(a,b,c)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1995_AIME_Problems/Problem_11) · MAA AMC.

### Solution

The similar piece has scale factor q<1 and sorted sides qa,qb,qc, two of which are unchanged original side lengths. The unchanged lengths cannot include c, since qc<c; they therefore are a and b, forcing qb=a and qc=b. Consequently $ac=b^2$ and $a<b<c$. Conversely any such factor pair works: cut the c-side to length $qa=a^2/b$, which is positive and less than c; the remaining two dimensions are a,b, as required. Now $1995=3\cdot5\cdot7\cdot19$, so $b^2$ has $3^4=81$ divisors. Excluding the central pair a=c=b and pairing reciprocal divisors gives $(81-1)/2=40$ triples.

**Answer:** 040.

**Methods:** factor pairing, hybrid geometry.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry, number_theory. Similarity under a planar cut constrains integer prism dimensions and their factor choices.

## 1995 AIME Problem 12: The internal dihedral angle of a square pyramid

A pyramid OABCD has square base ABCD and equal lateral edges OA,OB,OC,OD. Given ∠AOB=45°, its internal dihedral angle θ between faces OAB and OBC satisfies cosθ=m+√n. Find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1995_AIME_Problems/Problem_12) · MAA AMC.

### Solution

Scale the common lateral edge to √2. The perpendicular projections of A and C onto OB coincide at P, because both make angle 45° with OB; OP=1 and AP=CP=1. The internal dihedral angle is ∠APC. The cosine law in AOB gives AB²=4−2√2, so the square diagonal satisfies AC²=2AB²=8−4√2. Applying the cosine law in APC yields cosθ=(1+1−AC²)/2=−3+2√2=−3+√8. Hence m+n=5.

**Answer:** 005.

**Methods:** dihedral angles, orthogonal projections, square pyramids.

**Verification:** P lies on OB because OP=1<√2, and −3+2√2 lies between −1 and 0, as expected for the obtuse internal dihedral angle.

**Source comparison:** All three alternatives read. The projection method directly gives the internal angle. The normal-vector method first obtains its supplement and correctly reverses the cosine sign; that distinction must not be omitted.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Perpendicular projections onto a common edge give the internal dihedral angle.

## 1995 AIME Problem 14: Two equal chords and an asymmetric region

Two chords of length 78 in a circle of radius 42 meet at a point 18 from the center. Of the four regions they form, consider one bounded by chord segments of unequal lengths. Its area is mπ−n√d with d squarefree. Find m+n+d.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1995_AIME_Problems/Problem_14) · MAA AMC.

### Solution

Let O be the center and E the intersection. The distance from O to either chord is √(42²−39²)=9√3. If F is the midpoint of a chord, EF=√(18²−(9√3)²)=9, so its pieces have lengths 39−9=30 and 39+9=48. The two lines through E at that distance from O are symmetric about OE; the relevant acute angle between a 30-piece and a 48-piece is 60°. If their outer endpoints are U,V, the cosine law gives UV²=30²+48²−2·30·48·cos 60°=42². Thus arc UV has central angle 60°. The region is triangle EUV plus its circular segment: its area is (30·48/2)sin 60°+(π·42²/6−42²√3/4)=294π−81√3. Hence m+n+d=378.

**Answer:** 378.

**Methods:** equal chords, intersection geometry, circular segments.

**Verification:** The unequal chord pieces multiply to 30·48=1440=42²−18², agreeing with the intersecting-chord power identity.

**Source comparison:** The single alternative and its appended sine-area simplification were read. Its geometry and sector decomposition are valid; the sine formula replaces an unnecessary Heron calculation.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Equal chord distances fix a 60-degree intersection and a sector-minus-triangle area.

## 1996 AIME Problem 4: A cube’s perspective shadow

A unit cube rests on a horizontal plane. A point light source is directly above one upper vertex, at distance x from that vertex. The shadow area outside the cube’s footprint is 48. Find floor(1000x).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1996_AIME_Problems/Problem_4) · MAA AMC.

### Solution

The source is x+1 units above the plane, while the top face is x units below the source. Projection onto the plane therefore enlarges the top square by factor (x+1)/x=1+1/x. Its projected square contains the projections of all lower cube points and includes the unit footprint. Thus (1+1/x)²−1=48. Positivity gives 1+1/x=7, so x=1/6 and floor(1000x)=166.

**Answer:** 166.

**Methods:** perspective projection, similar triangles, shadow area.

**Verification:** For x=1/6 the enlargement factor is 7, giving total projected area 49 and exposed shadow area 48.

**Source comparison:** The sole alternative correctly includes the footprint to obtain a square of area 49. The new proof states the projection factor and why the top-face projection is the full shadow.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Perspective projection scales the cube’s top face into its square ground shadow.

## 1996 AIME Problem 13: An area ratio from projection onto a median

Triangle ABC has AB=√30, AC=√6, and BC=√15. A point D lies on the line through A and the midpoint of BC, with ∠ADB=90°, and segment AD bisects BC. Write [ADB]/[ABC]=m/n in lowest terms. Find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1996_AIME_Problems/Problem_13) · MAA AMC.

### Solution

Take A as the vector origin and write b=B,c=C,e=(b+c)/2 for the midpoint E of BC. The side lengths give b·c=(30+6−15)/2=21/2, hence |e|²=57/4 and b·e=81/4. Because BD is perpendicular to AD, D is the projection of B onto line AE, so D=(b·e/|e|²)e=(27/19)e. In particular E lies on AD, as required. Triangles ADB and AEB have the same altitude from B and base ratio AD/AE=27/19. Since [AEB]=[ABC]/2, the requested ratio is 27/38, yielding m+n=65.

**Answer:** 065.

**Methods:** median vectors, orthogonal projection, area ratios.

**Verification:** The projection multiplier 27/19 exceeds 1, so segment AD indeed contains the midpoint of BC.

**Source comparison:** Both alternatives correctly combine a median-length identity with right-triangle equations. The projection calculation determines D’s position and the area ratio at once, without assuming in advance that D lies beyond the midpoint.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A median vector and orthogonal projection determine the ratio of two triangle areas.

## 1996 AIME Problem 14: Cubes crossed by a space diagonal

A box of side lengths 150,324,375 is partitioned into unit cubes. Count cubes whose interiors meet a long diagonal.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1996_AIME_Problems/Problem_14) · MAA AMC.

### Solution

Parametrize the diagonal by $(150t,324t,375t)$, 0<t<1. A new cube begins at each distinct interior crossing of a coordinate-integer plane. The three crossing sets have sizes 149,323,374; pairwise overlaps have sizes $\gcd(150,324)-1=5$, $\gcd(324,375)-1=2$, $\gcd(150,375)-1=74$, and the triple overlap has size $\gcd(150,324,375)-1=2$. Inclusion-exclusion gives 767 crossing times. They divide the diagonal into 768 open intervals, each lying in exactly one cube interior. The answer is $768$.

**Answer:** 768.

**Methods:** inclusion-exclusion, lattice geometry.

**Verification:** Independent exact check passed: Built the exact union of all interior rational crossing times. Result 768. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 2 archived solution entries. Both sources use inclusion-exclusion of simultaneous coordinate-plane crossing times.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry, number_theory. Grid-plane crossings along a space diagonal are counted with gcd-based inclusion-exclusion.

## 1996 AIME Problem 15: A parallelogram determined by doubled angles

Diagonals of parallelogram ABCD meet at O. Both ∠CAB and ∠DBC equal twice ∠DBA. If ∠ACB=r∠AOB, find floor(1000r).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1996_AIME_Problems/Problem_15) · MAA AMC.

### Solution

Let θ=∠DBA. Then ∠CAB=∠DBC=2θ, ∠ACB=180°−5θ, and ∠AOB=180°−3θ, with 0<θ<36°. Since AO=CO, the sine law in ABO and CBO gives sin²2θ=sinθ sin 5θ. Put u=cos 2θ. Product-to-sum and the double/triple-angle formulas transform this equation into (u−1)(4u²−3)=0. The angle bound gives 0<u<1, so u=√3/2 and θ=15°. Therefore r=105/135=7/9 and floor(1000r)=777.

**Answer:** 777.

**Methods:** parallelogram diagonals, sine law, trigonometric factorization, angle bounds.

**Verification:** At θ=15°, sin²30°=sin 15°sin 75°=1/4, and the two requested angles are 105° and 135°.

**Source comparison:** All three alternatives read. Index 0 gives a valid factorization with a geometric branch choice. Index 1 miswrites the second quadratic root’s sign, and index 2 contains inconsistent angle labels. The explicit range 0<θ<36° selects the unique admissible root.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Parallelogram midpoint geometry yields a factored trigonometric equation for the angles.

## 1997 AIME Problem 2: Squares among grid rectangles

Let r be the number of rectangles and s the number of squares formed by the nine horizontal and nine vertical lines of a standard 8-by-8 board. Reduce s/r=m/n and find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1997_AIME_Problems/Problem_2) · MAA AMC.

### Solution

A rectangle is determined by two horizontal and two vertical boundary lines, so $r=\binom92^2=1296$. A square of side k cells has $(9-k)^2$ placements, giving $s=\sum_{j=1}^8j^2=204$. Thus $s/r=17/108$ and the answer is $125$.

**Answer:** 125.

**Methods:** grid counting, boundary choices.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Grid-line choices count rectangles while side-length classes count squares.

## 1997 AIME Problem 4: Four mutually tangent circles

Four circles of radii 5,5,8,r are mutually externally tangent. Write r=m/n in lowest terms and find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1997_AIME_Problems/Problem_4) · MAA AMC.

### Solution

Place the radius-5 centers at (−5,0),(5,0). The radius-8 center is then (0,12), after reflection if necessary, since its distances to them are 13. The fourth center is (0,t), with t²=(r+5)²−25=r²+10r. Tangency to the radius-8 circle gives |t−12|=r+8, so t=4−r or t=20+r. The latter would imply 400+30r=0, impossible for r>0. The former gives (4−r)²=r²+10r, so r=8/9 and m+n=17.

**Answer:** 017.

**Methods:** tangent circles, center distances, branch exclusion.

**Verification:** For r=8/9,t=28/9, the distances to the two radius-5 centers are 53/9 and to the radius-8 center are 80/9.

**Source comparison:** Both alternatives read. The coordinate method must exclude the second placement of the fourth center; doing so proves uniqueness. The Descartes alternative is correct here, although its general description of the smaller curvature branch as always enclosing is not universally valid.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Mutually tangent circle centers satisfy two distance equations with a unique positive radius.

## 1997 AIME Problem 6: An equilateral attachment and another regular polygon

An equilateral triangle A₁A₂B is attached externally to a regular n-gon A₁A₂…Aₙ. Find the largest n for which A₁,Aₙ,B can be three consecutive vertices of a regular polygon.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1997_AIME_Problems/Problem_6) · MAA AMC.

### Solution

To bound the maximum it suffices to consider n>6. The equal segments A₁Aₙ and A₁B then enclose angle 120°+360°/n, so A₁ must be the middle of the three consecutive vertices. If the new polygon has m sides, its interior angle gives 180°−360°/m=120°+360°/n. Rearranging yields (m−6)(n−6)=36, with m,n>6. Thus n−6≤36 and n≤42. Equality occurs for m=7,n=42: the two equal segments enclose precisely a regular heptagon’s interior angle, so they extend to its consecutive sides.

**Answer:** 042.

**Methods:** regular polygon angles, integer factorization, geometric attainability.

**Verification:** For n=42,120°+360°/42=900°/7=180°−360°/7. Independent exact check passed: Enumerate integer polygon angle compatibilities over the proven relevant range.

**Source comparison:** All three alternatives correctly solve the angle equation. The new proof explicitly treats the large-n regime relevant to maximality and explains why the shared vertex is the middle vertex of the second polygon.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory. Regular-polygon angle compatibility reduces to an integer factorization.

## 1997 AIME Problem 7: The midpoint time of a storm crossing

A car moves east at 2/3 mile per minute. A circular storm of radius 51 moves southeast at √2/2 mile per minute, initially centered 110 miles north of the car. If the car enters at t₁ and leaves at t₂, find (t₁+t₂)/2.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1997_AIME_Problems/Problem_7) · MAA AMC.

### Solution

Relative to the storm center, the car is at (t/6,t/2−110). Its squared distance is (5/18)t²−110t+12100. Entry and exit occur when this equals 51², so the two times are the roots of a quadratic with leading coefficient 5/18 and linear coefficient −110. Their average is 110/(2·5/18)=198.

**Answer:** 198.

**Methods:** relative motion, quadratic symmetry, Vieta formulas.

**Verification:** At t=198 the squared distance is 1210<2601, so two crossings do occur; their positive sum is 396 and positive product ensures both are after time zero.

**Source comparison:** All three alternatives read. Index 0 calls the quadratic vertex a maximum, although it is a minimum. Both the quadratic and relative-velocity projection methods correctly give the midpoint time without solving the individual entry and exit times.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Relative motion makes the average entry and exit time the minimum-distance time.

## 1997 AIME Problem 13: A wire graph made of unit diagonals

Let f(t)=abs(abs(abs(t)−2)−1). The planar set S is defined by f(x)+f(y)=1. Its total length is a√b with b squarefree. Find a+b.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1997_AIME_Problems/Problem_13) · MAA AMC.

### Solution

The equation forces |x|,|y|≤4. On each of the eight unit intervals between consecutive integers from −4 to 4, f is affine with slope ±1 and maps that interval onto [0,1]. Consequently, in each of the 64 unit squares of [−4,4]², the equation f(x)+f(y)=1 is exactly one diagonal of length √2. Different cell segments meet only at endpoints, so the total wire length is 64√2 and a+b=66.

**Answer:** 066.

**Methods:** absolute-value graphs, piecewise linear functions, grid decomposition.

**Verification:** The values of f at integers −4,…,4 alternate 1,0,1,0,1,0,1,0,1, so every unit cell contains one full diagonal.

**Source comparison:** All four alternatives read. Index 1 uses incorrect piecewise formulas outside their valid intervals. Indices 2 and 3 assert that each absolute value always multiplies total length by a fixed factor, which is false without domain and overlap checks. The unit-cell argument verifies exactly where every segment lies.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A piecewise-linear absolute-value function makes one diagonal segment in every unit grid cell.

## 1997 AIME Problem 14: A short arc probability

Two distinct 1997th roots of unity are chosen uniformly. Find numerator plus denominator for the chance that $|v+w|\ge\sqrt{2+\sqrt3}$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1997_AIME_Problems/Problem_14) · MAA AMC.

### Solution

If $\theta$ is their shorter angular separation, then $|v+w|^2=2+2\cos\theta$. The condition is $\cos\theta\ge\sqrt3/2$, or $\theta\le30^\circ$. Fixing $v$, the circular step distance can be any of $1,\ldots,\lfloor1997/12\rfloor=166$ in either direction. Thus 332 of the 1996 possible values of $w$ qualify. The probability is $83/499$, giving $582$.

**Answer:** 582.

**Methods:** cyclic symmetry, geometric probability.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 4 archived solution entries. Valid sources use rotation invariance and the cosine of the angular separation; one geometric derivation has incorrect equations.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry, algebra. Angular differences between roots of unity count pairs satisfying a vector-sum bound.

## 1997 AIME Problem 15: A rigorous maximum equilateral triangle in a rectangle

An equilateral triangle lies entirely inside a 10 by 11 rectangle. Its largest possible area is p√q−r, where q is squarefree. Find p+q+r.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1997_AIME_Problems/Problem_15) · MAA AMC.

### Solution

Any triangle has a vertex attaining two adjacent extrema of its axis-aligned bounding box, because four extrema are attained by three vertices. Reflect the picture so this vertex is both leftmost and lowest. For an equilateral triangle of side s, its two outgoing sides then make angles θ and θ+60° with the horizontal, with 0≤θ≤30°. Its bounding-box width and height are s cosθ and s sin(θ+60°). Thus s≤min(11/cosθ,10/sin(θ+60°)). The first bound increases and the second decreases on this interval, so their minimum is maximized at their unique intersection. There s cosθ=11 and s sin(θ+60°)=10, giving s sinθ=20−11√3. Hence s²=11²+(20−11√3)²=884−440√3. This bounding box fits exactly, so the bound is attained. The area is s²√3/4=221√3−330, yielding p+q+r=554.

**Answer:** 554.

**Methods:** bounding boxes, orientation optimization, equilateral triangles, attainment.

**Verification:** The intersection satisfies tanθ=(20−11√3)/11, which lies between 0 and tan 30°, so the maximizing orientation is admissible.

**Source comparison:** All three alternatives assume, without proof, that an optimal triangle has a vertex at a rectangle corner and its other vertices on the opposite sides. Their subsequent computations are correct. The bounding-box argument proves the global optimization over all translations and orientations.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Orientation-dependent bounding-box widths give a rigorous maximum for an inscribed equilateral triangle.

## 1998 AIME Problem 2: Integer points between two slope bounds

Count positive integer pairs with $x\le2y\le60$ and $y\le2x\le60$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1998_AIME_Problems/Problem_2) · MAA AMC.

### Solution

The inequalities require $1\le x,y\le30$, excluding points with x>2y or y>2x. These exclusions are disjoint. For x>2y, y ranges from 1 to 14 and there are 30−2y choices of x. The excluded count on one side is $\sum_{y=1}^{14}(30-2y)=210$. Therefore $30^2-2(210)=480$ pairs remain.

**Answer:** 480.

**Methods:** complement, lattice points.

**Verification:** Independent exact check passed: Directly tested all bounded positive lattice pairs. Result 480. The written proof supplies the general/exhaustive justification.

**Source comparison:** Read and compared all 5 archived solution entries. The reliable sources use Pick’s theorem or explicit sums of lattice rows; pattern-only alternatives are not proofs.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Integer lattice points are counted in the region defined by paired ratio inequalities.

## 1998 AIME Problem 3: Factoring a graph into four half-lines

The graph y²+2 xy+40|x|=400 encloses one bounded region. Find its area.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1998_AIME_Problems/Problem_3) · MAA AMC.

### Solution

For x≥0 the equation factors as (y+20)(y+2x−20)=0. For x≤0 it factors as (y−20)(y+2x+20)=0. The bounded region therefore has vertices (0,20),(20,−20),(0,−20),(−20,20). Its horizontal top and bottom edges each have length 20 and are 40 apart. Thus its area is 20·40=800.

**Answer:** 800.

**Methods:** absolute values, factored curves, parallelogram area.

**Verification:** Each stated vertex satisfies the original equation, and the bounded edges lie in the appropriate half-planes.

**Source comparison:** Both alternatives correctly factor the graph. The half-plane restrictions must be retained; treating all four factors as full lines would describe extra regions.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Factoring the absolute-value equation on two half-planes reveals a bounded parallelogram.

## 1998 AIME Problem 6: A geometric mean on a parallelogram transversal

In parallelogram ABCD, extend DA beyond A to P. The line PC meets AB at Q and diagonal DB at R. Given PQ=735 and QR=112, find RC.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1998_AIME_Problems/Problem_6) · MAA AMC.

### Solution

Triangles BRQ and DRC are similar, so QR/RC=BR/DR. Also triangles BRC and DRP are similar because BC∥DP, giving RC/RP=BR/DR. Consequently RC²=QR·RP. Since RP=PQ+QR=847, we obtain RC=√(112·847)=308.

**Answer:** 308.

**Methods:** similar triangles, parallelogram transversal, geometric mean.

**Verification:** 112·847=94864=308², and every segment length is positive.

**Source comparison:** Both alternatives are valid. The second identifies two matching similarity ratios directly and avoids an unnecessary quadratic expansion.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Two pairs of similar triangles give a geometric-mean identity along a transversal.

## 1998 AIME Problem 9: Overlapping coffee breaks

Two people arrive independently and uniformly during one hour and each stays m minutes. Their visits overlap with probability 40%. Write m=a−b√c with c squarefree and find a+b+c.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1998_AIME_Problems/Problem_9) · MAA AMC.

### Solution

The two arrival times form a uniform point in a 60-by-60 square. Nonoverlap is $|x-y|>m$, two corner triangles of total area $(60-m)^2$. Therefore $(60-m)^2/3600=3/5$. Taking the root with $0\le m\le60$ gives $m=60-12\sqrt{15}$ and $a+b+c=87$.

**Answer:** 087.

**Methods:** continuous probability, area complement.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 2 archived solution entries. The alternative conditions on one arrival time; its linear average needs the endpoint intervals to be handled correctly.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Uniform arrival pairs occupy a diagonal band in a square probability space.

## 1998 AIME Problem 10: A sphere tangent to eight spheres on a plane

Eight radius-100 spheres rest on a plane, with centers forming a regular octagon and each tangent to its two neighbors. A ninth sphere rests on the plane and is tangent to all eight. Its radius is a+b√c, with c squarefree. Find a+b+c.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1998_AIME_Problems/Problem_10) · MAA AMC.

### Solution

Let R be the octagon circumradius and r the ninth radius. Equal distances from the ninth center to all eight centers force its horizontal projection to be the octagon center. The octagon side is 200, so R²=200²/(2−√2). Tangency between the ninth sphere and any original sphere gives R²+(r−100)²=(r+100)², hence R²=400r. Therefore r=100/(2−√2)=100+50√2, and a+b+c=152.

**Answer:** 152.

**Methods:** sphere tangency, regular octagons, horizontal projection.

**Verification:** The derived radius is positive and gives center distance r+100 to every outer center while all spheres remain tangent to the plane.

**Source comparison:** Both alternatives correctly retain the vertical center difference, which is essential for spheres resting on one plane. Index 1 calls the octagon’s central 45° angle an interior angle; its cosine-law equation is nevertheless correct.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A regular-octagon circumradius and vertical center offsets determine a tangent sphere radius.

## 1998 AIME Problem 11: A cube section from its projected strip

Edges AB,BC,CD form a three-edge path in a cube, and AD is a body diagonal. Points P∈AB,Q∈BC,R∈CD satisfy AP=5, PB=15, BQ=15, CR=10. Find the area of the plane section through P,Q,R.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1998_AIME_Problems/Problem_11) · MAA AMC.

### Solution

Use coordinates A=(0,0,0), B=(20,0,0), C=(20,0,20), D=(20,20,20). Then P=(5,0,0), Q=(20,0,15), R=(20,10,20), so their plane is y=10−2x+2z. Its projection onto the xz-plane is the part of the 20×20 square satisfying −5≤z−x≤5. Removing the two corner triangles of leg 15 leaves projected area 400−225=175. Parametrizing the section as (x,10−2x+2z,z) gives constant area scale √(1+2²+2²)=3 relative to that projection. Therefore the section area is 3·175=525.

**Answer:** 525.

**Methods:** cube sections, orthogonal projection, plane area factor.

**Verification:** The section normal is (2,1,−2), of length 3, so projection onto the plane with normal (0,1,0) reduces area by exactly 1/3. Independent exact check passed: Compute the section area squared from the six spatial vertices by the vector polygon-area formula.

**Source comparison:** Both alternatives correctly identify the hexagonal section and obtain 525, despite the primary answer field being blank. Their final symmetry and shape decomposition need care; projection to a strip gives the area directly without reconstructing every side length.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A cube cross-section projects to a diagonal strip with a constant area scale factor.

## 1998 AIME Problem 12: A golden-ratio configuration in a medial triangle

In equilateral triangle ABC, D,E,F are the midpoints of BC,CA,AB. Points P∈DE,Q∈EF,R∈FD satisfy P∈CQ, Q∈AR, and R∈BP. If [ABC]/[PQR]=a+b√c with c squarefree, find a²+b²+c².

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1998_AIME_Problems/Problem_12) · MAA AMC.

### Solution

Affine maps preserve collinearity and area ratios, so use A=(0,0),B=(2,0),C=(0,2), giving D=(1,1),E=(0,1),F=(1,0). Write P=(p,1),Q=(q,1−q),R=(1,r). The three collinearities respectively give p=q/(1+q), q=1/(1+r), and r=1/(2−p). Eliminating p,q yields r²+r−1=0. Since 0≤r≤1, r=(√5−1)/2, q=r, and p=1−r. These values lie in the required segments and satisfy all three equations, proving existence and uniqueness. Triangle DEF has area 1/2; each of the three corner triangles cut off by PQR has area r(1−r)/2. Thus [PQR]=(1−3r(1−r))/2=(7−3√5)/2. Since [ABC]=2, their ratio is 4/(7−3√5)=7+3√5. The answer is 7²+3²+5²=83.

**Answer:** 083.

**Methods:** affine normalization, cyclic collinearity, golden ratio, area ratios.

**Verification:** With r²=1−r, the parameters satisfy all three collinearities and lie strictly between 0 and 1; the reciprocal area ratio rationalizes exactly to 7+3√5.

**Source comparison:** Both alternatives read. Both assume equal cyclic segment ratios without proving them. Index 0 uses a similarity involving the wrong vertex and obtains the complementary segment value; the symmetric area expression hides this error. Index 1 contains multiple sign errors in its polynomial substitutions. The three affine collinearity equations prove the unique configuration and show the area ratio holds for every nondegenerate triangle.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Cyclic collinearity constraints determine a unique medial-triangle configuration and its affine area ratio.

## 1999 AIME Problem 2: A congruent cut through a parallelogram center

A line through the origin cuts the parallelogram with vertices (10,45),(10,114),(28,153),(28,84) into two congruent polygons. If its slope is m/n in lowest terms, find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1999_AIME_Problems/Problem_2) · MAA AMC.

### Solution

The parallelogram center is the midpoint of opposite vertices (10,45),(28,153), namely (19,99). Every line through that center bisects its area by a half-turn. For a fixed direction, translating a line away from the center strictly increases the area on one side while it intersects the interior, so no other parallel line can bisect the area. Congruent pieces have equal area; hence the given line passes through (19,99). Its slope is 99/19, already reduced, and m+n=118. The central half-turn also proves the resulting pieces are congruent.

**Answer:** 118.

**Methods:** central symmetry, area bisection, parallelogram centers.

**Verification:** The line y=99x/19 meets both vertical sides within their stated segments, and the half-turn about (19,99) exchanges the pieces.

**Source comparison:** All four alternatives read. The centroid shortcut and direct center assertion need a necessity argument; equal-area cuts and strict monotonicity supply it. The coordinate alternatives assume the cut meets the two long sides, which can be checked after finding the line.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A line bisecting a centrally symmetric convex region’s area must pass through its center.

## 1999 AIME Problem 4: The intersection of two concentric unit squares

Two unit squares have the same center and intersect in an octagon. One side of the octagon has length 43/99. If its area is m/n in lowest terms, find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1999_AIME_Problems/Problem_4) · MAA AMC.

### Solution

Quarter-turn symmetry cycles the four octagon sides lying on either square. Reflection in an axis halfway between corresponding square axes exchanges the two squares and therefore exchanges these two four-side families. Thus all eight octagon sides have length 43/99. Every side lies on a square side, at distance 1/2 from the common center. Joining the center to the eight vertices partitions the octagon into triangles of area (1/2)(43/99)(1/2). Its area is 8·43/396=86/99, and m+n=185.

**Answer:** 185.

**Methods:** concentric squares, symmetry, tangential polygon area.

**Verification:** The area equals inradius times semiperimeter: (1/2)·(4·43/99)=86/99.

**Source comparison:** Both alternatives read. The first asserts congruence of the eight center triangles; the two symmetries stated here prove the equal side lengths directly. The corner-triangle subtraction in index 1 gives an independent area computation.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Symmetry of two concentric congruent squares makes their intersection octagon equilateral and tangential.

## 1999 AIME Problem 6: Square roots turn a quadrilateral into an annular sector

Apply (x,y)↦(√x,√y) to the region enclosed by (900,300),(1800,600),(600,1800),(300,900). If its image has area k, find floor(k).

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1999_AIME_Problems/Problem_6) · MAA AMC.

### Solution

The original region is bounded by y=x/3, y=3x, and x+y=1200,2400. In image coordinates (u,v), these become v=u/√3, v=√3u, and u²+v²=1200,2400. Thus the image is an annular sector between angles 30° and 60°. Its area is (30/360)π(2400−1200)=100π, whose floor is 314.

**Answer:** 314.

**Methods:** nonlinear coordinate maps, annular sectors, region transformations.

**Verification:** The square-root map is a bijection on the positive quadrant, and 314<100π<315.

**Source comparison:** The sole alternative correctly transforms the entire boundary rather than treating the image as the straight-edged quadrilateral joining the transformed vertices.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Coordinate square roots map the quadrilateral into an annular sector.

## 1999 AIME Problem 8: Exactly two thresholds on a simplex

On the nonnegative triangle $x+y+z=1$, take points satisfying exactly two of $x\ge1/2,y\ge1/3,z\ge1/6$. If their area fraction is $m/n$ reduced, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1999_AIME_Problems/Problem_8) · MAA AMC.

### Solution

The region satisfying $x\ge a,y\ge b$ is a translated copy of the original simplex scaled by $1-a-b$, so its area fraction is $(1-a-b)^2$. For the three pairs of thresholds, the residual scales are $1/6,1/3,1/2$. Their triple intersection is only the point $(1/2,1/3,1/6)$, since the thresholds sum to 1, so overlaps have zero area. The desired fraction is $1/36+1/9+1/4=7/18$, giving $25$.

**Answer:** 025.

**Methods:** exact multiplicity, geometric probability.

**Verification:** The derivation yields the answer in the independently hosted answer field; no separate exhaustive computation claimed.

**Source comparison:** Read and compared all 1 archived solution entries. The first archived solution uses the same central counting model; this is a newly written exposition after consultation.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. A simplex probability region is partitioned by which two coordinate thresholds hold.

## 1999 AIME Problem 9: An equidistant complex multiplier

For positive real a,b, the map f(z)=(a+bi)z sends every complex z to a point equidistant from z and 0. Given |a+bi|=8 and b²=m/n in lowest terms, find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1999_AIME_Problems/Problem_9) · MAA AMC.

### Solution

Apply the condition to z=1. It gives |a+bi−1|=|a+bi|, so (a−1)²+b²=a²+b² and a=1/2. The modulus condition then yields b²=64−1/4=255/4. Therefore m+n=259. Conversely, |a+bi−1|=|a+bi| implies the required equality for every z after multiplying both sides by |z|.

**Answer:** 259.

**Methods:** complex similarity, perpendicular bisectors, modulus identities.

**Verification:** The two multiplier moduli |1/2+bi| and |−1/2+bi| are equal for every real b, verifying the global condition.

**Source comparison:** All six alternatives read. Index 3 mislabels a hypotenuse factor and attributes the first-quadrant condition to z rather than the multiplier. Index 4 misexpands the imaginary coordinate. Testing z=1 is sufficient and avoids divisions by arbitrary coordinates or by z=0.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Equidistance under complex multiplication forces the multiplier’s real part to be one half.

## 1999 AIME Problem 12: A triangle from inradius and two tangent lengths

The incircle of triangle ABC has radius 21 and touches AB at P, with AP=23 and PB=27. Find the triangle’s perimeter.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1999_AIME_Problems/Problem_12) · MAA AMC.

### Solution

Equal tangent segments from each vertex let the three tangent lengths be 23,27,x, so the semiperimeter is s=50+x. The area is 21s, while Heron gives area squared s·23·27·x. Equating yields 441s²=621 sx. Since s>0, cancel s to get 441(50+x)=621x, hence x=245/2. The perimeter is 2s=100+245=345.

**Answer:** 345.

**Methods:** incircle tangent lengths, Heron formula, area equals inradius times semiperimeter.

**Verification:** The resulting sides are 50,291/2,299/2, satisfying all triangle inequalities; Heron divided by s² gives inradius squared 441.

**Source comparison:** All four entries read, including a diagram-only first entry. The Heron and half-angle approaches are valid. The last entry calls x an unknown side although its equations use the third tangent length; the new notation removes that ambiguity.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Tangent-length variables combine the inradius area formula with Heron’s formula.

## 1999 AIME Problem 14: The common angle at a Brocard point

Inside a triangle with AB=13, BC=14, CA=15, a point P satisfies ∠PAB=∠PBC=∠PCA=θ. Write tanθ=m/n in lowest terms and find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1999_AIME_Problems/Problem_14) · MAA AMC.

### Solution

Put U=13·AP+14·BP+15·CP. Apply the cosine law in PAB,PBC,PCA and add: the three squared distances from P cancel, leaving 2Ucosθ=13²+14²+15²=590. The triangle area is √(21·8·7·6)=84. Adding the three subtriangle areas gives Usinθ/2=84. Thus tanθ=168/295, already reduced, and m+n=463.

**Answer:** 463.

**Methods:** Brocard angle, cyclic cancellation, cosine law, area decomposition.

**Verification:** The general identity gives tanθ=4·84/590=168/295, and gcd(168,295)=1.

**Source comparison:** All five entries read, including the diagram-only entry 0. The summed cosine-law and area proof is complete and proves the general identity cotθ=(a²+b²+c²)/(4K). Index 4 uses a confusing permutation of angle labels; its intended sine-law computation reaches the same ratio.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Summed cosine-law and area identities determine the common Brocard angle.

## 1999 AIME Problem 15: Folding a medial triangle into a tetrahedron

A paper triangle has vertices (0,0),(34,0),(16,24). Fold along the three sides of its medial triangle so the original vertices meet at a tetrahedron apex. Find the volume.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/1999_AIME_Problems/Problem_15) · MAA AMC.

### Solution

The medial base has vertices F=(17,0,0), E=(8,12,0), D=(25,12,0), with area 17·12/2=102. If the folded apex is V=(x,y,h), preserved edge lengths give VF²=17²=289, VE²=8²+12²=208, and VD²=9²+12²=225. Subtracting the VE² equation from VD² gives −34x+561=17, so x=16. Subtracting it from VF² gives −18x+24y+81=81, hence y=12. Then h²=289−(16−17)²−12²=144, so the height is 12. The volume is 102·12/3=408.

**Answer:** 408.

**Methods:** folded tetrahedra, distance equations, medial triangles, disphenoids.

**Verification:** At V=(16,12,12), squared distances to F,E,D are 289,208,225 exactly, matching all three folded edges. Independent exact check passed: Independent Cayley–Menger determinant from the six preserved edge lengths.

**Source comparison:** All five alternatives read. Index 0’s orthocenter argument is useful but its later altitude labels are inconsistent; index 1 omits the actual linear equations. The box/disphenoid methods give valid alternative formulas. The explicit squared-distance subtraction proves the height directly.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Folding along the medial triangle fixes three apex distances, determining tetrahedron height.

## 2000 AIME I Problem 2: A reflected pentagon

Let $A=(u,v)$, where $u,v$ are integers with $0<v<u$. Obtain $B,C,D,E$ successively by reflecting $A$ across $y=x$, $B$ across the $y$-axis, $C$ across the $x$-axis, and $D$ across the $y$-axis. If pentagon $ABCDE$ has area $451$, find $u+v$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

The points are $B=(v,u),C=(-v,u),D=(-v,-u),E=(v,-u)$. Rectangle $BCDE$ has area $4uv$; triangle $ABE$ has area $u(u-v)$. Hence $u(u+3v)=451=11\cdot41$. Since $u<u+3v$, the possible factor pairs are $(1,451)$ and $(11,41)$. They give $v=150$ and $v=10$, respectively. Only $(u,v)=(11,10)$ satisfies $v<u$, so the answer is $21$.

**Answer:** 021.

**Methods:** coordinate area, reflections, factorization.

**Verification:** Exhaustive bounded integer search of the reflected-polygon area equation.

**Source comparison:** Both downloaded solutions were checked: area decomposition and the shoelace formula yield the same factor equation.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory. Coordinate reflections give an area polynomial whose integral solutions are controlled by factorization.

## 2000 AIME I Problem 4: Nine-square dissection as a linear system

A rectangle is tiled by nine squares with side lengths $a_1<\cdots<a_9$. Their edge relations are $a_3=a_1+a_2$, $a_4=a_1+a_3$, $a_5=a_3+a_4$, $a_6=a_4+a_5$, $a_7=a_2+a_3+a_5$, $a_8=a_2+a_7$, $a_9=a_1+a_4+a_6$, and $a_6+a_9=a_7+a_8$. Its width is $a_8+a_9$ and height is $a_6+a_9$. If these dimensions are coprime integers, find its perimeter.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

Put $a_1=a,a_2=b$. Successive substitution gives $a_3=a+b$, $a_4=2a+b$, $a_5=3a+2b$, $a_6=5a+3b$, $a_7=4a+4b$, $a_8=4a+5b$, $a_9=8a+4b$. The final edge relation is $13a+7b=8a+9b$, so $5a=2b$. Thus the square sides are $t(2,5,7,9,16,25,28,33,36)$, and the rectangle dimensions are $69t,61t$. Because $61$ and $69$ are coprime, integer dimensions force $t$ to be an integer by Bezout; their coprimality then forces $t=1$. The perimeter is $2(69+61)=260$.

**Answer:** 260.

**Methods:** dissections, linear systems, primitive scaling.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three source entries were reviewed. The first two encode equivalent edge systems. The third normalizes a smallest square to 1 and glosses over the subsequent rescaling; the proof here makes primitive scaling explicit. The textual edge relations replace the source diagram.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Shared edges of a square dissection form a homogeneous linear system, followed by primitive integer scaling.

## 2000 AIME I Problem 8: Turning a cone of liquid upside down

A right circular cone of height $12$ and base radius $5$ contains liquid to depth $9$ when its vertex points down. After it is turned vertex-up, the liquid depth is $m-n\sqrt[3]{p}$, with positive integers $m,n,p$ and cube-free $p$. Find $m+n+p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

The liquid occupies $(9/12)^3=27/64$ of the cone. After inversion the empty region is a similar cone occupying $37/64$ of the volume, so its height is $12(37/64)^{1/3}=3\sqrt[3]{37}$. Thus the liquid depth is $12-3\sqrt[3]{37}$ and $m+n+p=52$.

**Answer:** 052.

**Methods:** solid similarity, volume scaling.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All four source entries use equivalent similar-cone volume calculations and were checked.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Similarity makes volume a cube of the corresponding cone height.

## 2000 AIME I Problem 13: Fast highways and a slower prairie

Two perpendicular highways cross at the fire station. A truck travels at $50$ miles per hour on either highway and $14$ miles per hour elsewhere. The area it can reach in six minutes is $m/n$ square miles in lowest terms. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

An off-road segment joining highways can be replaced by highway travel through their intersection without increasing time: $(|a|+|b|)/50\le\sqrt{a^2+b^2}/14$. Segments returning to the same highway can likewise be replaced. Thus an optimal route uses one highway and then a straight off-road segment. In the sector $x\ge y\ge0$, for an exit $(s,0)$ the inequality $7(x-s)+24y\le25\sqrt{(x-s)^2+y^2}$ gives travel time at least $(7x+24y)/350$ (also using $|s|\ge s$). Equality occurs at $s=x-7y/24\ge0$. Negative exits are no better than the origin. For a nonnegative exit distance $s$, the squared distance from $(0,s)$ to $(x,y)$ exceeds that from $(s,0)$ by $2s(x-y)\ge0$. Thus the x-axis route is at least as good as any y-axis route. Hence the six-minute boundary is $7x+24y=35$ in this sector, with its reflection in $y=x$ in the other half-quadrant. The first-quadrant region has vertices $(0,0),(5,0),(35/31,35/31),(0,5)$ and area $175/31$. Multiplying by four gives $700/31$, so the answer is $731$.

**Answer:** 731.

**Methods:** geometric optimization, reachable regions, Cauchy inequality.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The single downloaded solution constructs an envelope of circles and its tangent line. Its geometric result is correct. The present proof explicitly reduces routes and explains the minimizing highway exit.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The reachable set is determined by a sharp weighted travel-time inequality, producing a polygonal envelope.

## 2000 AIME I Problem 14: An isosceles chain of equal segments

In triangle $ABC$, $AB=AC$. Points $P$ on $AC$ and $Q$ on $AB$ satisfy $AP=PQ=QB=BC$. Find $\lfloor1000\angle ACB/\angle APQ\rfloor$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Scale the four equal lengths to 1 and let $\angle A=\alpha$. Since $AP=PQ$, triangle $APQ$ has equal angles $\alpha$ at $A,Q$, so $AQ=2\cos\alpha$ and $AB=1+2\cos\alpha$. Bisecting the apex angle of $ABC$ yields $1=2AB\sin(\alpha/2)=2\sin(\alpha/2)(1+2\cos\alpha)=2\sin(3\alpha/2)$. Because $BC<AB$, the opposite angle $\alpha$ is smaller than either base angle, so $0<\alpha<60^\circ$. Thus $3\alpha/2=30^\circ$ and $\alpha=20^\circ$. The required ratio is $80/140=4/7$, giving $571$.

**Answer:** 571.

**Methods:** isosceles triangles, trigonometric identities, angle constraints.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All five entries were reviewed: angle chasing, an auxiliary rhombus, sine-law calculations, and triple-angle identities. The acute range used here explicitly rules out the extraneous sine branch.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Two isosceles triangles reduce the angle condition to a triple-angle sine identity.

## 2000 AIME II Problem 6: A parallel area bisector

The bases of a trapezoid differ by $100$. Its midline divides its area in the ratio $2:3$. A parallel segment of length $x$ bisects its area. Find $\lfloor x^2/100\rfloor$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

Let the smaller base be $b$. The midline has length $b+50$, and the two half-height trapezoids give $(2b+50)/(2b+150)=2/3$. Thus $b=75$, and the larger base is $175$. At the section of length $x$, the fraction of total height measured from the smaller base is $(x-75)/100$. Therefore its area fraction is $(x-75)(x+75)/(175^2-75^2)$. Setting this equal to $1/2$ gives $x^2=(75^2+175^2)/2=18125$, so the answer is $181$.

**Answer:** 181.

**Methods:** trapezoids, area ratios, linear interpolation.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The single source was checked. Its similar-triangle construction yields the same squared-length relation; stating the interpolation directly also covers overhanging trapezoids.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Parallel-section lengths vary linearly with height, making cumulative area proportional to a difference of squared lengths.

## 2000 AIME II Problem 8: A right trapezoid with perpendicular diagonals

In trapezoid $ABCD$, $AB\parallel CD$, $BC$ is perpendicular to the bases, and $AC\perp BD$. Given $AB=\sqrt{11}$ and $AD=\sqrt{1001}$, determine $BC^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

Use coordinates $C=(0,0),B=(0,h),A=(\sqrt{11},h),D=(d,0)$, where $d>0$. The diagonal dot product gives $h^2=d\sqrt{11}$. The other leg gives $h^2+(d-\sqrt{11})^2=1001$. Substitution reduces this to $d^2-\sqrt{11}d-990=0=(d-10\sqrt{11})(d+9\sqrt{11})$. Positivity forces $d=10\sqrt{11}$, so $BC^2=110$.

**Answer:** 110.

**Methods:** coordinates, perpendicular diagonals, dot products.

**Verification:** Exact check of perpendicular-diagonal and leg-length equations.

**Source comparison:** All four source entries were reviewed. The first three are consistent similarity, vector, and orthodiagonal-quadrilateral arguments. Entry 3 contains sign changes and an incorrect relation between CD squared and BC squared before reaching the correct quadratic.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The diagonal dot product relates height squared to the product of the bases.

## 2000 AIME II Problem 10: Radius from four tangent lengths

A circle inscribed in convex quadrilateral $ABCD$ touches $AB$ at $P$ and $CD$ at $Q$. If $AP=19$, $PB=26$, $CQ=37$, and $QD=23$, find the square of its radius.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

Let the four tangent lengths from the vertices be $a,b,c,d=19,26,37,23$, and let the radius be $r$. If $\theta_i$ is the angle at the center between a vertex ray and either adjacent tangency radius, then $\tan\theta_i=a_i/r$ and $\sum\theta_i=\pi$. Consequently the product $(r+ia)(r+ib)(r+ic)(r+id)$ is real. Its imaginary part is $r^3(a+b+c+d)-r(abc+abd+acd+bcd)=0$. Hence $r^2=(abc+abd+acd+bcd)/(a+b+c+d)=67935/105=647$.

**Answer:** 647.

**Methods:** tangential quadrilaterals, half angles, symmetric polynomials.

**Verification:** Independent numerical half-angle closure check for the claimed inradius.

**Source comparison:** All three entries were reviewed. The tangent-addition method and the stated tangential-area formula agree. The proof here derives the needed symmetric identity and avoids divisions by potentially vanishing tangent-addition denominators.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The four half-angle tangent parameters satisfy a symmetric cubic-to-linear radius identity.

## 2000 AIME II Problem 11: Integral equal legs restrict base directions

An isosceles trapezoid $ABCD$ has integer-coordinate vertices, $A=(20,100)$, $D=(21,107)$, no horizontal or vertical side, and only $AB\parallel CD$. The sum of the absolute values of all possible slopes of $AB$ is $m/n$ in lowest terms. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Translate $A$ to the origin, and put $d=\overrightarrow{AD}=(1,7)$, $e=\overrightarrow{BC}$. Since the legs have equal lengths, $e$ is an integer vector of squared length 50, hence is one of $(\pm1,\pm7),(\pm7,\pm1),(\pm5,\pm5)$. Parallel bases force $\overrightarrow{AB}$ to be parallel to $d-e$. The four choices $(\pm1,\pm7)$ yield a parallelogram, degeneracy, or a horizontal or vertical base. The remaining eight give slopes $-1,-4/3,3/4,1,-1/2,-3,1/3,2$. Each is attainable: set $B=2(d-e)$ and $C=B+e$; the resulting quadrilateral is convex, has unequal parallel bases and equal nonparallel legs. The absolute slopes sum to $119/12$, so the answer is $131$.

**Answer:** 131.

**Methods:** integer coordinates, sum of two squares, vector geometry.

**Verification:** Enumerated all integer leg vectors of squared norm 50 and summed distinct admissible slopes.

**Source comparison:** Both downloaded entries were checked. The reflection formulation and direct leg-vector enumeration agree. The explicit construction here supplies sufficiency for every listed direction.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory. Equal integer-coordinate leg lengths restrict the second leg to representations of 50 as a sum of two squares.

## 2000 AIME II Problem 12: A triangular section of a sphere

Three points $A,B,C$ on a sphere of radius $20$ satisfy $AB=13$, $BC=14$, $CA=15$. The distance from the center to triangle $ABC$ is $m\sqrt n/k$, with $m,k$ coprime positive integers and square-free $n$. Find $m+n+k$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2000_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Let $H$ be the projection of the sphere center $O$ onto the plane of $ABC$. The equal distances $OA=OB=OC$ imply $HA=HB=HC$, so $H$ is the circumcenter. The triangle is acute since $15^2<13^2+14^2$, hence $H$ lies inside it and $OH$ is also the distance to the triangular region. Heron gives area $84$, so its circumradius is $13\cdot14\cdot15/(4\cdot84)=65/8$. Therefore $OH=\sqrt{400-(65/8)^2}=15\sqrt{95}/8$, and the requested sum is $118$.

**Answer:** 118.

**Methods:** sphere sections, circumradius, Heron formula.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both source entries were reviewed. The circumcenter method is valid. The coordinate alternative attributes a midpoint constraint to the wrong isosceles triangle in its prose. The acute-triangle check here distinguishes distance to the triangle from distance to its plane.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The perpendicular projection of the sphere center onto the triangle plane is the triangle circumcenter.

## 2001 AIME I Problem 4: An angle bisector creates an isosceles triangle

In triangle $ABC$, $\angle A=60^\circ$, $\angle B=45^\circ$. The internal bisector $AT$ meets $BC$ and has length $24$. Write the area as $a+b\sqrt c$, with positive integers and square-free $c$, and find $a+b+c$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

We have $\angle C=75^\circ$, $\angle CAT=30^\circ$, and $\angle ATC=75^\circ$. Thus $AC=AT=24$. Drop perpendicular $CH$ to $AB$. The $30$-$60$-$90$ triangle gives $AH=12$, $CH=12\sqrt3$; because $\angle B=45^\circ$, $BH=CH$. Therefore $[ABC]=\tfrac12(12+12\sqrt3)(12\sqrt3)=216+72\sqrt3$, and the answer is $291$.

**Answer:** 291.

**Methods:** angle bisectors, special triangles, area.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both source solutions were reviewed: sine-law area and perpendicular decomposition agree.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Angle chasing identifies a known side, after which special right triangles give area.

## 2001 AIME I Problem 5: Equilateral triangle in an ellipse

An equilateral triangle inscribed in $x^2+4y^2=4$ has vertex $(0,1)$ and an altitude on the $y$-axis. If its squared side length is reduced $m/n$, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

The other vertices have coordinates $(\pm u,v)$ with $u>0$. The equilateral altitude condition is $v=1-\sqrt3u$. Substitution into the ellipse gives $u^2+4(1-\sqrt3u)^2=4$, or $u(13u-8\sqrt3)=0$. Nondegeneracy gives $u=8\sqrt3/13$. The side length is $2u$, so its square is $768/169$ and the answer is $937$.

**Answer:** 937.

**Methods:** conics, equilateral triangles, coordinate substitution.

**Verification:** Substituted the two lower vertices into the ellipse and independently compared squared side lengths.

**Source comparison:** All seven entries were inspected, including the diagram-only entry 0. Entries 2 and 4 incorrectly impose the positive square-root branch for a vertex below the x-axis; entry 4 also uses an incorrect equilateral altitude formula. Entries 1, 3, and 5 are sound. Entry 6 has a reused point label but a valid affine-circle argument.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The horizontal base and equilateral altitude impose a line equation that intersects the ellipse in a quadratic.

## 2001 AIME I Problem 7: A parallel through the incenter

In triangle $ABC$, $AB=21$, $AC=22$, and $BC=20$. The line through the incenter parallel to $BC$ meets $AB,AC$ at $D,E$. Write $DE=m/n$ in lowest terms and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

Let the area be $K$, the inradius $r$, and the altitude to $BC$ be $h$. Then $r=K/s$ with $s=63/2$, while $h=2K/20$. Thus $r/h=20/63$. Similarity gives $DE/20=(h-r)/h=43/63$, so $DE=860/63$ and $m+n=923$.

**Answer:** 923.

**Methods:** incenter, parallel sections, area cancellation.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All seven entries were reviewed. The isosceles-perimeter, area, and mass-point methods agree. Entry 4 changes 43 to 41 and 63 to 61; entry 5 drops a factor of 2 in the altitude formula; entry 6 confuses a bisector length with its square and mislabels similar triangles. The area cancels before any Heron calculation is needed.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The ratio of inradius to altitude equals the opposite side divided by the perimeter.

## 2001 AIME I Problem 9: Area from symmetric side fractions

In triangle $ABC$ with sides $13,15,17$, points $D\in AB,E\in BC,F\in CA$ satisfy $AD/AB=p$, $BE/BC=q$, $CF/CA=r$, where $p,q,r>0$, $p+q+r=2/3$, and $p^2+q^2+r^2=2/5$. If $[DEF]/[ABC]=m/n$ in lowest terms, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

The corner-triangle area fractions are $p(1-r)$, $q(1-p)$, and $r(1-q)$. Therefore $[DEF]/[ABC]=1-(p+q+r)+(pq+qr+rp)$. Squaring the first given sum shows $pq+qr+rp=((2/3)^2-2/5)/2=1/45$. The desired fraction is $1-2/3+1/45=16/45$, yielding $61$.

**Answer:** 061.

**Methods:** area ratios, symmetric polynomials.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed. The corner-area and determinant methods are valid. Entry 2 sets p=0 despite strict positivity and assumes the area is invariant before proving it; that shortcut alone is incomplete. The numerical side lengths are unnecessary.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Subtracting the three corner triangles expresses the area ratio through the first two symmetric sums of the side fractions.

## 2001 AIME I Problem 10: Parity classes of lattice points

Choose two distinct points uniformly from $\{0,1,2\}\times\{0,1,2,3\}\times\{0,1,2,3,4\}$. Their midpoint belongs to the same set with probability $m/n$ in lowest terms. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

The midpoint has integer coordinates precisely when the endpoints agree in all three coordinate parities. Counting ordered pairs, including coincidences, gives $(2^2+1^2)(2^2+2^2)(3^2+2^2)=520$. Subtract the $60$ coincident pairs. Therefore $P=460/(60\cdot59)=23/177$, yielding $200$. The coordinate bounds automatically hold for every midpoint.

**Answer:** 200.

**Methods:** parity, probability, product principle.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. A lattice midpoint is integral exactly when the endpoints agree in each coordinate parity, enabling parity-class counting.

## 2001 AIME I Problem 12: Insphere of a coordinate tetrahedron

A sphere is inscribed in the tetrahedron with vertices $(0,0,0),(6,0,0),(0,4,0),(0,0,2)$. Its radius is reduced $m/n$. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

Tangency to the coordinate planes places the center at $(r,r,r)$. The remaining face lies in $2x+3y+6z=12$, whose normal has length 7. Since the center is inside the tetrahedron, its distance to this plane is $(12-11r)/7$. Equating that distance to $r$ gives $18r=12$, hence $r=2/3$ and the answer is $5$.

**Answer:** 005.

**Methods:** inspheres, point-plane distance.

**Verification:** Exact inside point-plane distance check for the claimed insphere center.

**Source comparison:** All five entries were reviewed. The point-plane and volume/surface-area methods agree. Entry 3 misprints a normalized coefficient; entry 4 should specify the inside sign to exclude the exsphere solution. The stated proof uses that sign explicitly.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Tangency to the coordinate planes makes the center (r,r,r), reducing the fourth tangency to a point-plane distance.

## 2001 AIME I Problem 13: Three successive equal arcs

In a circle, a chord subtending an arc of $d^\circ$ has length $22$, and the chord of a $2d^\circ$ arc is $20$ longer than the chord of a $3d^\circ$ arc, where $0<d<120$. If the latter chord is $-m+\sqrt n$, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Take four successive points on the circle separated by arcs of $d^\circ$. The three consecutive sides have length 22, the fourth side has length $x$, and both diagonals have length $x+20$. Ptolemy gives $22^2+22x=(x+20)^2$, or $x^2+18x-84=0$. Positivity selects $x=-9+\sqrt{165}$, so the answer is $174$.

**Answer:** 174.

**Methods:** Ptolemy theorem, chord identities.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three source entries were reviewed. Ptolemy and the two trigonometric eliminations give the same quadratic. Taking four successive points makes the chord incidences explicit without a diagram.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Ptolemy links the chords of one, two, and three equal arcs without computing the radius.

## 2001 AIME I Problem 15: Hamilton cycles in a cube complement

Label the eight faces of a regular octahedron randomly by $1,\ldots,8$. No consecutive labels, including $8,1$, may share an edge. Express the probability as reduced $m/n$ and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Dualize the faces to cube vertices. Allowed consecutive moves form two disjoint $K_4$ graphs joined by a perfect matching. A Hamilton cycle uses either two or four matching edges. With two, choose their endpoints in $\binom42=6$ ways and order the two internal vertices in each $K_4$ in $2!^2$ ways: $24$ undirected cycles. With four, choose one of three perfect matchings inside the first $K_4$ and one of two different matchings inside the second: $6$ cycles. Thus there are $30\cdot8\cdot2=480$ labelings among $8!$, giving $1/84$ and answer $85$.

**Answer:** 085.

**Methods:** graphs, Hamilton cycles, probability.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 3: The proposed unique-completion claim is false: some partial assignments have zero or two completions. The later averaging remark does not prove the claimed bijection.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Octahedral face adjacency is the cube graph, and acceptable cyclic labelings are counted in its complement.

## 2001 AIME II Problem 4: A prescribed midpoint between two lines

Points $P,Q$ lie on $8y=15x$ and $10y=3x$, respectively, and have midpoint $(8,6)$. If $PQ=m/n$ in lowest terms, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

Write $P=(a,15a/8)$ and $Q=(b,3b/10)$. The midpoint equations are $a+b=16$ and $15a/8+3b/10=12$. They give $a=32/7,b=80/7$. Thus $Q-P=(48/7,-36/7)$, whose length is $60/7$. The answer is $67$.

**Answer:** 067.

**Methods:** midpoints, coordinates.

**Verification:** Exact endpoint substitution, midpoint check, and squared-distance calculation.

**Source comparison:** The sole source was reviewed; its midpoint system and distance calculation are correct.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The midpoint condition gives a two-by-two linear system for the endpoints.

## 2001 AIME II Problem 6: A small square between a chord and a circle

A unit-area square $ABCD$ is inscribed in a circle. Another square $EFGH$ has $E,F$ on side $CD$ and $G,H$ on the circle. Its area is reduced $m/n<1$. Find $10n+m$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

Place the circle center at the origin and $CD$ on $y=1/2$; the radius squared is $1/2$. If the second square has side $u$, the chord $GH$ is parallel to $CD$ and centered on the y-axis, so its endpoints have x-coordinates $\pm u/2$ and y-coordinate $1/2\pm u$. The circle equation gives $5u^2\pm4u-1=0$. For the inward square the positive root is $u=1$, excluded by the area condition. For the outward square it is $u=1/5$. Thus the area is $1/25$, and $10n+m=251$.

**Answer:** 251.

**Methods:** circle chords, squares, quadratic geometry.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries were reviewed. Their external-square calculation is correct. The proof here explicitly handles the inward orientation and excludes its unit-area square.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A chord midpoint fixes the smaller square centerline, and a quadratic selects the external square.

## 2001 AIME II Problem 7: Incircle cuts in a right triangle

In right triangle $PQR$ with $PQ=90$, $PR=120$, $QR=150$, the non-leg tangent to its incircle perpendicular to $PR$ cuts off triangle $RST$ at $R$; the analogous tangent perpendicular to $PQ$ cuts off triangle $QUV$ at $Q$. If the distance between the two new incenters is $\sqrt{10n}$, find $n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

Take $P=(0,0),Q=(90,0),R=(0,120)$. The original inradius is $(90+120-150)/2=30$, so the two tangent lines are $y=60$ and $x=60$. The triangle near $R$ is scaled by $60/120=1/2$, with inradius 15 and center $(15,75)$. The triangle near $Q$ is scaled by $30/90=1/3$, with inradius 10 and center $(70,10)$. Their squared distance is $55^2+65^2=7250$, giving $n=725$.

**Answer:** 725.

**Methods:** right-triangle inradius, similarity, coordinates.

**Verification:** Exact squared-distance check between the derived incenters; geometric center derivation remains analytic.

**Source comparison:** All four entries were reviewed. Coordinate and common-tangent decompositions agree. Entry 3 calls a five-vertex region a hexagon, but its distance calculation is unaffected.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Tangents parallel to the legs create similar right triangles with easily scaled inradii.

## 2001 AIME II Problem 12: Recursive tetrahedral growth

Begin with a unit-volume regular tetrahedron. At each stage replace the middle quarter-triangle of every triangular face by the three exposed faces of an outward regular tetrahedron. Find numerator plus denominator of the volume after three stages.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Each current triangular face produces six triangles of half its edge length: three old corner pieces and three new faces. Thus the number of new tetrahedra is multiplied by $6$ each stage while each new volume is multiplied by $1/8$. The added volumes are $1/2,3/8,9/32$. The final volume is $1+1/2+3/8+9/32=69/32$, so the answer is $101$.

**Answer:** 101.

**Methods:** recursive counting, geometric scaling.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. The iterative tetrahedral surface has a branching face count and a geometric series of added volumes.

## 2001 AIME II Problem 13: An angle bisector reveals a similarity

In convex quadrilateral $ABCD$, $\angle BAD=\angle ADC$ and $\angle ABD=\angle BCD$. Given $AB=8$, $BD=10$, $BC=6$, write $CD=m/n$ in lowest terms and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Put $\alpha=\angle BAD=\angle ADC$, $\beta=\angle ABD=\angle BCD$, and $\delta=180^\circ-\alpha-\beta=\angle ADB$. The quadrilateral angle sum gives $\angle DBC=2\delta$. Let its bisector meet $CD$ at $E$. Then triangles $EBC$ and $ADB$ have respective angles $(\alpha,\delta,\beta)$, so $CE/BC=AB/BD=4/5$, giving $CE=24/5$. The angle-bisector theorem gives $CE/ED=BC/BD=3/5$, hence $ED=8$. Thus $CD=64/5$, and the answer is $69$.

**Answer:** 069.

**Methods:** angle bisectors, similar triangles, angle sums.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed. The extension and angle-bisector constructions are correct. Entry 1 says BM is parallel to CD where its construction requires AD; the intended trapezoid argument is valid.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The quadrilateral angle sum doubles one triangle angle, so an angle bisector supplies a useful similar triangle.

## 2001 AIME II Problem 15: A triangular tunnel along a cube diagonal

In the cube $[0,8]^3$, drill the triangular prism parallel to $(1,1,1)$ whose cross-section has vertices $(2,0,0),(0,2,0),(0,0,2)$. Include the three tunnel walls in the remaining surface area. If that area is $m+n\sqrt p$, with positive integers and square-free $p$, find $m+n+p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2001_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

The prism is defined by $x+y-2z\le2$, $x+z-2y\le2$, and $y+z-2x\le2$. On each of the three faces incident to the origin, the removed area is a right triangle with legs 2, hence area 2. On each opposite face, local coordinates from $(8,8,8)$ give the quadrilateral $(0,0),(1,0),(2,2),(0,1)$, also area 2. Thus the exterior area left is $6\cdot64-12=372$. Parametrize the wall through $(2,0,0),(0,2,0)$ as $P(s,t)=(2-s+t,s+t,t)$. Inside the cube, $0\le s\le2$ and $0\le t\le6+\min(s,2-s)$. This parameter region is a $2$ by $6$ rectangle plus a triangle of area 1, totaling 13. The parameter directions $(-1,1,0)$ and $(1,1,1)$ are perpendicular with lengths $\sqrt2,\sqrt3$, so the wall area is $13\sqrt6$. The three congruent walls add $39\sqrt6$. The total is $372+39\sqrt6$, giving $417$.

**Answer:** 417.

**Methods:** solid geometry, surface area, parametric coordinates.

**Verification:** Computed the exact squared area of a tunnel wall from its five vertices using the polygon cross-product formula.

**Source comparison:** The single source was reviewed. Its decomposition into two trapezoids gives the correct wall area. The coordinate inequalities here independently justify the five-sided wall and both types of exterior opening, without relying on the perspective drawing.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Parametrizing each tunnel wall by its edge and diagonal directions turns its area into a simple polygon area.

## 2002 AIME I Problem 2: Three staggered rows of circles

Twenty congruent circles are packed in three horizontal rows of $7,6,7$. Adjacent circles in each row are tangent; each middle-row circle touches the two neighboring circles in each outer row. The enclosing rectangle is tangent to the extreme circles. Its longer-to-shorter side ratio is $(\sqrt p-q)/2$. Find $p+q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

Let the radius be $r$. The horizontal length is $14r$. Adjacent-row centers differ horizontally by $r$ and are $2r$ apart, so their vertical separation is $\sqrt3r$. The rectangle height is therefore $2r+2\sqrt3r$. Its aspect ratio is $7/(1+\sqrt3)=(7\sqrt3-7)/2=(\sqrt{147}-7)/2$, giving $154$.

**Answer:** 154.

**Methods:** circle packing, equilateral triangles.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries were reviewed. Entry 0 gives the correct dimensions. Entry 1 vaguely refers to three centers at distance 4 after normalizing r=1; the direct adjacent-row calculation here avoids that ambiguity. The row layout is explicitly restated.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Tangent-circle centers form equilateral triangles, determining the vertical row spacing.

## 2002 AIME I Problem 5: Squares through dodecagon vertices

How many squares in the plane have at least two vertices among the vertices of a fixed regular dodecagon?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

Each pair of dodecagon vertices defines three squares: one using the pair as a diagonal and two using it as a side. This gives $3\binom{12}{2}=198$ incidences. Any square having three dodecagon vertices lies on the same circumcircle, so also has its fourth vertex there. Exactly three squares have all four vertices in the dodecagon. Each was counted $\binom42=6$ times rather than once; subtract $3\cdot5$. The answer is $183$.

**Answer:** 183.

**Methods:** double counting, geometry hybrid.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Pairs of dodecagon vertices may be square sides or diagonals; incidence counting corrects repeated squares.

## 2002 AIME I Problem 10: Two area cuts along an angle bisector

Triangle $ABC$ is right at $B$, and its angle bisector $AD$ meets $BC$. Points $E\in AB,F\in AC$ satisfy $AE=3,EB=9,AF=10,FC=27$. Let $G=AD\cap EF$. Find the integer nearest to the area of quadrilateral $DCFG$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

We have $AB=12,AC=37$, so $BC=35$. The angle-bisector theorem gives $DC=35\cdot37/(12+37)=185/7$, hence $[ADC]=1110/7$. Also $\sin A=35/37$, so $[AEF]=\tfrac12\cdot3\cdot10\cdot35/37=525/37$. Since $AG$ bisects $\angle EAF$, the two triangles on its sides have area ratio $AF:AE=10:3$. Thus $[AGF]=\frac{10}{13}\frac{525}{37}=5250/481$. Subtracting gives $[DCFG]=497160/3367$, between $147.5$ and $148.5$, so the nearest integer is $148$.

**Answer:** 148.

**Methods:** angle bisectors, area ratios.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All four entries were reviewed. The exact area arguments are valid. Entry 1 rounds intermediate lengths without a rigorous error bound, and entry 2 leaves its coordinate computation unstated. The missing diagram incidence G=AD intersection EF is restored in the restatement.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The angle bisector controls both a base split and an internal area ratio, avoiding unnecessary lengths.

## 2002 AIME I Problem 11: Unfolding a reflected ray in a cube

A ray starts at a vertex of a cube of side $12$. Its first reflection is on the opposite face at offsets $7$ and $5$ from the two adjacent edges through the corresponding vertex. It reflects specularly until reaching another cube vertex. If the path length is $m\sqrt n$ with square-free $n$, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Unfold successive reflected cubes across their faces. The ray becomes the straight line $t(12,7,5)$, and cube vertices become points whose three coordinates are multiples of 12. The first coordinate forces integer t; then $7t$ being divisible by 12 forces $12\mid t$. The smallest positive possibility is $t=12$, and it also makes $5t$ divisible by 12. Thus the path length is $12\sqrt{12^2+7^2+5^2}=12\sqrt{218}$. Since $218=2\cdot109$ is square-free, the answer is $230$.

**Answer:** 230.

**Methods:** reflection unfolding, lattice intersections, least common multiples.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries were reviewed. Entry 1 gives a rigorous unfolded ray. Entry 0 describes the required 12 scale units as reflections, which can obscure additional side-face reflections; the unfolded parameter avoids this counting issue.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory. Unfolding makes the reflected path straight, and a vertex hit becomes simultaneous coordinate divisibility.

## 2002 AIME I Problem 13: A centroid and a secant through a midpoint

Triangle $ABC$ has medians $AD=18$ and $CE=27$, with $AB=24$. Extend $CE$ through $E$ to its second intersection $F$ with the circumcircle. If $[AFB]=m\sqrt n$ with square-free $n$, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Let $P$ be the centroid. Then $AP=12$, $EP=9$, and $AE=12$, so triangle $APE$ is isosceles with base 9. Its altitude to $EP$ is $\sqrt{12^2-(9/2)^2}=3\sqrt{55}/2$, yielding $[APE]=27\sqrt{55}/4$. The intersecting-chord theorem gives $EC\cdot EF=EA\cdot EB=144$, so $EF=16/3$. Triangles $AFE$ and $APE$ share the altitude to line CE, and $[AFB]=2[AFE]$. Therefore $[AFB]=2\cdot(16/27)\cdot27\sqrt{55}/4=8\sqrt{55}$, giving $63$.

**Answer:** 063.

**Methods:** centroid, power of a point, area transfer.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All five entries were reviewed. The centroid shortcuts avoid the first solution double median calculation. The barycentric entry 4 has reversed displacement labels and a missing symbol in one median identity; its final coordinates and area ratio are correct.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Centroid ratios give a small isosceles triangle, and intersecting chords transfer its area to the desired triangle.

## 2002 AIME I Problem 15: Coplanar faces determine a spatial edge

A polyhedron has faces $ABCD,ABFG,CDE,ADEG,BCEF,EFG$. The first is a square of side $12$; $ABFG$ is an isosceles trapezoid with $AB\parallel GF$, $AG=BF=8$, $GF=6$; and $CE=DE=14$. The distance from $E$ to square face $ABCD$ is $12$. If $EG^2=p-q\sqrt r$ with positive integers and square-free $r$, find $p+q+r$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Set $A=(0,0,0),B=(0,12,0),D=(12,0,0),C=(12,12,0)$. Equality $CE=DE$ gives $E=(x,6,h)$. The distance to the square forces $0\le x\le12$: if $x>12$, then $CE^2=12^2+6^2=180$, while if $x<0$, $CE^2=12^2-24x+180>324$, both impossible. Thus $h=12$ after choosing the upper side, and $(x-12)^2+36+144=196$ gives $x=8$. The trapezoid conditions put $G=(a,3,b)$, $F=(a,9,b)$. Plane $ADE$ has equation $z=2y$, so $b=6$. From $AG=8$, $a^2+3^2+6^2=64$, hence $a=\pm\sqrt{19}$. Therefore $EG^2=(8-a)^2+3^2+6^2=128\mp16\sqrt{19}$. The specified minus form selects $128-16\sqrt{19}$, yielding $163$.

**Answer:** 163.

**Methods:** polyhedron face planarity, coordinates, distance constraints.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed. The first two coordinate approaches are sound after making the projection-to-face condition explicit. Entry 0 swaps coordinate labels in its prose; entry 1 mislabels projection segments; entry 2 ends with an incorrect midpoint relation between different segments. The face-distance argument here excludes an otherwise possible exterior projection.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Face planarity fixes the height of a trapezoid vertex; distance equations then determine the remaining coordinate.

## 2002 AIME II Problem 2: An equilateral triangle of cube vertices

Three vertices of a cube are $(7,12,10),(8,8,1),(11,3,9)$. Find its surface area.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

Every pair of the given points has squared distance 98. For a cube of side s, squared vertex distances are $s^2,2s^2,3s^2$. Three pairwise adjacent vertices are impossible because the cube edge graph is bipartite; three pairwise opposite vertices are impossible because each vertex has only one opposite vertex. Thus the three distances are face diagonals, and $2s^2=98$. The surface area is $6s^2=294$.

**Answer:** 294.

**Methods:** cube vertices, distance geometry.

**Verification:** Exact pairwise squared-distance check for the three supplied cube vertices.

**Source comparison:** The sole source was reviewed. It recognizes an equilateral triangle of face diagonals; the proof here supplies the exclusion of the other distance types.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Equal pairwise cube-vertex distances force face diagonals rather than edges or body diagonals.

## 2002 AIME II Problem 4: Garden inside a hexagonal ring

Unit-side regular hexagonal tiles lie in a hexagonal grid. A single-cell-wide outer hexagonal ring has $202$ tiles along each straight side, including its corner tiles. Find the enclosed area excluding the ring, expressed as $m\sqrt3/2$, modulo $1000$ in the coefficient $m$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

A hexagonal ring at grid distance j from its center contains $6j$ cells; its side has $j+1$ cells. The boundary is therefore ring $j=201$, and the interior consists of the center and rings $1$ through $200$. It has $1+6(1+\cdots+200)=120601$ cells. A unit regular hexagon consists of six equilateral unit triangles and has area $3\sqrt3/2$. Hence $m=3\cdot120601=361803$, whose remainder is $803$.

**Answer:** 803.

**Methods:** hexagonal grids, polygon area, arithmetic sums.

**Verification:** Independently enumerated the enclosed hexagonal-grid cells in axial coordinates.

**Source comparison:** Both entries were reviewed. The direct ring count is correct. Entry 1 has inconsistent indexing in its named centered-hexagonal formula, so the explicit ring parameter is preferable. The grid arrangement is restated without the missing diagram.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Concentric hexagonal cell rings contain 6j cells, so summing the interior rings gives area.

## 2002 AIME II Problem 13: An affine height from intersecting cevians

In triangle $ABC$, $CD=2,DB=5$ on $BC$, and $CE=1,EA=3$ on $CA$, with $AB=8$. Let $P=AD\cap BE$. Through $P$, lines parallel to $CA,CB$ meet $AB$ at $Q,R$, respectively. If $[PQR]/[ABC]=m/n$ in lowest terms, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Assign weights 5,6,15 to $A,B,C$. The weighted average on BC is D because $BD:DC=15:6=5:2$, and the weighted average on AC is E because $AE:EC=15:5=3:1$. Thus the weighted average of all three vertices lies on both AD and BE, so $P=(5A+6B+15C)/26$. Its perpendicular height above AB is $15/26$ of the height of C. Triangle $PQR$ is similar to $CAB$, hence its area ratio is $(15/26)^2=225/676$. The answer is $901$.

**Answer:** 901.

**Methods:** barycentric coordinates, mass points, similarity.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed. The first two give valid mass-point calculations, though the second performs unnecessary extra work. Entry 2 mislabels P as Q and incorrectly sets PQ/AE equal to BP/PE; the correct ratio uses BP/BE. The weighted-average proof states the needed relation directly.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Barycentric weights determine the intersection height, which is also the similarity ratio of the small triangle.

## 2002 AIME II Problem 14: A circle centered on a leg of a right triangle

Right triangle $APM$ has right angle at $A$ and perimeter $152$. A circle of radius $19$, centered at $O\in AP$, is tangent to $AM$ and $PM$. Write $OP=m/n$ in lowest terms and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

Let $AM=b$ and $\theta=\angle AMP$. Tangency gives $AO=19$ and makes MO the internal angle bisector, so $t=\tan(\theta/2)=19/b<1$. The double-angle formulas give $AP/b=2t/(1-t^2)$ and $PM/b=(1+t^2)/(1-t^2)$. Therefore the perimeter is $2b/(1-t)=2b^2/(b-19)=152$. This simplifies to $(b-38)^2=0$, so $b=38$ and $t=1/2$. Hence $AP=b\cdot(2t)/(1-t^2)=152/3$, and $OP=AP-19=95/3$. The answer is $98$.

**Answer:** 098.

**Methods:** tangent circles, half-angle substitution, right triangles.

**Verification:** Exact Pythagorean, perimeter, and point-to-hypotenuse tangency checks for the derived right triangle.

**Source comparison:** All three entries were reviewed. Entries 0 and 2 yield valid similarity and half-angle arguments. Entry 1 includes unsupported square-root ratios and an incomplete elimination, so its numerical result is not a self-contained proof.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The center lies on the other vertex angle bisector, turning the perimeter condition into a perfect-square equation.

## 2002 AIME II Problem 15: Two tangent circles through one point

Two circles meet in two points, including $(9,6)$. Both are tangent to the x-axis and to $y=mx$, where $m>0$, and their radii have product $68$. Write $m=a\sqrt b/c$ in lowest radical form and find $a+b+c$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2002_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Both circles lie above the x-axis. They also lie on the same side of their other common tangent, since opposite-side disks could share at most a point on that line. Their centers therefore lie on the same angle-bisector ray and can be written $(kr_1,r_1),(kr_2,r_2)$. Passing through $(9,6)$ gives $k^2r^2-(18k+12)r+117=0$. The distinct circles have distinct radii, so Vieta gives $k^2=117/68$. Tangency to $y=mx$ gives $(1-km)^2=1+m^2$, hence $m=2k/(k^2-1)$. Because $m>0$ and $k^2>1$, k is positive. Thus $m=2\sqrt{117/68}/(49/68)=12\sqrt{221}/49$, and the answer is $282$.

**Answer:** 282.

**Methods:** circle tangency, Vieta formulas, angle bisectors.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed, including the parabola reinterpretation and explicit-center sidenote. Their main quadratic reductions agree. The original proofs assume the same angle-bisector branch; the shared-tangent separation argument here justifies that assumption.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The radii are roots of a common point-on-circle quadratic, so their product determines the common angle bisector.

## 2003 AIME I Problem 2: Alternating concentric annuli

Concentric circles have radii $1,2,\ldots,100$. Color the central disk red and alternate red and green on successive annuli. If the green area divided by the radius-100 disk area is reduced $m/n$, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

The green annuli have inner and outer radii $(2j-1,2j)$ for $1\le j\le50$. Their total area is $\pi\sum_{j=1}^{50}((2j)^2-(2j-1)^2)=\pi\sum_{j=1}^{50}(4j-1)=5050\pi$. Dividing by $10000\pi$ gives $101/200$, so the answer is $301$.

**Answer:** 301.

**Methods:** annular areas, arithmetic sums.

**Verification:** Direct exact sum of all 50 green annular area coefficients.

**Source comparison:** All three entries were reviewed, including the smaller-case pattern and alternate sum in entry 0. The exact arithmetic-series derivations are sound; the observed pattern alone would need proof.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Each green annulus has area given by a consecutive-square difference, so the total is an arithmetic sum.

## 2003 AIME I Problem 5: The unit neighborhood of a box

Find the volume of all points whose Euclidean distance from a $3$ by $4$ by $5$ rectangular box is at most 1. Write it as $(m+n\pi)/p$ with positive integers and $\gcd(n,p)=1$, and find $m+n+p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

Partition points by whether their nearest box point lies in the interior, a face, an edge, or a vertex. The box contributes 60. The six face slabs contribute $2(12+15+20)=94$. The twelve edge quarter-cylinders combine into three cylinders of lengths 3,4,5 and radius 1, contributing $12\pi$. The eight corner octants combine into one unit sphere, contributing $4\pi/3$. Thus the volume is $154+40\pi/3=(462+40\pi)/3$, and the answer is $505$.

**Answer:** 505.

**Methods:** parallel bodies, volume decomposition.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source was reviewed. Its geometric decomposition is correct; the nearest-point partition explains why the pieces exhaust the neighborhood without overlapping interiors.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Nearest-point regions of the box split into face slabs, edge quarter-cylinders, and corner sphere octants.

## 2003 AIME I Problem 6: Triangle types in a cube

Sum the areas of all triangles with vertices among the eight vertices of a unit cube. Write the sum as $m+\sqrt n+\sqrt p$ with integer parameters and find $m+n+p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

The $\binom83=56$ triangles split into three types. A face supplies four half-square triangles, giving $24$ of area $1/2$. Each cube edge belongs to two further right triangles with legs $1,\sqrt2$, giving $24$ of area $\sqrt2/2$. The remaining eight join three neighbors of one vertex and are equilateral with side $\sqrt2$, of area $\sqrt3/2$. Thus the sum is $12+12\sqrt2+4\sqrt3=12+\sqrt{288}+\sqrt{48}$, giving $348$.

**Answer:** 348.

**Methods:** double counting, geometry hybrid.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Cube-vertex triangles are classified by edge-distance patterns and their areas are summed with multiplicities.

## 2003 AIME I Problem 7: Integral distances in an isosceles triangle

Points $A,B,C$ are collinear in that order with $AB=9,BC=21$. A noncollinear point D satisfies $AD=CD$, and both AD and BD are integers. Find the sum of all possible perimeters of triangle ACD.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

The perpendicular bisector of AC contains D. The midpoint of AC is 15 from A and 6 from B. If $x=AD=CD$ and $y=BD$, subtracting the squared-distance equations gives $x^2-y^2=15^2-6^2=189$. The positive factor pairs for $(x-y,x+y)$ are $(1,189),(3,63),(7,27),(9,21)$, yielding $x=95,33,17,15$. The last gives zero height and is excluded; each other pair gives positive height and a valid D. The perimeter sum is $3\cdot30+2(95+33+17)=380$.

**Answer:** 380.

**Methods:** integer lengths, difference of squares.

**Verification:** Enumerated every possible equal-side length within the factor-pair bound and tested the second distance by integer square roots.

**Source comparison:** All three entries were reviewed. The perpendicular-bisector and cosine-law methods agree. Entry 1 reverses the sign after its correct Stewart equation; the required identity is AD squared minus BD squared equals 189.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory. Subtracting two right-triangle equations leaves a small difference-of-squares factorization.

## 2003 AIME I Problem 10: A hidden isosceles triangle from complementary angles

In isosceles triangle $ABC$, $AC=BC$ and $\angle ACB=106^\circ$. Interior point M satisfies $\angle MAC=7^\circ$ and $\angle MCA=23^\circ$. Find $\angle CMB$ in degrees.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

Scale $AC=BC=1$. Triangle AMC has angle $150^\circ$ at M, so the sine law gives $CM=\sin7^\circ/\sin150^\circ=2\sin7^\circ$. Also $\angle MCB=106^\circ-23^\circ=83^\circ$. The cosine law in CMB now yields $MB^2=1+4\sin^27^\circ-4\sin7^\circ\cos83^\circ=1$. Thus $MB=CB$, and its base angles at M,C are equal. Therefore $\angle CMB=83^\circ$.

**Answer:** 083.

**Methods:** sine law, cosine law, complementary angles.

**Verification:** Constructed M from its ray and sine-law distance, then independently checked the claimed hidden equal side numerically.

**Source comparison:** All seven entries were inspected, including diagram-only entry 0. The reflection and trigonometric methods agree. Entry 4 has incorrect equal-side labels and a mislabeled final angle; entry 5 finds a trigonometric-Ceva root by inspection without proving uniqueness; entry 6 uses an undefined point P and inconsistent side labels. The cosine-law proof makes the hidden isosceles relation explicit.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A sine-law length and one cosine-law expansion reveal equality of two sides.

## 2003 AIME I Problem 11: Triangle inequalities as interval probability

Choose $x$ uniformly from $(0,90^\circ)$. The probability that $\sin^2x,\cos^2x,\sin x\cos x$ fail to form a triangle is $d/n$, where $d$ is the degree measure of $\arctan m$ and $m+n<1000$. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Reflection $x\mapsto90^\circ-x$ preserves the event. On $(0,45^\circ)$ the largest length is $\cos^2x$, so failure means $\cos2x\ge\tfrac12\sin2x$, or $x\le\tfrac12\arctan2$. The two symmetric intervals have total length $\arctan2$, hence probability $(\arctan2)/90$. The requested value is $2+90=92$. Endpoints have probability zero.

**Answer:** 092.

**Methods:** continuous probability, symmetry.

**Verification:** Analytic derivation checked against the archived answer; not independently machine-checked.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry, algebra. A random angle produces a geometric-probability event governed by triangle inequalities and trigonometric thresholds.

## 2003 AIME I Problem 12: Equal opposite angles cancel two cosine laws

Convex quadrilateral $ABCD$ has $\angle A=\angle C$, $AB=CD=180$, $AD\ne BC$, and perimeter $640$. Find $\lfloor1000\cos A\rfloor$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

Put $u=AD,v=BC$. The two cosine laws for diagonal BD give $180^2+u^2-360u\cos A=180^2+v^2-360v\cos A$. Thus $(u-v)(u+v-360\cos A)=0$. Since $u\ne v$, and $u+v=640-360=280$, we obtain $\cos A=7/9$. Hence the requested floor is $777$.

**Answer:** 777.

**Methods:** cosine-law subtraction, quadrilaterals.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries were reviewed. The subtraction proof is direct and valid. The alternate ambiguous-SSA construction reaches the same relation but needs careful point ordering; no such auxiliary construction is needed here.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The common diagonal has two cosine-law expressions whose difference factors by the unequal sides.

## 2003 AIME I Problem 15: Median crossing a perpendicular to an angle bisector

Triangle $ABC$ has $AB=360,BC=507,CA=780$. Let M be the midpoint of CA and let the internal angle bisector BD meet CA at D. Through D draw the perpendicular to BD, meeting BC at F and BM at E. Write $DE/EF=m/n$ in lowest terms and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Put B at the origin and BD on the positive x-axis. With $u=360,v=507$ and half-angle $\theta$, write $A=(u\cos\theta,u\sin\theta)$, $C=(v\cos\theta,-v\sin\theta)$. Then $M=((u+v)\cos\theta/2,(u-v)\sin\theta/2)$. If $D=(d,0)$, the line DF is $x=d$. Its intersections with BC and BM have y-coordinates $-d\tan\theta$ and $d(u-v)\tan\theta/(u+v)$. Hence $DE/EF=(v-u)/(2u)=147/720=49/240$. The answer is $289$.

**Answer:** 289.

**Methods:** angle-bisector coordinates, medians, segment ratios.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All five entries were reviewed. The area, reflection, and mass-point methods agree. Entry 3 misorders its cross-ratio labels and changes DE to DF during the final ratio manipulation, so it is not reliable as written. The coordinate cancellation shows that CA is unnecessary for this ratio.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Coordinates aligned with the angle bisector cancel the angle and all scale factors from the requested segment ratio.

## 2003 AIME II Problem 4: The tetrahedron of face centroids

The centers of the four faces of a regular tetrahedron form another tetrahedron. Write the smaller-to-larger volume ratio as reduced $m/n$ and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

Let the original vertex vectors be $V_1,\ldots,V_4$ and their centroid G. The centroid of the face opposite $V_i$ is $(4G-V_i)/3=G-(V_i-G)/3$. Thus all four new vertices arise from the original ones by a homothety of ratio $-1/3$. Volume scales by the cube of the absolute ratio, so it is $1/27$, yielding $28$.

**Answer:** 028.

**Methods:** homothety, centroids, volume ratios.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three downloaded textual entries were reviewed; the external video reference was not watched. Coordinate, dihedral-angle, and altitude arguments agree. The affine centroid proof also works for nonregular tetrahedra when face centers mean centroids.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The face-centroid map is a homothety of ratio minus one third about the tetrahedron centroid.

## 2003 AIME II Problem 5: A tangent wedge of a cylinder

A cylindrical log has diameter $12$. A plane perpendicular to its axis and another plane making $45^\circ$ with it cut off a wedge. Their intersection line touches the log at exactly one point. If the wedge volume is $n\pi$, find n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

Choose the circular cross-section $x^2+y^2\le36$ and the first cut $z=0$. The intersection line is tangent to the cross-section, so the second cut may be written $z=x+6$ after rotating coordinates; the coefficient 1 expresses the $45^\circ$ angle. The heights above opposite points $(x,y)$ and $(-x,-y)$ sum to 12, so the mean height is 6. The volume is $6\cdot36\pi=216\pi$, giving $216$.

**Answer:** 216.

**Methods:** cylindrical wedges, symmetry, volume.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source was reviewed. Its two-congruent-wedges construction is valid; the complementary-height argument makes the volume relation explicit.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Opposite points of the circular cross-section have complementary heights, giving the average height directly.

## 2003 AIME II Problem 6: A triangle united with its centroid reflection

Triangle ABC has side lengths $13,14,15$ and centroid G. Reflect all three vertices through G to obtain triangle $A\prime B\prime C\prime$. Find the area of the union of the two triangular regions.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

Area ratios and centroid reflection are preserved by nonsingular affine maps. Normalize the original triangle to vertices $(0,0),(1,0),(0,1)$; its reflected vertices are $(2/3,2/3),(-1/3,2/3),(2/3,-1/3)$. Their intersection is obtained from the original by imposing $x\le2/3$, $y\le2/3$, $x+y\ge1/3$. These remove three disjoint corner triangles, each with area ratio $1/9$, so the overlap ratio is $2/3$. The union ratio is therefore $2-2/3=4/3$. Heron gives original area $\sqrt{21\cdot8\cdot7\cdot6}=84$, hence union area $112$.

**Answer:** 112.

**Methods:** affine invariance, centroid reflection, area unions.

**Verification:** Exact rational polygon clipping computed the intersection and union of the original 13-14-15 triangle and its centroid reflection.

**Source comparison:** All three entries were reviewed. Entry 0 incorrectly calls its small triangles congruent for a scalene original; equal areas are sufficient. Entry 2 provides a sound homothety argument. The affine calculation proves the ratio for every triangle.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. An affine normalization makes the overlap a triangle with three one-third-scale corners removed.

## 2003 AIME II Problem 7: A rhombus from two circumradii

In rhombus ABCD, triangles ABD and ACD have circumradii $25/2$ and $25$, respectively. Find the rhombus area.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

Let half of BD be u and half of AC be v. The side squared is $u^2+v^2$, and each triangle has area uv. The circumradius formula gives $(u^2+v^2)/(2v)=25/2$ and $(u^2+v^2)/(2u)=25$. Thus $u^2+v^2=25v=50u$, so $v=2u$ and $5u^2=50u$. Hence $u=10,v=20$, and the rhombus area is $(2u)(2v)/2=400$.

**Answer:** 400.

**Methods:** rhombi, circumradius, diagonals.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries were reviewed. The half-diagonal and extended-sine-law calculations are equivalent and valid.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Half-diagonals express both triangle circumradii through the same side-length square.

## 2003 AIME II Problem 11: Area using a perpendicular bisector as the base

Right triangle ABC has $AC=7$, $BC=24$, and right angle C. Let M be the midpoint of AB, and let D lie on C's side of AB with $AD=BD=15$. Write $[CDM]=m\sqrt n/p$ in lowest radical form and find $m+n+p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

We have $AB=25$, and D lies on the perpendicular bisector through M. Thus $DM=\sqrt{15^2-(25/2)^2}=5\sqrt{11}/2$. Let N be the perpendicular projection of C onto AB. The right-triangle projection formula gives $BN=BC^2/AB=576/25$, so $MN=576/25-25/2=527/50$. Since DM is perpendicular to AB, MN is the distance from C to line DM. Therefore $[CDM]=\tfrac12 DM\cdot MN=527\sqrt{11}/40$, yielding $578$.

**Answer:** 578.

**Methods:** right-triangle projections, perpendicular bisectors, area.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All four entries were reviewed. The projection, angle, and similar-triangle methods agree. Entry 2 has a mistaken repeated MD in its component-length equality, while its final coordinates are correct.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The midpoint and projection on the hypotenuse give the altitude to the isosceles-triangle axis.

## 2003 AIME II Problem 14: An equilateral hexagon with six prescribed heights

A convex equilateral hexagon ABCDEF has $A=(0,0)$, $B=(b,2)$, $\angle FAB=120^\circ$, and opposite sides parallel. Its vertex y-coordinates are exactly $0,2,4,6,8,10$. Write its area as $m\sqrt n$ with square-free n, and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2003_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

Let the first three directed sides be u,v,w. Convexity and equal opposite parallel sides make the remaining sides $-u,-v,-w$, so the vertices are $0,u,u+v,u+v+w,v+w,w$. Central symmetry makes opposite y-coordinates sum to 10. Thus $D_y=10,E_y=8$, while $(F_y,C_y)$ is either $(4,6)$ or $(6,4)$. Reflect horizontally if needed so $b>0$. Writing $s=F_y$, rotation through $120^\circ$ gives $u=(2(s+1)/\sqrt3,2)$ and $w=(-(s+4)/\sqrt3,s)$. If s=6, then $v_y=2$; equal lengths force either $v=u$, causing collinearity, or $v=(-14/\sqrt3,2)$, for which $u\times v>0$ but $v\times w<0$, contradicting convexity. Thus s=4. We obtain $u=(10/\sqrt3,2)$, $v=(8/\sqrt3,4)$, $w=(-8/\sqrt3,4)$; the other sign for v would make v=w. Shoelace on the six displayed vertices gives area $144/\sqrt3=48\sqrt3$, so the answer is $51$.

**Answer:** 051.

**Methods:** centrally symmetric polygons, convexity, coordinate area.

**Verification:** Exact scaled-coordinate checks of all six equal lengths, positive turns, and area; actual x-coordinates are divided by sqrt(3).

**Source comparison:** All four entries were reviewed. Every source assumes the crucial height order without a full exclusion of the alternative; the proof here supplies that missing convexity argument. Entry 2 includes an erroneous factor 1/2 in its parallelogram area display. Entry 3 misprints the negative root of its auxiliary quadratic.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Opposite parallel equal sides force central symmetry; convexity eliminates the competing height order before coordinates determine area.

## 2004 AIME I Problem 3: Pairs of polyhedron vertices

A convex polyhedron has $26$ vertices, $60$ edges, $24$ triangular faces and $12$ quadrilateral faces. Count pairs of vertices whose segment is neither an edge nor contained in a face.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

Every pair determines an edge, a face diagonal, or a space diagonal. There are $\binom{26}{2}=325$ pairs, $60$ edges, and $12\cdot2=24$ face diagonals. Convexity ensures a nonedge cannot be a diagonal in two distinct faces. The required count is $325-60-24=241$.

**Answer:** 241.

**Methods:** complement, geometric incidence.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Vertex pairs are counted after excluding edges and within-face diagonals of a convex polyhedron.

## 2004 AIME I Problem 4: Midpoints of sliding fixed-length chords

In a square of side 2, consider every length-2 segment with endpoints on adjacent sides. Its midpoints trace a closed boundary. If the enclosed area rounded to two decimal places is k, find $100k$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

For the corner at $(0,0)$, endpoints $(a,0),(0,b)$ satisfy $a^2+b^2=4$ and $0\le a,b\le2$. Their midpoint $(a/2,b/2)$ traces exactly the unit quarter-circle centered at that corner. The four corners give four such arcs, bounding the square with four unit quarter-disks removed. Thus the enclosed area is $4-\pi\approx0.858407$, which rounds to $0.86$. The answer is $86$.

**Answer:** 086.

**Methods:** loci, midpoints, circular areas.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed. The coordinate and rectangle-diagonal proofs establish the locus; the sliding-ladder analogy in entry 2 alone is less explicit about why every point of the arc occurs.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The midpoint of a segment joining perpendicular rays lies on a circle of half the segment length.

## 2004 AIME I Problem 8: Regular star polygons

Count similarity classes of connected regular $1000$-vertex star polygons with equal edge lengths and equal counterclockwise turning angles less than $180^\circ$, requiring a genuine edge crossing.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

Equal turns and lengths make successive edges a geometric progression of unit directions. Closure and distinct vertices therefore give the regular star $\{1000/k\}$, with $\gcd(k,1000)=1$. The counterclockwise turn condition chooses $1\le k<500$; $k=1$ is the convex polygon and must be excluded. Coprime residues pair as $k,1000-k$, so the number is $\varphi(1000)/2-1=400/2-1=199$.

**Answer:** 199.

**Methods:** cyclic permutations, totient, geometry hybrid.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry, number_theory. Star polygon connectivity is a coprimality condition on a cyclic step, followed by symmetry and crossing exclusions.

## 2004 AIME I Problem 9: Matching triangle-and-trapezoid dissections

A $3$-$4$-$5$ triangle and a $6$ by $7$ rectangle are each cut by one segment into a triangle U and a trapezoid V. The two U pieces are similar, and the two V pieces are similar. Find m+n if the smallest possible area of the triangle piece in the original triangle is reduced m/n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

A cut leaving a triangle and trapezoid in the original triangle is parallel to one side, so its triangle piece is similar to the whole $3$-$4$-$5$ triangle. In the rectangle, the cut joins a vertex to the opposite side; the removed right triangle must therefore have leg ratio $3:4$ or $4:3$. If its full rectangle leg is 6, the other leg must be $9/2$ (the alternative 8 exceeds 7); the remaining trapezoid has base ratio $(7-9/2)/7=5/14$. If its full leg is 7, the other is $21/4$ (the alternative $28/3$ exceeds 6), giving base ratio $(6-21/4)/6=1/8$. Similarity makes this base ratio the linear scale of the small triangle cut from the original. Both are attainable by a cut parallel to the appropriate leg; their right-trapezoid angles and base ratios match. The smaller area is $6(1/8)^2=3/32$, yielding $35$.

**Answer:** 035.

**Methods:** similar dissections, right trapezoids, case analysis.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source was reviewed. Its two admissible rectangle cuts are exhaustive. The proof here explicitly explains how the common base ratio determines the small triangle scale and why both cases are attainable.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Parallel cuts preserve the 3:4:5 triangle shape; the two possible rectangle cuts determine the trapezoid base ratios.

## 2004 AIME I Problem 10: A random disk avoids a diagonal

A unit-radius disk has its center uniformly distributed among positions where it fits in a $15\times36$ rectangle. Find numerator plus denominator of the probability that it misses a fixed diagonal.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

Allowed centers form a $13\times34$ rectangle. The centers of disks entirely on one side of the diagonal form the triangle obtained by shifting each side of a $15,36,39$ right triangle inward by one. Its original inradius is $(15+36-39)/2=6$, so the new triangle has similarity ratio $5/6$ and area $(15\cdot36/2)(5/6)^2=375/2$. The two sides contribute total area $375$. Thus $P=375/442$ and the answer is $817$.

**Answer:** 817.

**Methods:** continuous probability, geometry hybrid.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: For a nonsquare rectangle, the claimed diagonal reflection is not a symmetry. Central symmetry justifies the equal-area conclusion.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Allowed disk centers form a rectangle, and avoiding the diagonal is a geometric area probability.

## 2004 AIME I Problem 11: Equal painted-area and volume ratios

A cone of height 4 and radius 3 is painted on its entire exterior, including its base. A parallel cut separates a smaller cone C and a frustum F. Their painted-area ratio C:F equals their volume ratio C:F, namely reduced m/n. Find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

The original slant height is 5, so its lateral and total painted areas are $15\pi$ and $24\pi$. Let the smaller cone have linear scale t. Its painted-area fraction of the whole is $(15/24)t^2=(5/8)t^2$, while its volume fraction is $t^3$. Equal part-to-remainder ratios force these fractions equal, so $t=5/8$ since $t>0$. Therefore $m/n=t^3/(1-t^3)=125/387$, and $m+n=512$.

**Answer:** 512.

**Methods:** similarity exponents, painted surfaces, ratio conversion.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries were reviewed. Their radius and scale-factor calculations are correct. Passing directly to part-to-whole fractions cancels the common remainder denominators before solving.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Equality of part-to-remainder ratios is equivalent to equality of part-to-whole fractions, which exposes the scale exponents.

## 2004 AIME I Problem 12: Area selected by even logarithmic floors

Let S consist of $(x,y)\in(0,1]^2$ for which both $\lfloor\log_2(1/x)\rfloor$ and $\lfloor\log_5(1/y)\rfloor$ are even. If S has area reduced m/n, find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

For a base $b>1$, an even logarithmic floor selects intervals $(b^{-(2j+1)},b^{-2j}]$ for $j\ge0$. Their total length is $(1-1/b)\sum_{j\ge0}b^{-2j}=b/(b+1)$. The allowed x and y sets therefore have lengths $2/3$ and $5/6$. Since S is their Cartesian product, its area is $5/9$, giving $14$.

**Answer:** 014.

**Methods:** geometric series, floor functions, product regions.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source was reviewed. Its interval lengths and product calculation are correct; some endpoints are written open instead of closed, which does not affect area.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. The two independent coordinate conditions select geometric sequences of intervals, so their measures multiply.

## 2004 AIME I Problem 14: A taut rope partly wrapped around a cylinder

A rope of length 20 runs taut from ground level on a cylindrical tower of radius 8 to an endpoint 4 above ground and 4 from the tower surface. Part of the rope lies against the tower. Its contact length is $(a-\sqrt b)/c$, where a,b,c are positive integers and c is prime. Find a+b+c.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

In horizontal projection, the free segment is tangent to the radius-8 circle from distance 12 from its center, so its horizontal length is $\sqrt{12^2-8^2}=4\sqrt5$. Unroll the cylinder at the departure tangent plane. A taut rope is a straight segment in this development, so its total horizontal developed length is $\sqrt{20^2-4^2}=8\sqrt6$, with the same slope on its contact and free portions. Hence the free rope length is $20\cdot4\sqrt5/(8\sqrt6)=5\sqrt{30}/3$. The contact length is $20-5\sqrt{30}/3=(60-\sqrt{750})/3$. Thus the answer is $60+750+3=813$.

**Answer:** 813.

**Methods:** cylinder development, taut paths, similarity.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries were reviewed. The development argument is correct. Entry 1 interchanges sine and cosine after describing its inclination relative to the horizontal, although its final length factor is the correct one.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Developing the cylinder and tangent plane makes the taut rope straight with a constant slope, so horizontal projection ratios determine lengths.

## 2004 AIME II Problem 1: A chord halfway along a radius

A chord is perpendicular to a radius at its midpoint. The ratio of the larger circular region to the smaller is $(a\pi+b\sqrt c)/(d\pi-e\sqrt f)$ with positive integers, square-free c,f, and $\gcd(a,e)=1$. Find $abcdef\bmod1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

Scale the radius to 1. Half the chord, the half-radius, and a full radius form a $30$-$60$-$90$ triangle. Thus the chord subtends $120^\circ$, and its two-radius triangle has area $\sqrt3/4$. The smaller segment area is $\pi/3-\sqrt3/4$, and the larger is $2\pi/3+\sqrt3/4$. Their ratio is $(8\pi+3\sqrt3)/(4\pi-3\sqrt3)$. The parameter product is $8\cdot3\cdot3\cdot4\cdot3\cdot3=2592$, with remainder $592$.

**Answer:** 592.

**Methods:** circular segments, sector area.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source was reviewed; its sector-minus-triangle calculation and normalization are correct.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The distance from the center identifies a 120-degree sector, and subtracting its triangle gives the circular segment.

## 2004 AIME II Problem 3: Hidden cubes

A rectangular block made of unit cubes has exactly $231$ cubes invisible when three mutually adjacent faces are viewed. Find the least possible total number of cubes.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

For side lengths $a+1,b+1,c+1$, the unseen block has dimensions $a,b,c$, so $abc=231$. Assume $a\le b\le c$. Then $a\le\sqrt[3]{231}<7$, hence $a=1$ or $3$. If $a=1$, the possibilities $(b,c)=(1,231),(3,77),(7,33),(11,21)$ have minimum total $2\cdot12\cdot22=528$. If $a=3$, the only ordered possibility with $b\ge3$ is $(b,c)=(7,11)$, giving $4\cdot8\cdot12=384$.

**Answer:** 384.

**Methods:** finite case analysis, geometry hybrid.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** The first archived source asserts that balancing factors minimizes the product without proving the discrete case. Explicit factor enumeration here justifies the minimum.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry, number_theory. Invisible cubes form an interior rectangular block, whose factor triples are optimized for the total cube count.

## 2004 AIME II Problem 7: A fold as a perpendicular bisector

Rectangle ABCD is folded so B maps to $B\prime$ on AD. The crease meets AB at E and CD at F, with $AE=8,EB=17,CF=3$. If its perimeter is reduced m/n, find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

Place $A=(0,0),B=(25,0),D=(0,h),C=(25,h)$. Then $E=(8,0)$ and $F=(22,h)$. Since E is on the crease, $EB\prime=EB=17$, so $B\prime=(0,15)$. Likewise $FB\prime=FB$ gives $22^2+(h-15)^2=3^2+h^2$. Thus $30h=700$, or $h=70/3$. The perimeter is $2(25+70/3)=290/3$, giving $293$.

**Answer:** 293.

**Methods:** paper folding, perpendicular bisectors, coordinates.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All seven entries were reviewed. The two distance and slope methods are sound. Entry 2 confuses several segment names and signs while using a reflected orientation; entries 4 and 6 also mislabel triangle vertices and DB where a projected segment is intended. Entry 5 gives a longer valid area comparison with some undefined labels. Equal distances at the two crease points suffice.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Points on the crease have equal distances to the original and reflected corner, reducing the unknown height to a linear equation.

## 2004 AIME II Problem 11: A shortest path on a cone

A right circular cone has radius 600 and height $200\sqrt7$. Two points on opposite generators are at distances 125 and $375\sqrt2$ from the vertex. Find the shortest distance along the cone surface between them.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

The slant height is $\sqrt{600^2+(200\sqrt7)^2}=800$. Development of the lateral surface has sector angle $2\pi\cdot600/800=3\pi/2$. Opposite generators therefore differ by $3\pi/4$ in either minimal winding direction. Place the points at $(125,0)$ and $(-375,375)$ in that development. The connecting segment stays inside the sector and has length $\sqrt{500^2+375^2}=625$. Other windings require at least a half-turn in a continuous development; a path hitting the opposite ray has length at least the sum $125+375\sqrt2>625$ by triangle inequalities. A route using the base must first travel at least $(800-125)+(800-375\sqrt2)>625$. Thus the minimum is $625$.

**Answer:** 625.

**Methods:** cone development, geodesics, cosine law.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source was reviewed. Its sector angle is correct, but it writes a negative y-coordinate for a point described as lying in quadrant II; the distance is unchanged. The proof here also excludes longer winding and base routes.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Developing the cone converts opposite generators to a 135-degree angle and the shortest surface route to a straight chord.

## 2004 AIME II Problem 12: A circle between four vertex circles

Isosceles trapezoid ABCD has $AB=6,CD=4,AD=BC=5$. Circles centered at A,B have radius 3, and those at C,D have radius 2. A circle contained in the trapezoid is tangent to all four. Write its radius as $(-k+m\sqrt n)/p$ with square-free n and $\gcd(k,p)=1$, and find $k+m+n+p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Use $A=(0,0),B=(6,0),D=(1,h),C=(5,h)$, where $h=\sqrt{24}$. Internal tangency to a corner circle would put the desired circle inside that disk; tangency also to the neighboring disk, which touches it on a trapezoid side, would force the desired center onto that boundary side, impossible for a positive-radius contained circle. Thus all four tangencies are external; equal distances to A,B place its center at $(3,y)$. For radius r, the tangencies give $y^2=r^2+6r$ and $(h-y)^2=r^2+4r$. Subtraction yields $y=(12+r)/h$. Substituting back gives $23r^2+120r-144=0$, whose unique positive root is $(-60+48\sqrt3)/23$. It satisfies the original unsquared tangency equations and lies in the interior gap. Hence the answer is $60+48+3+23=134$.

**Answer:** 134.

**Methods:** tangent circles, symmetry axes, quadratic elimination.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source was reviewed. Its radical-sum equation is correct; subtracting squared distances avoids repeated squaring and displays the unique positive root directly.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Equal-radius tangencies force the symmetry axis, and subtracting two squared distance equations makes the center height linear in the radius.

## 2004 AIME II Problem 13: A pentagon built from three parallel directions

Convex pentagon ABCDE satisfies $AB\parallel CE$, $BC\parallel AD$, $AC\parallel DE$, $\angle ABC=120^\circ$, $AB=3$, $BC=5$, and $DE=15$. If $[ABC]/[EBD]=m/n$ in lowest terms, find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2004_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

The cosine law gives $AC^2=3^2+5^2-2\cdot3\cdot5\cos120^\circ=49$, so $AC=7$. Let $F=AD\cap CE$. Then ABCF is a parallelogram, and triangle FDE is similar to FCA with scale $15/7$. Convexity places DE beyond F on the side opposite AC: the other orientation would place D across line AB from C. If h is the distance from B to AC, the parallelogram puts F at distance h on the other side of AC, and DE a further $(15/7)h$ away. Thus the distance from B to DE is $(2+15/7)h=29h/7$. The area ratio is $(7/15)(7/29)=49/435$, yielding $484$.

**Answer:** 484.

**Methods:** parallel lines, parallelograms, similar triangles.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The source entry and its trigonometry-free AC calculation were both reviewed. Its three-height decomposition is correct; the explicit convexity placement explains why those heights add rather than subtract.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A parallelogram and a similar triangle turn the area ratio into a product of base and height ratios.

## 2005 AIME I Problem 1: A ring of six tangent circles

Six congruent circles form a closed ring, each externally tangent to its two neighbors and internally tangent to a circle of radius 30. If K is the area inside the large circle but outside all six small circles, find $\lfloor K\rfloor$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

Let each small radius be r. Their centers lie on the radius-$30-r$ circle with equal consecutive chords $2r$, so they form a regular hexagon. Its circumradius equals its side, giving $30-r=2r$ and $r=10$. Therefore $K=900\pi-6\cdot100\pi=300\pi$, whose floor is $942$.

**Answer:** 942.

**Methods:** circle rings, regular hexagons.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source was reviewed; its equilateral-triangle relation gives the correct radius and area.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The six equal circle centers form a regular hexagon whose circumradius equals its side length.

## 2005 AIME I Problem 7: Two sixty-degree base angles

Quadrilateral ABCD has $BC=8$, $CD=12$, $AD=10$, and $\angle A=\angle B=60^\circ$. If $AB=p+\sqrt q$ with positive integers p,q, find p+q.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

Put $A=(0,0)$ and $B=(x,0)$, choosing the quadrilateral above AB. The angle conditions give $D=(5,5\sqrt3)$ and $C=(x-4,4\sqrt3)$. Thus $CD^2=(x-9)^2+3=144$, so $x=9\pm\sqrt{141}$. Only the plus sign is positive. Therefore $AB=9+\sqrt{141}$ and the answer is $150$.

**Answer:** 150.

**Methods:** coordinate projections, special angles.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All four entries were reviewed. The projection and equilateral-extension methods reach the same quadratic. Several auxiliary labels in entries 0 and 1 are inconsistent; the coordinate statement fixes the incidences explicitly.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Projections of the two known sides leave a right triangle with known vertical difference.

## 2005 AIME I Problem 9: Local exposure types in a random cube

Each of $27$ unit cubes has four painted faces, with its two unpainted faces adjacent. Orient them independently uniformly in a $3\times3\times3$ cube. If the probability that the outer surface is painted is $p^a/(q^b r^c)$ in prime form, find $a+b+c+p+q+r$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

The interior cube is unrestricted. Each of six face-center cubes succeeds with probability $4/6=2/3$. Each of twelve edge cubes exposes a pair of adjacent faces: five of the twelve possible pairs are both painted, giving $5/12$. Each of eight corner cubes exposes three incident faces; two of eight such triples are fully painted, giving $1/4$. Independence gives $(2/3)^6(5/12)^{12}(1/4)^8=5^{12}/(2^{34}3^{18})$. The requested sum is $74$.

**Answer:** 074.

**Methods:** local types, product probability, geometric incidence.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Cube positions are classified by exposed faces and independent orientation probabilities are multiplied.

## 2005 AIME I Problem 10: Move along a median to prescribe area

Triangle ABC has area 70, with $B=(12,19)$ and $C=(23,20)$. Its median from $A=(p,q)$ to BC has slope $-5$. Find the largest p+q.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

The midpoint of BC is $M=(35/2,39/2)$, so write $A=M+t(1,-5)$. Since $C-B=(11,1)$, the determinant of $C-B$ and $A-B$ is $-56t$. Thus the area condition gives $28|t|=70$, or $t=\pm5/2$. The coordinate sum is $p+q=37-4t$, maximized at $t=-5/2$, giving $47$.

**Answer:** 047.

**Methods:** median coordinates, determinants, linear parameterization.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All four entries were reviewed. Entry 0 omits the absolute-value branch and assumes the desired ordering; entry 1 initially omits a square root in the point-line denominator before correcting it; entries 2 and 3 give valid two-branch calculations. The parameter proof treats both signs at once.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A line parameter through the midpoint makes oriented area linear in one scalar.

## 2005 AIME I Problem 11: Largest semicircle in a square

A semicircular region lies inside a square of side 8. Its largest possible diameter is $m-\sqrt n$ for positive integers m,n. Find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Let its radius be r. By square symmetries, take the diameter direction as $(\cos\theta,\sin\theta)$ with $0\le\theta\le\pi/2$, and the curved half on the side with normal $(-\sin\theta,\cos\theta)$. Its horizontal width is $r(1+\cos\theta)$ and vertical width is $r(1+\sin\theta)$: in each coordinate one extreme lies on the arc and the other at a diameter endpoint. Fitting inside the square requires $r(1+\max(\cos\theta,\sin\theta))\le8$. Since the maximum is at least $1/\sqrt2$, $r\le8/(1+1/\sqrt2)=16-8\sqrt2$. Equality is attained at $\theta=\pi/4$ by translating the bounding square onto the given square. The diameter is $32-16\sqrt2=32-\sqrt{512}$, so the answer is $544$.

**Answer:** 544.

**Methods:** convex widths, orientation optimization, semicircles.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All six entries were reviewed, including the incomplete introductory entry 0. They calculate the diagonal placement correctly but justify its global optimality only heuristically or by assertion. The two-width bound proves the maximum over all translations and orientations.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Horizontal and vertical widths give a global orientation bound, attained by a diagonal diameter.

## 2005 AIME I Problem 14: Constructing a square by perpendicular normal coordinates

A unique square has the points $A=(0,12)$, $B=(10,9)$, $C=(8,0)$, $D=(-4,7)$ on four different sides. If its area is K, find the remainder of 10K modulo 1000.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Consider the four lines $-x+3y=36$, $-x+3y=-8$, $3x+y=39$, and $3x+y=-5$. Their normals $(-1,3)$ and $(3,1)$ are perpendicular and have equal length $\sqrt{10}$; each strip has width $44/\sqrt{10}$, so their intersection is a square. A,B,C,D lie on the respective four lines, and their values in the other normal coordinate lie within the corresponding strip, so they are on the actual sides. By the supplied uniqueness, this is the required square. Hence $K=44^2/10$ and $10K\equiv936\pmod{1000}$.

**Answer:** 936.

**Methods:** normal coordinates, supporting lines, square reconstruction.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries were reviewed. Their rotated-vector and normal-vector methods agree. The second calls the prescribed side points opposite vertices, a wording error; the explicit strip construction verifies the required side incidences.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Two perpendicular linear forms provide equal-width strips whose boundary lines pass through the four prescribed points.

## 2005 AIME I Problem 15: An incircle trisecting a median

Triangle ABC has $BC=20$. Its incircle meets median AD at the two trisection points. If its area is $m\sqrt n$ with square-free n, find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Let $b=CA,c=AB$, and write $AD=L$. The two secant powers are equal: $\operatorname{Pow}(A)=\operatorname{Pow}(D)=2L^2/9$. If the incircle touches BC at T and the semiperimeter is s, the tangent lengths give $\operatorname{Pow}(A)=(s-20)^2$ and $\operatorname{Pow}(D)=DT^2=(b-c)^2/4$. Thus $b+c-20=|b-c|$, so the smaller of b,c is 10. Take $b=10,c>10$. The median formula gives $L^2=(c^2-100)/2$. Equating the power at A yields $9(c-10)^2=4(c^2-100)$, or $(c-10)(c-26)=0$. Nondegeneracy forces $c=26$. Heron gives area $\sqrt{28\cdot8\cdot18\cdot2}=24\sqrt{14}$, so the answer is $38$.

**Answer:** 038.

**Methods:** power of a point, incircle tangents, median formula.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed. Their tangent-length and median calculations are valid. Expressing the two equal powers symmetrically avoids assuming the side ordering before deriving which side must equal 10.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Equal secant powers at the median endpoints force one side to be half the base, after which the median formula determines the other side.

## 2005 AIME II Problem 8: A common tangent chord in an enclosing circle

Circles of radii 4 and 10 are externally tangent and internally tangent to a third circle, with all centers collinear. A common external tangent of the smaller circles cuts a chord from the third. Write its length as $m\sqrt n/p$ in lowest radical form and find m+n+p.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

The small centers are 14 apart. The enclosing center must lie between them, so $(R-4)+(R-10)=14$, giving $R=14$. Its position is 10 from the radius-4 center along the 14-unit center segment. Distances from those endpoints to the common external tangent are 4 and 10, on the same side; linear interpolation gives the enclosing center distance $4+(10/14)(10-4)=58/7$. Thus the chord length is $2\sqrt{14^2-(58/7)^2}=8\sqrt{390}/7$. The answer is $405$.

**Answer:** 405.

**Methods:** common tangents, affine distances, chord length.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries were reviewed, including the alternate similar-triangle calculation in entry 0. Their offset and chord values agree. The proof here also explains the enclosing radius from collinearity.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Signed distance to a line interpolates linearly along the collinear centers, giving the chord offset without finding the tangent equation.

## 2005 AIME II Problem 10: An octahedron and its face-center cube

For a regular octahedron O, let C be the cube whose vertices are its face centers. Write $\operatorname{Vol}(O)/\operatorname{Vol}(C)=m/n$ in lowest terms and find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

Scale the octahedron vertices to $(\pm3,0,0),(0,\pm3,0),(0,0,\pm3)$. The eight face centroids are $(\pm1,\pm1,\pm1)$, forming a cube of volume 8. The octahedron consists of eight coordinate tetrahedra, each with volume $3\cdot3\cdot3/6=9/2$, so its volume is 36. The requested ratio is $36/8=9/2$, giving $11$.

**Answer:** 011.

**Methods:** dual polyhedra, centroid coordinates, volume decomposition.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were inspected, including diagram-only entry 0. Both textual solutions calculate the reciprocal ratio 2/9 instead of the requested 9/2; this happens not to change the numerator-plus-denominator answer. The proof states the requested orientation explicitly.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Axis coordinates make the face centroids a cube and split the octahedron into eight orthogonal tetrahedra.

## 2005 AIME II Problem 12: A forty-five-degree view of a segment

In square ABCD of side 900 and center O, points E,F lie on AB in that order, with $AE<BF$, $EF=400$, and $\angle EOF=45^\circ$. If $BF=p+q\sqrt r$ with square-free r, find p+q+r.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Put $O=(0,0),A=(-450,450),B=(450,450)$, and write $E=(x,450),F=(x+400,450)$. The cross-product magnitude of OE and OF is 180000, while their dot product is $x(x+400)+202500$. For an angle of $45^\circ$, these are equal, so $x^2+400x+22500=0$. Thus $x=-200\pm50\sqrt7$. Now $AE=x+450$ and $BF=50-x$; the inequality $AE<BF$ requires $x<-200$, selecting the minus sign. Hence $BF=250+50\sqrt7$, and the answer is $307$.

**Answer:** 307.

**Methods:** dot products, cross products, angle constraints.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All ten entries were reviewed. The tangent, rotation, complex, and similarity methods agree. Entry 1 misprints 160000 as 16000; entry 3 has incompatible area and squared-length values; entry 5 swaps endpoint labels; entry 6 mixes a length with its square; entry 8 is only an unfinished recipe; entry 9 mislabels a straight angle and includes a radical typo. The direct vector equation avoids these auxiliary assumptions.

**Archived entries inspected:** 10 of 10. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The cross-product-to-dot-product ratio gives the angle condition without assuming where the side midpoint lies.

## 2005 AIME II Problem 14: Isogonal cevians multiply side ratios

Triangle ABC has $AB=13$, $BC=15$, $CA=14$. Point D lies on BC with $CD=6$. Point E lies on BC and satisfies $\angle BAE=\angle CAD$. If $BE=p/q$ in lowest terms, find q.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

For a point X on BC, comparing areas gives $BX/XC=AB\sin\angle BAX/(AC\sin\angle XAC)$. The given equality makes AD and AE isogonal, so the two sine ratios are reciprocal. Multiplying yields $(BD/DC)(BE/EC)=(AB/AC)^2$. Since $BD/DC=9/6$, we get $BE/EC=169/294$. With $BE+EC=15$, this gives $BE=2535/463$, already reduced, so $q=463$.

**Answer:** 463.

**Methods:** isogonal cevians, area ratios, sine rule.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All nine entries were reviewed. Entries 0, 2, 4, 6, and 8 support the same length. Entry 1 misprints 52 as 53 in a denominator; entry 3 uses an incorrect sum BE+KE and later loses a division sign; entry 5 swaps perpendicular-foot labels; entry 7 drops a square in a sine identity, gives an incorrect quadratic, and confuses BE with ED. The isogonal ratio identity avoids all length reconstruction.

**Archived entries inspected:** 9 of 9. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The sine factors cancel when the area-ratio formulas for two isogonal cevians are multiplied.

## 2005 AIME II Problem 15: Tangent-circle centers form an ellipse

Circles $w_1,w_2$ have equations $x^2+y^2+10x-24y-87=0$ and $x^2+y^2-10x-24y+153=0$. Let m be the least positive slope of a line through the origin containing the center of a circle internally tangent to $w_1$ and externally tangent to $w_2$. If $m^2=p/q$ in lowest terms, find p+q.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2005_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

The given centers are $F_1=(-5,12),F_2=(5,12)$ with radii 16 and 4. Since the smaller given disk lies strictly inside the larger, the sought circle must itself lie inside the larger; otherwise it could not be externally tangent to the smaller. For center X and radius r, $XF_1=16-r$ and $XF_2=4+r$, so the locus is the ellipse $x^2/100+(y-12)^2/75=1$. Conversely, its focal distances range from 5 to 15, so $r=XF_2-4\in[1,11]$ makes every point a valid center. Substituting $y=ax$ gives $(3+4a^2)x^2-96ax+276=0$. Its discriminant is $48(100a^2-69)$, so a positive-slope line meets the ellipse exactly when $a^2\ge69/100$. Equality is attainable and gives the least slope. Thus $m^2=69/100$, and the answer is $169$.

**Answer:** 169.

**Methods:** ellipse loci, circle tangency, tangent discriminant.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All six entries were reviewed. The discriminant, reflection, calculus, and affine-circle methods agree. The locus equivalence here explicitly checks positive radii and rules out the reversed internal-tangency interpretation; entry 3 has a malformed fraction in its derivative line.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The tangency distances have constant sum, and the least positive slope through the resulting ellipse is determined by a zero discriminant.

## 2006 AIME I Problem 1: Two successive right triangles

Quadrilateral $ABCD$ has $AB=18$, $BC=21$, $CD=14$, $AB\perp BC$, and $AC\perp CD$. Find its perimeter.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

The two right triangles give $AC^2=18^2+21^2$ and $AD^2=AC^2+14^2=961$. Therefore $AD=31$, and the perimeter is $18+21+14+31=84$.

**Answer:** 084.

**Methods:** Pythagorean theorem.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source uses the same two right triangles; all numerical steps are sound.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Two Pythagorean steps determine a quadrilateral side.

## 2006 AIME I Problem 7: Alternating strips in an angle

An angle has its vertex between parallel lines $L_0,L_1$ in an equally spaced family. Both rays cross $L_1,L_2,\ldots$. Let $A$ be its triangular part before $L_1$ and let $B,C,D$ be its portions between $L_2,L_3$, between $L_4,L_5$, and between $L_6,L_7$, respectively. If $[C]/[B]=11/5$, find $[D]/[A]$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

Normalize the line spacing to one and let the vertex be distance $t$ before $L_1$, with $0<t<1$. Similarity makes the area up to a line at distance $u$ from the vertex equal to $cu^2$. Hence $[A]=ct^2$, $[B]=c((t+2)^2-(t+1)^2)=c(2t+3)$, $[C]=c(2t+7)$, and $[D]=c(2t+11)$. The given ratio yields $5(2t+7)=11(2t+3)$, so $t=1/6$. The desired ratio is $(2t+11)/t^2=408$.

**Answer:** 408.

**Methods:** similarity, area differences.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries read. The first two give equivalent similarity arguments. The third has a reversed ratio, mixed-variable typographical errors, and an inconsistent final multiplication.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Similar-triangle area differences form a linear progression.

## 2006 AIME I Problem 8: Possible areas of the central rhombus

Four congruent rhombi surround a fifth rhombus. All five have a common side length $s$; each outer rhombus has acute angle $\theta$, and the central rhombus has an angle $2\theta$, where $0<\theta<90^\circ$. Each outer area is $\sqrt{2006}$. How many positive integer areas can the central rhombus have?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

The outer area condition is $s^2\sin\theta=\sqrt{2006}$. Thus the central area is $K=s^2\sin(2\theta)=2\sqrt{2006}\cos\theta$. As $\theta$ runs over $(0,90^\circ)$ and $s$ is chosen from the area condition, every value in $(0,2\sqrt{2006})$ occurs. Since $89^2<8024<90^2$, exactly the integers $1,\ldots,89$ occur.

**Answer:** 089.

**Methods:** rhombus area, continuous range.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries reviewed. Their trigonometric and diagonal parametrizations agree; endpoint degeneracy requires strict inequalities, and attainability follows from the continuous free angle.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A five-rhombus configuration reduces the central area to a continuous cosine range.

## 2006 AIME I Problem 10: A line bisecting eight disks

Eight radius-$1/2$ disks have centers $(i+1/2,j+1/2)$ for $i,j\in\{0,1,2\}$, omitting $(5/2,5/2)$. A line of slope $3$ bisects their total area. Write it as $ax=by+c$ with positive coprime integers $a,b,c$, and find $a^2+b^2+c^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

The line through $(1,1/2)$ and $(3/2,2)$ is $6x-2y=5$. The disks centered at $(1/2,1/2),(3/2,1/2)$ form a centrally symmetric pair about the first point; the disks at $(3/2,3/2),(3/2,5/2)$ form such a pair about the second. The line bisects each pair. The remaining four disks lie wholly on one side or the other, two on each side, as their center distances from the line exceed $1/2$. Hence the whole area is bisected. Parallel translation changes the area monotonically, and strictly near this line since it cuts disk interiors, so no other parallel line bisects. The requested value is $36+4+25=65$.

**Answer:** 065.

**Methods:** central symmetry, area bisection.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All four entries reviewed, including the diagram-only first entry. Pairwise half-turn symmetry supplies a rigorous certificate. Replacing disks by squares is not generally valid; the relevant source eventually checks the candidate geometrically.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Central symmetry of two disk pairs certifies an area-bisecting line.

## 2006 AIME I Problem 14: Height of a shortened tripod

Three rigid tripod legs of length $5$ meet pairwise at equal angles, placing their common top $4$ above the ground. One leg is shortened to length $4$, without changing the angles between legs. The new height is $m/\sqrt n$ in lowest squarefree-radical form. Find $\lfloor m+\sqrt n\rfloor$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Before shortening, choose the top $T=(0,0,4)$ and feet $A=(3,0,0)$, $B=(-3/2,3\sqrt3/2,0)$, $C=(-3/2,-3\sqrt3/2,0)$. Equal pairwise leg angles justify this equilateral base. The shortened foot is $S=T+\frac45(A-T)=(12/5,0,4/5)$. The plane through $B,C,S$ is $8x-39z+12=0$. Its distance from $T$ is $144/\sqrt{8^2+39^2}=144/\sqrt{1585}$. Since $1585=5\cdot317$ is squarefree and $39^2<1585<40^2$, the answer is $144+39=183$.

**Answer:** 183.

**Methods:** solid geometry, point-plane distance.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries reviewed. Volume ratios, plane coordinates, and a symmetry cross-section give equivalent derivations. The first diagram places the top at height 5 despite the stated height 4; the numerical proofs use 4 correctly.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The new support plane is determined in coordinates while the leg angles remain fixed.

## 2006 AIME II Problem 1: An equilateral hexagon with two right angles

A convex hexagon has six equal sides. Two opposite angles are $90^\circ$, and the other four angles are equal. Its area is $2116(1+\sqrt2)$. Find its side length.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

The four equal angles are $(720^\circ-180^\circ)/4=135^\circ$. Join the neighbors of each right-angle vertex. This cuts off two isosceles right triangles with legs $s$ and leaves a rectangle with sides $s$ and $s\sqrt2$. Thus the total area is $s^2(1+\sqrt2)$, so $s^2=2116$ and $s=46$.

**Answer:** 046.

**Methods:** angle sums, area dissection.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries reviewed. The second explicitly justifies the 135-degree angles required for the rectangle dissection.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Angle sums expose two right triangles and a rectangle.

## 2006 AIME II Problem 2: Logarithms as triangle sides

For how many positive integers $n$ do $\log_{10}12$, $\log_{10}75$, and $\log_{10}n$ form the sides of a nondegenerate triangle?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

The triangle criterion for a third side $c$ is $|a-b|<c<a+b$. Here it becomes $\log_{10}(75/12)<\log_{10}n<\log_{10}(12\cdot75)$, or $25/4<n<900$. Thus $n=7,8,\ldots,899$, giving $899-7+1=893$.

**Answer:** 893.

**Methods:** triangle inequality, logarithms.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source has the correct strict bounds. These automatically guarantee positivity of the third side and the remaining triangle inequality.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Strict triangle inequalities become bounds on an integer logarithm argument.

## 2006 AIME II Problem 6: An axis-parallel square in a right triangle

In unit square $ABCD$, points $E\in BC$ and $F\in CD$ make $AEF$ equilateral. A smaller square lies inside $ABCD$, has vertex $B$, parallel sides, and its opposite vertex on $AE$. Its side is $(a-\sqrt b)/c$ in reduced form with squarefree $b$. Find $a+b+c$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

Set $B=(0,0)$, $A=(0,1)$, $C=(1,0)$, $D=(1,1)$ and $E=(t,0)$. From $AE=AF$, the point $F$ is $(1,1-t)$. Then $AE^2=1+t^2$ and $EF^2=2(1-t)^2$, giving $t=2-\sqrt3$ after rejecting the root above one. The line $AE$ is $x/t+y=1$. Its intersection with the diagonal $x=y=s$ gives $s=t/(1+t)=(3-\sqrt3)/6$. Therefore $a+b+c=3+3+6=12$.

**Answer:** 012.

**Methods:** equilateral triangle, line intercepts, inscribed square.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All five entries read. The Pythagorean and similarity methods agree. One trigonometric entry labels original unit sides by the new square side, a notation error avoided here.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. An equilateral condition sets an intercept, then a line intercept equation determines the smaller square.

## 2006 AIME II Problem 9: Intersecting internal common tangents

Circles with centers $(0,0),(12,0),(24,0)$ have radii $1,2,4$. The first two have a common internal tangent of positive slope; the last two have one of negative slope. Their intersection has $x$-coordinate $p-q\sqrt r$ in reduced squarefree form. Find $p+q+r$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

An internal tangent crosses the centers' line in the ratio of the radii. Thus the first tangent crosses at $x=4$ and the second at $x=16$. If their inclinations have absolute values $\alpha,\beta$, then $\sin\alpha=(1+2)/12=1/4$ and $\sin\beta=(2+4)/12=1/2$. Their equations are $y=(x-4)/\sqrt{15}$ and $y=-(x-16)/\sqrt3$. Solving gives $x=(16\sqrt5+4)/(\sqrt5+1)=19-3\sqrt5$. The answer is $19+3+5=27$.

**Answer:** 027.

**Methods:** circle tangency, homothety centers.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source reaches the same tangent equations through several auxiliary right triangles; the inclination formula shortens the computation.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Signed center distances determine the two tangent equations.

## 2006 AIME II Problem 12: A cyclic triangle and a parallelogram diagonal

An equilateral triangle $ABC$ has circumradius $2$. Points $D$ beyond $B$ on ray $AB$ and $E$ beyond $C$ on ray $AC$ satisfy $AD=13$, $AE=11$. Complete parallelogram $ADFE$. Let $G\ne A$ be the second intersection of $AF$ with the circumcircle. Express $[BCG]=p\sqrt q/r$ in reduced squarefree form and find $p+q+r$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

The diagonal $AF$ lies strictly inside angle $BAC$, so $G$ is on the arc $BC$ avoiding $A$. Thus $\angle BGC=120^\circ=\angle AEF$, while $\angle GBC=\angle GAC=\angle FAE$. Hence triangles $GBC$ and $EAF$ are similar, with $BC$ corresponding to $AF$. We have $BC^2=12$, $AF^2=13^2+11^2+13\cdot11=433$, and $[EAF]=143\sqrt3/4$. Consequently $[BCG]=(12/433)(143\sqrt3/4)=429\sqrt3/433$, yielding $865$.

**Answer:** 865.

**Methods:** cyclic quadrilateral, similarity, law of cosines.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All four entries reviewed. Similarity and coordinate methods are sound. The longer Ptolemy entry confuses DF with EF and gives an incorrect angle in its chord formula; its final lengths agree with the sound methods.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Inscribed-angle similarity converts a small cyclic area to a known parallelogram triangle.

## 2006 AIME II Problem 15: A radical system encoding triangle altitudes

Real numbers satisfy $x=\sqrt{y^2-1/16}+\sqrt{z^2-1/16}$, $y=\sqrt{z^2-1/25}+\sqrt{x^2-1/25}$, and $z=\sqrt{x^2-1/36}+\sqrt{y^2-1/36}$. If $x+y+z=m/\sqrt n$ with squarefree $n$ and positive integers $m,n$, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2006_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

The equations imply $x,y,z>0$ and the strict triangle inequalities. In the first equation, the two nonnegative radicals are the projections of sides $y,z$ onto a base of length $x$, giving a triangle of height $1/4$. The other equations construct congruent triangles with heights $1/5$ and $1/6$ over the other sides. If their common area is $K$, then $x=8K$, $y=10K$, $z=12K$. Heron's formula now yields $K^2=(15K)(7K)(5K)(3K)=1575K^4$, so $K=1/(15\sqrt7)$ and $x+y+z=2/\sqrt7$. These sides form an acute $4:5:6$ triangle, so all projection signs agree with the original radicals. The answer is $9$.

**Answer:** 009.

**Methods:** triangle altitudes, Heron formula, radical systems.

**Verification:** Numerically substituted the proposed solution into all three original radical equations, including radical signs.

**Source comparison:** Both entries read. The geometric source proves triangle existence but does not fully justify its initial acute-angle assumption; the projection construction here supplies that missing link. The algebraic elimination offers an independent symmetric-polynomial derivation.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Each radical equation constructs an altitude of the same triangle.

## 2007 AIME I Problem 9: Two equal exterior tangent circles

Right triangle $ABC$ has $CA=30$, $CB=16$. Outside the triangle, two equal-radius circles touch the hypotenuse and, respectively, the extensions of $CA$ beyond $A$ and $CB$ beyond $B$. They also touch each other externally. If the common radius is $p/q$ in lowest terms, find $p+q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

The hypotenuse is $34$, the area is $240$, and the semiperimeter is $40$. The excenter $I$ opposite $C$ is distance $240/(40-34)=40$ from $AB$. Each small center lies on the corresponding external angle bisector $AI$ or $BI$, and their equal distances $r$ from $AB$ make their connecting line parallel to $AB$. Similarity gives the center separation $34|1-r/40|$. External tangency requires $34|1-r/40|=2r$. The branch $r\ge40$ has no positive solution; the other gives $r=680/57$. Thus $p+q=737$.

**Answer:** 737.

**Methods:** excenter, homothety, tangent circles.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All nine entries reviewed, including the brief diagram-dependent homothety reference. Half-angle, coordinate, and excenter methods agree. The third entry swaps triangle-angle labels; the coordinate alternative remains a useful numerical check. The absolute-value branch is made explicit here.

**Archived entries inspected:** 9 of 9. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. An excenter similarity turns the tangency condition into a linear radius equation.

## 2007 AIME I Problem 12: Overlap of two rotated isosceles triangles

Let $A=(0,0)$, $B=(20,0)$, and let $C$ lie in the first quadrant with $AC=BC$ and $\angle BAC=75^\circ$. Rotate the triangle counterclockwise until $C$ reaches the positive vertical axis. If the common area is $p\sqrt2+q\sqrt3+r\sqrt6+s$, find $(p-q+r-s)/2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

The rotation is $15^\circ$; denote the new vertices by $B_1,C_1$. Put $D=AC\cap B_1C_1$, $E=BC\cap B_1C_1$, and $F=BC\cap AB_1$. The overlap is $ADEF$, obtained from triangle $ADB_1$ by removing $EFB_1$. The first triangle has angles $60^\circ,75^\circ,45^\circ$ and side $AB_1=20$, so its area is $20^2\sin60^\circ\sin75^\circ/(2\sin45^\circ)=150+50\sqrt3$. Since $AF\perp BC$, $AF=20\cos15^\circ=5(\sqrt6+\sqrt2)$. Therefore $[EFB_1]=\frac12(20-5\sqrt6-5\sqrt2)^2\tan75^\circ=750+400\sqrt3-500\sqrt2-300\sqrt6$. Subtraction gives the common area $500\sqrt2-350\sqrt3+300\sqrt6-600$, and the requested value is $875$.

**Answer:** 875.

**Methods:** rotation, polygon intersection, trigonometric area.

**Verification:** Independently clipped the original and rotated triangles numerically and compared their polygon area with the radical expression.

**Source comparison:** All five entries reviewed, including the diagram-only entry. The first dissection and coordinate equations support the result. The second has a malformed intermediate denominator; the third duplicates and then loses an area term in its final simplification.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The overlap is a larger triangle with one right triangular corner removed.

## 2007 AIME I Problem 13: A pentagonal section of a square pyramid

A square pyramid $ABCDE$ has all eight edges of length $4$, with base $ABCD$. A plane passes through the midpoints of $AE$, $BC$, and $CD$. Its section has area $\sqrt p$. Find $p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Use $A=(-2,2,0)$, $B=(2,2,0)$, $C=(2,-2,0)$, $D=(-2,-2,0)$, and $E=(0,0,2\sqrt2)$. The section plane is $x-y+2\sqrt2z=2$. Its vertices, in order, are $P=(-1,1,\sqrt2)$, $X=(3/2,3/2,\sqrt2/2)$, $Q=(2,0,0)$, $R=(0,-2,0)$, and $Y=(-3/2,-3/2,\sqrt2/2)$; direct edge substitution verifies this list. Their horizontal projection has shoelace area $8$. Because the plane is the graph $z=(2-x+y)/(2\sqrt2)$, its area factor over horizontal projection is $\sqrt{1+1/8+1/8}=\sqrt5/2$. The section area is therefore $4\sqrt5=\sqrt{80}$, giving $p=80$.

**Answer:** 080.

**Methods:** plane sections, coordinate geometry, area projection.

**Verification:** Computed the section area by a 3D polygon cross product, independently of horizontal projection.

**Source comparison:** All three entries reviewed. Their geometric decompositions agree. The first has reversed coefficient equalities while deriving the correct plane; the second calls the section vertex E instead of P. Projection supplies a shorter area calculation.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A section plane and projected polygon determine the spatial area.

## 2007 AIME I Problem 15: An inscribed sixty-degree triangle

In equilateral triangle $ABC$, points $F\in AB$, $D\in BC$, and $E\in CA$ satisfy $AF=5$, $CD=2$, $\angle DEF=60^\circ$, and $[DEF]=14\sqrt3$. The two possible side lengths are $p\pm q\sqrt r$ with rational $p,q$ and squarefree integer $r$. Find $r$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Write $AB=x$ and $AE=y$. Subtracting the three corner triangles from $ABC$ gives $x^2=5y+(x-5)(x-2)+2(x-y)+56$, hence $3y=5x-66$. Angle chasing using $\angle DEF=60^\circ$ gives $\triangle AEF\sim\triangle CDE$, so $5/(x-y)=y/2$, or $y(x-y)=10$. Eliminating $y$ produces $10x^2-462x+4446=0$, whence $x=(231\pm3\sqrt{989})/10$. Both roots have $x>5$ and $0<y<x$; conversely the product relation gives the corner-triangle similarity by SAS and thus the required angle, so both configurations exist. Since $989=23\cdot43$, the answer is $989$.

**Answer:** 989.

**Methods:** area decomposition, similarity, quadratic discriminant.

**Verification:** Constructed both candidate triangles in coordinates and independently checked the 60-degree angle, prescribed area, and segment placements.

**Source comparison:** Both entries reviewed. The first provides the efficient area-and-similarity reduction. The second chooses a radical sign without accounting for both configurations; the present argument verifies both roots geometrically.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Area decomposition and angle-induced similarity yield a quadratic for the outer side.

## 2007 AIME II Problem 3: Two exterior right triangles on a square

Square $ABCD$ has side $13$. Exterior points $E,F$ satisfy $AE=CF=12$ and $BE=DF=5$. Find $EF^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

The $5$-$12$-$13$ triangles are right at $E,F$ and are exchanged by the half-turn about the square center $O$. Thus $EF=2OE$. Also $\angle AEB=\angle AOB=90^\circ$, so $AEBO$ is cyclic. Ptolemy gives $13\,OE=AE\cdot BO+BE\cdot AO=(12+5)(13/\sqrt2)$. Hence $EF=17\sqrt2$, and $EF^2=578$.

**Answer:** 578.

**Methods:** Ptolemy theorem, central symmetry.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All seven entries read, including the one-line coordinate suggestion. The square-completion, coordinates, and Ptolemy methods agree. One Ptolemy display mistakenly uses AO in place of OE; the trigonometric entry has an arcsine denominator typo.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A central symmetry and Ptolemy identity determine the distance.

## 2007 AIME II Problem 5: Grid cells below a rational line

Count unit grid squares whose interiors lie in the first quadrant and below $9x+223y=2007$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

The intercept rectangle has $223\cdot9=2007$ cells. Its diagonal crosses $223+9-\gcd(223,9)=231$ cells: one initial cell and one new cell for each interior grid-line crossing. Since the intercepts are coprime, no interior horizontal and vertical crossings coincide. Half of the remaining cells lie on each side by central symmetry. Thus the answer is $(2007-231)/2=888$.

**Answer:** 888.

**Methods:** lattice geometry, symmetry.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry, number_theory. A lattice-square count is a sum of floor-function row lengths below a line.

## 2007 AIME II Problem 9: Two incircle contact points on one side

Rectangle $ABCD$ has $AB=63$ and $BC=448$. Points $E\in AD$ and $F\in BC$ satisfy $AE=CF=84$. The incircles of $BEF$ and $DEF$ touch $EF$ at $P,Q$, respectively. Find $PQ$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

We have $BE=DF=\sqrt{63^2+84^2}=105$, $BF=DE=364$, and $EF=\sqrt{63^2+280^2}=287$. The triangles are congruent with semiperimeter $s=(105+364+287)/2=378$. The equal-tangent rule gives $EP=s-BF=14$ and $FQ=s-DE=14$. Therefore $PQ=287-14-14=259$.

**Answer:** 259.

**Methods:** incircle tangency lengths, Pythagorean triples.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All five entries reviewed. Tangent-length subtraction is complete and avoids inradius calculations. The incenter-distance entry is only an unfinished sketch; the scaling alternatives give the correct difference.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Equal tangent lengths turn a contact-point distance into a difference of triangle sides.

## 2007 AIME II Problem 11: Rolling over a smaller cylinder

A radius-$72$ cylinder rolls along a plane, over a fixed parallel radius-$24$ cylinder, and back onto the plane without slipping. After exactly one complete rotation, its horizontal displacement is $a\pi+b\sqrt c$, with integer coefficients and squarefree $c$. Find $a+b+c$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

At first and last contact with the small cylinder, the center separation is $96$ and the vertical difference is $48$. Thus each horizontal offset is $48\sqrt3$, and the large center traverses an angle $2\pi/3$ around the small center. On this arc its speed is $96\dot\theta$. No slipping makes its spin speed $96\dot\theta/72$, so this portion consumes rolling length $96(2\pi/3)=64\pi$ from the total one-revolution length $144\pi$. The remaining flat travel is $80\pi$, while the obstacle crossing contributes horizontal distance $96\sqrt3$. Hence the answer is $80+96+3=179$.

**Answer:** 179.

**Methods:** rolling without slipping, circular motion.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The source correctly combines the two large-circle angular contributions with the small-circle arc. The instantaneous velocity relation here makes the no-slip accounting explicit.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. No-slip rotation relates center-arc travel to the consumed revolution.

## 2007 AIME II Problem 15: Four equal circles in a triangle

Inside a triangle of side lengths $13,14,15$, three equal circles are tangent to the respective pairs of sides at the three vertices. A fourth circle of the same radius is externally tangent to all three. If the radius is $m/n$ in lowest terms, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2007_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Heron gives area $84$, so the triangle has inradius $\rho=84/21=4$ and circumradius $R=13\cdot14\cdot15/(4\cdot84)=65/8$. For common small radius $r$, the three corner-circle centers lie on the angle bisectors and form the inward parallel triangle at distance $r$ from each side. This is a homothetic copy with ratio $(\rho-r)/\rho$. The fourth center is its circumcenter, and its circumradius is $2r$. Thus $2r=R(\rho-r)/\rho$, giving $r=\rho R/(2\rho+R)=260/129$. Consequently $m+n=389$.

**Answer:** 389.

**Methods:** homothety, inradius and circumradius, equal tangent circles.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All five entries reviewed, including the generalized formula. Their similarity or homothety arguments agree. The simplified general expression r=rho R/(2rho+R) is valid for an existing configuration; arbitrary triangles also require checking that the fourth disk lies inside.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. An inward parallel triangle of centers is homothetic to the original triangle.

## 2008 AIME I Problem 2: A triangle overlapping a square

An isosceles triangle has as its base one side of a side-$10$ square. Their overlap has area $80$. Find the altitude of the triangle to that base.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

The apex must lie on the square side of the base, at height $h>10$, since height at most ten gives area at most fifty. At height ten the triangle has width $10(1-10/h)$ by similarity. Its overlap with the square is a trapezoid, so $80=\frac{10}{2}(10+10-100/h)=100-500/h$. Thus $h=25$.

**Answer:** 025.

**Methods:** similarity, trapezoid area.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source correctly identifies the apex as beyond the opposite square side, then uses the same similar triangles.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A trapezoid area and similarity determine the triangle height.

## 2008 AIME I Problem 5: A cone rolling around its vertex

A right circular cone of base radius $r$ and height $h$ rolls on a plane without slipping, keeping its vertex fixed. During its first full circuit around the vertex it makes $17$ rotations. Write $h/r=m\sqrt n$ with squarefree $n$, and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

Let $\ell=\sqrt{r^2+h^2}$ be the slant height. The base contact point traces a circle of radius $\ell$. No slipping equates the distance in one circuit, $2\pi\ell$, with $17$ base circumferences, $17(2\pi r)$. Thus $\ell=17r$, giving $h^2/r^2=17^2-1=288$. Therefore $h/r=12\sqrt2$ and $m+n=14$.

**Answer:** 014.

**Methods:** rolling cones, surface development.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source compares the traced circumference with seventeen base circumferences. The restatement makes its intended first-circuit meaning explicit.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Unrolling the lateral surface compares slant-circle travel with base circumference.

## 2008 AIME I Problem 10: A trapezoid forced by equality bounds

An isosceles trapezoid $ABCD$ has longer base $AD\parallel BC$, base angles $60^\circ$, and diagonals $10\sqrt{21}$. A point $E$ satisfies $EA=10\sqrt7$, $ED=30\sqrt7$. If $F$ is the perpendicular projection of $C$ onto $AD$, write $EF=m\sqrt n$ in squarefree form and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

Write $AD=x$, $CD=y$. The two distances from $E$ imply $x\ge ED-EA=20\sqrt7$. The cosine rule in $ADC$ gives $2100=x^2+y^2-xy=(y-x/2)^2+3x^2/4$, so $x\le20\sqrt7$. Equality holds in both bounds: $y=x/2=10\sqrt7$, and $E,A,D$ are collinear in that order. Since $DF=y\cos60^\circ=5\sqrt7$, we get $AF=15\sqrt7$ and $EF=25\sqrt7$. The answer is $32$.

**Answer:** 032.

**Methods:** equality cases, law of cosines, reverse triangle inequality.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** Both entries reviewed. The first gives the essential tight bounds. The second assumes the incorrect length AD=40 sqrt(7) and unsupported right-triangle angles, so it does not establish the result.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A reverse triangle inequality meets a quadratic discriminant bound.

## 2008 AIME I Problem 14: Maximizing a tangent projection distance

Circle $\omega$ has diameter $AB=18$. A point $C$ lies beyond $A$ on ray $BA$, and $CT$ is tangent to the circle. Let $P$ be the perpendicular projection of $A$ onto $CT$. If $m$ is the largest possible $BP$, find $m^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Let $O$ be the center and let $\theta$ be the acute angle between $CA$ and the tangent. Write $u=\sin\theta=9/OC$, so $0<u<1$. If $Q$ is the perpendicular projection of $B$ onto the tangent, then $BQ=9(1+u)$ and $PQ=18\cos\theta$. Therefore $BP^2=81(1+u)^2+324(1-u^2)=81(5+2u-3u^2)=432-243(u-1/3)^2$. Equality occurs at $u=1/3$, corresponding to $OC=27$, so $m^2=432$.

**Answer:** 432.

**Methods:** tangent projections, quadratic optimization.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All six entries reviewed; the external forum link in entry four was not opened. The trigonometric quadratic and reciprocal-distance methods are sound. Entry four has a squared-variable typo in AP; the final entry overstates the admissible altitude range, though its optimizer is feasible.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A tangent-line coordinate system makes the squared distance a concave quadratic.

## 2008 AIME I Problem 15: The height of a folded paper tray

At each corner of a side-$100$ square, mark points distance $\sqrt{17}$ along the adjacent edges. Cut from both marks to a common interior point on the corner diagonal, with angle $60^\circ$ between the cuts, removing the corner wedge. Fold along the lines joining neighboring cut-intersection points and join each pair of cut edges to form a tray. Its height is $\sqrt[n]m$ in reduced form, $m<1000$. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

At one corner use coordinates $(0,0)$ with marks $(s,0),(0,s)$, where $s=\sqrt{17}$. The cut triangle is equilateral with side $s\sqrt2=\sqrt{34}$. Its interior apex is $(t,t)$, where $t=(s+\sqrt3s)/2$. The folded bottom is the square through these four apexes. Relative to a bottom corner, the corresponding upper corner has equal outward horizontal offsets $d=t-s=(\sqrt{51}-\sqrt{17})/2$: these are fixed by the lengths along the rigid side panels. Its connecting edge has length $\sqrt{34}$. Consequently the height satisfies $h^2=34-2d^2=17\sqrt3$, so $h=\sqrt[4]{867}$. Since $867=3\cdot17^2$ contains no fourth power, the answer is $871$.

**Answer:** 871.

**Methods:** paper folding, solid geometry, Pythagorean theorem.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries reviewed, including the diagram-only entry. The first computes the unfolded offsets; the second uses direction cosines. Both give the same rigid-edge height relation.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Rigid face lengths and two horizontal offsets determine the folded height.

## 2008 AIME II Problem 3: Ten slices from a rectangular block

A $10\times13\times14$ rectangular solid loses ten slices, each one unit thick and parallel to a face of the remaining block. What is the largest possible remaining volume?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

Every slice reduces one dimension by one. Thus the remaining positive dimensions $a,b,c$ satisfy $a+b+c=10+13+14-10=27$. AM-GM yields $abc\le9^3=729$. Cutting one unit from the first dimension, four from the second, and five from the third produces a $9\times9\times9$ cube, so the bound is attained.

**Answer:** 729.

**Methods:** AM-GM, geometric optimization.

**Verification:** Exhaustively enumerated every nonnegative allocation of the ten unit slices with a positive remaining first dimension.

**Source comparison:** Both entries reviewed. The AM-GM proof is complete; the greedy alternative lists a successful path but leaves its global optimality assertion unstated.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. A fixed sum of remaining dimensions makes AM-GM sharp.

## 2008 AIME II Problem 5: Midpoints of bases with complementary base angles

Trapezoid $ABCD$ has $BC\parallel AD$, $BC=1000$, $AD=2008$, and base angles $\angle A=37^\circ$, $\angle D=53^\circ$. If $M,N$ are the midpoints of $BC,AD$, find $MN$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

Extend the legs to their intersection $E$. Since the base angles sum to $90^\circ$, triangles $EAD$ and $EBC$ are right at $E$. Their hypotenuse medians have lengths $EN=AD/2=1004$ and $EM=BC/2=500$. The homothety centered at $E$ between the triangles sends one midpoint to the other, so $E,M,N$ are collinear. Therefore $MN=1004-500=504$.

**Answer:** 504.

**Methods:** right triangle median, homothety.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All eight entries reviewed. The median and coordinate methods are complete. The third contains reciprocal and squared-trigonometric errors; the sixth substitutes 45-degree angles without proving invariance. The final rotation entry has several labeling and arithmetic typos.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Extending the legs creates similar right triangles with known median lengths.

## 2008 AIME II Problem 9: An affine rotation with period eight

Start at $(5,0)$. A move rotates the point counterclockwise by $45^\circ$ about the origin and then translates it ten units right. After $150$ moves the point is $(p,q)$. Find $\lfloor|p|+|q|\rfloor$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

Identify the plane with complex numbers and let $\zeta=e^{i\pi/4}$. A move is $z\mapsto\zeta z+10$. Since $\zeta^8=1$ and $\sum_{j=0}^{7}\zeta^j=0$, eight moves are the identity. Thus $150$ moves equal six, giving $z=5\zeta^6+10\sum_{j=0}^{5}\zeta^j=5(-i)-10(\zeta^6+\zeta^7)=-5\sqrt2+(5+5\sqrt2)i$. Therefore $|p|+|q|=5+10\sqrt2$. The inequalities $1.4<\sqrt2<1.5$ give $19<5+10\sqrt2<20$, so the answer is $19$.

**Answer:** 019.

**Methods:** affine rotations, roots of unity.

**Verification:** Numerically applied all 150 original rotation-and-translation moves.

**Source comparison:** All four entries reviewed; the external Desmos link was not opened. The periodicity is correct. The second has a summation-index error, the fixed-center entry calls a positive-angle rotation clockwise, and the matrix entry asserts false pairwise cancellations even though the full eight-term sum is zero.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The sum of eighth roots of unity annihilates the translation over one period.

## 2008 AIME II Problem 10: Increasing distances on a small grid

On the sixteen points $\{0,1,2,3\}^2$, a path visits distinct points with strictly increasing successive distances. Let $m$ be its maximum number of points and $r$ the number of paths attaining that maximum. Find $mr$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

The only squared distances are $1,2,4,5,8,9,10,13,18$, so $m\le10$. Reverse a maximal path. Up to eight square symmetries its first three points are $(0,0),(3,3),(1,0)$. The required remaining squared lengths force $(2,3),(2,0),(0,2),(2,1),(0,1),(1,2)$; alternatives at each stage either repeat a vertex or prevent the next required length. The final unit step has three choices: $(1,1),(2,2),(1,3)$. Thus ten-point paths exist and $r=8\cdot3=24$, giving $240$.

**Answer:** 240.

**Methods:** extremal paths, symmetry, finite enumeration.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Increasing-distance paths on a finite lattice require an extremal length bound and enumeration.

## 2008 AIME II Problem 11: Two tangent circles along an isosceles base

Triangle $ABC$ has $AB=AC=100$, $BC=56$. A radius-$16$ circle touches $AC$ and $BC$. Another circle lies entirely inside the triangle, touches $AB$ and $BC$, and is externally tangent to the first circle. Its radius is $m-n\sqrt k$ with squarefree $k$. Find $m+nk$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Choose $B=(-28,0)$, $C=(28,0)$, $A=(0,96)$. Half the base angle has tangent $3/4$, so the first center is $(20/3,16)$ and the second is $(-28+4r/3,r)$. External tangency gives $((104-4r)/3)^2+(16-r)^2=(16+r)^2$, or $(26-r)^2=36r$. Thus $r=44\pm6\sqrt{35}$. Every contained circle has radius at most the inradius $2688/128=21$, excluding the plus sign. The smaller root is positive and below 21, and its corner circle consequently lies inside all three side half-planes. The answer is $44+6\cdot35=254$.

**Answer:** 254.

**Methods:** tangent circles, half-angle ratios.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All four entries reviewed. The first and incenter-based third are sound. The second is garbled and dimensionally inconsistent; the fourth contains incorrect numerators in both its similarity ratio and final base-length equation.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Angle-bisector offsets and the external tangency distance produce a quadratic radius equation.

## 2008 AIME II Problem 13: Inverting the exterior of a regular hexagon

A regular hexagon centered at $0$ in the complex plane has opposite sides one unit apart, including a pair parallel to the imaginary axis. Let $S=\{1/z:z\text{ is outside the hexagon}\}$. If its area is $a\pi+\sqrt b$, find $a+b$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

In the angular sector $-\pi/6\le\theta\le\pi/6$, the original boundary is $r\cos\theta=1/2$. Reciprocal inversion reflects the angle and sends the exterior radial interval to $0<\rho\le2\cos\theta$. Thus its boundary arc belongs to the unit circle centered at $(1,0)$. Rotating by multiples of $60^\circ$ gives the six boundary arcs. Their endpoints form a regular hexagon of circumradius $\sqrt3$, with area $9\sqrt3/2$. Each outward circular segment has central angle $120^\circ$, hence area $\pi/3-\sqrt3/4$. Adding six segments gives $2\pi+3\sqrt3=2\pi+\sqrt{27}$. Therefore $a+b=29$.

**Answer:** 029.

**Methods:** complex inversion, circular segments.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries reviewed. The inversion sketch, circular-segment construction, and polar integral agree. The geometric entry misstates the centers as angles k*pi/6; the six centers are spaced by pi/3. Boundary and omitted-origin conventions do not affect area.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Reciprocal inversion turns the six supporting lines into six unit-circle arcs.

## 2008 AIME II Problem 14: An equilateral constraint inside a rectangle

For $a\ge b>0$, suppose $a^2+y^2=b^2+x^2=(a-x)^2+(b-y)^2$ has a solution with $0\le x<a$, $0\le y<b$. Let $\rho$ be the largest possible $a/b$. If $\rho^2=m/n$ in lowest terms, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2008_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

Let the common value be $L$. Expanding the last square gives $L=2L-2(ax+by)$, so $L=2ax+2by$. Since $2by\ge y^2$, the equality $a^2+y^2=2ax+2by$ implies $x\le a/2$. Also $b^2+x^2=a^2+y^2\ge a^2$, hence $b^2\ge a^2-x^2\ge3a^2/4$. Thus $\rho^2\le4/3$. Equality is attained by $(a,b,x,y)=(1,\sqrt3/2,1/2,0)$, which satisfies every constraint. The answer is $4+3=7$.

**Answer:** 007.

**Methods:** inequalities, equilateral triangle, equality cases.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All six entries reviewed. The direct inequality proof is complete. The geometric alternatives need care at allowed zero endpoints; one mislabels x as sqrt(1-a^2), and the final entry reverses an angle bound. The present proof checks the boundary equality explicitly.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. Nonnegativity bounds an equal-distance system by a sharp quadratic inequality.

## 2009 AIME I Problem 4: A diagonal meeting a short intercept segment

In parallelogram $ABCD$, points $M\in AB$ and $N\in AD$ satisfy $AM/AB=17/1000$ and $AN/AD=17/2009$. If $P=AC\cap MN$, find $AC/AP$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

Use the independent vectors $AB,AD$ as an affine coordinate basis, so $A=(0,0)$, $C=(1,1)$, $M=(17/1000,0)$, and $N=(0,17/2009)$. The line $MN$ is $1000x+2009y=17$. On $AC$, write $x=y=t$, giving $t=17/3009=1/177$. Therefore $AC/AP=177$.

**Answer:** 177.

**Methods:** affine coordinates, intercept form.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All six entries reviewed. The vector and mass-point methods are rigorous. The first collapses the diagram to a line without justification; the last assumes a rectangle without first invoking affine invariance and also gives N an incorrect sign. Affine coordinates avoid both issues.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Affine coordinates turn the intersection ratio into a sum of reciprocals.

## 2009 AIME I Problem 5: A midpoint reflection and an angle bisector

In triangle $ABC$, $AC=450$, $BC=300$. Let $K$ be the midpoint of $AC$, and let the angle bisector $CL$ meet $AB$ at $L$. Put $P=BK\cap CL$ and reflect $P$ across $K$ to obtain $M$. If $AM=180$, find $LP$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

The diagonals $AC$ and $MP$ bisect each other, so $AMCP$ is a parallelogram and $AM\parallel CP$. Thus $\triangle BLP\sim\triangle BAM$. By the angle-bisector theorem, $AL/LB=450/300=3/2$, so $BL/BA=2/5$. Consequently $LP=(2/5)AM=72$.

**Answer:** 072.

**Methods:** midpoint reflection, angle bisector, similarity.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All four entries reviewed. The parallelogram-similarity proof is shortest. Mass points gives the same ratio; the lengthy cosine and area calculations are unnecessary and contain minor final-label errors.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A parallelogram converts the requested segment into an angle-bisector ratio.

## 2009 AIME I Problem 11: Integral triangle areas on a line

Choose distinct nonnegative lattice points $P,Q$ on $41x+y=2009$. Count triangles $OPQ$ of positive integer area, where $O=(0,0)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Write the two x-coordinates as $u,v\in\{0,\ldots,49\}$. Their determinant is $2009(u-v)$, so the area is integral exactly when $u,v$ have the same parity. Each parity class contains $25$ values. Every distinct pair yields positive area, hence the count is $2\binom{25}{2}=600$.

**Answer:** 600.

**Methods:** parity, geometry hybrid.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 2: The inference that the base is an integral multiple of twice the primitive lattice length requires the lattice-spacing condition; integrality of area alone is insufficient.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry, number_theory. Lattice-point pairs are filtered by the parity condition for integral triangle area.

## 2009 AIME I Problem 12: A universal perimeter ratio from an altitude circle

Right triangle $ABC$ has $AC=12$, $BC=35$, and altitude $CD$ to hypotenuse $AB$. The circle with diameter $CD$ has nonbase tangents from $A$ and $B$ meeting at $I$ outside $ABC$. Write the perimeter of $ABI$ divided by $AB$ as reduced $m/n$, and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

Put $AD=u$, $DB=v$ and let $t$ be either tangent length from $I$ to the circle. The circle is the incircle of $ABI$, whose side lengths are $u+v,u+t,v+t$ and semiperimeter $s=u+v+t$. The altitude theorem gives $CD^2=uv$, so the circle radius satisfies $r^2=uv/4$. Heron and area $rs$ yield $suvt=r^2s^2=uvs^2/4$. Canceling positive factors gives $4t=s$, or $t=(u+v)/3$. Therefore the perimeter divided by $AB=u+v$ is $2s/(u+v)=8/3$, giving $m+n=11$.

**Answer:** 011.

**Methods:** Heron formula, incircle tangency, altitude theorem.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All seven entries reviewed. The tangent-length/Heron proof reveals a ratio independent of the given legs. The second contains area notation errors and a rational guess; the ruler-and-compass numerical estimate is explicitly not a proof. Trigonometric alternatives agree after their label errors are corrected.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Heron and the inradius area formula cancel all triangle dimensions.

## 2009 AIME I Problem 15: A fixed-angle arc from two incenter circles

Triangle $ABC$ has $AB=10$, $BC=14$, $CA=16$. For $D$ inside $BC$, let $I_B,I_C$ be the incenters of $ABD,ACD$. The circles through $B,I_B,D$ and through $C,I_C,D$ meet again at $P$. The maximum area $[BPC]$ is $a-b\sqrt c$ in reduced squarefree form. Find $a+b+c$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

The cosine rule gives $\angle A=60^\circ$. Put $\alpha=\angle BAD$ and $\beta=\angle DAC$. The incenter angles are $\angle BI_BD=90^\circ+\alpha/2$ and $\angle CI_CD=90^\circ+\beta/2$. Cyclic supplementary angles at the second intersection therefore give $\angle BPC=(90^\circ-\alpha/2)+(90^\circ-\beta/2)=150^\circ$. The second intersection is below $BC$: in coordinates $B=(0,0)$, $C=(14,0)$, $D=(d,0)$, the circle equations have positive linear-y coefficients $d\tan(\alpha/2)$ and $(14-d)\tan(\beta/2)$, and their nonbase intersection has negative y-coordinate. Thus P lies on the fixed lower arc subtending $150^\circ$. As D moves continuously from B to C, P varies continuously from B to C: the corresponding endpoint circle shrinks to that endpoint, and the two tangents at D are distinct throughout the interior. Hence P attains the perpendicular bisector of BC. On the fixed arc that is the unique farthest point from BC, with height $7\tan15^\circ=7(2-\sqrt3)$. The maximal area is $7\cdot7(2-\sqrt3)=98-49\sqrt3$, giving $150$.

**Answer:** 150.

**Methods:** incenter angles, cyclic quadrilaterals, locus optimization.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries reviewed. They obtain the correct fixed angle and upper bound but leave attainability of the middle of the arc implicit. The continuous-intersection argument and endpoint limits here supply that missing condition.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Cyclic angle sums fix a locus, while continuity ensures the extremal point is attained.

## 2009 AIME II Problem 3: Perpendicular lines in a rectangle

Rectangle $ABCD$ has $AB=100$. If $E$ is the midpoint of $AD$ and $AC\perp BE$, find the greatest integer less than $AD$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

Choose $A=(0,0)$, $B=(100,0)$, $D=(0,h)$, so $C=(100,h)$ and $E=(0,h/2)$. The perpendicular vectors $AC=(100,h)$ and $BE=(-100,h/2)$ give $-10000+h^2/2=0$. Thus $h=100\sqrt2$. Since $141^2<20000<142^2$, the answer is $141$.

**Answer:** 141.

**Methods:** dot product, rectangle geometry.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All four entries reviewed. Similarity, slopes, and vectors give the same equation. The auxiliary-parallelogram entry misses a square in one Pythagorean display.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A zero dot product fixes the rectangle aspect ratio.

## 2009 AIME II Problem 5: A circle tangent to three interior circles

An equilateral triangle is inscribed in a radius-$10$ circle. Three internally tangent circles touch the outer circle at the triangle vertices and have radii $3,2,2$. A fourth circle is externally tangent to all three. Its radius is reduced $m/n$. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

Place the outer center at the origin and the three inner centers at $(0,7)$ and $(\pm4\sqrt3,-4)$. A fourth center equidistant from the last two lies at $(0,y)$. If its radius is $r>0$, then $|y-7|=r+3$ and $48+(y+4)^2=(r+2)^2$. The branch $y=10+r$ yields $r=-10$, impossible. Thus $y=4-r$, and substitution gives $48+(8-r)^2=(r+2)^2$, so $20r=108$. Hence $r=27/5$ and $m+n=32$.

**Answer:** 032.

**Methods:** tangent circles, symmetry, distance equations.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source uses the same symmetry with a cosine rule, assuming the center lies below the origin. The two-branch calculation here proves that the selected location is the unique positive-radius option.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Symmetry and distance equations make the unknown radius linear after cancellation.

## 2009 AIME II Problem 10: Two equal-angle observations

Points $A,B,C,D$ satisfy $AB=5$, $BC=12$, $AC=13$, $\angle BAD=\angle CAD$, and $\angle ACB=\angle DCB$. Write $AD=p\sqrt q/r$ in reduced squarefree form and find $p+q+r$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

Place $B=(0,0)$, $A=(5,0)$, $C=(0,12)$. The second angle equality makes ray $CD$ the reflection of $CA$ across $CB$, so its line is $y=12+12x/5$; the other choice would place the distinct point D at A. The line $AD$ is the internal angle-bisector line at A, whose direction is $(-1,0)+(-5,12)/13$, hence $y=(10-2x)/3$. Intersecting gives $D=(-65/23,120/23)$. Therefore $AD=\sqrt{180^2+120^2}/23=60\sqrt{13}/23$, and the answer is $96$.

**Answer:** 096.

**Methods:** angle bisectors, reflection, coordinates.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All six entries reviewed. The reflection, Stewart, cosine, and sine methods agree. Some source diagrams use vertical leg 13 rather than 12, but their numerical derivations use the correct 5-12-13 triangle.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Reflection and an angle bisector determine a point by two lines.

## 2009 AIME II Problem 13: A product of semicircle chords

A radius-$2$ semicircle with diameter endpoints $A,B$ is divided into seven equal arcs by $C_1,\ldots,C_6$. Let $N=\prod_{k=1}^{6}AC_k\,BC_k$. Find $N$ modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Each triangle $ABC_k$ is right, and its altitude to diameter $AB=4$ is $2\sin(k\pi/7)$. Comparing its two area formulas gives $AC_k\,BC_k=8\sin(k\pi/7)$. For $\zeta=e^{2\pi i/7}$, evaluation at one of $(x^7-1)/(x-1)=\prod_{k=1}^{6}(x-\zeta^k)$ yields $7=\prod_{k=1}^{6}|1-\zeta^k|=2^6\prod_{k=1}^{6}\sin(k\pi/7)$. Therefore $N=8^6\cdot7/2^6=7\cdot2^{12}=28672$, giving remainder $672$.

**Answer:** 672.

**Methods:** roots of unity, sine products, chord lengths.

**Verification:** Directly multiplied the twelve chord lengths using six paired altitude products.

**Source comparison:** All four entries reviewed. The roots-of-unity proofs are complete. One paired-root index should be 7-k rather than k-7; the final solution misses a factor four when adding the diameter chord, though its final numerical expression restores the correct power.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A roots-of-unity product evaluates a sine product exactly.

## 2009 AIME II Problem 15: Maximum separation of two chord intercepts

Circle diameter $MN$ has length one. On one semicircle, $A$ is the arc midpoint and $MB=3/5$. A variable point $C$ lies on the other semicircle. The chords $AC,BC$ meet $MN$ at $D,E$. If the largest $DE$ is $r-s\sqrt t$ in reduced squarefree form, find $r+s+t$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2009_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Put $MC=x$, $NC=y$, so $x,y>0$ and $x^2+y^2=1$. Since A is an arc midpoint, $CA$ bisects $\angle MCN$, yielding $MD=x/(x+y)$. Also $BN=4/5$, and the sine form of the cevian ratio gives $ME/EN=x\sin\angle MCB/(y\sin\angle BCN)=3x/(4y)$. Hence $ME=3x/(3x+4y)$, so $DE=xy/((x+y)(3x+4y))=1/(7+3x/y+4y/x)$. AM-GM gives $3x/y+4y/x\ge4\sqrt3$. Equality occurs at $x=2/\sqrt7$, $y=\sqrt3/\sqrt7$, which is realized by a point on the semicircle. Thus the maximum is $1/(7+4\sqrt3)=7-4\sqrt3$, and the answer is $14$.

**Answer:** 014.

**Methods:** generalized angle bisector, AM-GM, chord intersections.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All five entries reviewed. The elementary cevian-ratio argument supplies both the bound and explicit equality. The cross-ratio alternatives have notation errors, and one omits the attainment check; the calculus methods agree with the same optimum.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The generalized angle-bisector ratio reduces the chord separation to AM-GM.

## 2010 AIME I Problem 8: The smallest disk enclosing floor-defined squares

Let $R=\{(x,y):\lfloor x\rfloor^2+\lfloor y\rfloor^2=25\}$. The smallest closed disk containing $R$ has radius $\sqrt m/n$ in reduced squarefree form. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

The relevant integer pairs are $(\pm5,0),(0,\pm5),(\pm3,\pm4),(\pm4,\pm3)$, each indexing a half-open unit square. Any closed containing disk also contains their closures. Centering a disk at $(1/2,1/2)$, its squared distance to a vertex is at most $25+|u|+|v|+1/2$, maximized at $|u|+|v|=7$. Thus radius $\sqrt{130}/2$ covers every cell. Conversely closure vertices $(5,4)$ and $(-4,-3)$ are distance $\sqrt{130}$ apart, so every containing disk has radius at least half that. Hence $m+n=130+2=132$.

**Answer:** 132.

**Methods:** lattice points, minimum enclosing disk, central symmetry.

**Verification:** Enumerated all closure-cell vertices, their distances from the proposed center, and all pairwise distances.

**Source comparison:** The sole source gives the correct radius but calls the half-open cells symmetric and does not explicitly prove that another center cannot improve it. Passing to the closure and using a diametral pair supplies both details.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory. Lattice solutions identify square cells, and antipodal closure points certify the enclosing radius.

## 2010 AIME I Problem 11: Revolving a triangular inequality region

The region satisfying $|8-x|+y\le10$ and $3y-x\ge15$ is revolved around $3y-x=15$. Write its volume as $m\pi/(n\sqrt p)$ in reduced squarefree form and find $m+n+p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

The region is the triangle with apex $(8,10)$ and base endpoints $(9/2,13/2)$ and $(39/4,33/4)$ on the axis. The perpendicular apex distance is $r=7/\sqrt{10}$, and the base length is $L=7\sqrt{10}/4$. The foot lies between the endpoints, so rotation gives two cones whose heights sum to L. Their combined volume is $\pi r^2L/3=343\pi/(12\sqrt{10})$, giving $343+12+10=365$.

**Answer:** 365.

**Methods:** solids of revolution, point-line distance, cones.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** The sole source correctly identifies the triangular region and adds the two cone volumes.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The rotated triangle becomes two cones with a shared base.

## 2010 AIME I Problem 13: A rectangle and semicircle cut in a fixed area ratio

A rectangle $ABCD$ and a semicircle with diameter $AB$ lie on opposite sides of $AB$. A line meets the semicircle at $N$, $AB$ at $U$, and $CD$ at $T$, dividing their union in area ratio $1:2$. Given $AU=84$, $UB=168$, $AN=126$, write $AD=m\sqrt n$ in squarefree form and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Scale lengths by 42. Use $A=(0,0)$, $B=(6,0)$ and rectangle below the axis with height h. The circle radius is three, and $AN=3$ forces $N=(3/2,3\sqrt3/2)$, since the center $(3,0)$ forms an equilateral triangle with A,N. As $U=(2,0)$, the line meets the bottom at $T=(2+h/(3\sqrt3),-h)$; the condition $T\in CD$ gives $0<h\le12\sqrt3$. The left piece has area $L=2h+h^2/(6\sqrt3)+3\pi/2-3\sqrt3/4$, whereas total area is $S=6h+9\pi/2$. It cannot equal $2S/3$, since $L-2S/3=h^2/(6\sqrt3)-2h-3\pi/2-3\sqrt3/4<0$ on that height range. Hence $L=S/3$, giving $h^2/(6\sqrt3)=3\sqrt3/4$, or $h=3\sqrt6/2$. Restoring the scale yields $AD=63\sqrt6$ and answer $69$.

**Answer:** 069.

**Methods:** area cancellation, circular sectors, branch exclusion.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All six entries reviewed, including the diagram-only entry. The intended smaller-side calculation is correct, but the claim that the same side is always smaller is not valid over the full admissible height range. The explicit alternate-ratio exclusion here repairs that gap. Several entries also confuse NU with its horizontal projection or misprint sqrt(3) as sqrt(2).

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Circular-sector terms cancel against a target area fraction, with the alternate ratio branch excluded.

## 2010 AIME I Problem 15: Equal inradii determine a cevian length

Triangle $ABC$ has $AB=12$, $BC=13$, $AC=15$. A point $M$ inside $AC$ makes triangles $ABM$ and $BCM$ have equal inradii. Write $AM/CM=p/q$ in lowest terms and find $p+q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Let the common inradius be r, the original inradius R, total area K, semiperimeter $s=20$, and $BM=d$. Adding the two area formulas gives $K=r(s+d)$, while $K=Rs$. The tangent lengths from A and C to the smaller incircles sum to $s-d$; they also equal $r(\cot(A/2)+\cot(C/2))$. For the original incircle, $R(\cot(A/2)+\cot(C/2))=AC=15$. Thus $r/R=(20-d)/15=20/(20+d)$, yielding $d^2=100$ and $d=10$. Equal inradii also give $AM/CM=(12+d)/(13+d)=22/23$ after cross-multiplying the area ratio. This cevian exists: coordinates $A=(0,0)$, $C=(15,0)$ give $B=(20/3,\sqrt{896}/3)$, and $M=(22/3,0)$ has $BM=10$ and the required area-perimeter ratio. Hence the answer is $45$.

**Answer:** 045.

**Methods:** incircle tangency, equal inradii, cevian length.

**Verification:** Constructed the proposed point in Cartesian coordinates and independently compared the two area-over-semiperimeter inradii; optimality and uniqueness remain analytic.

**Source comparison:** All eight entries reviewed, including the diagram-only entry and the homothety addendum. The contact-length sum gives the shortest elimination. Quartic/Stewart approaches are valid after sign filtering; several source displays omit factors or misuse a ratio, and the answer-range shortcut via the rational-root theorem is unnecessary.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Adding contact lengths and area formulas eliminates the two smaller inradii.

## 2010 AIME II Problem 2: Distance to the nearest side

Choose a point uniformly inside a unit square. Its distance to the nearest side is $d$. Find numerator plus denominator of $P(1/5\le d\le1/3)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

The event $d\ge t$ is a concentric square of side $1-2t$. Thus the desired area is $(3/5)^2-(1/3)^2=56/225$, and the answer is $281$.

**Answer:** 281.

**Methods:** continuous probability, complement.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: The two inner-square areas are attached to the wrong distance thresholds. Their difference is nevertheless computed correctly.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Uniform area probability is found by subtracting inset squares.

## 2010 AIME II Problem 9: A regular hexagon bounded by rotated chords

In regular hexagon $ABCDEF$, let $G,H,I,J,K,L$ be the midpoints of $AB,BC,CD,DE,EF,FA$. The segments $AH,BI,CJ,DK,EL,FG$ bound a smaller regular hexagon. If its area divided by the original area is reduced $m/n$, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

Normalize the outer circumradius and side length to one. Take $A=(1,0)$, $B=(1/2,\sqrt3/2)$, $C=(-1/2,\sqrt3/2)$, so $H=(0,\sqrt3/2)$. The line $AH$ is $\sqrt3x+2y=\sqrt3$, at distance $\sqrt{3/7}$ from the center. The six rotated lines give the smaller hexagon this apothem, while the original apothem is $\sqrt3/2$. Similar regular polygons have area ratio equal to the squared apothem ratio, here $4/7$. Thus $m+n=11$.

**Answer:** 011.

**Methods:** regular polygons, apothem, similarity.

**Verification:** Independently clipped the outer hexagon by all six defining lines and computed the area ratio by shoelace.

**Source comparison:** All four entries reviewed, including the diagram/setup entry and brief similarity suggestion. The coordinate-intersection entry misprints the y-coordinate of B in its line equation; the correct computed intersection agrees with the direct apothem method. Its external image link was not separately opened.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Distances from the common center to a side line give the area ratio directly.

## 2010 AIME II Problem 12: Two isosceles triangles with equal area and perimeter

Two noncongruent integer-sided isosceles triangles have equal areas and perimeters, and their base lengths are in ratio $8:7$. Find their least possible common perimeter.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Write the bases as $8t,7t$ with positive integer t. Equal perimeters make their difference t twice the difference of equal-side lengths, so t is even; put $t=2u$. With common semiperimeter s, the side triples are $(s-8u,s-8u,16u)$ and $(s-7u,s-7u,14u)$, and s is integral. Heron gives equal squared areas $64u^2s(s-16u)=49u^2s(s-14u)$. Thus $15s=338u$. Since 15 and 338 are coprime, the least positive scale is $u=15$, $s=338$. The resulting triples $(218,218,240)$ and $(233,233,210)$ satisfy the triangle inequalities, so the minimum perimeter is $676$.

**Answer:** 676.

**Methods:** Heron formula, parity, primitive integer scaling.

**Verification:** Exhausted all integer-sided isosceles pairs with base ratio 8:7 and perimeter through 676, comparing exact squared areas.

**Source comparison:** Both entries reviewed, including the parity note. The main scaling calculation is correct, but integrality of the parameter in bases 16u and 14u requires the parity argument supplied here.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory, algebra. Parity and Heron reduce the primitive integral solution to a coprime scaling condition.

## 2010 AIME II Problem 14: A doubled angle in a right triangle

Right triangle $ABC$ has right angle C, $AB=4$, and $\angle A<45^\circ$. A point $P$ on $AB$ satisfies $CP=1$ and $\angle APC=2\angle ACP$. If $AP/BP=p+q\sqrt r$ in squarefree form, find $p+q+r$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

Let $\theta=\angle ACP$ and $\beta=\angle ABC$. In triangle BCP, the sine rule gives $BP=\cos\theta/\sin\beta$. In triangle ACP, using $AC=4\sin\beta$, it gives $AP=AC\sin\theta/\sin2\theta=2\sin\beta/\cos\theta$. Hence $AP\cdot BP=2$ and $AP+BP=4$, so the two lengths are $2\pm\sqrt2$. Also $\angle A=180^\circ-3\theta<45^\circ$ forces $\theta>45^\circ>\angle A$, so $AP>CP=1$. Therefore $AP=2+\sqrt2$, yielding $AP/BP=3+2\sqrt2$ and answer $7$.

**Answer:** 007.

**Methods:** sine rule, angle doubling, branch selection.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All six entries reviewed. The sine-rule and power-of-a-point methods give the correct product. Several entries assert AP greater than BP without using the angle condition; the explicit angle comparison here selects the correct root. The long angle-bisector derivation also contains a denominator typo.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Two sine-rule equations cancel the auxiliary angles and determine a chord product.

## 2010 AIME II Problem 15: A radical axis evaluated by endpoint powers

Triangle $ABC$ has $AC=13$, $BC=14$, $AB=15$. Let M,N be the midpoints of AC,AB, and let the angle bisectors from B,C meet AC,AB at D,E. The circles AMN and ADE meet again at P. Ray AP meets BC at Q. If $BQ/CQ=m/n$ in lowest terms, find $m-n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2010_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Let $F(X)=\operatorname{Pow}_{AMN}(X)-\operatorname{Pow}_{ADE}(X)$. The quadratic parts of the two power functions cancel, so F is affine and vanishes on their radical axis AP. At B, secants along BA give $F(B)=BA(BN-BE)=15(15/2-70/9)=-25/6$, because the angle-bisector theorem gives $BE=14\cdot15/27=70/9$. At C, similarly $F(C)=CA(CM-CD)=13(13/2-182/29)=169/58$. These have opposite signs, so the zero on BC lies inside the segment. Affine interpolation yields $BQ/CQ=-F(B)/F(C)=(25/6)/(169/58)=725/507$. Thus $m-n=218$.

**Answer:** 218.

**Methods:** radical axis, power of a point, affine interpolation.

**Verification:** Exact evaluation of the radical-axis affine ratio; the geometric power interpretation is established analytically.

**Source comparison:** All four entries reviewed, including the stated concurrency extension; its cited external reference was not opened. Power interpolation gives the shortest proof. The first general formula cancels an extra factor only because a-b=c-a=1 in this instance; the explicit numeric powers avoid overstating that cancellation.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The difference of circle powers is affine along the opposite side.

## 2011 AIME I Problem 2: Parallel segments across a rectangle

In rectangle $ABCD$, $AB=12$ and $BC=10$. Interior points $E,F$ satisfy $BE=9$, $DF=8$, $BE\parallel DF$, and $EF\parallel AB$; the line $BE$ meets side $AD$. Write $EF=m\sqrt n-p$ with squarefree $n$ and positive integers $m,n,p$, and find $m+n+p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

Use $D=(0,0)$, $B=(12,10)$ and write $F=8(u,v)$, $E=B-9(u,v)$, where $u^2+v^2=1$ and $u,v>0$. Equal heights give $17v=10$, hence $17u=\sqrt{17^2-10^2}=3\sqrt{21}$. Their horizontal separation is $17u-12$, so $EF=3\sqrt{21}-12$ and the answer is $3+21+12=36$.

**Answer:** 036.

**Methods:** parallel vectors, Pythagorean theorem.

**Verification:** Independent coordinate reconstruction verifies both segment lengths, equal heights, and the requested separation.

**Source comparison:** All three entries were reviewed. Their similar-triangle or extended-segment constructions encode the same length-17 right triangle. One longer algebraic derivation has a squared-expression transcription error; the vector computation avoids it.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Parallel vectors reduce a rectangular configuration to a right triangle.

## 2011 AIME I Problem 3: Coordinates in rotated perpendicular axes

Line $L$ has slope $5/12$ and contains $(24,-1)$. Its perpendicular $M$ contains $(5,6)$. Use $L,M$ as the new coordinate axes, with positive directions toward these respective points. If $(-14,27)$ has coordinates $(\alpha,\beta)$ in this system, find $\alpha+\beta$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

Unit vectors in the positive axis directions are $(12,5)/13$ and $(-5,12)/13$. Since the new first coordinate vanishes on $M$ and the second on $L$, the coordinate functions are $\alpha=(12x+5y-90)/13$ and $\beta=(-5x+12y+132)/13$. Their values at the specified direction points are positive, verifying orientation. At $(-14,27)$ they give $-123/13$ and $526/13$, whose sum is $31$.

**Answer:** 031.

**Methods:** orthogonal projection, signed coordinates.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed. Signed distances avoid computing the intersection of the axes. The long coordinate alternative has a mistyped right-hand-side coordinate; the final projection entry is only an outline.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Signed orthogonal projections determine the rotated coordinates.

## 2011 AIME I Problem 4: Feet on angle bisectors

Triangle $ABC$ has $AB=125$, $AC=117$, and $BC=120$. Let $M,N$ be the perpendicular projections of $C$ onto the internal angle bisectors at $B,A$, respectively. Find $MN$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

Reflect $C$ across the bisector at $B$ to $P$ on ray $BA$, and across the bisector at $A$ to $Q$ on ray $AB$. Then $BP=120$, $AQ=117$, and $M,N$ are the midpoints of $CP,CQ$. On segment $AB$, $AP=125-120=5$, so $PQ=117-5=112$. The midpoint theorem gives $MN=56$.

**Answer:** 056.

**Methods:** angle bisectors, reflection, midpoint theorem.

**Verification:** Computed both perpendicular projections from Cartesian side-length coordinates, independently of the reflection proof.

**Source comparison:** All four entries were reviewed. Reflection gives the shortest proof; the cyclic-quadrilateral, trigonometric, and Ptolemy approaches are longer. One trigonometric transcription has an inconsistent final arithmetic line, which the direct length calculation avoids.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Reflection across each angle bisector turns perpendicular feet into midpoints.

## 2011 AIME I Problem 8: Folding triangular legs of equal height

A triangular sheet has side lengths $23,27,30$. Cut off a corner triangle at each vertex by a fold line parallel to the opposite side, with the three corner interiors disjoint. Fold these corners downward through $90^\circ$ so their vertex tips lie on one plane below the central tabletop. What is the greatest height, written $m\sqrt n/p$ in reduced form with squarefree $n$? Find $m+n+p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

The area is $K=\sqrt{40\cdot17\cdot13\cdot10}=20\sqrt{221}$. If the common height is $h$, the corner similarity ratios are $23h/(2K)$, $27h/(2K)$, and $30h/(2K)$, because each corner altitude becomes a vertical leg. Along each original side the two adjacent ratios must sum to at most 1. The strongest of these three conditions is $57h/(2K)\le1$. At equality the other two inequalities are strict, so the configuration exists and the central tabletop has positive area. Thus $h=40\sqrt{221}/57$, giving $40+221+57=318$.

**Answer:** 318.

**Methods:** similarity, folding, linear constraints, Heron formula.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All three entries were reviewed. Each uses corner similarity and the first pair of legs to meet. The proof here explicitly checks all three edge constraints and attainment, allowing the two limiting fold lines to share a point.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Similar corner triangles translate a folding problem into pairwise linear constraints.

## 2011 AIME I Problem 10: Obtuse triangles in a regular polygon

Three vertices are chosen uniformly from a regular $n$-gon. Their triangle is obtuse with probability $93/125$. Find the sum of all possible $n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

An obtuse triangle has a unique circular gap greater than a semicircle. The vertex after that gap is a unique anchor, and its other two vertices must be among the next $h=\lfloor(n-1)/2\rfloor$ vertices. Thus $P=n\binom h2/\binom n3$. If $n=2t$, this simplifies to $3(t-2)/(2(2t-1))$, giving $t=188$ and $n=376$. If $n=2t-1$, it is $3(t-2)/(2(2t-3))$, giving $t=64$ and $n=127$. The sum is $503$.

**Answer:** 503.

**Methods:** cyclic gaps, geometric probability.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** Reviewed all available source arguments. The solution here gives an independently written proof, checked against the archived answer. Audit findings: Source 1: The obtuse-triangle formula has an off-by-one error and does not produce the two values subsequently claimed. Trial values also do not prove exhaustiveness.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry, number_theory. Count obtuse vertex triangles of a regular polygon and solve the resulting rational equation.

## 2011 AIME I Problem 13: The height of a tilted cube

A cube of edge length $10$ lies above a plane. Its nearest vertex is $A$, and the three vertices adjacent to $A$ are at distances $10,11,12$ from the plane. Express the distance of $A$ as $(r-\sqrt s)/t$ in reduced form and find $r+s+t$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Let $h$ be the height of $A$. The vertical components of its three mutually perpendicular length-10 edges are $10-h,11-h,12-h$. For an orthonormal basis the squared components of the unit vertical vector sum to 1, so $(10-h)^2+(11-h)^2+(12-h)^2=100$. Setting $z=11-h$ yields $3z^2+2=100$. Since $A$ is the nearest vertex, $h<10$ and $z>0$. Therefore $h=11-7\sqrt6/3=(33-\sqrt{294})/3$, giving $330$.

**Answer:** 330.

**Methods:** orthonormal basis, spatial projection, quadratic equation.

**Verification:** Numerically checked the vertical-component identity and nearest-vertex branch.

**Source comparison:** Both entries were reviewed. The normal-vector identity gives a direct proof; the centroid-and-tilt construction reaches the same quadratic with more geometry. The nearest-vertex hypothesis selects the correct root.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Orthogonal edge directions give a sum of squared vertical components.

## 2011 AIME I Problem 14: Projecting the midpoint square of an octagon

In a regular octagon $A_1\cdots A_8$, let $M_i$ be the midpoint of $A_iA_{i+1}$ for odd $i$. Inward rays from $M_1,M_3,M_5,M_7$ are perpendicular to their neighboring rays. Their successive intersections are $B_1,B_3,B_5,B_7$, with $B_1\in R_1\cap R_3$. If $B_1B_3$ equals an octagon side, write $\cos(2\angle A_3M_3B_1)=m-\sqrt n$ and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Scale the octagon side to 2. The odd-side midpoints form a square on a circle of radius $a=1+\sqrt2$, and $M_1M_5$ is parallel to side $A_3A_4$. Because $R_1$ and $R_5$ are perpendicular to $R_3$, the points $B_1,B_3$ are the perpendicular projections of $M_1,M_5$ onto its line. If $\theta=\angle A_3M_3B_1$, the projection length is $2a|\cos\theta|=2$. Consequently $\cos2\theta=2/a^2-1=2(\sqrt2-1)^2-1=5-\sqrt{32}$, so the answer is $37$.

**Answer:** 037.

**Methods:** regular octagon, orthogonal projection, double-angle identity.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All five entries were reviewed. The projection interpretation gives the shortest route and avoids relying on an unproved symmetry of the intersection square. One alternative mistakenly calls the octagon a hexagon; its intended projection calculation is recognizable.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Adjacent perpendicular rays make their intersection gap a projection of a diameter.

## 2011 AIME II Problem 2: Three equal segments spanning a square

In square $ABCD$, points $E$ and $F$ lie in the interiors of $AD$ and $BC$, respectively. If $BE=EF=FD=30$, find the area of the square.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

Set $A=(0,0)$, $B=(s,0)$, $C=(s,s)$, $D=(0,s)$, $E=(0,e)$, and $F=(s,f)$, with $0<e,f<s$. From $BE=FD$ we obtain $e=s-f$. Then $BE=EF$ gives $e^2=(s-2e)^2$, or $(s-e)(s-3e)=0$. The interior condition excludes $e=s$, so $e=s/3$. Finally $900=BE^2=s^2+(s/3)^2=10s^2/9$, and the area is $810$.

**Answer:** 810.

**Methods:** distance equations, square, degenerate cases.

**Verification:** Direct distance check of the nondegenerate trisection configuration.

**Source comparison:** The sole entry was reviewed. It asserts the trisection without deriving it. The coordinate proof derives it and makes explicit the intended distinct-point convention: allowing E=D and F=B would create a different degenerate answer.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Source correction:** The archived wording says points lie on sides without explicitly excluding endpoints. The intended distinct-vertex configuration has interior E,F and area 810; the coincident choice E=D,F=B would instead give area 450. The restatement states the intended nondegeneracy explicitly.

**Subject classification:** geometry, algebra. Equal distances force the two side points to trisect their respective sides.

## 2011 AIME II Problem 3: Integer angles in arithmetic progression

The interior angle measures of a convex $18$-gon, in increasing order, form a strictly increasing arithmetic progression of integers. Find its smallest angle in degrees.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

Write the angles as $a,a+d,\ldots,a+17d$, with positive integer $d$. Their sum is $16\cdot180$, so $2a+17d=320$. Thus $d$ is even. The largest angle equals $160+17d/2<180$, yielding $d<40/17$. The only positive even possibility is $d=2$, and $a=160-17=143$.

**Answer:** 143.

**Methods:** polygon angle sum, arithmetic progression, parity.

**Verification:** Exhaustive integer search over all convex arithmetic-progressive angle lists.

**Source comparison:** All four entries were reviewed. The angle-sum equation supplies the parity condition sometimes left implicit in median arguments. The final entry incorrectly describes every angle as 160 before listing a progression; the intended average is 160.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory, algebra. The polygon angle sum and convexity bound an even integral common difference.

## 2011 AIME II Problem 4: A midpoint on an angle bisector

In triangle $ABC$, $AB=20$ and $AC=11$. The internal bisector from $A$ meets $BC$ at $D$, and $M$ is the midpoint of $AD$. Line $BM$ meets $AC$ at $P$. If $CP/PA=m/n$ in lowest terms, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

Take $A$ as vector origin, with position vectors $b,c$ for $B,C$. The angle-bisector theorem gives $BD:DC=20:11$, so $D=(11b+20c)/31$ and $M=(11b+20c)/62$. A point on $BM$ is $(1-t)b+tM$. Its $b$ coefficient vanishes at $t=62/51$, giving $P=20c/51$. Thus $AP:PC=20:31$, and $m+n=51$.

**Answer:** 051.

**Methods:** angle-bisector theorem, affine coordinates, mass points.

**Verification:** Complete analytic proof checked against the archived answer; no independent numerical check claimed.

**Source comparison:** All nine entries were reviewed, including one attribution-only entry. Mass points, Menelaus, and area ratios are valid routes. The barycentric entry reverses its final written fraction; another assumes a right triangle without explaining affine invariance. The vector argument works for every allowed shape.

**Archived entries inspected:** 9 of 9. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The angle-bisector ratio and affine coordinates give a second cevian ratio.

## 2011 AIME II Problem 8: Independent choices among rotated complex roots

Let $z_1,\ldots,z_{12}$ be the roots of $z^{12}=2^{36}$. Independently choose each $w_j$ to equal $z_j$ or $iz_j$. If the maximum of $\operatorname{Re}\sum_jw_j$ is $m+\sqrt n$ for positive integers $m,n$, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

The roots are $8e^{ik\pi/6}$ for $0\le k<12$. For a root $z=a+bi$, the best contribution is $\max(a,-b)$. Opposite roots together contribute $\max(a,-b)+\max(-a,b)=|a+b|$. For $k=0,1,2,3,4,5$, these pair contributions are $8$, $4(\sqrt3+1)$, $4(\sqrt3+1)$, $8$, $4(\sqrt3-1)$, $4(\sqrt3-1)$. Their sum is $16+16\sqrt3=16+\sqrt{768}$. Every choice is independent, so this upper bound is attained; the answer is $784$.

**Answer:** 784.

**Methods:** complex roots, independent maximization, absolute-value identity.

**Verification:** Computed all twelve complex roots numerically and maximized each allowed two-choice real contribution directly.

**Source comparison:** All five stored entries were reviewed, and the full statement was recovered from the alternate archive. The first projection method is sound. Later entries contain errors: sin(x)=cos(x+pi/2) has the wrong sign, the root angle is k*pi/6 rather than k*pi/12, and changing a root sign is not an allowed independent choice. Pairing the already-present opposite roots avoids those issues.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Source correction:** The primary statement was truncated after the first choice; the complete alternate statement specifies w_j in {z_j, i z_j} and asks for the maximum real sum.

**Subject classification:** algebra, geometry. Separability of the objective and opposite root pairs reduce a complex maximum to absolute projections.

## 2011 AIME II Problem 10: A diameter through two chord projections

In a circle of radius $25$ centered at $O$, chords of lengths $30$ and $14$ meet at $P$. Their midpoints are $12$ units apart. If $OP^2=m/n$ in lowest terms, find the remainder of $m+n$ modulo $1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

Let the chord midpoints be $E,F$. Perpendicular projection gives $OE=\sqrt{25^2-15^2}=20$ and $OF=\sqrt{25^2-7^2}=24$. Since $OE\perp EP$ and $OF\perp FP$, both $E,F$ lie on the circle with diameter $OP$. Triangle $OEF$ has sides $20,24,12$ and area $K=\sqrt{28\cdot8\cdot4\cdot16}=32\sqrt{14}$. Its circumradius is $20\cdot24\cdot12/(4K)=45/\sqrt{14}$, so $OP=90/\sqrt{14}$ and $OP^2=4050/7$. Thus the requested remainder is $57$.

**Answer:** 057.

**Methods:** chord midpoint, diameter circle, circumradius, Heron formula.

**Verification:** Independent Cartesian intersection of the two chord lines gives OP squared and the specified midpoint distance.

**Source comparison:** All seven entries were reviewed. The diameter-circle method avoids the vertex-order ambiguities of Ptolemy and trigonometric approaches. Several longer alternatives have mislabeled segments or angles; these do not affect the clean circumradius proof. One entry calls the circumcircle an inscribed circle.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The chord midpoints and intersection lie on the circle with diameter OP.

## 2011 AIME II Problem 13: Circumcenters along a square diagonal

Point $P$ lies inside diagonal $AC$ of square $ABCD$, with $AP>CP$ and side length $12$. Let $O_1,O_2$ be the circumcenters of $ABP,CDP$. If $\angle O_1PO_2=120^\circ$ and $AP=\sqrt a+\sqrt b$ for positive integers $a,b$, find $a+b$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2011_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Put $A=(-s,0)$, $B=(0,s)$, $C=(s,0)$, $D=(0,-s)$, where $s=6\sqrt2$, and $P=(p,0)$ with $0<p<s$. The perpendicular bisectors give $O_1=((p-s)/2,(s-p)/2)$ and $O_2=((p+s)/2,-(p+s)/2)$. Both vectors from $P$ have squared length $(p^2+s^2)/2$, and their dot product is $(p^2-s^2)/2$. Therefore $(p^2-s^2)/(p^2+s^2)=\cos120^\circ=-1/2$, so $p=s/\sqrt3=2\sqrt6$. Thus $AP=s+p=\sqrt{72}+\sqrt{24}$ and the answer is $96$.

**Answer:** 096.

**Methods:** circumcenter, dot product, diagonal coordinates.

**Verification:** Independent distance and dot-product checks verify the proposed circumcenter configuration and 120-degree angle.

**Source comparison:** All nine entries were reviewed, along with the extra solution accidentally attached to the primary statement. The diagonal-coordinate method is reliable and short. Several angle-chasing alternatives interchange circumcenter labels or omit factors of two; one coordinate entry misstates a midpoint while using the correct resulting line.

**Archived entries inspected:** 9 of 9. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Diagonal coordinates make the angle between two circumradius vectors explicit.

## 2012 AIME I Problem 8: A cube slice is a truncated tetrahedron

Take the unit cube $[0,1]^3$ and cut it by the plane through $(0,0,0)$, $(1/2,1,0)$, and $(1,0,1/2)$. These coordinates specify the vertex and edge-midpoints of the archived diagram. If the larger part has reduced volume $p/q$, find $p+q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

The cutting plane is $2x-y-4z=0$. Consider the tetrahedron with vertices
$$D=(0,0,0),\ C=(1,0,0),\ P=(1,2,0),\ N=(1,0,1/2).$$
Its points satisfy $0\le x\le1$, $y,z\ge0$, and $y+4z\le2x$. Thus its intersection with the unit cube is precisely the smaller-side candidate below the cut; the only portion outside the cube has $y>1$. The plane $y=1$ cuts all three edges from $P$ at their midpoints, so that removed tetrahedron is similar to the whole with scale $1/2$.

The base $CPN$ has area $\tfrac12\cdot2\cdot\tfrac12=1/2$ and perpendicular height one from $D$, giving total tetrahedron volume $1/6$. The portion inside the cube therefore has volume $(1-1/8)/6=7/48<1/2$. The larger part has volume $41/48$, and $p+q=89$.

**Answer:** 089.

**Methods:** solid geometry, similar tetrahedra, volume subtraction.

**Verification:** A direct rational cross-section integration independently gives 7/48 for the smaller volume.

**Source comparison:** All seven stored alternatives inspected, including coordinate integration, cross sections, a frustum, and pyramid decomposition. The new proof specifies the missing diagram by coordinates and justifies exactly which part lies outside the cube before subtracting volumes.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Extending the cut creates two similar tetrahedra whose volumes subtract.

## 2012 AIME I Problem 11: Reachability in a lattice semigroup

From $(0,0)$ allow jumps $(7,2),(2,7),(-5,-10),(-10,-5)$. Let $M$ count reachable lattice points with $|x|+|y|\le100$. Find $M\bmod1000$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Necessarily $x+y=3u$, $x-y=5v$ for integers $u,v$ of the same parity. Conversely the jumps in $(u,v)$ are $(3,\pm1),(-5,\pm1)$. Choose large nonnegative $C\equiv u\pmod3$ and put $A=(u+5C)/3$. Then $3A-5C=u$, while $L=A+C\ge|v|$ and $L\equiv u\equiv v\pmod2$. Among these $L$ jumps choose $(L+v)/2$ plus signs, obtaining the target with nonnegative counts. Hence the invariants are sufficient. Now $|x|+|y|=\max(|3u|,|5v|)$, so $-33\le u\le33$, $-20\le v\le20$. Equal parities give $33\cdot21+34\cdot20=1373$ points, hence $373$.

**Answer:** 373.

**Methods:** lattice invariants, reachability, parity.

**Verification:** Independent exact computation passed in tools/verify_middle.py; matches archived answer.

**Source comparison:** The first archived sufficiency argument does not clearly enforce nonnegative jump counts. Taking a sufficiently large solution and assigning signs here proves actual reachability.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, number_theory, geometry. A lattice reachability semigroup is characterized by congruences, and a coordinate transformation turns the diamond region into a rectangle for counting.

## 2012 AIME I Problem 12: An angle bisector inside a trisected right angle

Triangle $ABC$ is right at $C$. Rays $CD,CE$ trisect that right angle and meet $AB$ in the order $A,D,E,B$. Given $DE/EB=8/15$, write $\tan B=m\sqrt p/n$ in reduced squarefree form and find $m+n+p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

In triangle $CDB$, the ray $CE$ bisects the $60^\circ$ angle at $C$. Thus the angle-bisector theorem gives $CD/CB=DE/EB=8/15$. Scale so $CD=8$ and $CB=15$. Drop $DF$ perpendicular to $CB$. Since $\angle DCB=60^\circ$, we have $CF=4$ and $DF=4\sqrt3$, and therefore $BF=15-4=11$. Because $BD$ lies on $BA$,
$$\tan B=\frac{DF}{BF}=\frac{4\sqrt3}{11}.$$
Hence the requested sum is $4+11+3=18$.

**Answer:** 018.

**Methods:** angle bisectors, special right triangles, trigonometric ratios.

**Verification:** The scale-normalized triangle CDB has projection lengths 4,11 and altitude 4√3.

**Source comparison:** All eight stored entries inspected; the last is only an attribution line, not a proof. The others use the angle-bisector theorem, cosine/sine rules, altitudes, or a circumcircle. Several contain swapped labels or missing factors; the angle-bisector route here keeps the construction and side ratios explicit.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. One of the trisectors bisects a smaller triangle angle and gives a side ratio immediately.

## 2012 AIME I Problem 13: Equilateral triangles with three prescribed center distances

Three circles have a common center and radii $3,4,5$. Among equilateral triangles having one vertex on each circle, maximize the area. Write it as $a+(b/c)\sqrt d$, with positive integers, $b,c$ coprime and $d$ squarefree, and find $a+b+c+d$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Let the side length be $s>0$. Place the triangle at $A=(-s/2,0)$, $B=(s/2,0)$, $C=(0,\sqrt3s/2)$ and let the common circle center be $O=(u,v)$, with distances $OA=3$, $OB=4$, $OC=5$. Subtraction and addition of the first two squared-distance equations, followed by the third, give
$$u=-\frac7{2s},\qquad v=\frac{s^2-25}{2\sqrt3s},\qquad 2u^2+2v^2+\frac{s^2}{2}=25.$$
Substituting yields $s^4-50s^2+193=0$, hence
$$s^2=25\pm12\sqrt3.$$
Both values are positive. For either value, the displayed real coordinates $u,v$ satisfy all three original squared-distance equations: the last displayed equation and $2us=-7$ restore $OA^2=9,OB^2=16$, and the expression for $v$ restores $OC^2=25$. Thus both candidate shapes exist, regardless of whether their center is inside the triangle. Area increases with $s^2$, so the maximum is
$$\frac{\sqrt3}{4}(25+12\sqrt3)=9+\frac{25}{4}\sqrt3.$$
The required sum is $9+25+4+3=41$.

**Answer:** 041.

**Methods:** distance-difference linearization, equilateral triangles, quadratic elimination, attainment.

**Verification:** Substitution in the three distance equations verifies both positive squared-side roots.

**Source comparison:** All five stored alternatives inspected. They use a 60-degree rotation, angle equations, Fermat/pedal geometry, coordinates, or another rotation construction. The first assumes an interior center, while the coordinate route handles both configurations. The new proof explicitly reconstructs the center for both algebraic roots and therefore proves the maximum is attainable.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Subtracting distance equations determines the circle center and a quadratic in the squared side length, with a converse.

## 2012 AIME I Problem 14: A zero root sum places the triangle centroid at the origin

The complex roots $a,b,c$ of $z^3+qz+r$ form a nondegenerate right triangle in the complex plane and satisfy $|a|^2+|b|^2+|c|^2=250$. If its hypotenuse is $h$, find $h^2$. The coefficients $q,r$ need not be real.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Vieta gives $a+b+c=0$. Expanding squared complex distances gives the identity
$$|a-b|^2+|b-c|^2+|c-a|^2
=3(|a|^2+|b|^2+|c|^2)-|a+b+c|^2=750.$$
For a right triangle, the two leg squares add to the hypotenuse square, so the sum of all three side squares is $2h^2$. Consequently $h^2=750/2=375$. No conjugate-root symmetry or isosceles condition is needed.

**Answer:** 375.

**Methods:** Vieta formulas, centroids, squared-distance identity.

**Verification:** For arbitrary right-triangle legs, translating its centroid to zero gives total squared vertex norm two-thirds of its hypotenuse square.

**Source comparison:** All seven stored entries inspected. The second and fourth assume real coefficients or an isosceles triangle without authorization; a source comment recognizes this defect. The new proof works for arbitrary complex coefficients and needs only the zero root sum and the right angle.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. Vieta and the centroid squared-distance identity determine the hypotenuse without a real-coefficient assumption.

## 2012 AIME II Problem 4: Three equal travel times determine a rectangle

From a rectangle's northeast corner, riders of speeds $8.6$, $6.2$, and $5$ m/s start together. The first follows the boundary westward, the second southward, and the third rides straight to a point $D$ on the south side. They first reach $D$ simultaneously. The east-west side is longer. Find the primitive ratio of length, width, and distance from the southeast corner to $D$, and report its three entries' sum.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

Scale lengths so the common travel time is one second. Let the east-west length be $L$, north-south width $W$, and the southeast-to-$D$ distance $d$. The three route lengths give
$$2L+W-d=43/5,\qquad W+d=31/5,\qquad W^2+d^2=25.$$
Subtracting the first two yields $L-d=6/5$. Also $(W-d)^2=2(25)-(31/5)^2=(17/5)^2$, so $\{W,d\}=\{7/5,24/5\}$. If $W=24/5,d=7/5$, then $L=13/5<W$, forbidden. Thus $W=7/5,d=24/5,L=6$, with $0<d<L$. The ratio is $30:7:24$, and its entries sum to $61$.

**Answer:** 061.

**Methods:** rates, rectangle geometry, symmetric elimination, branch selection.

**Verification:** Exact squared-distance check (7/5)²+(24/5)²=25 and route lengths 43/5,31/5.

**Source comparison:** Both stored entries inspected. They derive the same unordered pair and use the long-side condition to choose it. The new exposition explicitly verifies that D lies inside the south edge.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Path lengths and a diagonal produce two symmetric dimensions, then the long-side condition selects the branch.

## 2012 AIME II Problem 5: A four-flap net folds into a square pyramid

Concentric, parallel-sided squares have side lengths $40$ and $15$. Attach to each side of the smaller square the triangle whose apex is the midpoint of the corresponding outer side. Fold the four triangles into the lateral faces of a pyramid on the smaller square. Find its volume.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

Each flap has altitude $(40-15)/2=25/2$ from the midpoint of its base side. Its two equal edges become equal lateral edges of the pyramid; consequently the apex projects to the square center, which is equidistant from all four base vertices. The horizontal distance from that center to a side midpoint is $15/2$. Thus the vertical height is
$$h=\sqrt{(25/2)^2-(15/2)^2}=10.$$
The base area is $15^2=225$, and the volume is $225\cdot10/3=750$. These dimensions give a nondegenerate pyramid with exactly the prescribed congruent faces.

**Answer:** 750.

**Methods:** polyhedral nets, square pyramids, Pythagorean theorem.

**Verification:** The slant-height right triangle has squared legs 100 and 225/4, summing to 625/4.

**Source comparison:** The sole stored solution inspected. The new restatement describes the net without its drawing and the proof justifies that the apex lies above the center.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The net determines slant height, then a right triangle gives the pyramid altitude.

## 2012 AIME II Problem 6: A complex-distance maximum fixes a fourth power

Choose $z=a+bi$ with $|z|=5$ and $b>0$ to maximize $|(1+2i)z^3-z^5|$. If $z^4=c+di$, find $c+d$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

Factor out $z^3$: the quantity is $125|1+2i-z^2|$. Since $|z^2|=25$, the triangle inequality bounds it by $125(\sqrt5+25)$. Equality requires $z^2$ to point directly opposite $1+2i$, so
$$z^2=-\frac{25}{\sqrt5}(1+2i).$$
This nonreal number has two opposite square roots, exactly one with positive imaginary part, so the bound is attained under the given restriction. Squaring the displayed equation gives
$$z^4=125(1+2i)^2=-375+500i.$$
Therefore $c+d=125$.

**Answer:** 125.

**Methods:** complex modulus, triangle inequality, equality feasibility.

**Verification:** The resulting fourth power has real and imaginary parts −375 and 500, with modulus 625 as required.

**Source comparison:** Both stored alternatives inspected. One uses vector direction and the other arguments. The new proof gives the explicit triangle-inequality equality condition and checks the upper-half-plane square-root restriction.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. The triangle inequality on a circle determines the maximizing direction and an attainable square-root branch.

## 2012 AIME II Problem 13: Sum squared distances before computing rotated vertices

An equilateral triangle $ABC$ has side $\sqrt{111}$. The two points $D_1,D_2$ satisfy $AD_i=\sqrt{111}$ and $BD_i=\sqrt{11}$. For each segment $AD_i$, construct both equilateral third vertices, giving four points $E_1,\ldots,E_4$. Find $\sum_{j=1}^4 CE_j^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Use vector coordinates with $A=0$, $B=(s,0)$, $C=(s/2,\sqrt3s/2)$ and $s^2=111$. Subtracting $|D_i-B|^2=11$ from $|D_i|^2=111$ gives $(D_i)_x=211/(2s)$. The two circle intersections have opposite vertical coordinates, so $D_1+D_2=(211/s,0)$.

The two equilateral third vertices built on $AD_i$ are the rotations $R_{60}D_i$ and $R_{-60}D_i$. Their sum is $2\cos60^\circ D_i=D_i$, and each has squared norm $111$. Therefore $\sum_jE_j=D_1+D_2$ and
$$\sum_{j=1}^4|C-E_j|^2
=4|C|^2+\sum_j|E_j|^2-2C\cdot\sum_jE_j
=888-211=677.$$
This computes the aggregate without evaluating any individual radical coordinate.

**Answer:** 677.

**Methods:** rotation sums, vector projections, squared distances.

**Verification:** The common horizontal projection is 211/(2√111); the four squared distances sum to 888−211.

**Source comparison:** All five stored alternatives inspected, using angle-sum cosines, complex rotations, or paired cosine rules. The new proof isolates the common cancellation as a two-rotation vector identity, avoiding the labeling and repeated-term typos in some entries.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Pairing opposite rotations cancels perpendicular components and leaves a single projection.

## 2012 AIME II Problem 15: Two circle equations and their common chord

A triangle with $AB=5$, $AC=3$, $BC=7$ has circumcircle $\omega$. Its internal angle bisector from $A$ meets $BC$ at $D$ and $\omega$ again at $E$. The circle with diameter $DE$ meets $\omega$ again at $F\ne E$. Write $AF^2=m/n$ in lowest terms and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2012_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

The cosine rule gives $\cos A=(25+9-49)/(2\cdot5\cdot3)=-1/2$, so $A=120^\circ$. Place $A=(0,0)$ with its bisector on the positive horizontal axis, and choose
$$B=(5/2,5\sqrt3/2),\qquad C=(3/2,-3\sqrt3/2).$$
The angle-bisector ratio $BD:DC=5:3$ gives $D=(15/8,0)$. The circle through $A,B,C$ has equation
$$x^2+y^2-8x-\frac2{\sqrt3}y=0,$$
so its second horizontal-axis point is $E=(8,0)$. The circle with diameter $DE$ is
$$x^2+y^2-\frac{79}{8}x+15=0.$$
Subtracting these equations gives their common chord line
$$y=\frac{15\sqrt3}{16}(x-8).$$
Put $t=x-8$ and substitute into the first circle. The equation factors as $t(1568+931t)=0$. The root zero is $E$; the other is $t=-32/19$, giving
$$F=\left(\frac{120}{19},-\frac{30\sqrt3}{19}\right).$$
It satisfies both circle equations and differs from $E$, so it is the required point. Hence $AF^2=(14400+2700)/361=900/19$, and $m+n=919$.

**Answer:** 919.

**Methods:** angle bisectors, circle equations, radical axis, exact coordinates.

**Verification:** Exact substitution of F verifies both circles and AF²=900/19.

**Source comparison:** All six stored alternatives inspected: inversion with reflection, trigonometric projection, a symmedian argument, an auxiliary diameter, angle chasing, and a longer inversion computation. Several have missing labels or incorrect general factors. The new coordinate proof subtracts the two circle equations and verifies the second intersection directly.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Angle-bisector coordinates and a radical-axis subtraction locate the second circle intersection exactly.

## 2013 AIME I Problem 3: Area fractions determine a reciprocal side ratio

Two perpendicular cuts parallel to the sides partition a square into two squares and two nonsquare rectangles. Let $a,b$ be the two segment lengths into which either cut divides its perpendicular side. The two smaller squares occupy $9/10$ of the original area. Find $a/b+b/a$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

The two smaller squares must be diagonally opposite: adjacent square cells would force all four cells to be squares, contrary to the two nonsquare rectangles. Thus their sides are $a,b$, and each rectangle has sides $a,b$. Hence
$$a^2+b^2=\frac9{10}(a+b)^2,\qquad 2ab=\frac1{10}(a+b)^2.$$
Dividing gives $(a^2+b^2)/(ab)=18$, the requested sum. Positive unequal lengths exist: the ratio solves $t^2-18t+1=0$, with positive roots $9\pm4\sqrt5$.

**Answer:** 018.

**Methods:** square partitions, symmetric sums, area ratios.

**Verification:** The positive ratio roots have product one and sum eighteen.

**Source comparison:** All seven stored entries inspected. They use area complements, normalization, Vieta, or an explicit quadratic. The present argument retains the common invariant and explains why the square cells are opposite.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A square partition gives a symmetric ratio invariant from areas.

## 2013 AIME I Problem 7: Triangle through three face centers

A rectangular box has side lengths $12,16,h$, with $h>0$. The centers of the three faces incident to one vertex form a triangle of area $30$. Write $h=m/n$ in lowest terms and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

Place the corner at the origin and write $h=2t$. The three centers are $(6,8,0)$, $(6,0,t)$, and $(0,8,t)$. From the first center, the edge vectors are $(0,-8,t)$ and $(-6,0,t)$; their cross product has squared norm $64t^2+36t^2+48^2$. Consequently
$$4(30)^2=100t^2+2304,$$
so $t^2=324/25$. Positivity gives $t=18/5$ and $h=36/5$, hence the answer is $41$.

**Answer:** 041.

**Methods:** solid geometry, cross product, triangle area.

**Verification:** Exact squared cross-product check: 100·(18/5)²+2304=3600.

**Source comparison:** All six stored entries inspected, including altitude, vector, Heron, de Gua, cosine-rule and expanded-Heron routes. One Heron entry displays an extraneous factor 1/2; the independently written cross-product computation avoids that transcription error.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A spatial triangle area is obtained from a cross product.

## 2013 AIME I Problem 9: A folding crease from equal distances

An equilateral triangle $ABC$ has side $12$. Reflect $A$ onto the point $D$ of $BC$ with $BD=9$. Find the length of the crease inside the triangle as $m\sqrt p/n$, with $m,n$ coprime and $p$ squarefree, and report $m+n+p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

Let the crease meet $AB,AC$ at $P,Q$, and put $AP=u$, $AQ=v$. Reflection gives $DP=u$ and $DQ=v$. The cosine rule in $BPD$ gives
$$u^2=(12-u)^2+9^2-9(12-u),$$
so $u=39/5$. Similarly, in $CQD$,
$$v^2=(12-v)^2+3^2-3(12-v),$$
so $v=39/7$. Both values lie between zero and twelve, verifying that the intersections are on the sides. The line through these two equal-distance points is the perpendicular bisector of $AD$, so it is exactly the required crease. Finally $\angle PAQ=60^\circ$, and
$$PQ^2=u^2+v^2-uv=\frac{39^2\cdot39}{35^2}.$$
Thus $PQ=39\sqrt{39}/35$ and the answer is $113$.

**Answer:** 113.

**Methods:** reflection, perpendicular bisectors, cosine rule.

**Verification:** Exact cosine-rule calculation with u=39/5 and v=39/7 gives 39³/35².

**Source comparison:** All five stored entries inspected: trigonometric, equal-distance, similarity, coordinate, and a sketch-only Heron route. The last entry is incomplete and has compressed numeric transcription; it is not treated as an additional complete proof.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Reflection makes the crease a perpendicular bisector, reducing its endpoints to linear equations.

## 2013 AIME I Problem 12: A supporting line fixes a hexagon enclosure

A regular hexagon $ABCDEF$ of side one is contained in a triangle $PQR$ with angles $P=75^\circ$, $Q=60^\circ$, $R=45^\circ$. Its edges $AB,CD$ lie on $PQ,QR$, and another vertex lies on $RP$. Write the triangle area as $(a+b\sqrt c)/d$, with $c$ squarefree and $a,d$ coprime, and find $a+b+c+d$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

Place $Q=(0,0)$ with $QP$ along the positive horizontal axis. The intersection of the two hexagon side lines makes $QBC$ equilateral. Up to reflection the vertices therefore have coordinates
$$A=(2,0),\ B=(1,0),\ C=(1/2,\sqrt3/2),\ D=(1,\sqrt3),\ E=(2,\sqrt3),\ F=(5/2,\sqrt3/2).$$
The line $QR$ is $y=\sqrt3x$. Since the angle at $P$ is $75^\circ$, the line $PR$ has equation $y+(2+\sqrt3)x=k$. Containment and contact mean $k$ is the maximum of this linear expression on the six vertices. Evaluation gives its unique maximum at $F$, namely $k=5+3\sqrt3$. This establishes which vertex touches the side without a diagram assumption.

The horizontal intercept is $QP=k/(2+\sqrt3)=1+\sqrt3$. Intersecting with $y=\sqrt3x$ gives $y_R=(3+2\sqrt3)/2$. All six vertices satisfy the three containing half-plane inequalities, so this construction is feasible. The area is
$$\frac12 QP\,y_R=\frac{9+5\sqrt3}{4},$$
which yields $9+5+3+4=21$.

**Answer:** 021.

**Methods:** regular polygons, supporting lines, coordinate geometry, containment.

**Verification:** Coordinates verify unit side lengths, the two side lines, the supporting maximum, and the exact area.

**Source comparison:** All seven stored entries inspected. Several assume the touching vertex from a diagram; the new proof certifies it by a supporting linear functional. The second stored entry has an incorrect line intercept (5+√3 instead of 5+3√3). The fifth uses undefined auxiliary labels without a retained diagram and is not regarded as a self-contained textual proof.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A regular hexagon is enclosed by three lines of prescribed directions; a support maximum determines the final side.

## 2013 AIME I Problem 13: A self-similar union sums to one rational area

Begin with a triangle $AB_0C_0$ of side lengths $AB_0=12$, $B_0C_0=17$, $AC_0=25$. At each stage choose $B_n$ on $AB_{n-1}$ and $C_n$ on $AC_{n-1}$ so that, in the displayed vertex order,
$$AB_nC_n\sim B_{n-1}C_nC_{n-1}\sim AB_{n-1}C_{n-1}.$$
If the union of triangles $B_{n-1}C_nB_n$ for $n\ge1$ has reduced rational area $p/q$, determine $q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Heron's formula gives original area $\sqrt{27\cdot15\cdot10\cdot2}=90$. The similarity from $AB_0C_0$ to $B_0C_1C_0$ has scale $17/25$, hence $C_1C_0=289/25$ and $AC_1=336/25$. Thus the nested triangle $AB_1C_1$ has linear scale
$$t=\frac{336}{625}.$$
The same scale applies at every stage because all containing triangles are similar with the same ordered construction. The triangle $AB_0C_1$ has area $90t$, while $AB_1C_1$ has area $90t^2$; subtracting gives first target area $90t(1-t)$. Subsequent target triangles are scaled by successive factors $t^2$ in area. Their interiors are disjoint because each lies in the part removed from its containing nested triangle. Since $0<t<1$, the total is
$$\frac{90t(1-t)}{1-t^2}=\frac{90t}{1+t}=\frac{30240}{961}.$$
Now $961=31^2$ and $30240\equiv15\pmod{31}$, so the fraction is reduced. Therefore $q=961$.

**Answer:** 961.

**Methods:** similarity, geometric series, disjoint area decomposition.

**Verification:** Exact rational geometric-series computation gives 30240/961; gcd(30240,961)=1.

**Source comparison:** All four stored entries inspected. They sum either the target pieces or their complements. Several display inconsistent series powers or a missing original-area factor. The fourth incorrectly calls 961 prime; the final reduction here explicitly uses 961=31² and checks the numerator modulo 31.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Similar triangles produce disjoint geometric-series area contributions.

## 2013 AIME II Problem 4: Choose the correct equilateral vertex by rotation

Let $A=(1,0)$ and $B=(2,2\sqrt3)$. Of the two equilateral triangles on $AB$, choose the one with third vertex $C$ in the first quadrant. If its center is $(x,y)$ and $xy=p\sqrt q/r$ in reduced squarefree form, find $p+q+r$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

Rotate the displacement $B-A=(1,2\sqrt3)$ clockwise by $60^\circ$. The result is $(7/2,\sqrt3/2)$, so $C=(9/2,\sqrt3/2)$. The opposite rotation gives $C'=(-3/2,3\sqrt3/2)$, outside the first quadrant, confirming the branch. All centers of an equilateral triangle coincide with its centroid, giving
$$(x,y)=\frac{A+B+C}{3}=\left(\frac52,\frac{5\sqrt3}{6}\right).$$
Thus $xy=25\sqrt3/12$, and the answer is $25+3+12=40$.

**Answer:** 040.

**Methods:** rotation, equilateral triangles, centroids.

**Verification:** Rotation preserves the side length √13; both candidate coordinates and the positive-quadrant choice are checked exactly.

**Source comparison:** All seven stored entries inspected: perpendicular-bisector, complex rotation, slope, matrix, circle-intersection, midpoint-vector, and complex quadratic routes. The first has a final summand typo; the new proof explicitly checks both rotated vertices.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A 60-degree rotation constructs the third vertex, and the center is its centroid.

## 2013 AIME II Problem 5: An angle sine from one small triangle area

In an equilateral triangle $ABC$, the points $D,E$ divide $BC$ into three equal parts. Express $\sin\angle DAE$ as $a\sqrt b/c$, with $a,c$ coprime and $b$ squarefree, and find $a+b+c$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

Scale the side length to three. The altitude is $3\sqrt3/2$, while each of $D,E$ is distance $1/2$ from its foot. Hence $AD^2=AE^2=1/4+27/4=7$. Since $DE=1$, the area of $ADE$ is $3\sqrt3/4$. The sine-area formula now gives
$$\sin\angle DAE=\frac{2[ADE]}{AD\cdot AE}=\frac{3\sqrt3}{14}.$$
Thus the required sum is $3+3+14=20$.

**Answer:** 020.

**Methods:** triangle area, similarity normalization, sine area formula.

**Verification:** Exact squared cevian length seven and area 3√3/4 give the stated sine.

**Source comparison:** All five stored alternatives inspected: double angle, area ratio, complex quotient, cosine rule, and dot product. The fourth initially labels the cosine-rule angle incorrectly; the area argument bypasses that typo and unnecessary inverse trigonometry.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Similarity normalization and the area formula avoid finding the angle itself.

## 2013 AIME II Problem 8: Repeated chord lengths force a diameter

A convex hexagon inscribed in a circle has successive side lengths $22,22,20,22,22,20$. Its circumradius is $p+\sqrt q$, for positive integers $p,q$. Find $p+q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

Relabel cyclically so that $AB=CD=DE=FA=22$ and $BC=EF=20$. Each side length occurs more than once. No boundary arc can exceed a semicircle: if one did, another equal chord would require the complementary minor arc, and these two arcs alone would already total a full circle, leaving no room for the other edges. A semicircle is likewise impossible. Thus equal chords have equal boundary arcs, and each three-edge block $22,20,22$ spans exactly half the circle. Hence $AD$ is a diameter.

In the cyclic quadrilateral $ABCD$, the equal end chords give $AC=BD=x$. Ptolemy gives $x^2=22^2+20(2R)$. The right triangle $ABD$ gives $x^2+22^2=(2R)^2$. Combining,
$$R^2-10R-242=0.$$
The positive root is $R=5+\sqrt{267}$, so $p+q=272$.

**Answer:** 272.

**Methods:** cyclic quadrilaterals, Ptolemy theorem, arc order, diameters.

**Verification:** Substitution R=5+√267 verifies R²−10R−242=0 and R>11, the chord-radius lower bound.

**Source comparison:** All eight stored entries inspected. The first is diagram code only; the others use trigonometry, trapezoid coordinates, Ptolemy, or similarity. The new proof justifies the diameter and symmetry that most entries assume from the figure. A squared-equation alternative selects a branch from the answer format; the present quadratic has only one positive root.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Arc order justifies central symmetry, then Ptolemy and a right triangle determine the radius.

## 2013 AIME II Problem 10: A constant area ratio turns a secant maximum into a right angle

A circle has center $O$ and radius $\sqrt{13}$. A point $A$ has $AO=4+\sqrt{13}$, and $B$ is the point of the circle closest to $A$. As a secant through $A$ cuts the circle at $K,L$, maximize $[BKL]$. Write the maximum as $(a-b\sqrt c)/d$ in reduced squarefree form and find $a+b+c+d$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

For every line through $A$, perpendicular distances from $B$ and $O$ to the line have ratio $AB/AO=4/(4+\sqrt{13})$, since $A,B,O$ are collinear in that order. The two triangles share base $KL$, so
$$[BKL]=\frac4{4+\sqrt{13}}[OKL].$$
With $OK=OL=\sqrt{13}$, the latter area is at most $13/2$, with equality when the two radii are perpendicular. This equality is feasible for a secant through $A$: a right-angle chord is at distance $\sqrt{13/2}$ from $O$, and a line through $A$ at this distance exists because $AO>\sqrt{13/2}$. Thus the maximum is
$$\frac{26}{4+\sqrt{13}}=\frac{104-26\sqrt{13}}3.$$
The requested sum is $104+26+13+3=146$.

**Answer:** 146.

**Methods:** area ratios, secant chords, optimization, equality feasibility.

**Verification:** The attainable central-triangle maximum is 13/2; rationalization gives (104−26√13)/3.

**Source comparison:** All five stored entries inspected. Four contain arguments and one is a link-only pointer, whose linked page is not claimed separately reviewed. The first has a sign error in its radical area expression and does not justify its maximum. The constant-height-ratio route is retained with an explicit construction proving equality is feasible.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Heights from collinear fixed points have a constant ratio for lines through their common external point.

## 2013 AIME II Problem 13: Affine midpoint coordinates linearize two distances

In an isosceles triangle $ABC$ with $AC=BC$, choose $D$ on $BC$ so that $CD=3BD$, and let $E$ be the midpoint of $AD$. Given $CE=\sqrt7$ and $BE=3$, express $[ABC]=m\sqrt n$ with $n$ squarefree and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Write $A=(-u,0)$, $B=(u,0)$, $C=(0,h)$ with $u,h>0$. The prescribed divisions give
$$D=(3u/4,h/4),\qquad E=(-u/8,h/8).$$
Therefore the two squared distances yield
$$u^2+49h^2=448,\qquad81u^2+h^2=576.$$
Solving gives $u^2=7$, $h^2=9$. Their positive roots produce an actual nondegenerate triangle and points in the specified segments, so no extraneous candidate remains. The area is $\tfrac12(2u)h=3\sqrt7$, and $m+n=10$.

**Answer:** 010.

**Methods:** affine coordinates, squared-distance equations, isosceles triangles.

**Verification:** Substitution u²=7,h²=9 gives exactly CE²=7 and BE²=9.

**Source comparison:** All nine stored entries inspected: Stewart, cosine-rule systems, mass points, Cartesian and barycentric distances, and a right-angle approach. Some cosine formulas omit factors, and the right-angle route labels a full segment length incorrectly. The coordinate proof gives a short complete feasibility check.

**Archived entries inspected:** 9 of 9. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. An isosceles placement turns two squared-distance conditions into a linear system in squared dimensions.

## 2013 AIME II Problem 15: A triangle identity with a radical-sign branch condition

Triangle angles $A,B,C$ satisfy
$$\cos^2A+\cos^2B+2\sin A\sin B\cos C=15/8,$$
$$\cos^2B+\cos^2C+2\sin B\sin C\cos A=14/9.$$
The expression $\cos^2C+\cos^2A+2\sin C\sin A\cos B$ has the form $(p-q\sqrt r)/s$ for positive integers $p,q,r,s$, with $r$ squarefree and $\gcd(p+q,s)=1$. Determine $p+q+r+s$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2013_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

The sine rule permits a similar triangle with sides $\sin A,\sin B,\sin C$. Applying the cosine rule to it gives
$$\sin^2A+\sin^2B-2\sin A\sin B\cos C=\sin^2C.$$
Thus the first given expression equals $2-\sin^2C$; cyclically, the second equals $2-\sin^2A$, and the target equals $2-\sin^2B$. We obtain $\sin A=2/3$ and $\sin C=1/\sqrt8$.

Let $A_0,C_0$ be the acute angles with those sines. Since $A_0>C_0$, taking $C=\pi-C_0$ would force $A+C>\pi$, so $C=C_0$ and $\cos C=\sqrt{14}/4$. There remain two legitimate triangle branches, $A=A_0$ and $A=\pi-A_0$. Using $\sin B=\sin(A+C)$ gives
$$\sin^2B=\frac{33\pm4\sqrt{35}}{72},\qquad
2-\sin^2B=\frac{111\mp4\sqrt{35}}{72}.$$
The stipulated representation has a negative irrational term with a positive coefficient, so uniqueness of squarefree radical representation selects the minus sign in the target. This branch is feasible: $A_0,C_0$ are positive acute angles with sum less than $\pi$. Finally $\gcd(111+4,72)=1$, and the answer is $111+4+35+72=222$.

Without the stipulated negative-radical form, the two equations alone would allow both displayed target values.

**Answer:** 222.

**Methods:** sine rule, cosine rule, trigonometric identities, branch selection.

**Verification:** Both acute/supplementary A branches satisfy the two given equations; only the acute branch gives the specified negative radical coefficient.

**Source comparison:** All six stored entries inspected. They all choose positive cosines without proving the angle branch; one comment mentions an acute-triangle wording not present in the reviewed statement. The new solution keeps both feasible branches and uses the explicitly prescribed negative-radical form to select the requested one. Other sign/transcription errors in the alternatives do not affect the independently derived identity.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Source correction:** **Type:** missing_branch_argument_in_sources **Note:** The given equations allow two triangle shapes. The positive q in the prescribed p−q√r form selects the intended target; no blanket acute-triangle assumption is made.

**Subject classification:** geometry, algebra. The sine-rule cosine identity simplifies the expressions, but the prescribed radical sign is needed to select an angle branch.

## 2014 AIME I Problem 1: The length of a crossed shoelace

Eight eyelets lie at four equally spaced positions on each long side of a $50$ by $80$ mm rectangle. A lace joins the two eyelets at one short end, then has two crossing strands between each successive eyelet pair. Each free end needs another $200$ mm. Find its minimum length.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

Each crossing strand has horizontal displacement $50$ and vertical displacement $80/3$, so its length is $\sqrt{50^2+(80/3)^2}=170/3$. There are six such strands, one short-side segment, and two free ends. The minimum is $6(170/3)+50+2(200)=790$ mm.

**Answer:** 790.

**Methods:** Pythagorean theorem, segment lengths.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** The sole source uses the same six-diagonal decomposition; all dimensions and lace connections are stated explicitly here.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The length of a crossed shoelace; Pythagorean theorem, segment lengths supply the essential reduction.

## 2014 AIME I Problem 5: Disk-separable vertex subsets

Count subsets of a regular dodecagon that are precisely its vertices strictly inside some circle.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

On the circumcircle $|X|=R$, the disk condition $|X-c|^2<r^2$ becomes the linear inequality $c\cdot X>(R^2+|c|^2-r^2)/2$. Consequently a nonempty proper subset must be a consecutive cyclic interval. Conversely each such interval is cut off by a suitable line, and a disk realizes the same strict inequality on the circumcircle. There are $12$ intervals of each size $1$ through $11$; add the empty and full sets: $12\cdot11+2=134$.

**Answer:** 134.

**Methods:** cyclic intervals, geometry counting.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The source identifies consecutive vertices; this proof supplies the missing linearization and converse.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Disk-separable vertex subsets; the proof uses cyclic intervals, geometry counting.

## 2014 AIME I Problem 7: The largest argument seen from an exterior point

Complex numbers satisfy $|w|=1$ and $|z|=10$. Let $\theta=\arg((w-z)/z)$. If the maximum of $\tan^2\theta$ is $p/q$ in lowest terms, find $p+q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

The complex number $w/z-1$ ranges over the circle of radius $1/10$ centered at $-1$. Its greatest angle away from the negative real axis occurs on a tangent ray from the origin. The resulting right triangle has hypotenuse $1$, opposite leg $1/10$, and adjacent leg $\sqrt{99}/10$. Therefore the largest squared tangent is $1/99$, giving $p+q=100$.

**Answer:** 100.

**Methods:** complex loci, tangent extremum.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three sources inspected. Differentiation, an AM-GM cosine bound, and the tangent-circle construction agree. The geometric tangent proof avoids calculus.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. The largest argument seen from an exterior point; complex loci, tangent extremum supply the essential reduction.

## 2014 AIME I Problem 10: A disk rolling around a larger disk

A unit disk rolls without slipping around the outside of a fixed radius-5 disk. Initially their tangency point is $A$ and the larger center is $E$. After the unit disk makes one full rotation relative to the plane, its marked point initially at $A$ is $B$. Write $\sin^2\angle BEA=m/n$ in lowest terms and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

If the line of centers sweeps angle $\alpha$, no-slip rolling turns the unit disk through $(5+1)\alpha$: the contact arc contributes $5\alpha$ and the moving radius another $\alpha$. Thus one full rotation gives $\alpha=\pi/3$. Put $E=(0,0)$, $A=(5,0)$, and the initial small center at $(6,0)$. The new center is $(3,3\sqrt3)$. The marked radius has returned to its initial vector $(-1,0)$, so $B=(2,3\sqrt3)$. Hence $\sin^2\angle BEA=27/(4+27)=27/31$, giving $58$.

**Answer:** 058.

**Methods:** rolling circles, angular motion, coordinates.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both sources inspected. Arc-length reasoning and the extra revolution of external rolling give a 60-degree center displacement. Coordinates shorten the final trigonometry.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A disk rolling around a larger disk; rolling circles, angular motion, coordinates supply the essential reduction.

## 2014 AIME I Problem 11: Diagonal endpoint of a random walk

A planar simple random walk starts at the origin and takes six unit axis steps. Find numerator plus denominator of its probability of ending on either diagonal $y=x$ or $y=-x$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Use coordinates $u=x+y, v=x-y$. Each step independently chooses a uniform sign for $u$ and for $v$, so $u$ and $v$ are independent six-step one-dimensional walks. Each is zero with probability $\binom63/2^6=5/16$. Thus $P(uv=0)=2(5/16)-(5/16)^2=135/256$. Answer: $391$.

**Answer:** 391.

**Methods:** random walks, coordinate bijection, inclusion-exclusion.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Diagonal endpoint of a random walk; the proof uses random walks, coordinate bijection, inclusion-exclusion.

## 2014 AIME I Problem 13: A square cut by equal perpendicular chords

Points $E,F,G,H$ lie respectively on sides $AB,BC,CD,DA$ of a square. Segments $EG,FH$ are perpendicular, each of length 34, and meet at $P$. The areas $AEPH,BFPE,CGPF,DHPG$ have ratio $269:275:405:411$. Find the square area.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Let the side be $s$, with $A=(0,s),B=(0,0),C=(s,0),D=(s,s)$, and put $t=G_y-E_y$. The lower trapezoid has half the square area, so $E_y=(s-t)/2$ and $G_y=(s+t)/2$. Perpendicularity gives $H_x-F_x=-t$; the right trapezoid has area $3s^2/5$, giving $F_x+H_x=4s/5$. Thus the segment midpoints are $Q=(s/2,s/2)$ and $R=(2s/5,s/2)$. The right triangle $PQR$ has legs $s^2/(10\cdot34)$ and $st/(10\cdot34)$. Subtracting the equal corner triangles, or applying the shoelace formula to these coordinates, gives $[DHPG]=3s^2/10+[PQR]$. Since $411/1360-3/10=3/1360$, we obtain $st/34^2=15/34$, hence $st=510$. Also $s^2+t^2=34^2=1156$. Therefore $s^2$ is either $850$ or $306$; the latter would make the square diagonal shorter than 34. The area is $850$.

**Answer:** 850.

**Methods:** area ratios, perpendicular projections, quadratic elimination.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four sources inspected. Two rigorous area/projection arguments and a related similarity calculation agree. Index 2 merely guesses Pythagorean-type representations from the answer format and is not used as a proof.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A square cut by equal perpendicular chords; area ratios, perpendicular projections, quadratic elimination supply the essential reduction.

## 2014 AIME I Problem 15: A circle through a right-triangle vertex

In right triangle $ABC$, $AB=3,BC=4,AC=5$. A circle meets $AB$ at $B,E$, $BC$ at $B,D$, and $AC$ at $F,G$. Suppose $EF=DF$ and $DG/EG=3/4$. Write $DE=a\sqrt b/c$ in reduced radical form and find $a+b+c$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Use $B=(0,0),A=(0,3),C=(4,0)$, $D=(d,0),E=(0,e)$. Since $\angle DBE=90^\circ$, $DE$ is a diameter. Equal chords $DF,EF$ subtend equal angles at $B$, so $BF$ bisects the right angle; intersecting $y=x$ with $3x+4y=12$ gives $F=(12/7,12/7)$. The chord ratio is $DG/EG=\sin\angle DBG/\sin\angle EBG=G_y/G_x=3/4$, so $G=(2,3/2)$. The circle through $B,D,E$ has equation $x^2+y^2=dx+ey$. Substituting $F,G$ yields $d+e=24/7$ and $4d+3e=25/2$. Hence $d=31/14,e=17/14$, and $DE=\sqrt{d^2+e^2}=25\sqrt2/14$. The answer is $41$.

**Answer:** 041.

**Methods:** equal chords, angle bisectors, circle equations.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All seven sources inspected. Equal chords identify the angle bisector and the 3:4 chord ratio identifies the hypotenuse midpoint. Source methods finish with power of a point, Ptolemy, or trigonometry; a circle equation supplies a compact independent finish.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A circle through a right-triangle vertex; equal chords, angle bisectors, circle equations supply the essential reduction.

## 2014 AIME II Problem 3: A hinged rectangle retaining its area

A rectangle has sides $a$ and 36. Hinges at the vertices and midpoints of the 36-sides allow it to become a convex hexagon: the length-$a$ sides remain parallel 24 units apart, and each former 36-side becomes two 18-unit segments meeting outward. If area is unchanged, find $a^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

The hexagon consists of an $a\times24$ rectangle and two isosceles triangles with sides 18,18,24. Each triangle has altitude $\sqrt{18^2-12^2}=6\sqrt5$ and area $72\sqrt5$. Thus $36a=24a+144\sqrt5$, so $a=12\sqrt5$ and $a^2=720$.

**Answer:** 720.

**Methods:** area decomposition, Pythagorean theorem.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both sources inspected. Heron and a direct altitude computation give identical triangle areas; the latter is shorter.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A hinged rectangle retaining its area; area decomposition, Pythagorean theorem supply the essential reduction.

## 2014 AIME II Problem 8: Three mutually tangent circles and a diameter

A radius-2 circle has diameter $AB$. A smaller circle is internally tangent at $A$. A third circle is internally tangent to the large circle, externally tangent to the second circle, and tangent to $AB$. The second radius is three times the third. Write it as $\sqrt m-n$ and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

Let the third radius be $r$. Put the large center at $(0,0)$ and $A=(-2,0)$; the second center is $(3r-2,0)$. Reflect if necessary so the third center is $(x,r)$. Its distance to the second center is $4r$, so their horizontal separation is $\sqrt{15}r$. The left-hand choice would give $x=(3-\sqrt{15})r-2<-2$, impossible inside the large circle. Hence $x=(3+\sqrt{15})r-2$. Internal tangency gives $x^2+r^2=(2-r)^2$. Removing the positive factor $r$ yields $(24+6\sqrt{15})r=8+4\sqrt{15}$. Thus $3r=4\sqrt{15}-14=\sqrt{240}-14$, and the answer is 254.

**Answer:** 254.

**Methods:** circle tangency, distance equations.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four sources inspected. Direct coordinates, a cosine-law calculation, and Descartes after reflection agree. The independent coordinate argument checks the horizontal-sign choice explicitly.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Three mutually tangent circles and a diameter; circle tangency, distance equations supply the essential reduction.

## 2014 AIME II Problem 10: A reciprocal equation creates an equilateral triangle

Let $|z|=2014$. Form the polygon with vertices $z$ and all complex $w$ satisfying $1/(z+w)=1/z+1/w$. Its area is $n\sqrt3$. Find $n$ modulo 1000.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

The equation becomes $w^2+wz+z^2=0$, so $w/z$ is one of the two nontrivial cube roots of unity. The three vertices therefore form an equilateral triangle with circumradius 2014 and area $(3\sqrt3/4)2014^2=3\cdot1007^2\sqrt3$. Thus $n\equiv3\cdot7^2=147\pmod{1000}$.

**Answer:** 147.

**Methods:** roots of unity, complex ratios, regular polygons.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four sources inspected. Algebraic factorization, direct coordinates, and complex-angle interpretations all identify the equilateral triangle.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. A reciprocal equation creates an equilateral triangle; roots of unity, complex ratios, regular polygons supply the essential reduction.

## 2014 AIME II Problem 11: An isosceles extension of a triangle

In triangle $RED$, angles at $R,E$ are 75 and 45 degrees and $RD=1$. Let $M$ be the midpoint of $RD$, and choose $C$ on $ED$ with $RC\perp EM$. Extend $DE$ beyond $E$ to $A$ so that $AC=AR$. If $AE=(a-\sqrt b)/c$ in reduced form, find $a+b+c$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Let $P$ be the foot from $A$ to $RC$. Since $AC=AR$, $P$ is the midpoint of $RC$. The midpoint theorem gives $PM\parallel CD$ and $PM=CD/2$; also $AP\parallel EM$. Thus $APME$ is a parallelogram and $AE=CD/2$. Set $D=(0,0)$, $R=(1/2,\sqrt3/2)$, $E=((1+\sqrt3)/2,0)$. Then $M=(1/4,\sqrt3/4)$, and perpendicular slopes give $C_x=(\sqrt3-1)/(1+2\sqrt3)$. Consequently $AE=(\sqrt3-1)/(2+4\sqrt3)=(7-3\sqrt3)/22=(7-\sqrt{27})/22$, giving 56.

**Answer:** 056.

**Methods:** midpoint theorem, perpendicular slopes, isosceles triangles.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three source solutions inspected. The midpoint-parallelogram relation reduces the construction to CD/2; direct coordinates then give the required radical.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. An isosceles extension of a triangle; midpoint theorem, perpendicular slopes, isosceles triangles supply the essential reduction.

## 2014 AIME II Problem 12: A triple-angle condition forces one angle

Triangle angles satisfy $\cos3A+\cos3B+\cos3C=1$. Two sides have lengths 10 and 13. The greatest possible third side is $\sqrt m$; find $m$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Since $C=\pi-A-B$, the condition becomes $\cos3A+\cos3B-\cos(3A+3B)-1=0$. Sum-to-product factors the left side as $4\sin(3A/2)\sin(3B/2)\cos(3(A+B)/2)$. With positive triangle angles, its vanishing means $A=120^\circ$, $B=120^\circ$, or $C=120^\circ$. Conversely each case satisfies the condition. To maximize the unknown side, put it opposite that 120-degree angle; any other placement makes it shorter than the known longest side 13. The cosine law gives $m=10^2+13^2-260\cos120^\circ=399$.

**Answer:** 399.

**Methods:** trigonometric factorization, cosine law, extremal side length.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four sources inspected. The sum-to-product solution is complete. The first introduces unsigned square roots for sine values, and the last simply guesses 120 degrees from answer integrality; these arguments are not used.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A triple-angle condition forces one angle; trigonometric factorization, cosine law, extremal side length supply the essential reduction.

## 2014 AIME II Problem 14: Midpoint projections on an angle bisector

Triangle $ABC$ has $AB=10$, angle $A=30^\circ$, and angle $C=45^\circ$. On line $BC$, let $H$ be the foot from $A$, $D$ the internal angle-bisector intersection, and $M$ the midpoint of $BC$. Let $N$ be the midpoint of $HM$, and choose $P$ on ray $AD$ with $PN\perp BC$. If $AP^2=m/n$ in lowest terms, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2014_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

The sine law gives $BC=5\sqrt2$ and $AC=5(1+\sqrt3)$. Since angle $C$ is 45 degrees, $CH=AC/\sqrt2$; hence $HM=CH-CM=5\sqrt6/2$. The angle between $AH$ and $AD$ is 30 degrees: $AH$ makes 45 degrees with $AC$, while the bisector makes 15 degrees. The horizontal projection of $AP$ is therefore $AP/2=HN=HM/2$. Thus $AP=HM=5\sqrt6/2$, so $AP^2=75/2$ and the answer is 77.

**Answer:** 077.

**Methods:** angle bisectors, orthogonal projection, midpoint geometry.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five sources inspected. Several synthetic constructions are much longer; the shared short relation AP=HM follows directly from a 30-degree projection. One alternative misprints cos 60 where cos 30 is intended.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Midpoint projections on an angle bisector; angle bisectors, orthogonal projection, midpoint geometry supply the essential reduction.

## 2015 AIME I Problem 4: Midpoints between adjacent equilateral triangles

Collinear points $A,B,C$ occur in that order, with $AB=16$ and $BC=4$. Equilateral triangles $ABD$ and $BCE$ lie on the same side of the line. Let $M,N$ be the midpoints of $AE,CD$. If $[BMN]=x$, find $x^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

Use $B=(0,0)$, $A=(-16,0)$, $C=(4,0)$, $D=(-8,8\sqrt3)$, and $E=(2,2\sqrt3)$. Then $M=(-7,\sqrt3)$ and $N=(-2,4\sqrt3)$. Their determinant has magnitude $26\sqrt3$, so $[BMN]=13\sqrt3$ and $x^2=507$.

**Answer:** 507.

**Methods:** coordinates, midpoint vectors, determinant area.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. Coordinates give a short direct area calculation; the rotation approach additionally observes that BMN is equilateral.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Midpoints between adjacent equilateral triangles; coordinates, midpoint vectors, determinant area supply the essential reduction.

## 2015 AIME I Problem 6: Two equal-step arcs sharing endpoints

On one circle, $A,B,C,D,E$ occur at equal steps along a minor arc. On a circle centered at $C$, points $E,F,G,H,I,A$ occur at equal steps along a minor arc. If $\angle ABD-\angle AHG=12^\circ$, find $\angle BAG$ in degrees.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

Let the successive arc steps be $x,y$ degrees. The angle $ECA$ is $180-2x$ as an inscribed angle of the first circle and $5y$ as a central angle of the second. Also $\angle ABD=180-3x/2$ and $\angle AHG=180-3y/2$. Hence $2x+5y=180$ and $y-x=8$, giving $x=20,y=28$. Finally $\angle BAG=\angle BAE+\angle EAG=3x/2+y=58^\circ$.

**Answer:** 058.

**Methods:** inscribed angles, central angles, linear systems.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. The two angular step sizes reduce the configuration to two linear equations. The third alternative has a mislabeled intercepted arc; the equations here specify each angle.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Two equal-step arcs sharing endpoints; inscribed angles, central angles, linear systems supply the essential reduction.

## 2015 AIME I Problem 7: Two nested squares in a square

In square $ABCD$, let $E$ be the midpoint of $AD$. A square $FGHJ$ has $F,G$ on $CE$, $H$ on $AB$, and $J$ on $BC$. A square $KLMN$ has $K,L$ on $GH$, $M$ on $AD$, and $N$ on $AB$. If its area is 99, find the area of $FGHJ$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

Let the two inner side lengths be $x$ and $y$. Since $CE$ has perpendicular projections in ratio $2:1$, all the relevant right triangles have side ratio $1:2:\sqrt5$. Resolving the sides of $FGHJ$ along the outer square gives $BC=BJ+JC=x/\sqrt5+\sqrt5x/2=7\sqrt5x/10$. Similarly, along $AB$, the nested square gives $AN+NH= y/\sqrt5+\sqrt5y/2$, and $HB=2x/\sqrt5$. Equating $AB$ and $BC$ yields $7y=3x$. Thus $x^2=(49/9)y^2=(49/9)99=539$.

**Answer:** 539.

**Methods:** similar right triangles, nested squares, length ratios.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. The two rigorous alternatives use the same 1:2 right-triangle structure; the final alternative explicitly estimates a drawing with a ruler and is not a proof.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Two nested squares in a square; similar right triangles, nested squares, length ratios supply the essential reduction.

## 2015 AIME I Problem 11: Integral isosceles triangles with a fixed incenter distance

An isosceles triangle has $AB=AC$, positive integer side lengths, and incenter $I$ satisfying $BI=8$. Find its minimum perimeter.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Write $AB=AC=a$ and $BC=b$. If $\theta=\angle IBC$, the projection of $BI$ onto $BC$ gives $\cos\theta=b/16$, while $\cos2\theta=b/(2a)$. The double-angle identity therefore gives $a=64b/(b^2-128)$. Positivity requires $b^2>128$, and the triangle inequality $2a>b$ gives $b^2<256$. Thus $b=12,13,14,15$. The corresponding $a$ values are $48,832/41,224/17,960/97$; only 48 is integral. The unique possible perimeter, and hence the minimum, is $2(48)+12=108$.

**Answer:** 108.

**Methods:** incenter projection, double angles, integer bounds.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. They derive equivalent rational formulas by half-angle identities, bisector lengths, or tangency. The four-case integer check establishes uniqueness as well as minimality.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory. Integral isosceles triangles with a fixed incenter distance; incenter projection, double angles, integer bounds supply the essential reduction.

## 2015 AIME I Problem 15: The area of an oblique cylinder section

A solid cylinder has radius 6 and height 8. A plane passes through its center and two points on one rim whose smaller arc measures 120 degrees. The plane section has area $a\pi+b\sqrt c$, with positive integers $a,b$ and squarefree $c$. Find $a+b+c$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Center the cylinder at the origin with axis along $z$. Rotate coordinates so that the plane is $z=4x/3$: the rim chord is distance $6\cos60^\circ=3$ from the axis. Its horizontal projection is the portion of $x^2+y^2\le36$ with $|x|\le3$, and the area stretch is $\sqrt{1+(4/3)^2}=5/3$. Each removed circular cap has area $12\pi-9\sqrt3$, so the projected area is $36\pi-2(12\pi-9\sqrt3)=12\pi+18\sqrt3$. The section area is $20\pi+30\sqrt3$, giving 53.

**Answer:** 053.

**Methods:** orthogonal projection, area scaling, circular segments.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. One uses a direct affine stretch, one justifies it by narrow strips, and one integrates the same section. The projection method avoids calculus.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The area of an oblique cylinder section; orthogonal projection, area scaling, circular segments supply the essential reduction.

## 2015 AIME II Problem 4: Logarithmic lengths form a familiar triangle

An isosceles trapezoid has bases $\log3,\log192$ and altitude $\log16$, with a common logarithm base greater than 1. Its perimeter is $\log(2^p3^q)$. Find $p+q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

Put $L=\log2$. Half the base difference is $\tfrac12\log64=3L$, and the altitude is $4L$. Each leg is therefore $5L$. The perimeter is $\log3+\log192+10L=16\log2+2\log3=\log(2^{16}3^2)$. The answer is 18.

**Answer:** 018.

**Methods:** logarithm laws, isosceles trapezoids, Pythagorean triples.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. Each reduces to a 3-4-5 triangle; one changes the logarithm base without explaining that this uniformly rescales all lengths.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Logarithmic lengths form a familiar triangle; logarithm laws, isosceles trapezoids, Pythagorean triples supply the essential reduction.

## 2015 AIME II Problem 5: Adjacent cells in a random pair

Two different cells are chosen uniformly from an $n$ by $n$ square grid. Find the least $n$ for which their probability of sharing an edge is below $1/2015$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

The grid has $2n(n-1)$ adjacent unordered pairs. Thus the probability is $2n(n-1)/\binom{n^2}2=4/[n(n+1)]$. We require $n(n+1)>8060$. Since $89\cdot90=8010$ and $90\cdot91=8190$, the least $n$ is $90$.

**Answer:** 090.

**Methods:** double counting, probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Adjacent cells in a random pair; the proof uses double counting, probability.

## 2015 AIME II Problem 7: The area polynomial of an inscribed rectangle

Triangle $ABC$ has $AB=12$, $BC=25$, $CA=17$. A rectangle has two adjacent vertices $P,Q$ on $AB,AC$ and its opposite side on $BC$. If $PQ=\omega$ and its area is $\alpha\omega-\beta\omega^2$, write $\beta=m/n$ in lowest terms and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

Heron gives triangle area $\sqrt{27\cdot15\cdot2\cdot10}=90$, hence altitude $h=2(90)/25=36/5$. Similar triangles show that the rectangle height is $h(1-\omega/25)$. Its area is therefore $(36/5)\omega-(36/125)\omega^2$. Thus $\beta=36/125$ and the answer is 161.

**Answer:** 161.

**Methods:** similarity, Heron formula, quadratic area law.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six alternatives inspected. They obtain the same height-width relation through similarity, a parallelogram, or special widths. Direct similarity works for every admissible width.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The area polynomial of an inscribed rectangle; similarity, Heron formula, quadratic area law supply the essential reduction.

## 2015 AIME II Problem 9: A cube corner enters a circular opening

A water-filled cylinder has radius 4 and height 10. A cube of side 8 is lowered with a body diagonal on the cylinder axis until it first meets the rim. If the displaced water volume is $v$, find $v^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

The rim cuts the three edges at the lowest cube vertex equally, forming an equilateral triangle inscribed in a radius 4 circle. Its side is $4\sqrt3$, so the three mutually perpendicular edge segments have length $(4\sqrt3)/\sqrt2=2\sqrt6$. The submerged tetrahedron has volume $(2\sqrt6)^3/6=8\sqrt6$, giving $v^2=384$. The edge segments are shorter than 8, and the penetration depth is $(2\sqrt6)/\sqrt3=2\sqrt2<10$, confirming that neither another cube vertex nor the cylinder floor interferes.

**Answer:** 384.

**Methods:** trihedral tetrahedra, equilateral cross-sections, volume.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. They use right-tetrahedron volume, a perpendicular altitude, or De Gua. The size checks explain why the corner-section model is valid for the specified cube and cylinder.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A cube corner enters a circular opening; trihedral tetrahedra, equilateral cross-sections, volume supply the essential reduction.

## 2015 AIME II Problem 11: A line through the circumcenter perpendicular to a radius

An acute triangle has $AB=5$, $BC=4$, and circumcenter $O$. The line through $O$ perpendicular to $OB$ meets lines $AB,BC$ at $P,Q$, with $BQ=9/2$. If $BP=m/n$ in lowest terms, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Let the circumradius be $R$ and let $N$ be the midpoint of chord $BA$. The right triangles $BNO$ and $BOP$ are similar, so $BN\cdot BP=R^2$, or $BA\cdot BP=2R^2$. Applying the same argument to chord $BC$ gives $BC\cdot BQ=2R^2$. Hence $BP=BC\cdot BQ/BA=4(9/2)/5=18/5$, and the answer is 23.

**Answer:** 023.

**Methods:** circumcenter perpendicular bisectors, right-triangle similarity.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six alternatives inspected. Similarity, a cyclic-quadrilateral power argument, and reflection give the same product identity. A long trigonometric alternative uses an unsupported sign selection; the invariant product avoids it.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A line through the circumcenter perpendicular to a radius; circumcenter perpendicular bisectors, right-triangle similarity supply the essential reduction.

## 2015 AIME II Problem 15: Equal areas cut from two tangent circles

Two externally tangent circles have radii 1 and 4 and meet at $A$. A common external tangent touches them at $B,C$. A line through $A$ meets the circles again at $D,E$, respectively. If $B,C$ lie on the same side of the line and $[DBA]=[ACE]=m/n$ in lowest terms, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2015_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Place the centers at $(-1,0)$ and $(4,0)$, with $A=(0,0)$. A common tangent has contacts $B=(-8/5,-4/5)$ and $C=(8/5,-16/5)$, as follows by using a unit normal with horizontal component $-3/5$. The homothety of ratio $-4$ centered at $A$ gives $AE=4AD$. Thus equal areas require the distance from $B$ to the line to be four times that from $C$. Write its equation $ux+vy=0$. Since $B,C$ are on the same side, their signed values satisfy $uB_x+vB_y=4(uC_x+vC_y)$, giving $-40u+60v=0$. Hence the line is $3x+2y=0$. Its second intersection with $(x+1)^2+y^2=1$ is $D=(-8/13,12/13)$, so $AD=4/\sqrt{13}$. The distance from $B$ to this line is $32/(5\sqrt{13})$. The common area is $\tfrac12(4/\sqrt{13})(32/(5\sqrt{13}))=64/65$, giving 129.

**Answer:** 129.

**Methods:** homothety, signed distances, circle equations.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eleven alternatives inspected. Homothety makes the equal-area condition a linear signed-distance equation. The coordinate and tangent-secant methods are efficient; several longer angle-chasing alternatives contain reversed homothety ratios or mislabeled lengths, so every sign and coordinate is derived explicitly here.

**Archived entries inspected:** 11 of 11. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Equal areas cut from two tangent circles; homothety, signed distances, circle equations supply the essential reduction.

## 2016 AIME I Problem 3: Downward simple paths on an icosahedron

Orient an icosahedron with top and bottom vertices and two horizontal pentagons. Count vertex-simple edge paths from top to bottom that never move upward.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

Choose the first upper vertex in $5$ ways. A simple path on a pentagon from a fixed start has $1+2\cdot4=9$ possibilities: stay, or move $1$ through $4$ steps in either direction. From the last upper vertex choose one of two descending edges. The lower pentagon again offers $9$ paths, followed by its edge to the bottom. Total $5\cdot9\cdot2\cdot9=810$.

**Answer:** 810.

**Methods:** product rule, graph paths.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Downward simple paths on an icosahedron; the proof uses product rule, graph paths.

## 2016 AIME I Problem 4: A dihedral angle in a hexagonal prism

A right prism has regular hexagonal bases of side 12 and height $h$. A tetrahedron consists of a vertex $A$ and its three adjacent prism vertices. Its face in the base and its face opposite $A$ meet at a 60-degree dihedral angle. Find $h^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

Let $B,C$ be the two base neighbors of $A$ and $D$ the vertex directly above it. If $M$ is the midpoint of $BC$, then $AM=12\cos60^\circ=6$. Both $AM$ and $DM$ are perpendicular to $BC$, so the dihedral angle is $\angle AMD=60^\circ$. In right triangle $AMD$, $h=AD=6\tan60^\circ=6\sqrt3$. Thus $h^2=108$.

**Answer:** 108.

**Methods:** dihedral cross-sections, regular hexagons, right triangles.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. The second labels BC as a variable slant edge incorrectly, but its final midpoint equation is valid. The perpendicular cross-section gives the result directly.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A dihedral angle in a hexagonal prism; dihedral cross-sections, regular hexagons, right triangles supply the essential reduction.

## 2016 AIME I Problem 6: The arc midpoint and the incenter

The internal angle bisector from $C$ in triangle $ABC$ meets $AB$ at $L$ and the circumcircle again at $D$. The incenter is $I$, with $LI=2$ and $LD=3$. Write $CI=p/q$ in lowest terms and find $p+q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

The order is $C,I,L,D$. Inscribed angles give $\angle DAB=\angle DCB=\angle DCA$. Also $\angle DAI=\angle DAB+\angle BAI=\angle ICA+\angle IAC=\angle DIA$, so $DA=DI=5$. Triangles $DAL$ and $DCA$ share their angle at $D$ and have $\angle DAL=\angle DCA$; hence $DA^2=DL\cdot DC$. Therefore $DC=25/3$ and $CI=DC-DI=10/3$, giving 13.

**Answer:** 013.

**Methods:** arc midpoint lemma, incenter angles, similar triangles.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All twelve stored entries inspected, including one author-only entry. Several alternatives assume the triangle is isosceles without justification; another mislabels the excenter. The angle proof works for every triangle and needs neither assumption.

**Archived entries inspected:** 12 of 12. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The arc midpoint and the incenter; arc midpoint lemma, incenter angles, similar triangles supply the essential reduction.

## 2016 AIME I Problem 9: A rectangle optimization with a segment inconsistency

Triangle $ABC$ has $AB=40$, $AC=31$, and $\sin A=1/5$. It lies in rectangle $AQRS$ with $B$ on segment $QR$ and $C$ on segment $RS$. Determine the maximum rectangle area. The reported contest answer is 744; the segment conditions require the correction below.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

Place $A=(0,0)$, $B=40(\cos\theta,\sin\theta)$, and $C=31(\cos(\theta+A),\sin(\theta+A))$, with $Q=(B_x,0)$ and $S=(0,C_y)$. Necessarily $A$ is acute, so $\cos A=2\sqrt6/5$. The area is $620[\sin(2\theta+A)+1/5]$, whose unrestricted maximum 744 occurs at $\theta_*=(\pi/2-A)/2$. But there $B_y\le C_y$ would require $\tan\theta_*\le31/40$, whereas $\tan\theta_*=\sqrt6/3>31/40$. Thus 744 is unattainable for the literal statement. The segment constraint instead gives $\tan\theta\le t=31/(200-62\sqrt6)<\tan\theta_*$. The area increases throughout this allowed interval, so the true maximum occurs at $B=R$, namely $1600t/(1+t^2)=248(1600-496\sqrt6)/(2561-992\sqrt6)$. At this boundary $C_x<B_x$, so the second segment condition holds. The reported answer 744 solves the relaxed problem permitting B on the line containing QR.

**Reported answer:** 744.

**Methods:** trigonometric optimization, feasibility of equality, segment constraints.

**Verification:** The equality configuration fails the explicit segment inequality; the exact boundary maximizer is derived and meets both segment constraints.

**Source comparison:** All five stored alternatives inspected. The final entry explicitly warns that 744 violates the side condition. The licensed LIVE archive independently confirms the same lengths and segment wording, but also incorrectly asserts the equality configuration is allowed.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Source correction:** **Type:** literal_statement_inconsistency **Reported answer:** 744 **Literal maximum:** $\dfrac{248(1600-496\sqrt6)}{2561-992\sqrt6}$ **Verified statement url:** [Verified source](https://live.poshenloh.com/past-contests/aime/2016I) **Note:** The licensed archive retains the segment condition and the reported answer744. The proof distinguishes the literal feasible maximum from the relaxed intended calculation.

**Subject classification:** geometry, algebra. A rectangle optimization with a segment inconsistency; trigonometric optimization, feasibility of equality, segment constraints supply the essential reduction.

## 2016 AIME I Problem 14: Lattice shapes intersected by a rational line

At every lattice point place a radius $1/10$ circle and an axis-parallel side $1/5$ square. Count the total shapes meeting the segment from $(0,0)$ to $(1001,429)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

The line is $3x-7y=0$. A centered circle meets it only when $|3x-7y|/\sqrt{58}\le 1/10$, forcing the integer numerator to $0$. There are $144$ such centers, $(7k,3k),0\le k\le 143$. A square meets the line exactly when $|3x-7y|\le 1$, because its half-width changes this linear form by at most $1$. Besides $144$ on-line centers, each of the $143$ fundamental strips has one center of each offset $\pm 1$. Endpoints create no extra centers. Thus there are $144$ circles and $430$ squares, for a total of $574$.

**Answer:** 574.

**Methods:** lattice counting, periodicity.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Lattice shapes intersected by a rational line; the proof uses lattice counting, periodicity.

## 2016 AIME I Problem 15: A tangent configuration gives a difference of squares

Circles meet at $X,Y$ and share an external tangent touching them at $A,B$, closer to $X$ than $Y$. A circle through $A,B$ meets the first again at $D$ and the second again at $C$, where $D,Y,C$ are collinear. Given $XD=37$, $XY=47$, $XC=67$, find $AB^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Let $F=AD\cap BC$. The radical-axis theorem puts $F$ on $XY$. Applying the elementary Miquel theorem to triangle $FDC$, with points $A,B,Y$ on its side lines, shows $F,A,X,B$ are cyclic. Let $Z=XY\cap AB$. Equal tangent powers give $ZA^2=ZX\cdot ZY=ZB^2$, so $Z$ is the midpoint of $AB$. Power in circle $FAXB$ then places $F$ opposite $X$ across $Z$ and gives $ZF=ZY$. As $X$ is closer to the tangent, the order is $F,Z,X,Y$. Moreover, directed-angle identities $\angle XFC=\angle XFB=\angle XAB=\angle XDA=\angle XDF$ and $\angle XCF=\angle XCB=\angle XBA=\angle XFA=\angle XFD$ show $\triangle DXF\sim\triangle FXC$. Thus $FX^2=XD\cdot XC=37\cdot67$. Put $u=ZX$; then $ZY=u+47$ and $FX=2u+47$. Finally $AB^2=4ZA^2=4u(u+47)=FX^2-47^2=37\cdot67-47^2=270$.

**Answer:** 270.

**Methods:** radical axes, Miquel theorem, tangent power, directed-angle similarity.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eight alternatives inspected. Miquel plus radical axes exposes the midpoint relation and the difference-of-squares invariant. Longer Stewart and linear-power proofs reach the same identity; one source is only an unannotated formula fragment.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A tangent configuration gives a difference of squares; radical axes, Miquel theorem, tangent power, directed-angle similarity supply the essential reduction.

## 2016 AIME II Problem 5: An infinite chain of right-triangle altitudes

Right triangle $ABC_0$ has pairwise coprime positive integer sides and perimeter $p$. Let $C_1$ be the foot from $C_0$ to $AB$; for $n\ge2$, let $C_n$ be the foot from $C_{n-1}$ to $C_{n-2}B$. If $C_0C_1+C_1C_2+\cdots=6p$, find $p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

Put $a=BC_0$, $b=AC_0$, $c=AB$. The first altitude is $ab/c$, and successive similar right triangles multiply it by $a/c$. Thus the total is $ab/(c-a)=6(a+b+c)$. Using $c^2=a^2+b^2$ to simplify gives $7a=6(b+c)$. Hence $6b=7a-6c$; squaring and substituting for $b^2$ yields $85a^2=84ac$, so $a/c=84/85$. Coprimality forces $a=84,c=85$, and then $b=13$. Therefore $p=182$.

**Answer:** 182.

**Methods:** similarity chains, geometric series, primitive Pythagorean triples.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six alternatives inspected. The geometric-series derivation is reliable; several finish by guessing a triple or choose the wrong parity orientation in Euclid’s parametrization. Eliminating with the Pythagorean identity proves the unique primitive ratio.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra, number_theory. An infinite chain of right-triangle altitudes; similarity chains, geometric series, primitive Pythagorean triples supply the essential reduction.

## 2016 AIME II Problem 7: Three nested squares with two integer areas

Two concentric squares have parallel sides. The outer area is 2016 and the inner area is a smaller positive integer. A third square has one vertex on each outer side, while each inner vertex lies on one of its sides. Find the difference between the greatest and least possible positive integer areas of this third square.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

If the third square is rotated through $\theta\in[0,\pi/4]$, its side length is the outer side divided by $\cos\theta+\sin\theta$. The inner side is divided by the same factor again. Consequently, if the middle and inner areas are $M,N$, then $M^2=2016N$ and $1008\le M<2016$. Since $2016=2^5\cdot3^2\cdot7$, integrality of $N$ requires $168\mid M$. Thus the least and greatest possibilities are 1008 and 1848; their inner areas are 504 and 1694, both integers. The continuous rotation realizes both, and the difference is 840.

**Answer:** 840.

**Methods:** nested-square similarity, square divisibility, integer extrema.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** The single source states the area geometric progression and the extrema. The explicit divisibility condition supplies a complete proof that no larger integer middle area is possible.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory. Three nested squares with two integer areas; nested-square similarity, square divisibility, integer extrema supply the essential reduction.

## 2016 AIME II Problem 10: A chord length from a ratio of subtriangle areas

In triangle $ABC$ on a circle, points $P,Q$ lie on $AB$ in the order $A,P,Q,B$, with $AP=4$, $PQ=3$, $QB=6$. Rays $CP,CQ$ meet the circle again at $S,T$. If $AS=7$ and $BT=5$, write $ST=m/n$ in lowest terms and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

Let $\alpha=\angle ACP$ and $\beta=\angle PCQ$. Triangles $ACQ$ and $BTQ$ are similar by their vertical angles at $Q$ and equal inscribed angles, so $AC/CQ=BT/BQ=5/6$. The triangles $ACP,PCQ$ have bases 4,3 on the same line; comparing their sine-area formulas gives $4/3=(AC/CQ)(\sin\alpha/\sin\beta)$. Hence $\sin\alpha/\sin\beta=8/5$. The chord formula on the common circle gives $AS/ST=\sin\alpha/\sin\beta$, so $ST=7(5/8)=35/8$, and the answer is 43.

**Answer:** 043.

**Methods:** sine area ratios, inscribed angles, chord ratios.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six alternatives inspected. Cross-ratio invariance and Ptolemy are valid alternatives, but one similarity and one area ratio already determine the desired chord.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A chord length from a ratio of subtriangle areas; sine area ratios, inscribed angles, chord ratios supply the essential reduction.

## 2016 AIME II Problem 14: A common sphere through a triangular bipyramid

An equilateral triangle $ABC$ has side 600. Points $P,Q$ on opposite sides of its plane are each equidistant from $A,B,C$. The face half-planes $PAB,QAB$ form a 120-degree dihedral angle. A point $O$ is distance $d$ from all five vertices. Find $d$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2016_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

Let $K$ be the triangle center and $M$ the midpoint of $AB$. Then $KM=100\sqrt3$ and $KA=200\sqrt3$. The points $P,Q,O$ lie on the perpendicular axis through $K$; since $OP=OQ$, $O$ is the midpoint of $PQ$. Write $KP=x,KQ=y>0$. Equality $OA=OP$ gives $((x-y)/2)^2+120000=((x+y)/2)^2$, so $xy=120000$. The perpendicular cross-section through $M,K$ has $\angle PMQ=120^\circ$. Applying tangent addition yields $((x+y)/(100\sqrt3))/(1-xy/30000)=-\sqrt3$, hence $x+y=900$. Therefore $d=PQ/2=450$. Positive heights exist because the quadratic with sum 900 and product 120000 has two positive roots.

**Answer:** 450.

**Methods:** sphere-axis reduction, dihedral cross-sections, tangent addition.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eight alternatives inspected. The common-sphere condition fixes the product of the heights; the dihedral angle fixes their sum. Several longer coordinate proofs introduce unnecessary radicals or contain mislabeled angles, while this pair of invariants avoids them.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A common sphere through a triangular bipyramid; sphere-axis reduction, dihedral cross-sections, tangent addition supply the essential reduction.

## 2017 AIME I Problem 1: Triangles from boundary points

A triangle has $3$ additional points on one side, $4$ on another, and $5$ on the third. Count nondegenerate triangles whose vertices are among all $15$ marked points.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

Choose any three points and remove collinear triples. A line not equal to a side meets the triangle boundary at at most two points, so only side triples are degenerate. The count is $\binom{15}3-\binom53-\binom63-\binom73=455-10-20-35=390$.

**Answer:** 390.

**Methods:** complementary counting, geometry counting.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Triangles from boundary points; the proof uses complementary counting, geometry counting.

## 2017 AIME I Problem 4: Equal lateral edges above an isosceles base

A tetrahedron has base side lengths 20,20,24 and all three remaining edges of length 25. Its volume is $m\sqrt n$ with squarefree positive integer $n$. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

The base altitude is $\sqrt{20^2-12^2}=16$, so its area is 192. Its circumradius is $R=(20\cdot20\cdot24)/(4\cdot192)=25/2$. The apex projects to the circumcenter because its distances to the three vertices agree. Hence its height is $\sqrt{25^2-(25/2)^2}=25\sqrt3/2$. The volume is $(1/3)192(25\sqrt3/2)=800\sqrt3$, giving 803.

**Answer:** 803.

**Methods:** circumradius from area, equidistant apex, tetrahedron volume.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. Circumradius immediately determines the height. Some longer displayed volume computations omit a factor 1/3 or mis-evaluate a radical, despite reporting the correct final result.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Equal lateral edges above an isosceles base; circumradius from area, equidistant apex, tetrahedron volume supply the essential reduction.

## 2017 AIME I Problem 6: A chord intersecting an isosceles triangle

An inscribed isosceles triangle has equal angles $x$ degrees. A chord with two independent uniform endpoints intersects the triangle with probability $14/25$. Find the difference between possible $x$ values.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

The complementary event has both endpoints on the same one of the three complementary arcs. Their normalized lengths are $x/180, x/180,1-2x/180$. Thus $2(x/180)^2+(1-2x/180)^2=11/25$. This yields $x^2-120x+3024=0$, with roots $36$ and $84$. Difference $48$.

**Answer:** 048.

**Methods:** geometric probability, complementary counting.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. A chord intersecting an isosceles triangle; the proof uses geometric probability, complementary counting.

## 2017 AIME I Problem 8: Two random right-triangle vertices

On the same semicircle of diameter $OP=200$, select $Q, R$ so that angles $POQ$ and $POR$ are independently uniform between $0$ and $75$ degrees. Find numerator plus denominator of $P(QR\le 100)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

The central angle between $Q, R$ is $2|a-b|$, so $QR=200\sin|a-b|$. The condition is $|a-b|\le 30$. In the $75$ by $75$ parameter square, the excluded triangles have combined area $45^2$. Thus the probability is $1-45^2/75^2=16/25$; answer $41$.

**Answer:** 041.

**Methods:** geometric probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Two random right-triangle vertices; the proof uses geometric probability.

## 2017 AIME I Problem 10: A real cross ratio traces a circle

Let $z_1=18+83i$, $z_2=18+39i$, and $z_3=78+99i$. Among complex $z\ne z_3$ making $\frac{z_3-z_1}{z_2-z_1}\frac{z-z_2}{z-z_3}$ real, take the one with greatest imaginary part. Find its real part.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

A real cross ratio means the directed angles subtending the fixed endpoints $z_2,z_3$ agree modulo $\pi$; thus the locus is their circle through $z_1$, with $z_3$ removed. Its center lies on the perpendicular bisector $y=61$ of $z_1z_2$ and on the perpendicular bisector $y=-x+117$ of $z_2z_3$. Therefore the center is $(56,61)$. The topmost point has real part 56 and is not the excluded point $z_3$, so the answer is 56.

**Answer:** 056.

**Methods:** real cross ratios, cyclic loci, perpendicular bisectors.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eight stored entries inspected; the first four are connected pieces of one geometric discussion. Some assert angle equality without its moduloπ qualification, and one informally includes the undefined point z 3. The circle-locus formulation handles both issues.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. A real cross ratio traces a circle; real cross ratios, cyclic loci, perpendicular bisectors supply the essential reduction.

## 2017 AIME I Problem 15: The smallest equilateral triangle between three sides

A right triangle has legs 5 and $2\sqrt3$. An equilateral triangle has one vertex on each side. Its least possible area is $m\sqrt p/n$, where $m/n$ is reduced and $p$ squarefree. Find $m+n+p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Place the outer vertices at $(0,0),(5,0),(0,2\sqrt3)$. Let two inner vertices be $(a,0),(0,b)$. The third, inside the first quadrant, is $((a+\sqrt3b)/2,(\sqrt3a+b)/2)$. Requiring it on the hypotenuse gives $7\sqrt3a+11b=20\sqrt3$. By Cauchy–Schwarz, $1200\le(147+121)(a^2+b^2)$, so the squared inner side is at least $300/67$. Equality holds at $a=105/67$, $b=55\sqrt3/67$; both lie on the required legs, and the third vertex $(135/67,80\sqrt3/67)$ lies on the hypotenuse. Thus the minimum area is $75\sqrt3/67$, giving 145.

**Answer:** 145.

**Methods:** rotation coordinates, linear constraints, Cauchy-Schwarz equality.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All thirteen alternatives inspected. Coordinate rotation and a point-to-line distance give the shortest proof. Many sources omit the equality placement or mislabel side length versus its square; the explicit feasible coordinates establish attainment.

**Archived entries inspected:** 13 of 13. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The smallest equilateral triangle between three sides; rotation coordinates, linear constraints, Cauchy-Schwarz equality supply the essential reduction.

## 2017 AIME II Problem 3: Voronoi region inside a triangle

A point is uniform in the triangle with vertices $(0,0),(12,0),(8,10)$. Find numerator plus denominator of its probability of being closest to $(12,0)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

The relevant perpendicular bisectors are $x=6$ and $y=2x/5+1$. Their intersection is $(6,17/5)$. The favorable region has vertices $(6,0),(12,0),(10,5),(6,17/5)$, with area $109/5$ by the shoelace formula. The whole area is $60$, giving probability $109/300$ and answer $409$.

**Answer:** 409.

**Methods:** geometric probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Voronoi region inside a triangle; the proof uses geometric probability.

## 2017 AIME II Problem 10: An area bisector in a cut rectangle

Rectangle $ABCD$ has $AB=84$, $AD=42$. Let $M$ be the midpoint of $AD$, $N$ the point on $AB$ with $AN=28$, and $O=CM\cap DN$. A point $P$ on the boundary of $BCON$ makes segment $BP$ bisect its area. Find $[CDP]$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

Use $D=(0,0)$, $A=(0,42)$, $B=(84,42)$, $C=(84,0)$. Then $CM$ is $y=21-x/4$ and $DN$ is $y=3x/2$, giving $O=(12,18)$. The quadrilateral area is $84\cdot42-[AND]-[DOC]=3528-588-756=2184$. Since $[BCO]=1512>1092$, the bisecting endpoint lies on $CO$. Thus $[BCP]=1092$, so $42(84-P_x)/2=1092$ and $P_x=32$. On $CO$, $P_y=21-32/4=13$. Therefore $[CDP]=84\cdot13/2=546$.

**Answer:** 546.

**Methods:** coordinate intersections, area subtraction, area bisectors.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. The area comparison explicitly locates P on CO before the base-height calculation; this location is merely asserted in the sources.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. An area bisector in a cut rectangle; coordinate intersections, area subtraction, area bisectors supply the essential reduction.

## 2017 AIME II Problem 12: The limit point of rotating nested circles

Starting with a unit circle centered at $O$, choose $A_0$ on it. For $n\ge1$, a circle of radius $r^n$ is internally tangent to the preceding circle at $A_{n-1}$, and $A_n$ is 90 degrees counterclockwise from that tangency point on the new circle. For $r=11/60$, write the distance from $O$ to the common limit point as $m/n$ and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Use complex coordinates with $O=0,A_0=1$. The successive center displacements are $(1-r),(1-r)ri,(1-r)(ri)^2,\ldots$, because each construction rotates the contact radius 90 degrees and scales it by r. Their sum is $B=(1-r)/(1-ri)$. The nested radii tend to zero, so this is their unique common point; indeed its distance from the nth center is $r^n|B|<r^n$. Hence $OB=(1-r)/\sqrt{1+r^2}=(49/60)/(61/60)=49/61$. The answer is 110.

**Answer:** 110.

**Methods:** complex geometric series, nested circles, contraction limits.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. Center displacements give the complex series directly and prove uniqueness of the common point. One invariant-based alternative has an inverted squared-distance formula; the last coordinate alternative prints 538 where the imaginary numerator should be 539.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The limit point of rotating nested circles; complex geometric series, nested circles, contraction limits supply the essential reduction.

## 2017 AIME II Problem 13: Isosceles triangles in regular polygons

Let $f(n)$ count isosceles vertex triangles of a regular $n$-gon, including equilateral ones. Find the sum of $n\ge 3$ satisfying $f(n+1)-f(n)=78$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Choose the apex and equally distant vertices, then correct equilateral overcounting: $f(n)=n\lfloor(n-1)/2\rfloor-(2n/3)[3\mid n]$. For residues $n\equiv0,1,2,3,4,5 \pmod{6}$, the differences are respectively $13n/6, (n-1)/2, (5n-4)/6, (7n-3)/6,3n/2,(-n-7)/6$. Solving and enforcing each residue leaves $n=36,157,52$. Their sum is $245$.

**Answer:** 245.

**Methods:** geometry counting, periodic cases.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Isosceles triangles in regular polygons; the proof uses geometry counting, periodic cases.

## 2017 AIME II Problem 14: Lines containing exactly eight lattice points

In $\{1,\ldots,10\}^3$ count lines containing exactly $8$ grid points.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

A primitive direction has coordinate steps in $\{0,\pm 1\}$; any larger coordinate step permits at most $5$ points. Axis-parallel lines have $10$ points. For two nonzero coordinates there are $3\cdot2=6$ unoriented directions. Each has $2$ offsets of length $8$ in its coordinate square and $10$ choices of constant coordinate, giving $120$. For three nonzero coordinates there are $4$ unoriented directions. After reflecting to $(1,1,1)$, the initial point lies in $\{1,2,3\}^3$ with minimum $1$ and maximum $3:3^3-2\cdot2^3+1=12$ choices. Thus $120+4\cdot12=168$.

**Answer:** 168.

**Methods:** lattice lines, primitive directions.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The first archived solution uses the same mathematical reduction; this argument is independently written.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Lines containing exactly eight lattice points; the proof uses lattice lines, primitive directions.

## 2017 AIME II Problem 15: The geometric median of a disphenoid

A tetrahedron has opposite edge pairs $AD=BC=28$, $AC=BD=44$, and $AB=CD=52$. If the least possible value of $AX+BX+CX+DX$ over points $X$ in space is $m\sqrt n$ with squarefree $n$, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2017_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Realize the vertices as $A=(u,v,w)$, $B=(u,-v,-w)$, $C=(-u,v,-w)$, $D=(-u,-v,w)$. The edge equations give $u^2+v^2=196$, $u^2+w^2=484$, $v^2+w^2=676$, so $(u^2,v^2,w^2)=(2,194,482)$. This realizes the given tetrahedron and places all vertices at distance $R=\sqrt{678}$ from the origin, with vector sum zero. For any $X$ and vertex $V$, Cauchy–Schwarz gives $|X-V|\ge(V-X)\cdot V/R=R-X\cdot V/R$. Summing cancels the dot products, giving total distance at least $4R$, with equality at $X=0$. Thus the minimum is $4\sqrt{678}$; since $678=2\cdot3\cdot113$ is squarefree, the answer is 682.

**Answer:** 682.

**Methods:** disphenoid coordinates, supporting-plane inequality, geometric median.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. Symmetrization also proves the centroid minimizes the sum, but one source invokes central symmetry incorrectly: a tetrahedron is not centrally symmetric. The equal-radius and zero-vector-sum inequality proves the minimum globally.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The geometric median of a disphenoid; disphenoid coordinates, supporting-plane inequality, geometric median supply the essential reduction.

## 2018 AIME I Problem 4: An equal-sided chain inside an isosceles triangle

Triangle $ABC$ has $AB=AC=10$ and $BC=12$. Interior side points $D\in AB$, $E\in AC$ satisfy $AD=DE=EC$. Write $AD=p/q$ in lowest terms and find $p+q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_I_Problems/Problem_4) · MAA AMC.

### Solution

The cosine law gives $\cos A=(100+100-144)/200=7/25$. Put $AD=DE=EC=x$, so $AE=10-x>0$. Applying the cosine law in $ADE$ gives $x^2=x^2+(10-x)^2-2x(10-x)(7/25)$. Divide by $10-x$ to obtain $10-x=14x/25$, hence $x=250/39$. This lies strictly between 0 and 10 and satisfies the original equation, so the answer is 289.

**Answer:** 289.

**Methods:** cosine-law cancellation, isosceles subtriangles.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All thirteen alternatives inspected. Many introduce additional altitudes, coordinates, or angle chasing; the two cosine-law equations suffice. The interior-point condition justifies removing the otherwise extraneous solution x=10.

**Archived entries inspected:** 13 of 13. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. An equal-sided chain inside an isosceles triangle; cosine-law cancellation, isosceles subtriangles supply the essential reduction.

## 2018 AIME I Problem 7: Isosceles triangles in a hexagonal prism

A right regular hexagonal prism has base side $1$ and height $2$. Count isosceles triangles among its $12$ vertices.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_I_Problems/Problem_7) · MAA AMC.

### Solution

Each base has $6$ triangles of side pattern $(1,1,\sqrt3)$ and $2$ equilateral triangles, giving $16$. In a mixed triangle, choose its solitary vertex on one base in $12$ ways. From that vertex, two vertices on the other base can be symmetric one step or two steps away ($2$ choices), or they can be the directly opposite-base vertex and its diametrical partner ($1$ choice, because both the height and base diameter equal $2$). These exhaust equal-distance possibilities. Total $16+12\cdot3=52$.

**Answer:** 052.

**Methods:** geometry counting, distance classes.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All six sources inspected. Counting equal-distance neighbor pairs at each apex gives 60, then subtracting twice each of four equilateral triangles gives 52. Some alternative geometric casework is informal; index 2 calls the equilateral side length 1 although it is $\sqrt{3}$. The independent distance-multiplicity argument is complete.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Isosceles triangles in a hexagonal prism; the proof uses geometry counting, distance classes.

## 2018 AIME I Problem 8: The largest disk in an equiangular hexagon

A convex equiangular hexagon $ABCDEF$ has successive side lengths $AB=6$, $BC=8$, $CD=10$, $DE=12$. If the largest disk inside it has diameter $d$, find $d^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

Use successive edge directions $0,60,120,180,240,300$ degrees. Closure forces $EF=2,FA=16$, giving vertices $A=(0,0)$, $B=(6,0)$, $C=(10,4\sqrt3)$, $D=(5,9\sqrt3)$, $E=(-7,9\sqrt3)$, $F=(-8,8\sqrt3)$. The parallel sides $CD,FA$ lie on $\sqrt3x+y=14\sqrt3$ and 0, whose separation is $7\sqrt3$. Thus $d\le7\sqrt3$. A center at $(2,5\sqrt3)$ has inward distances to the six side lines, in order, $5\sqrt3,9\sqrt3/2,7\sqrt3/2,4\sqrt3,13\sqrt3/2,7\sqrt3/2$. Therefore the disk of radius $7\sqrt3/2$ lies in every supporting half-plane and hence inside the hexagon. The bound is attained, giving $d^2=147$.

**Answer:** 147.

**Methods:** equiangular polygon closure, parallel-strip bounds, feasible inscribed disk.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. They identify the limiting parallel sides but rely on a drawing to assert the disk clears the other four sides. The explicit center and six distances verify feasibility.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The largest disk in an equiangular hexagon; equiangular polygon closure, parallel-strip bounds, feasible inscribed disk supply the essential reduction.

## 2018 AIME I Problem 13: The area between two subtriangle incenters

Triangle $ABC$ has $AB=30$, $BC=32$, $AC=34$. For $X$ interior to $BC$, let $I_1,I_2$ be the incenters of $ABX,ACX$. Find the least possible area of $AI_1I_2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Put $\alpha=\angle AXB$, and use the outer triangle angles $A,B,C$. Since $\angle I_1AI_2=A/2$, the sine law in $ABI_1$ and $ACI_2$ gives $AI_1=30\sin(B/2)/\cos(\alpha/2)$ and $AI_2=34\sin(C/2)/\sin(\alpha/2)$. Hence $[AI_1I_2]=30\cdot34\sin(A/2)\sin(B/2)\sin(C/2)/\sin\alpha$. Its minimum occurs at $\alpha=90^\circ$; the perpendicular foot is indeed interior because its distance from B is $(30^2+32^2-34^2)/(64)=12$. With semiperimeter $s=48$, the half-angle formulas give the minimum $(s-32)(s-34)(s-30)/32=16\cdot14\cdot18/32=126$.

**Answer:** 126.

**Methods:** incenter angle formulas, sine-law optimization, half-angle products.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. The sine-law proof explicitly isolates the variable angle. One alternative assumes without proof that minimizing AX minimizes the target area; another develops the valid general identity area=r·AX/2 but drops a factor 1/2 in an intermediate displayed line.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The area between two subtriangle incenters; incenter angle formulas, sine-law optimization, half-angle products supply the essential reduction.

## 2018 AIME I Problem 15: Three cyclic side orders share an area invariant

Four distinct stick lengths form three noncongruent convex cyclic quadrilaterals, all of circumradius 1 and common area $K$. The sines of their acute diagonal angles are $2/3,3/5,6/7$. Write $K=m/n$ in lowest terms and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Label the side lengths $a,b,c,d$ in one cyclic order and put $U=ac+bd$, $V=ab+cd$, $W=ad+bc$. The three side orders give diagonal products $U,V,W$ by Ptolemy. If the corresponding diagonal-angle sines are $s_U,s_V,s_W$, then $2K=Us_U=Vs_V=Ws_W$. For the first quadrilateral let the diagonals be e,f. Splitting along them and using triangle area $abc/(4R)$ with $R=1$ gives $K=eV/4=fW/4$. Consequently $e=2s_V,f=2s_W$, and $K=ef s_U/2=2s_Us_Vs_W=2(2/3)(3/5)(6/7)=24/35$. Thus the answer is 59.

**Answer:** 059.

**Methods:** Ptolemy theorem, circumradius area formula, side-order invariants.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five stored entries inspected, including an author-only entry. The half-arc argument is short but needs supplementary-angle care because the specified diagonal angles are acute. The side-product proof uses only their sines and avoids that ambiguity.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Three cyclic side orders share an area invariant; Ptolemy theorem, circumradius area formula, side-order invariants supply the essential reduction.

## 2018 AIME II Problem 4: Six regions of a crossed octagon

An equiangular octagon has cyclic labels $C,A,R,O,L,I,N,E$, with alternating side lengths $\sqrt2,1$, starting at CA. Joining the same vertices in the order $C,O,R,N,E,L,I,A$ forms six disjoint triangular regions. If their total area is $a/b$ in lowest terms, find $a+b$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

Place $C=(0,2),A=(1,3),R=(2,3),O=(3,2),L=(3,1),I=(2,0),N=(1,0),E=(0,1)$. The crossing segments lie on $y=2$, $y=1$, $y=-3x+6$, and $y=3x-3$. The sloping lines meet at $(3/2,3/2)$, and their intersections with y=2 are $(4/3,2),(5/3,2)$; the lower intersections are their reflections across y=3/2. Four outer triangular regions have base $4/3$ and height 1, so area $2/3$ each. The two central regions each have base $1/3$ and height $1/2$, so area $1/12$. Total area is $4(2/3)+2(1/12)=17/6$, giving 23.

**Answer:** 023.

**Methods:** self-intersecting polygons, line intersections, triangle decomposition.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. Their diagram-dependent labels are replaced by explicit coordinates and all intersection lines, making the six-region decomposition self-contained.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Six regions of a crossed octagon; self-intersecting polygons, line intersections, triangle decomposition supply the essential reduction.

## 2018 AIME II Problem 7: Rational lengths among equal-area parallel slices

A triangle has sides $AB=9$, $AC=12$, $BC=5\sqrt3$. Lines parallel to BC divide it into 2450 equal-area regions. Let the kth parallel segment, including BC as the 2450 th, bound the first k regions nearest A. How many of these 2450 segments have rational length?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

The kth similar triangle has k/2450 of the total area, so its parallel side has length $5\sqrt3\sqrt{k/2450}=\sqrt{6k}/14$. A rational square root of an integer is an integer; thus the length is rational exactly when $6k$ is a square, equivalently $k=6t^2$ for a positive integer t. The bound $6t^2\le2450$ gives $1\le t\le20$. Therefore 20 segments have rational length.

**Answer:** 020.

**Methods:** similarity area ratios, squarefree kernels, rational square roots.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. The squarefree kernel 6 controls the rational indices. The problem includes the base segment; it is irrational and does not alter the count, but the inclusive indexing is retained.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory. Rational lengths among equal-area parallel slices; similarity area ratios, squarefree kernels, rational square roots supply the essential reduction.

## 2018 AIME II Problem 9: A fan of triangle centroids is a scaled midpoint polygon

An octagon has vertices $A=(0,6),B=(8,0),C=(19,0),D=(27,6),E=(27,17),F=(19,23),G=(8,23),H=(0,17)$. Let $J$ be the midpoint of AH. The segments from J to B through G form seven triangles. Find the area of the convex polygon formed by their centroids.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

For any consecutive vertices U,V in the chain A through H, the centroid of JUV equals $J+\tfrac23((U+V)/2-J)$. Thus the centroid polygon is the image, under a homothety of ratio 2/3 centered at J, of the seven edge midpoints. Those midpoints are $(4,3),(27/2,0),(23,3),(27,23/2),(23,20),(27/2,23),(4,20)$. The vertical cuts at $x=27/2$ and x=23 divide this polygon into two trapezoids of area $(17+23)(19/2)/2=190$ each and a triangle of area $17\cdot4/2=34$. Its area is 414; the required area is $(4/9)414=184$.

**Answer:** 184.

**Methods:** centroid homothety, midpoint polygons, area scaling.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. The midpoint homothety avoids seven separate centroid computations. The explicit octagon coordinates describe the original 23-by 27 rectangle with 6-8-10 corner triangles removed, without relying on its diagram.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A fan of triangle centroids is a scaled midpoint polygon; centroid homothety, midpoint polygons, area scaling supply the essential reduction.

## 2018 AIME II Problem 12: An area balance bisects one diagonal

A convex quadrilateral has $AB=CD=10$, $BC=14$, $AD=2\sqrt{65}$. Its diagonals meet at P, with $[APB]+[CPD]=[BPC]+[APD]$. Find its area.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Using the common sine of the diagonal angles, the area condition factors as $(AP-CP)(BP-DP)=0$. We may assume $AP=CP=u$: if instead BD is bisected, relabel $(A,B,C,D)$ as $(D,C,B,A)$, which preserves every stated side length and exchanges the diagonals. Set $BP=v,DP=w$, and $c=\cos\angle APB$. The cosine law gives $u^2+v^2=148$, $uvc=24$, $u^2+w^2=180$, and $uwc=40$. Hence $w/v=5/3$ and $w^2-v^2=32$, giving $v=3\sqrt2,w=5\sqrt2,u=\sqrt{130}$. Thus $c=4/\sqrt{65}$ and the diagonal-angle sine is $7/\sqrt{65}$. The area is $u(v+w)\sin\angle APB=\sqrt{130}(8\sqrt2)(7/\sqrt{65})=112$.

**Answer:** 112.

**Methods:** opposite area balance, diagonal bisection, cosine-law systems.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eleven alternatives inspected. Several discard one of the two possible bisected diagonals without proof or incorrectly claim one case makes a parallelogram. The explicit label symmetry preserves all side data, so it rigorously handles both cases.

**Archived entries inspected:** 11 of 11. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. An area balance bisects one diagonal; opposite area balance, diagonal bisection, cosine-law systems supply the essential reduction.

## 2018 AIME II Problem 14: A tangent through a near chord endpoint

The incircle of triangle ABC touches BC at X. Line AX meets it again at Y. A tangent at Y meets segments AB,AC at P,Q. Given $AP=3$, $PB=4$, $AC=8$, write $AQ=m/n$ in lowest terms and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2018_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

Let the incircle touch AB,AC at Z,W, and write $AZ=AW=t$. The tangent at the nearer intersection Y separates A from the circle, so $PY=PZ=t-3$; also $BX=BZ=7-t$. The tangent-chord theorem gives equal sines for $\angle PYA$ and $\angle BXA$, while $\angle PAY=\angle BAX$. Applying the sine law in APY and ABX therefore gives $(t-3)/3=(7-t)/7$, so $t=21/5$. Repeating the same argument on the C side, with $q=AQ$, gives $(t-q)/q=(8-t)/8$. Hence $q=8t/(16-t)=168/59$, and the answer is 227.

**Answer:** 227.

**Methods:** equal tangents, tangent-chord theorem, harmonic length relation.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. Sine-law ratios give the harmonic relation directly. Projective polarity and Brianchon are alternatives, but the final projective proof assumes a special normalization without establishing all of its required incidences.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A tangent through a near chord endpoint; equal tangents, tangent-chord theorem, harmonic length relation supply the essential reduction.

## 2019 AIME I Problem 2: A gap between ordered samples

Choose distinct $J, B$ uniformly from $[20]$ in order. Find numerator plus denominator of $P(B-J\ge 2)$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

Symmetry gives $P(B>J)=1/2$. There are $19$ adjacent increasing pairs among $380$ ordered pairs, so the desired probability is $1/2-19/380=9/20$. Answer $29$.

**Answer:** 029.

**Methods:** symmetry, probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The symmetry, order-statistic, and direct pair counts agree; the original proof specifies the uniform subset model.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. A gap between ordered samples; the proof uses symmetry, probability.

## 2019 AIME I Problem 3: An inset hexagon in a right triangle

In right triangle PQR, $PR=15$, $QR=20$, $PQ=25$. Points A,B lie on PQ, C,D on QR, and E,F on PR, in cyclic order around the triangle, with $PA=QB=QC=RD=RE=PF=5$. Find the area of hexagon ABCDEF.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

The triangle area is 150. Remove the three corner triangles PAF, QBC, RDE. Their areas, using the angle sines $\sin P=4/5$, $\sin Q=3/5$, $\sin R=1$, are respectively 10, $15/2$, and $25/2$. The remaining area is $150-10-15/2-25/2=120$.

**Answer:** 120.

**Methods:** area subtraction, sine area formula.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six alternatives inspected. Corner-area subtraction avoids the coordinate calculations for the hexagon itself.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. An inset hexagon in a right triangle; area subtraction, sine area formula supply the essential reduction.

## 2019 AIME I Problem 6: Two perpendiculars turn a product into a square

In convex quadrilateral KLMN, $MN\perp KM$ and $KL\perp LN$. The perpendicular from L to KN meets KM at O. Given $MN=65$, $KL=28$, and $KO=8$, find MO.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

Let T be the foot of L on KN. In right triangle KLN, the projection theorem gives $KL^2=KT\cdot KN$. Triangles KTO and KMN are similar: both are right, and their angles at K are formed by the same two lines. Hence $KT/KO=KM/KN$, so $KL^2=KO\cdot KM$. Thus $KM=28^2/8=98$ and $MO=98-8=90$.

**Answer:** 090.

**Methods:** right-triangle projection theorem, similarity.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All nine alternatives inspected. Two similarities give the product identity without needing MN. One source invokes power at K in a circle containing K, which is not the stated product; the projection proof avoids that mistake.

**Archived entries inspected:** 9 of 9. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Two perpendiculars turn a product into a square; right-triangle projection theorem, similarity supply the essential reduction.

## 2019 AIME I Problem 11: A circle tangent to all three excircles

An integer-sided triangle has $AB=AC$. A circle centered at its incenter is internally tangent to the A-excircle and externally tangent to the other two excircles. Find the smallest possible perimeter.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Normalize $BC=2$ and $AB=AC=t>1$, with altitude $h=\sqrt{t^2-1}$. The inradius is $r=h/(t+1)$; the A-exradius is $h/(t-1)$, and the other exradii equal h. Put the base midpoint at the origin and A at $(0,h)$. The incenter is $(0,r)$ and a lateral excenter is $(t,h)$. Internal tangency forces the required circle radius to be $R=r+2h/(t-1)$; the A-excircle cannot contain its center, which is outside that excircle. External tangency then gives $\sqrt{t^2+(h-r)^2}=R+h$. Simplifying both sides yields $t\sqrt{2t/(t+1)}=t(t+3)/h$, hence $(t+3)^2=2t(t-1)$ and $(t-9)(t+1)=0$. Thus the side ratio is 9:9:2. An integral scaling has integer scale because gcd(9,2)=1. The smallest perimeter is 20, and these lengths satisfy all positive-radius equations.

**Answer:** 020.

**Methods:** inradius and exradii, circle tangency, primitive integer ratios.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. Normalizing the base makes the three radii and center distance explicit. Positivity excludes the extraneous negative quadratic root, and coprimality proves the minimum integral scale.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory. A circle tangent to all three excircles; inradius and exradii, circle tangency, primitive integer ratios supply the essential reduction.

## 2019 AIME I Problem 12: A right angle becomes a purely imaginary quotient

Let $f(z)=z^2-19z$. Complex numbers z,f(z),f(f(z)) form a nondegenerate right triangle, with right angle at f(z). One admissible z is $m+\sqrt n+11i$ for positive integers m,n, with n squarefree. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

The quotient of the two directed successive sides is $\frac{f(f(z))-f(z)}{f(z)-z}=(z-19)(z+1)=(z-9)^2-100$, provided $z\ne0,20$. A right angle makes this quotient purely imaginary. Writing $z=u+11i$, its real part is $(u-9)^2-221$, so $u=9\pm\sqrt{221}$. The stated positive form selects $u=9+\sqrt{221}$; since $221=13\cdot17$, it is squarefree. The quotient has nonzero imaginary part $22\sqrt{221}$, verifying nondegeneracy. Thus the answer is 230.

**Answer:** 230.

**Methods:** complex angle quotient, polynomial cancellation, nondegeneracy.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six alternatives inspected. Factoring the differences first reduces the fourth-degree iterate to a quadratic expression. The nonzero-side and nonzero-quotient checks ensure the formal right-angle condition really gives a triangle.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. A right angle becomes a purely imaginary quotient; complex angle quotient, polynomial cancellation, nondegeneracy supply the essential reduction.

## 2019 AIME I Problem 13: Two cyclic quadrilaterals share a radical axis

Triangle ABC has $AB=4$, $BC=5$, $CA=6$. Points A,B,D,E occur in this order on a line. The circumcircles of ACD and EBC meet again at F, with $DF=2$, $EF=7$. Write $BE=(a+b\sqrt c)/d$ in reduced form with c squarefree; find $a+b+c+d$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Let X be the intersection of CF with the base line. The intersecting-chord angle relations give $\angle DFE=\angle ACB$, whose cosine is $(6^2+5^2-4^2)/(2\cdot6\cdot5)=3/4$. Thus $DE^2=2^2+7^2-2\cdot2\cdot7(3/4)=32$. The cyclic similarities $\triangle XFD\sim\triangle XAC$ and $\triangle XFE\sim\triangle XBC$ give $XF=XA/3=7XB/5$. To fix the order, put A=0,B=4,D=d,E=e on the base, where 4<d<e. Subtracting the circle equations puts their radical-axis intersection at $X=4e/(e+4-d)$, which lies strictly between 4 and d. Thus $XA=XB+4$ and $XB=5/4$. Equal powers in the two circles give $XA\cdot XD=XB\cdot XE$; writing $XD=d_0$ and $XE=d_0+4\sqrt2$ yields $d_0=5\sqrt2/4$. Hence $BE=XB+XD+DE=(5+21\sqrt2)/4$, and the answer is 32.

**Answer:** 032.

**Methods:** cyclic similarities, radical-axis power, cosine law.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six alternatives inspected. Similarities determine the intersection coordinate before power gives the remaining length. Some alternatives mislabel angle C as angle A or write BE where they have computed XE; those slips do not affect the corrected derivation.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Two cyclic quadrilaterals share a radical axis; cyclic similarities, radical-axis power, cosine law supply the essential reduction.

## 2019 AIME I Problem 15: Two internally tangent circles locate a chord midpoint

P lies on chord AB of a circle, with $AP=5$, $PB=3$. A circle through A,P is internally tangent to the original circle at A; another through B,P is internally tangent at B. Their other intersection is Q. The line PQ cuts an 11-unit chord XY of the original circle. If $PQ^2=m/n$ reduced, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Let O,O_1,O_2 be the three centers, and take O as vector origin. The homotheties centered at A and B have ratios 5/8 and 3/8, so $O_1=3A/8$, $O_2=5B/8$, and $P=O_1+O_2$. The common chord PQ is perpendicular to the center line L, and Q is the reflection of P across L. Since the midpoint of OP is also the midpoint of $O_1O_2$, reflection across L puts Q on the line through O parallel to L. Thus $OQ\perp PQ$, making Q the midpoint of XY. Power of P gives $PX\cdot PY=AP\cdot PB=15$. With $PX+PY=11$, the squared distance from P to the midpoint is $PQ^2=(11/2)^2-15=61/4$. The answer is 65.

**Answer:** 065.

**Methods:** homothety of tangent circles, reflected chord endpoints, power of a point.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eight alternatives inspected. The center parallelogram proves the midpoint claim directly. The answer-format guessing alternatives do not prove that claim and are not used.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Two internally tangent circles locate a chord midpoint; homothety of tangent circles, reflected chord endpoints, power of a point supply the essential reduction.

## 2019 AIME II Problem 1: The overlap of two congruent triangles

Congruent triangles ABC and BAD lie on the same side of AB, with C distinct from D, $AB=9$, $BC=AD=10$, $CA=DB=17$. If their intersection area is $m/n$ in lowest terms, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

Put $A=(0,0)$ and $B=(9,0)$. Subtracting the squared distance equations for C gives $C=(15,8)$; reflection in $x=9/2$ gives $D=(-6,8)$. The overlap is triangle ABE, where $E=AC\cap BD$. The two sides have slopes $8/15$ and $-8/15$, so E has coordinates $(9/2,12/5)$. Its area is $(1/2)9(12/5)=54/5$, and the answer is 59.

**Answer:** 059.

**Methods:** congruent-triangle symmetry, coordinate intersection, area.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All nine alternatives inspected. Several coordinate alternatives swap the 10 and 17 sides or write 16 instead of 15, and one defines the intersection of parallel bases. The explicit distance equations and actual diagonal intersection avoid these errors.

**Archived entries inspected:** 9 of 9. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The overlap of two congruent triangles; congruent-triangle symmetry, coordinate intersection, area supply the essential reduction.

## 2019 AIME II Problem 7: Three parallel cuts determine a homothetic triangle

Triangle ABC has $AB=120$, $BC=220$, $CA=180$. Three lines cut interior segments parallel to BC,CA,AB of lengths 55,45,15 respectively. Find the perimeter of the triangle formed by the three lines.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

Use barycentric coordinates $x+y+z=1$ relative to ABC. A segment parallel to BC has length $(1-x)BC$, so the three lines are $x=3/4$, $y=3/4$, $z=7/8$. Their pairwise intersections form a triangle whose sides are parallel to those of ABC. For example, the vertices on $x=3/4$ have y-coordinates 3/4 and $1-3/4-7/8=-5/8$, a difference 11/8. Thus the similarity factor is 11/8. The perimeter is $(11/8)(120+220+180)=715$.

**Answer:** 715.

**Methods:** parallel-line barycentrics, signed similarity, perimeter scaling.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. An affine-coordinate calculation proves the common scale factor directly; it also explains the equilateral-distortion illustration without assuming Euclidean lengths survive an arbitrary affine map.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Three parallel cuts determine a homothetic triangle; parallel-line barycentrics, signed similarity, perimeter scaling supply the essential reduction.

## 2019 AIME II Problem 11: Two tangent circles and a median

Triangle ABC has $AB=7$, $BC=8$, $CA=9$. One circle passes through B and is tangent to AC at A; another passes through C and is tangent to AB at A. Their other intersection is K. If $AK=m/n$ reduced, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Invert about A with radius $AK=t$. The two circles become lines through K parallel to AC and AB respectively. The images $B^{\prime},C^{\prime}$ therefore form parallelogram $AB^{\prime}KC^{\prime}$, with $AB^{\prime}=t^2/7$, $AC^{\prime}=t^2/9$. Triangle $AB^{\prime}C^{\prime}$ is similar, with B and C interchanged, to ABC with scale $t^2/63$. The median from A in ABC has length $\sqrt{(7^2+9^2)/2-8^2/4}=7$. In the image triangle the median is half the parallelogram diagonal AK, so $t/2=7t^2/63$. Since $t>0$, $t=9/2$ and the answer is 11.

**Answer:** 011.

**Methods:** inversion of tangent circles, parallelogram, median scaling.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six alternatives inspected. Inversion reduces the circle configuration to a parallelogram and gives the general formula $AK=AB\cdot AC/(2AM)$. The longer coordinate and trigonometric alternatives contain isolated transcription errors but agree on the length.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Two tangent circles and a median; inversion of tangent circles, parallelogram, median scaling supply the essential reduction.

## 2019 AIME II Problem 13: Curved sector areas are affine in the interior point

A regular octagon $A_1\ldots A_8$ is inscribed in a circle of area 1. An interior point P forms curved regions bounded by $PA_i,PA_{i+1}$ and the minor arc between consecutive vertices. Regions 12 and 34 have areas 1/7 and 1/9. Region 67 has area $1/8-\sqrt2/n$. Find n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Let $s_i$ be the curved-region area, and $n_i$ the outward unit normal of side $A_iA_{i+1}$. If the common side length is L and P has displacement vector p from the center, then $s_i=1/8-(L/2)n_i\cdot p$: the circular cap is fixed and the triangle altitude changes linearly. The octagon normals satisfy $n_6=-(n_1+n_3)/\sqrt2$. Consequently $s_6-1/8=-[(s_1-1/8)+(s_3-1/8)]/\sqrt2=-(1/56-1/72)/\sqrt2=-\sqrt2/504$. Thus n=504.

**Answer:** 504.

**Methods:** affine area functions, regular-polygon normals, signed displacement.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. Subtracting the central area 1/8 cancels the circular caps and makes the normal-vector relation immediate, without computing the circle radius.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Curved sector areas are affine in the interior point; affine area functions, regular-polygon normals, signed displacement supply the essential reduction.

## 2019 AIME II Problem 15: Two chord powers recover both sides of a triangle

In acute triangle ABC, P is the perpendicular foot from C to AB and Q the foot from B to AC. Line PQ meets the circumcircle at X,Y in the order X,P,Q,Y, with $XP=10$, $PQ=25$, $QY=15$. If $AB\cdot AC=m\sqrt n$ with n squarefree, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2019_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Write $AP=p$, $PB=q$, $AQ=r$, $QC=s$. Chord power gives $pq=10\cdot40=400$ and $rs=15\cdot35=525$. Since B,C,P,Q lie on the circle with diameter BC, power at A gives $p(p+q)=r(r+s)$, hence $p^2-r^2=125$. Also $\cos A=r/(p+q)$. The cosine law in APQ yields $625=p^2+r^2-2pr^2/(p+q)$. Substituting $p^2=r^2+125$ and $p(p+q)=r^2+525$ reduces this to $500=800r^2/(r^2+525)$, so $r^2=875$. Therefore $p=10\sqrt{10}$, $q=4\sqrt{10}$, $r=5\sqrt{35}$, $s=3\sqrt{35}$. Their side product is $(p+q)(r+s)=560\sqrt{14}$, giving 574.

**Answer:** 574.

**Methods:** power of a point, diameter circle, linearized cosine law.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five stored entries inspected, including an author-only entry. The two circle powers reduce the system to one variable. The orthic-triangle alternative is valid but introduces extra half-angle calculations.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Two chord powers recover both sides of a triangle; power of a point, diameter circle, linearized cosine law supply the essential reduction.

## 2020 AIME I Problem 1: Three equal-length steps force a seventh of a straight angle

In isosceles triangle ABC with $AB=AC$, interior side points $D\in AC$ and $E\in AB$ satisfy $AE=ED=DB=BC$. Write angle ABC as $m/n$ degrees in lowest terms and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

Put $\angle BAC=x$. Since $AE=ED$, triangle AED has base angles x. Its exterior angle BED is 2 x. As $ED=DB$, angle EBD also equals 2 x. The exterior angle BDC of triangle ADB is therefore 3 x. Since $DB=BC$, angle BCD is 3 x, and the outer isosceles triangle has both base angles 3 x. Thus $7x=180^\circ$ and $\angle ABC=540/7$ degrees, giving 547.

**Answer:** 547.

**Methods:** isosceles angle chasing, exterior angles.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five stored entries inspected, including an author-only entry. Following exterior angles gives a three-step chase; several longer accounts mislabel an intermediate angle.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Three equal-length steps force a seventh of a straight angle; isosceles angle chasing, exterior angles supply the essential reduction.

## 2020 AIME I Problem 6: Equal spheres resting in unequal circular holes

Two circular holes of radii 1 and 2 have centers 7 units apart in a horizontal board. Two equal spheres rest in the holes, with their centers above the board, and touch each other. If their common radius squared is $m/n$ reduced, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

Put $u=r^2$. The center heights are $\sqrt{u-1}$ and $\sqrt{u-4}$, while the horizontal separation is 7 and the center distance is 2 r. Thus $49+(\sqrt{u-1}-\sqrt{u-4})^2=4u$, giving $22-u=\sqrt{(u-1)(u-4)}$. Squaring and canceling $u^2$ yields $39u=480$, so $u=160/13$. This has u≥4 and 22−u>0, and substitution verifies the unsquared equation. The answer is 173.

**Answer:** 173.

**Methods:** sphere cross-sections, center distances, radical equations.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. The vertical-plane cross-section gives one equation and a required sign check. The radical-axis approach is valid but substantially longer.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Equal spheres resting in unequal circular holes; sphere cross-sections, center distances, radical equations supply the essential reduction.

## 2020 AIME I Problem 8: A shrinking spiral is a complex geometric series

A bug starts at O and walks 5 units east. Before each later walk it turns 60 degrees counterclockwise and halves its walking distance. Its positions converge to P. If $OP^2=m/n$ reduced, find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

In complex coordinates, consecutive displacement vectors have ratio $q=(1+i\sqrt3)/4$, of modulus 1/2. Their absolutely convergent sum is $P=5/(1-q)$. Therefore $OP^2=25/|1-q|^2=25/((3/4)^2+(\sqrt3/4)^2)=100/3$. The answer is 103.

**Answer:** 103.

**Methods:** complex geometric series, rotation and scaling, modulus.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All seven alternatives inspected. Complex summation and coordinate sums agree. The final source incorrectly replaces the square of a sum by the sum of squares; it happens to reach the same number, but its omitted cross terms require justification and the argument is not used.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. A shrinking spiral is a complex geometric series; complex geometric series, rotation and scaling, modulus supply the essential reduction.

## 2020 AIME I Problem 13: A perpendicular bisector cuts two angle bisectors

Triangle ABC has $AB=4$, $BC=5$, $CA=6$. Its angle bisector AD meets BC at D. The perpendicular bisector of AD meets the internal angle-bisector lines from B,C at E,F. If $[AEF]=m\sqrt n/p$ reduced with n squarefree, find $m+n+p$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Put $B=(0,0),C=(5,0)$. The side lengths give $A=(1/2,3\sqrt7/2)$, and the angle-bisector theorem gives $D=(2,0)$. The perpendicular bisector of AD is $y=(x+4)/\sqrt7$. From the half-angle formula and $\cos B=1/8$, $\cos C=3/4$, the other bisectors are $y=x\sqrt7/3$ and $y=(5-x)/\sqrt7$. Their intersections with the perpendicular bisector are $E=(3,\sqrt7)$ and $F=(1/2,9\sqrt7/14)$. Segment AF is vertical, of length $6\sqrt7/7$, and the horizontal distance of E from it is 5/2. Hence $[AEF]=(1/2)(6\sqrt7/7)(5/2)=15\sqrt7/14$, giving 36.

**Answer:** 036.

**Methods:** angle-bisector theorem, half-angle slopes, coordinate area.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All twelve alternatives inspected. Coordinates remove the diagram-dependent auxiliary constructions. Some synthetic alternatives interchange E,F or write $3\sqrt3$ for the bisector length $3\sqrt2$; these transcription slips are avoided.

**Archived entries inspected:** 12 of 12. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A perpendicular bisector cuts two angle bisectors; angle-bisector theorem, half-angle slopes, coordinate area supply the essential reduction.

## 2020 AIME I Problem 15: An orthocenter tangent determines a chord and an altitude

An acute triangle ABC has orthocenter H and circumcircle omega. The tangent at H to the circumcircle of HBC meets omega at X,Y. Given $HA=3$, $HX=2$, $HY=6$, write $[ABC]=m\sqrt n$ with n squarefree and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Let D be the foot from A to BC. The reflection of H in BC lies on omega, so power at H gives $3(2HD)=2\cdot6$, hence HD=2 and AD=5. Use coordinates $H=(0,0),A=(0,3),D=(0,-2)$. The reflected point is $(0,-4)$, so omega has equation $x^2+y^2+ux+y-12=0$ for some real u. Its intersections B,C with y=−2 have x-coordinates satisfying $x^2+ux-10=0$. The circle HBC consequently has equation $x^2+y^2+ux+7y=0$, and its tangent at H is $ux+7y=0$. Parameterize this line by $(x,y)=t(c,s)$ with $c^2+s^2=1$. Substitution into omega gives $t^2-6st-12=0$, since uc+7 s=0. Its roots are−2 and 6 after choosing direction, so s=2/3 and c²=5/9. Therefore $u^2=49s^2/c^2=196/5$. The squared difference of the two base coordinates is $BC^2=u^2+40=396/5$. Thus $[ABC]=(5/2)BC=3\sqrt{55}$, giving 58.

**Answer:** 058.

**Methods:** orthocenter reflection, circle equations, tangent line, chord roots.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eight alternatives inspected. The reflected orthocenter fixes the altitude immediately. Explicit circle equations supply the remaining length without assumptions about the relative positions of auxiliary circumcenters.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. An orthocenter tangent determines a chord and an altitude; orthocenter reflection, circle equations, tangent line, chord roots supply the essential reduction.

## 2020 AIME II Problem 2: A random slope in a square

Choose $P$ uniformly in the unit square. Find numerator plus denominator of the chance that its slope from $(5/8,3/8)$ is at least $1/2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

The comparison line is $y=x/2+1/16$. For $x<5/8$ choose points below it; for $x>5/8$ choose points above it. The two trapezoid areas total $\frac12(1/16+3/8)(5/8)+\frac12(5/8+7/16)(3/8)=43/128$. Answer $171$.

**Answer:** 171.

**Methods:** geometric probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Both area decompositions agree. The vertical line has measure zero and does not affect the probability.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. A random slope in a square; the proof uses geometric probability.

## 2020 AIME II Problem 4: A quarter turn with an unknown center

A clockwise rotation through m degrees, $0<m<180$, takes vertices $(0,0),(0,12),(16,0)$ to $(24,18),(36,18),(24,2)$ respectively. If the center is $(x,y)$, find $m+x+y$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_II_Problems/Problem_4) · MAA AMC.

### Solution

The vector from the first to second vertex changes from $(0,12)$ to $(12,0)$, so m=90. A 90-degree clockwise rotation around $(x,y)$ sends the origin to $(x-y,x+y)$. Hence $x-y=24$ and $x+y=18$, giving center $(21,-3)$. The same rotation sends the third vertex to $(24,2)$, so it verifies all correspondences. The requested value is $90+18=108$.

**Answer:** 108.

**Methods:** rotation vectors, fixed-center equations.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eight alternatives inspected. The displacement vector determines the angle before the center is solved. The matrix alternative has a copied right-hand side error, and the final trigonometric alternative misstates one distance.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A quarter turn with an unknown center; rotation vectors, fixed-center equations supply the essential reduction.

## 2020 AIME II Problem 7: The largest sphere in two perpendicular cones

Two congruent solid right circular cones have radius 3 and height 8. Their perpendicular axes meet at an interior point O,3 units from each base. A sphere must lie inside both cones. If the greatest radius squared is m/n reduced, find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

Take O as origin, with the cone apices $(5,0,0)$ and $(0,5,0)$ and base planes x=−3,y=−3. For a sphere center $(x,y,z)$, its radius r cannot exceed the perpendicular distances to the nearest lateral supporting planes: $r\sqrt{73}\le15-3x-8\sqrt{y^2+z^2}$ and $r\sqrt{73}\le15-3y-8\sqrt{x^2+z^2}$. Adding and using square roots at least the corresponding absolute coordinates gives $2r\sqrt{73}\le30-3(x+y)-8(|x|+|y|)\le30$. Thus $r\le15/\sqrt{73}$. The sphere centered at O with this radius clears both lateral surfaces and both bases, whose distance is 3. Hence the bound is attained, $r^2=225/73$, and the answer is 298.

**Answer:** 298.

**Methods:** cone supporting planes, symmetric optimization, attained upper bound.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. They evaluate the radius at O but do not rigorously justify that a displaced center cannot improve it; one asserts every maximizing center must lie on both axes. The summed supporting-plane inequalities establish the required global bound.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The largest sphere in two perpendicular cones; cone supporting planes, symmetric optimization, attained upper bound supply the essential reduction.

## 2020 AIME II Problem 12: A line crossing a numbered grid

An odd $m$ by odd $n$ row-major grid has label $200$ in its top row and $2000$ in its bottom row. Count $(m, n)$ for which the line through those cell centers enters cell $1099$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

The midpoint of the two centers is the center of cell $1100$; cell $1099$ is immediately left in the same middle row. Thus the line enters its interior exactly when its slope has absolute value below $1$: $|1800-(m-1)n|>m-1$. The endpoint-row requirements give $m=3,5,7,9$. Their odd $n$ ranges and exclusions are respectively $667\ldots999$ excluding $899,901$; $401\ldots499$ excluding $449,451$; $287\ldots333$ excluding $299,301$; $223\ldots249$ excluding $225$. Counts $165,48,22,13$ sum $248$.

**Answer:** 248.

**Methods:** lattice geometry, casework.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Source 0 states an imprecise modular slope criterion. Source 1 and the new proof use the signed horizontal displacement and exclude slopes of absolute value 1.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. A line crossing a numbered grid; the proof uses lattice geometry, casework.

## 2020 AIME II Problem 13: Tangent lengths and a monotone angle sum

A convex pentagon ABCDE has an incircle and side lengths $AB=5$, $BC=CD=DE=6$, $EA=7$. Find its area.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_II_Problems/Problem_13) · MAA AMC.

### Solution

Equal tangents from each vertex give tangent lengths 3,2,4,2,4 in order, by solving adjacent sums equal to the side lengths. If the inradius is r, half the exterior angle at a vertex with tangent length t is $\arctan(t/r)$. The exterior angles sum to 360 degrees, so $\arctan(3/r)+2\arctan(2/r)+2\arctan(4/r)=180^\circ$. The left side strictly decreases with r. At r=4, the last term is 90 degrees, while $2\arctan(1/2)$ is acute with tangent 4/3 and hence complements $\arctan(3/4)$. Thus r=4 is the unique solution. The area is the inradius times semiperimeter, $4\cdot15=60$.

**Answer:** 060.

**Methods:** tangent-length systems, exterior-angle closure, monotonicity.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eight alternatives inspected. Monotonic angle closure verifies r=4 and excludes the spurious small root of the quartic without extra geometric casework. The approximation and answer-format guessing alternatives are not proofs.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Tangent lengths and a monotone angle sum; tangent-length systems, exterior-angle closure, monotonicity supply the essential reduction.

## 2020 AIME II Problem 15: A projection parallelogram from two circle tangents

In acute scalene triangle ABC, the tangents at B,C to its circumcircle meet at T. Points X,Y are the perpendicular projections of T onto lines AB,AC. Given $BT=CT=16$, $BC=22$, and $TX^2+TY^2+XY^2=1143$, find $XY^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2020_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Let M be the midpoint of BC, so $TM\perp BC$. Since $\angle BXT=\angle BMT=90^\circ$, B,X,T,M are cyclic. The tangent-chord theorem then gives $MX\perp AC$: in directed angles, the angle between MX and AB equals $90^\circ-\angle BAC$. Similarly $MY\perp AB$. Thus MX is parallel to TY and MY is parallel to TX, making MXTY a parallelogram. Its diagonals are MT and XY, so $MT^2+XY^2=2(TX^2+TY^2)$. Also $MT^2=16^2-11^2=135$. Substituting the given sum gives $135+XY^2=2(1143-XY^2)$, hence $XY^2=717$.

**Answer:** 717.

**Methods:** tangent-chord angles, projection parallelogram, parallelogram law.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. The projection parallelogram turns the requested expression into a diagonal identity. The last alternative prints 153 for 135 and mixes a squared length with a square root; the geometric identity and corrected arithmetic give 717.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A projection parallelogram from two circle tangents; tangent-chord angles, projection parallelogram, parallelogram law supply the essential reduction.

## 2021 AIME I Problem 2: Two rectangles sharing a diagonal

Rectangles ABCD and AECF share diagonal AC. The first has $AB=3$, $BC=11$; the second has $AF=7$, $FC=9$. Their placement has E beyond side BC and F beyond side AD, so AE crosses BC and CF crosses AD. If the overlap area is m/n reduced, find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

Let $G=AD\cap FC$ and put AG=x. The right triangles AFG and CDG are similar, with corresponding sides AF=7,CD=3. Hence $FG=7(11-x)/3$ and $CG=3x/7$. Since FG+CG=FC=9, $7(11-x)/3+3x/7=9$, giving x=35/4. By central symmetry about the common diagonal midpoint, the overlap is a parallelogram with a side AG and height 3. Its area is 105/4, so the answer is 109.

**Answer:** 109.

**Methods:** overlapping rectangles, similar right triangles, parallelogram area.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six alternatives inspected. The placement conditions from the original diagram are included explicitly. Several longer coordinate alternatives contain expanded-square slips; the two similarity ratios determine the overlap directly.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Two rectangles sharing a diagonal; overlapping rectangles, similar right triangles, parallelogram area supply the essential reduction.

## 2021 AIME I Problem 6: A spatial British-flag identity

AB,AC,AD are the three cube edges from A, and G is the opposite vertex. A point P has distances $BP=60\sqrt{10}$, $CP=60\sqrt5$, $DP=120\sqrt2$, $GP=36\sqrt7$. Find AP.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

Take A as the origin and the three edges as coordinate axes, with common length s. Expanding the four squared distances cancels all terms in s and the linear coordinates of P, giving $BP^2+CP^2+DP^2-GP^2=2AP^2$. Hence $2AP^2=36000+18000+28800-9072=73728$, so AP=192.

**Answer:** 192.

**Methods:** squared-distance cancellation, cube coordinates, British-flag identity.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. The identity holds for any point in three-dimensional space, so no assumption that P is inside the cube is needed. The affine-function alternative calls a function linear when it is generally affine; the cancellation identity remains valid.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A spatial British-flag identity; squared-distance cancellation, cube coordinates, British-flag identity supply the essential reduction.

## 2021 AIME I Problem 9: Three altitudes determine a trapezoid through a side ratio

An isosceles trapezoid ABCD has $AB\parallel CD$, $AD=BC$, and $AB<CD$. The distances from A to lines BC,CD,BD are 15,18,10. If its area is K, find $\sqrt2K$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

By symmetry the distance from B to AC is 10. Thus triangle ABC has altitudes 15,18,10 opposite BC,AB,AC respectively, and its side ratio is $AB:BC:AC=5:6:9$. Write these lengths as 5 t,6 t,9 t. Heron gives area $10\sqrt2t^2$, while base AB and altitude 18 give 45 t, so $t=9/(2\sqrt2)$. The cosine law gives $\cos B=(25+36-81)/60=-1/3$. Each leg therefore overhangs the shorter base by $6t/3=2t$, making CD=9 t. The trapezoid area is $18(5t+9t)/2=126t=567/\sqrt2$. The answer is 567.

**Answer:** 567.

**Methods:** inverse altitude ratios, Heron formula, trapezoid overhangs.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All ten alternatives inspected. The three-altitude reduction gives a 5:6:9 triangle and avoids simultaneous radical equations. Some alternatives mislabel feet or equate angles from the wrong cyclic quadrilateral; the area-ratio method does not use those steps.

**Archived entries inspected:** 10 of 10. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Three altitudes determine a trapezoid through a side ratio; inverse altitude ratios, Heron formula, trapezoid overhangs supply the essential reduction.

## 2021 AIME I Problem 11: Projecting a quadrilateral onto its opposite diagonals

A cyclic quadrilateral has side lengths $AB=4$, $BC=5$, $CD=6$, $DA=7$. Project A,C orthogonally to line BD to obtain $A_1,C_1$, and project B,D to AC to obtain $B_1,D_1$. If the perimeter of $A_1B_1C_1D_1$ is m/n reduced, find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Let the acute diagonal angle be theta. In each triangle formed by the diagonal intersection and two adjacent vertices, the two perpendicular feet are separated by the opposite side times $\cos\theta$; this follows by similarity, or by projecting onto the two intersecting lines and reflecting across their angle bisector. Thus the new perimeter is $22\cos\theta$. Subtracting the four cosine-law equations around the diagonal intersection gives $2AC\cdot BD\cos\theta=|AB^2+CD^2-BC^2-DA^2|=22$. Ptolemy gives $AC\cdot BD=4\cdot6+5\cdot7=59$. Hence the perimeter is 242/59, and the answer is 301.

**Answer:** 301.

**Methods:** projection similarity, diagonal cosine identity, Ptolemy theorem.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six stored entries inspected, including the common introductory proof. The projection relation and alternating squared-side identity are valid. One alternative incorrectly assumes equal diagonals of length $\sqrt{59}$; its appended repair recovers the product-based argument.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Projecting a quadrilateral onto its opposite diagonals; projection similarity, diagonal cosine identity, Ptolemy theorem supply the essential reduction.

## 2021 AIME I Problem 13: An affine power difference measures a radical-axis distance

Circles of radii 961 and 625 intersect at A,B. A third circle is externally tangent to both. Line AB cuts a 120-degree minor arc from the third circle. Find the distance between the centers of the first two circles.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Write their centers U,V, distance d, radii R=961,S=625. Their power difference $F(Z)=|Z-U|^2-R^2-|Z-V|^2+S^2$ is affine, with gradient length 2 d, and vanishes on AB. If the third circle has center W and radius r, external tangency gives $F(W)=(R+r)^2-R^2-(S+r)^2+S^2=2r(R-S)$. Thus the distance from W to AB is $|F(W)|/(2d)=r(R-S)/d$. The 120-degree chord condition makes this distance $r\cos60^\circ=r/2$. Canceling r gives $d=2(R-S)=672$.

**Answer:** 672.

**Methods:** affine circle powers, radical-axis distance, chord angle.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All nine alternatives inspected. The affine power proof avoids signed-distance assumptions. Several coordinate versions reverse the radii in a signed formula, while the special-radius and infinite-radius arguments do not justify replacing the given configuration.

**Archived entries inspected:** 9 of 9. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. An affine power difference measures a radical-axis distance; affine circle powers, radical-axis distance, chord angle supply the essential reduction.

## 2021 AIME I Problem 15: Perpendicular parabolas share a circle of intersection

For positive integer k, consider $y=x^2-k$ and $x=2(y-20)^2-k$. Let S contain k for which the curves meet at four distinct points on a circle of radius at most 21. Find the sum of the least and greatest members of S.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

Adding the first equation to half the second and completing squares shows every intersection lies on $(x-1/4)^2+(y-41/2)^2=(24k+325)/16$. Thus the radius restriction is exactly k≤280. Substitution gives $F_k(x)=2(x^2-k-20)^2-x-k=0$. For k≥6, put $t=\sqrt{k+20}<k$. Then $F_k(-t)<0$, $F_k(0)>0$, $F_k(t)<0$, and $F_k(x)\to+\infty$ at both ends. Four disjoint sign-changing intervals give four distinct real roots. For k=5, x=−5 is a root with derivative−1, so F is negative just to its right; together with F(0)>0,F(5)<0 and the positive tail, this again gives four distinct roots. For k≤4, a negative intersection must have −k≤x≤0, giving y≤k²−k≤12 from the first curve, but $y\ge20-\sqrt{k/2}>18$ from the second, impossible. The quartic has at most two positive roots by its two coefficient sign changes. Thus S consists exactly of integers 5 through 280, and the answer is 285.

**Answer:** 285.

**Methods:** linear combinations of conics, circle completion, real-root sign intervals.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. The circle equation is elementary; one longer focal-parameter source gives an incorrect radius formula. The sign-interval proof replaces sketch-based claims that four intersections exist and handles the boundary k=5 explicitly.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Perpendicular parabolas share a circle of intersection; linear combinations of conics, circle completion, real-root sign intervals supply the essential reduction.

## 2021 AIME II Problem 2: An equilateral slice and an exterior isosceles triangle

ABC is equilateral of side 840. Point D lies on the perpendicular to BC through B, toward A. The parallel to BC through D meets AB,AC at E,F. Extend EF beyond F to G so AFG is isosceles. If $[AFG]:[BED]=8:9$, find AF.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_II_Problems/Problem_2) · MAA AMC.

### Solution

Put AF=x. Triangle AEF is equilateral; since angle AFG is 120 degrees, its equal sides are AF=FG=x. Thus $[AFG]=x^2\sqrt3/4$. Triangle BED is 30-60-90 with hypotenuse BE=840−x, so its legs are $(840-x)/2$ and $(840-x)\sqrt3/2$, giving area $(840-x)^2\sqrt3/8$. The ratio becomes $2x^2/(840-x)^2=8/9$. Since 0<x<840, $x/(840-x)=2/3$, hence x=336.

**Answer:** 336.

**Methods:** equilateral similarity, obtuse isosceles triangle, area ratio.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. The 120-degree angle identifies which sides of the isosceles triangle are equal, preventing an ambiguous isosceles case split.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. An equilateral slice and an exterior isosceles triangle; equilateral similarity, obtuse isosceles triangle, area ratio supply the essential reduction.

## 2021 AIME II Problem 5: When fixed sides and area specify one obtuse triangle

For s>0, consider all obtuse triangles of area s having sides 4 and 10. The values of s for which such triangles exist and are all congruent form $[a,b)$. Find $a^2+b^2$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

Let theta be the included angle between the sides 4 and 10. Area is $20\sin\theta$. For each 0<s<20 there are exactly two possible included angles, theta and 180−theta, and hence two possible side-length triples. The obtuse included-angle choice always gives an obtuse triangle. For the acute choice, the only possible obtuse angle is opposite side 10. Its boundary is the right triangle of hypotenuse 10 and leg 4, with area $2\sqrt{10^2-4^2}=4\sqrt{21}$. Below this area the acute-included-angle triangle is also obtuse; at or above it that triangle is right or acute. Thus exactly one obtuse congruence class remains for $4\sqrt{21}\le s<20$. The answer is 336+400=736.

**Answer:** 736.

**Methods:** sine-area ambiguity, obtuse-triangle threshold, endpoint analysis.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eight alternatives inspected. Monotonicity on the two angle branches establishes the exact number of congruence classes and the endpoint inclusion. The final source has a missing square in a sine radical and reverses a monotonicity assertion.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. When fixed sides and area specify one obtuse triangle; sine-area ambiguity, obtuse-triangle threshold, endpoint analysis supply the essential reduction.

## 2021 AIME II Problem 8: Nonbacktracking walk on a cube

On a cube, an ant starts at a bottom vertex, chooses its first edge uniformly, and thereafter uniformly chooses either edge that does not reverse its previous step. Find numerator plus denominator of its chance of being on top after $8$ steps.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

Count paths by last-edge types $BB, BT, TB, TT$. Start with $(2,1,0,0)$. If the vector is $(a, b, c, d)$, the next is $(a+2c,a,d,d+2b)$: a horizontal edge allows one horizontal and one vertical continuation, a vertical edge two horizontal continuations. Seven iterations give $(118,66,62,138)$. Thus top probability $(66+138)/(3\cdot2^7)=17/32$, answer $49$.

**Answer:** 049.

**Methods:** memory states, nonbacktracking walks.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Source 4 multiplies dependent marginal probabilities and therefore gives an invalid derivation, even though cancellation happens to produce the correct linear recurrence. The four last-edge states, or a properly conditioned two-step recurrence, are sufficient.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Nonbacktracking walk on a cube; the proof uses memory states, nonbacktracking walks.

## 2021 AIME II Problem 10: Three spheres determine the opening of a common wedge

Three pairwise externally tangent spheres have radii 36,36,13. Two distinct common tangent planes meet in line ell. Find the distance from ell to the 13-sphere’s tangency point on either plane, expressed as m/n reduced; report m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

On either plane, the tangency points of two externally tangent spheres of radii r,s are distance $2\sqrt{rs}$ apart, by subtracting the squared normal separation $(r-s)^2$ from center distance $(r+s)^2$. Thus the three tangency points form an isosceles triangle with base 72 and equal sides $12\sqrt{13}$; its altitude is 24. The line ell is parallel to the base, because the two equal spheres have identical distances to both planes. In the perpendicular cross-section, the centers lie on the angle bisector of the wedge. Their normal distances to the plane differ by 36−13=23 while their projected distances differ by 24, so the half-angle has tangent 23/24. The smaller sphere center has height 13 above the plane, hence its tangency point is distance $13/(23/24)=312/23$ from ell. The answer is 335.

**Answer:** 335.

**Methods:** tangent sphere contact distances, dihedral cross-section, similar right triangles.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. Projecting the sphere-center triangle first gives a 24-unit altitude and avoids the more complicated radical distances between the center plane and the common line.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Three spheres determine the opening of a common wedge; tangent sphere contact distances, dihedral cross-section, similar right triangles supply the essential reduction.

## 2021 AIME II Problem 12: Diagonal angle from area and alternating side squares

A convex quadrilateral has consecutive side lengths 5,6,9,7 and area 30. Let theta be its acute diagonal angle. Write $\tan\theta=m/n$ reduced and find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

Write the diagonal lengths p,q. Splitting into four triangles gives $2K=pq\sin\theta$. Adding the cosine-law equations for alternate sides and subtracting the other pair gives $|5^2-6^2+9^2-7^2|=2pq\cos\theta$. Divide these identities to obtain $\tan\theta=4K/|5^2-6^2+9^2-7^2|=120/21=40/7$. The answer is 47.

**Answer:** 047.

**Methods:** diagonal area formula, alternating squared-side identity.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five stored entries inspected, including a standalone formula note. The diagonal identity works for every convex quadrilateral; an alternative begins with a cyclic-only Ptolemy identity, which cannot be assumed here, though its final general tangent formula is correct.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Diagonal angle from area and alternating side squares; diagonal area formula, alternating squared-side identity supply the essential reduction.

## 2021 AIME II Problem 14: Two right-angle circles transfer an angle

An acute triangle ABC has circumcenter O and centroid G. The tangent at A meets the perpendicular to OG through G at X; line XG meets BC at Y. Angles ABC,BCA,XOY have ratio 13:2:17. Write angle BAC as m/n degrees reduced and find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2021_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

Let M be the midpoint of BC, so A,G,M are collinear and $OM\perp BC$. The right angles show O,A,X,G and O,M,Y,G are cyclic. Their inscribed-angle identities imply that angles XOY and AOM agree up to supplementation. Put B=13 t,C=2 t, so A=180−15 t. Acuteness gives 6<t<90/13. Since B>C, the smaller central angle AOM equals $180-(B-C)=180-11t$; its supplement is 11 t. But the prescribed angle XOY=17 t is obtuse in this range, while 11 t is acute. Hence $17t=180-11t$, giving t=45/7 and A=585/7 degrees. The answer is 592.

**Answer:** 592.

**Methods:** cyclic right-angle quadrilaterals, circumcenter angles, angle-branch selection.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. Most use the intended diagram to choose angle orientation. The acute-triangle bounds select the correct supplementary branch explicitly, making the proof independent of the drawing.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Two right-angle circles transfer an angle; cyclic right-angle quadrilaterals, circumcenter angles, angle-branch selection supply the essential reduction.

## 2022 AIME I Problem 3: Angle bisectors meet on the trapezoid midline

An isosceles trapezoid ABCD has parallel bases AB=500, CD=650 and legs AD=BC=333. The internal bisectors at A,D meet at P; those at B,C meet at Q. Find PQ.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

Each intersection is equally distant from both parallel bases, hence lies on the trapezoid midline. Let L,R be the leg midpoints. Since adjacent angles are supplementary, angle APD is 90 degrees. Thus L, the midpoint of its hypotenuse, satisfies LP=AD/2=333/2; similarly RQ=333/2. These segments point inward along the midline, whose length is LR=(500+650)/2=575. Since 575>333, their endpoints occur in order L,P,Q,R. Therefore PQ=575−333=242.

**Answer:** 242.

**Methods:** angle-bisector distances, trapezoid midline, hypotenuse midpoint.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eight alternatives inspected. The right-angle and midpoint argument avoids coordinates and trigonometric expressions. A source writes the cosine double-angle identity with the wrong sign; it is unnecessary here.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Angle bisectors meet on the trapezoid midline; angle-bisector distances, trapezoid midline, hypotenuse midpoint supply the essential reduction.

## 2022 AIME I Problem 5: Subtract squared swimming velocities

A 264-foot-wide river flows east at 14 feet per minute. Melanie, swimming at 80 feet per minute relative to the water, starts D feet downstream from Sherry, whose swimming speed is 60. They swim straight to the same opposite-bank point, equally far from their starting points, and arrive together. Find D.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

Equal travel times and equal ground distances give equal ground speeds. Their ground velocity vectors are therefore (−u,v) and (u,v), with v>0, since the destination lies above their starting midpoint. Relative to the water these become (−u−14,v) and (u−14,v). Subtracting their squared speed equations gives $56u=80^2-60^2=2800$, so u=50. Then $v^2=60^2-36^2=2304$, giving v=48. The travel time is 264/48=11/2 minutes, and D=2 u(11/2)=550.

**Answer:** 550.

**Methods:** relative velocity, difference of squares, symmetry.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. Equal-time symmetry makes the two horizontal ground velocities opposites; subtracting their squared speeds eliminates the crossing speed immediately.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** algebra, geometry. Subtract squared swimming velocities; relative velocity, difference of squares, symmetry supply the essential reduction.

## 2022 AIME I Problem 8: Intersections of the three vertex circles

An equilateral triangle has circumradius 18. At each vertex, a circle is tangent to both incident side segments and internally tangent to the circumcircle. Their six pairwise intersections form two equilateral triangles. Write the smaller triangle’s side as $\sqrt a-\sqrt b$, with positive integers a,b, and find a+b.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

Let r be a vertex-circle radius and O its circumcenter. Its center lies on the vertex bisector at distance 2 r from that vertex. Internal tangency gives $|18-2r|=18-r$, whose nonzero solution is r=12. The three circle centers consequently lie 6 units from O, away from their respective vertices. Choose their coordinates as $(0,-6),(3\sqrt3,3),(-3\sqrt3,3)$. The last two circles intersect at $(0,3\pm\sqrt{117})$. Rotating the nearer intersection around O produces the smaller equilateral triangle, of circumradius $\sqrt{117}-3$. Its side is $\sqrt3(\sqrt{117}-3)=\sqrt{351}-\sqrt{27}$, so the answer is 378.

**Answer:** 378.

**Methods:** internal circle tangency, rotational symmetry, chord coordinates.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. Explicit center coordinates distinguish the inner and outer intersection triangles and avoid ambiguous diameter statements in the introductory source.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Intersections of the three vertex circles; internal circle tangency, rotational symmetry, chord coordinates supply the essential reduction.

## 2022 AIME I Problem 10: Equal-radius slices of tangent spheres

Three pairwise externally tangent spheres have radii 11,13,19. A plane cuts them in equal-radius circles centered A,B,C, respectively. All sphere centers lie on the same side of the plane. Given AB squared=560, find AC squared.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

Let the center heights above the plane be h_A,h_B,h_C and the common section radius be rho. Then $h_B^2-h_A^2=13^2-11^2=48$. Tangency and AB squared=560 give $(h_B-h_A)^2=24^2-560=16$. Since h_B>h_A, their difference is 4 and sum 12, so h_A=4,h_B=8. Thus rho squared=121−16=105, and h_C squared=361−105=256, giving h_C=16. Finally $AC^2=30^2-(16-4)^2=756$.

**Answer:** 756.

**Methods:** orthogonal projection, sphere cross-sections, difference of squares.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. The same-side condition fixes the height signs; the rest follows from two applications of the Pythagorean theorem.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Equal-radius slices of tangent spheres; orthogonal projection, sphere cross-sections, difference of squares supply the essential reduction.

## 2022 AIME I Problem 11: Tangent lengths determine a parallelogram

A circle is tangent to segments DA,AB,BC of parallelogram ABCD, whose angle A is acute. Diagonal AC meets the circle at P,Q in that order, with AP=3,PQ=9,QC=16. Write the parallelogram’s area as $a\sqrt b$ with b squarefree; find a+b.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Power gives tangent lengths 6 from A and 20 from C. Let L,R be the contacts on the parallel sides AD,BC. With the circle center as origin, take L=(−r,0), R=(r,0), A=(−r,−6), and C=(r,20). The opposite signs follow because the contacts lie on the segments and A,C are opposite vertices. Since AC=28, $(2r)^2+26^2=28^2$, giving 2 r=6 $\sqrt{3}$. Write t for the tangent length from B. Then AB=6+t, BC=20+t, and the component of AB parallel to AD has length 6−t in signed coordinates. Thus $(6+t)^2-(6-t)^2=(2r)^2=108$, so t=9/2. The area is $(20+t)(2r)=147\sqrt3$, giving 150.

**Answer:** 150.

**Methods:** power of a point, equal tangents, parallel-side coordinates.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All eight alternatives inspected. Tangent powers give 6 and 20 immediately; coordinates along the two parallel contact lines then avoid mislabeled lengths in several longer solutions.

**Archived entries inspected:** 8 of 8. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Tangent lengths determine a parallelogram; power of a point, equal tangents, parallel-side coordinates supply the essential reduction.

## 2022 AIME I Problem 14: Perimeter-bisecting cleavers determine a120-degree angle

A triangle has BC=219 and positive integer sides AB,AC. The lines through the midpoints of AB and AC that divide the triangle into two regions of equal perimeter meet at 30 degrees. Find its perimeter.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

A perimeter-bisecting line through a side midpoint is parallel to the opposite internal angle bisector. To verify this, put C=0,A=b u,B=a v for unit vectors u,v and M=(b u+a v)/2. If a≥b, the other boundary point X satisfies CX=(a−b)/2, so $X-M=-b(u+v)/2$; the case b≥a is analogous. Consequently the acute angle between the two given lines is 90−A/2, forcing A=120 degrees. Put p=AB,q=AC. The cosine law gives $p^2+pq+q^2=219^2$. Modulo 3, p≡q; substituting this into the equation modulo 9 forces 3|p and 3|q. Write p=3 x,q=3 y, and u=x+y,v=x−y. Then $3u^2+v^2=4\cdot73^2=21316$. Positivity gives 73<u≤84. For u=74 through 84, the possible v squared values are 4888,4441,3988,3529,3064,2593,2116,1633,1144,649,148. Only 2116=46 squared is a square. Thus u=80, {x,y}={63,17}, and the perimeter is 219+3(80)=459.

**Answer:** 459.

**Methods:** cleaver theorem, cosine law, quadratic-form bounds.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. The cleaver direction is proved by a vector calculation. A short bounded search after extracting the factor 3 replaces unsupported uniqueness claims or a much longer Eisenstein-integer argument.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory. Perimeter-bisecting cleavers determine a120-degree angle; cleaver theorem, cosine law, quadratic-form bounds supply the essential reduction.

## 2022 AIME II Problem 3: Circumsphere of a right square pyramid

A right square pyramid has base side 6 and volume 54. Its five vertices lie on a sphere of radius m/n in lowest terms. Find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

The pyramid height is $3\cdot54/36=9/2$. Place the base center at height 0 and the apex at height 9/2. By symmetry the sphere center has height z on this axis. A base vertex is horizontal distance 3 $\sqrt{2}$ from the axis, so equality of squared radii gives $18+z^2=(9/2-z)^2$. Hence z=1/4 and the radius is 9/2−1/4=17/4. The answer is 21.

**Answer:** 021.

**Methods:** pyramid volume, axial symmetry, circumsphere.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. Equating squared distances on the symmetry axis gives a linear equation for the sphere center.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Circumsphere of a right square pyramid; pyramid volume, axial symmetry, circumsphere supply the essential reduction.

## 2022 AIME II Problem 7: The triangle of common tangents

Two externally tangent circles have radii 6 and 24. Their three common tangent lines form a triangle. Find its area.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

The two external common tangents meet at T, the external homothety center. Its distances to the centers are in ratio 1:4 and differ by 30, so the smaller distance is 10. The half-angle between those tangents has sine 6/10=3/5 and tangent 3/4. Put the smaller center at 0 and the larger at 30 along their axis; then T is at−10 and the internal common tangent is at 6. The triangle altitude from T is 16, and its half-base is 16(3/4)=12. Its area is 16(24)/2=192.

**Answer:** 192.

**Methods:** external homothety center, common tangents, half-angle triangle.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. The external center and a 3-4-5 right triangle determine both altitude and base directly.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The triangle of common tangents; external homothety center, common tangents, half-angle triangle supply the essential reduction.

## 2022 AIME II Problem 9: Regions between two supporting lines

Join all $m$ marked points on one line to all $n$ on a parallel line, with no triple interior intersection. Including the supporting lines, count bounded regions for $m=7, n=5$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

For $n=1$, the $m$ segments and supporting line create $m-1$ bounded regions. Adding the jth lower point creates $m$ new regions from its fan, and $(j-1)\binom m2$ more from crossings with previous fans; the no-triple condition makes all these crossings distinct. Thus $R(m,n)=mn-1+\binom m2\binom n2$. At $(7,5)$ this is $34+210=244$.

**Answer:** 244.

**Methods:** planar regions, incremental counting.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** The fan-insertion and planar Euler counts agree. The no-triple-crossing hypothesis is essential for counting intersections by endpoint pairs.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Regions between two supporting lines; the proof uses planar regions, incremental counting.

## 2022 AIME II Problem 11: Two angle-bisector reflections determine a quadrilateral

A convex quadrilateral ABCD has AB=2,AD=7,CD=3. The acute angles DAB and ADC have internal bisectors meeting at the midpoint M of BC. Find the square of its area.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Take A=(0,0),D=(7,0). Reflection in AM takes B to P=(2,0), while reflection in DM takes C to Q=(4,0). Since MB=MC, we have MP=MQ; hence M=(3,h) with h>0. The reflection formulas give $B=\frac{12}{9+h^2}(3,h)-(2,0)$ and $C=(10,0)+\frac{24}{16+h^2}(-4,h)$. Because B+C=2 M, their vertical coordinates yield $6/(9+h^2)+12/(16+h^2)=1$. This simplifies to $(h^2-5)(h^2+12)=0$, so h=$\sqrt{5}$. M is equidistant from the three lines AB,AD,DC; its distance to each is h. Decomposing the quadrilateral into ABM,ADM,DCM gives area $(2+7+3)h/2=6\sqrt5$. Its square is 180.

**Answer:** 180.

**Methods:** reflection in angle bisectors, midpoint coordinates, equidistance area sum.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All seven alternatives inspected. Reflection gives a short coordinate derivation without an unproved similarity. Several alternatives contain mislabeled angle variables or a typographical AM-squared identity; the final barycentric approach is also valid once its extended-line configuration is established.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Two angle-bisector reflections determine a quadrilateral; reflection in angle bisectors, midpoint coordinates, equidistance area sum supply the essential reduction.

## 2022 AIME II Problem 12: Pair the foci of two intersecting ellipses

Reals a>4,b>1,x,y satisfy $x^2/a^2+y^2/(a^2-16)=1$ and $(x-20)^2/(b^2-1)+(y-11)^2/b^2=1$. Find the minimum of a+b.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

The first ellipse has foci U=(−4,0),V=(4,0), and the second has foci W=(20,10),Z=(20,12). For P=(x,y), their focal definitions give $2(a+b)=PU+PV+PW+PZ\ge UW+VZ=26+20=46$. Equality holds when P lies on both segments UW and VZ. Their intersection is P=(14,15/2), giving PU=39/2,PV=25/2,PW=13/2,PZ=15/2, hence a=16,b=7. These satisfy the strict parameter bounds. The attained minimum is 23.

**Answer:** 023.

**Methods:** ellipse focal definition, paired triangle inequalities, equality verification.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** The single stored solution inspected. Pairing the foci proves the bound, and the explicit segment intersection verifies simultaneous equality and both strict parameter restrictions.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Pair the foci of two intersecting ellipses; ellipse focal definition, paired triangle inequalities, equality verification supply the essential reduction.

## 2022 AIME II Problem 15: Ptolemy and opposite-angle products in a cyclic hexagon

Two externally tangent circles have centers U,V at distance 15. A third circle through U,V meets the first at B,C and the second at A,D, in convex cyclic order A,B,U,C,D,V. Given AB=2 and CD=16, find the hexagon area.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2022_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Write the small-circle radii r,s, so r+s=15, and q=rs. In cyclic quadrilateral U,A,V,D, the angles at A,D are supplementary and AV=DV=s. Adding their cosine-law formulas gives $UA\cdot UD=UV^2-s^2=225-s^2=q+15r$. Similarly $VB\cdot VC=q+15s$. Ptolemy in the two quadrilaterals on opposite sides of UV gives $UA\cdot VB=q+30$ and $UD\cdot VC=q+240$. Multiplication therefore yields $(q+15r)(q+15s)=(q+30)(q+240)$, or q squared+450 q=q squared+270 q+7200, hence q=40. Brahmagupta on U,B,A,V gives area squared $14(16-r)(1+r)=14(16+q)=784$. On U,C,D,V it gives $56(23-r)(8+r)=56(184+q)=12544$. The areas add to 28+112=140.

**Answer:** 140.

**Methods:** cyclic opposite angles, Ptolemy theorem, Brahmagupta formula.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. The opposite-angle cosine identity supplies the length product attributed only to an SSA observation in the last source. This makes the Ptolemy product proof explicit; the reflection alternatives have inconsistent prime labels and the long central-angle source incorrectly calls a common chord a perpendicular bisector.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Ptolemy and opposite-angle products in a cyclic hexagon; cyclic opposite angles, Ptolemy theorem, Brahmagupta formula supply the essential reduction.

## 2023 AIME I Problem 1: No opposite pair of men

Five men and nine women stand randomly at $14$ cyclic positions. Find numerator plus denominator of the probability every man is opposite a woman.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_I_Problems/Problem_1) · MAA AMC.

### Solution

The five male positions are uniform among $\binom{14}5$ subsets. Choose five distinct diameters among $7$, and one of their two endpoints for each man: $\binom75 2^5$ favorable subsets. Probability $48/143$; answer $191$.

**Answer:** 191.

**Methods:** opposite pairs, probability.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All nine stored solutions inspected. Diameter selection, sequential placement, sequential opposite-partner exposure, and labeled arrangements all give 48/143. Each method must consistently distinguish labeled positions from rotations; the independent diameter-subset count avoids extra symmetry factors.

**Archived entries inspected:** 9 of 9. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. No opposite pair of men; the proof uses opposite pairs, probability.

## 2023 AIME I Problem 5: Two diameter triangles recover a square’s area

P lies on the circumcircle of square ABCD, with PA times PC=56 and PB times PD=90. Find the square area.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

Let d be the diameter. Because AC and BD are perpendicular diameters, APC and BPD are right triangles. Their areas show that the distances from P to AC and BD are 56/d and 90/d. Those distances are the absolute orthogonal coordinates of P relative to the circle center, so $(56/d)^2+(90/d)^2=(d/2)^2$. Hence the square area $d^2/2=\sqrt{56^2+90^2}=106$.

**Answer:** 106.

**Methods:** diameter right angles, perpendicular coordinates, area products.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All ten alternatives inspected. Altitudes to the two perpendicular diameters yield the answer with no choice of arc or angle. The longer trigonometric and coordinate alternatives agree after several mislabeled lines and factors are corrected.

**Archived entries inspected:** 10 of 10. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Two diameter triangles recover a square’s area; diameter right angles, perpendicular coordinates, area products supply the essential reduction.

## 2023 AIME I Problem 8: Use inward normals to settle an angle branch

A rhombus ABCD has acute angle A. P lies on its incircle and has distances 9,5,16 from lines DA,AB,BC, respectively. Find the perimeter.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

The distance between DA and BC is 9+16=25, so the inradius is 25/2. Let O be the center, e the unit vector OP, and n 1,n 2 the inward unit normals to DA,AB. Then $e\cdot n_1=-7/25$ and $e\cdot n_2=-3/5=-15/25$. Their perpendicular components have absolute values 24/25 and 20/25. Therefore $n_1\cdot n_2=(105\pm480)/625$, giving 117/125 or−3/5. Their angle is 180−A and is obtuse, so the dot product must be−3/5. Thus cos A=3/5,sin A=4/5. A side has length 25/(4/5)=125/4, and the perimeter is 125.

**Answer:** 125.

**Methods:** inward unit normals, circle projections, angle-branch selection.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six alternatives inspected. Several proofs select perpendicular-foot orders from the diagram. The negative dot product of inward normals uses the stated acute angle to choose the branch rigorously.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Use inward normals to settle an angle branch; inward unit normals, circle projections, angle-branch selection supply the essential reduction.

## 2023 AIME I Problem 12: Sum three directed projections in an equilateral triangle

In equilateral ABC of side 55, D,E,F lie on BC,CA,AB with BD=7,CE=30,AF=40. An interior P satisfies angle AEP=angle BFP=angle CDP=alpha. Find tan squared alpha.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

Let u,v,w be unit vectors along AB,BC,CA, so u+v+w=0. Write f=FP,d=DP,e=EP. Their projections along those oriented sides give $(f+d+e)\cos\alpha=(P-F)\cdot u+(P-D)\cdot v+(P-E)\cdot w$. Choose A=0,B=55 u,C=55(u+v). Since distinct direction vectors have dot product−1/2, the right side is $-(40+(7-55/2)+(30-55))=11/2$. The perpendicular distances from P to the sides sum to the altitude 55 $\sqrt{3}$/2, by adding the three triangle areas. Thus $(f+d+e)\sin\alpha=55\sqrt3/2$. Dividing yields tan alpha=5 $\sqrt{3}$, and its square is 75.

**Answer:** 075.

**Methods:** directed projection sum, Viviani theorem, equilateral symmetry.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six alternatives inspected. Summing projections eliminates the unknown point and handles the signs automatically. Some cosine-law alternatives incorrectly obtain a negative cosine, and the final cyclic-Ptolemy calculation contains incorrect intermediate lengths; the independent projection proof avoids these defects.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Sum three directed projections in an equilateral triangle; directed projection sum, Viviani theorem, equilateral symmetry supply the essential reduction.

## 2023 AIME I Problem 13: A Gram determinant distinguishes two rhombohedra

Every face of each of two noncongruent parallelepipeds is a rhombus with diagonals $\sqrt{21}$ and $\sqrt{31}$. Write the larger volume divided by the smaller as m/n reduced; find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

Let u,v,w be the three edge vectors at a vertex. The parallelogram law gives squared edge length 13 and each pairwise dot product equal to plus or minus 5/2. The squared volume is the Gram determinant $13^3-13\cdot3(5/2)^2+2(u\cdot v)(v\cdot w)(w\cdot u)$. Consequently its two possible values are $13^3-975/4\pm125/4$, namely 3969/2 and 1922. Both are positive and realized by taking all three off-diagonal dot products positive or all negative. Changing the sign of an edge reverses two dot-product signs, so the two product signs exhaust the possibilities up to congruence. The volume ratio is $\sqrt{(3969/2)/1922}=63/62$, giving 125.

**Answer:** 125.

**Methods:** Gram determinant, parallelogram law, sign invariants.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. The determinant treats all sign patterns at once and explains why only two volumes occur. The tetrahedron alternatives are shorter numerically but require establishing their symmetric vertex choices.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A Gram determinant distinguishes two rhombohedra; Gram determinant, parallelogram law, sign invariants supply the essential reduction.

## 2023 AIME II Problem 3: A Brocard point gives two similar triangles

In an isosceles right triangle ABC with right angle A, an interior point P satisfies angle PAB=angle PBC=angle PCA and AP=10. Find the triangle area.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

Let the common angle be theta. Then angle APC=90 degrees, while triangles APB and BPC each have angles theta,45−theta,135 degrees. Their corresponding sides AB,BC are in ratio 1:$\sqrt{2}$. Thus PB=$\sqrt{2}$ times AP=10 $\sqrt{2}$ and PC=$\sqrt{2}$ times PB=20. The right triangle APC gives AC squared=100+400=500. Since AB=AC, the required area is 500/2=250.

**Answer:** 250.

**Methods:** Brocard angles, similarity chain, right-isosceles triangle.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All seven alternatives inspected. The direct similarity proof avoids a separate Brocard-angle formula. Some sources mislabel APC as 135 degrees or state AB=BC; the corrected angle and side correspondences are explicit.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A Brocard point gives two similar triangles; Brocard angles, similarity chain, right-isosceles triangle supply the essential reduction.

## 2023 AIME II Problem 6: Midpoints in an L-shaped region

Choose two independent uniform points in a $2$ by $2$ square with its upper-right unit square removed. Find numerator plus denominator of the chance their midpoint remains in the region.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

A midpoint can fail only when the points lie in the upper-left and lower-right squares, in either order, probability $2/9$. Conditional on that, each coordinate of the midpoint exceeds $1$ with probability $1/2$, independently. Failure probability is $1/18$, so success $17/18$ and answer $35$.

**Answer:** 035.

**Methods:** geometric probability, conditioning.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All four sources inspected. Complementary conditioning on diagonally separated unit squares gives a one-quarter conditional failure chance. Integration, coordinate independence, and four-point symmetry average are equivalent. The independent proof uses coordinate independence and symmetry.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Midpoints in an L-shaped region; the proof uses geometric probability, conditioning.

## 2023 AIME II Problem 7: Avoiding monochromatic rectangles

Color $12$ cyclic vertices red or blue. Count colorings with no monochromatic rectangle among the vertices.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_II_Problems/Problem_7) · MAA AMC.

### Solution

Every inscribed rectangle uses two diameters. Hence among the six opposite pairs, at most one may be $RR$ and at most one $BB$. With no monochromatic pair, there are $2^6$ colorings; with one, $6\cdot2\cdot2^5$; with one of each, $6\cdot5\cdot2^4$. Total $64+384+480=928$.

**Answer:** 928.

**Methods:** opposite-pair encoding, forbidden configurations.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** All four sources inspected. Every inscribed rectangle uses two diameters, so monochromatic opposite-pair counts give a complete three-case classification. All reach 928.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Avoiding monochromatic rectangles; the proof uses opposite-pair encoding, forbidden configurations.

## 2023 AIME II Problem 9: A common tangent and radical axis determine a trapezoid

Circles meet at P,Q with PQ=5. Their common external tangent nearer P touches at A,B. The parallel through P meets them again at X,Y, with PX=10,PY=14. Write the area of trapezoid XABY as m $\sqrt{n}$, n squarefree; find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_II_Problems/Problem_9) · MAA AMC.

### Solution

Put P=(0,0) and the tangent at height h>0. If X=(x,0),Y=(y,0), the tangent points are A=(x/2,h),B=(y/2,h), since the radii bisect the parallel chords. The radical axis PQ meets AB at its midpoint M=((x+y)/4,h), by equality of tangent powers. If x,y have the same sign, then AB=2 and MP≥6, while MP times MQ=1 and MQ≥MP−5≥1, a contradiction. Hence x,y have opposite signs: AB=12,XY=24, and the horizontal component of MP has absolute value 1. Because this tangent is nearer P, the order on the secant is M,P,Q, so MP(MP+5)=36. Thus MP=4 and h squared=16−1=15. The trapezoid area is (12+24)$\sqrt{15}$/2=18 $\sqrt{15}$, giving 33.

**Answer:** 033.

**Methods:** common tangent chord midpoints, radical axis, secant power, configuration branches.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. They assume X,P,Y occur in that order from a diagram; the same-side contradiction establishes it. The nearer-tangent condition selects the correct secant root.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A common tangent and radical axis determine a trapezoid; common tangent chord midpoints, radical axis, secant power, configuration branches supply the essential reduction.

## 2023 AIME II Problem 12: Use the stated uniqueness to construct the point

Triangle ABC has AB=13,BC=14,CA=15, and M is the midpoint of BC. The ray AM meets the circumcircle again at P beyond M. A unique Q on AM satisfies angle PBQ=angle PCQ. Write AQ=m/$\sqrt{n}$, with m,n coprime positive integers; find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

The median formula gives $AM^2=(13^2+15^2)/2-7^2=148$. Power at M gives AM times MP=49. Reflect P across M to obtain Q 0. Since MP=49/$\sqrt{148}$<AM, Q 0 lies on segment AM. The quadrilateral B,Q 0,C,P is a parallelogram because its diagonals bisect each other at M; its opposite angles at B,C are therefore equal. Thus Q 0 satisfies the given angle condition, and the stated uniqueness identifies it as Q. Consequently $AQ=AM-MP=(148-49)/\sqrt{148}=99/\sqrt{148}$. The requested sum is 247.

**Answer:** 247.

**Methods:** median length, power of a point, central reflection, uniqueness construction.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. Constructing the central reflection uses the uniqueness explicitly supplied by the problem. Several alternatives have transcription slips in their sine-law ratios or AQ/PM labels; none is needed in the short construction.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Use the stated uniqueness to construct the point; median length, power of a point, central reflection, uniqueness construction supply the essential reduction.

## 2023 AIME II Problem 14: Cut a tilted cube into two simplexes

A cube has parallel edges AB,CD and face diagonals AC,BD, with rectangle ABDC in a vertical plane. Their heights above a horizontal plane are 0,2,8,10 meters, respectively. Water fills the cube up to height 7. Write its volume as m/n reduced; find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2023_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

Let the three edge vectors from A be u,v,w, with u=AB and v+w=AC. The vertical direction lies in the span of u and v+w, so the vertical components of v,w are equal; each is 4, while that of u is 2. If the edge length is s, the squared components of the vertical unit vector in this orthonormal edge frame sum to 1: $(2/s)^2+(4/s)^2+(4/s)^2=1$. Hence s=6. In fractional cube coordinates, height is 2 x+4 y+4 z. Reflecting all coordinates about 1/2 turns the air region into 2 x+4 y+4 z<3 in the unit cube. Without upper bounds this is a tetrahedron of volume 27/(6 times 2 times 4 times 4)=27/192. Only x can exceed 1; translating that excess leaves the analogous tetrahedron with threshold 1 and volume 1/192. Thus the air fraction is 26/192=13/96. The water volume is 216(1−13/96)=747/4, giving 751.

**Answer:** 751.

**Methods:** orthonormal projections, affine height, simplex volume subtraction.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. Orthogonal components derive the edge length without an assumed drawing scale. Subtracting two tetrahedra gives the exact water volume without calculus or an unproved frustum identification.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Cut a tilted cube into two simplexes; orthonormal projections, affine height, simplex volume subtraction supply the essential reduction.

## 2024 AIME I Problem 5: Power of a point between offset rectangles

Rectangles ABCD and EFGH lie on opposite sides of their common baseline, with D,E,C,F in that order. A,D,H,G are concyclic. Given BC=16,AB=107,FG=17,EF=184, find CE.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

Let DE=x, and let the lines AD and GH meet at T. Since the rectangles occupy opposite sides of the baseline, TD=17,TA=33,TH=x,TG=x+184. Power in the circle through A,D,H,G gives $x(x+184)=17\cdot33=561$. Thus $(x-3)(x+187)=0$, and x>0 gives x=3. Hence CE=107−3=104.

**Answer:** 104.

**Methods:** power of a point, secant products, rectangle coordinates.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six alternatives inspected. The figure places the rectangles on opposite sides of the common baseline; the restatement states this explicitly. Power gives a quadratic with a unique positive root. The final ruler-and-compass estimate is not a proof.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Power of a point between offset rectangles; power of a point, secant products, rectangle coordinates supply the essential reduction.

## 2024 AIME I Problem 8: A row of congruent circles determines the inradius

Inside triangle ABC, a row of eight circles of radius 34 is tangent to BC, with consecutive circles tangent and the two end circles tangent to AB,AC. A row of 2024 radius-one circles fits in the same way. Write the inradius as m/n reduced; find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

Let $K=\cot(B/2)+\cot(C/2)$ and L=BC. A row of n circles of radius rho has end offsets rho cot(B/2),rho cot(C/2) and n−1 center gaps 2 rho. Thus $L=\rho[K+2(n-1)]$. The two rows give 34(K+14)=K+4046, so K=1190/11. The incircle is the n=1 case, hence r=L/K=1+4046/K=192/5. The answer is 197.

**Answer:** 197.

**Methods:** angle-bisector tangent lengths, circle rows, linear elimination.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. The raw statement omits the all-circles tangent-to-BC condition conveyed by its figure and misnames one end side; the restatement makes the diagram configuration explicit. An isosceles assumption in one source and a collinearity claim in another are unnecessary.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A row of congruent circles determines the inradius; angle-bisector tangent lengths, circle rows, linear elimination supply the essential reduction.

## 2024 AIME I Problem 9: A rhombus approaches a hyperbola’s asymptote

Four points on $x^2/20-y^2/24=1$ form a rhombus with diagonal intersection at the origin. Find the greatest real number strictly below BD squared for every such rhombus.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

The diagonals are perpendicular and bisect each other. Write their lines as y=mx and y=−x/m. Each must meet the hyperbola, so $5/6<m^2<6/5$. A point B on the first line has $x^2=120/(6-5m^2)$, hence $BD^2=480(1+m^2)/(6-5m^2)$. This is strictly increasing in m squared; as m squared decreases to 5/6 it tends to 480, without reaching it. Every m squared inside the stated interval yields four valid points and a rhombus, so values approach 480 arbitrarily closely. Therefore 480 is the greatest strict lower bound.

**Answer:** 480.

**Methods:** perpendicular diagonals, hyperbola asymptotes, unattained infimum.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four stored entries inspected. One entry explicitly warns that its square argument is wrong, and another merely guesses a product of constants. The slope interval proves both the bound and its sharpness.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A rhombus approaches a hyperbola’s asymptote; perpendicular diagonals, hyperbola asymptotes, unattained infimum supply the essential reduction.

## 2024 AIME I Problem 10: Tangent similarities and Ptolemy determine a symmedian chord

Triangle ABC has AB=5,BC=9,CA=10. The circumcircle tangents at B,C meet at D. Segment AD meets the circle again at P. Write AP=m/n reduced; find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

The tangent-chord theorem gives $\triangle PBD\sim\triangle BAD$ and $\triangle PCD\sim\triangle CAD$. Since DB=DC, these imply PB/PC=AB/AC=1/2. Put PB=t,PC=2 t. The cosine law in ABC gives cos A=11/25, and cyclicity gives cos BPC=−11/25. Hence $81=t^2+4t^2+4t^2(11/25)=(169/25)t^2$, so t=45/13. Ptolemy in ABPC gives $9AP=5(2t)+10t=20t$, yielding AP=100/13 and answer 113.

**Answer:** 113.

**Methods:** tangent-chord similarities, symmedian ratios, Ptolemy theorem.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. The ratio from the equal tangents and one Ptolemy equation avoid computing the remote tangent intersection or invoking an unproved median-symmedian similarity.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Tangent similarities and Ptolemy determine a symmedian chord; tangent-chord similarities, symmedian ratios, Ptolemy theorem supply the essential reduction.

## 2024 AIME I Problem 11: Rotating blue vertices away from themselves

Color the eight vertices of a regular octagon independently red or blue. Find numerator plus denominator of the probability that some rotation sends every blue vertex to a red vertex.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_I_Problems/Problem_11) · MAA AMC.

### Solution

Let $B\subset\mathbb Z_8$ be the blue set. If $|B|\le3$, its difference set has at most $1+2\binom32=7$ elements, so some rotation makes $B$ disjoint from itself. If $|B|>4$, this is impossible. For $|B|=4$, a successful shift sends $B$ to its complement. An odd shift forces an alternating coloring, giving $2$ choices. A shift by $2$ or $6$ gives $4$ choices, alternating on each parity cycle. A shift by $4$ gives $2^4=16$ choices, one blue vertex per opposite pair. These three classes are disjoint because the first two are invariant under shift $4$. Thus there are $1+8+28+56+22=115$ successful colorings out of $256$, and the answer is $371$.

**Answer:** 371.

**Methods:** difference sets, cyclic symmetry, complement pairing.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Both source solutions enumerate blue-set shapes. Their small-support sufficiency arguments are informal. The independent difference-set bound and shift-cycle classification replace the shape testing.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Rotating blue vertices away from themselves; the proof uses difference sets, cyclic symmetry, complement pairing.

## 2024 AIME I Problem 14: Place a disphenoid in a rectangular box

A tetrahedron has AB=CD=$\sqrt{41}$, AC=BD=$\sqrt{80}$, and BC=AD=$\sqrt{89}$. Its insphere radius is m $\sqrt{n}$/p in reduced squarefree form. Find m+n+p.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

The coordinates $A=(0,0,0),B=(4,5,0),C=(4,0,8),D=(0,5,8)$ realize exactly the six given lengths. Their centroid I=(2,5/2,4) is interior. The half-turn symmetries of this rectangular-box construction permute the four faces while fixing I, so its four face distances are equal. Plane BCD is 10 x+8 y+5 z=80. Thus the common distance is $|20+20+20-80|/\sqrt{100+64+25}=20/\sqrt{189}=20\sqrt{21}/63$. The requested sum is 104.

**Answer:** 104.

**Methods:** disphenoid box coordinates, face symmetry, point-plane distance.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All seven alternatives inspected. The box coordinates are checked against the exact labels, which several sources swap. A trigonometric source has an incorrect cosine and sine calculation, and the final volume-subtraction note omits a factor 1/2; the direct distance formula avoids both.

**Archived entries inspected:** 7 of 7. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Place a disphenoid in a rectangular box; disphenoid box coordinates, face symmetry, point-plane distance supply the essential reduction.

## 2024 AIME I Problem 15: A double-root boundary gives the largest box diagonal

Consider all rectangular boxes of surface area 54 and volume 23. Let r be the least radius such that each box fits inside a sphere of radius r. Write r squared=p/q reduced; find p+q.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

For edge lengths x,y,z, we have xy+yz+zx=27 and xyz=23. The least enclosing radius of that box is half its space diagonal: opposite vertices give the lower bound and the midpoint sphere attains it. Thus maximize $x^2+y^2+z^2=(x+y+z)^2-54$. The feasible set is compact: each coordinate lies between 23/27 and 729/92, the latter from 27≥2 $\sqrt{23 x}$. At a maximum of S=x+y+z, at least two edges coincide. Otherwise the cubic $t^3-St^2+27t-23$ has three distinct positive roots, and a small increase in S preserves three positive roots by the intermediate value theorem on three disjoint root neighborhoods, contradicting maximality. Put y=z=a. Then $(a-2)(a^2+2a-23)=0$, so a=2 or−1+2 $\sqrt{6}$. The respective sums S are 39/4 and $(96\sqrt6-21)/23$; the latter is smaller, since $\sqrt{6}$<5/2 gives it less than 219/23<39/4. Hence the maximum occurs at (23/4,2,2). Therefore $r^2=[(23/4)^2+8]/4=657/64$, giving 721.

**Answer:** 721.

**Methods:** enclosing sphere, symmetric cubic, repeated-root extremum, compactness.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. Symmetry alone does not prove two edges are equal at an optimum. The compactness and root-perturbation argument supplies that step, and comparing both positive double-root candidates establishes the global maximum.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A double-root boundary gives the largest box diagonal; enclosing sphere, symmetric cubic, repeated-root extremum, compactness supply the essential reduction.

## 2024 AIME II Problem 5: Similar corner triangles give a reciprocal-side formula

A convex equilateral hexagon has each pair of opposite sides parallel. The extended lines of alternating sides form a triangle with side lengths 200,240,300. Find the hexagon side length.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

Let the common side be s. On the 300-unit side of the outer triangle, the central hexagon edge has length s. The two remaining pieces lie in corner triangles similar to the outer triangle; their lengths along this side are 300 s/200 and 300 s/240, because their parallel cut edges are also s. Thus $300=s+(300/200)s+(300/240)s=(15/4)s$, giving s=80. Equivalently, $1/s=1/200+1/240+1/300$.

**Answer:** 080.

**Methods:** parallel-side similarity, corner cuts, reciprocal length identity.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. Similarity proves the result; the scale-drawing trial in the other alternative is not an exact argument.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Similar corner triangles give a reciprocal-side formula; parallel-side similarity, corner cuts, reciprocal length identity supply the essential reduction.

## 2024 AIME II Problem 8: Axial sections reduce torus tangency to two circles

A torus has tube radius 3 and its tube centers are 6 units from its axis. A sphere has radius 11. When the torus is internally or externally tangent to the sphere along a circle, those circle radii are r_i,r_o. Write r_i−r_o=m/n reduced; find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

In an axial section through the sphere center O, a tube circle has center C at perpendicular distance 6 from the axis and radius 3. Internal tangency gives OC=11−3=8; external tangency gives OC=11+3=14. The tangency point lies on OC and is distance 11 from O, so its perpendicular distance from the axis is 11 times 6/OC. Revolving that point gives the contact circle. Therefore $r_i=66/8=33/4$, $r_o=66/14=33/7$, and the difference is 99/28. The answer is 127.

**Answer:** 127.

**Methods:** surfaces of revolution, axial sections, tangent-circle homothety.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. The axial section and the ratio along the line of centers determine the contact radii directly.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Axial sections reduce torus tangency to two circles; surfaces of revolution, axial sections, tangent-circle homothety supply the essential reduction.

## 2024 AIME II Problem 10: A perpendicular center line forces a side-sum identity

Triangle ABC has circumcenter O, incenter I, circumradius 13, and inradius 6. If AI is perpendicular to OI, find AB times AC.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

Let AI meet the circumcircle again at D. The perpendicular from O bisects chord AD, so AI=ID and AD=2 ID. The usual arc-midpoint angle chase gives DB=DC=DI: for example, angles IBD and BID both equal 90−C/2. Ptolemy in ABDC now gives $AB\cdot DC+AC\cdot DB=AD\cdot BC$, hence AB+AC=2 BC. Writing a=BC,b=CA,c=AB, the area is $r(a+b+c)/2=3ar/2$, but also abc/(4 R). Canceling a yields bc=6 Rr=6 times 13 times 6=468.

**Answer:** 468.

**Methods:** arc-midpoint incenter lemma, chord midpoint, Ptolemy theorem, area identities.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All nine stored entries inspected, including the introductory setup and theorem proof. The side-sum relation avoids Euler’s center-distance formula entirely. The angle chase proving the arc-midpoint lemma is included rather than assumed.

**Archived entries inspected:** 9 of 9. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A perpendicular center line forces a side-sum identity; arc-midpoint incenter lemma, chord midpoint, Ptolemy theorem, area identities supply the essential reduction.

## 2024 AIME II Problem 12: The unique ladder through a point touches an astroid

Let A=(1/2,0),B=(0,$\sqrt{3}$/2). Among unit segments joining the positive coordinate axes, there is a unique interior point C of AB lying on no other such segment. Write OC squared=p/q reduced, where O is the origin; find p+q.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

For an interior point C=(x,y), a unit segment has intercepts cos theta,sin theta, with 0<theta<$\pi$/2, and contains C exactly when $F(\theta)=x\sec\theta+y\csc\theta=1$. This function tends to infinity at both ends and is strictly convex, because both secant and cosecant have positive second derivatives on this interval. Consequently it has exactly one solution precisely when its minimum equals 1. For the segment AB, theta=$\pi$/3. The derivative condition is $x\sin\theta/\cos^2\theta=y\cos\theta/\sin^2\theta$, so $x/\cos^3\theta=y/\sin^3\theta$. Together with F=1 this gives x=cos cubed theta=1/8 and y=sin cubed theta=3 $\sqrt{3}$/8. Thus OC squared=28/64=7/16, giving 23.

**Answer:** 023.

**Methods:** fixed-length intercept segments, convex envelope, uniqueness via strict convexity.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. A stationary envelope calculation alone does not prove that exactly one segment passes through the point. Strict convexity and endpoint divergence provide the necessary-and-sufficient uniqueness argument.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. The unique ladder through a point touches an astroid; fixed-length intercept segments, convex envelope, uniqueness via strict convexity supply the essential reduction.

## 2024 AIME II Problem 15: Rectangles supported by dodecagon chords

Count rectangles whose four sides lie on sides or diagonals of a regular dodecagon. Rectangle corners need not be polygon vertices.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2024_AIME_II_Problems/Problem_15) · MAA AMC.

### Solution

Chord directions occur in multiples of $15^\circ$, giving six perpendicular direction pairs. Three pairs have one coordinate pattern and three have the pattern rotated by $15^\circ$. For a unit circumcircle in the first pattern, available horizontal levels are $0,\pm1/2,\pm\sqrt3/2$, with respective half-widths $1,\sqrt3/2,1/2$. Among pairs of horizontal lines, $3$ pairs allow $5$ vertical lines and $7$ pairs allow $3$, yielding $3\binom52+7\binom32=51$. In the rotated pattern the levels are $\pm\sin15^\circ,\pm\sin45^\circ,\pm\sin75^\circ$. Respectively $1,5,9$ horizontal pairs allow $6,4,2$ vertical lines, yielding $\binom62+5\binom42+9\binom22=54$. These counts follow by requiring all four intersections to lie within both chord segments. Every rectangle has a unique perpendicular direction pair. Total $3(51+54)=315$.

**Answer:** 315.

**Methods:** geometric enumeration, direction classes.

**Verification:** Independently enumerated horizontal and vertical chord endpoints for both orientation types: 51 and 54.

**Source comparison:** All three source solutions inspected. They split six direction classes into two symmetric triples, obtaining 51 and 54 per orientation. The independent chord-coordinate table verifies the segment-length restrictions without relying on missing diagrams.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Rectangles supported by dodecagon chords; the proof uses geometric enumeration, direction classes.

## 2025 AIME I Problem 2: Affine coordinates preserve a reflected heptagon’s area

On AB, points A,D,E,B occur with consecutive lengths 4,16,8; on AC, A,F,G,C occur with lengths 13,52,26. Reflect D about F to get M, and G about E to get N. If DEGF has area 288, find the area of heptagon AFNBCEM.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_I_Problems/Problem_2) · MAA AMC.

### Solution

Use A as origin and write D=u,F=v. Then E=5 u,B=7 u,G=5 v,C=7 v,M=2 v−u,N=10 u−5 v. Put J=the absolute determinant of u,v. The quadrilateral DEGF is the difference of triangles AEG and ADF, so its area is $(25-1)J/2=12J=288$, giving J=24. In the heptagon’s ordered determinant sum, the nonzero coefficients of the determinant of u,v are−10,35,49,−35,10, whose sum is 49. Thus its area is 49 J/2=588.

**Answer:** 588.

**Methods:** affine coordinates, point reflection, shoelace area.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. The determinant calculation makes the area-preservation claim exact. One source is truncated, and another incorrectly declares DE and FG parallel to BC and describes a collinear reflected triangle as congruent; neither affects the independent coordinate proof.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Affine coordinates preserve a reflected heptagon’s area; affine coordinates, point reflection, shoelace area supply the essential reduction.

## 2025 AIME I Problem 6: A tangential trapezoid determines its base sums

An isosceles trapezoid of area 72 has an incircle of radius 3. Its unequal parallel bases have lengths r,s. Find r squared+s squared.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_I_Problems/Problem_6) · MAA AMC.

### Solution

The height is the incircle diameter 6, so r+s=24. Equal tangent lengths give the sum of the bases equal to the sum of the two legs; thus each leg is 12. Dropping perpendiculars between the bases gives $(r-s)^2/4=12^2-6^2=108$. Therefore $r^2+s^2=[(r+s)^2+(r-s)^2]/2=(576+432)/2=504$.

**Answer:** 504.

**Methods:** Pitot theorem, isosceles trapezoid height, symmetric sums.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All six alternatives inspected. The tangent-length identity and one right triangle establish the result without quoting a special trapezoid-radius formula.

**Archived entries inspected:** 6 of 6. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A tangential trapezoid determines its base sums; Pitot theorem, isosceles trapezoid height, symmetric sums supply the essential reduction.

## 2025 AIME I Problem 8: A circle has exactly one point on each tangent

For real k, the equations $|25+20i-z|=5$ and $|z-4-k|=|z-3i-k|$ have exactly one complex solution z. Write the sum of all possible k as m/n reduced; find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_I_Problems/Problem_8) · MAA AMC.

### Solution

Writing z=a+bi, the first locus is a circle centered(25,20) of radius 5. Squaring and subtracting in the second gives the line 8 a−6 b−8 k−7=0. There is exactly one common point precisely when its distance from the circle center is 5: $|200-120-8k-7|/10=5$. Hence 73−8 k=±50, giving k=23/8 or 123/8. Their sum is 73/4, so the answer is 77.

**Answer:** 077.

**Methods:** complex distance loci, perpendicular bisector, tangent-line distance.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All five alternatives inspected. The distance-to-line equation proves there are exactly two parameter values. A source’s arbitrary opposite-point experiment is unnecessary and includes a pair that is not diametrically opposite.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. A circle has exactly one point on each tangent; complex distance loci, perpendicular bisector, tangent-line distance supply the essential reduction.

## 2025 AIME I Problem 9: Use reflection symmetry to construct the required intersection

Rotate the parabola y=x squared−4 by 60 degrees counterclockwise about the origin. Its unique fourth-quadrant intersection with the original has y-coordinate $(a-\sqrt b)/c$, with a,c coprime positive integers. Find a+b+c.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_I_Problems/Problem_9) · MAA AMC.

### Solution

The original parabola is invariant under reflection in the y-axis. Composing that reflection with the 60-degree rotation is reflection in the line of angle 120 degrees, namely y=−$\sqrt{3}$ times x. Thus a point of the original parabola on this line also belongs to the rotated parabola. Solving $x^2-4=-\sqrt3x$ gives the positive root $x=(\sqrt{19}-\sqrt3)/2$, which has y<0. By the stated uniqueness, this is the requested intersection. Its height is $y=(3-\sqrt{57})/2$, giving 3+57+2=62.

**Answer:** 062.

**Methods:** reflection-rotation composition, symmetry construction, quadratic intersection.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. One incorrectly claims equal distances force equal y-coordinates, overlooking another algebraic branch; another equates coordinates of differently parameterized points. The reflection construction uses only the uniqueness explicitly supplied by the problem.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Use reflection symmetry to construct the required intersection; reflection-rotation composition, symmetry construction, quadratic intersection supply the essential reduction.

## 2025 AIME I Problem 12: Order chambers divide an equilateral simplex

In the plane x+y+z=75, the strict inequalities $x-yz<y-zx<z-xy$ describe three disjoint convex regions, exactly one of finite area. Write that finite area as a $\sqrt{b}$ with b squarefree; find a+b.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

Put X=x+1,Y=y+1,Z=z+1, so X+Y+Z=78. The inequalities factor as $(X-Y)Z<0$ and $(Y-Z)X<0$. In the positive-coordinate triangle they are exactly 0<X<Y<Z. This is a full connected component: leaving it would require crossing X=0,Z=0,X=Y,or Y=Z, all excluded by the strict inequalities. It is bounded, so the given uniqueness identifies it as the desired component. The positive-coordinate triangle has vertices(78,0,0),(0,78,0),(0,0,78), side 78 $\sqrt{2}$ and area 3042 $\sqrt{3}$. Permuting coordinates partitions it into six congruent order chambers, so the required area is 3042 $\sqrt{3}$/6=507 $\sqrt{3}$. The answer is 510.

**Answer:** 510.

**Methods:** inequality factorization, translated simplex, permutation symmetry.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. Translating by 1 reveals the sign structure and divides the positive-coordinate simplex into six congruent regions. This avoids a diagram-only identification and swapped vertex coordinates in one source.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Order chambers divide an equilateral simplex; inequality factorization, translated simplex, permutation symmetry supply the essential reduction.

## 2025 AIME I Problem 13: Expected regions from random chords

Two perpendicular diameters divide a disk into four quadrants. Add $25$ independent chords, each choosing uniformly a pair of distinct quadrants and then uniform endpoints within those quadrants. Find the expected number of regions.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_I_Problems/Problem_13) · MAA AMC.

### Solution

A chord crosses $1$ diameter when its quadrants are adjacent and $2$ when opposite, so the mean is $4/3$. For two random chords, condition on the first quadrant pair. If adjacent, among the six second pairs four share one quadrant (intersection chance $1/2$), one equals it (chance $1/2$), and one is disjoint (chance $0$): total $5/12$. If opposite, the disjoint pair instead intersects surely, giving $7/12$. Thus the unconditional probability is $(2/3)(5/12)+(1/3)(7/12)=17/36$. Each new chord adds one plus its number of crossings, almost surely. Expected regions are $4+25(1+4/3)+\binom{25}2(17/36)=204$.

**Answer:** 204.

**Methods:** linearity of expectation, random arrangements.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** Both sources inspected. Incremental regions and pair-crossing expectations agree. Source index 1 calls all 30 remaining quadrant-pair cases shared-one-quadrant cases, overlooking six identical pairs; these also have crossing probability one-half, so the result survives the inaccurate description.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Expected regions from random chords; the proof uses linearity of expectation, random arrangements.

## 2025 AIME I Problem 14: Two Ptolemy bounds share an equality point

A convex pentagon ABCDE has consecutive sides 14,7,24,13,26 and angles B=E=60 degrees. Find m+n+p if the least value of AX+BX+CX+DX+EX over planar points X is m+n $\sqrt{p}$, with p squarefree.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

The cosine law gives AC=7 $\sqrt{3}$,AD=13 $\sqrt{3}$, and angles BAC=DAE=30 degrees. In ACD, cos CAD=1/7 and sin CAD=4 $\sqrt{3}$/7, so cos BAE=cos(CAD+60 degrees)=−11/14. Hence BE squared=14 squared+26 squared−2(14)(26)(−11/14)=1444, giving BE=38. Ptolemy’s inequality in ABCX gives $AX+2CX\ge\sqrt3BX$; in AEDX it gives $AX+2DX\ge\sqrt3EX$. Adding and using BX+EX≥BE yields $f(X)\ge(1+\sqrt3/2)BE=38+19\sqrt3$. To verify equality constructively, take B=(0,0),E=(38,0) and A=(241/19,65 $\sqrt{3}$/19). The given 60-degree angles and convex order place $C=(109/19,-44\sqrt3/19)$ and $D=(553/19,-104\sqrt3/19)$. At the foot H=(241/19,0), the three distances AH,CH,DH are respectively 65,88,208 times $\sqrt{3}$/19, whose sum is 19 $\sqrt{3}$; also BH+HE=38. Thus the bound is attained, and the answer is 38+19+3=60.

**Answer:** 060.

**Methods:** Ptolemy inequality, geometric median, simultaneous equality construction.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All three alternatives inspected. A lower bound alone does not establish simultaneous cyclic equality. Explicit coordinates for the perpendicular-foot witness verify attainment and avoid assuming an optimizer lies on BE before proving it.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Two Ptolemy bounds share an equality point; Ptolemy inequality, geometric median, simultaneous equality construction supply the essential reduction.

## 2025 AIME II Problem 1: Recover one base and reuse its altitude

Collinear points A,B,C,D,E,F occur in order, with AC=26,BD=22,CE=31,DF=33,AF=73. Off-line point G has CG=40,DG=30. Find the area of BGE.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_II_Problems/Problem_1) · MAA AMC.

### Solution

We have CD=AF−AC−DF=73−26−33=14. Also BE=BD+CE−CD=22+31−14=39. Heron gives triangle CGD area $\sqrt{42\cdot28\cdot12\cdot2}=168$, so its altitude to the common line is 2(168)/14=24. Triangle BGE uses the same altitude and has area 39(24)/2=468.

**Answer:** 468.

**Methods:** collinear segment sums, Heron formula, shared altitude.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. Only CD and BE are needed; solving for all five adjacent gaps adds no information.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Recover one base and reuse its altitude; collinear segment sums, Heron formula, shared altitude supply the essential reduction.

## 2025 AIME II Problem 5: Read minor arcs from the medial triangle

Triangle ABC has angles A=84,B=60,C=36 degrees. D,E,F are the midpoints of BC,CA,AB. Their circumcircle meets BD,AE,AF again at G,H,J, in cyclic order G,D,E,H,J,F. Find arc DE+2 arc HJ+3 arc FG in degrees.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_II_Problems/Problem_5) · MAA AMC.

### Solution

The medial triangle has angle DFE=36 degrees, so the minor arc DE is 72 degrees. Because DF is parallel to AC and DG lies toward B on BC, angle FDG=36 degrees, giving arc FG=72 degrees. The arc from F through D to E is twice angle FHE; equivalently it is 360 minus the minor arc FE=360−2(84)=192 degrees. The two secants from A give $84=(192-\widehat{HJ})/2$, hence arc HJ=24 degrees. The requested total is 72+2(24)+3(72)=336.

**Answer:** 336.

**Methods:** medial triangle, inscribed angles, external secant angle.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. The specified cyclic order identifies the relevant minor arcs. The second source uses inconsistent labels for some medial angles; the direct angles at F and D avoid that ambiguity.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Read minor arcs from the medial triangle; medial triangle, inscribed angles, external secant angle supply the essential reduction.

## 2025 AIME II Problem 6: Equal triangle areas cancel the rectangle’s product

A radius-six circle centered A is internally tangent at B to a radius-fifteen circle. BC is a diameter of the larger circle, and AD is perpendicular to BC with D on that circle. A rectangle EFGH is inscribed in the smaller circle, EF perpendicular to BC, with C nearer GH and D nearer FG. If DGF and CHG have equal areas, write the rectangle area m/n reduced; find m+n.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

Put A=(0,0),B=(−6,0),C=(24,0). The larger center is(9,0), so D=(0,12), after reflecting vertically if necessary. Write the rectangle’s vertices as(±u,±v), with u,v>0 and u squared+v squared=36. The specified near sides are GH at x=u and FG at y=v. The triangle areas are $[DGF]=u(12-v)$ and $[CHG]=v(24-u)$. Equality cancels uv and gives u=2 v. Thus v squared=36/5 and the rectangle area is 4 uv=8 v squared=288/5, giving 293.

**Answer:** 293.

**Methods:** circle coordinates, centered rectangle, area cancellation.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All four alternatives inspected. The direct coordinates encode both near-side conditions. One ruler-based alternative is not a proof and also gives the wrong diagonal-square equation; the independent area equations establish the 2:1 ratio.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Equal triangle areas cancel the rectangle’s product; circle coordinates, centered rectangle, area cancellation supply the essential reduction.

## 2025 AIME II Problem 11: Equal-length perfect matchings on a polygon

Pair all vertices of a regular $24$-gon so that the twelve resulting chords have the same length. Count the pairings.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_II_Problems/Problem_11) · MAA AMC.

### Solution

Fix the cyclic step $d\in\{1,\ldots,12\}$. For $d<12$, the graph of chords of that length consists of $g=\gcd(24,d)$ cycles, each of length $24/g$. An odd cycle has no perfect matching; an even cycle has two, independently. The counts for $d=1,\ldots,11$ are $2,4,8,16,2,64,2,0,8,4,2$. For $d=12$, the diameters form one matching. Their sum is $113$.

**Answer:** 113.

**Methods:** cycle decomposition, perfect matchings.

**Verification:** The displayed mathematical count agrees with the archived answer.

**Source comparison:** No solution text occurs in the downloaded source record. Independent equal-chord graph decomposition gives 113.

**Archived entries inspected:** 0 of 0. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. Equal-length perfect matchings on a polygon; the proof uses cycle decomposition, perfect matchings.

## 2025 AIME II Problem 12: Equal-area fan triangles alternate their radial lengths

A nonconvex 11-gon A 1,...,A 11 has perimeter 20. For i=2 through 10, triangle Ai,A 1,A(i+1) has area 1 and cosine of its angle at A 1 equal 12/13. Write A 1 A 2+A 1 A 11 as $(m\sqrt n-p)/q$ in normalized squarefree form; find m+n+p+q.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

The common angle sine is 5/13. If consecutive radial lengths are r_i,r_(i+1), the area equation gives r_i r_(i+1)=26/5. Thus the ten radial lengths alternate between positive u,v, with uv=26/5. The nine outer edges all have squared length $u^2+v^2-2uv(12/13)=(u+v)^2-20$. Put S=u+v, which is also the requested sum. The perimeter equation is $S+9\sqrt{S^2-20}=20$. Squaring with S<20 gives $4S^2+2S-101=0$, whose positive root is $(9\sqrt5-1)/4$. It satisfies the original equation, so the answer is 9+5+1+4=19.

**Answer:** 019.

**Methods:** equal-area products, alternating recurrence, cosine law, perimeter equation.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** Both alternatives inspected. Only nine consecutive product equations are given; one source adds an unwarranted closing radial-product equation, though it happens to be consistent with the alternation. The authored proof uses precisely the nine specified triangles.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Equal-area fan triangles alternate their radial lengths; equal-area products, alternating recurrence, cosine law, perimeter equation supply the essential reduction.

## 2025 AIME II Problem 14: An equilateral triangle inside a right triangle controls area

Right triangle $ABC$ has $\angle A=90^\circ$ and $BC=38$. Interior points $K,L$ satisfy $AK=AL=BK=CL=KL=14$. The area of $BKLC$ is $n\sqrt3$; find $n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2025_AIME_II_Problems/Problem_14) · MAA AMC.

### Solution

Choose A=(0,0),B=(0,2 b),C=(2 a,0). Equal distances place K=(d,b),L=(a,c), with a,b,c,d>0. The length equations are $a^2+b^2=361$, $a^2+c^2=b^2+d^2=196$, and $(a-d)^2+(b-c)^2=196$. Consequently $a^2-d^2=b^2-c^2=165$, so x=a−d,y=b−c are positive. We have x squared+y squared=196 and $a=(x+165/x)/2$, $b=(y+165/y)/2$. Substituting into a squared+b squared=361 gives $1444=196+660+165^2\cdot196/(x^2y^2)$, hence xy=55 $\sqrt{3}$. Triangle AKL is equilateral, so its area is $(ab-cd)/2=49\sqrt3$. The shoelace formula for BKLC rearranges as $(ab-cd)/2+(a-d)(b-c)$, giving 49 $\sqrt{3}$+55 $\sqrt{3}$=104 $\sqrt{3}$. Thus n=104.

**Answer:** 104.

**Methods:** perpendicular bisectors, equilateral area, symmetric elimination, shoelace formula.

**Verification:** The exact derivation yields the archived answer.

**Source comparison:** All twelve alternatives inspected, including the incomplete entries and linked-diagram note. Many solve for every coordinate or rely on a particular drawing orientation. The positive differences a−d,b−c and their product determine the area directly without choosing either symmetric coordinate solution.

**Archived entries inspected:** 12 of 12. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. An equilateral triangle inside a right triangle controls area; perpendicular bisectors, equilateral area, symmetric elimination, shoelace formula supply the essential reduction.

## 2026 AIME I Problem 3: A sphere fitting inside a hemisphere

A hemisphere of radius 200 has its flat face on a horizontal disk of radius 200. Let $T$ be the possible tangency points on the disk for a sphere of radius 42 contained in the hemisphere. If $[T]/[\text{disk}]=p/q$ in lowest terms, find $p+q$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_I_Problems/Problem_3) · MAA AMC.

### Solution

At horizontal distance $\rho$ from the hemisphere center, the small sphere has center at height $42$. It lies in the upper half-space automatically, and lies in the radius-200 ball exactly when $\sqrt{\rho^2+42^2}+42\le200$. Thus $T$ is precisely the disk with squared radius $158^2-42^2=23200$. The area ratio is $23200/40000=29/50$, giving $79$.

**Answer:** 079.

**Methods:** sphere containment, center distances, area ratios.

**Verification:** The exact boundary identity is 23200+42²=158², and 23200/40000 reduces to 29/50.

**Source comparison:** Both alternatives read. A right-triangle calculation and a power-of-a-point construction agree; the containment inequality also proves that every point inside the boundary disk is feasible.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. A smaller sphere fits exactly when its center distance plus radius does not exceed the hemisphere radius.

## 2026 AIME I Problem 5: Two opposite rotations reduce to one cosine

Let $AB=1$. Rotate $A$ counterclockwise about $B$ through an acute angle $\theta$ to $A^{\prime}$, then rotate $B$ clockwise about $A^{\prime}$ through $\theta$ to $B^{\prime}$. Given $AB^{\prime}=4/3$, write $\cos\theta=m/n$ in lowest terms and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_I_Problems/Problem_5) · MAA AMC.

### Solution

Put $A=(0,0)$ and $B=(1,0)$, and abbreviate $c=\cos\theta$, $s=\sin\theta$. The first rotation gives $A^{\prime}=(1-c,-s)$. The vector from $A^{\prime}$ to $B$ is $(c,s)$, whose clockwise rotation is $(1,0)$, so $B^{\prime}=(2-c,-s)$. Consequently $16/9=(2-c)^2+s^2=5-4c$, giving $c=29/36$. This lies between zero and one, as required; the answer is $65$.

**Answer:** 065.

**Methods:** rotation vectors, Pythagorean identity.

**Verification:** Substitution yields 5−4(29/36)=16/9 and an acute angle.

**Source comparison:** All four alternatives read. The parallelogram and half-angle methods give the correct cosine. Source 3 equates a squared distance to 4/3 instead of 16/9; source 0 also describes a rotation around the wrong center in its final note. Explicit rotation vectors avoid both slips.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Composing two rotations gives a displacement whose squared length is a linear function of cos θ.

## 2026 AIME I Problem 10: Area of a triangle and its rotated interlacing

Triangle $ABC$ has $AB=13$, $BC=14$, $CA=15$. Rotate it about its circumcenter to $A^{\prime} B^{\prime} C^{\prime}$ so that $A^{\prime} C^{\prime}\perp BC$ and $A^{\prime},B$ lie on opposite sides of $B^{\prime} C^{\prime}$. Find the nearest integer to the area of hexagon $AA^{\prime} CC^{\prime} BB^{\prime}$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_I_Problems/Problem_10) · MAA AMC.

### Solution

Take $B=(0,0)$, $C=(14,0)$, $A=(5,12)$; the circumcenter is $O=(7,33/8)$. The two rotations making $A^{\prime} C^{\prime}$ vertical have cosine and sine $(4/5,-3/5)$ or $(-4/5,3/5)$. The former gives $A^{\prime}=(81/8,93/8)$, $B^{\prime}=(-43/40,201/40)$, $C^{\prime}=(81/8,-27/8)$. The oriented determinants against line $B^{\prime} C^{\prime}$ for $A^{\prime}$ and $B$ are $168$ and $-189/4$, so this is the required branch; the other gives $168$ and $651/4$. Split the hexagon along $A^{\prime} B$. Quadrilateral $A^{\prime} CC^{\prime} B$ has perpendicular diagonals of lengths 15 and 14, so area 105. Quadrilateral $AA^{\prime} BB^{\prime}$ has diagonals $AB,A^{\prime} B^{\prime}$ of length 13 and included-angle sine $3/5$, so area $13^2(3/5)/2=507/10$. Total area is $1557/10$, whose nearest integer is 156.

**Answer:** 156.

**Methods:** rotation matrices, branch selection, quadrilateral diagonal area.

**Verification:** Exact rational rotation and shoelace calculation independently give area 1557/10; determinant signs select the required rotation.

**Source comparison:** All four alternatives read. Coordinate rotation, circumcenter triangles, and quadrilateral decomposition agree. The clean alternate statement accidentally loses the primes in A′C′; the main statement and all solutions retain the intended perpendicular pair. Several source displays and some vertex orders are corrupted; the explicit branch determinants and diagonal-area calculation supply a complete check.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. The required circumcenter rotation and a quadrilateral diagonal-area identity determine an interlacing hexagon area.

## 2026 AIME I Problem 12: Sphere radii form an affine function

In a plane, $AB=6$, $AC=4$, and $\angle BAC=90^\circ$. Reflect the centroid of $ABC$ across $BC$ to obtain $D$. Spheres of radii $1,2,3,r$ touch the plane at $A,B,C,D$ on the same side. All also touch a second plane on the same side of it. Find numerator plus denominator of $r$ in lowest terms.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_I_Problems/Problem_12) · MAA AMC.

### Solution

Use $A=(0,0)$, $B=(6,0)$, $C=(0,4)$ in the plane $z=0$. Orient a unit normal to the second plane so that its signed distance from every center equals the corresponding radius. Its equation yields $ax+by+(c-1)z+d=0$ for all centers. Since the second plane is distinct, $c\ne1$; thus the radius $z$ is an affine function of its contact point. The first three radii determine $z=1+x/6+y/2$. The centroid is $(2,4/3)$, and reflection across $2x+3y=12$ gives $D=(42/13,124/39)$. Hence $r=1+7/13+62/39=122/39$, giving 161. Existence is verified by the second plane $6x+18y-13z+36=0$: its normal has length 23 and its signed distance from each center equals its radius.

**Answer:** 161.

**Methods:** signed plane distances, affine interpolation, reflection.

**Verification:** Exact reflection gives D=(42/13,124/39); substituting all four centers into the normalized second-plane equation returns their radii.

**Source comparison:** All four alternatives read. Source 0 asserts coplanarity of the centers without explanation, source 1 proves it implicitly through signed distances, source 2 invokes linearity informally, and source 3 uses the intersection line of the tangent planes. The affine equation establishes the common missing justification and the explicit second plane verifies existence.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Equal signed distances to two tangent planes make sphere radii affine in their contact points; reflection locates the fourth input.

## 2026 AIME I Problem 14: Closure controls an equiangular pentagon

An equiangular pentagon has side-length squares summing to 308 and diagonal-length squares summing to 800. Its perimeter squared is $m\sqrt n$, where $m,n$ are positive integers and $n$ is squarefree. Find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_I_Problems/Problem_14) · MAA AMC.

### Solution

Let $S=\sum a_i^2=308$, $J=\sum a_i a_{i+1}$, $K=\sum a_i a_{i+2}$, with cyclic indices, and put $\phi=(1+\sqrt5)/2$. Since the angle between successive side vectors is $72^\circ$, summing the squared diagonal lengths gives $800=2S+J/\phi$, so $J=184\phi$. The five side vectors sum to zero. Taking the squared norm and grouping adjacent and nonadjacent pairs gives $0=S+J/\phi-\phi K$, because $2\cos72^\circ=1/\phi$ and $2\cos144^\circ=-\phi$. Thus $K=492/\phi$. Therefore the perimeter squared is $S+2J+2K=308+368\phi+984(\phi-1)=676\sqrt5$, giving 681.

**Answer:** 681.

**Methods:** vector closure, golden-ratio angles, cyclic quadratic sums.

**Verification:** Exact arithmetic in Q(√5) verifies J=184φ, K=492/φ and perimeter squared 676√5.

**Source comparison:** All five alternatives read. The extended-side constructions and complex-vector closure lead to the same two equations for adjacent and nonadjacent products. Source 2 guesses the missing rational cancellation from the requested answer form and is not a proof. The closure identity determines it without guessing.

**Archived entries inspected:** 5 of 5. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Equiangular side-vector closure relates adjacent and nonadjacent products, determining the perimeter from two quadratic sums.

## 2026 AIME I Problem 15: Five rectangular cell loops

A cell loop consists of the boundary cells of an axis-aligned rectangle with both dimensions at least two. Count partitions of a $10\times10$ board into five cell loops.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_I_Problems/Problem_15) · MAA AMC.

### Solution

For an $H\times W$ board with $H\ge W$, take the two cell diagonals $D=\{(i,i):1\le i\le W\}$ and $E=\{(H+1-i,i):1\le i\le W\}$. A rectangular boundary meets either in at most two cells. Thus a partition into $W/2$ loops forces every loop to meet each diagonal twice. Let the upper-left corner loop have dimensions $r\times c$. Its interior is a union of whole loops, so its two diagonal counts are equal: $\min(r,c)-2=r+c-H-2$. (The second count is nonnegative because the corner loop meets $E$ twice.) Hence $\max(r,c)=H$. A tall-board corner loop therefore spans its full height; a square-board corner loop spans at least one side. Its other dimension is even.

Let $T(a,b)$ count partitions of a $2a\times2b$ board into $b$ loops, where $a>b$. A corner loop of width $2k$ leaves independent rectangles $2(a-1)\times2(k-1)$ and $2a\times2(b-k)$, both using their minimum loop counts. Therefore $T(a,b)=\sum_{k=1}^b T(a-1,k-1)T(a,b-k)$, with empty-width count $1$. Induction using the Catalan recurrence gives $T(a,b)=C_b$.

For the square count $S_n$, a full outer-square loop contributes $S_{n-1}$. A proper full-height corner loop contributes $\sum_{k=1}^{n-1}C_{k-1}C_{n-k}$; full-width loops contribute the same. Thus $S_n=S_{n-1}+2(C_n-C_{n-1})$, and $S_0=1$ gives $S_n=2C_n-1$. Finally $S_5=2\binom{10}5/6-1=83$.

**Answer:** 083.

**Methods:** Catalan numbers, diagonal invariants, structural decomposition.

**Verification:** Independent exact-cover enumeration, without using the corner-loop lemma, gives 1,3,9,27,83 for square side lengths 2,4,6,8,10. The 10-by-10 count visits 3053 occupied-cell states.

**Source comparison:** All three archived solutions were read; their structural arguments have gaps or false claims. The independent two-diagonal corner-loop lemma proves the Catalan formula rigorously. See the detailed Catalan-loop addendum.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** combinatorics, geometry. A two-diagonal restriction on rectangular cell loops leads to a Catalan recurrence for minimum-loop tilings.

## 2026 AIME II Problem 3: An indented pentagon gives one residue class

A simple nonconvex pentagon $ABCDE$ has interior angles $A=E=90^\circ$, $B=D=45^\circ$, with $DE<AB$, $AE=20$, $BC=14\sqrt2$. Vertices $B,C,D$ lie on one side of $AE$. How many integer lengths $AB<2026$ make its area a multiple of 16?

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_II_Problems/Problem_3) · MAA AMC.

### Solution

Put $A=(0,0)$, $E=(0,20)$ and $B=(b,0)$. The angle conditions force $C=(b-14,14)$ and $D=(b-8,20)$: the other possible direction of $BC$ would give $C=(b-14,-14)$ and $DE=b+20$, contradicting $DE<AB$. The same-side condition is exactly $b>14$. These coordinates give a simple pentagon with the required reflex angle at $C$ for every $b>14$. Its area by the shoelace formula is $20b-164$. This is divisible by 16 exactly when $b\equiv1\pmod4$. The permitted integers are $17,21,\ldots,2025$, numbering $(2025-17)/4+1=503$.

**Answer:** 503.

**Methods:** angle-constrained coordinates, polygon area, congruence counting.

**Verification:** Exact enumeration of integers 15 through 2025 confirms 503 with (20 b−164) divisible by 16; the coordinate determinants verify the stated side lengths and turns.

**Source comparison:** The sole stored alternative read. Its rectangle-and-two-triangles calculation is correct, but it leaves the geometric branch and the positivity of the horizontal offset implicit. Coordinates justify both before counting the residue class.

**Archived entries inspected:** 1 of 1. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory. The angle data fix an indented polygon shape up to one integer length, and its area imposes a residue class.

## 2026 AIME II Problem 6: Normal distances from a point to a parabola

Find the sum of all radii of circles centered at $(4,39)$ that are tangent to the parabola $2y=x^2-8x+12$ at at least one point.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_II_Problems/Problem_6) · MAA AMC.

### Solution

Parametrize the parabola by $(x,y)=(4+u,u^2/2-2)$. Its squared distance from the given center is $F(u)=u^2+(u^2/2-41)^2=u^4/4-40u^2+1681$. A circle is tangent at this regular point exactly when its radius vector is perpendicular to the tangent vector, equivalently $F^{\prime}(u)=u(u^2-80)=0$. At $u=0$ the radius is 41; at $u=\pm\sqrt{80}$ it is 9. Both are positive and the tangent condition is satisfied, so the requested sum is $41+9=50$.

**Answer:** 050.

**Methods:** normal-line tangency, squared-distance critical points, quartic factorization.

**Verification:** F′ factors as u(u²−80), with F(0)=1681 and F(±√80)=81; these exhaust the stationary distances.

**Source comparison:** All four alternatives read. The normal-slope and derivative methods are valid. A discriminant in y alone misses the vertex tangency unless treated separately. Source 3 estimates a radius and assumes it is an integer because of the contest format; that is not a proof. The parameter derivative lists all tangencies exactly.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra. Tangency is a stationary-distance condition along the parabola, producing all admissible radii from one factored quartic derivative.

## 2026 AIME II Problem 8: An integer isosceles triangle with a tiny incenter triangle

In an isosceles triangle $ABC$, $AB=BC$ and $I$ is the incenter. The perimeters of $ABC$ and $AIC$ have ratio $125:6$. All side lengths of both triangles are integers. Find the least possible $AB$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_II_Problems/Problem_8) · MAA AMC.

### Solution

Write $AC=2x$, $AB=L$, and $AI=CI=u$. The altitude from $B$ contains $I$, so $\cos A=x/L$ and $\cos(A/2)=x/u$. With $t=u/x>1$, the double-angle formula gives $L/x=t^2/(2-t^2)$, where $t<\sqrt2$. The perimeter ratio becomes $2/((2-t^2)(t+1))=125/6$, or $(t-7/5)(t^2+12t/5+34/25)=0$. The quadratic factor is positive for $t>0$, so $t=7/5$ and $L/x=49$. If $AC=b$ is an integer, then $AI=7b/10$ forces $10\mid b$; also $L=49b/2$. Hence $L\ge245$, attained at side lengths $245,245,10$ and $AI=CI=7$. These lengths satisfy the ratio and the angle identity, verifying attainment.

**Answer:** 245.

**Methods:** half-angle identity, unique positive root, integrality scaling.

**Verification:** The cubic factors exactly as shown; for base 10 the altitude is 100√6, the inradius is 2√6, and AI²=5²+(2√6)²=49. Perimeters 500 and 24 have ratio 125:6.

**Source comparison:** All three alternatives read. Source 0 introduces an integer substitution after normalization without proving it and then guesses the root. Source 1 mislabels the base as BC but contains the intended half-angle reduction. Source 2 finds a working example without proving minimality. The factored cubic proves the unique shape, and divisibility by 10 then proves the minimum.

**Archived entries inspected:** 3 of 3. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, algebra, number_theory. A half-angle relation determines a unique isosceles shape, and denominator divisibility gives its smallest integral scale.

## 2026 AIME II Problem 10: An angle bisector and tangent secants

In triangle $ABC$, $AB=200$, $AC=225$, and $AD$ bisects angle $A$, with $D$ on $BC$. A circle through $A$ is tangent to $BC$ at $D$ and meets $AB,AC$ again at $E,F$ on those segments. If $AE,AF,BD,CD$ are positive integers, find the greatest possible $BC$. An alternate version asks for the sum of all possible values.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_II_Problems/Problem_10) · MAA AMC.

### Solution

The angle-bisector theorem and integrality give $BD=8m$, $CD=9m$ for a positive integer $m$. Tangent-secant power gives $BE=BD^2/200=8m^2/25$ and $CF=CD^2/225=9m^2/25$. Integrality forces $5\mid m$; write $m=5k$. Then $AE=200-8k^2$, $AF=225-9k^2$, and $BC=85k$. Positivity gives $k=1,2,3,4$. Conversely each of these gives triangle sides $200,225,85k$, satisfying the strict triangle inequalities. The unique circle through $A$ tangent to $BC$ at its bisector foot $D$ exists: its center lies on the perpendicular at $D$, and the equal-distance equation to $A,D$ determines a positive radius. Its second secant intersections have the computed positive lengths less than 200 and 225, so they lie on the required segments. Hence the possible bases are $85,170,255,340$. Their maximum is 340; their sum, requested in the alternate version, is 850.

**Answer:** 340.

**Methods:** angle bisector theorem, tangent-secant power, divisibility, existence converse.

**Verification:** Exact enumeration of the angle-bisector factor yields k=1,2,3,4; the corresponding bases are 85,170,255,340 and their sum is 850.

**Source comparison:** All four alternatives read. Source 0 explicitly notes an international sum variant. Source 1 initially lets the common factor be real and then infers integer divisibility without stating why; BD,CD integral and coprime ratio 8:9 supply that step. The completed converse checks triangle existence and segment intersections for every candidate. The main maximum answer 340 and alternate sum answer 850 are retained separately.

**Archived entries inspected:** 4 of 4. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry, number_theory. The angle-bisector ratio and tangent-secant powers turn four integrality conditions into one bounded integer parameter.

## 2026 AIME II Problem 12: The centers of a tetrahedron with two unequal opposite edges

A tetrahedron has two faces with side lengths $5\sqrt{10},5\sqrt{10},10$ and two with $5\sqrt{10},5\sqrt{10},18$. Its circumcenter and incenter are $S,R$. Write $RS=m/n$ in lowest terms and find $m+n$.

[Published problem and solutions](https://artofproblemsolving.com/wiki/index.php/2026_AIME_II_Problems/Problem_12) · MAA AMC.

### Solution

The edges of lengths 10 and 18 are opposite, since no face contains both. Set their endpoints to $A=(-5,0,0)$, $B=(5,0,0)$ and $C=(0,9,12)$, $D=(0,-9,12)$; all four remaining edges then have squared length $25+81+144=250$. The two reflection symmetries put both centers on the $z$-axis. Write $S=(0,0,s)$. Equal vertex distances give $25+s^2=81+(12-s)^2$, hence $s=25/3$. For $R=(0,0,r)$ inside the tetrahedron, distances to representative face planes $4y-3z=0$ and $12x-5z+60=0$ are $3r/5$ and $(60-5r)/13$. Equality gives $r=75/16$, lying between 0 and 12; symmetry supplies the other two tangencies. Consequently $RS=25/3-75/16=175/48$, giving 223.

**Answer:** 223.

**Methods:** tetrahedral symmetry, circumcenter equations, signed face distances.

**Verification:** Exact squared edge lengths and plane-normal lengths verify the model; circumcenter height 25/3 and incenter height 75/16 give reduced distance 175/48.

**Source comparison:** Both alternatives read. A coordinate model and two perpendicular cross-sections give the same centers. The second source calls a midpoint separation EF despite using M,N elsewhere; its numerical value 12 is correct. Explicit opposite-edge placement makes the symmetry and plane-distance calculations self-contained.

**Archived entries inspected:** 2 of 2. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.

**Subject classification:** geometry. Opposite unequal edges determine a symmetric tetrahedron whose two centers follow from vertex and face distances.
