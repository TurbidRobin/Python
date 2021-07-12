from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.widget import Widget


class MainWidget(Widget):
	adj = input("Adjective : ")
	verb1 = input("Verb : ")
	verb2 = input("Verb : ")
	famous_person = input("Famous Person : ")
	text_input_str = StringProperty("Foo")

	mad_lib = f"Computer Programming is so {adj}! It makes me so excited all the time because \n I love to {verb1}. " \
f"Stay hydrated and {verb2} like you are {famous_person}!"

	def on_text_validate(self, widget):
		self.text_input_str = widget.text


class test(App):
	pass


test().run()
