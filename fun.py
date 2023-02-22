import random


def create_list(quantity):
    ls = []
    for i in range(quantity):
        ls.append(random.randint(5, 15))
    return ls


def check_ext(filename):
    lst = ["exe", "bat", "html", "png", "mp4", "psd", "mp3"]
    if filename[-3:] in lst or filename[-4:] in lst:
        return "Correct extension"
    else:
        return "Incorrect extension"
