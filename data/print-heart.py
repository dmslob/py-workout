import random

def draw_binary_heart(width=30, height=15):
    # Adjusting the aspect ratio because terminal characters are taller than they are wide
    for y in range(height, -height, -1):
        line = ""
        for x in range(-width, width):
            # Normalizing coordinates to fit the heart formula
            nx = x / (width / 1.5)
            ny = y / (height / 1.5)

            # The heart equation
            if (nx**2 + ny**2 - 1)**3 - nx**2 * ny**3 <= 0:
                # ANSI escape code for Red (\033[91m)
                # Choosing a random 0 or 1
                char = random.choice(["0", "1"])
                line += f"\033[91m{char}\033[0m"
            else:
                line += " "
        print(line)

if __name__ == "__main__":
    draw_binary_heart()