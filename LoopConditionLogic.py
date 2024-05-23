# Task 1: Loop Condition Exploration
# Write a while loop with a condition that will never be false (an infinite loop).
#  Inside the loop, print a statement. Then, use a break statement to exit the loop 
# after 5 iterations.

score = 0
while True:
    print(score + 1)
    score += 1
    if score == 5:
        break










# Task 2: Conditional Exit
# Modify the infinite loop from Task 1 to include a condition that will eventually be true
# and remove the break statement. The loop should terminate naturally once the condition is met.

score1 = 6
while score1 !=1:
    print(score1 - 1)
    score1 -= 1