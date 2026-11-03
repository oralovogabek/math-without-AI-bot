import ast
import operator
from aiogram import Router, F
from aiogram.types import Message

router = Router()
OPS = {
    ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
    ast.Div: operator.truediv, ast.Pow: operator.pow, ast.Mod: operator.mod,
    ast.USub: operator.neg, ast.UAdd: operator.pos,
}

def safe_calculate(expression):
    if len(expression) > 80:
        raise ValueError("Ifoda juda uzun.")
    tree = ast.parse(expression, mode="eval")
    def calc(node):
        if isinstance(node, ast.Expression):
            return calc(node.body)
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in OPS:
            left, right = calc(node.left), calc(node.right)
            if isinstance(node.op, ast.Pow) and abs(right) > 10:
                raise ValueError("Daraja 10 dan oshmasin.")
            value = OPS[type(node.op)](left, right)
            if abs(value) > 10**15:
                raise ValueError("Natija juda katta.")
            return value
        if isinstance(node, ast.UnaryOp) and type(node.op) in OPS:
            return OPS[type(node.op)](calc(node.operand))
        raise ValueError("Faqat sonlar va + - * / ** % amallaridan foydalaning.")
    result = calc(tree)
    if isinstance(result, float) and result.is_integer():
        return int(result)
    return result

@router.message(F.text == "➗ Kalkulyator")
async def calculator_help(message: Message):
    await message.answer("➗ Ifodani yuboring. Masalan: 12*(5+3) yoki 2**5\nBekor qilish uchun /cancel.")

@router.message(F.text.startswith("/cancel"))
async def cancel(message: Message):
    await message.answer("Amal bekor qilindi.")

@router.message(F.text.regexp(r"^[0-9\s+\-*/().%]+$"))
async def calculate(message: Message):
    try:
        await message.answer(f"🧮 Natija: <b>{safe_calculate(message.text)}</b>", parse_mode="HTML")
    except ZeroDivisionError:
        await message.answer("❌ Nolga bo'lish mumkin emas.")
    except Exception as e:
        await message.answer(f"❌ Ifodani hisoblab bo'lmadi: {e}")
