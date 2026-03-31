import ast
import builtins
from typing import List, Dict, Any


class ErrorDetector(ast.NodeVisitor):
    def __init__(self):
        self.defined_vars = set()
        self.used_vars = set()
        self.imports = {}
        self.used_imports = set()
        self.issues = []
        self.builtin_names = set(dir(builtins))

    # -----------------------------
    # IMPORTS
    # -----------------------------
    def visit_Import(self, node):
        for alias in node.names:
            name = alias.asname if alias.asname else alias.name
            self.imports[name] = node.lineno
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            name = alias.asname if alias.asname else alias.name
            self.imports[name] = node.lineno
        self.generic_visit(node)

    # -----------------------------
    # VARIABLE DEFINITIONS
    # -----------------------------
    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.defined_vars.add(target.id)

                # Check redefined builtins
                if target.id in self.builtin_names:
                    self.issues.append({
                        "type": "redefined_builtin",
                        "message": f"Redefining built-in '{target.id}'",
                        "line": node.lineno
                    })

        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.defined_vars.add(node.name)

        # function args are also defined
        for arg in node.args.args:
            self.defined_vars.add(arg.arg)

        self.generic_visit(node)

    def visit_ClassDef(self, node):
        self.defined_vars.add(node.name)
        self.generic_visit(node)

    # -----------------------------
    # VARIABLE USAGE
    # -----------------------------
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.used_vars.add(node.id)

            # Check undefined variable
            if (
                node.id not in self.defined_vars and
                node.id not in self.imports and
                node.id not in self.builtin_names
            ):
                self.issues.append({
                    "type": "undefined_variable",
                    "message": f"Undefined variable '{node.id}'",
                    "line": node.lineno
                })

        elif isinstance(node.ctx, ast.Store):
            self.defined_vars.add(node.id)

        self.generic_visit(node)

    # -----------------------------
    # IMPORT USAGE
    # -----------------------------
    def visit_Attribute(self, node):
        if isinstance(node.value, ast.Name):
            self.used_imports.add(node.value.id)
        self.generic_visit(node)

    # -----------------------------
    # FINAL ANALYSIS
    # -----------------------------
    def report(self) -> List[Dict[str, Any]]:
        # Unused variables
        for var in self.defined_vars:
            if var not in self.used_vars and var not in self.imports:
                self.issues.append({
                    "type": "unused_variable",
                    "message": f"Variable '{var}' is defined but never used",
                    "line": None
                })

        # Unused imports
        for imp, line in self.imports.items():
            if imp not in self.used_imports:
                self.issues.append({
                    "type": "unused_import",
                    "message": f"Import '{imp}' is not used",
                    "line": line
                })

        return self.issues


# -----------------------------
# MAIN FUNCTION
# -----------------------------
def analyze_code(code: str) -> List[Dict[str, Any]]:
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return [{
            "type": "syntax_error",
            "message": str(e),
            "line": e.lineno
        }]

    detector = ErrorDetector()
    detector.visit(tree)
    return detector.report()