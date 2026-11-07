skateboard_colors = {}
i = 0

while i < 4:
    name = input(f"enter the name of skater {i}: ")
    color = input("enter the skateboard color: ")
    skateboard_colors[name] = color
    i += 1

print(skateboard_colors)
