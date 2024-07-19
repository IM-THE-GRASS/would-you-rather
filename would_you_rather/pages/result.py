import random
import json
import reflex as rx

f = open("choices.json")
filedata = f.read()
f.close()

class State(rx.State):
    scenarios = json.loads(filedata)
    current_scenario: dict = random.choice(scenarios)
    choice: str = ""

    def new_scenario(self):
        self.current_scenario = random.choice(self.scenarios)
        self.choice = ""

    def make_choice(self, option: str):
        self.choice = option
@rx.page("/result/[qid]/[option]")
def result():
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
                    
                    spacing="4",
                    align="center",
                ),
                width="600px",
            ),
            rx.hstack(
                
                spacing="4",
                width="600px",
                justify="center",
            ),
            rx.cond(
                State.choice != "",
                rx.text(f"You chose: {State.choice}", font_size="lg", font_weight="bold", color="purple.500", text_align="center"),
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
    )