import reflex as rx


def footer() -> rx.Component:
    return (
        rx.box(
            rx.hstack(
                rx.link(
                    "Developed by Mohit Nair",
                    href="https://github.com/themohitnair",
                    underline="hover",
                    is_external=True,
                ),
                rx.link(
                    "Source Code",
                    href="https://github.com/themohitnair/yage",
                    underline="hover",
                    is_external=True,
                ),
                width="100%",
                justify="between",
                padding="1em",
            ),
            position="fixed",
            bottom="0",
            width="100%",
            bg="var(--accent-2)",
        ),
    )


def heading(text: str) -> rx.Component:
    return rx.heading(f"{text}", size="9", color="dodgerblue")


def subtext(text: str) -> rx.Component:
    return rx.text(f"{text}", size="4", color="var(--gray-a7)")
