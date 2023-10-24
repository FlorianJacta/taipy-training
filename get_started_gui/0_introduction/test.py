from taipy.gui import Gui
from math import cos, exp

value = 10

page = """
Markdown
# Taipy *Demo*
"""

Gui(page).run(use_reloader=True, port=5002)