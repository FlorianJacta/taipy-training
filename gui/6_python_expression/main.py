from taipy.gui import Gui, notify

text = ""
revealed = False

page = """
<|{text if text else 'Write something in the input'}|>

<|{text}|input|on_change={lambda s: notify(s, 'i', s.text)}|>

<|part|render={len(text)>0}|
Part hidden and discovered after input
|>

-----

<|Push|button|on_action={lambda s: s.assign("revealed", True)}|>

<|part|render={revealed}|
Part hidden and discovered after button
|>
"""

Gui(page).run()