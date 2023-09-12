## Beginner RL Exercises

### Definitions
Decide whether the following statements are true or false.
1. When we run Q-learning on a fixed dataset of (state, action, next state, reward) tuples once, it will always converge to the optimal Q-values. 
2. Q-learning is a model-based reinforcement learning method. 

### Commuting
In the directed graph below, we formulate the problem of commuting in the Bay Area as a simple MDP, where the cities (nodes) represent the states, and the arrows represent possible actions. We will use the direction of the arrows in the graph, i.e., "up", "down", "left", and "right" to refer to the actions.

<img src="https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/images/Bay1.png" width="300" height="150">


Let’s assume that the agent does not always succeed in every action, and we want to build an estimate of the transition function $\hat{P}$ and reward function $\hat{R}$ from data (for model-based reinforcement learning). The agent follows some policy $\pi$ to collect a dataset of (current state, action, next state, reward) tuples, as listed below.

<img src="https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/images/Bay2.png" width="300" height="150">

1. What is $\hat{P}(San Francisco, up, Oakland)$?
2. What is $\hat{R}(San Francisco, up, Oakland)$?



[View Solutions for Beginner RL](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/RL/Solutions/Beginner_Solutions.md)

[Move forward to Medium RL Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/RL/Medium.md)

*If the page doesn't render correctly, reload it. That should fix it.*
