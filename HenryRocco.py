class PizzaComponent:
    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost


class BasePizza(PizzaComponent):
    cost = 5.0


class IngredientDecorator(PizzaComponent):
    def __init__(self, pizzaComponent):
        self.component = pizzaComponent

    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)

    def getDescription(self):
        return self.component.getDescription() + ' ' + PizzaComponent.getDescription(self)


class Cheese(IngredientDecorator):
    cost = 2.0

    def __init__(self, pizzaComponent):
        super().__init__(pizzaComponent)


class Tomato(IngredientDecorator):
    cost = 1.5

    def __init__(self, pizzaComponent):
        super().__init__(pizzaComponent)


class Ham(IngredientDecorator):
    cost = 3.0

    def __init__(self, pizzaComponent):
        super().__init__(pizzaComponent)


class Olives(IngredientDecorator):
    cost = 1.0

    def __init__(self, pizzaComponent):
        super().__init__(pizzaComponent)


class Mushrooms(IngredientDecorator):
    cost = 1.75

    def __init__(self, pizzaComponent):
        super().__init__(pizzaComponent)


# Criação de Pizzas com diferentes ingredientes
margherita = Cheese(Tomato(BasePizza()))
print(margherita.getDescription() + ": $" + str(margherita.getTotalCost()))

ham_and_cheese = Ham(Cheese(BasePizza()))
print(ham_and_cheese.getDescription() + ": $" + str(ham_and_cheese.getTotalCost()))

deluxe = Mushrooms(Olives(Ham(Cheese(Tomato(BasePizza())))))
print(deluxe.getDescription() + ": $" + str(deluxe.getTotalCost()))
