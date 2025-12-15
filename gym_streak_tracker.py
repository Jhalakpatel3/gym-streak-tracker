# Gym Streak Tracker Micro Project

attendance = list(map(int, input(
    "Enter gym attendance (1 for went, 0 for missed) separated by space:\n"
).split()))

current_streak = 0
longest_streak = 0

for day in attendance:
    if day == 1:
        current_streak += 1
        longest_streak = max(longest_streak, current_streak)
    else:
        current_streak = 0

print("Current Streak:", current_streak)
print("Longest Streak:", longest_streak)
