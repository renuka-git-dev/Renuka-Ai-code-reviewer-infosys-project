from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from typing import Dict, Any
import json
import re


class AISuggester:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("Groq API key is required")

        self.llm = ChatGroq(
            groq_api_key=api_key,
            model_name="llama-3.1-8b-instant",
            temperature=0.2
        )

        self.prompt = PromptTemplate(
            input_variables=["code"],
            template="""
You are a senior software engineer.

Analyze the following Python code and return a structured response.

Code:
{code}

Return strictly in JSON format with these keys:
- errors
- improvements
- time_complexity
- space_complexity
- pep8_issues

Only return JSON. No explanation.
"""
        )

        # ✅ Modern chain (no LLMChain)
        self.chain = self.prompt | self.llm

    def extract_json(self, text: str) -> str:
        """Extract JSON block safely from LLM response"""
        match = re.search(r"\{.*\}", text, re.DOTALL)
        return match.group(0) if match else "{}"

    def analyze(self, code: str) -> Dict[str, Any]:
        try:
            response = self.chain.invoke({"code": code})

            # LangChain returns object → convert to string
            text = response.content if hasattr(response, "content") else str(response)

            json_text = self.extract_json(text)

            return json.loads(json_text)

        except Exception as e:
            return {
                "error": "LLM processing failed",
                "details": str(e)
            }
        # Add at the end of ai_suggester.py
def suggest_fix(code: str, errors=None, api_key: str = "YOUR_GROQ_API_KEY") -> dict:
    """
    Wrapper for backward compatibility. Uses AISuggester internally.
    """
    suggester = AISuggester(api_key=api_key)
    return suggester.analyze(code)