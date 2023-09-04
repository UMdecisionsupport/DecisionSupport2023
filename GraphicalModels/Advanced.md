## Advanced Graphical Models Exercises

### Help the Farmer
<img src="https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/images/farmer.png" width="750" height="300">

Chris is a farmer. He has a hen in his barn, and it will lay at most one egg per day. Chris collects data and discovers conditions that influence his hen to lay eggs on a certain day, which he describes above. For a single hen, variables O, W, S, H , and E denote the event of an outbreak (O), sunny weather (W), sickness (S), happiness (H), and egg being laid (E). If an event does occur, we denote it with a $+$, otherwise $-$, e.g., $+o$ denotes an outbreak having occurred and $-o$ denotes no outbreak occurred.

#### Inference
Which of the following equations are equivalent to $P(+e|+w,-o)$?
- $\alpha P(+w)P(-o)\sum_{s'\in dom_S}(P(s'|-o,+w)\sum_{h'\in dom_H}(P(h'|+w)P(+e|s',h')))$
- $\alpha P(+w)\sum_{h'\in dom_H}(P(h'|+w)\sum_{s'\in dom_S}(P(s'|+w,-o)P(+e|s',h')P(-o))) $
- $\alpha P(+w)P(-o)\sum_{s'\in dom_S}(P(s'|-o,+w)P(+h|+w)P(+e|s',+h))+P(+w)P(-o)\sum_{s'\in dom_S}(P(s'|-o,+w)P(-h|+w)P(+e|s',-h)) $

#### Sampling I
Chris wants to estimate the probability that the hen lays an egg given it’s good weather and the hen is not sick, e.g., $P(+e|+w,-s)$. Suppose we receive the samples: 

$(-o, +w, -s, -h, +e), (-o, +w, -s, +h, -e), (+o, +w, -s, -h, -e) $

- Chris decides to amend the usual likelihood weighting method. Instead of weighting by the whole evidence, he weights each sample only with $P(-s| + w, O)$, i.e. he omits weighting by $P(+w)$. Does Chris’ method results in the correct answer for the query $P(+e| + w, -s)$?
- Using likelihood weighting with the samples listed above, what is the probability the hen lays an egg given it’s good weather and the hen is not sick, i.e., $P(+e|+w, -s)$?

#### Sampling II
Chris uses Gibbs sampling to sample tuples of $(O, W, S, H, E)$.

- As a step in our Gibbs sampling, suppose we currently have the assignment of $(-o, -w, +s, +h, +e)$.  Then we resample the “sickness” variable, i.e., $S$. What is the probability that the next assignment is the same, i.e., $(−o, −w, +s, +h, +e)$?
- What will be the most observed tuple of $(O, W, S, H, E)$ if we keep running Gibbs sampling for a long time?

### Sampling I
<img src="https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/images/sampling.png" width="750" height="200">

Consider the above Bayes Net, where we have observed that $D = +d$.
### Part A
Below is a list of samples that were collected using prior sampling. What samples would be rejected by rejection sampling?
- $+a, -b, +c, -d $
- $+a, -b, +c, +d $
- $-a, +b, -c, -d $
- $+a, +b, +c, +d$

#### Part B
You now receive a set of samples shown below:
- $+a, +b, +c, +d $
- $-a, -b, -c, +d $
- $+a, +b, +c, +d $
- $+a, -b, -c, +d $
- $-a, -b, -c, +d$
Estimate the probability $P(+a|+d)$ if these new samples were collected using:
- rejection sampling
- likelihood weighting

### Sampling II
<img src="https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/images/sampling2.png" width="550" height="500">

Consider the above Bayes Net, where we have observed that $D = +d$.

[View Solutions for Advanced Graphical Models](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/GraphicalModels/Solutions/Advanced_Solutions.md)

[Move back to Medium Graphical Models Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/GraphicalModels/Medium.md)

*If the page doesn't render correctly, reload it. That should fix it.*
