people = [
    {"name": "Levi", "surname": "Ackerman"},
    {"name": "Mikasa", "surname": "Ackerman"},
    {"name": "Eren", "surname": "Yeager"},
    {"name": "Armin", "surname": "Arlert"},
    {"name": "Historia", "surname": "Reiss"},
    {"name": "Reiner", "surname": "Braun"},
    {"name": "Erwin", "surname": "Smith"},
    {"name": "Marco", "surname": "Bott"},
    {"name": "Zeke", "surname": "Jaeger"},
    {"name": "Hange", "surname": "Zoe"}
]

messages = ["Thank you for your support:)!", "System keeps crashing, I need urgent help!", "I am very angry, nothing works for 3 days!", "Titans are comming, joins us in battle"]

current_id = _items[-1]["json"]["id"]

def pick(arr, index):
    return arr[index % len(arr)]

def get_next_id(current_id):
    # Sprawdzamy czy ID to "empty" lub czy jest puste
    if current_id == "empty" or not current_id:
        return "TICKET-001"
    else:
        # Rozdzielamy stringa TICKET-001 na ["TICKET", "001"]
        try:
            parts = current_id.split("-")
            # Bierzemy część z numerem (001) i zamieniamy na int (1)
            number = int(parts[1])
            # Zwiększamy o 1 i formatujemy z powrotem do 002
            return f"TICKET-{number + 1:03d}"
        except:
            # W razie błędu formatu, bezpiecznie wracamy do początku
            return "TICKET-001"

def build_email(name, surname, i):
    return f"{name.lower()}.{surname.lower()}@gmail.com"          

def generate_record(i, current_id):
    new_id = get_next_id(current_id)
    try:
        number = int(new_id.split("-")[1])
    except:
        number = 1
      
    person_index = (number - 1) % len(people)
    person = people[person_index]
    name = person["name"]
    surname = person["surname"]
    email = build_email(name, surname, number) # użyłem number zamiast i
    message = pick(messages, number)           # użyłem number zamiast i
    return {
        "json": {
            "id": new_id,
            "name": name, 
            "surname": surname, 
            "email": email, 
            "message": message
        }
    }

tracking_id = _items[-1]["json"]["id"] 
results = []

for i in range(5): 
    record = generate_record(i, tracking_id)
    results.append(record)
    tracking_id = record["json"]["id"]

return results