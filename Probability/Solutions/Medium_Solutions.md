## Solutions to the Medium Exercises

### High School
- $B=\{b}$ so $P(B)=P(b)=0.27$
- $M=\{b,h,a,o}$ so $P(M) = P(b)+P(h)+P(a)+P(o)=1-P(w)=0.49$

### Independence
No, the percentage of people quitting smoking changes depending on whether or not they wear seat belts.

### Rafting
0.15

### College
- $P(FM|H)=\frac{P(FM\wedge H)}{P(H)}=\frac{0.05}{0.3}=\frac{1}{6}\approx0.17 $
- $P(H|FM)=\frac{P(H\wedge FM)}{P(FM)}=\frac{0.05}{0.2}=\frac{1}{4}=0.25 $

### Counters
- The probability of selecting a red counter from the first bag is 3/7 and from the second 2/7. Multiplying these together gives a probability of 2 red counters of 6/49.
- For 1 red counter, need to consider the probability of getting a red counter from the first bag and a blue from the second, or the reverse. So $\frac{3}{7}\cdot\frac{5}{7}+\frac{4}{7}\cdot\frac{2}{7} = \frac{23}{49}$.

### Engineers
- If E and F were independent, then $P(E|F)=P(E)$. Here, that would require 0.15=0.25  so the events are not independent.
- $P(E\wedge F)=P(E|F)P(F)=0.15\cdot 0.54=0.081$

### Emails
First to define some events:
- $A$: event that an email is detected as spam
- $B$: event that an email is spam
- $\neg B$: event that an email is not spam

From the question:
- $P(B)=P(\neg B)=0.5 $
- $P(A|B)=0.99 $
- $P(A|\neg B)=0.05 $

Hence:

$P(\neg B|A) = \frac{P(A|\neg B)P(\neg B)}{(P(A|B)P(B) + P(A|\neg B)P(\neg B))}$

$P(B^c|A) = \frac{0.05\times 0.5}{(0.99\times 0.5 + 0.05\times 0.5)}=\frac{5}{104}\approx0.05$

### Fruit Machine
- There is only one permutation of the wheels that will give the big payout. There are $4^3 = 64$ possible results of the fruit machine. So the probability is $1/64 = 0.015625$.
- Of the 64 possible permutations:
  - 3 payout from all 3 of the slots matching.
  - 3 pay out from having 2 Cherries followed by 1 of something else.
  - 3x3 = 9 pay out from having 1 Cherry followed by 2 with anything else.
  - That leaves 64 − 16 = 48 with a return of 0.
  - Expected return = $(1\cdot20+1\cdot15+1\cdot5+1\cdot3+3\cdot2+9\cdot1+48\cdot0)/64=58/64=0.906$. Hence 90.6% expected payback percentage.
- As seen in the first part of the solution, 16 of the 64 possible permutations delivers a win. So 0.25 probability of a win.

### Senators
- $P(M|D) = \frac{P(M\wedge D)}{P(D)} = \frac{30}{44}\approx 0.68$
-	$P(D|M)= \frac{P(D\wedge M)}{P(M)} = \frac{30}{80}\approx 0.38$ 
- $P(F|R)= \frac{P(F\wedge R)}{P(R)} = \frac{6}{54}\approx 0.11$ 
- $P(R|F)= \frac{P(R\wedge F)}{P(F)} = \frac{6}{20}\approx0.30$ 

[Move back to Beginner Probability Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/Probability/Beginner.md)

[Move forward to Advanced Probability Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/Probability/Advanced.md)

*If the page doesn't render correctly, reload it. That should fix it.*
