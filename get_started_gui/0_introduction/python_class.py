from taipy.gui import Gui, Page, Markdown
import taipy.gui.builder as tgb
from math import cos, exp


def compute_data(decay: int) -> list:
    return [cos(i / 6) * exp(-i * decay / 600) for i in range(100)]


class SinWavePage(Page):
    # --------- State Initialization  --------- #
    def __init__(self):
        self.value: int = 10 
        self.data: list = compute_data(self.value)

        super().__init__()

    def on_slider(self):
        self.data = compute_data(self.value)

    ## ------- Page Creation ------- ##
    def create_page(self):
        with tgb.Page() as page:
            tgb.text(value="# Taipy Demo", mode="md")
            tgb.text(value="Value: {value}")
            tgb.slider(value="{value}", on_change=self.on_slider)
            tgb.chart(data="{data}")
        return page


if __name__ == '__main__':
    Gui(page=SinWavePage()).run()