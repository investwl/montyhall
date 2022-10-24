from random import shuffle
import boxes
#File untuk shuffling list untuk montyhall

#Buat variable yang valuenya 2 hadiah jelek dan 1 hadiah bagus dan isinya dirandomized dengan import library random

#Karena montyhall ini hanya akan 3 terus dan variablenya selalu itu2 aja, maka kita pakai tuple aja
prize_boxes = ["$1.000.000", "$1", "$1"]
shuffled_prize = shuffle(prize_boxes)

def check_non_grand_prize(user_first_box):
    list_non_grand = []
    list_index_non_grand = []
    for i in range(len(shuffled_prize)):
        if shuffled_prize[i] == "$1":
            list_non_grand.append(shuffled_prize[i])
            list_index_non_grand.append(i) #ini supaya tau di index ke berapa yang shuffled_prize itu mana yg $1
    if shuffled_prize[user_first_box] in list_non_grand:
        list_non_grand.remove(shuffled_prize[user_first_box])
        #habis remove, tampilkan option shuffled yang $1 yg tersisa di list_index_non_grand (jadi tampilin itu)
        #BIG WARNING : DO NOT USE REMOVE AT SHUFFLED_PRIZE BECAUSE IT WOULD AFFECT THE INDEX
        #setelah tampilin, tanya lagi masih mau keep or change
        #bikin variable baru untuk tampung, either keep or change. kalo keep berarti bikin var baru merujuk ke shuffled index sisa dengan logic biasa
        #kalo change ya tinggal isi aja indexnya
        #terus udh gitu, lgsg print box sesuai index


def start_game(username):
    #Variable untuk simpan box pilihan user
    print("Welcome, %s"%(username))
    print("Let's start the Monty Hall's Game, shall we?\n\nHere i have three boxes below, choose a box that you feel you would win the grandprize!")
    boxes.all_closed_box() #takes a totally unrevealed box function
    while True:
        try:
            first_choose_box = int(input("Now, choose your box! Either 1, 2, or 3!\nYour box (number only) :"))
        except:
            print("Only number is accepted.")
            continue
        if first_choose_box == 1:
            user_first_box = 0 #because index of the list starts from 0
        elif first_choose_box == 2:
            user_first_box = 1
        elif first_choose_box == 3:
            user_first_box = 2
        else:
            print("Only accepting 1, 2, or 3 because only 3 boxes exists.")

        

start_game("ayam")