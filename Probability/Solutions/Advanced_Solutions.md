## Solutions to the Advanced Exercises

### Probability Game
The probability of 10, 20 and 30 points is $\frac{4}{7}  , \frac{2}{7}  and \frac{1}{7}$  respectively.
$E(Points)=\frac{4}{7}\cdot10+\frac{2}{7}\cdot20+\frac{1}{7}\cdot30=15.7$

### Tennis Match
$P(1st|2nd)=\frac{P(1st\wedge 2nd)}{P(2nd)}=\frac{3/5\cdot 9/10}{3/5\cdot 9/10+2/5\cdot 1/2}=\frac{27}{37} $

### Measles
$P(M|R)=\frac{P(R|M)P(M)}{P(R|M)P(M)+P(R|F)P(F)}=\frac{0.95\cdot0.10}{0.95\cdot0.10+0.08\cdot0.90}\approx0.57$

### Mice
Both parents can be considered as $Bb$ (The order of the genes is ignored for both, and $Bb$ treated as the same as $bB$). The mouse in question is a black mouse, so it could have either $Bb$ or $BB$.

The prior probability of the mouse being black is:

$P(Black)=1-P(Brown)=1-\frac{1}{2}\cdot\frac{1}{2}=0.75 $

For the mouse to be homozygous, it must have B from both of the parents. The probability of this is:

$P(BB|Black)=\frac{P(Black|BB)P(BB)}{P(Black)}=\frac{1\cdot0.25}{0.75}=\frac{1}{3} $

For the mouse to be heterozygous, it must have B from one parent and b from the other. The probability of this is:

$P(Bb|Black)=\frac{P(Black|Bb)P(Bb)}{P(Black)}=\frac{1\cdot0.5}{0.75}=\frac{2}{3} $

Now this black mouse has mated with a brown mouse ($bb$). This has resulted in 7 black offspring, which must clearly all be $Bb$ and they must have received a $B$ from the black mouse. All of these following probabilities are taken in the world where the fact the parent mouse is black is known.

$P(BB|7black)=\frac{P(7black|BB)P(BB)}{P(7black)}=\frac{1\cdot1/3}{P(7black)}$ 

But what is the prior probability of having 7 black offspring?

$P(7black)=P(BB)P(7black|BB)+P(Bb)P(7black|Bb)=\frac{1}{3}\cdot1+\frac{2}{3}\cdot\frac{1}{2^7}=\frac{65}{192} $

$Hence P(BB|7black)=\frac{64}{65}\approx0.985 $

### Game Day
It depends. With no further information, it does not but if $J$ and $S$ are independent given $W$, i.e., $P(J|W,S)=P(J|W)$, then this suffices.

[Move back to Medium Probability Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/Probability/Medium.md)

*If the page doesn't render correctly, reload it. That should fix it.*
