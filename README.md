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
Input ID: 0249156007
Gender: Female
Birth Date: 15 September 1902
Country: Bulgaria
Registration Message: Born in Bulgaria, registered as Female on 15 September 1902.
```

---

### 🇮🇹 Italy (Codice Fiscale)

**Input:** `RSSMRA85M01H501U`

```
Input ID: RSSMRA85M01H501U
Gender: Male
Birth Date: 01 December 1985
Country: Italy
Registration Message: Born in Italy, registered as Male on 01 December 1985.
```

---

### 🇸🇪 Sweden (Personnummer)

**Input:** `990203+1234`

```
Input ID: 990203+1234
Gender: Male
Birth Date: 03 February 1999
Country: Sweden
Registration Message: Born in Sweden, registered as Male on 03 February 1999.
```

---

### 🇳🇱 Netherlands (BSN)

**Input:** `123456782`

```
Input ID: 123456782
Gender: Male
Country: Netherlands
Registration Message: Registered in the Netherlands as Male.
```

---

## 📦 Installation

No installation needed. Just run the script with Python 3.

---



