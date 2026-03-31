import reflex as rx
from app.states.code_state import CodeState


def analyze_page():
    return rx.center(
        rx.vstack(
            # ---------------------------
            # TITLE
            # ---------------------------
            rx.heading("AI Code Analyzer", size="7"),

            # ---------------------------
            # INPUT BOX
            # ---------------------------
            rx.text_area(
                placeholder="Paste your code here...",
                value=CodeState.code,
                on_change=CodeState.set_code,
                width="100%",
                height="200px",
            ),

            # ---------------------------
            # BUTTONS
            # ---------------------------
            rx.hstack(
                rx.button(
                    "Analyze",
                    on_click=CodeState.analyze,
                    is_loading=CodeState.is_loading,
                    color_scheme="blue",
                ),
                rx.button(
                    "Reset",
                    on_click=CodeState.clear_all,
                    color_scheme="red",
                ),
            ),

            # ---------------------------
            # SCORE + TIME
            # ---------------------------
            rx.cond(
                CodeState.score > 0,
                rx.text(f"Score: {CodeState.score}/100"),
            ),

            rx.cond(
                CodeState.execution_time > 0,
                rx.text(f"Execution Time: {CodeState.execution_time}s"),
            ),

            # ---------------------------
            # ERRORS
            # ---------------------------
            rx.cond(
                CodeState.errors,
                rx.box(
                    rx.heading("Errors Detected:", size="5"),
                    rx.foreach(
                        CodeState.errors,
                        lambda err: rx.text(f"• {err}")
                    ),
                    width="100%",
                ),
            ),

            # ---------------------------
            # OUTPUT (CORRECTED CODE)
            # ---------------------------
            rx.cond(
                CodeState.corrected_code != "",
                rx.box(
                    rx.heading("Suggested Fix:", size="5"),
                    rx.code_block(
                        CodeState.corrected_code,
                        language="python",
                        width="100%",
                    ),
                    width="100%",
                ),
            ),

            spacing="4",
            width="70%",
        ),
        padding="40px",
    )