import random
# PART 1: Dice Roll Simulation
print("DICE ROLL SIMULATION\n")
six_count = 0
for i in range(20):
    dice = random.randint(1, 6)
    print(f"Roll {i + 1}: {dice}")

    if dice == 6:
        six_count += 1
print("\nNumber of times 6 appeared:", six_count)
print("\n----------------------------------------\n")
# PART 2: Workout Program

print("WORKOUT PROGRAM\n")

total_jump_jacks = 0

for set_number in range(1, 11):
    print(f"Set {set_number}: Do 10 Jumping Jacks")
    total_jump_jacks += 10

    tired = input("Are you tired? (yes/no): ").strip().lower()

    if tired == "yes":
        skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()

        if skip == "yes":
            print("\nWorkout stopped early.")
            break
        else:
            print("Take a short break and continue!")

print("\nTotal Jumping Jacks completed:", total_jump_jacks)
