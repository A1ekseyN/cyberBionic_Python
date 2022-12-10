import art
from colorama import Back, Fore, Style


def logo():
    return print(art.text2art(f"Hello, my friend.", font="cybermedum"))


def hello():
    return print("Я чат-бот. Могу предложить несколько варинтов для взаимодействия:")
