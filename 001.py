import time
import math
import numpy as np
import matplotlib.pyplot as plt
import requests

url = "https://notify-api.line.me/api/notify"
access_token = 'yV5ZQBy1ivBKmXqiTUBrVayOicKs7ZunFKJRwDTRqcg'
headers = {'Authorization': 'Bearer ' + access_token}

# パラメータ設定
v0 = 20.0    # 初速度(m/s)
theta = 60   # 水平方向から上方にθ(deg)
g = 9.8      # 重力加速度m/s^2
filetime = time.perf_counter() # ファイル名に使う時間

# シミュレーション
dt = 0.1  # 位置計算の時間間隔
iter = 80 # シミュレーション繰返し回数

theta = math.radians(theta) # deg -> rad

arr_x=[0]*iter # X位置を格納するリストの初期化
arr_y=[0]*iter # Y位置　〃

arr_x[0] = x = 0  # Xの初期位置
arr_y[0] = y = 0  # Yの 〃
vx = v0 * math.cos(theta) # X成分の初期速度 
vy = v0 * math.sin(theta) # Y成分 〃

fig = plt.figure()
a = fig.add_subplot(111)
a.set_xlim(0, 90)
a.set_ylim(0, 20)

# シミュレーション
for i in range(1,iter):
  vy = vy - g * dt # Y方向の速度更新
  x = x + vx * dt  # X位置の計算
  y = y + vy * dt  # Y位置 〃

  # 地面衝突の反発 (バウンド) の処理
  if y < 0:
    y = 0
    vy = -vy * 0.8  # 反発係数

  arr_x[i] = x
  arr_y[i] = y
  m1 = f"{i}秒経過しました。物体の位置はx={x},y={y}です。"
  if y == 0:
    m1 = m1+"跳ね返りました。"
  a.plot(x,y,'*')
  plt.savefig(f"otherpic/{i}.png")
  payload = {'message': m1}
  files = {'imageFile': open(f"otherpic/{i}.png", 'rb')}
  r = requests.post(url, headers=headers, params=payload, files=files)
  
  time.sleep(4.0)

# 可視化（現状でここから先は理解不要）
fig,ax = plt.subplots(dpi=120)
ax.scatter(arr_x,arr_y,marker='o',s=20,alpha=0.5)
ax.axhline(0,c='black',lw=0.5)
ax.set_aspect('equal', adjustable='box')
ax.set_ylim(-1,20)
plt.savefig(f"otherpic/{filetime}.png")

message = f"写真を撮影しました。最終的な物体の位置はx={x},y={y}です。"
image = f"otherpic/{filetime}.png"
payload = {'message': message}
files = {'imageFile': open(image, 'rb')}
r = requests.post(url, headers=headers, params=payload, files=files)

plt.show()