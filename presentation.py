import concurrent.futures
import os
import subprocess
import time
import pygame # found @ https://github.com/pygame/pygame
import random
from terminology import in_red, in_yellow, in_green, in_blue, in_magenta, in_white # found @ https://github.com/juanrgon/terminology

pygame.mixer.init()


def clear_terminal():
    os.system("clear")  # Mac only, replace with "cls" for Windows


def ascii(file_location):
    try:
        subprocess.run(["ascii_py", "-t", file_location])  # found @ https://github.com/ProfOak/ascii_py/
    except FileNotFoundError:
        print(
            "Error: The 'ascii_py' command not found. Please install by using the command python3 -m pip install ascii_py to install ascii ")
    time.sleep(1)


def gif(file_location):
    try:
        loop_gif = ["pairprogramming.gif"]
        option = "--loops=5" if file_location in loop_gif else "--loops=2" # q to quit

        subprocess.run(["timg","--fit-width", "--grid=2", "-U", option, file_location])  # found @ https://github.com/hzeller/timg/

    except FileNotFoundError:
        print(
            "Error: The 'timg' or 'mpv' command not found. Please install by using the command python3 -m pip install timg to install timg or python3 -m pip install mpv to install mpv ")
    time.sleep(1)


def type_text(text):
    for char in text:
        print(char, end='', flush=True)
        delay = random.uniform(0.01,0.1)
        pygame.mixer.music.load("key_sound.wav")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.008)
        time.sleep(delay)
    print()


def fireworks(file_location):
    mpv_command = ["mpv","--end=0:20", "--no-config", "--vid=0", "--audio-delay=1","--volume=20", "--msg-level=all=warn" ,file_location] # found @ https://github.com/mpv-player/mpv
    gif_command = ["timg", "--fit-width", "--grid=3", "-U" ,file_location]

    # Run the commands concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(subprocess.run, mpv_command)
        executor.submit(subprocess.run, gif_command)

# Slide content
slides = [
    "This is My Journey So Far as an " + in_green("NGINX").in_bold() + "/" + in_red("F5").in_bold() + " Intern \n/wbr-NGINX-F5-AMA-1-featured-500x300-removebg-preview.png",# file location for ascii image after \n/

    "Hi, I'm Alex! I am an int"
    "ern at " + in_green("NGINX").in_bold() + ", a company owned by " + in_red("F5").in_bold() + ", and I'm based in Cork, Ireland.\nI am currently "
    "studying Software Development in " + in_yellow("M").in_bold() + in_red("T").in_bold() + in_blue("U").in_bold()
    + " Cork. This is my journey so far as an intern at " + in_green("NGINX").in_bold() + "! "
    "\n/mtu-ireland.png",

    "The first day was quite " + in_white("unique").in_bold().underlined() + ", 2 other interns started with me on the 1st of February! It was also our "
    + in_red("F5").in_bold() + " day.\nMet lots of people, got set up, had a tour and even had a few games of pool!\nWe had pizza, cupcakes and a"
    " presentation afterwards. It was definitely an eventful day." + in_blue("\nDid anyone else have an unusual start to their internship?").in_bold().underlined() +
    "\n/1707205688312.jpeg",

    "The initial two weeks were " + in_white("overwhelming").in_bold().underlined() + " with lots of information being thrown all at once,\nencountering outdated "
    "on-boarding notes and finding programs no longer being used by my team,\nadapting to the "
    "team's workflow and I was also getting better at talking about my tasks daily."
    + in_blue("\nHow did you handle the overwhelming amount of information during your initial weeks? ").in_bold().underlined() +
    " \n./elmo.gif",

    "Adapting to " + in_magenta("macOS").in_bold().underlined() + " was a struggle for a while and is hard to go back and forth with " + in_blue("Windows").in_bold().underlined() + " now due to different "
    "placement of keys and new buttons. \nI still struggle with some key binds to this day. "
    + in_blue("\nDid any of you face challenges in transitioning to a new operating system or program?").in_bold().underlined() +
    " \n/macos.jpeg",

    "Coming from university, I knew the basics of a lot of programming languages but staring at " + in_green("NGINX").in_bold() + ", I had to learn "
    "a new programming language called " + in_blue("Go.").in_bold().underlined() + " \nThis was a challenge, but converting an old university python project to "
    "go was surprisingly fun! " + in_blue("\nHas anyone else faced a steep learning curve during the internship?").in_bold().underlined() +
    "\n./learningcurve.gif",

    "After a lot of training and overcoming " + in_red("challenges").in_bold().underlined() + ", I received my first task from the manager –  simple but still "
    "encountered some issues trying to finish it. \nWith help from my work buddy, I managed to get through it. "
    "\n./skill-issue-coding.gif",

     "I got tasked to do another " + in_white("'easy'").in_bold().underlined() + " change to the code base, it was to move 1 line of code in two files up. \n"
    "This took a turn as I had to do a lot of testing and it took way longer than expected. \nI had to make my own app, "
    "integrate it within the " + in_green("NGINX").in_bold() + " program and debug it.\nI struggled a lot but having a co-worker helping and working "
    "with me helped a lot. \nI learned a lot new programs and tools which will be very important for my future in "
    + in_green("NGINX").in_bold() + "." + in_blue("\nWhat was your first significant task as an intern?").in_bold().underlined() +
    "\n./itsworking.gif",

    "As stated in the past 2 slides, " + in_white("Collaboration").in_bold().underlined() + " was key, especially during " + in_red("challenging").in_bold().underlined() + " tasks. Being able to reach "
    "out and get help from the team helps a lot. "  + in_blue("\nWhat valuable lessons have you learned from working with others?").in_bold().underlined() +
    "\n./pairprogramming.gif",

    "In conclusion, my journey so far has been very informative and fun and I'm really enjoying my time at " + in_green("NGINX").in_bold() + ". "
    "\nThrough collaboration and learning, I've grown a lot both personally and professionally.\nI could not have asked "
    "for a better company for the first job. Thank you for your time."
    "\n... fireworks.mp4"
]

# Display slides
for slide_content in slides:
    clear_terminal()

    if '\n/' in slide_content:
        delay = random.uniform(0.04,0.1)
        parts = slide_content.split('\n/', 1)
        type_text(parts[0])
        time.sleep(1.5)
        ascii(parts[1])
    elif '\n./' in slide_content:
        parts = slide_content.split('\n./', 1)
        delay = random.uniform(0.04,0.1)
        type_text(parts[0])
        time.sleep(3)
        gif(parts[1])
    elif '\n... ' in slide_content:
        parts = slide_content.split('\n... ', 1)
        delay = random.uniform(0.04,0.1)
        type_text(parts[0])
        time.sleep(3)
        fireworks(parts[1])
    else:
        type_text(slide_content)
    if not slide_content.__contains__("\n/"):
        input("\nPress Enter to continue...\n")
