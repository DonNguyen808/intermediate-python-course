import random

def main():
  dice_rolls = 2
  dice_sums = 0

  for i in range(0,dice_rolls):
    roll = random.randint(1, 6)
    dice_sums += roll
    print(f'You rolled a {roll}')
  print(f"You have rolled a total of {dice_sums}")

if __name__== "__main__":
  main()