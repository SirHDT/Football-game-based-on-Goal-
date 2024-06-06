import time
import random
import os
import platform

def show_menu():
    print("\n=== Main Menu ===")
    print("1. Play")
    print("2. Exit")

def show_play():
    print("\n=== Play Menu ===")
    print("1. Local")
    print("2. Multiplayer")
    print("3. Back to Main Menu")

def show_play_local():
    print("\n=== Local Game ===")
    print("1. VS Computer")
    print("2. VS Player")
    print("3. Back to Play Menu")

def show_tactics():
    print("\n=== Tactics ===")
    print("1. 3-4-3 Attacking Formation")
    print("2. 3-5-2 Midfield Dominance")
    print("3. 3-6-1 Overloaded Midfield")
    print("4. 4-3-3 Offensive Formation")
    print("5. 4-4-2 Classic Formation")
    print("6. 4-5-1 Defensive Midfield")
    print("7. 5-2-3 Counter-Attack")
    print("8. 5-3-2 Defensive Formation")
    print("9. 5-4-1 Defensive Stance")
    print("0. Back to Local Menu")


def option1():
    while True:
        clear_console()
        show_play()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            play_local()
        elif choice == '2':
            play_multiplayer()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

def play_local():
    while True:
        clear_console()
        show_play_local()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            play_local_computer()
        elif choice == '2':
            play_local_player()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

def play_local_computer():
    class player:
        def __init__(self, name, team):
            self.name = name
            self.team = team

    clear_console()
    nickname_1 = input("Player 1 nickname: ")
    team_name_1 = input("Team 1 Name: ")
    player_1 = player(nickname_1, team_name_1)
    random_names = ['Chad', 'Kyle', 'Rick', 'Morty', 'Pepe', 'Hank', 'Bart', 'Homer', 'Peter', 'Joe']
    random_teams = [
        "Manchester United", "Real Madrid", "FC Barcelona", "Juventus", "Bayern Munich",
        "Liverpool FC", "Paris Saint-Germain", "Chelsea FC", "Borussia Dortmund", "AC Milan",
        "Inter Milan", "Manchester City", "Arsenal FC", "Atletico Madrid", "Tottenham Hotspur",
        "Ajax", "Benfica", "Porto", "Sevilla FC", "Lazio", "Sporting"
    ]
    nickname_2 = random.choice(random_names)
    team_name_2 = random.choice(random_teams)
    player_2 = player(nickname_2, team_name_2)

    while True:
        clear_console()
        print(f"{player_1.name} choose tactic for {player_1.team}")
        show_tactics()
        choice = input("Enter your choice (0-9): ")

        if choice == '0':
            break
        elif choice == '1':
            print("You have chosen 3-4-3 Attacking Formation")
            class team:
                def __init__(self):
                    self.defense = 3
                    self.midfield = 4
                    self.attack = 3
                    self.team = "3-4-3"
            p1_team = team()
            info_game_start(p1_team, player_1, player_2)
        elif choice == '2':
            print("You have chosen 3-5-2 Midfield Dominance")
            class team:
                def __init__(self):
                    self.defense = 3
                    self.midfield = 5
                    self.attack = 2
                    self.team = "3-5-2"
            p1_team = team()
            info_game_start(p1_team, player_1, player_2)
        elif choice == '3':
            print("You have chosen 3-6-1 Overloaded Midfield")
            class team:
                def __init__(self):
                    self.defense = 3
                    self.midfield = 6
                    self.attack = 1
                    self.team = "3-6-1"
            p1_team = team()
            info_game_start(p1_team, player_1, player_2)
        elif choice == '4':
            print("You have chosen 4-3-3 Offensive Formation")
            class team:
                def __init__(self):
                    self.defense = 4
                    self.midfield = 3
                    self.attack = 3
                    self.team = "4-3-3"
            p1_team = team()
            info_game_start(p1_team, player_1, player_2)
        elif choice == '5':
            print("You have chosen 4-4-2 Classic Formation")
            class team:
                def __init__(self):
                    self.defense = 4
                    self.midfield = 4
                    self.attack = 2
                    self.team = "4-4-2"
            p1_team = team()
            info_game_start(p1_team, player_1, player_2)
        elif choice == '6':
            print("You have chosen 4-5-1 Defensive Midfield")
            class team:
                def __init__(self):
                    self.defense = 4
                    self.midfield = 5
                    self.attack = 1
                    self.team = "4-5-1"
            p1_team = team()
            info_game_start(p1_team, player_1, player_2)
        elif choice == '7':
            print("You have chosen 5-2-3 Counter-Attack")
            class team:
                def __init__(self):
                    self.defense = 5
                    self.midfield = 2
                    self.attack = 3
                    self.team = "5-2-3"
            p1_team = team()
            info_game_start(p1_team, player_1, player_2)
        elif choice == '8':
            print("You have chosen 5-3-2 Defensive Formation")
            class team:
                def __init__(self):
                    self.defense = 5
                    self.midfield = 3
                    self.attack = 2
                    self.team = "5-3-2"
            p1_team = team()
            info_game_start(p1_team, player_1, player_2)
        elif choice == '9':
            print("You have chosen 5-4-1 Defensive Stance")
            class team:
                def __init__(self):
                    self.defense = 5
                    self.midfield = 4
                    self.attack = 1
                    self.team = "5-4-1"
            p1_team = team()
            info_game_start(p1_team, player_1, player_2)
        else:
            print("Invalid choice. Please enter a number between 0 and 9.")

def generate_bot_team():
    random_bot_team_number = random.randint(1, 9)
    if random_bot_team_number == 1:
        class r_team:
            def __init__(self):
                self.defense = 3
                self.midfield = 4
                self.attack = 3
                self.team = "3-4-3"
                self.player = False
        bot_team = r_team()
    elif random_bot_team_number == 2:
        class r_team:
            def __init__(self):
                self.defense = 3
                self.midfield = 5
                self.attack = 2
                self.team = "3-5-2"
                self.player = False
        bot_team = r_team()
    elif random_bot_team_number == 3:
        class r_team:
            def __init__(self):
                self.defense = 3
                self.midfield = 6
                self.attack = 1
                self.team = "3-6-1"
                self.player = False
        bot_team = r_team()
    elif random_bot_team_number == 4:
        class r_team:
            def __init__(self):
                self.defense = 4
                self.midfield = 3
                self.attack = 3
                self.team = "4-3-3"
                self.player = False
        bot_team = r_team()
    elif random_bot_team_number == 5:
        class r_team:
            def __init__(self):
                self.defense = 4
                self.midfield = 4
                self.attack = 2
                self.team = "4-4-2"
                self.player = False
        bot_team = r_team()
    elif random_bot_team_number == 6:
        class r_team:
            def __init__(self):
                self.defense = 4
                self.midfield = 5
                self.attack = 1
                self.team = "4-5-1"
                self.player = False
        bot_team = r_team()
    elif random_bot_team_number == 7:
        class r_team:
            def __init__(self):
                self.defense = 5
                self.midfield = 2
                self.attack = 3
                self.team = "5-2-3"
                self.player = False
        bot_team = r_team()
    elif random_bot_team_number == 8:
        class r_team:
            def __init__(self):
                self.defense = 5
                self.midfield = 3
                self.attack = 2
                self.team = "5-3-2"
                self.player = False
        bot_team = r_team()
    elif random_bot_team_number == 9:
        class r_team:
            def __init__(self):
                self.defense = 5
                self.midfield = 4
                self.attack = 1
                self.team = "5-4-1"
                self.player = False
        bot_team = r_team()
    return bot_team

def info_game_start(p1_team, player_1, player_2):
    clear_console()
    bot_team = generate_bot_team()

    print(f"{player_1.team} VS {player_2.team}")
    print(f"{player_1.name}    {player_2.name}")
    print(f"{p1_team.team}    {bot_team.team}")
    input("\nPress [Enter] to Start the Match")
    class game:
        def __init__(self):
            self.who_start = random.randint(1, 2)
            self.field_pos = 0
            self.score_1 = 0
            self.score_2 = 0
    game_object = game()
    start_local_game(game_object, p1_team, bot_team, player_1, player_2)

def start_local_game(game_object, p1_team, p2_team, player_1, player_2):
    class timer:
        def __init__(self):
            self.time_match = 0
    time_game = timer()
    while True:
        start_gameplay(game_object, p1_team, p2_team, time_game, player_1, player_2)

        if time_game.time_match >= 90:
            clear_console()
            print("\nFull time! The game has ended.")
            print(f"Score:{player_1.team}  {game_object.score_1} - {game_object.score_2} {player_2.team}")
            input("\nPress [Enter] to continue")
            break
        
        time.sleep(1)  # Wait for 1 second before updating the time

def start_gameplay(game, team_1, team_2, time_game, player_1, player_2):
    time_game.time_match += 2
    input("\nPress [Enter] to continue")
    clear_console()
    print("-----------------------------------------------------------------")
    print(f"Score: {player_1.team} {game.score_1} {game.score_2} {player_2.team}")
    print(f"Time: {time_game.time_match}")
    print("-----------------------------------------------------------------")
    if game.who_start == 1:
        game.who_start = 0
        player_1_mid_turn(game, team_1, team_2, time_game, player_1, player_2)
    elif game.who_start == 2:
        game.who_start = 0
        bot_mid_turn(game, team_1, team_2, time_game, player_1, player_2)
    else:
        if game.field_pos == 1:
            bot_goal_turn(game, team_2)
        elif game.field_pos == 2:
            player_1_def_turn(game, team_1, team_2, time_game, player_1, player_2)
        elif game.field_pos == 3:
            bot_attack_turn(game, team_1, team_2, time_game, player_1, player_2)
        elif game.field_pos == 4:
            player_1_mid_turn(game, team_1, team_2, time_game, player_1, player_2)
        elif game.field_pos == 5:
            bot_mid_turn(game, team_1, team_2, time_game, player_1, player_2)
        elif game.field_pos == 6:
            player_1_attack_turn(game, team_1, team_2, time_game, player_1, player_2)
        elif game.field_pos == 7:
            bot_def_turn(game, team_1, team_2, time_game, player_1, player_2)
        elif game.field_pos == 8:
            player_1_goal_turn(game, team_2)
        else:
            print("error")
    
def player_1_mid_turn(game, team_1, team_2, time_game, player_1, player_2):
    print("Player 1's mid turn")
    input("\nPress [Enter] to Start")

    random_object = random_mid(team_1, team_2, player_1, player_2)
    if random_object[0] > random_object[1]:
        print("Player 1 pass the ball to the attack")
        game.field_pos = 6
    elif random_object[1] > random_object[0]:
        print("Player 2 retrieved the ball in the midfield")
        game.field_pos = 5
    else:
        print("Ball is loose in the midfield")
        time_game.time_match += 2
        game.field_pos = 4
        start_gameplay(game, team_1, team_2, time_game, player_1, player_2)

def bot_mid_turn(game, team_1, team_2, time_game, player_1, player_2):
    print("Player 2's mid turn")
    input("\nPress [Enter] to Start")

    random_object = random_mid(team_1, team_2, player_1, player_2)
    if random_object[1] > random_object[0]:
        print("Player 2 pass the ball to the attack")
        game.field_pos = 3
    elif random_object[0] > random_object[1]:
        print("Player 1 retrieved the ball in the midfield")
        game.field_pos = 4
    else:
        print("Ball is loose in the midfield")
        time_game.time_match += 2
        game.field_pos = 5
        start_gameplay(game, team_1, team_2, time_game, player_1, player_2)

def player_1_def_turn(game, team_1, team_2, time_game, player_1, player_2):
    print("Player 1's defense turn")
    input("\nPress [Enter] to Start")

    random_object = random_def(team_1, team_2, player_1, player_2)
    if random_object[0] > random_object[1]:
        print("Player 1 pass the ball to the midfield")
        game.field_pos = 4
    elif random_object[1] > random_object[0]:
        print("Player 2 steal's the ball ready to attack")
        game.field_pos = 3
    else:
        print("Ball is loose in the defense of Player 1")
        time_game.time_match += 2
        game.field_pos = 2
        start_gameplay(game, team_1, team_2, time_game, player_1, player_2)

def bot_def_turn(game, team_1, team_2, time_game, player_1, player_2):
    print("Player 2's defense turn")
    input("\nPress [Enter] to Start")

    random_object = random_def(team_1, team_2, player_1, player_2)
    if random_object[1] > random_object[0]:
        print("Player 2 pass the ball to the midfield")
        game.field_pos = 5
    elif random_object[0] > random_object[1]:
        print("Player 1 steal's the ball ready to attack")
        game.field_pos = 6
    else:
        print("Ball is loose in the defense of Player 2")
        time_game.time_match += 2
        game.field_pos = 7
        start_gameplay(game, team_1, team_2, time_game, player_1, player_2)

def player_1_attack_turn(game, team_1, team_2, time_game, player_1, player_2):
    print("Player 1's attack turn")
    input("\nPress [Enter] to Start")

    random_object = random_att(team_1, team_2, player_1, player_2)
    if random_object[0] > random_object[1]:
        print("Player 1 SHOOTS")
        game.field_pos = 8
    elif random_object[1] > random_object[0]:
        print("Player 2 retrived the ball in the defense")
        game.field_pos = 7
    else:
        print("Ball is loose in the attack of Player 1")
        time_game.time_match += 2
        game.field_pos = 6
        start_gameplay(game, team_1, team_2, time_game, player_1, player_2)

def bot_attack_turn(game, team_1, team_2, time_game, player_1, player_2):
    print("Player 2's attack turn")
    input("\nPress [Enter] to Start")

    random_object = random_att(team_1, team_2, player_1, player_2)
    if random_object[1] > random_object[0]:
        print("Player 2 SHOOTS")
        game.field_pos = 1
    elif random_object[0] > random_object[1]:
        print("Player 1 retrived the ball in the defense")
        game.field_pos = 2
    else:
        print("Ball is loose in the attack of Player 2")
        time_game.time_match += 2
        game.field_pos = 3
        start_gameplay(game, team_1, team_2, time_game, player_1, player_2)

def player_1_goal_turn(game, team_2):
    print("Player 1's goal turn")
    player_1 = 0
    input("\nPress [Enter] to continue")
    if team_2.player == True:
        game = goal_or_kepper(game, player_1)
    else:
        game = goal_or_kepper_bot(game, player_1)

def bot_goal_turn(game, team_2):
    print("Player 2's goal turn")
    player_2 = 1
    input("\nPress [Enter] to continue")
    if team_2.player == True:
        game = goal_or_kepper(game, player_2)
    else:
        game = goal_or_kepper_bot(game, player_2)

def random_mid(team_1, team_2, player_1, player_2):
    random_t1 = random.randint(0, team_1.midfield)
    random_t2 = random.randint(0, team_2.midfield)
    print(f"{player_1.team} {random_t1} - {random_t2} {player_2.team} ")
    return random_t1, random_t2

def random_def(team_1, team_2, player_1, player_2):
    random_t1 = random.randint(0, team_1.defense)
    random_t2 = random.randint(0, team_2.defense)
    print(f"{player_1.team} {random_t1} - {random_t2} {player_2.team} ")
    return random_t1, random_t2

def random_att(team_1, team_2, player_1, player_2):
    random_t1 = random.randint(0, team_1.attack)
    random_t2 = random.randint(0, team_2.attack)
    print(f"{player_1.team} {random_t1} - {random_t2} {player_2.team} ")
    return random_t1, random_t2

def goal_or_kepper_bot(game, who_shoots):
    allowed_characters = ['w', 'a', 's', 'd']
    print("Scorer Turn")
    if who_shoots == 0:
        while True:
            scorer_input = input("Please enter one of the following characters (w, a, s, d): ").lower()
            if scorer_input in allowed_characters:
                break
            else:
                print("Invalid input. Please try again.")
        print("Goalkeeper turn")
        time.sleep(1)
        bot_random = random.choice(allowed_characters)
        if scorer_input == bot_random:
            print("Goalkeeper saved the shot")
            game.field_pos = 5
            return game
        else:
            print("Goal scored")
            game.score_1 += 1
            game.field_pos = 5
            return game
    else:
        bot_random = random.choice(allowed_characters)
        while True:
            goalkepper_input = input("Please enter one of the following characters (w, a, s, d): ").lower()
            if goalkepper_input in allowed_characters:
                break
            else:
                print("Invalid input. Please try again.")
        if goalkepper_input == bot_random:
            print("Goalkeeper saved the shot")
            game.field_pos = 4
            return game
        else:
            print("Goal scored")
            game.score_2 += 1
            game.field_pos = 4
            return game

def goal_or_kepper(game, who_shoots):
    allowed_characters = ['w', 'a', 's', 'd']
    print("Scorer Turn")
    if who_shoots == 0:
        while True:
            scorer_input = input("Please enter one of the following characters (w, a, s, d): ").lower()
            if scorer_input in allowed_characters:
                break
            else:
                print("Invalid input. Please try again.")
        print("Goalkeeper turn")
        while True:
            goalkepper_input = input("Please enter one of the following characters (w, a, s, d): ").lower()
            if goalkepper_input in allowed_characters:
                break
            else:
                print("Invalid input. Please try again.")
        if scorer_input == goalkepper_input:
            print("Goalkeeper saved the shot")
            game.field_pos = 5
            return game
        else:
            print("Goal scored")
            game.score_1 += 1
            game.field_pos = 5
            return game
    else:
        while True:
            scorer_input = input("Please enter one of the following characters (w, a, s, d): ").lower()
            if scorer_input in allowed_characters:
                break
            else:
                print("Invalid input. Please try again.")
        print("Goalkeeper turn")
        while True:
            goalkepper_input = input("Please enter one of the following characters (w, a, s, d): ").lower()
            if goalkepper_input in allowed_characters:
                break
            else:
                print("Invalid input. Please try again.")
        if scorer_input == goalkepper_input:
            print("Goalkeeper saved the shot")
            game.field_pos = 4
            return game
        else:
            print("Goal scored")
            game.score_2 += 1
            game.field_pos = 4
            return game

def play_local_player():
    class player:
        def __init__(self, name, team):
            self.name = name
            self.team = team

    clear_console()
    nickname_1 = input("Player 1 nickname: ")
    team_name_1 = input("Team 1 Name: ")
    player_1 = player(nickname_1, team_name_1)
    clear_console()
    nickname_2 = input("Player 2 nickname: ")
    team_name_2 = input("Team 2 Name: ")
    player_2 = player(nickname_2, team_name_2)
    
    while True:
        clear_console()
        print(f"{player_1.name} choose tactic for {player_1.team}")
        show_tactics()
        choice = input("Enter your choice (0-9): ")

        if choice == '0':
            play_local()
        elif choice == '1':
            print("You have chosen 3-4-3 Attacking Formation")
            class team:
                def __init__(self):
                    self.defense = 3
                    self.midfield = 4
                    self.attack = 3
                    self.team = "3-4-3"
            p1_team = team()
            break
        elif choice == '2':
            print("You have chosen 3-5-2 Midfield Dominance")
            class team:
                def __init__(self):
                    self.defense = 3
                    self.midfield = 5
                    self.attack = 2
                    self.team = "3-5-2"
            p1_team = team()
            break
        elif choice == '3':
            print("You have chosen 3-6-1 Overloaded Midfield")
            class team:
                def __init__(self):
                    self.defense = 3
                    self.midfield = 6
                    self.attack = 1
                    self.team = "3-6-1"
            p1_team = team()
            break
        elif choice == '4':
            print("You have chosen 4-3-3 Offensive Formation")
            class team:
                def __init__(self):
                    self.defense = 4
                    self.midfield = 3
                    self.attack = 3
                    self.team = "4-3-3"
            p1_team = team()
            break
        elif choice == '5':
            print("You have chosen 4-4-2 Classic Formation")
            class team:
                def __init__(self):
                    self.defense = 4
                    self.midfield = 4
                    self.attack = 2
                    self.team = "4-4-2"
            p1_team = team()
            break
        elif choice == '6':
            print("You have chosen 4-5-1 Defensive Midfield")
            class team:
                def __init__(self):
                    self.defense = 4
                    self.midfield = 5
                    self.attack = 1
                    self.team = "4-5-1"
            p1_team = team()
            break
        elif choice == '7':
            print("You have chosen 5-2-3 Counter-Attack")
            class team:
                def __init__(self):
                    self.defense = 5
                    self.midfield = 2
                    self.attack = 3
                    self.team = "5-2-3"
            p1_team = team()
            break
        elif choice == '8':
            print("You have chosen 5-3-2 Defensive Formation")
            class team:
                def __init__(self):
                    self.defense = 5
                    self.midfield = 3
                    self.attack = 2
                    self.team = "5-3-2"
            p1_team = team()
            break
        elif choice == '9':
            print("You have chosen 5-4-1 Defensive Stance")
            class team:
                def __init__(self):
                    self.defense = 5
                    self.midfield = 4
                    self.attack = 1
                    self.team = "5-4-1"
            p1_team = team()
            break
            
        else:
            print("Invalid choice. Please enter a number between 0 and 9.")
    while True:
        clear_console()
        print(f"{player_2.name} choose tactic for {player_2.team}")
        show_tactics()
        choice = input("Enter your choice (0-9): ")

        if choice == '0':
            play_local()
        elif choice == '1':
            print("You have chosen 3-4-3 Attacking Formation")
            class team:
                def __init__(self):
                    self.defense = 3
                    self.midfield = 4
                    self.attack = 3
                    self.team = "3-4-3"
                    self.player = True
            p2_team = team()
            break
        elif choice == '2':
            print("You have chosen 3-5-2 Midfield Dominance")
            class team:
                def __init__(self):
                    self.defense = 3
                    self.midfield = 5
                    self.attack = 2
                    self.team = "3-5-2"
                    self.player = True
            p2_team = team()
            break
        elif choice == '3':
            print("You have chosen 3-6-1 Overloaded Midfield")
            class team:
                def __init__(self):
                    self.defense = 3
                    self.midfield = 6
                    self.attack = 1
                    self.team = "3-6-1"
                    self.player = True
            p2_team = team()
            break
        elif choice == '4':
            print("You have chosen 4-3-3 Offensive Formation")
            class team:
                def __init__(self):
                    self.defense = 4
                    self.midfield = 3
                    self.attack = 3
                    self.team = "4-3-3"
                    self.player = True
            p2_team = team()
            break
        elif choice == '5':
            print("You have chosen 4-4-2 Classic Formation")
            class team:
                def __init__(self):
                    self.defense = 4
                    self.midfield = 4
                    self.attack = 2
                    self.team = "4-4-2"
                    self.player = True
            p2_team = team()
            break
        elif choice == '6':
            print("You have chosen 4-5-1 Defensive Midfield")
            class team:
                def __init__(self):
                    self.defense = 4
                    self.midfield = 5
                    self.attack = 1
                    self.team = "4-5-1"
                    self.player = True
            p2_team = team()
            break
        elif choice == '7':
            print("You have chosen 5-2-3 Counter-Attack")
            class team:
                def __init__(self):
                    self.defense = 5
                    self.midfield = 2
                    self.attack = 3
                    self.team = "5-2-3"
                    self.player = True
            p2_team = team()
            break
        elif choice == '8':
            print("You have chosen 5-3-2 Defensive Formation")
            class team:
                def __init__(self):
                    self.defense = 5
                    self.midfield = 3
                    self.attack = 2
                    self.team = "5-3-2"
                    self.player = True
            p2_team = team()
            break
        elif choice == '9':
            print("You have chosen 5-4-1 Defensive Stance")
            class team:
                def __init__(self):
                    self.defense = 5
                    self.midfield = 4
                    self.attack = 1
                    self.team = "5-4-1"
                    self.player = True
            p2_team = team()
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 9.")
    info_game_start_local_2players(p1_team, p2_team, player_1, player_2)       

def info_game_start_local_2players(p1_team, p2_team, player_1, player_2):
    clear_console()
    print(f"{player_1.team} VS {player_2.team}")
    print(f"{player_1.name}    {player_2.name}")
    print(f"{p1_team.team}    {p2_team.team}")
    input("\nPress [Enter] to Start the Match")
    class game:
        def __init__(self):
            self.who_start = random.randint(1, 2)
            self.field_pos = 0
            self.score_1 = 0
            self.score_2 = 0
    game_object = game()
    start_local_game(game_object, p1_team, p2_team, player_1, player_2)

def play_multiplayer():
    print("IN DEVELOPMENT")
    time.sleep(2)

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            option1()
        elif choice == '2':
            print("Exiting the menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 2.")

if __name__ == "__main__":
    main()
