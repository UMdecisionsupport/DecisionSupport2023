## Beginner Decision Theory Exercises

### Existence of Utility Theorem
Complete the following statements by replacing $\text\[...\]$ with the correct symbols.

Existence of Utility Theorem: There exists a function U such that when $A\prec B$, $U(\text\[...\])>U(\text\[...\])$. \\
And when $A\sim B$, $U(A) \text{\[...\]}  U(B)$.

### True or False
Select the correct answer for each statement.
- The agent’s preferences are captured by a reward function.
- The value of perfect information is always non-negative.
- Decision nodes are represented as rectangles.
- To calculate the Value of Perfect Information, it is necessary to know the previous expected utility.

### Bike Ride
You are preparing to go for a bike ride and are trying to decide whether to use your thin road tyres or your thicker, knobbier tyres. You know from previous experience that your road tyres are more likely to go flat during a ride. There’s a 40% chance your road tyres will go flat but only a 10% chance that the thicker tyres will go flat. Because of the risk of a flat, you also have to decide whether or not to bring your tools along on the ride (a pump, tyre levers and a puncture kit). These tools will weigh you down.
The advantage of the thin road tyres is that you can ride much faster. The table below gives the utilities for these variables:

Bring tools| Flat tyre |	Road tyres |	Satisfaction|
-----------|-----------|-------------|--------------|
T	         |T	         |T	           |50            |
T	         |T	         |F	           |40            |
T	         |F	         |T	           |75            |
T	         |F	         |F	           |65            |
F	         |T	         |T	           |0             |
F	         |T	         |F	           |0             |
F	         |F          |T	           |100           |
F	         |F	         |F	           |75            |

- What is the optimal policy?
- What is the expected utility?

### Pacman

<img src="https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/images/pacman.png" width="450" height="250">

After years of battles between the ghosts and Pacman, the ghosts challenge Pacman to a winner-take-all showdown, and the game is a coin flip. Pacman has a decision to make: whether to accept the challenge (accept) or decline (decline). If the coin comes out heads ($+h$) Pacman wins. If the coin comes out tails ($-h$), the ghosts win. No matter what decision Pacman makes, the outcome of the coin is revealed.

Compute EU(accept) and EU(decline). From this, select the optimal decision.

### Robot Mailman
A robot must choose its route to pick up the mail. There is a short route and long route. On the short route, the robot might slip and fall. The can put on pads. Pads won’t change the probability of an accident. However, if an accident happens, pads will reduce the damage. Unfortunately, the pads add weight and slow the robot down. The robot would like to pick up the mail as quickly as possible while minimizing the damage caused by an accident.

- When an accident does **NOT** happen, which of the following is true? 
  - (A) The robot prefers not wearing pads to wearing pads. 
  - (B) The robot prefers the long route over the short route. 
  - (C) Both (A) and (B) are true. 
  - (D) Both (A) and (B) are false.

- What shape should each of the nodes be?
  - Accident	
  - Route	
  - Pads	
  - Utility

- Which arrows (if any) should definitely be included between the following pairs?
  - Accident and Route	
  - Accident and	Pads	
  - Accident	and Utility	
  - Route	and Pads	
  - Route and	Utility	
  - Pads and Utility


[View Solutions for Beginner Decision Theory](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/DecisionTheory/Solutions/Beginner_Solutions.md)

[Move forward to Medium Decision Theory Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/DecisionTheory/Medium.md)

*If the page doesn't render correctly, reload it. That should fix it.*
