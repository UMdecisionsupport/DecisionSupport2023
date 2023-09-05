## Solutions to the Advanced Exercises

Let $w_1$ and $c_2$ indicate a walk on the first day and cleaning on the second day respectively. $s_t$ and $r_t$ refer to sun or rain on the respective days.

The work for the first 4 parts needs to be done together to then calculate $P(w_1,c_2)$.

$P(s_1,s_2|w_1,c_2)=\frac{P(s_1,s_2,w_1,c_2)}{P(w_1,c_2)}=\frac{0.4\cdot0.6\cdot0.6\cdot0.1}{P(w_1,c_2)}=\frac{0.0144}{P(w_1,c_2)}$ 

$P(s_1,r_2|w_1,c_2)=\frac{P(s_1,r_2,w_1,c_2)}{P(w_1,c_2)}=\frac{0.4\cdot0.6\cdot0.4\cdot0.5}{P(w_1,c_2)}=\frac{0.048}{P(w_1,c_2)}$ 

$P(r_1,s_2|w_1,c_2)=\frac{P(r_1,s_2,w_1,c_2)}{P(w_1,c_2)}=\frac{0.6\cdot0.1\cdot0.3\cdot0.1}{P(w_1,c_2)}=\frac{0.0018}{P(w_1,c_2)}$ 

$P(r_1,r_2|w_1,c_2)=\frac{P(r_1,r_2,w_1,c_2)}{P(w_1,c_2)}=\frac{0.6\cdot0.1\cdot0.7\cdot0.5}{P(w_1,c_2)}=\frac{0.021}{P(w_1,c_2)}$ 

It is now clear that Sunny, Rainy is the most likely sequence. However, the calculation of the actual probabilities is not yet complete.

$P(w_1,c_2)=0.0144+0.048+0.0018+0.021=0.0852$ 

Substituting this into the equations above gives the correct answers:

|Yesterday|	Today	| Probability |
|---------|-------|-------------|
|Sunny    | Sunny	| 0.17        |
|Sunny	  | Rainy	| 0.56        |
|Rainy	  | Sunny	| 0.02        |
|Rainy	  | Rainy	| 0.25        |

[Move back to Medium HMMs Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/HMMs/Medium.md)

*If the page doesn't render correctly, reload it. That should fix it.*
