import os
import sys
import time
from datetime import date

# ANSI Colors
BLUE = "\033[94m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def logo():
    print(f"""{BLUE}
   \\     /  
    \\   /   
     \\ /    
      |     
      |     
      |     
      |     
   _________
  |   IDI   |
  |_________|
{RESET}""")

def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def interpret_cnp(cnp, country):
    if country == "Romania" and len(cnp) == 13:
        interpret_romanian_cnp(cnp)
    elif country == "Bulgaria" and len(cnp) == 10:
        interpret_bulgarian_egn(cnp)
    elif country == "Italy" and len(cnp) == 16:
        interpret_italian_codice_fiscale(cnp)
    elif country == "Sweden" and len(cnp) == 11:
        interpret_swedish_personnummer(cnp)
    elif country == "Netherlands" and len(cnp) == 9:
        interpret_dutch_bsn(cnp)
    else:
        print(f"{RED}Invalid ID format for selected country.{RESET}")

def interpret_romanian_cnp(cnp):
    control_key = "279146358279"
    suma = sum(int(cnp[i]) * int(control_key[i]) for i in range(12))
    cifra_control_calculata = suma % 11
    if cifra_control_calculata == 10:
        cifra_control_calculata = 1
    cifra_control = int(cnp[12])
    is_valid = cifra_control == cifra_control_calculata

    gender_century_map = {
        '1': ('Male', 1900, 'born between 1900-1999 in Romania'),
        '2': ('Female', 1900, 'born between 1900-1999 in Romania'),
        '3': ('Male', 1800, 'born between 1800-1899 in Romania'),
        '4': ('Female', 1800, 'born between 1800-1899 in Romania'),
        '5': ('Male', 2000, 'born between 2000-2099 in Romania'),
        '6': ('Female', 2000, 'born between 2000-2099 in Romania'),
        '7': ('Male (foreign resident)', 2000, 'born between 2000-2099 abroad'),
        '8': ('Female (foreign resident)', 2000, 'born between 2000-2099 abroad'),
        '9': ('Foreign citizen', 2000, 'assigned to a foreign citizen')
    }

    county_map = {
        '01': 'Alba', '02': 'Arad', '03': 'Argeș', '04': 'Bacău', '05': 'Bihor', '06': 'Bistrița-Năsăud',
        '07': 'Botoșani', '08': 'Brașov', '09': 'Brăila', '10': 'Buzău', '11': 'Caraș-Severin', '12': 'Cluj',
        '13': 'Constanța', '14': 'Covasna', '15': 'Dâmbovița', '16': 'Dolj', '17': 'Galați', '18': 'Gorj',
        '19': 'Harghita', '20': 'Hunedoara', '21': 'Ialomița', '22': 'Iași', '23': 'Ilfov', '24': 'Maramureș',
        '25': 'Mehedinți', '26': 'Mureș', '27': 'Neamț', '28': 'Olt', '29': 'Prahova', '30': 'Satu Mare',
        '31': 'Sălaj', '32': 'Sibiu', '33': 'Suceava', '34': 'Teleorman', '35': 'Timiș', '36': 'Tulcea',
        '37': 'Vaslui', '38': 'Vâlcea', '39': 'Vrancea', '40': 'București', '41': 'București - Sector 1',
        '42': 'București - Sector 2', '43': 'București - Sector 3', '44': 'București - Sector 4',
        '45': 'București - Sector 5', '46': 'București - Sector 6', '51': 'Călărași', '52': 'Giurgiu'
    }

    s = cnp[0]
    aa = int(cnp[1:3])
    ll = int(cnp[3:5])
    zz = int(cnp[5:7])
    jj = cnp[7:9]
    nnn = int(cnp[9:12])

    gender, century, _ = gender_century_map.get(s, ("Unknown", 0, "unknown"))
    birth_year = century + aa
    try:
        birth_date = date(birth_year, ll, zz).strftime("%d %B %Y")
    except ValueError:
        birth_date = "Invalid date"

    age = date.today().year - birth_year - ((date.today().month, date.today().day) < (ll, zz))
    is_adult = age >= 18
    valid_country = "Romania"
    county = county_map.get(jj, "Unknown")

    # Determine Bucharest sector if applicable
    sector = None
    if jj in {'41', '42', '43', '44', '45', '46'}:
        sector_number = int(jj) - 40
        sector = f"Sector {sector_number}"

    registration_message = f"Born in {county}, Romania, registered as {nnn}-th person on {birth_date}."

    typewriter(f"\n{CYAN}Details from the ID Number:{RESET}")
    print(f"{CYAN}Input ID: {YELLOW}{cnp}")
    print(f"{CYAN}Validity: {GREEN if is_valid else RED}{'Valid' if is_valid else 'Invalid'}{RESET}")
    print(f"{CYAN}Gender: {YELLOW}{gender}")
    print(f"{CYAN}Birth Date: {YELLOW}{birth_date}")
    print(f"{CYAN}Country: {YELLOW}{valid_country}")
    print(f"{CYAN}County (Județ): {YELLOW}{county}")
    if sector:
        print(f"{CYAN}Bucharest Sector: {YELLOW}{sector}")
    print(f"{CYAN}Registration Message: {GREEN}{registration_message}")
    print(f"{CYAN}Age: {YELLOW}{age}")
    print(f"{CYAN}Is Adult: {YELLOW}{'Yes' if is_adult else 'No'}{RESET}")
    print(f"{CYAN}{'-' * 50}{RESET}")


def interpret_bulgarian_egn(cnp):
    s = cnp[0]
    aa = int(cnp[1:3])
    ll = int(cnp[3:5])
    zz = int(cnp[5:7])
    gender = "Male" if int(s) % 2 != 0 else "Female"
    birth_year = 1900 + aa if int(s) < 3 else 1800 + aa
    birth_date = date(birth_year, ll, zz).strftime("%d %B %Y")

    typewriter(f"\n{CYAN}Details from the ID Number:{RESET}")
    print(f"{CYAN}Input ID: {YELLOW}{cnp}")
    print(f"{CYAN}Gender: {YELLOW}{gender}")
    print(f"{CYAN}Birth Date: {YELLOW}{birth_date}")
    print(f"{CYAN}Country: {YELLOW}Bulgaria")
    print(f"{CYAN}Registration Message: {GREEN}Born in Bulgaria, registered as {gender} on {birth_date}.{RESET}")
    print(f"{CYAN}{'-' * 50}{RESET}")

def interpret_italian_codice_fiscale(cnp):
    year = int(cnp[6:8])
    month = int(cnp[8:10])
    day = int(cnp[10:12])
    gender_digit = int(cnp[15])
    gender = "Male" if gender_digit % 2 == 1 else "Female"
    birth_date = date(1900 + year, month, day).strftime("%d %B %Y")

    typewriter(f"\n{CYAN}Details from the ID Number:{RESET}")
    print(f"{CYAN}Input ID: {YELLOW}{cnp}")
    print(f"{CYAN}Gender: {YELLOW}{gender}")
    print(f"{CYAN}Birth Date: {YELLOW}{birth_date}")
    print(f"{CYAN}Country: {YELLOW}Italy")
    print(f"{CYAN}Registration Message: {GREEN}Born in Italy, registered as {gender} on {birth_date}.{RESET}")
    print(f"{CYAN}{'-' * 50}{RESET}")

def interpret_swedish_personnummer(cnp):
    year = int(cnp[0:2])
    month = int(cnp[2:4])
    day = int(cnp[4:6])
    century = "19" if int(cnp[6]) < 4 else "20"
    birth_year = int(century + str(year))
    gender_digit = int(cnp[9])
    gender = "Male" if gender_digit % 2 == 1 else "Female"
    birth_date = date(birth_year, month, day).strftime("%d %B %Y")

    typewriter(f"\n{CYAN}Details from the ID Number:{RESET}")
    print(f"{CYAN}Input ID: {YELLOW}{cnp}")
    print(f"{CYAN}Gender: {YELLOW}{gender}")
    print(f"{CYAN}Birth Date: {YELLOW}{birth_date}")
    print(f"{CYAN}Country: {YELLOW}Sweden")
    print(f"{CYAN}Registration Message: {GREEN}Born in Sweden, registered as {gender} on {birth_date}.{RESET}")
    print(f"{CYAN}{'-' * 50}{RESET}")

def interpret_dutch_bsn(cnp):
    if len(cnp) != 9 or not cnp.isdigit():
        print(f"{RED}Invalid BSN format{RESET}")
        return
    gender = "Male" if int(cnp[0]) % 2 != 0 else "Female"

    typewriter(f"\n{CYAN}Details from the ID Number:{RESET}")
    print(f"{CYAN}Input ID: {YELLOW}{cnp}")
    print(f"{CYAN}Gender: {YELLOW}{gender}")
    print(f"{CYAN}Country: {YELLOW}Netherlands")
    print(f"{CYAN}Registration Message: {GREEN}Registered in the Netherlands as {gender}.{RESET}")
    print(f"{CYAN}{'-' * 50}{RESET}")

def main():
    while True:
        clear_screen()
        logo()
        typewriter(f"{CYAN}Select country for the ID number:{RESET}")
        print(f"{YELLOW}1. Romania\n2. Bulgaria\n3. Italy\n4. Sweden\n5. Netherlands{RESET}")
        country_choice = input(f"{CYAN}Enter country number: {RESET}").strip()

        country_map = {
            "1": "Romania",
            "2": "Bulgaria",
            "3": "Italy",
            "4": "Sweden",
            "5": "Netherlands"
        }

        country = country_map.get(country_choice)
        if not country:
            typewriter(f"{RED}Invalid selection. Try again.{RESET}")
            time.sleep(1.5)
            continue

        cnp_input = input(f"{CYAN}Enter the ID Number: {RESET}").strip()
        interpret_cnp(cnp_input, country)

        typewriter(f"\n{CYAN}Press Enter to restart or type 'q' to quit.{RESET}")
        restart = input().strip().lower()
        if restart == 'q':
            typewriter(f"{GREEN}Goodbye!{RESET}")
            break

if __name__ == "__main__":
    main()
