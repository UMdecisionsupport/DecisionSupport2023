## Medium MDPs Exercises

### Pacman 
Pacman is using MDPs to maximize his expected utility. In each environment:
- Pacman has the standard actions \{North, East, South, West\} unless blocked by an outer wall.
- There is a reward of 1 point when eating the dot.
- The game ends when the dot is eaten.

Consider a Pacman level that begins with cherries in locations D and F. Landing on a grid position with cherries is worth 5 points and then the cherries at that position disappear. There is still one dot, worth 1 point. The game only ends when the dot is eaten. The states are simply the grid locations. Let there be no discount ($\gamma$ = 1) and a living reward of -1 (applied at each time step).

<img src="https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/images/pacmanmdp2.png" width="150" height="100">


- How many different states need a policy to be assigned? (Count the existence or not of each cherry as inducing a separate state. Assume the Pacman could have started at any square.)
- What is the optimal policy if the Pacman is at E, and both cherries are still present?
- What is the optimal policy if the Pacman is at A, and both cherries are still present?

### Flying Pacman
Pacman is in a 1-dimensional grid with squares labeled 0 through to n, inclusive, as shown below:

<img src="https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/images/flyingpacman.png" width="350" height="100">

Pacman’s goal is to reach square n as cheaply as possible. From state n, there are no more actions or rewards available.

At any given state, if Pacman is not in n, Pacman has two actions to choose from:
- Run: Pacman deterministically advances to the next state (i.e. from state i to state i + 1). This action costs Pacman \$1.
- Fly: With probability p, Pacman directly reaches state n. With probability 1 - p, Pacman is stuck in the same state. This action costs Pacman \$2

Fill in the blank boxes below to define the MDP. i represents an arbitrary state in the range \{0, … , n - 1\}.

| s | a | s' | P(s,a,s')| R(s,a)|
|---|---|----|----------|-------|
| i |Run| i+1|    ?     |   ?   | 
| i |Fly|  i |    ?     |   ?   | 
| i |Fly|  ? |    ?     |   ?   | 




[View Solutions for Medium MDPs](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/MDPs/Solutions/Medium_Solutions.md)

[Move back to Beginner MDPs Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/MDPs/Beginner.md)

[Move forward to Advanced MDPs Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/MDPs/Advanced.md)

*If the page doesn't render correctly, reload it. That should fix it.*
