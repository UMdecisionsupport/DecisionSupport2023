## Solutions to the Medium Exercises

### Pacman 
There are 16 separate states to consider. For A, C, and E, there are then four possible combinations of whether or not 1 or both cherries are still present. D and F each provide two as only the other cherry needs to be considered. B does not introduce any states to assign policies to as the game would be over.

East and South respectively. For both, getting both of the cherries will give the best reward. For the first, it is better to get the cherry in F first as going back for it would use more steps. For the second, the dot must be avoided in order to be able to then collect the cherries.

### Flying Pacman

| s | a | s' | P(s,a,s')| R(s,a)|
|---|---|----|----------|-------|
| i |Run| i+1|    1     |   -1  | 
| i |Fly|  i |   1-p    |   -2  | 
| i |Fly|  n |    p     |   -2  | 


When run is selected, Pacman will move from i to i+1. This is certain, so has a probability of 1. The cost is -1. When fly is selected, the state s' is uncertain and this is represented with p. The cost is always the same at -2.



[Move back to Beginner MDPs Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/MDPs/Beginner.md)

[Move forward to Advanced MDPs Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/MDPs/Advanced.md)

*If the page doesn't render correctly, reload it. That should fix it.*
