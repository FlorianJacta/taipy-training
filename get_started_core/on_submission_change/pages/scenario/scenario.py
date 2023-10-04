from taipy.gui import Markdown

lol = "lol"

def on_submission(state, submittable , details):
    print(submittable, details)
    print('hello')

scenario = None

def on_init(state):
    state.lol = 'hello'

def on_change(state):
    print("Local")

scenario_md = Markdown('pages/scenario/scenario.md')