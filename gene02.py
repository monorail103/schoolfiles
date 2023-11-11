import sys
import random
import time
import pygame
import os
import json
import datetime
from pygame.locals import *

# 画像ファイルのパス
APPLE = "images/apple.png"
BANANA = "images/banana.png"
GRAPE = "images/grape.png"

# jsonランキングファイル
fn = 'slot/ranking.json'
if not os.path.isfile(fn):
  raise FileNotFoundError(f'{fn} は存在しません。強制終了します。')
# 開く
with open(fn, encoding='utf_8') as file:
  data = json.load(file)
print(len(data))

# ランキング名前用時間設定
t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)

# 画面のサイズ
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# スロットのサイズと位置
SLOT_WIDTH = 100
SLOT_HEIGHT = 100
SLOT_X = 200
SLOT_Y = 100

# プログレスバーのサイズと位置(現在使用停止)
BAR_WIDTH = 400
BAR_HEIGHT = 40
BAR_X = 100
BAR_Y = 210

# ランキングの位置
RANK_X = 50
RANK_Y = 250

# ボタンのサイズと位置
BUTTON_WIDTH = 130
BUTTON_HEIGHT = 50
BUTTON_X = 450
BUTTON_Y = 300

# メッセージの位置
MESSAGE_X = 220
MESSAGE_Y = 50

# ポイント表示の位置
POINT_X = 50
POINT_Y = 60

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# ポイント定義
point = 100

# 回数カウンター
count = 0

# pygameの初期化
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Slot Game")
clock = pygame.time.Clock()

# 画像の読み込み
apple = pygame.image.load(APPLE)
banana = pygame.image.load(BANANA)
grape = pygame.image.load(GRAPE)
apple = pygame.transform.scale(apple, (100, 100))
banana = pygame.transform.scale(banana, (100, 100))
grape = pygame.transform.scale(grape, (100, 100))

# 絵柄のリスト
symbols = [apple, banana, grape]

# スロットの初期化
slot1 = apple
slot2 = banana
slot3 = grape

# プログラスバー関連の変数
progress = 0
start = False

# フォントの作成
font = pygame.font.Font('datas/M_PLUS_1p/MPLUS1p-Regular.ttf', 25)
font2 = pygame.font.Font('datas/M_PLUS_1p/MPLUS1p-Regular.ttf', 30)

# メッセージの初期化
message = ""
start_text = "START"

# 絵柄の角度を表す変数を定義する
angle1 = 0
angle2 = 0
angle3 = 0

nametmp = ""

# メインループ
while True:
    # イベントの処理
    for event in pygame.event.get():
        if event.type == QUIT: # ウィンドウを閉じたら終了
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN: # マウスをクリックしたら
            x, y = pygame.mouse.get_pos() # クリックした位置を取得
            # ボタンの範囲内ならば
            if BUTTON_X <= x <= BUTTON_X + BUTTON_WIDTH and BUTTON_Y <= y <= BUTTON_Y + BUTTON_HEIGHT and count < 11:
                count += 1
                for i in range(10):
                    # スロットをランダムに回転させる
                    slot1 = random.choice(symbols)
                    slot2 = random.choice(symbols)
                    slot3 = random.choice(symbols)
                    # 絵柄の角度をランダムに設定する
                    angle1 = random.randint(0, 360)
                    angle2 = random.randint(0, 360)
                    angle3 = random.randint(0, 360)

                    # スロットを画面に描画する
                    # rotate関数を使って、絵柄をangleの値だけ回転させた画像を作る
                    rotated1 = pygame.transform.rotate(slot1, angle1)
                    rotated2 = pygame.transform.rotate(slot2, angle2)
                    rotated3 = pygame.transform.rotate(slot3, angle3)
                    # scale関数を使って、回転させた画像をスロットのサイズに合わせて拡大縮小する
                    scaled1 = pygame.transform.scale(rotated1, (SLOT_WIDTH+(i*5), SLOT_HEIGHT+(i*5)))
                    scaled2 = pygame.transform.scale(rotated2, (SLOT_WIDTH+(i*5), SLOT_HEIGHT+(i*5)))
                    scaled3 = pygame.transform.scale(rotated3, (SLOT_WIDTH+(i*5), SLOT_HEIGHT+(i*5)))
                    # 拡大縮小した画像を画面に描画する
                    screen.blit(scaled1, (SLOT_X, SLOT_Y))
                    screen.blit(scaled2, (SLOT_X + SLOT_WIDTH, SLOT_Y))
                    screen.blit(scaled3, (SLOT_X + SLOT_WIDTH * 2, SLOT_Y))
                    # 画面を更新する
                    pygame.display.update()
                    time.sleep(0.1)

                # start = True

                # 絵柄が揃ったらメッセージを表示する
                if slot1 == slot2 == slot3:
                    if point<0:
                        message = "マイナス脱却! ポイント7倍"
                        point = abs(point)
                    else:
                        for i in range(20):
                            point += random.randrange(0,2400,50)
                            pointstr = "POINT:"+str(point)
                            point_text = f"{pointstr}ポイント追加!"
                            point_text = font.render(pointstr, True, RED)
                            screen.blit(point_text, (MESSAGE_X+(i*10), MESSAGE_Y+(i*10)))
                            pygame.display.update()
                            time.sleep(0.1)
                        message = "ポイント大量加算!"
                    point = point*7
                elif slot1 == slot2 or slot2 == slot3:
                    message = "ポイント+20"
                    point += 20
                else:
                    message = "あなたの負け... ポイント-100"
                    point -= 100
                
                if count == 11:
                    start_text = "結果"
                    nametmp = now.strftime('%y%m-%H%M%S')
                    tmp = {'name':nametmp, 'point':str(point)}
                    data.append(tmp)

    pointstr = "POINT:"+str(point)
    # 画面を白で塗りつぶす
    screen.fill(WHITE)
    
    # ランキング
    for i in range(len(data)):
        rank = f"{ data[i]['name'] }  ポイント:{ data[i]['point'] }"
        ranking_text = font.render(rank, True, RED)
        screen.blit(ranking_text, (RANK_X, RANK_Y+(i*30)))

    with open(fn, mode='w', encoding='utf_8') as file:
        json.dump(data, file, ensure_ascii=False,indent = 4)

    # # プログレスバーを画面に描画する
    # pygame.draw.rect(screen, BLACK, (BAR_X, BAR_Y, BAR_WIDTH, BAR_HEIGHT), 5) # 枠を描く
    # pygame.draw.rect(screen, GREEN, (BAR_X, BAR_Y, progress, BAR_HEIGHT)) # 塗りつぶしを描く

    # # プログレスバーの更新
    # while start:
    #     # 2秒間で満タンになるようにする
    #     progress += BAR_WIDTH / 20
    #     pygame.draw.rect(screen, GREEN, (BAR_X, BAR_Y, progress, BAR_HEIGHT)) # 塗りつぶしを描く
    #     pygame.display.update()
    #     time.sleep(0.1)
    #     # プログレスバーが満タンになったら
    #     if progress >= BAR_WIDTH:
    #         progress = 0
    #         # プログレスバーの更新を停止する
    #         start = False

    # スロットを画面に描画する
    # rotate関数を使って、絵柄をangleの値だけ回転させた画像を作る
    rotated1 = pygame.transform.rotate(slot1, angle1)
    rotated2 = pygame.transform.rotate(slot2, angle2)
    rotated3 = pygame.transform.rotate(slot3, angle3)
    # scale関数を使って、回転させた画像をスロットのサイズに合わせて拡大縮小する
    scaled1 = pygame.transform.scale(rotated1, (SLOT_WIDTH, SLOT_HEIGHT))
    scaled2 = pygame.transform.scale(rotated2, (SLOT_WIDTH, SLOT_HEIGHT))
    scaled3 = pygame.transform.scale(rotated3, (SLOT_WIDTH, SLOT_HEIGHT))
    # 拡大縮小した画像を画面に描画する
    screen.blit(scaled1, (SLOT_X, SLOT_Y))
    screen.blit(scaled2, (SLOT_X + SLOT_WIDTH, SLOT_Y))
    screen.blit(scaled3, (SLOT_X + SLOT_WIDTH * 2, SLOT_Y))

    # ボタンを画面に描画する
    pygame.draw.rect(screen, GREEN, (BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT))
    button_text = font.render(start_text, True, BLACK)
    screen.blit(button_text, (BUTTON_X + 20, BUTTON_Y + 10))

    # メッセージを画面に描画する
    message_text = font.render(message, True, RED)
    screen.blit(message_text, (MESSAGE_X, MESSAGE_Y))
    point_text = font2.render(pointstr, True, BLACK)
    screen.blit(point_text, (POINT_X, POINT_Y))

    # 画面を更新する
    pygame.display.update()
    clock.tick(10)
