import re
from medicine_corrector import correct_single_medicine_name


def clean_medicine_name(name):
    name = name.strip()

    name = re.sub(r"^(tab|tablet|cap|capsule|syp|syrup|inj)\.?\s*", "", name, flags=re.I)
    name = re.sub(r"\b(morning|afternoon|night|days|day|before|after|food)\b", "", name, flags=re.I)
    name = re.sub(r"\b(od|bd|tds|qid|hs|sos|x|v|y|jf)\b", "", name, flags=re.I)
    name = re.sub(r"\d+\s*(mg|ml|mcg|g)?", "", name, flags=re.I)
    name = re.sub(r"[^A-Za-z+\- ]", " ", name)
    name = re.sub(r"\s+", " ", name).strip()

    return name


def extract_medicine_names(text):
    print("OCR TEXT:")
    print(text)
    medicines = []

    for raw_line in text.splitlines():
        line = raw_line.strip()

        if not line:
            continue

        lower = line.lower()

        if any(word in lower for word in ["next visit", "signature", "doctor", "date"]):
            continue

        if re.match(r"^\s*\d+", line):
            line = re.sub(r"^\s*\d+\s*", "", line)

            medicine = clean_medicine_name(line)

            if medicine:
                medicine = correct_single_medicine_name(medicine)

                if medicine and medicine not in medicines:
                    medicines.append(medicine)

    print("FINAL MEDICINES:", medicines)
    return medicines