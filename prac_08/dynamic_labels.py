from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Kivy app to list names within a dictionary and dynamically creates a separate label for each one"""
    label_text = StringProperty()

    def __init__(self, **kwargs):
        """Initialize data"""
        super().__init__(**kwargs)
        self.name_to_label = {"Sinclair": "Boy", "Demian": "Friend", "Kromer": "Bully"}

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        for name in self.name_to_label:
            temp_label = Label(text=f"{name} is a {self.name_to_label[name]}")
            self.root.ids.main.add_widget(temp_label)
        return self.root


DynamicLabelsApp().run()
