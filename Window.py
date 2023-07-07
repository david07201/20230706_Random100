import tkinter as tk


class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Random100')
        self.config(bg='#D0D0D0')
        self.width = 500
        self.height = 500

        self.withdraw()

        kwargs = {
            'master': self,
            'bg': '#D0D0D0',
        }
        self.label1 = tk.Label(text='label1', font=('標楷體', 16), **kwargs)
        self.label2 = tk.Label(text='label1', font=('標楷體', 16), **kwargs)
        self.label3 = tk.Label(text='label2', font=('標楷體', 144), **kwargs)
        self.label4 = tk.Label(text='label3', font=('標楷體', 16), **kwargs)

        self.label1.pack(anchor='w')
        self.label2.pack(anchor='w')
        self.label3.pack(padx=5, pady=10, expand=True)
        self.label4.pack(side='bottom', anchor='e')

        frame_width = self.winfo_rootx() - self.winfo_x()
        win_width = self.width + 2 * frame_width
        titlebar_height = self.winfo_rooty() - self.winfo_y()
        win_height = self.height + titlebar_height + frame_width
        x = (self.winfo_screenwidth() - win_width) // 2
        y = (self.winfo_screenheight() - win_height) // 2
        self.geometry(f'{self.width}x{self.height}+{x}+{y}')
        self.deiconify()


if __name__ == '__main__':
    main = Window()
    main.mainloop()