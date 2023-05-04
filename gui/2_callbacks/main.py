from taipy.gui import Gui, notify 

text = ""

page_1 = """
# Page 1
<|{text}|>
"""

page_2 = """
# Page 2
<|Raise error|button|on_action=raise_error|>
"""

hidden_page_3 = """
# Hidden Page
"""

def raise_error(state):
    raise(ValueError("This is an error"))


def on_init(state):
    print("When a new client connects, this function is called")
    state.text = "Hello, world!"

def on_change(state, var_name, var_value):
    notify(state, 'i', f'{var_name} changed')

def on_navigate(state, page_name: str): 
    if page_name == "hidden_page_3":
        return "page_1"
    notify(state, 'i', f'{page_name} navigated')
    return page_name

def on_exception(state, function_name: str, ex: Exception):
    err = f"A problem occured in {function_name}"
    print(err)
    notify(state, 'e', err)

pages = {
         "/":"<|navbar|>",
         "page_1": page_1,
         "page_2": page_2, 
         "hidden_page_3": hidden_page_3}

Gui(pages=pages).run()

