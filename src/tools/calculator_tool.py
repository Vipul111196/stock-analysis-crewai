import ast
import operator
from crewai.tools import BaseTool


# Supported operators for safe math evaluation
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


def _safe_eval(node: ast.AST) -> float:
    """Recursively evaluate an AST node using only arithmetic operators."""
    if isinstance(node, ast.Expression):
        return _safe_eval(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
        left = _safe_eval(node.left)
        right = _safe_eval(node.right)
        return OPERATORS[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp) and type(node.op) in OPERATORS:
        return OPERATORS[type(node.op)](_safe_eval(node.operand))
    raise ValueError(f"Unsupported expression: {ast.dump(node)}")


class CalculatorTool(BaseTool):
    name: str = "Calculator tool"
    description: str = (
        "Useful to perform any mathematical calculations, like sum, minus, "
        "multiplication, division, etc. The input should be a mathematical "
        "expression, e.g. '200*7' or '5000/2*10'."
    )

    def _run(self, operation: str) -> float:
        tree = ast.parse(operation, mode="eval")
        return _safe_eval(tree)
