import re
from medicine_corrector import correct_single_medicine_name


def clean_medicine_name(name):
    name = name.strip()

    name = re.sub(r"^(tab|tablet|cap|capsule|syp|syrup|inj)\.?\s*", "", name, flags=re.I)
    name = re.sub(r"\b(morning|afternoon|night|days|day|before|after|food)\b", "", name, flags=re.I)
    name = re.sub(r"\b(od|bd|tds|qid|hs|sos|x|v|y|jf)\b", "", name, flags=re.I)
    name = re.sub(r"\bimg\b", "", name, flags=re.I)  # OCR error
    name = re.sub(r"\d+\s*(mg|ml|mcg|g)?", "", name, flags=re.I)
    name = re.sub(r"[^A-Za-z+\- ]", " ", name)
    name = re.sub(r"\s+", " ", name).strip()

    return name


def extract_medicine_names(text):
    print("OCR TEXT:")
    print(text)

    medicines = []

    skip_words = ["fatty acid", "capsules", "morning",
                  "afternoon", "night", "medicine"]

    for raw_line in text.splitlines():
        line = raw_line.strip()

        if not line:
            continue

        lower = line.lower()

        if any(word in lower for word in
               ["next visit", "signature", "doctor", "date"]):
            continue

        # Accept serial numbers like 1, l, I
        if re.match(r"^\s*(\d+|[lI])\s+", line):
            line = re.sub(r"^\s*(\d+|[lI])\s+", "", line)

            medicine = clean_medicine_name(line)

            if not medicine:
                continue

            if any(w in medicine.lower() for w in skip_words):
                continue

            medicine = correct_single_medicine_name(medicine)

            if medicine and medicine not in medicines:
                medicines.append(medicine)

    print("FINAL MEDICINES:", medicines)
    return medicines