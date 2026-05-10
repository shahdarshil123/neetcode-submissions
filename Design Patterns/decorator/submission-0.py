class Coffee(ABC):
    @abstractmethod
    def getCost(self):
        pass

class SimpleCoffee(Coffee):
    def getCost(self):
        return 1.1

class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee

    def getCost(self):
        return self.coffee.getCost()

class MilkDecorator(CoffeeDecorator):
    # Implement the Milk decorator
    def __init__(self, coffee):
        super().__init__(coffee)
    
    def getCost(self) -> float:
        return super().getCost() + 0.5

class SugarDecorator(CoffeeDecorator):
    # Implement the Sugar decorator
    def __init__(self, coffee):
        super().__init__(coffee)
    
    def getCost(self) -> float:
        return super().getCost() + 0.2

class CreamDecorator(CoffeeDecorator):
    # Implement the Cream decorator
    def __init__(self, coffee):
        super().__init__(coffee)
    
    def getCost(self) -> float:
        return super().getCost() + 0.7