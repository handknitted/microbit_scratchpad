# Add your Python code here. E.g.
from microbit import *
import speech

number_words = {
    10: "wunty",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen"
}

full_range = "01234567898765432101234567890"
index = 0
while True:
    string_to_use = '%s:' % full_range[index: index+5]
    print("Index %s, String %s" % (index, string_to_use))
    image_string = (string_to_use * 5)[:-1]
    image_to_display = Image(image_string)
    display.show(image_to_display)
    number = number_words.get(index, index)
    intensity = (200 - (10 * index))
    speech.say("Index is %s" % number, pitch=intensity, speed=intensity, mouth=intensity, throat=intensity)
    sleep(1000)
    index += 1
    if index == 18:
        index = 0
