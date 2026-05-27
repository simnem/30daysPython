import random
import string


def user_id_gen_by_user():
    length = int(input('What would you like length of your ID to be?'))
    amount = int(input('How many IDs you need in total?'))
    all_ids = []
    for i in range(0, amount):
        id = ''
        for i in range(0, length):
            type = random.randint(0,1)
            if type == 0:
                id += random.choice(string.ascii_letters)
            else:
                id += random.choice(string.digits)
        all_ids.append(id)
    for id in all_ids:
        print(id)

def rgb_color_gen():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255) )

def list_of_hexa(amount):
    letters = ['a','b', 'c', 'd', 'e', 'f']
    all_colors = []
    for i in range(0, amount):
        color = '#'
        for i in range(1, 7):
            color += random.choice(random.choice([letters, list(string.digits)]))
        all_colors.append(color)
    return all_colors

def list_rgb(amount):
    all_colors = []
    for i in range(0, amount):
        all_colors.append(f'rgb{(random.randint(0,255), random.randint(0,255), random.randint(0,255))}')
    return all_colors

def generate_colors(type, amount):
    return list_rgb(amount) if type == 'rgb' else list_of_hexa(amount)

def shuffle_list(list):
   new_list = random.sample(list, len(list))
   return new_list

def unique_numbers():
    number_list = []

    while len(number_list) != 7:
        new_num = random.randint(0,9)
        if new_num not in number_list:
            number_list.append(new_num) 
    return number_list
