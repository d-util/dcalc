import json
import colorama
import pyttsx3
from mw_distance import distance, which_enter_which_exit, distance_dict, places_dict, exits_dict
from spellchecker import SpellChecker
from sys import exit

engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
version: str = '0.11.23'

def clear_styles():
    print(colorama.Style.RESET_ALL + '', end='', sep='')

user_preferences = None
spell: SpellChecker

def load_jsons():
    global spell
    spell = SpellChecker()
    with open('places.json', 'r') as f:
        spell.word_frequency.load_words(list(json.load(f).keys()))

    global user_preferences
    with open('user_settings.json', 'r') as f:
        user_preferences = json.load(f)

def exit_error(code):
    from sys import exit
    exit(code)

def display_error_cookies():
    print('error. run cookies.py first.')
    exit_error(1)

def check_cookies():
    try:
        _ = user_preferences['name']
    except KeyError:
        display_error_cookies()
    except ValueError:
        display_error_cookies()

clear_styles()
load_jsons()

try:
    _ = user_preferences['name']
except KeyError:
    print('error. run cookies.py first.')
    from sys import exit
    exit(1)
except ValueError:
    print('error. run cookies.py first.')
    from sys import exit
    exit(1)

print(f'Hi, {user_preferences['name'].title()}!')
location: str = user_preferences['home']
where_would_you_like_to_go_today = 'Where would you like to go today? '

destination: str = input(where_would_you_like_to_go_today).lower()
navigation_prep_message = f'Navigating from {location.title()} to {destination.title()}...'
print(navigation_prep_message)
clear_styles()

display_distance: str # Predefining Display Distance due to scope.
str_distance: str = distance(location.lower(), destination.lower())
if "ERROR" in str_distance:
    if str_distance == "ERROR1":
        print(f'Error. no such place as \'{location.title()}\'. Check your location preferences."')
        print('If your spelling is correct, Probably your location is not in the place database.')

    elif str_distance == "ERROR2":
        print(f'Error. no such place as \'{destination.title()}\'.', end=" ")
        spell_correction: str = spell.correction(destination.lower())
        if spell.correction(destination.lower()) in places_dict.keys():
            print(f'Did you mean {spell.correction(destination.lower()).title()}?')
            print('If your spelling is correct, Probably your destination is not in the place database.')

        else:
            print('\nThe place appears not to be in our place database :(')

elif location.lower() == destination.lower():
    you_are_already_at = f'You are already at {destination.title()}, aren\'t you?'
    print(you_are_already_at)

else:
    km_distance: float = float(str_distance)
    rounded_distance: float = km_distance
    if rounded_distance >= 50.0:
        rounded_distance = float(round(rounded_distance))
    if rounded_distance >= 2000.0:
        rounded_distance = float(round(rounded_distance / 5) * 5)
    display_distance: str = f'{rounded_distance:.1f}'
    if rounded_distance == round(rounded_distance):
        display_distance = str(int(rounded_distance))
    distance_from_message: str = f'Distance from {location.title()} to {destination.title()}: {display_distance}km'
    print(distance_from_message)
    mw_display: str = 'E18'
    mw_display_direction: str = ''
    if mw_display == 'E18':
        if distance_dict(location, destination)['direction'] > 0:
            mw_display_direction = 'Kristiansand'
        else:
            mw_display_direction = 'Oslo'
    instructions: str = ''''''
    DECIMAL_PLACES = 1
    if distance_dict(location, destination)['motorway'] == 0:
        if distance_dict(location, destination)['direction'] > 0:
            instructions += f'Stay on the closest main road in the direction away from the main motorway for {distance_dict(location, destination)['exit']:.1f}km\n'
        else:
            instructions += f'Stay on the closest main road in the direction towards the main motorway for {distance_dict(location, destination)['exit']:.1f}km\n'
    else:
        en_dict = which_enter_which_exit(location, destination)[0]
        ex_dict = which_enter_which_exit(location, destination)[1]
        instructions += f'Enter {exits_dict[en_dict]['number']}\n'
        instructions += f'Stay on {mw_display} {mw_display_direction} for {distance_dict(location, destination)['motorway']:.1f}km\n'
        instructions += f'Exit {exits_dict[ex_dict]['number']}\n'
        instructions += f'Stay on the road for {distance_dict(location, destination)['exit']:.1f}km\n'
    print('Starting Tkinter Window...')
    from tkinter import *
    from tkinter import ttk
    root = Tk()
    root.title = 'dmaps'
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text=f'Distance: {display_distance}km').grid(column=0, row=0)
    ttk.Label(frm, text='========INSTRUCTIONS========').grid(column=0, row=1)
    ttk.Label(frm, text=instructions + 'You have reached your destination\n'
              ).grid(column=0, row=2)
    ttk.Button(frm, text='Quit', command=root.destroy).grid(column=2, row=3)
    print('Started Tkinter Window...')
    root.mainloop()
    print('Tkinter Window Stopped')
    exit(0)

exit(0)
