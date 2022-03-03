from Card import*
import random
class Player():
    def __init__(self):
        self.deck=[]
        self.deck_count=0
        self.clock=0
        self.clock_area=[]
        self.level=0
        self.level_area=[]
        self.front_stage=[]
        self.front_stage_count=0
        self.rear_stage=[]
        self.rear_stage_count=0
        self.hand=[]
        self.hand_count=0
        self.wating_room=[]
        self.wating_room_count=0
        self.wating_room_climax_count=0
        self.stock=[]
        self.stock_count=0
        self.climax_area=[]
        self.memory_area=[]
        self.memory_area_count=0

        
def Game_Start():
    player1=Player()
    player2=Player()
    turn=True
    turn_count=0
    gamestate=Game_init;
    player1=gamestate[0]
    player2=gamestate[1]
    while True:
        if player1.level>=4 or player2.level>=4:
            Game_end
            break;
    #turn
    if turn:
        player=player1
    else:
        player=player2
    #stand_phase
    if player.front_stage_count>0:
        for x in range(0,player.front_stage_count):
            if player.front_stage[x]!=None:
                if player.front_stage[x].tab=="Die":
                    player.front_stage[x]=None
                    player.front_stage_count-=1
                else:
                    player.front_stage[x].tab="Stand"
    #draw_phase
    Draw_card(player,True)
    #clock_phase
    choice_hand_index=0
    Clock_draw(player,choice_hand_index)

    #main_phase
    Chara_set(player,where,card)

    #climax_phase
    
def Draw_card(player,damage_check):
    top_card=player.deck[0]
    player.hand.append(top_card)
    del player.deck[0]
    Refresh_deck(player)
    if damage_check:
        Refresh_damage(player)
def Clock_draw(player,choice_hand_index):
    player.clock_area.append(player.hand[choice_hand_index])
    Level_Up(player)
    del player.hand[choice_hand_index]
    Draw_card(player,False)
    Draw_card(player,True)

def Deck_Suffle(player):
    random.shuffle(player.deck)
def Refresh_deck(player):
    if player.deck_count<=0:
        player.deck=player.wating_room
        player.wating_room=[]
        random.shuffle(player.deck)
        player.deck_count=player.wating_room_count
        player.wating_room_count=0
        player.wating_room_climax_count=0

def Refresh_damage(player):
    top_card=player.deck[0]
    player.clock_area.append(top_card)
    del player.deck[0]
    Level_Up(player)
    
def Level_Up(player):
    if player.clock>=7:
        player.clock=0
        chosen_index=choice_level_zone_card(player)
        player.level_area.append(player.clock_area[chosen_index])
        player.level=player.level+1
        del player.clock_area[chosen_index]
        for x in range(0,len(player.clock_area[x])):
            player.waiting_room.append(player.clock_area[x])
        player.clock_area=[]

def choice_level_zone_card(player):
    print('test')
    return 0
def Game_end():
    print("game end")

def Chara_set(player,where,card):
    player.

def Chara_Attack()

def Chara_