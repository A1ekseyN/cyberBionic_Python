import random


story_list = []


with open('story.txt', 'r', encoding='utf-8') as story_file:
    for row in story_file:
        story_list.append(row)


def story_random():
    # Функция для отображение случайной истории из файла
    rnd_story_ind = random.randint(0, len(story_list) - 1)
    print(story_list[rnd_story_ind])
