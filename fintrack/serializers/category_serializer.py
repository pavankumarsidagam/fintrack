class CategorySerializer:
    def __init__(self, category):
        self.category = category

    def data(self):
        return {
            "id": str(self.category.id),
            "name": self.category.name,
            "type": self.category.type,
            "iconLib": self.category.iconLib,
            "iconName": self.category.iconName,
            "colorClass": self.category.colorClass,
        }
