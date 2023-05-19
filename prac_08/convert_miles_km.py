from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

KILOMETRES_IN_MILES = 1.60934


class ConvertMilesToKmApp(App):
    """ConvertMilestoKmApp is a Kivy App for converting miles (input) into kilometres (output)."""
    result = StringProperty()

    def build(self):
        """Built the Kivy app for the kv file."""
        Window.size = (300, 100)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self):
        """Handle calculation, output result to label widget."""
        value = self.handle_invalid()
        self.result = str(value * KILOMETRES_IN_MILES)

    def handle_increment(self, increment):
        """Handle increase or decrease of inputted number for calculation."""
        value = self.handle_invalid()
        self.root.ids.input_number.text = str(value + increment)

    def handle_invalid(self):
        """Handle invalid inputs."""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0.0


ConvertMilesToKmApp().run()
