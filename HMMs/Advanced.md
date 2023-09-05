## Advanced HMMs Exercises

### Guessing game
Consider that there are two close friends, Alice and Bob, who live far away from each other but talk over the phone every day and discuss what they did. They decide to play a guessing game where Alice would try to guess the weather, based only on what Bob told her he was doing that day.
For simplicity, let’s imagine Bob’s behavior is pretty limited. He can do one of three things during the day – walk in the park, go shopping, or clean his apartment.  Additionally, his actions fully depend on the weather on the given day. The weather will also have only two states – “rainy” or “sunny”.
Since Alice has an idea of the weather in Bob’s area we can also translate her knowledge into probabilities:
If yesterday was sunny, there is a 0.6 probability that today is sunny again and a 0.4 probability that it will rain. Likewise, if yesterday was raining, there is a 0.7 probability that it rains again and a 0.3 probability that it is sunny. And since the sequence has to start from somewhere she says that there is a 0.6 probability of starting with a rainy day and 0.4 for starting with a sunny day.

Consider Bob went for a walk yesterday and cleaned his apartment today. What is the most likely sequence of weather for the two days? 

[View Solutions for Advanced HMMs](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/HMMs/Solutions/Advanced_Solutions.md)

[Move back to Medium HMMs Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/HMMs/Medium.md)

*If the page doesn't render correctly, reload it. That should fix it.*
