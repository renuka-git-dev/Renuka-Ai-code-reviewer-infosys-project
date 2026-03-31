import reflex as rx

def about():
    return rx.box(
        rx.vstack(
            # navbar(),  ❌ removed because you don't have it

            rx.center(
                rx.box(
                    rx.vstack(
                        # 🔥 Title
                        rx.heading(
                            "About AI Code Reviewer",
                            size="8",
                            color="white"
                        ),

                        # 🔹 Description
                        rx.text(
                            "AI Code Reviewer is an intelligent platform designed to "
                            "analyze, optimize, and improve Python code using advanced AI techniques.",
                            text_align="center",
                            color="white",
                        ),

                        # 🔹 Points (Features)
                        rx.vstack(
                            rx.text("• Real-time code analysis", color="white"),
                            rx.text("• PEP8 compliance checking", color="white"),
                            rx.text("• AI-powered suggestions for optimization", color="white"),
                            rx.text("• Detects errors and bad practices", color="white"),
                            rx.text("• Improves readability and performance", color="white"),
                            rx.text("• Helps developers learn best coding standards", color="white"),
                            rx.text("• Scalable and secure system design", color="white"),
                            spacing="2",
                            align="start",
                        ),

                        spacing="6",
                        align="center",
                    ),

                    # 🔥 BOX STYLING
                    bg="rgba(0, 0, 0, 0.6)",   
                    padding="40px",
                    border_radius="20px",
                    width="60%",
                    box_shadow="0px 0px 25px rgba(0,0,0,0.5)",  
                ),
            ),

            spacing="6",
        ),

        # 🔥 Background Image
        width="100%",
        min_height="100vh",
        background_image="url('/background.jpg')",
        background_size="cover",
        background_position="center",
    )