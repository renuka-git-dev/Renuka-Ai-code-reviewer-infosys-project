import ast
from typing import Dict, List, Any


class CodeParser:
    def __init__(self, code: str):
        self.code = code
        self.tree = None

    def parse(self) -> None:
        """Parse code into AST"""
        try:
            self.tree = ast.parse(self.code)
        except SyntaxError as e:
            raise ValueError(f"Syntax Error: {e}")

    def get_imports(self) -> List[str]:
        """Extract import statements"""
        imports = []

        for node in ast.walk(self.tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)

            elif isinstance(node, ast.ImportFrom):
                module = node.module if node.module else ""
                for alias in node.names:
                    imports.append(f"{module}.{alias.name}")

        return imports

    def get_functions(self) -> List[Dict[str, Any]]:
        """Extract function names and arguments"""
        functions = []

        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                func_name = node.name
                args = [arg.arg for arg in node.args.args]

                functions.append({
                    "name": func_name,
                    "args": args,
                    "lineno": node.lineno
                })

        return functions

    def get_variables(self) -> List[str]:
        """Extract variable names"""
        variables = set()

        for node in ast.walk(self.tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        variables.add(target.id)

            elif isinstance(node, ast.AnnAssign):
                if isinstance(node.target, ast.Name):
                    variables.add(node.target.id)

        return list(variables)

    def analyze(self) -> Dict[str, Any]:
        """Run full analysis"""
        if self.tree is None:
            self.parse()

        return {
            "imports": self.get_imports(),
            "functions": self.get_functions(),
            "variables": self.get_variables(),
        }
