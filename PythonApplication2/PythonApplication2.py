import random
import time

level = 1
correct_streak = 0

while True:
    sequence_length = 5 + (level - 1)  
    seq = [random.randint(0, 9) for z in range(sequence_length)]
    
    print(f"Level {level}")
    print("Memorize these numbers")
    print(' '.join(map(str, seq)))
    time.sleep(6)
    print("\n" * 50)
    guess = input("input your guess (or type 'quit' to stop): \n\n\n").split()

    if 'quit' in guess:
        break

    if guess == list(map(str, seq)):
        print("Correct!\n")
        correct_streak += 1
        if correct_streak == 2:
            level += 1
            correct_streak = 0
            print(f"Congratz level up! Now at Level {level}\n")
    else:
        print("Incorrect! These were tge numbers:", ' '.join(map(str, seq)), "\n")
        correct_streak = 0  