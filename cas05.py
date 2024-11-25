import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import cv2
import numpy as np
from PIL import Image, ImageTk
from ultralytics import YOLO

model = YOLO("cascade/yolov8n-cls.pt")
cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_alt.xml')

class CameraApp:

    # モザイクをいれるかどうか
    is_mosaic = False
    # 更新を止めるか
    is_stop = False

    def __init__(self, root):
        self.root = root
        self.root.title("Camera App")
        
        self.video_source = 0
        self.vid = cv2.VideoCapture(self.video_source)
        
        self.canvas = tk.Canvas(root, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()
        
        self.btn_frame = ttk.Frame(root)
        self.btn_frame.pack(anchor=tk.CENTER, expand=True)

        self.btn_snapshot = ttk.Button(self.btn_frame, text="撮影", command=self.snapshot)
        self.btn_snapshot.pack(side=tk.LEFT)

        self.btn_mosaic = ttk.Button(self.btn_frame, text="モザイクを入れる", command=self.mosaic)
        self.btn_mosaic.pack(side=tk.LEFT)

        self.btn_object_detection = ttk.Button(self.btn_frame, text="物体検出", command=self.object_detection)
        self.btn_object_detection.pack(side=tk.LEFT)

        self.btn_fileget = ttk.Button(self.btn_frame, text="ファイルを選択", command=self.fileget)
        self.btn_fileget.pack(side=tk.LEFT)

        self.seekbar = ttk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=self.seek)
        self.seekbar.pack(anchor=tk.CENTER, expand=True)
        self.seekbar.set(0)

        self.btn_stop = ttk.Button(root, text="停止", command=self.stop)
        self.btn_stop.pack(anchor=tk.CENTER, expand=True)

        self.delay = 15
        self.update()
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    # ファイルを取得
    def fileget(self):
        self.video_source = filedialog.askopenfilename()
        if self.video_source == "":
            self.video_source = 0
            messagebox.showinfo("Info", "No file selected!")
            return
        self.vid.release()
        self.vid = cv2.VideoCapture(self.video_source)
        self.canvas.config(width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.seekbar.config(to=int(self.vid.get(cv2.CAP_PROP_FRAME_COUNT)))
        self.seekbar.set(0)
        if not self.is_stop:
            self.update()  # 再生中であれば、update メソッドを再起動する
    
    def snapshot(self):
        ret, frame = self.vid.read()
        if ret:
            cv2.imwrite("frame-" + str(int(self.vid.get(cv2.CAP_PROP_POS_FRAMES))) + ".jpg", frame)
            messagebox.showinfo("Info", "Snapshot taken!")
    
    def mosaic(self):
        self.is_mosaic = not self.is_mosaic
        if self.is_mosaic:
            self.btn_mosaic.config(text="モザイクを外す")
        else:
            self.btn_mosaic.config(text="モザイクを入れる")
    
    def stop(self):
        self.is_stop = not self.is_stop
        if self.is_stop:
            self.btn_stop.config(text="再生")
        else:
            self.btn_stop.config(text="停止")
            self.update()  # 再生ボタンが押されたら update メソッドを再起動する
    
    def object_detection(self):
        ret, frame = self.vid.read()
        if ret:
            results = model(frame, conf=0.5)
            result = results[0]
            plot = result.plot()

            plot_rgb = cv2.cvtColor(plot, cv2.COLOR_BGR2RGB)
            cv2.imwrite("object-detection-" + str(int(self.vid.get(cv2.CAP_PROP_POS_FRAMES))) + ".jpg", plot_rgb)
            messagebox.showinfo("Info", "Object detection completed!")
    
    def update(self):
        # 停止ボタンが押されたら何もしない
        if self.is_stop:
            return
        
        ret, frame = self.vid.read()
        if ret:
            if self.is_mosaic:
                face = cascade.detectMultiScale(frame)
                for x, y, w, h in face:
                    mosaic = cv2.resize(frame[y:y+h, x:x+w], (w//50, h//50))
                    frame[y:y+h, x:x+w] = cv2.resize(mosaic, (w, h))
        
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame_rgb))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.seekbar.set(self.vid.get(cv2.CAP_PROP_POS_FRAMES))
        self.root.after(self.delay, self.update)
    
    def seek(self, value):
        frame_number = int(float(value))
        self.vid.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = self.vid.read()
        
        if ret:
            if self.is_mosaic:
                face = cascade.detectMultiScale(frame)
                for x, y, w, h in face:
                    mosaic = cv2.resize(frame[y:y+h, x:x+w], (w//50, h//50))
                    frame[y:y+h, x:x+w] = cv2.resize(mosaic, (w, h))
        
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame_rgb))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
    
    def on_closing(self):
        self.vid.release()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root)
    root.mainloop()