import re
from typing import List, Optional
from expander.logic.ast.nodes import Node, Const, Frac, Var, Add, Mul, Pow

class Token:
    def __init__(self, type:str, value:str):
        self.type = type; self.value = value
    def __repr__(self): return f"Token({self.type!r},{self.value!r})"

_TOKEN = re.compile(r"\s*(?:(\d+)|([A-Za-z]+)|(\^|\*|\+|\-|\(|\)|/))")

class Parser:
    def __init__(self, text:str):
        self.tokens = self._tokenize(text)
        self.pos = 0

    def _tokenize(self, text:str)->List[Token]:
        toks:List[Token] = []
        for num,var,op in _TOKEN.findall(text):
            if num: toks.append(Token("INT",num))
            elif var: toks.append(Token("VAR",var))
            else: toks.append(Token(op,op))
        return toks

    def _peek(self)->Optional[Token]:
        return self.tokens[self.pos] if self.pos<len(self.tokens) else None

    def _next(self)->Token:
        tok = self._peek()
        if tok is None:
            raise SyntaxError("EOF inesperado")
        self.pos+=1
        return tok

    def parse(self)->Node:
        node = self._expr()
        if self._peek() is not None:
            raise SyntaxError(f"Token extra {self._peek()}")
        return node

    def _expr(self)->Node:
        node = self._term()
        while (tok:=self._peek()) and tok.type in ("+","-"):
            op = self._next()
            right = self._term()
            if op.type=="+":
                node = Add(node, right)
            else:
                node = Add(node, Mul(Const(-1), right))
        return node

    def _term(self)->Node:
        node = self._factor()
        while (tok:=self._peek()) and tok.type=="*":
            self._next()
            node = Mul(node, self._factor())
        return node

    def _factor(self)->Node:
        node = self._base()
        if (tok:=self._peek()) and tok.type=="^":
            self._next()
            exp = self._next()
            if exp.type!="INT":
                raise SyntaxError("Se esperaba entero como exponente")
            node = Pow(node, int(exp.value))
        return node

    def _base(self)->Node:
        tok = self._peek()
        if not tok:
            raise SyntaxError("EOF en base")
        if tok.type=="INT":
            self._next()
            num_value = int(tok.value)
            
            # Verificar si hay una fracción (siguiente token es "/")
            if (next_tok := self._peek()) and next_tok.type == "/":
                self._next()  # consumir "/"
                denom_tok = self._peek()
                if not denom_tok or denom_tok.type != "INT":
                    raise SyntaxError("Se esperaba entero como denominador")
                self._next()  # consumir denominador
                return Frac(num_value, int(denom_tok.value))
            else:
                return Const(num_value)
                
        if tok.type=="VAR":
            self._next()
            var_node = Var(tok.value)
            
            # Verificar si hay una fracción después de la variable (x/2)
            if (next_tok := self._peek()) and next_tok.type == "/":
                self._next()  # consumir "/"
                denom_tok = self._peek()
                if not denom_tok or denom_tok.type != "INT":
                    raise SyntaxError("Se esperaba entero como denominador")
                self._next()  # consumir denominador
                # Crear (1/denominador) * variable
                frac_node = Frac(1, int(denom_tok.value))
                return Mul(frac_node, var_node)
            else:
                return var_node
                
        if tok.type=="(":
            self._next()
            n = self._expr()
            if not self._peek() or self._peek().type!=")":
                raise SyntaxError("Falta ')' ")
            self._next()
            return n
        raise SyntaxError(f"Token inesperado {tok}")
        if tok.type=="(":
            self._next()
            n = self._expr()
            if not self._peek() or self._peek().type!=")":
                raise SyntaxError("Falta ')' ")
            self._next()
            return n
        raise SyntaxError(f"Token inesperado {tok}")

def parse(text:str)->Node:
    return Parser(text).parse()
