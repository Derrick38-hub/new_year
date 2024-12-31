import pyfiglet
from colorama import Fore, Style

ascii_art = pyfiglet.figlet_format("Happy New Year!")

print(Fore.WHITE + ascii_art + Style.RESET_ALL)