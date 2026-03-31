import reflex as rx

def footer():
    return rx.vstack(
        rx.hstack(
            rx.link("About", href="/about"),
            rx.link("GitHub",href="https://github.com"),
            rx.link("Contact",href="/contact"),
            spacing="5",
        ),
        rx.text(" 2026 AI Code Reviewer"),
        padding="20px",
        align="center")
