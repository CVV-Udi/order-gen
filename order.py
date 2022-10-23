class Order:
    def __init__(self, value: dict, categories: dict, name_index: int):
        self.value = value
        self.categories = categories
        self.name = list(value.values())[name_index]

    def getCategory(self, name: str):
        indexes = self.categories[name]
        values = list(self.value.values())
        keys = list(self.value.keys())
        return [dict(qnt=values[int(index)] if values[int(index)] != '' else 0, name=keys[int(index)]) for index in indexes]
