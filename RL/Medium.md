## Medium RL Exercises

### Grid Learning
See the grid below. The state space is determined by the letters in each square. The agent can take any one of four actions; up, down, right and left.

<img src="https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/images/grid.png" width="350" height="100">

Start with the following Q-values for each of the states, for all of the possible actions.

|        | A | B | C | D | E | F | G | H | I | J | K | L |
|--------|---|---|---|---|---|---|---|---|---|---|---|---|
|Q_0(s,a)| 0 |-10| 0 | 0 | 0 | 0 |-10| 10| 0 | 25| 50|100|


Operate with the following instructions:
1. A discount factor of $\gamma=0.9$.
2. A terminal reward is received after leaving a terminal state. The only action available in a terminal state is to exit.
3. A living reward of -1 for all other transitions.
4. A learning rate of $\alpha=0.5$.

Using $Q(s,a) \leftarrow (1-\alpha)Q(s,a) + \alpha[r + \gamma\max\limits_{a'}Q(s',a')]$, update any Q(s,a) values which would be changed by following the (s,a,s') of (F, down, I).

Which Q(s,a) is updated? What is the new value?










[View Solutions for Medium RL](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/RL/Solutions/Medium_Solutions.md)

[Move back to Beginner RL Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/RL/Beginner.md)

[Move forward to Advanced RL Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/RL/Advanced.md)

*If the page doesn't render correctly, reload it. That should fix it.*
