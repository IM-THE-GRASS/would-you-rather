import random
import json
import reflex as rx

f = open("choices.json")
filedata = f.read()
f.close()

class State(rx.State):
    scenarios = json.loads(filedata)
    current_scenario: dict = random.choice(scenarios)
    choice:str
    redirect_url:str
    qid:int
    def get_redirect_url(self):
        self.redirect_url = "/result?qid=" + str(self.qid)+ "&choice=" + self.choice
    def new_scenario(self):
        self.current_scenario = random.choice(self.scenarios)
        self.choice = ""
        self.qid = self.scenarios.index(self.current_scenario)
    def make_choice(self, option: str):
        self.choice = option
        self.get_redirect_url()
        
def confirm_button():
    return rx.cond(
        State.choice != "",
        rx.button(
            "Confirm",
            color_scheme="teal",
            size="3",
            width="600px",
            on_click=rx.redirect(
                State.redirect_url
            ),
        ),
        rx.button(
            "Confirm",
            color_scheme="teal",
            disabled=True,
            size="3",
            width="600px",
            on_click=rx.redirect(
                State.redirect_url
            ),
        )
    )
    
def index():
    return rx.box(
        rx.vstack(
            rx.heading(
                "Would You Rather?",
                size="2xl",
                color="#ADF0DD",
                font_weight="bold",
                text_align="center"
            ),
            rx.box(
                rx.vstack(
                    rx.text(State.current_scenario["option1"], font_size="20px", font_weight="bold", text_align="center", color ="#0BD8B6"),
                    rx.text("OR", font_size="25px", font_weight="bolder", color="#ADF0DD"),
                    rx.text(State.current_scenario["option2"], font_size="20px", font_weight="bold", text_align="center",color ="#0BD8B6"),
                    spacing="4",
                    align="center",
                ),
                width="600px",
            ),
            rx.hstack(
                rx.button(
                    State.current_scenario["option1"],
                    on_click=lambda: State.make_choice("option1"),
                    color_scheme="teal",
                    width="45%",
                    font_weight="bold",
                    size="3",
                    height="4em"
                ),
                rx.button(
                    State.current_scenario["option2"],
                    on_click=lambda: State.make_choice("option2"),
                    color_scheme="teal",
                    font_weight="bold",
                    width="45%",
                    size="3",
                    height="4em",
                ),
                spacing="4",
                width="600px",
                justify="center",
            ),
#            rx.cond(
#                State.choice != "",
#                rx.text(f"You chose: {State.current_scenario[State.choice]}", font_size="lg", font_weight="bold", color="purple.500", text_align="center"),
#            ),
            confirm_button(),
            
            width="800px",
            spacing="6",
            align="center",
        ),
        min_height="100vh",
        bg="#12FBE60C",
        display="flex",
        justify_content="center",
        align_items="center",
        on_mount=State.new_scenario
    )