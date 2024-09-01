import numpy as np
import matplotlib.pyplot as plt
from numba import jit

SIMULATIONS = 1_000_000_000

GAME_TIME_COST = 10 # minutes average
LOWER_TIME_COST = 10 # minutes average

@jit(nopython=True)
def simulate(streak_goal, winrate):
    LOWER_XP = np.array([0, 1100, 2640, 4680] + [7800 + 3000 * (i - 4) for i in range(4, 20)])
    WIN_XP = np.array([4200, 4675, 5190, 5688] + [6600] * 16)
    
    streak = 0
    xp = 0

    sim_time = 0

    while sim_time < SIMULATIONS:
        win = np.random.random() < winrate
        sim_time += GAME_TIME_COST
        if win:
            xp += WIN_XP[min(streak, 19)]
            streak += 1
        else:
            xp += 700
            streak = 0
        if streak >= streak_goal:
            xp += LOWER_XP[min(streak, 19)]
            streak = 0
            sim_time += LOWER_TIME_COST
    return xp

def find_optimal_streak(winrate):
    return max(range(1, 20), key=lambda i: simulate(i, winrate))

winrates = [0.1, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
streaks = range(1, 20)

plt.figure(figsize=(12, 8))
for winrate in winrates:
    print(f"Simulating Winrate: {winrate}")
    xp = [simulate(i, winrate) for i in streaks]
    best_streak = streaks[np.argmax(xp)]
    plt.plot(streaks, xp, label=f"Winrate: {winrate}")
    plt.scatter(best_streak, max(xp), color='red')
    plt.text(best_streak, max(xp), str(best_streak), fontsize=9)

plt.xlabel("Streak")
plt.ylabel("XP")
plt.legend()
plt.title("XP vs Streak for Different Winrates")
plt.show()
