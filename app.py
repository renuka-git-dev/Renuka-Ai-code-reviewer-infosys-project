import reflex as rx
from app.pages.analyze import analyze_page
from app.pages.about import about
from app.pages.help import help_page

# Navbar function
def navbar():
    return rx.hstack(
        rx.text("AI Code Reviewer", font_weight="bold", font_size="20px"),
        rx.spacer(),
        rx.hstack(
            rx.link("Analyze", href="/analyze"),
            rx.link("About", href="/about"),
            rx.link("Help", href="/help"),
            spacing="6",
        ),
        padding="20px",
        width="100%",
    )

# Home page function
def home_page():
    return rx.box(
        rx.vstack(
            navbar(),  # your navbar function
            rx.center(
                rx.vstack(
                    rx.heading("Welcome to AI Code Reviewer", font_size="64px"),
                    rx.text(
                        "The best place to correct your code",
                        font_size="24px",
                        color="gray",
                        text_align="center",
                    ),
                    rx.text(
                        "Detect errors, get suggestions, and improve instantly!",
                        font_size="18px",
                        color="gray",
                        text_align="center",
                    ),
                ),
                height="80vh",
            ),
        ),
        width="100vw",
        height="100vh",
        bg_image='url("assets/background.jpg")',
        bg_size="cover",
        bg_position="center",
    )

# Create the app object
app = rx.App()

# Add pages
app.add_page(home_page, route="/")
app.add_page(analyze_page, route="/analyze")
app.add_page(about, route="/about")
app.add_page(help_page, route="/help")