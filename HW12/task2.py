class Beelefant:
    def __init__(self, part_B, part_E) -> None:
        self.part_B = part_B
        self.part_E = part_E

    def fly(self) -> bool:
        return True if self.part_B > self.part_E else False
    
    def trumpet(self) -> str:
        return "wzzzz" if self.part_B > self.part_E else "tu-tu-doo-doo"
    
    def eat(self, meal, value) -> None:
        if meal == "nectar":
            self.part_B += value
            if self.part_B > 100:
                self.part_B = 100

            self.part_E -= value
            if self.part_E < 0:
                self.part_E = 0

        elif meal == "grass":
            self.part_B -= value
            if self.part_B < 0:
                self.part_B = 0

            self.part_E += value
            if self.part_E > 100:
                self.part_E = 100

beelephant = Beelefant(46, 78)

print(f"Can fly: {beelephant.fly()}")
print(f"Sound: {beelephant.trumpet()}")
print()

beelephant.eat("nectar", 20)

print(f"Can fly: {beelephant.fly()}")
print(f"Sound: {beelephant.trumpet()}")
print()
        