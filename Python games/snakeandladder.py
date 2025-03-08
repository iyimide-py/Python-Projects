import random
logo = """
                                                      
                                 88                   
                                 88                   
                                 88                   
,adPPYba, 8b,dPPYba,  ,adPPYYba, 88   ,d8  ,adPPYba,  
I8[    "" 88P'   `"8a ""     `Y8 88 ,a8"  a8P_____88  
 `"Y8ba,  88       88 ,adPPPPP88 8888[    8PP"""""""  
aa    ]8I 88       88 88,    ,88 88`"Yba, "8b,   ,aa  
`"YbbdP"' 88       88 `"8bbdP"Y8 88   `Y8a `"Ybbd8"'  

"""

p1 = '30'
p2 = 'S'
p3 = '28'
p4 = '27'
p5 = 'S'
p6 = '25'
p7 = '19'
p8 = 'L'
p9 = 'S'
p10 = '22'
p11 = '23'
p12 = '24'
p13 = '18'
p14 = '17'
p15 = '16'
p16 = 'S'
p17 = '14'
p18 = '13'
p19 = '07'
p20 = 'L'
p21 = '09'
p22 = '10'
p23 = '11'
p24 = '12'
p25 = '06'
p26 = '05'
p27 = '04'
p28 = '03'
p29 = 'L'
p30 = '01'

a = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30]
b = a[0:6]
c = a[6:12]
d = a[12:18]
e = a[18:24]
f = a[24:30]

snakes = {15: 5, 21: 5, 26: 6, 29: 7}
ladders = {2: 16, 8: 24, 20: 27}

nl = f'{b}\n{c}\n{d}\n{e}\n{f}'


def roll_dice():
    return random.randint(1, 6)

def game():
    print("WELCOME TO SNAKES & LADDERS!!!")
    print(logo)
    print(nl)
    snakes = {15: 5, 20: 5, 26: 6, 29: 7}
    ladders = {2: 16, 8: 24, 20: 27}
    player_position = 0
    while player_position < 30:
        user_input = input("Type R to roll the dice\n").lower()
        if user_input == "r":
            roll_dice()
            value = roll_dice()
            print(f"You rolled position {value}.")

            player_position += value
            print(f"You're currently at {player_position}.")

            if player_position > 30:
                player_position -= value
                print(f"You remain at {player_position}")


            if player_position in snakes:
                print(f"You got bitten by a snake at {player_position}")
                player_position = snakes[player_position]
                print(f"You go back to {player_position}")
            elif player_position in ladders:
                print(f"You landed on a ladder at {player_position}.")
                player_position = ladders[player_position]
                print(f"You climb up to {player_position}")

            elif player_position == 30:
                print("You win!")
                game()



game()