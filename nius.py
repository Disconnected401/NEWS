from colorama import Fore
import time
import os

W = Fore.WHITE
M = Fore.MAGENTA
ML = Fore.LIGHTMAGENTA_EX
B = Fore.BLUE
R = Fore.LIGHTRED_EX
Y = Fore.LIGHTYELLOW_EX
G = Fore.LIGHTGREEN_EX
C = Fore.LIGHTCYAN_EX
GR = Fore.LIGHTBLACK_EX

COLOR_1 = (255, 255, 255)
COLOR_2 = (25, 25, 25)


logo = """









           __  ___     __    __              _   __     __                      __      _   __                 
          / / / (_)___/ /___/ /__  ____     / | / /__  / /__      ______  _____/ /__   / | / /__ _      _______
         / /_/ / / __  / __  / _ \/ __ \   /  |/ / _ \/ __/ | /| / / __ \/ ___/ //_/  /  |/ / _ \ | /| / / ___/
        / __  / / /_/ / /_/ /  __/ / / /  / /|  /  __/ /_ | |/ |/ / /_/ / /  / ,<    / /|  /  __/ |/ |/ (__  ) 
       /_/ /_/_/\__,_/\__,_/\___/_/ /_/  /_/ |_/\___/\__/ |__/|__/\____/_/  /_/|_|  /_/ |_/\___/|__/|__/____/      



       

       
       






"""

def color_gradient(starter_color, end_color, steps):
    gradient = []
    for i in range(steps):
        r = int((i * end_color[0] + (steps - i) * starter_color[0]) / steps)
        g = int((i * end_color[1] + (steps - i) * starter_color[1]) / steps)
        b = int((i * end_color[2] + (steps - i) * starter_color[2]) / steps)
        gradient.append((r, g, b))
    return gradient

def color_text(text, color_gradient):
    colored_text = ""
    for i, znak in enumerate(text):
        color = color_gradient[i % len(color_gradient)]
        colored_text += f"\033[38;2;{color[0]};{color[1]};{color[2]}m{znak}"
    return colored_text

gradient = color_gradient(COLOR_1, COLOR_2, len(logo))

title = "Hidden Network NEWS"
os.system(f"title {title}")

os.system("cls")

print(color_text(logo, gradient))

time.sleep(5)

os.system("cls")

print(f"{Y}DATE - 20.11.2023{W}")
print(f"{B}• {W}Admin Pass?\n")
print(f"""
{W}Login:  {G}admin2@technischools.com
{W}Hasło:  {G}Tiamat2023!@{W}
""")

print(f"\n\n{Y}DATE - 20.11.2023{W}")
print(f"{B}• {W}WiFi Pass\n")
print(f"""
{ML}WIFI{W}

SSID:   TechniSchools
Hasło:  {G}TS2023!@%{W}

SSID:   GUEST
Hasło:  {G}#guest#guest#guest#{W}

SSID:   Tslublin
Hasło:  {G}hikari77{W}
""")

print(f"\n\n{Y}DATE - 30.11.2023{W}")
print(f"{B}• {W}Note\n")
print(f"""
one day the administrator used his private phone (hotspot) to download a file from the Internet faster, 
his hotspot password was {GR}hikari77{W} it may have something to do with something else but I don't know what
""")

input(f"\n\n\n{R}press ENTER to exit {W}")
os.system("cls")
