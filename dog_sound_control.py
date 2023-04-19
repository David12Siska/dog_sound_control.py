# Название файла: dog_sound_control.py

import random

sounds = ["Гав", "Тяф", "Вуфф", "Ррр"]

while True:
    command = input("Введите команду ('заткнись' для завершения): ")
    if command == "заткнись":
        break
    else:
        sound = random.choice(sounds)
        print(f"{sound}!")
