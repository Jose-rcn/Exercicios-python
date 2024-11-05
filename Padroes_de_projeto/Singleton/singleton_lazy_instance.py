class Singleton:
    __instance = None
    def __init__(self, value:int) -> None:
        self.value = value