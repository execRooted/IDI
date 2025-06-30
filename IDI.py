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


def interpret_bulgarian_egn(egn):
    if len(egn) != 10 or not egn.isdigit():
        print(f"{RED}Invalid EGN format (must be 10 digits).{RESET}")
        return

    yy = int(egn[0:2])
    mm = int(egn[2:4])
    dd = int(egn[4:6])
    region_code = int(egn[6:9])
    gender = "Female" if region_code % 2 == 0 else "Male"
    check_digit = int(egn[9])

    # Determine century and adjust month
    if 1 <= mm <= 12:
        year = 1900 + yy
        month = mm
    elif 21 <= mm <= 32:
        year = 1800 + yy
        month = mm - 20
    elif 41 <= mm <= 52:
        year = 2000 + yy
        month = mm - 40
    else:
        print(f"{RED}Invalid month in EGN.{RESET}")
        return

    try:
        birth_date_obj = date(year, month, dd)
        birth_date = birth_date_obj.strftime("%d %B %Y")
    except ValueError:
        print(f"{RED}Invalid birth date in EGN.{RESET}")
        return

    # Validate checksum
    weights = [2, 4, 8, 5, 10, 9, 7, 3, 6]
    checksum = sum(int(egn[i]) * weights[i] for i in range(9)) % 11
    calculated_check_digit = checksum if checksum < 10 else 0
    is_valid = calculated_check_digit == check_digit

    # Age
    today = date.today()
    age = today.year - year - ((today.month, today.day) < (month, dd))
    is_adult = age >= 18

    typewriter(f"\n{CYAN}Details from the EGN:{RESET}")
    print(f"{CYAN}Input EGN: {YELLOW}{egn}")
    print(f"{CYAN}Validity: {GREEN if is_valid else RED}{'Valid' if is_valid else 'Invalid'}{RESET}")
    print(f"{CYAN}Birth Date: {YELLOW}{birth_date}")
    print(f"{CYAN}Gender: {YELLOW}{gender}")
    print(f"{CYAN}Age: {YELLOW}{age}")
    print(f"{CYAN}Is Adult: {YELLOW}{'Yes' if is_adult else 'No'}")
    print(f"{CYAN}Century: {YELLOW}{year // 100 * 100}s")
    print(f"{CYAN}Registration Message: {GREEN}Born in Bulgaria, registered as {gender} on {birth_date}.{RESET}")
    print(f"{CYAN}{'-' * 50}{RESET}")


def interpret_italian_codice_fiscale(codice):
    months = {'A':'January','B':'February','C':'March','D':'April',
              'E':'May','H':'June','L':'July','M':'August',
              'P':'September','R':'October','S':'November','T':'December'}
    comuni = {'H501':'Rome','F205':'Milan','G273':'Naples','D612':'Florence','Z404':'Foreign'}

    if len(codice) != 16:
        print(f"{RED}Invalid Codice Fiscale length.{RESET}")
        return

    sname = codice[0:3]; fname = codice[3:6]
    yc = codice[6:8]; mc = codice[8]; dc = codice[9:11]
    cc = codice[11:15]; check = codice[15]

    try:
        year = int(yc)
        current_yy = date.today().year % 100
        birth_year = (1900 + year if year <= current_yy else 1900 + year)
        month = months.get(mc, None)
        day = int(dc)
        gender = "Female" if day > 40 else "Male"
        birth_day = day - 40 if day > 40 else day
        if not month:
            print(f"{RED}Invalid month code.{RESET}")
            return

        birth_date = f"{birth_day:02d} {month} {birth_year}"
        comune = comuni.get(cc, "Unknown Comune")

        typewriter(f"\n{CYAN}Details from the Codice Fiscale:{RESET}")
        print(f"{CYAN}Input ID: {YELLOW}{codice}")
        print(f"{CYAN}Surname Code: {YELLOW}{sname}")
        print(f"{CYAN}Name Code: {YELLOW}{fname}")
        print(f"{CYAN}Year of Birth: {YELLOW}{birth_year}")
        print(f"{CYAN}Month of Birth: {YELLOW}{month}")
        print(f"{CYAN}Day of Birth: {YELLOW}{birth_day}")
        print(f"{CYAN}Gender: {YELLOW}{gender}")
        print(f"{CYAN}Comune Code: {YELLOW}{cc}")
        print(f"{CYAN}Comune Name: {YELLOW}{comune}")
        print(f"{CYAN}Check Character: {YELLOW}{check}")
        print(f"{CYAN}Full Birth Date: {YELLOW}{birth_date}")
        print(f"{CYAN}Country: {YELLOW}Italy")
        print(f"{CYAN}Registration Message: {GREEN}Born in {comune} on {birth_date}.{RESET}")
        print(f"{CYAN}{'-' * 50}{RESET}")
    except ValueError:
        print(f"{RED}Invalid numerical values in the Codice Fiscale.{RESET}")


def interpret_swedish_personnummer(pnr):
    import re

    # Normalize format (remove dash/plus and spaces)
    pnr = pnr.strip().replace(" ", "").replace("-", "").replace("+", "")

    if not re.match(r"^\d{10}$|^\d{12}$", pnr):
        print(f"{RED}Invalid format. Use YYMMDD-XXXX or YYYYMMDD-XXXX.{RESET}")
        return

    # Extract components
    if len(pnr) == 12:
        year = int(pnr[0:4])
        month = int(pnr[4:6])
        day = int(pnr[6:8])
        serial = pnr[8:11]
        check_digit = int(pnr[11])
    else:  # 10-digit format
        yy = int(pnr[0:2])
        month = int(pnr[2:4])
        day = int(pnr[4:6])
        serial = pnr[6:9]
        check_digit = int(pnr[9])

        # Determine century
        current_year = date.today().year
        current_century = current_year // 100 * 100
        century = current_century if yy <= (current_year % 100) else current_century - 100
        year = century + yy

    # Validate birth date
    try:
        birth_date_obj = date(year, month, day)
        birth_date = birth_date_obj.strftime("%d %B %Y")
    except ValueError:
        print(f"{RED}Invalid birth date in personal number.{RESET}")
        return

    # Determine gender
    gender_digit = int(serial[-1])
    gender = "Male" if gender_digit % 2 == 1 else "Female"

    # Calculate Luhn checksum
    def luhn_check(num):
        digits = [int(x) for x in num]
        total = 0
        for i in range(len(digits)):
            val = digits[i]
            if i % 2 == 0:
                val *= 2
                if val > 9:
                    val -= 9
            total += val
        return total % 10 == 0

    luhn_input = (pnr[-10:-1]) if len(pnr) == 12 else (pnr[0:9])
    valid_luhn = luhn_check(luhn_input + str(check_digit))

    # Age calculation
    today = date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    is_adult = age >= 18

    typewriter(f"\n{CYAN}Details from the Swedish Personnummer(10 digit format):{RESET}")
    print(f"{CYAN}Input ID: {YELLOW}{pnr}")
    print(f"{CYAN}Formatted Date of Birth: {YELLOW}{birth_date}")
    print(f"{CYAN}Gender: {YELLOW}{gender}")
    print(f"{CYAN}Age: {YELLOW}{age}")
    print(f"{CYAN}Is Adult: {YELLOW}{'Yes' if is_adult else 'No'}")
    print(f"{CYAN}Checksum Validity: {GREEN if valid_luhn else RED}{'Valid' if valid_luhn else 'Invalid'}{RESET}")
    print(f"{CYAN}Country: {YELLOW}Sweden")
    print(f"{CYAN}Registration Message: {GREEN}Born in Sweden, registered as {gender} on {birth_date}.{RESET}")
    print(f"{CYAN}{'-' * 50}{RESET}")


def interpret_dutch_bsn(bsn):
    if len(bsn) != 9 or not bsn.isdigit():
        print(f"{RED}Invalid BSN format (must be 9 digits).{RESET}")
        return

    digits = [int(d) for d in bsn]

    # Apply 11-proof checksum:
    # Sum = 9*digit1 + 8*digit2 + ... + 2*digit8 + (-1)*digit9
    total = sum((9 - i) * digits[i] for i in range(8)) - digits[8]

    if total % 11 == 0:
        print(f"{GREEN}Valid BSN number. \n Info can not be decoded from this number, \n as this tipe of code is more private \n then the others.{RESET}")
    else:
        print(f"{RED}Invalid BSN number (failed checksum).{RESET}")




def main():
    while True:
        clear_screen()
        logo()
        typewriter(f"{CYAN}Select country for the ID number:{RESET}")
        print(f"{YELLOW}1. Romania\n2. Bulgaria\n3. Italy\n4. Sweden(10-digit format)\n5. Netherlands{RESET}")
        country_choice = input(f"{CYAN}Enter country number: {RESET}").strip()

        country_map = {
            "1": "Romania",
            "2": "Bulgaria",
            "3": "Italy",
            "4": "Sweden(10-digit format)",
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
