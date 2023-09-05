## Medium Game Theory Exercises

### Business Deals
Consider the game below, played by two firms $i = 1, 2$, each of them simultaneously and independently selecting to adopt either technology A or B. Technology A is regarded as superior by both firms, yielding a payoff of 2 to
each firm if they both adopt it, while the adoption of technology B by both firms only entails a payoff of 1. Importantly, if firms do not adopt the same technology, both obtain a payoff of zero. This can be explained because, even if firm $i$ adopts technology A, such a technology is worthless if firm $i$ cannot exchange files, new products and practices with the other firm. 

Find the Nash Equilibria and Pareto Optima for this game.

|     | A   | B   |
|-----|-----|-----|
| A   | 2,2 | 0,0 |
| B   | 0,0 | 1,1 |

### Duopoly
Two countries produce oil and each can choose between producing 2 millions barrels/day or 4 millions barrels/day. The total output will be then 4, 6, or 8 millions barrels/day and the corresponding price will be $20, $12, $7 per barrel (a decreasing price reflects basic law of supply and demand).

Find the Nash Equilibria and Pareto Optima for this game.

|     | 2M  | 4M  |
|-----|-----|-----|
| 2M  |40,40|24,48|
| 4M  |48,24|28,28|

### Joint Activities
Each player, Alice (A) and Bob (B) has a preferred location (football or cinema) but the more important consideration for both is that they show up at the same location.

|        |Football| Cinema |
|--------|--------|--------|
|Football| 3,2    | 1,1    |
| Cinema | 0,0    | 2,3    |


Now construct a variant with the following characteristics:
- Bob’s payoffs from the different outcomes remains as before.
- Alice still prefers football to the cinema but the more important consideration for her now is that she avoids Bob.

Reuse the payoffs 0, 1, 2 and 3 but put them in the cells appropriate for the new situation:

|        |Football| Cinema |
|--------|--------|--------|
|Football|        |        |
| Cinema |        |        |

Does this new game have a Nash equilibrium?

### Prisoner's Dilemma

|        |Testify | Refuse |
|--------|--------|--------|
|Testify |  x,x   |  -6,0  |
|Refuse  |  0,-6  |  -1,-1 |

Which value(s) of x will result in the top left being a Pareto optimum in this Prisoners’ Dilemma game?
	- x ≥ -6
	- -6 ≤ x < -1
	- -1 ≤ x < 0
	- x ≥ -1
	- x ≥ 0

Which value(s) of x will result in the top left being a Nash equilibrium?
- -6 ≤ x < -1
- x ≥ -1
- x ≥ -6
- x ≥ 0
- -1 ≤ x < 0

### Snowdrift II
I will give to Robert and Chelsea each a gift worth $40 if I receive $30 in cash. Their options are to either pay the fee or to not pay the fee knowing that if both of them decide to pay, then they will share the fee and pay $15 each.

Find all the Nash equilibria and Pareto optima for the Snowdrift game.

|       | Pay   |Not Pay|
|-------|-------|-------|
|Pay	| 25,25 | 10,40 |
|Not Pay| 40,10 |  0,0  |


### Ultimatum II
Consider the following experiment where $100 are handed to Robert and he is given the task to split the amount of money between himself and Chelsea any
way he wants. Then Chelsea has the option to accept the deal and take the money offered, or to refuse in which case both go empty-handed. Here, Robert has two options: offer a fair split, say 60-40, or offer a unequal split, 85-15. Chelsea also has two options, accepting any offer or accepting only the fair offer.

Find all the Nash equilibria and Pareto optima for the Ultimatum game.

|            |Accept Any|Accept Fair|
|-------     |-------   |-------    |
|Fair Split  | 60,40  	|  60,40    |
|Unfair Split| 85,15    |   0,0     |


[View Solutions for Medium Game Theory](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/GameTheory/Solutions/Medium_Solutions.md)

[Move back to Beginner Game Theory Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/GameTheory/Beginner.md)

[Move forward to Advanced Game Theory Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/GameTheory/Advanced.md)

*If the page doesn't render correctly, reload it. That should fix it.*
