from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Term:
    coeff: int
    exponents: dict[str,int]  # ej: {'x':2, 'y':1}

    def __repr__(self) -> str:
        parts = []
        for v,e in sorted(self.exponents.items()):
            if e == 0: continue
            parts.append(f"{v}^{e}" if e!=1 else v)
        vars_part = "*".join(parts)
        return f"{self.coeff}*{vars_part}" if vars_part else str(self.coeff)
