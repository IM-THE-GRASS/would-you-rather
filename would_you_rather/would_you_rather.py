import reflex as rx
import random
import json
f = open("choices.json")
filedata = f.read()
f.close()

class state(rx.State):
    scenarios = json.loads(filedata)
    current_scenario: dict = random.choice(scenarios)
    
    option1 = current_scenario["option1"]
    option2 = current_scenario["option2"]
    choice: str = ""

    def new_scenario(self):
        self.current_scenario = random.choice(self.scenarios)
        self.choice = ""

    def make_choice(self, option: str):
        self.choice = option

def index():
    return rx.center(
        rx.vstack(
            rx.heading("Would You Rather?", size="2xl"),
            rx.box(
                rx.vstack(
                    rx.text(state.current_scenario["option1"]),
                    rx.text("OR"),
                    rx.text(state.current_scenario["option2"]),
                    spacing="4",
                ),
            ),
            rx.hstack(
                rx.button(
                    state.current_scenario["option1"],
                    on_click=state.make_choice(state.current_scenario["option1"]),
                ),
                rx.button(
                    state.current_scenario["option2"],
                    on_click=state.make_choice(state.current_scenario["option2"]),
                ),
            ),
            rx.text(f"You chose: {state.choice}"),

            rx.button("Next Scenario", on_click=state.new_scenario),
            width="100%",
            max_width="600px",
            spacing="4",
        ),
        height="100vh",
    )

app = rx.App()
app.add_page(index)
