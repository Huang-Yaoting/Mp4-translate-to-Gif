# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, filedialog
from moviepy.editor import VideoFileClip
import os

class VideoToGifConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Video to GIF Converter")
        self.root.geometry("700x400")
        self.root.configure(bg="#f0f0f0")
        
        # 创建主框架
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 样式设置
        style = ttk.Style()
        style.configure("Custom.TButton", padding=10, font=("Arial", 10))
        style.configure("Custom.TLabel", font=("Arial", 11))
        
        # 输入文件选择
        ttk.Label(main_frame, text="Select Video File:", style="Custom.TLabel").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.input_path = tk.StringVar()
        input_entry = ttk.Entry(main_frame, textvariable=self.input_path, width=50)
        input_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(main_frame, text="Browse", style="Custom.TButton", command=self.select_input).grid(row=0, column=2, padx=5, pady=5)
        
        # 输出文件选择
        ttk.Label(main_frame, text="Save GIF to:", style="Custom.TLabel").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.output_path = tk.StringVar()
        output_entry = ttk.Entry(main_frame, textvariable=self.output_path, width=50)
        output_entry.grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(main_frame, text="Browse", style="Custom.TButton", command=self.select_output).grid(row=1, column=2, padx=5, pady=5)
        
        # 参数设置框架
        params_frame = ttk.LabelFrame(main_frame, text="Parameters", padding="10")
        params_frame.grid(row=2, column=0, columnspan=3, pady=20, sticky=(tk.W, tk.E))
        
        # 截取时长设置
        ttk.Label(params_frame, text="Duration (sec):", style="Custom.TLabel").grid(row=0, column=0, pady=5)
        self.duration = ttk.Entry(params_frame, width=10)
        self.duration.insert(0, "5")
        self.duration.grid(row=0, column=1, pady=5)
        
        # FPS设置
        ttk.Label(params_frame, text="FPS:", style="Custom.TLabel").grid(row=0, column=2, padx=20, pady=5)
        self.fps = ttk.Entry(params_frame, width=10)
        self.fps.insert(0, "15")
        self.fps.grid(row=0, column=3, pady=5)
        
        # 宽度设置
        ttk.Label(params_frame, text="Width (px):", style="Custom.TLabel").grid(row=0, column=4, padx=20, pady=5)
        self.width = ttk.Entry(params_frame, width=10)
        self.width.insert(0, "720")
        self.width.grid(row=0, column=5, pady=5)
        
        # 转换按钮
        convert_btn = ttk.Button(main_frame, text="Convert", style="Custom.TButton", command=self.convert)
        convert_btn.grid(row=3, column=0, columnspan=3, pady=20)
        
        # 状态标签
        self.status_label = ttk.Label(main_frame, text="", style="Custom.TLabel")
        self.status_label.grid(row=4, column=0, columnspan=3)
        
    def select_input(self):
        filename = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mov")])
        if filename:
            self.input_path.set(filename)
            
    def select_output(self):
        filename = filedialog.asksaveasfilename(defaultextension=".gif", filetypes=[("GIF Files", "*.gif")])
        if filename:
            self.output_path.set(filename)
            
    def convert(self):
        try:
            input_path = self.input_path.get()
            output_path = self.output_path.get()
            duration = float(self.duration.get())
            fps = int(self.fps.get())
            width = int(self.width.get())
            
            if not input_path or not output_path:
                self.status_label.config(text="Please select input and output file paths!")
                return
                
            self.status_label.config(text="Converting...")
            self.root.update()
            
            clip = VideoFileClip(input_path).subclip(0, duration).resize(width=width)
            clip.write_gif(output_path, fps=fps)
            
            self.status_label.config(text=f"Conversion complete! GIF saved to: {output_path}")
        except Exception as e:
            self.status_label.config(text=f"Conversion failed: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoToGifConverter(root)
    root.mainloop()