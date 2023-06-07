from taipy.gui import Gui

selected = []

a = [1, 2]
b = [2, 3]

selector_lov = [a, b]

page = """
<|{selected}|selector|lov={selector_lov}|adapter={lambda s: s.name}|>
"""

gui = Gui(page)
gui.run()