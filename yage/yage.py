import reflex as rx

from rxconfig import config
from .components import footer, heading, subtext


class State(rx.State):
    query: str = ""

    @rx.event
    def set_query(self, new_query: str):
        self.query = new_query


def search_bar() -> rx.Component:
    return (
        rx.vstack(
            rx.hstack(
                rx.input(
                    variant="soft",
                    placeholder="Consumable(s)/Drug(s)",
                    on_change=State.set_query,
                    width=rx.breakpoints(initial="300px", sm="300px", lg="700px"),
                    height="40px",
                    style={
                        "_placeholder": {
                            "color": "var(--gray-7)",
                            "font_weight": "500",
                        },
                    },
                    radius="large",
                ),
                rx.upload(
                    rx.button(
                        rx.icon("upload"),
                        bg="dodgerblue",
                        height="38px",
                    ),
                    accept={
                        "image/png": [".png"],
                        "image/jpeg": [".jpg", ".jpeg"],
                        "image/webp": [".webp"],
                    },
                    max_files=1,
                    disabled=False,
                    no_keyboard=True,
                    border="none",
                    padding="0em",
                ),
                spacing="2",
                align="center",
            ),
            rx.button("Search", type="submit", height="38px", width="100%"),
        ),
    )


def header() -> rx.Component:
    return (
        rx.vstack(
            heading(config.app_name),
            subtext(config.app_desc),
            spacing="3",
            justify="center",
            align="center",
        ),
    )


def index() -> rx.Component:
    return rx.box(
        rx.container(
            rx.color_mode.button(position="top-right"),
            rx.center(
                rx.vstack(
                    header(),
                    search_bar(),
                    spacing="4",
                    justify="center",
                    min_height="85vh",
                    align="center",
                ),
            ),
        ),
        footer(),
    )


app = rx.App()
app.add_page(index)
