## Beginner MDPs Exercises

### Discount Factor
A large discount factor $\gamma$ (approaching 1) on an MDP means that the agent emphasizes long-term rewards. True or False?

### Pacman

Pacman is using MDPs to maximize his expected utility. In each environment:
- Pacman has the standard actions \{North, East, South, West\} unless blocked by an outer wall.
- There is a reward of 1 point when eating the dot (for example, in the grid below, R(C, South, F ) = 1).
- The game ends when the dot is eaten.

Consider a the following grid where there is a single food pellet in the bottom right corner (F ). The discount factor is 0.5. The states are simply the grid locations. There is no explicit penalty for taking more steps.

<img src="https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/images/pacmanmdp1.png" width="150" height="100">


1. What is the optimal policy for each state?
2. What is the optimal value for the state of being in the upper left corner (A)?



[View Solutions for Beginner MDPs](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/MDPs/Solutions/Beginner_Solutions.md)

[Move forward to Medium MDPs Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/MDPs/Medium.md)

*If the page doesn't render correctly, reload it. That should fix it.*
