## Medium MDPs Exercises

### Pacman 
Pacman is using MDPs to maximize his expected utility. In each environment:
- Pacman has the standard actions \{North, East, South, West\} unless blocked by an outer wall.
- There is a reward of 1 point when eating the dot.
- The game ends when the dot is eaten.

Consider a Pacman level that begins with cherries in locations D and F. Landing on a grid position with cherries is worth 5 points and then the cherries at that position disappear. There is still one dot, worth 1 point. The game only ends when the dot is eaten. The states are simply the grid locations. Let there be no discount ( = 1) and a living reward of -1 (applied at each time step).

\includegraphics[width=0.2\textwidth]{pacmanmdp2.png}

\begin{enumerate}
    \item How many different states need a policy to be assigned? (Count the existence or not of each cherry as inducing a separate state. Assume the Pacman could have started at any square.)
    \item What is the optimal policy if the Pacman is at E, and both cherries are still present?
    \item What is the optimal policy if the Pacman is at A, and both cherries are still present?
\end{enumerate}


[View Solutions for Medium MDPs](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/MDPs/Solutions/Medium_Solutions.md)

[Move back to Beginner MDPs Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/MDPs/Beginner.md)

[Move forward to Advanced MDPs Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/MDPs/Advanced.md)

*If the page doesn't render correctly, reload it. That should fix it.*
