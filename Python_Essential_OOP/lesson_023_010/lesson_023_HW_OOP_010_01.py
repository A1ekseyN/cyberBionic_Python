# Ready
import re

text = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce auctor metus vel quam tempus pharetra. In orci '
        'lorem, ultrices quis dapibus sodales, laoreet a felis. Vivamus id turpis at mi iaculis malesuada. Orci varius '
        'natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Proin blandit semper felis, eu '
        'condimentum.')

pattern_01 = 'lorem'


def search_a():
    global search_01
    search_01 = re.findall(pattern_01, text.lower())
    return search_01


def search_b():
    global search_02
    search_02 = re.findall('ipsum', text.lower())
    return search_02


search_a()
search_b()

print(f'В тексте, по паттерну - "{pattern_01}", найдено {len(search_01)} совпадений.')
print(f'А по паттерну - "ipsum", найдено {len(search_02)} совпадений.')

print(search_01)
print(search_02)
