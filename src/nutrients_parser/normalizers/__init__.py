from .split_energy import split_energy

def normalize_all(data):
    data = split_energy(data)
    return data