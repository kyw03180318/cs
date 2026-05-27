import tkinter as tk

window = tk.Tk()
window.title("이름입력")
window.geometry("600x200")
en_name = tk.Entry(window)
btn_name = tk.button(window, text="클릭")
lbl_name = tk.Label(window, text ("이름입력:"))

lbl_name.pack()
en_name.pack()
btn_name.pack()
window.mainloop()
