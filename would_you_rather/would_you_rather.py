import reflex as rx
from .pages import index
from .pages import result
app = rx.App()
app.add_page(index.index)
app.add_page(result.result)
