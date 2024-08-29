class SuperStr(str):
    def is_repeatance(self, s) -> bool:
        if len(self) % len(s) != 0:
            return False
        elif self.count(s) == len(self) // len(s):
            return True
        else:
            return False

    def is_palindrom(self) -> bool:
        if len(self) == 0 or len(self) == 1:
            return True
        count = len(self) // 2 + 1
        for i in range(0, count):
            if self[i] != self[-1 - i]:
                return False
        return True
    
ss1 = SuperStr("блаблабла")
ss2 = SuperStr("топот")

print("Палиндром?")
print(ss1.is_palindrom())
print(ss2.is_palindrom())

print("Повторения?")
print(ss1.is_repeatance("бла"))
print(ss2.is_repeatance("бла"))
