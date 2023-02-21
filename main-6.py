#function for Computer's move
def computer(sticks, max_sticks):
  #we use a modulo here to make sure that the computer always only takes between 1 and max_sticks.
  return (sticks) % (max_sticks + 1)


#function for the game
def nim(sticks, max_sticks):
  print("Welcome to the game of NIM!!!")
  #if sticks are not 0, keep the loop going
  while sticks > 0:
    print("There are", sticks, "sticks left.")
    #the computer is always going to take the first move.
    computer_turn = computer(sticks, max_sticks)
    print("Computer takes", computer_turn, "sticks.")
    sticks = sticks - computer_turn
    print("After Computer's turn, there are", sticks,
          "sticks left in the pile.")
    #the computer wins if there are 0 sticks left.
    if sticks <= 0:
      print("Computer wins!")
      break
    #player's turn
    player1 = int(
      input(
        f"How many sticks do you want to take between 1 and {max_sticks}? : "))
    #player has to choose a valid number of sticks and if they choose sticks beyond the range specified, they get a message to try again.
    while player1 < 1 or player1 > 5 or player1 > sticks:
            player1 = int(input('The input is invalid. You can only take 1 to 5 sticks. Try again! '))
    #the player wins if there are 0 sticks left.
    sticks -= player1
    if sticks <= 0:
      print('You win!')


#initialize the game with 15 sticks, and max sticks than can be taken out 5. The number of sticks and max sticks taken allowed can be changed at your convenience
nim(15, 5)
