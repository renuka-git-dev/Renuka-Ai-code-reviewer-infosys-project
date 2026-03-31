import reflex as rx

def help_page():
    return rx.box(

        rx.vstack(
           

            rx.center(
                rx.box(

                    rx.vstack(
                        # 🔥 Title
                        rx.heading("Help & Support", size="8", color="white"),

                        rx.text(
                            "If you need assistance or have any queries, feel free to reach out to us.",
                            text_align="center",
                            color="white",
                        ),

                        # 📧 Emails
                        rx.box(
                            rx.vstack(
                                rx.text("📩 Support Email:", font_weight="bold", color="white"),
                                rx.text("support@aicodereviewer.com", color="white"),

                                rx.text("📧 Customer Care:", font_weight="bold", color="white", margin_top="10px"),
                                rx.text("care@aicodereviewer.com", color="white"),

                                spacing="3",
                                align="center",
                            ),
                        ),

                        spacing="6",
                        align="center",
                    ),

                    # 🔥 Styled Box
                    bg="rgba(0,0,0,0.6)",
                    padding="40px",
                    border_radius="20px",   # curved edges
                    width="50%",
                    box_shadow="0px 0px 25px rgba(0,0,0,0.5)",

                    # 🔥 Optional glass effect
                    backdrop_filter="blur(10px)",
                    border="1px solid rgba(255,255,255,0.2)",
                ),
            ),

            spacing="6",
        ),

        # 🌌 Background Image
        width="100%",
        min_height="100vh",
        background_image="url('/background.jpg')",
        background_size="cover",
        background_position="center",
    )