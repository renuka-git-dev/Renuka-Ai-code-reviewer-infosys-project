import reflex as rx
import time
from backend.analyzer import analyze_code_local as analyze_code


class CodeState(rx.State):
    # ---------------------------
    # INPUT
    # ---------------------------
    code: str = ""

    # ---------------------------
    # OUTPUT
    # ---------------------------
    corrected_code: str = ""
    errors: list[str] = []
    score: int = 0

    # ---------------------------
    # EXTRA (for better UX)
    # ---------------------------
    is_loading: bool = False
    execution_time: float = 0.0

    # ---------------------------
    # ACTION: UPDATE CODE INPUT
    # ---------------------------
    def set_code(self, value: str):
        self.code = value

    # ---------------------------
    # ACTION: ANALYZE CODE
    # ---------------------------
    def analyze(self):
        if not self.code.strip():
            self.corrected_code = "⚠️ Please paste some code first."
            self.errors = []
            self.score = 0
            return

        self.is_loading = True

        start_time = time.time()

        try:
            result = analyze_code(self.code)

            self.corrected_code = result.get("suggestion", "")
            self.errors = result.get("errors", [])
            self.score = result.get("score", 0)

        except Exception as e:
            self.corrected_code = f"❌ Error during analysis: {str(e)}"
            self.errors = []
            self.score = 0

        end_time = time.time()
        self.execution_time = round(end_time - start_time, 2)

        self.is_loading = False

    # ---------------------------
    # RESET EVERYTHING
    # ---------------------------
    def clear_all(self):
        self.code = ""
        self.corrected_code = ""
        self.errors = []
        self.score = 0
        self.execution_time = 0.0
        self.is_loading = False