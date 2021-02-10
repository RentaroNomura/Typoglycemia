# Typoglycemia
Typoglycemia written in Python.
I tested this code only on macOS, if there are any issuses feel free to leave message in the isuues section of this repository.

# Library requirement
- Python 3
- tkinter
- pykakasi(available on pip)
- random
- unicodedata

# How to use
This program converts the text whitch you type in the text filed into Typoglycemia.

- **Mode**

I deployed two mode. English mode(EN) and Japanese mode(JP).

**EN mode:** This mode is default 

**JP mode:** You can select this mode from radioButton placed upper-right corner of the window. In this mode, you can input a space and characters in "Zenkaku" including "Kanji" but if you use "Kanji", It'll be automatically converted to "Hiragana". 

I used *pykakasi* to realize this feature and I'm alredy aware of some errors in convertion. just take it easy!

- **Buttons:**

I arranged four buttons. Here are the descriptions.

- convert: Typoglycemia of the text you typed will be created and shown on the second label simultaneously, but if you want to change the result you can push this button to change.

- hide: This button is used to hide the text you typed. If you want to see only Typoglycemia, you can use this button.

- show: Once you hide the text you typed, you can make it apper again by pushing this button.

- reset: This button allows you to reset all the widget on the tkinter window, the text field, the text you typed and Typoglycemia will be cleared and you can start over.



**Enjoy Typoglycemia**
