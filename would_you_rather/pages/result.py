import random
import json
import reflex as rx

f = open("choices.json")
scenariofiledata = f.read()
f.close()
f = open("stats.json")
statfiledata = f.read()
f.close()

from ..components import pie
class State(rx.State):
    scenarios = json.loads(scenariofiledata)
    stats = json.loads(statfiledata)
    pie_data:list
    choice:str
    qid:int
    
    def update_pie_data(self):
        dic = self.stats[str(self.qid)]
        self.pie_data = [
            {"name": "Option 1", "value": dic["option1"]},
            {"name": "Option 2", "value": dic["option2"]}
        ]
    def set_qid(self, new_qid):
        self.qid = int(new_qid)
        self.update_pie_data()
    def set_choice(self, new_choice):
        self.choice = new_choice
    def get_arguments(self):
        return [
            rx.call_script(
                """var urlParams = new URLSearchParams(window.location.search);
                urlParams.get("choice")""",
                callback= State.set_choice
            ),
            rx.call_script(
                """var urlParams = new URLSearchParams(window.location.search);
                urlParams.get("qid")""",
                callback= State.set_qid
            ),
        ]
    
    

def result():
    return rx.box(
        rx.vstack(
            rx.heading(
                State.qid,
                size="2xl",
                color="#ADF0DD",
                font_weight="bold",
                text_align="center"
            ),
            pie.pie(State.pie_data),
            rx.box(
                rx.vstack(
                    
                    spacing="4",
                    align="center",
                ),
                width="600px",
            ),
            
            
            width="800px",
            spacing="6",
            align="center",
        ),
        min_height="100vh",
        bg="#12FBE60C",
        display="flex",
        justify_content="center",
        align_items="center",
        on_mount= State.get_arguments
    )
