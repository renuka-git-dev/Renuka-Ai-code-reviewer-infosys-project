import reflex as rx

def header():
    return rx.hstack(
        rx.hstack(
            rx.image(
                src="/icon.png",
                width="30px",
            ),
            rx.text("AI Code Reviewer", font_weight="bold"),
            align="center",
            spacing="2",
        ),

        rx.spacer(),

        rx.hstack(
            rx.text("Home"),
            rx.text("History"),
            rx.text("About"),
            rx.text("Help"),
            spacing="4",
        ),

        padding="1em",
        width="100%",
        bg="black",
        color="white",
    )