#-*-coding:utf8;-*-
#qpy:3
#qpy:console

from time import sleep
from random import randint

team_game = False
types = {"Warrior": [125,25,1], "Archer": [150,15,2], "Mage": [50,10,4]}

class Player:
    def __init__(self, name,type):
        self.name = name
        self.type = type
        self.health = types.get(type)[0]
        self.damage = types.get(type)[1]
        self.luck = types.get(type)[2]
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

players = [
Player("Guts", "Warrior"),
Player("Casca", "Archer"),
Player("Judeau", "Mage"),
Player("Griffith", "Warrior"),
Player("Rickert", "Archer")
]

def CalLuck(luck):
    x = randint(1,5)
    if x <= luck:
        return True
    else:
        return False

def NextTurn(teams, team_game):

    for team in teams:

        if teams.index(team) == 0:
            enemy_team = teams[1]
        else:
            enemy_team = teams[0]

        print("\n\n\n\n\n\n\n\n\n\n\n")
        print("Team {}\n".format(teams.index(team)+1))

        for player in team:

            print("Chosen player: [{}] {} {}".format(player.health, player.name, player.type))
            print("\nEnemies:")

            for enemy_nr in range(len(enemy_team)):
                enemy = enemy_team[enemy_nr]

                print("{}) [{}] {} {}".format(str(enemy_nr + 1), enemy.health, enemy.name, enemy.type))

            print()

            target = enemy_team[int(input("Target: "))-1]

            print("\n\n\n\n\n\n")

            if CalLuck(target.luck) == False:
                last_target_health = target.health

                if CalLuck(player.luck) == True:
                    target.health -= player.damage*3
                    print("Critical hit!")

                else:
                    target.health -= player.damage
                    print("Hit!")

                print()
                print("{} {} [{}] -> [{}]".format(target.name, target.type, last_target_health, target.health))
                print("\n")
                if player.type == "Warrior" and target.health > 0:
                    last_player_health = player.health
                    player.health -= int(target.damage)
                    print("The enemy counterattacked!")
                    print()
                    print("{} {} [{}] -> [{}]".format(player.name, player.type, last_player_health, player.health))
                    print()

            else:
                print("Miss!")
                print()

            if player.health <= 0:
                print("{} {} d.".format(player.name, player.type))
                del teams[teams.index(team)][team.index(player)]

            if target.health <= 0:
                print("{} {} died.".format(target.name, target.type))
                del teams[teams.index(enemy_team)][enemy_team.index(target)]

            if len(team) == 0 or len(enemy_team) == 0:

                if len(team) == 0:
                    winner = teams.index(team)+1
                if len(enemy_team) == 0:
                    winner = teams.index(enemy_team)+1

                print("\n\n\n\n\n\n\n\n\n\n\n")
                print("Team {} Wins".format(winner))

                sleep(10)

                return

            sleep(3)

            print("\n\n\n")

    NextTurn(teams, team_game)

def Launcher():
    avaible_players = players

    x = int(input("Team game? [0|1]: "))

    if x == 1:
        team_game = True
    elif x == 0:
        team_game = False
    else:
        Launcher()

    if team_game == True:
        team_player_count = int(input("Choose team player count [1|{}]: ".format(int(len(players)/2))))
    else:
        team_player_count = 1

    print("\n\n")

    if team_player_count > 0 and team_player_count <= int(len(players)/2):
        teams = [[None]*team_player_count,[None]*team_player_count]

        for y in range(2):
            print("\n\n\n\n")
            print("Team {}\n".format(str(y+1)))


            for z in range(team_player_count):
                for i in range(len(avaible_players)):
                    print(str(i+1)+ ") {} {}".format(avaible_players[i].name, avaible_players[i].type))

                print()

                chosen_player = int(input(f"Choose player {str(z+1)}: "))-1
                teams[y][z] = avaible_players[chosen_player]
                del avaible_players[chosen_player]
                print()

    NextTurn(teams, team_game)



while True:
    print("\nDungeon Warriors\n")
    Launcher()
