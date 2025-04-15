# -*- coding: utf-8 -*-
from moviepy.editor import VideoFileClip
import os

# 设置工作目录下的路径
video_path = r"D:\vivado\input.mp4"  # 使用原始字符串来处理路径
gif_path = r"D:\vivado\output.gif"

# 加载视频，截取前5秒，调整宽度为720
clip = VideoFileClip(video_path).subclip(0, 5).resize(width=720)

# 输出高清GIF
clip.write_gif(gif_path, fps=15)

print(f"GIF has been saved to: {gif_path}")
