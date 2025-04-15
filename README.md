# Mp4-translate-to-Gif
# Video to GIF Converter

一个简单易用的视频转GIF工具，基于Python开发的图形界面应用程序。

## 功能特点

- 支持将MP4、AVI、MOV等格式的视频转换为GIF动图
- 可自定义GIF参数：
  - 截取时长（秒）
  - 帧率（FPS）
  - 输出宽度（像素）
- 友好的图形界面，操作简单直观
- 实时转换状态显示

## 使用说明

1. 点击"Browse"按钮选择要转换的视频文件
2. 选择GIF保存位置
3. 设置转换参数（可选）：
   - Duration：设置GIF时长，默认5秒
   - FPS：设置GIF帧率，默认15帧/秒
   - Width：设置GIF宽度，默认720像素
4. 点击"Convert"按钮开始转换
5. 等待转换完成，转换状态会实时显示

## 环境要求

- Python 3.6+
- 依赖库：
  - tkinter：GUI界面库
  - moviepy：视频处理库

## 安装步骤

1. 确保已安装Python 3.6或更高版本
2. 安装依赖库：
   ```bash
   pip install moviepy
   ```
3. 运行程序：
   ```bash
   python GUI.py
   ```

## 注意事项

- 支持的视频格式：MP4、AVI、MOV
- 转换时间取决于视频大小和设置的参数
- 建议根据需要调整FPS和宽度参数，以平衡GIF质量和文件大小
