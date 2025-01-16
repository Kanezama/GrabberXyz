import googlesearch
from googlesearch import search
from urllib.parse import urlparse
import os
import subprocess
import time
import threading
import sys

def clear_screen():
    """Function to clear the terminal screen."""
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

def install_package(package):
    """Function to install packages using pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_packages():
    """Check and install required packages."""
    try:
        import googlesearch
    except ImportError:
        print("Package 'googlesearch-python' not found. Installing...")
        install_package("googlesearch-python")
    
    try:
        import requests
    except ImportError:
        print("Package 'requests' not found. Installing...")
        install_package("requests")

def mez():
    """Display purchase information."""
    print(" Buy The Unencrypted Version For V1 Only 15K. \n   Contact wa.me/+6285695450203 / t.me/@TitanSi_KangWebshell")

def loading_animation():
    """Display a loading animation."""
    animation = "|/-\\"
    idx = 0
    while not stop_event.is_set():
        sys.stdout.write(f"\rPlease Wait, Loading [❌] {animation[idx]}")
        sys.stdout.flush()
        idx = (idx + 1) % len(animation)
        time.sleep(0.1)

def animz():
    """Show animation with loading and success message."""
    global stop_event
    stop_event = threading.Event()
    animation_thread = threading.Thread(target=loading_animation)
    animation_thread.start()
    time.sleep(5)
    stop_event.set()
    animation_thread.join()
    print("\rSuccess [✔]")
    time.sleep(1)

def login():
    """Handle user authentication."""
    password = "KanezamaXyz"
    for _ in range(3):
        pass_input = input("Enter The Password: ")
        if pass_input == password:
            time.sleep(2)
            print("Login Succeed!")
            return True
        print("Password Failed. Try Again!")
        time.sleep(2)
    print("Too Many Trials, Program Terminated")
    return False

def google_search(query, num_results):
    """Perform Google search and save results to file."""
    results = search(query, num_results=num_results)
    
    with open(filename, "w") as file:
        for i, result in enumerate(results, start=1):
            domain = urlparse(result).netloc
            file.write(f"{domain}\n")
    
    print(f"Results Has Saved In {filename}.")

if __name__ == "__main__":
    print("Checking Your Packages...")
    check_and_install_packages()
    os.system("clear")
    clear_screen()
    os.system(1)
    
    # Display ASCII art banner
    print("""  ▄████  ██▀███   ▄▄▄       ▄▄▄▄    ▄▄▄▄   ▓████  ██▀███  
 ██▒ ▀█▒▓██ ▒ ██▒▒████▄    ▓█████▄ ▓█████▄ ▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒  ▀█▄▒██▒  ▀█▄▒███   ▓██ ░▄█ ▒
░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██ ▒██░  ▄▄▒██░  ▄▄▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒░▓█  ██▓░▓█  ██▓░▒████▒░██▓ ▒██▒
 ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▒▓███▀▒░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░▒░▒   ░ ▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░░   ░   ░   ▒    ░    ░  ░    ░    ░     ░░   ░ 
      ░    ░           ░  ░ ░      ░         ░  ░   ░       
                                 ░       ░       By Kanezama |  Aizen.my.id """)
    
    if login():
        clear_screen()
        mez()
        os.system(2)
        clear_screen()
        
        query = input("Enter Your Keywords: ")
        num_results = int(input("Enter the number of websites you want: "))
        os.system(1)
        filename = input("Enter the name of the file you want to save (eg: results.txt) :")
        google_search(query, num_results)
