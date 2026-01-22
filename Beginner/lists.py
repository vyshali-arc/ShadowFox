justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

# 1. Calculate the number of members in the Justice League
print("Number of members:", len(justice_league))
print("\n----------------------------------------\n")
# 2. Batman recruited Batgirl and Nightwing as new members
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl and Nightwing:", justice_league)
print("\n----------------------------------------\n")
# 3. Wonder Woman is now the leader of the Justice League
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman the leader:", justice_league)
print("\n----------------------------------------\n")
# 4. Aquaman and Flash are having conflicts.
justice_league.remove("Green Lantern")
aquaman_index = justice_league.index("Aquaman")
flash_index = justice_league.index("Flash")
insert_position = min(aquaman_index, flash_index) + 1
justice_league.insert(insert_position, "Green Lantern")
print("After resolving Aquaman and Flash conflict:", justice_league)
print("\n----------------------------------------\n")
# 5. Superman decides to assemble a new team
justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]
print("New Justice League team:", justice_league)
print("\n----------------------------------------\n")
# 6. Sort the Justice League alphabetically
justice_league.sort()
print("Alphabetically sorted Justice League:", justice_league)
# Hero at 0th index becomes the new leader
print("New Leader:", justice_league[0])
