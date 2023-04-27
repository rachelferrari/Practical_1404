COLOURS_TO_CODE = {"absolute zero": "#0048ba", "cadet grey": "#91a3b0", "frostbite": "#e936a7", "goldenrod": "#daa520",
                   "isabelline": "#f4f0ec", "magenta": "#ff00ff", "pale silver": "#c9c0bb", "purple": "#a020f0",
                   "radical red": "#ff355e", "slate blue": "#6a5acd"}

print(COLOURS_TO_CODE)
colours = input("Colours: ").lower()
while colours != "":
    if colours not in COLOURS_TO_CODE:
        print("Invalid input")
        colours = input("Colours: ").lower()
    else:
        print(COLOURS_TO_CODE[colours])
        colours = input("Colours: ").lower()
