from taipy.gui import Markdown

lol = "lol"

def on_submission(state, submittable , details):
    print(submittable, details)
    print('hello')

scenario = None

def init(state):
    state.lol = 'hello'



scenario_md = Markdown('pages/scenario/scenario.md')