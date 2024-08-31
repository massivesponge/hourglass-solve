"""
Hourglass Stats
12600 per level (after 100) (LINEAR LEVELING)

Loss = 700

Win (with 0 streak) = 4200
Win (with 1 streak) = 5675
Win (with 2 streak) = 5190
Win (with 3 streak) = 5688
Win (with >3 streak) = 6600

Streak 1 Lower = 1100
Streak 2 Lower = 2640
Streak 3 Lower = 4680
Streak 4 Lower = 7800 + 3000 * (streak - 4)
"""

# Find optimal Streak to lower at based on winrate

import random

simulations = 1000000

def get_lower_xp(streak):
    if streak == 1:
        return 1100
    elif streak == 2:
        return 2640
    elif streak == 3:
        return 4680
    else:
        return 7800 + 3000 * (streak - 4)
    
def get_win_xp(streak):
    if streak == 0:
        return 4200
    elif streak == 1:
        return 5675
    elif streak == 2:
        return 5190
    elif streak == 3:
        return 5688
    else:
        return 6600

def simulate(streak_goal, winrate):
    streak = 0
    xp = 0
    sim = 0
    while sim < simulations:
        win = random.random() < winrate

        if win:
            xp += get_win_xp(streak)
            streak += 1
        else:
            xp += 700
            streak = 0

        if streak >= streak_goal:
            xp += get_lower_xp(streak)
            streak = 0

        sim += 1

    return xp

def find_optimal_streak(winrate):
    optimal_streak = 0
    best_xp = 0
    for i in range(1,14):
        xp = simulate(i, winrate)
        if xp > best_xp:
            optimal_streak = i
            best_xp = xp

        print(f"Streak: {i}, XP: {xp}")

    return optimal_streak

# Plotting the best streak for different winrates

import matplotlib.pyplot as plt

winrates = [0.1, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
streaks = range(1,20)

for winrate in winrates:
    print(f"Simulating Winrate: {winrate}")
    xp = [simulate(i, winrate) for i in streaks]
    best_streak = streaks[xp.index(max(xp))]
    plt.plot(streaks, xp, label=f"Winrate: {winrate}")
    plt.scatter(best_streak, max(xp), color='red')
    plt.text(best_streak, max(xp), best_streak, fontsize=9)

plt.xlabel("Streak")
plt.ylabel("XP")
plt.legend()
plt.show()
