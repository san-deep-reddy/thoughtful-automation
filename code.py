def sort(width, height, length, mass):

    volume = length * width * height
    bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    heavy = mass >= 20

    if bulky or heavy:
        return "SPECIAL"
    elif bulky and heavy:
        return "REJECTED"
    else:
        return "STANDARD"
