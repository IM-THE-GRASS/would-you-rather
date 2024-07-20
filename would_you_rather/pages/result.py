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
    dic:dict
    option_1_num:int
    option_2_num:int
    agreed_percent_msg:str
    def get_agreed_percent(self):
        if self.choice == "option1":
            print("1")
            agreed_percent = round((self.option_1_num / (self.option_1_num + self.option_2_num)) * 100)
            if agreed_percent < 50:
                self.agreed_percent_msg = f"Only {agreed_percent}% of people agreed with you 😔"
            else:
                self.agreed_percent_msg = f"{agreed_percent}% of people agreed with you! 🥳"
        else:
            print("2")
            agreed_percent = round((self.option_2_num / (self.option_1_num + self.option_2_num)) * 100)
            if agreed_percent < 50:
                self.agreed_percent_msg = f"Only {agreed_percent}% of people agreed with you 😔"
            else:
                self.agreed_percent_msg = f"{agreed_percent}% of people agreed with you! 🥳"
    def update_pie_data(self):

        if self.choice == "option2":
            self.pie_data = [
                    {"name": "Option 1", "value": self.option_1_num, "fill": "var(--red-8)"},
                    {"name": "Option 2", "value": self.option_2_num, "fill": "var(--green-8)"}
            ]
        else:
            self.pie_data = [
                    {"name": "Option 1", "value": self.option_1_num, "fill": "var(--green-8)"},
                    {"name": "Option 2", "value": self.option_2_num, "fill": "var(--red-8)"}
            ]
    def set_qid(self, new_qid):
        
        self.qid = int(new_qid)
        
        self.dic = self.stats[str(self.qid)]
        self.option_1_num = self.dic["option1"]
        self.option_2_num = self.dic["option2"]
        self.get_agreed_percent()
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
                State.agreed_percent_msg,
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
            rx.button(
                "Next Scenario",
                color_scheme="teal",
                size="3",
                width="400px",
                on_click=rx.redirect(
                    "/"
                ),
            ),
            
            width="800px",
            spacing="6",
            align="center",
        ),
#        rx.cond(
#            State.choice != "",
#            rx.text(f"You chose: {State.current_scenario[State.choice]}", font_size="lg", font_weight="bold", color="purple.500", text_align="center"),
#        ),
        min_height="100vh",
        bg="#12FBE60C",
        display="flex",
        justify_content="center",
        align_items="center",
        on_mount= State.get_arguments
    )
