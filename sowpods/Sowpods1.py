import random as ran

def get_word():
    file = "sowpods.txt"
    words = []
    with open(file,"r") as f:
        words = f.readlines()

    return ran.choice(words).strip()


if __name__ == "__main__":
    print(get_word())