from logging import root
import os
import shutil
import threading

from tkinter import *

origin_path = "C:\\Users\\balic\\AppData\\LocalLow\\Games Damian made\\Slasher_s Keep\\"
target_path = "C:\\Users\\balic\\Desktop\\Slashers Keep save files\\"

global is_on
is_on = False


def read_origin_dir():
    dir_content = os.listdir(origin_path)
    return dir_content


def read_target_dir():
    dir_content = os.listdir(target_path)
    return dir_content


def navigate_target():
    dir_list = read_target_dir()
    # for i in range(0, len(dir_list)):
    #     dir_list[i] = int(dir_list[i])
    return str(len(dir_list)-1), str(len(dir_list))


def verify_time():
    dir_list = read_origin_dir()
    time = os.path.getmtime(origin_path + dir_list[0])
    return time


def copy_files():
    dir_list = read_origin_dir()
    last_file = (navigate_target()[0]) + "\\"
    # print(last_file)

    for i in dir_list:
        o = origin_path + i
        t = target_path + last_file + i
        shutil.copyfile(o, t)


def execute_on():
    global is_on
    timer = threading.Timer(5.0, execute_on)

    origin_time = os.path.getmtime(origin_path)
    target_time = os.path.getmtime(target_path)

    last_file = navigate_target()[1]

    if is_on == True:
        timer.start()
        state = "ON"
        print(state)
        if origin_time > target_time:
            os.mkdir(target_path + last_file)
            copy_files()
        else:
            status = "ok"
            print(status)
            return status
    else:
        timer.cancel()
        state = "OFF"
        print(state)


# def thread():
#     global is_on
#     timer = threading.Timer(5.0, execute_on)

#     if is_on == True:
#         timer.start()
#         # execute()
#         state = "ON"
#         print(state)
#     else:
#         timer.cancel()
#         state = "OFF"
#         print(state)


# def off_thread():
#     on_thread().cancel()
#     state = "OFF"
#     print(state)
#     return state

root = Tk()
root.title("Slasher's Keep - savefile cheat")
img = PhotoImage(file="sk.png")
root.tk.call("wm", "iconphoto", root._w, img)
root.geometry("200x200")


my_label = Label(root, text="OFF", fg="red", font=("Helvetica", 32))
my_label.pack(pady=10)


def switch():
    global is_on

    if is_on == False:
        is_on = True
        on_button.config(image=on)
        my_label.config(text="ON", fg="green",)
        execute_on()

    else:
        is_on = False
        on_button.config(image=off)
        my_label.config(text="OFF", fg="red",)
        execute_on()


on = PhotoImage(file="on.png")
off = PhotoImage(file="off.png")

on_button = Button(root, image=off, bd=0, command=switch)
on_button.pack(pady=10)

root.mainloop()
# def main():
#     on_thread()


# if __name__ == "__main__":
#     main()
