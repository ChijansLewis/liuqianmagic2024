from utils import *
import time

def magic():
    # 选择四张牌
    hand_cards = choose_four_cards()

    # 展示选中的牌
    print("已选的四张牌：")
    show_cards(hand_cards)

    # 撕开扑克牌
    hand_cards.extend(hand_cards)
    print("现在的手牌")
    show_cards(hand_cards)

    # STEP1：名字的字数
    n_name_char = int(input("名字的字数："))
    for _ in range(n_name_char):
        card = hand_cards.pop(0)
        hand_cards.append(card)

    # STEP2：最上面三张插进中间任何一个位置
    print("拿开前3张，还有5张，选择1，2，3，4四个位置之一插入")
    i = int(input("你的选择："))
    fst = hand_cards.pop(0)
    scd = hand_cards.pop(0)
    thr = hand_cards.pop(0)
    hand_cards.insert(i, fst)
    hand_cards.insert(i+1, scd)
    hand_cards.insert(i+2, thr)

    # STEP3：最上面一张牌藏起来
    print("最上面一张牌藏起来...")
    time.sleep(1.5)
    saved_card = hand_cards.pop(0)

    # STEP4：南方还是北方？
    print("你认为自己是南方人请输入1，北方人输入2，其他请输入3")
    m = int(input("你的选择："))
    time.sleep(0.5)
    if m == 1:
        print("拿开1张，还有6张，选择1，2，3，4，5五个位置之一插入")
        i = int(input("你的选择："))
        fst = hand_cards.pop(0)
        hand_cards.insert(i, fst)
    elif m == 2:
        print("拿开2张，还有5张，选择1，2，3，4四个位置之一插入")
        i = int(input("你的选择："))
        fst = hand_cards.pop(0)
        scd = hand_cards.pop(0)
        hand_cards.insert(i, fst)
        hand_cards.insert(i+1, scd)
    else:
        print("拿开前3张，还有4张，选择1，2，3三个位置之一插入")
        i = int(input("你的选择："))
        fst = hand_cards.pop(0)
        scd = hand_cards.pop(0)
        thr = hand_cards.pop(0)
        hand_cards.insert(i, fst)
        hand_cards.insert(i+1, scd)
        hand_cards.insert(i+2, thr)

    # STEP5：男生女生
    time.sleep(1)
    gender = int(input("你是男生请输入1，女生请输入2，抱歉不支持其他性别："))
    if gender == 1:
        del hand_cards[0]
    else:
        del hand_cards[:2]

    # STEP6：见证奇迹的时刻！
    time.sleep(1)
    print("接下来是见证奇迹的时刻，和我一起喊：")
    for char in "见证奇迹的时刻":
        print(char+'!')
        card = hand_cards.pop(0)
        hand_cards.append(card)
        time.sleep(1)
    
    # STEP7：好运留下来，烦恼丢出去
    time.sleep(1)
    print("接下来和我做：")
    while len(hand_cards) > 1:
        time.sleep(1)
        print("好运留下来！")
        card = hand_cards.pop(0)
        hand_cards.append(card)
        time.sleep(1)
        print("烦恼丢出去！")
        del hand_cards[0]

    # STEP8：见证奇迹！
    time.sleep(1)
    print("让我们",end='')
    if hand_cards[0] == saved_card:
        print(f"见证奇迹！{hand_cards[0][0]}{hand_cards[0][1]}和{saved_card[0]}{saved_card[1]}！")
        print("新年快乐！")
    else:
        print("再试一次吧")

if __name__ == "__main__":
    magic()
