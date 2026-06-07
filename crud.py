import secrets

def id_gen():
    return secrets.token_hex(4)

def read_status(a):
    if a:
        return "📚 Shelved"
    else:
        return "⏳ Current Read"

def new_book(a,b,c):
    structure = {
    "id": id_gen(),
    "name": a,
    "finished": b,
    "notes": c
    }
    return structure

