import random

def game():
    print("You are playing the game...")

    score = random.randint(1, 61)

    # Fetch the high score
    try:
        with open("hiscore.txt") as f:
            high_score = f.read().strip()
            if high_score == "":
                high_score = 0
            else:
                high_score = int(high_score)
    except FileNotFoundError:
        high_score = 0

    print(f"Your score: {score}")

    if score > high_score:
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
        print("New high score!")

    return score

game()
