import os
import customtkinter as ctk


DIRECTORY = os.path.dirname(os.path.abspath(__file__))
out_numeration = False
in_numeration = False
readed = False


def out_checkbox_event(cb: ctk.CTkCheckBox):
    global out_numeration
    if cb.get() == 1:
        out_numeration = True
    else:
        out_numeration = False


def read_file():
    global readed
    if not readed:
        fr = open('data.txt', 'r', encoding='utf-8')
        readed = True
        fields = fr.readlines()
        textbox = []
        for c in fields:
            plchdr = c
            textbox.append(ctk.CTkEntry(window,
                                        border_width=4,
                                        height=20,
                                        width=400,
                                        placeholder_text=plchdr))

        for tb in range(len(textbox)):
            textbox[tb].place(x=220, y=5 + tb * 25)

        button = ctk.CTkButton(
            window,
            text='Создать файл',
            command=lambda: file_create(textbox)
        )
        button.place(x=5, y=65)

        out_checkbox = ctk.CTkCheckBox(window,
                                       text='Нумеровать данные в файле',
                                       command=lambda: out_checkbox_event(out_checkbox))
        out_checkbox.place(x=5, y=95)
    else:
        pass


# Надо будет сделать чтение пронумерованных параметров и ставить их по порядку (или не надо, надо будет спросить)
def read_numerated_file():
    fr = open('data.txt', 'r', encoding='utf-8')
    fields = fr.readlines()
    textbox = []
    for c in fields:
        plchdr = c
        textbox.append(ctk.CTkEntry(window,
                                    border_width=4,
                                    height=20,
                                    width=400,
                                    placeholder_text=plchdr))

    for tb in range(len(textbox)):
        textbox[tb].place(x=220, y=5+(tb)*25)

    button = ctk.CTkButton(
        window,
        text='Создать файл',
        command=lambda: file_create(textbox)
    )
    button.place(x=5, y=35)


def file_create(line):
    lines = []
    for tn in line:
        lines.append(tn.get())
    with open('mark.txt', 'w') as f:
        if out_numeration:
            for n in range(len(lines)):
                print(str(n+1) + ' ' + lines[n], file=f)
        else:
            for n in range(len(lines)):
                print(lines[n], file=f)
# str(n+1) + ' ' +
# , encoding='cp1252'
# count = 4


window = ctk.CTk()
window.title('Составление файла для маркиратора')
window.geometry('625x510')

in_checkbox = ctk.CTkCheckBox(window, text='Данные пронумерованны')
# in_checkbox.place(x=5, y=35)

buttonGet = ctk.CTkButton(
    window,
    text='Получить поля для заполнения',
    command=lambda: read_file()
)
buttonGet.place(x=5, y=5)

window.mainloop()
