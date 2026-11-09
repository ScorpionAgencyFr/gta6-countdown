
import time
import os
from datetime import datetime
from zoneinfo import ZoneInfo

# Date officielle de sortie : Belgique
target = datetime(
    2026, 11, 19, 0, 0, 0,
    tzinfo=ZoneInfo("Europe/Brussels")
)

PURPLE = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

try:
    while True:
        now = datetime.now(ZoneInfo("Europe/Brussels"))
        remaining = int((target - now).total_seconds())

        os.system("clear")

        print(PURPLE + BOLD)
        print("========================================")
        print("          GRAND THEFT AUTO VI")
        print("========================================")
        print(RESET)

        if remaining <= 0:
            print(CYAN + BOLD)
            print("       WELCOME TO VICE CITY!")
            print("          GTA VI IS HERE!")
            print(RESET)
            break

        days, remaining = divmod(remaining, 86400)
        hours, remaining = divmod(remaining, 3600)
        minutes, seconds = divmod(remaining, 60)

        print(CYAN + BOLD)
        print("          LIVE COUNTDOWN")
        print(RESET)

        print(WHITE + BOLD)
        print(f"       {days:03d} JOURS")
        print(f"       {hours:02d} HEURES")
        print(f"       {minutes:02d} MINUTES")
        print(f"       {seconds:02d} SECONDES")
        print(RESET)

        print(PURPLE)
        print("----------------------------------------")
        print("       SORTIE : 19 NOVEMBRE 2026")
        print("       HEURE : 00:00")
        print("       FUSEAU : BELGIQUE")
        print("----------------------------------------")
        print(RESET)

        print("Actualisation automatique chaque seconde.")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nCompte à rebours arrêté.")
