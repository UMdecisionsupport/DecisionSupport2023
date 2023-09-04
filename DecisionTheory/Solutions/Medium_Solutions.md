## Solutions to the Medium Exercises

### Pacman Network
E: G is a value the ghost can choose so it should be a rectangle. From the ghost's perspective, P, X and Y are all random variables so should be ovals. U should be a diamond. All of the variables are involved in the calculation of U, so there should be an arrow from each. Y's distribution is influenced by X so there should be an arrow from X to Y. This leaves a single correct solution.

### Racetrack
#### Part A
- Placing no bet at all will give a profit of $0.
- EU(Belle) = 0.7 · 1 + 0.3 · −1 = $0.40
- EU(Jeb) = 0.1 · 10 + 0.9 · −1 = $0.10
Hence, you should bet on Belle as this has the best expected utility.

#### Part B
When also considering insurance, the expected utilities from the first part remain unchanged. For the second
part, we now need to calculate the utilities when accepting the insurance.

EU(Belle) = 0.7 · 2.5 + 0.3 · 1 = $2.05
EU(Jeb) = 0.1 · 7 + 0.9 · 1 = $1.60
The best options is now to accept the insurance and bet on Belle.

### Skiing
#### Part A
Yes, with an EU of 0 vs -2.

#### Part B
f you knew your leg was broken, then $E(Ski)=0.1\cdot50+0.9\cdot -50=-40$ and $E(\neg Ski)=-10$, so you would choose not to ski and have an expected utility of -10. If you knew your leg was not broken, then $E(Ski)=0.1\cdot100+0.9\cdot0=10$  and $E(\neg Ski)=0$, so you would choose to ski and have an expected utility of 10. Using the probability of each of these scenarios, have $EU(withinfo)=0.2\cdot-10+0.8\cdot10=6$. Hence the value of the information is 6-0=6.

#### Part C
If you knew you would win, then $E(Ski)=0.2\cdot50+0.8\cdot100=90$  and $E(\neg Ski)=0.2\cdot-10+0.8\cdot0=-2$, so you would choose to ski with an expected utility of 90. If you knew you would lose, $E(Ski)=0.2\cdot-50+0.8\cdot0=-10$ and $E(\neg Ski)=0.2\cdot-10+0.8\cdot0=-2$, so you would choose not to ski with an expected utility of -2. Using the probability of each of these scenarios, have $EU(withinfo)=0.1\cdot90+0.9\cdot-2=7.2$. Hence the value of the information is 7.2-0=7.2.



[Move back to Beginner Decision Theory Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/DecisionTheory/Beginner.md)

[Move forward to Advanced Decision Theory Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/DecisionTheory/Advanced.md)

*If the page doesn't render correctly, reload it. That should fix it.*
