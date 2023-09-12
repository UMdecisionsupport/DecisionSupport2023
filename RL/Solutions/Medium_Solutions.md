## Solutions to the Medium Exercises

### Grid Learning I 
Q(F,down) is updated to -0.5 since $Q(F,down)=0.5\cdot Q(F,down)+0.5(-1+0.9\cdot\max\limits_{a'}Q(I,a'))=0.5\cdot0+0.5(-1+0.9\cdot0)=-0.5$.

If your answer was incorrect, you can try repeating the process for now following the (s,a,s') of (I, down, L). This should update Q(I, down) to 44.5.

### Grid Learning II

1. State H
2. State L
3. State H
4. Exit


The optimal first step from A is to move down, thus moving to state D. The optimal step from D is also to move down, resulting in state H. These optimal moves can be seen by looking at the largest Q value in each column.

[Move back to Beginner RL Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/RL/Beginner.md)

[Move forward to Advanced RL Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/RL/Advanced.md)

*If the page doesn't render correctly, reload it. That should fix it.*
