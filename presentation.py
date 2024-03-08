import os
import subprocess
import time
from colorama import init, Fore, Style

init(autoreset=True)

delay = 0.04

def clear_terminal():
    os.system("clear")  # Use 'cls' for Windows, 'clear' for Linux/Mac

def ascii(file_location):
    expanded_path = os.path.expanduser(file_location)
    try:
        subprocess.run(["ascii_py", "-s", "10", "-t", expanded_path])
    except FileNotFoundError:
        print("Error: The 'ascii_py' command not found. Please make sure it's installed and in your PATH.")

    time.sleep(1)  # Adjust as needed

def type_text(text, delays):
    colored_text = (
        text.replace("[nginx]", f"{Fore.GREEN}[nginx]{Style.RESET_ALL}")
        .replace("[f5]", f"{Fore.RED}[f5]{Style.RESET_ALL}")
    )

    for char in colored_text:
        print(char, end='', flush=True)
        time.sleep(delays)
    print()

# Slide content
slides = [
    "My Journey So Far as an F5/NGINX Intern\n~/Downloads/wbr-NGINX-F5-AMA-1-featured-500x300-removebg-preview.png",
    "Hi, I'm Alex! I am an intern at NGINX, a company owned by F5, based in Cork, Ireland. I am a student studying Software Development at MTU Cork. This is my journey so far in my first job as an intern in F5/NGNIX! \n~/Downloads/2052094765_256312f117_c.jpg",
    "The first day was quite unique, I started with 2 other interns on the 1st of February which was a weird to start because it was a Thursday! It was also an early F5 day so big day to start. Met lots of new people, had a tour and even had a few games of pool! **How crazy is that?** We had pizza for lunch and a presentation afterwards.  **Has anyone else had an unusual start to their internship?**"
]

# Display slides
for slide_content in slides:
    clear_terminal()
    if '\n~' in slide_content:
        parts = slide_content.split('\n', 1)
        type_text(parts[0], delay)
        time.sleep(0.5)
        clear_terminal()
        ascii(parts[1])
    else:
        type_text(slide_content, delay)
        if not slide_content.startswith("[ASCII"):
            input("\nPress Enter to continue...")
