class Soda:
    def __init__(self, taste=None):
        self.taste = taste

    def __repr__(self) -> str:
        if self.taste == None:
            return "У вас обычная газировка"
        else:
            return f"У вас газировка с {self.taste} вкусом"

soda1 = Soda()
print(soda1)

soda2 = Soda("клубничный")
print(soda2)