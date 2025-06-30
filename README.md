# IDI — ID Interpreter

**IDI** (Cross-national ID Parser) is a Python script that validates and interprets national identification numbers from several European countries: **Romania**, **Bulgaria**, **Italy**, **Sweden**, and **Netherlands**.

---

## 🌍 Supported Countries

- 🇷🇴 **Romania** — CNP (Cod Numeric Personal)
- 🇧🇬 **Bulgaria** — EGN (Единен граждански номер)
- 🇮🇹 **Italy** — Codice Fiscale
- 🇸🇪 **Sweden** — Personnummer
- 🇳🇱 **Netherlands** — BSN (Burgerservicenummer)

---

## ⚙️ Features

- Validates length and control digits
- Extracts birth date and gender
- Displays registration information
- Romanian CNP includes county (județ)
- Colored terminal output using ANSI codes

---

## ▶️ Usage

Run the script using Python 3:

```bash
python IDI.py
```

Follow the on-screen instructions to select the country and input the ID number.

---

## 📋 Example Outputs

### 🇷🇴 Romania (CNP)

**Input:** `1960527410018`

```
Enter the ID Number: 1960527410018

Details from the ID Number:
Input ID: 1960527410018
Validity: Invalid
Gender: Male
Birth Date: 27 May 1996
Country: Romania
Registration Message: Born in Romania, registered as 1-th person on 27 May 1996.
Age: 29
Is Adult: Yes
```

---

### 🇧🇬 Bulgaria (EGN)

**Input:** `0249156007`

```
Details from the EGN:
Input EGN: 0249156007
Validity: Valid
Birth Date: 15 September 1902
Gender: Female
Age: 121
Is Adult: Yes
Century: 1900s
Registration Message: Born in Bulgaria, registered as Female on 15 September 1902.
--------------------------------------------------

```

---

### 🇮🇹 Italy (Codice Fiscale)

**Input:** `RSSMRA85M01H501U`

```
Details from the Codice Fiscale:
Input ID: RSSMRA85M01H501U
Surname Code: RSS
Name Code: MRA
Year of Birth: 1985
Month of Birth: August
Day of Birth: 1
Gender: Male
Comune Code: H501
Comune Name: Rome
Check Character: U
Full Birth Date: 01 August 1985
Country: Italy
Registration Message: Born in Rome on 01 August 1985.
--------------------------------------------------

```

---

### 🇸🇪 Sweden (Personnummer)

**Input:** `990203+1234`

```
Details from the Swedish Personnummer(10 digit format):
Input ID: 9902031234
Formatted Date of Birth: 03 February 1999
Gender: Male
Age: 26
Is Adult: Yes
Checksum Validity: Valid
Country: Sweden
Registration Message: Born in Sweden, registered as Male on 03 February 1999.
--------------------------------------------------

```

---

### 🇳🇱 Netherlands (BSN)

**Input:** `123456782`

```
Valid BSN number. 
 Info can not be decoded from this number, 
 as this tipe of code is more private 
 then the others.

```

---

## 📦 Installation

No installation needed. Just run the script with Python 3.

---



