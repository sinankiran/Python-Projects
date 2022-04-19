import random
#Basic Dice Rolling Example

def main():
    #1. Asks how many sides will be and runs dice function
    print("How many sides will have of the dice?")
    question = dice(int(input("")))
    #5. Prints the answer
    answer = question
    print(answer)


def dice(side):
    #2. Just gives an info to user about dice is rolling
    print(f"{side} Sided dice is rolling...")
    #3. Randomises a number between 1 an "f{side}"
    side = random.randint(1, side)
    #4. Returns the answer
    return side

#to run the program
main()