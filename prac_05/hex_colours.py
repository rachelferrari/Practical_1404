colours_to_code = {"absolute zero": "#0048ba", "cadet grey": "#91a3b0", "frostbite": "#e936a7", "goldenrod": "#daa520",
                   "isabelline": "#f4f0ec", "magenta": "#ff00ff", "pale silver": "#c9c0bb", "purple": "#a020f0",
                   "radical red": "#ff355e", "slate blue": "#6a5acd"}

colours = input("Colours: ")
while colours != "":
    if colours not in colours_to_code:
        print("Invalid input")
        colours = input("Colours: ")
    else:
        print(colours_to_code[colours])
        colours = input("Colours: ")
