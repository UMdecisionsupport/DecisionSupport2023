## Advanced Graphical Models Exercises

### Farmer Inference
<img src="https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/images/farmer.png" width="750" height="450">

Which of the following equations are equivalent to P(+e|+w,-o)?
\alpha P(+w)P(-o)\sum_{s'\in dom_S}(P(s'|-o,+w)\sum_{h'\in dom_H}(P(h'|+w)P(+e|s',h'))) 
\alpha P(+w)\sum_{h'\in dom_H}(P(h'|+w)\sum_{s'\in dom_S}(P(s'|+w,-o)P(+e|s',h')P(-o))) 
\alpha P(+w)P(-o)\sum_{s'\in dom_S}(P(s'|-o,+w)P(+h|+w)P(+e|s',+h))+P(+w)P(-o)\sum_{s'\in dom_S}(P(s'|-o,+w)P(-h|+w)P(+e|s',-h)) 


[View Solutions for Advanced Graphical Models](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/GraphicalModels/Solutions/Advanced_Solutions.md)

[Move back to Medium Graphical Models Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/GraphicalModels/Medium.md)

*If the page doesn't render correctly, reload it. That should fix it.*
