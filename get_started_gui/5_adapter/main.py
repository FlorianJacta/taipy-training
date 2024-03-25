from taipy.gui import Gui

selected = []

class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

person_a = Person(1, "Jack")
person_b = Person(2, "Peter")

selector_lov = [person_a, person_b]

page = """
<|{selected}|selector|lov={selector_lov}|adapter={lambda s: s.name}|>

<|{selected.name + ' ' + str(selected.id)}|>
"""

gui = Gui(page)
gui.run()