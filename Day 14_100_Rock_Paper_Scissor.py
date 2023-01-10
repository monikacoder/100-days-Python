player1_name = input("Enter player-1 name: ")
player2_name = input("Enter player-1 name: ")

print('''Enter your moves. R for Rock, P for Paper, S for scissors.
            Anyone can press E to exit\n''')

round_winner = player1_name
total_rounds = 0
while True:
    if round_winner == player1_name:
        print("----------Round starts-----------")
        player1_move = input(player1_name + " will start, enter your move: ").upper()
        player2_move = input(player2_name + " goes now, enter your move: ").upper()
    else:
        print("---------Round starts------------")
        player2_move = input(player2_name + " will start, enter your move: ").upper()
        player1_move = input(player1_name + " goes now, enter your move: ").upper()

    if player1_move not in ('R','P','S','E') or player2_move not in ('R','P','S','E'):
        print("One of the player made wrong move. We will start the round again! ")
        continue

    if player1_move == "E" or player2_move == "E":
        print(f"We will exit now. You have played total {total_rounds} rounds.  Bye!")
        break

    total_rounds = total_rounds + 1
    if player1_move == "R":
        if player2_move == "P":
               print(f"{player2_name} wins. Paper covers Rock!")
               round_winner = player2_name
        elif player2_move == "S":
               print(f"{player1_name} wins. Rock smashes Scissor!")
               round_winner = player1_name
        else:
               print(f"Its a tie!")
    elif player1_move == "P":
           if player2_move == "S":
                  print(f"{player2_name} wins. Scissor cuts Paper!")
                  round_winner = player2_name
           elif player2_move == "R":
                  print(f"{player1_name} wins. Paper covers Rock!")
                  round_winner = player1_name
           else:
               print(f"Its a tie!")
    elif player1_move == "S":
           if player2_move == "R":
                  print(f"{player2_name} wins. Rock smashes Scissor!")
                  round_winner = player2_name
           elif player2_move == "P":
                  print(f"{player1_name} wins. Scissor cuts Paper!")
                  round_winner = player1_name
           else:
               print(f"Its a tie!")

