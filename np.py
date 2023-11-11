import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import IPython

# パラメータ設定
v0 = 20.0    # 初速度(m/s)
theta = 60   # 水平方向から上方にθ(deg)に向けて投射
g = 9.8      # 重力加速度m/s^2

# シミュレーションの準備・設定
dt = 0.1  # 位置を計算する時間間隔
iter = 80 # シミュレーション繰返し回数

theta = math.radians(theta) # deg -> rad 変換

arr_x=[0]*iter # X位置を格納するリストの初期化
arr_y=[0]*iter # Y位置　〃

assert len(arr_x) == len(arr_y)

arr_x[0] = x = 0  # t=0 のX位置
arr_y[0] = y = 0  #  〃 のY位置

vx = v0 * math.cos(theta) # 初速度のX成分
vy = v0 * math.sin(theta) # 　〃　のY成分

# シミュレーション
for i in range(1,iter):
  vy = vy - g * dt # Y方向の速度更新
  x = x + vx * dt  # X位置の更新計算
  y = y + vy * dt  # Y位置 〃

  # 地面衝突の反発 (バウンド) の処理
  if y < 0:
    y = 0
    vy = -vy * 0.8  # 反発係数

  arr_x[i] = x # 更新されたX位置をリストに格納
  arr_y[i] = y #   〃    Y位置を  〃

# アニメーション
fig,ax = plt.subplots(dpi=120)
ss = 5
def frame(i):
  ax.clear()
  ax.set_aspect('equal', adjustable='box')
  ax.set_ylim(-1,30)
  ax.set_xlim(0, round(max(arr_x),-1)+5)
  ax.axhline(0,c='black',lw=0.5)
  ax.text(0.01,0.98,f't={i*dt:.2f}',va='top',transform=ax.transAxes)
  for t in range(ss):
    ax.scatter(arr_x[i+t],arr_y[i+t],
               marker='o',s=20,c='tab:blue',alpha=t/(ss+1))

ani = animation.FuncAnimation(fig, frame, interval=100,frames=iter-ss)
plt.close()

IPython.display.HTML(ani.to_jshtml())
# 講義資料のIndexに移動