# I SOLVED HOURGLASS: BEST HOURGLASS STREAK FOUND
## Outline
- Intro
- The Problem
- The Info we have
- The Solution
- How to winrate
- How to use the graph
- Other considerations
    - Why you should never lower
    - Why you should lower at 4

## Video Script

### Intro

I don't want to waste your time, so here's the final graph. If you want to know how to use this graph, keep watching.

Ok, so you've been lied to.

Other streamers and youtubers have said that the best streak is 2 or 4 or 5 or never lower...

In reality, its more complicated than that. Today, im going to solve it, using brute force computer programming.

### The Problem

Here's the issue, when you are on a high streak, the higher you go, the larger the reward. But, the higher you go, the more likely you are to lose it all.
This means that there is no single best streak, but rather a best streak for your winrate. (I'll explain how to find your winrate later)

### The Info we have
From level 0 to 100, the levels you gain are faster at the start, and slower at the end, but beyond 100, the levels are linear.
So, instead of talking about levels, im going to explain in terms of xp.
Quick disclaimer, I personally didnt find these numbers, I found them from DavidSOT's video, linked in description.

Every level requires 12,600 xp, (after level 100)

a Loss gives 700 xp

a Win (with 0 streak) = 4200 xp
a Win (with 1 streak) = 5675 xp
a Win (with 2 streak) = 5190 xp
a Win (with 3 streak) = 5688 xp
a Win (with >= 4 streak) = 6600 xp

Lowering a 1 = 1100 xp
Lowering a 2 = 2640 xp
Lowering a 3 = 4680 xp
Lowering a 4 = 7800 + 3000 * (streak - 4) xp

So if you are paying attention youll notice that you gain more xp from being beyond a 4 streak.
And this increases the higher you go.

### The Solution

Now because I cant be bothered to find some sort of formula, I'll need to brute force this by simulating hourglass games.
My idea is to simulate some number of games with different winrates and different streak goals (the point we lower at)

we'll try simulating say 1 billion games?

So I made some basic if statements to calculate the xp we get for a streak or for a win at a streak, and a function to simulate a session where we play a couple million games and record the xp we get.

basically we pick a random number between 0 and 1, and if its less than our winrate, we win, and if its more, we lose.
if we reach our streak goal, we lower, and if we lose, we reset the streak.
at the end of our billion games, we record the xp we got, and compare it with other winrates and streak goals.

then I plotted the results into a graph, marking the streak with highest xp we got for each winrate.

my code was slow, so I asked ai to optimize it, and it did it wrong so I fixed it and now its good.

but one problem with this solution is that it doesnt take into account the time it takes for an hourglass game or a lower.
so I made the estimate that an hourglass game can be between 2 minutes and like 30+ but usually will take 8 minutes, plus 2 minutes of queuing. This tracks bc generally nessie and I will be on a 6 streak in an hour. I also estimated that it would take 10 minutes to lower, as sometime you are further from the island and sometimes you have flags. Also note that we are ignoring flags in all calculations as they are too random (you might get 10 Grade V's or 1 Grade I in a session), treat them like a bonus.

And with these time estimations I remade my simulation to take into account the time it takes to play a game or lower a streak.

Running this simulation, I produced this graph, showing the best streak for each winrate, and the relation between streak goal and xp gained.

### How to use the graph

So, how do you use this graph?

well, find ur winrate and look at the graph, and find the highest point for your winrate, and that is the best streak for you.

but how do you find your winrate?

### How to winrate

To find your winrate, go to ship's log, milestones, pirate milestones, pick either The Guardian or The Servant
get your total battles completed.
get your battles won by seeking
get your battles won by repelling
add the two together
divide the sum by the total battles completed
thats ur winrate
if you want it to be more accurate, add other factions totals together and do the same thing.

### Other considerations

If you are going for a commendation requiring you to get to a champion streak 50 times, you should simply lower at 4 every time, as this will get the commendation the fastest. (but will slow down ur xp gain)

If you want to improve and xp is an afterthought, you should never lower, as this will let you dive quickly and get more practice in, improving faster, increasing your winrate, and increasing your xp gain.

### Conclusion

Thanks for watching, i'll link a github repo with my code in the description, and if you have any questions or ammendments, feel free to comment below.