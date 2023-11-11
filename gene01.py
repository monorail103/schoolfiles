# Bing AI テスト
# pythonのpygameライブラリやpysimpleguiライブラリ、tkinterライブラリなどを用いて、カービィに出てくる「刹那の見切り」のようなゲームのプログラムを作成してください
# pygameライブラリのインポート
import pygame
import time
from pygame.locals import *
import random

# pygameの初期化
pygame.init()


# ゲーム画面のサイズとタイトルを設定
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("刹那の見切り")

# ゲームに使用する色を定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# ゲームに使用するフォントを定義
font = pygame.font.Font('datas/M_PLUS_1p/MPLUS1p-Bold.ttf', 60)
font_small = pygame.font.Font('datas/M_PLUS_1p/MPLUS1p-Regular.ttf', 30)

# ゲームに使用する画像を読み込む
kirby = pygame.image.load("images/baby01.png")
dedede = pygame.image.load("images/dedede.jpg")
waddledee = pygame.image.load("images/dedede.jpg")
kirby = pygame.transform.scale(kirby, (100, 100))
dedede = pygame.transform.scale(dedede, (100, 100))
waddledee = pygame.transform.scale(waddledee, (100, 100))

# ゲームに使用する音声を読み込む
# slash = pygame.mixer.Sound("slash.wav")
# fail = pygame.mixer.Sound("fail.wav")
# bgm = pygame.mixer.music.load("bgm.mp3")

# ゲームの状態を管理する変数
game_state = "start" # ゲームの状態（start, play, win, lose）
score = 0 # スコア
delay = 0 # 反応までの時間差
level = 1 # 難易度
enemy = None # 敵のキャラクター
timer = 0 # タイマー
wait = 0 # 待ち時間
signal = False # 合図
time_sta = time.time() # 反応までの時間差を計算するための変数1

# ゲームループ
running = True
while running:
    # イベント処理
    for event in pygame.event.get():
        # ゲーム画面を閉じるとき
        if event.type == pygame.QUIT:
            running = False
        # キーを押したとき
        if event.type == pygame.KEYDOWN:
            # スペースキーを押したとき
            if event.key == pygame.K_SPACE:
                # ゲームの状態がstartのとき
                if game_state == "start":
                    # ゲームの状態をplayに変更
                    game_state = "play"
                    # BGMを再生
                    # pygame.mixer.music.play(-1)
                    # 敵のキャラクターをランダムに選択
                    enemy = random.choice([dedede, waddledee])
                    # 待ち時間をランダムに設定
                    wait = random.randint(100, 720)
                    time_sta = time.time()
                # ゲームの状態がplayのとき
                elif game_state == "play":
                    # 合図が出たとき
                    if signal:
                        # スラッシュ音を再生
                        # slash.play()
                        # ゲームの状態をwinに変更
                        game_state = "win"
                        time_end = time.time()
                        # 時間差を計算
                        delay = round(time_end-time_sta,5)
                        # スコアを加算
                        score += 1
                        # 難易度を上げる
                        level += 1
                    # 合図が出ていないとき
                    else:
                        # 失敗音を再生
                        # fail.play()
                        # ゲームの状態をloseに変更
                        game_state = "lose"
                # ゲームの状態がwinまたはloseのとき
                elif game_state in ["win", "lose"]:
                    # ゲームの状態をstartに戻す
                    game_state = "start"
                    # タイマーと合図をリセット
                    timer = 0
                    signal = False

    # ゲームのロジック
    # ゲームの状態がplayのとき
    if game_state == "play":
        # タイマーを増やす
        timer += 1
        # タイマーが待ち時間に達したとき
        if timer == wait:
            # 合図を出す
            signal = True

    # ゲームの描画
    # 画面を白色で塗りつぶす
    screen.fill(WHITE)
    # ゲームの状態がstartのとき
    if game_state == "start":
        # タイトルと説明を表示
        title = font.render("刹那の見斬り", True, BLACK)
        screen.blit(title, (400 - title.get_width() // 2, 100))
        message = font_small.render("スペースキーでスタート", True, BLACK)
        screen.blit(message, (400 - message.get_width() // 2, 300))
    # ゲームの状態がplayのとき
    elif game_state == "play":
        # カービーと敵のキャラクターを表示
        screen.blit(kirby, (100, 200))
        screen.blit(enemy, (600, 200))
        # 合図が出たとき
        if signal:
            # 「!」マークを表示
            mark = font.render("!", True, RED)
            screen.blit(mark, (400 - mark.get_width() // 2, 200))
    # ゲームの状態がwinのとき
    elif game_state == "win":
        # カービーと敵のキャラクターを表示
        screen.blit(kirby, (100, 200))
        screen.blit(enemy, (600, 200))
        # 「!」マークを表示
        mark = font.render("!", True, RED)
        screen.blit(mark, (400 - mark.get_width() // 2, 200))
        # 勝利メッセージとスコアを表示
        message = font.render("勝ち！", True, GREEN)
        screen.blit(message, (400 - message.get_width() // 2, 100))
        score_text = font_small.render(f"スコア：{score}", True, BLACK)
        time_text = font_small.render(f"反応時間：{delay}", True, BLACK)
        screen.blit(score_text, (400 - score_text.get_width() // 2, 300))
        screen.blit(time_text, (400 - time_text.get_width() // 2, 400))
    # ゲームの状態がloseのとき
    elif game_state == "lose":
        # カービーと敵のキャラクターを表示
        screen.blit(kirby, (100, 200))
        screen.blit(enemy, (200, 200))
        # 敗北メッセージとスコアを表示
        message = font.render("負け…", True, BLUE)
        screen.blit(message, (400 - message.get_width() // 2, 100))
        score_text = font_small.render(f"スコア：{score}", True, BLACK)
        screen.blit(score_text, (400 - score_text.get_width() // 2, 300))

    # 画面を更新
    pygame.display.update()

# pygameの終了
pygame.quit()
