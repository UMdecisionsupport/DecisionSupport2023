## Solutions to the Beginner Exercises


### Existence of Utility Theorem
Complete the following statements by replacing $\text\[...\]$ with the correct symbols..
Existence of Utility Theorem: There exists a function U such that when $A\prec B$, $U(A)>U(B)$. And when $A\sim B$, $U(A) =  U(B)$.

### True or False
- The agent’s preferences are captured by a reward function. **False**
- The value of perfect information is always non-negative. **True**
- Decision nodes are represented as rectangles. **True**
- To calculate the Value of Perfect Information, it is necessary to know the previous expected utility. **True**

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
$EU(accept)=P(+h)U(+h,accept)+P(-h)U(-h,accept)=0.5\cdot100+0.5\cdot-100=0 $

$EU(decline)=P(+h)U(+h,decline)+P(-h)U(-h,decline)=0.5\cdot-30+0.5\cdot50=10 $

So the optimal decision is to decline the offer.

### Robot Mailman
- When an accident does **NOT** happen, A is true.

- What shape should each of the nodes be?
  - Accident: oval
  - Route: rectangle
  - Pads: rectangle
  - Utility: diamond

- Which arrows (if any) should definitely be included between the following pairs?
  - Accident and Route: right to left
  - Accident and	Pads: none
  - Accident	and Utility: left to right
  - Route	and Pads: none
  - Route and	Utility: left to right
  - Pads and Utility: left to right

[Move forward to Medium Decision Theory Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/DecisionTheory/Medium.md)

*If the page doesn't render correctly, reload it. That should fix it.*
