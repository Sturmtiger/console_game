from players import Player, Computer
from random import shuffle


def game():
    player_name = input('Enter your name to start the game: ').strip()
    while len(player_name) == 0:
        player_name = input('Enter your name to start the game, please: ').strip()

    player = Player(player_name)
    computer = Computer()

    score = {player.name: 0, computer.name: 0}

    game_condition = True
    while game_condition:  # This while loop is for the re-opportunity to play (game score)
        print(f' Welcome to the console game, {player.name}! '.center(70, '*'), end='\n\n')
        users_deck = [player, computer]

        if player.health < 100 or computer.health < 100:
            for user in users_deck:
                user.health = 100

        shuffle(users_deck)  # Random sequence of players moves
        move_counter = 0

        while player.health > 0 and computer.health > 0:
            move_counter += 1
            for user in users_deck:
                print(f' Player [{user.name}] move ({move_counter}) '.center(70, '*'))

                if isinstance(user, Computer):
                    user.make_some_decision(player)

                else:
                    actions = ['mid_damage_the_enemy', 'high_damage_the_enemy', 'heal_yourself']
                    print('Choose some action:',
                          '1. Inflict middle damage(18-25hp) to the enemy',
                          '2. Inflict high damage(10-35hp) to the enemy',
                          '3. Heal yourself(18-25hp)', sep='\n')

                    action_choice = actions[int(input('Enter a number: '))-1]
                    if action_choice == 'heal_yourself':
                        getattr(user, action_choice)()
                    else:
                        getattr(user, action_choice)(computer)

                print(' Players health data '.center(70, '-'))
                for user_hp in users_deck:  # Print the health data of players after the move.
                    print(user_hp)
                print('-' * 70, end='\n\n')

                if player.health <= 0:
                    score[computer.name] += 1
                    print(f'{player.name}, you Lose!')
                    break
                elif computer.health <= 0:
                    score[player.name] += 1
                    print(f'Congratulations! {player.name}, you Won!')
                    break

        print(' SCORE '.center(70, '*'))
        for key, value in score.items():
            print(f'{key}: {value}')
        print('*' * 70)

        print('Play again?',
              '1. No',
              '2. Yes', sep='\n')
        game_condition = [False, True][int(input('Enter a number: '))-1]
