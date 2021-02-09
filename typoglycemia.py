import random
import tkinter as tk
from tkinter import font
from tkinter import messagebox
from pykakasi import kakasi
import unicodedata

background_color = "#262829"
new_line_limits = 70
new_line_limits_zenkaku = 32

max_len = 200
max_len_zenkaku = 74

main_window = tk.Tk()
main_window.configure(background=background_color)

input = tk.StringVar()
monitor = tk.StringVar()
typoglycemia = tk.StringVar()
lang_status = tk.IntVar()

def all_hiragana(text):
    status = lang_status.get()

    if status == 1: #JP
        myKakasi = kakasi()

        myKakasi.setMode('J', 'H')
        converter = myKakasi.getConverter()
        converted_text = converter.do(text)


    if status == 0:  #EN
        text = text.replace("　", " ")
        converted_text = text

    main_window.update_idletasks()
    return converted_text

def filter(input_sentence):
    word_split_list = input_sentence.split()
    filted_sentence = ""
    old_filted_sentence = ""
    status = lang_status.get()

    if status == 0: #EN

        for word_selector in range(len(word_split_list)):
            if word_split_list[word_selector] == "　":
                word_split_list[word_selector] = " "

            if word_split_list[word_selector] == "*":
                filted_sentence = old_filted_sentence + word_split_list[word_selector]
                old_filted_sentence = filted_sentence

            else:
                filted_sentence = old_filted_sentence + word_split_list[word_selector]
                old_filted_sentence = filted_sentence + " "

    elif status == 1: #JP

        for word_selector in range(len(word_split_list)):
            if word_split_list[word_selector] == "　":
                word_split_list[word_selector] = " "

            filted_sentence = old_filted_sentence + word_split_list[word_selector]
            old_filted_sentence = filted_sentence + "　"

    return filted_sentence

def call_back(*args): #monitor

    monitor_data = input.get()

    monitor_data_hiragana_converted = all_hiragana(monitor_data)
    monitor_data_hiragana_converted = adjuster(monitor_data_hiragana_converted, new_line_limits, new_line_limits_zenkaku)
    main_window.update_idletasks()
    monitor.set(monitor_data_hiragana_converted)


def convert(*args): #typoglycemia

    typoglycemia.set(adjuster(make_typoglycemia(all_hiragana(input.get())), new_line_limits, new_line_limits_zenkaku))

def gui_init(window_title, window_size):

    main_window.title(str(window_title))
    main_window.geometry(str(window_size))
    main_window.resizable(width=False, height=True)

def gui_build():

    main_frame = tk.Frame(main_window, background=background_color)

    font_heading = font.Font(family='Helvetica', size=23, weight='bold')
    font_body = font.Font(family='Helvetica', size=20)

    heading_frame = tk.Frame(main_frame, background=background_color)
    heading_text = tk.Label(heading_frame, text="Typoglycemia\n", font=font_heading, background=background_color)

    body_frame = tk.Frame(main_frame, background=background_color)

    description_frame = tk.Frame(body_frame, background=background_color)

    body_text = tk.Label(description_frame, text="Please type the sentence below to convert into Typoglycemia    ", font=font_body, background=background_color)

    radiobutton_frame = tk.Frame(description_frame, background=background_color)
    lang_status.set(0)
    body_lang_button_en = tk.Radiobutton(radiobutton_frame, value=0, variable=lang_status, text="EN", foreground="white", background=background_color, highlightbackground=background_color)
    body_lang_button_jp = tk.Radiobutton(radiobutton_frame, value=1, variable=lang_status, text="JP", foreground="white", background=background_color, highlightbackground=background_color)

    body_textfiled = tk.Entry(body_frame, textvariable=input)

    def on_write(*args):

        status = lang_status.get()

        if status == 0: #EN
            limited_input = input.get()
            if len(limited_input) > max_len:
                input.set(limited_input[:max_len])
                messagebox.showwarning("Error", "ERROR\n input is full")

        if status == 1: #JP
            limited_input = input.get()
            if len(limited_input) > max_len_zenkaku:
                input.set(limited_input[:max_len_zenkaku])
                messagebox.showwarning("Error", "ERROR\n input is full")


    input.trace("w", on_write)
    input.trace('w', call_back)
    input.trace('w', convert)

    body_grid_frame = tk.Frame(body_frame, background=background_color)
    body_input_monitor = tk.Label(body_grid_frame, textvariable=monitor, font=font_heading, background=background_color, anchor=tk.W, justify=tk.LEFT)

    buttons_frame = tk.Frame(body_frame)

    buttons_convert_button = tk.Button(buttons_frame, text="convert", command=lambda: convert(), foreground=background_color, background=background_color, highlightbackground=background_color)
    buttons_reset_button = tk.Button(buttons_frame, text="reset", command=lambda: reset(), foreground="red", background=background_color, highlightbackground=background_color)
    buttons_hide_button = tk.Button(buttons_frame, text="hide", command=lambda: hide(), foreground=background_color, highlightbackground=background_color, background=background_color)
    buttons_show_button = tk.Button(buttons_frame, text="show", command=lambda: show(), foreground=background_color, highlightbackground=background_color, background=background_color)

    body_typoglycemia = tk.Label(body_frame, textvariable=typoglycemia, font=font_heading, background=background_color, anchor=tk.W, justify=tk.LEFT)

    body_monitor_label = tk.Label(body_frame, text="nomal text:", font=font_heading, background=background_color, anchor=tk.W)
    body_typloglycemia_label = tk.Label(body_frame, text="typoglycemia:", font=font_heading, background=background_color, anchor=tk.W)

    body_space_1 = tk.Label(body_frame, text="\n", background=background_color)
    body_space_2 = tk.Label(body_frame, text="\n", background=background_color)

    def reset():

        body_textfiled.delete(0, tk.END)
        body_input_monitor.grid()
        main_window.update_idletasks()

    def hide():
        body_input_monitor.grid_remove()
        main_window.update_idletasks()

    def show():
        body_input_monitor.grid()
        main_window.update_idletasks()

    main_frame.pack(fill='x')

    heading_frame.pack()
    heading_text.pack()

    body_frame.pack(fill='x')

    description_frame.pack()

    body_text.pack(anchor=tk.W, side=tk.LEFT)

    radiobutton_frame.pack()

    body_lang_button_en.pack()
    body_lang_button_jp.pack(side=tk.LEFT)

    body_textfiled.pack(fill='x')

    body_monitor_label.pack(anchor=tk.W)

    body_grid_frame.pack(anchor=tk.W)
    body_input_monitor.grid()

    body_space_1.pack()

    body_typloglycemia_label.pack(anchor=tk.W)
    body_typoglycemia.pack(anchor=tk.W)
    body_space_2.pack()

    buttons_frame.pack(anchor=tk.W)
    buttons_convert_button.pack(side=tk.LEFT)
    buttons_hide_button.pack(side=tk.LEFT)
    buttons_show_button.pack(side=tk.LEFT)
    buttons_reset_button.pack(side=tk.LEFT)

    main_window.mainloop()

def adjuster(input, words, words_zenkaku):
    input_length = len(input)
    adjusted_input = ""

    status = lang_status.get()

    quotient = input_length//words
    quotient_zenkaku = input_length//words_zenkaku
    remainder = input_length%words
    remainder_zenkaku = input_length%words_zenkaku

    if status == 1: #JP

        if input_length >= words_zenkaku:

            if remainder_zenkaku >= 0:
                for index in range(quotient_zenkaku):
                    if (index+1) == 1:
                        adjusted_input = input[:((index+1)*words_zenkaku)] + "\n" + input[((index+1)*words_zenkaku):]
                    else:
                        adjusted_input = adjusted_input[:((index+1)*words_zenkaku+(index))] + "\n" + adjusted_input[((index+1)*words_zenkaku+(index)):]

                return adjusted_input
        else:
            return input

    elif status == 0: #EN

        if input_length >= words:

            if remainder >= 0:
                for index in range(quotient):
                    if (index+1) == 1:
                        adjusted_input = input[:((index+1)*words)] + "\n" + input[((index+1)*words):]
                    else:
                        adjusted_input = adjusted_input[:((index+1)*words+(index))] + "\n" + adjusted_input[((index+1)*words+(index)):]

                return adjusted_input
        else:
            return input
    else:
        messagebox.showwarning("Error", "ERROR\n format eroor")

def make_typoglycemia(input_sentence):

    status = lang_status.get()

    if input_sentence == "":
        typoglycemia = ""
        return typoglycemia

    word_split_list = input_sentence.split()
    old_word = ""

    if status == 0: #EN

        for word_selector in range(len(word_split_list)):
            word_split_list[word_selector] = shuffle(word_split_list[word_selector])

            typoglycemia = old_word + word_split_list[word_selector]
            old_word = typoglycemia + " "

    if status == 1: #JP

        for word_selector in range(len(word_split_list)):
            word_split_list[word_selector] = shuffle(word_split_list[word_selector])

            typoglycemia = old_word + word_split_list[word_selector]
            old_word = typoglycemia + "　"

    return typoglycemia

def shuffle(input_word):

    space_replace =False

    if input_word == "　":
        space_replace = Trued
        input_word = input_word.replace("　", " ")

    if input_word =="":
        shuffled_word = ""
        return shuffled_word

    input_word_length = len(input_word)
    body = ""
    header = str(input_word[0])
    footer = str(input_word[input_word_length-1])

    body_num = list(range(1,input_word_length-1))
    random.shuffle(body_num)

    old_word = ""

    if input_word_length == 1:
        return input_word

    if input_word_length == 4:
        body = input_word[2] + input_word[1]
        shuffled_word = header + body + footer
        return shuffled_word

    for num_selector in range(0,input_word_length-2):
        body = old_word + input_word[body_num[num_selector]]
        old_word = body

    shuffled_word = header + body + footer

    if space_replace == True:
        shuffled_word = shuffled_word.replace(" ","　")
        space_replace = False

    return shuffled_word

gui_init("Typoglycemia", "800x550")

gui_build()
