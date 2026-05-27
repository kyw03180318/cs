import tkinter as tk

def click_name_button():
    name=en_name.get()
    lbl_name.config(text=f"제이름은 {name}입니다")

window = tk.Tk()
window.title("클라우드")
window.geometry("600x200")

en_name = tk.Entry(window)
btn_name = tk.Button(window, text="클릭",command=click_name_button)
lbl_name = tk.Label(window, text=("이름입력:"))

lbl_name.pack()
en_name.pack()
btn_name.pack()
window.mainloop()
