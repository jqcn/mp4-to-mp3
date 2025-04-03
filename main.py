import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def jls_extract_def(self, master, text, row, column, padx, pady, width, command, columnspan):
    def __init__(self, master):
        self.master = master
        master.title("MP4转MP3转换器")
        # 创建界面组件
        self.label = tk.Label(master, text="选择MP4文件:")
        self.label.grid(row=0, column=0, padx=5, pady=5)
        self.file_entry = tk.Entry(master, width=40)
        self.file_entry.grid(row=0, column=1, padx=5, pady=5)
        self.browse_btn = tk.Button(master, text="浏览", command=self.select_file)
        self.browse_btn.grid(row=0, column=2, padx=5, pady=5)
        self.convert_btn = tk.Button(master, text="开始转换", command=self.convert_video)
        self.convert_btn.grid(row=1, column=1, padx=5, pady=5)
        self.status_label = tk.Label(master, text="准备就绪")
        self.status_label.grid(row=2, column=0, columnspan=3)
    return self

class VideoConverterApp:
    self = jls_extract_def(self, master, text, row, column, padx, pady, width, command, columnspan)
    def select_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("MP4文件", "*.mp4")]
        )
        if file_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)

    def convert_video(self):
        input_path = self.file_entry.get()
        if not input_path:
            messagebox.showerror("错误", "请先选择MP4文件")
            return      

        output_path = os.path.splitext(input_path)[0] + ".mp3"
        try:
            self.status_label.config(text="转换中...")
            self.master.update()
            # 使用ffmpeg进行转换
            command = [
                'ffmpeg',
                '-i', input_path,
                '-vn',         # 禁用视频流
                '-acodec', 'libmp3lame',
                '-q:a', '2',  # 音频质量
                output_path
            ]           

            subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            messagebox.showinfo("完成", f"转换成功！\n保存路径：{output_path}")
            self.status_label.config(text="转换完成")       

        except Exception as e:
            messagebox.showerror("错误", f"转换失败: {str(e)}")
            self.status_label.config(text="转换失败")


if __name__ == "__main__":
    root = tk.Tk()
    app = VideoConverterApp(root)
    root.mainloop()
