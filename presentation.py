import os
import subprocess
import time
import pygame

pygame.mixer.init()

delay = 0.06


def clear_terminal():
    os.system("clear")  # Mac only, replace with "cls" for Windows


def ascii(file_location):
    try:
        subprocess.run(["ascii_py", "-t", file_location])  # found @ https://github.com/ProfOak/ascii_py/
    except FileNotFoundError:
        print(
            "Error: The 'ascii_py' command not found. Please install by using the command python3 -m pip install ascii_py to install ascii ")
    time.sleep(1)


def mpv(file_location):
    try:
        loop_gifs = ["pairprogramming.gif", "fireworks.gif"]
        option = "--loop" if file_location in loop_gifs else "--speed=2" # q to quit

        subprocess.run(["mpv", "--no-config", "--vo=tct", option, file_location])  # found @ https://github.com/mpv-player/mpv
    except FileNotFoundError:
        print(
            "Error: The 'mpv' command not found. Please install by using the command python3 -m pip install mpv to install mpv ")
    time.sleep(1)


def type_text(text, delays):
    for char in text:
        print(char, end='', flush=True)
        pygame.mixer.music.load("key_sound.wav")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.008)
        time.sleep(delays)
    print()


# Slide content
slides = [
    "This is My Journey So Far as an F5/NGINX Intern \n/wbr-NGINX-F5-AMA-1-featured-500x300-removebg-preview.png",# file location for ascii image after \n/
    "Hi, I'm Alex! I am an intern at NGINX, a company owned by F5, and I'm based in Cork, Ireland.\nI am currently "
    "studying Software Development in MTU Cork. This is my journey so far as an intern at NGINX! "
    "\n/2052094765_256312f117_c.png",

    "The first day was quite unique, 2 other interns started with me on the 1st of February! It was also our "
    "F5 day. Met lots of people, got set up, had a tour and even had a few games of pool!\nWe had pizza, cupcakes and a"
    " presentation afterwards. It was definitely an eventful day. \nDid anyone else have an unusual start to their "
    "internship? \n/1707205688312.jpeg",

    "The initial two weeks were overwhelming with lots of information being thrown all at once, encountering outdated "
    "on-boarding notes and finding programs no longer being used by my team,\nadapting to the "
    "team's workflow and I was getting better at talking about my tasks daily."
    "\nHow did you handle the overwhelming amount of information during your initial weeks? \n./elmo.gif",

    "Adapting to macOS was a struggle for a while and is hard to go back and forth with windows now due to different "
    "placement of keys and new buttons. I still struggle with some key binds to this day. "
    "\nDid any of you face challenges in transitioning to a new operating system or program? \n/macos.jpeg",

    "Coming from university, I knew the basics of a lot of programming languages but staring at NGINX, I had to learn "
    "a new programming language called Go. \nThis was a challenge, but converting an old university python project to "
    "go was surprisingly fun! \nHas anyone else faced a steep learning curve during the internship? [small quick "
    "example video shown below of the project].",

    "After a lot of training and overcoming challenges, I received my first task from the manager –  simple but still "
    "encountered some issues trying to finish it. With help from my work buddy, I managed to get through it. "
    "\n./skill-issue-coding.gif",

    "I got tasked to do another 'easy' change to the code base, it was to move 1 line of code in two files up. This "
    "took a turn as I had to do a lot of testing and it took way longer than expected. \nI had to make my own app, "
    "integrate it within the NGINX program and debug it. I struggled a lot but having a co-worker helping and working "
    "with me helped a lot. \nI learned a lot new programs and tools which will be very important for my future in "
    "NGINX. [small video demonstrating it here]    \nWhat was your first significant task as an intern?",

    "As stated in the past 2 slides, Collaboration was key, especially during challenging tasks. Being able to reach "
    "out and get help from the team helps a lot. \nWhat valuable lessons have you learned from working with others? "
    "\n./pairprogramming.gif",

    "In conclusion, my journey so far has been very informative and fun and I'm really enjoying my time at NGINX. "
    "Through collaboration and learning, I've grown a lot both personally and professionally.\n I could not have asked "
    "for a better company for the first job. Thank you for your time."
    "\n./fireworks.gif"

]

# Display slides
for slide_content in slides:
    clear_terminal()
    if '\n/' in slide_content:
        parts = slide_content.split('\n/', 1)
        type_text(parts[0], delay)
        time.sleep(1.5)
        clear_terminal()
        ascii(parts[1])
    # elif '.\n/' in slide_content:
    #     parts = slide_content.split('.\n/', 1)
    #     ascii(parts[1])
    #     time.sleep(1.5)
    #     type_text(parts[0], delay)
    elif '\n./' in slide_content:
        parts = slide_content.split('\n./', 1)
        type_text(parts[0], delay)
        time.sleep(3)
        clear_terminal()
        mpv(parts[1])
    else:
        type_text(slide_content, delay)
    if not slide_content.__contains__("\n/"):
        input("\nPress Enter to continue...\n")
