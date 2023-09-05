## Medium Decision Theory Exercises

### Pacman Network

A <img src="https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/images/p1.png" width="150" height="250">
B <img src="https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/images/p2.png" width="150" height="250">
C <img src="https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/images/p3.png" width="150" height="250">
D <img src="https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/images/p4.png" width="150" height="250">
E <img src="https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/images/p5.png" width="150" height="250">
F <img src="https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/images/p6.png" width="150" height="250">

The ghost chooses a number $G$ and Pacman randomly chooses a number $P$ at the same time. A computer generates a number $X\sim U(0,10)$ and then another number $Y\sim U(0,X)$. The utility is $f(G,P,X,Y)$ for a fixed function $f$. Select the decision network(s) that can correctly represent the problem for the ghost.

### Racetrack
You go to the racetrack.
You can:
- Decline to place any bets at all.
- Bet on Belle. It costs $1 to place a bet; you will be paid $2 if she wins (for a net profit of $1).
- Bet on Jeb. It costs $1 to place a bet; you will be paid $11 if he wins (for a net profit of $10).

You believe that Belle has probability 0.7 of winning and that Jeb has probability 0.1 of winning.

#### Part A
Your goal is to maximize the expected value of your actions. What, if any, bet should you place, and what is your expected value (profit)?

#### Part B
Someone comes and offers you gambler’s anti-insurance. If you agree to it: 
- They pay you $2 up front.
- You agree to pay them 50% of any winnings (so $0.50 if Belle wins or $5 if Jeb wins).

What is the best action to take now?

### Skiing
You’re an Olympic skier. In practice today, you fell down and hurt your ankle. Based on the results of an x-ray, the doctor thinks that it’s broken with probability 0.2. So, the question is, should you ski in the race tomorrow?
If you ski, you think you’ll win with probability 0.1. If your leg is broken and you ski on it, then you’ll damage it further. So, your utilities are as follows: 
- if you win the race and your leg isn’t broken, +100;
- if you win and your leg is broken, +50;
- if you lose and your leg isn’t broken 0;
- if you lose and your leg is broken -50.

If you don’t ski, then
- if your leg is broken your utility is -10,
- and if it isn’t, it’s 0.

You might be able to gather some more information about the state of your leg by having more tests. You might be able to gather more information about whether you’ll win the race by talking to your coach or the TV sports commentators.

#### Part A
Based on this information, should you ski in the race tomorrow?

#### Part B
Compute the expected value of perfect information about the state of your leg. 

#### Part C
Compute the expected value of perfect information about whether you’ll win the race. 


[View Solutions for Medium Decision Theory](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/DecisionTheory/Solutions/Medium_Solutions.md)

[Move back to Beginner Decision Theory Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/DecisionTheory/Beginner.md)

[Move forward to Advanced Decision Theory Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/DecisionTheory/Advanced.md)

*If the page doesn't render correctly, reload it. That should fix it.*
