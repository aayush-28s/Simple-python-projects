import random
import cv2

x = "y"
while x.lower() == "y":
    dice_roll = random.randint(1, 6)

    if dice_roll == 1:
        img = cv2.imread("dice1.png")
        cv2.imshow("Dice Roll", img)
        cv2.waitKey(0)  # Wait indefinitely until key press
        cv2.destroyAllWindows()

    if dice_roll == 2:
        img = cv2.imread("dice2.png")
        cv2.imshow("Dice Roll", img)
        cv2.waitKey(0)  # Wait indefinitely until key press
        cv2.destroyAllWindows()

    if dice_roll == 3:
        img = cv2.imread("dice3.png")
        cv2.imshow("Dice Roll", img)
        cv2.waitKey(0)  # Wait indefinitely until key press
        cv2.destroyAllWindows()

    if dice_roll == 4:
        img = cv2.imread("dice4.png")
        cv2.imshow("Dice Roll", img)
        cv2.waitKey(0)  # Wait indefinitely until key press
        cv2.destroyAllWindows()

    if dice_roll == 5:
        img = cv2.imread("dice5.png")
        cv2.imshow("Dice Roll", img)
        cv2.waitKey(0)  # Wait indefinitely until key press
        cv2.destroyAllWindows()

    if dice_roll == 6:
        img = cv2.imread("dice6.png")
        cv2.imshow("Dice Roll", img)
        cv2.waitKey(0)  # Wait indefinitely until key press
        cv2.destroyAllWindows()

    x = input("Press 'y' to roll again or any other key to exit: ")



