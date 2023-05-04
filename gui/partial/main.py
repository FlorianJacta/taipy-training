from taipy.gui import Gui 


title = 1
md = """
<|{title}|number|on_change=change_partial|>

<|part|partial={p}|>
"""

def change_partial(state):
    title_int = int(state.title)
    new_html = f'<h{title_int}>test{title_int}</h{title_int}>'
    print(new_html)
    state.p.update_content(state, new_html)

gui = Gui(md)
p = gui.add_partial("<h1>test</h1>")
gui.run()