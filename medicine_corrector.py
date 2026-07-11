from difflib import get_close_matches

MEDICINE_LIST = [
    "Paracetamol", "Azithromycin", "Azee", "Amoxicillin", "Augmentin",
    "Ibuprofen", "Combiflam", "Cetirizine", "Metformin", "Aspirin",
    "Ecosprin", "Omeprazole", "Pantoprazole", "Dolo", "Crocin",
    "Calpol", "Allegra", "Montair", "Levocetirizine", "Vitamin D3",
    "Calcium", "Shelcal", "Cough Syrup","Amlodipine", "Telmisartan", "Atorvastatin"
]


def correct_single_medicine_name(word):
    word = str(word).strip().title()
    if len(word) < 3:
        return ""
    match = get_close_matches(word, MEDICINE_LIST, n=1, cutoff=0.70)
    return match[0] if match else word


def correct_medicine_name(text):
    corrected = []
    for word in text.split("\n"):
        name = correct_single_medicine_name(word)
        if name and name not in corrected:
            corrected.append(name)
    return corrected
