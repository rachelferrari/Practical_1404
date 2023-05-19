import random

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """BoxLayoutDemo is a Kivy App for saying hello to the user/inputted name."""
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_clear(self):
        """Handle clearing the input name."""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_greet(self):
        """Handle greeting the input name."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"


BoxLayoutDemo().run()
