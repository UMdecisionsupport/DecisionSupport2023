## Advanced RL Exercises

### Room Learning

Let's consider a situation in which our robot is placed inside a building that has a floorplan like that shown in the following image. 

<img src="https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/images/rooms1.gif" width="300" height="150">

We can characterize this space as an MDP, where each state represents one room in the building (or outside, e.g., room 5) and where the agent can transition between rooms by moving either north, south, east, or west. The agent cannot stay in the same state from time step to time step, except once it is outside. 

<img src="https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/images/rooms2.png" width="300" height="150">

We can specify the reward function as depicted in the following diagram, where the agent receives a reward when it transitions outside from either room 1 or room 4. Additionally, the agent continues reaping rewards once it's already outside every time step. 

<img src="https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/images/rooms3.png" width="300" height="150">

Our robot's goal in this world is to get outside (room 5) from it's starting position in room 2. Let the Q-values be initialised to the following:

|        | A | B | C | D | E | F | G | H | I | J | K | L |
|--------|---|---|---|---|---|---|---|---|---|---|---|---|
|rm_0    | 0 |-10| 0 | 0 | 0 | 0 |-10| 10| 0 | 25| 50|100|

\begin{center}
\begin{tabular}{|c|c|c|c|c|} 
 \hline
  & North & South & East & West \\ 
 \hline
 $rm_0$ & -1 & 0 & -1 & -1 \\ 
 \hline
 $rm_1$ & 0 & 0 & -1 & -1 \\ 
 \hline
 $rm_2$ & -1 & -1 & -1 & 0 \\ 
 \hline
 $rm_3$ & 0 & -1 & 0 & 0 \\ 
 \hline
 $rm_4$ & 0 & 0 & 0 & -1 \\ 
 \hline
 $rm_5$ & 0 & 0 & 0 & 0 \\ 
 \hline
\end{tabular}
\end{center}

Your goal in this exercise is to update according to the Q-learning algorithm. In this exercise we will make the following assumptions:

\begin{itemize}
    \item $\alpha=1$ so the update rule is thus $Q(s_t,a_t)\leftarrow r_t + \gamma\cdot\max_{a}Q(s_{t+1},a)$
    \item the discount factor $\gamma=0.8$
    \item Transitions are always made successfully (it's not possible for our agent to fail in its attempt to take an action)
\end{itemize}

Here is an action trajectory that you'll have your robot agent follow through the environment (assume that your agent always starts in room 2 at the beginning of a trajectory). For each action within the trajectory, update according to the Q-learning algorithm.

Trajectory: west, west, south, north 






[View Solutions for Advanced RL](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/RL/Solutions/Advanced_Solutions.md)

[Move back to Medium RL Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/RL/Medium.md)

*If the page doesn't render correctly, reload it. That should fix it.*
