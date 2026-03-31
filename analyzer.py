# backend/analyzer.py

from backend.code_parser import CodeParser
from backend.error_detector import analyze_code as detect_errors  # rename import
from backend.ai_suggester import AISuggester

def analyze_code_local(code: str) -> dict:
    """
    Analyze user code: parse, detect errors, suggest fixes, and calculate score.
    """

    # ---------------------------
    # STEP 0: EMPTY INPUT CHECK
    # ---------------------------
    if not code.strip():
        return {
            "errors": ["No code provided"],
            "suggestion": "Please paste some code to analyze.",
            "score": 0,
        }

    # ---------------------------
    # STEP 1: PARSE CODE
    # ---------------------------
    parser = CodeParser(code)
    parsed_code = parser.analyze()

    # If parser returned an error
    if isinstance(parsed_code, dict) and "error" in parsed_code:
        return {
            "errors": [f"Syntax Error: {parsed_code['error']}"],
            "suggestion": "Fix syntax errors before analysis.",
            "score": 0,
        }

    # ---------------------------
    # STEP 2: DETECT ERRORS
    # ---------------------------
    try:
        errors = detect_errors(code)  # ✅ use the renamed import
    except Exception:
        errors = ["Error detection failed"]

    # ---------------------------
    # STEP 3: GENERATE SUGGESTION
    # ---------------------------
    try:
        suggestion = AISuggester.suggest_fix(code, errors)
    except Exception:
        suggestion = "⚠️ Unable to generate suggestion."

    # ---------------------------
    # STEP 4: CALCULATE SCORE
    # ---------------------------
    # Simple scoring logic (can be upgraded later)
    score = max(0, 100 - len(errors) * 10)

    # ---------------------------
    # STEP 5: RETURN RESULT
    # ---------------------------
    return {
        "errors": errors,
        "suggestion": suggestion,
        "score": score,
    }
