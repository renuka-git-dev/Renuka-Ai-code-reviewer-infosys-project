import reflex as rx

def home():
    return rx.box(
        # Full screen
        width="100vw",
        height="100vh",
        # Background image from assets
        background_image="url('/wallpaper.jpg')",
        background_size="cover",
        background_position="center",
        children=[
            rx.center(
                rx.vstack(
                    # ---------------------------
                    # LOGO (from assets)
                    # ---------------------------
                    rx.image(
                        src="/icon.jpg",   # make sure this is inside assets/
                        width="100px",
                        height="100px",
                    ),

                    # ---------------------------
                    # TITLE
                    # ---------------------------
                    rx.heading("Neural Compile", size="8"),

                    # ---------------------------
                    # TAGLINE
                    # ---------------------------
                    rx.text(
                        "AI-Powered Code Reviewer & Analyzer",
                        font_size="18px",
                        color="gray",
                    ),

                    # ---------------------------
                    # DESCRIPTION
                    # ---------------------------
                    rx.text(
                        "Paste your code, detect errors, get AI suggestions, and improve instantly.",
                        text_align="center",
                        max_width="500px",
                    ),

                    # ---------------------------
                    # BUTTON → ANALYZE PAGE
                    # ---------------------------
                    rx.link(
                        rx.button(
                            "Start Analyzing",
                            size="4",
                            color_scheme="blue",
                        ),
                        href="/analyze",
                    ),

                    spacing="5",
                ),
                height="80vh",
            )
        ]
    )