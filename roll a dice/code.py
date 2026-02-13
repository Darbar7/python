
import random

def roll_dice(num_dice=1):
    return [random.randint(1, 6) for _ in range(num_dice)]

def show_dice(results):
    faces = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}
    display = " ".join(faces[d] for d in results)
    total = sum(results)
    print(f"🎲 You rolled: {display} (Total: {total})")

print("🎲 Dice Game!")
roll_history = []

while True:
    try:
        num = int(input("\nRoll 1 or 2 dice? (1/2): "))
        if num not in [1, 2]:
            print("❌ Choose 1 or 2 only!")
            continue
    except ValueError:
        print("❌ Enter number 1 or 2!")
        continue
    
    result = roll_dice(num)
    show_dice(result)
    
    roll_history.append(result)
    roll_history = roll_history[-3:]
    if len(roll_history) > 1:
        print(f"History: {roll_history}")
    
    if input("Roll again? (y/n): ").lower() != 'y':
        print("Thanks for playing! 🎲")
        break