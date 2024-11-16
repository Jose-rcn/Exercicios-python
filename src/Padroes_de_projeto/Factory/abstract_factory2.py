from abc import ABC, abstractmethod

# Produtos abstratos
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

# Produtos concretos para o tema Dark
class DarkButton(Button):
    def render(self):
        return "Rendering dark button"

class DarkCheckbox(Checkbox):
    def render(self):
        return "Rendering dark checkbox"

# Produtos concretos para o tema Light
class LightButton(Button):
    def render(self):
        return "Rendering light button"

class LightCheckbox(Checkbox):
    def render(self):
        return "Rendering light checkbox"

# Abstract Factory
class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

# Concrete Factory para tema Dark
class DarkUIFactory(UIFactory):
    def create_button(self):
        return DarkButton()

    def create_checkbox(self):
        return DarkCheckbox()

# Concrete Factory para tema Light
class LightUIFactory(UIFactory):
    def create_button(self):
        return LightButton()

    def create_checkbox(self):
        return LightCheckbox()

# Uso da Abstract Factory
factory = DarkUIFactory()
button = factory.create_button()
checkbox = factory.create_checkbox()

print(button.render())    # Output: Rendering dark button
print(checkbox.render())  # Output: Rendering dark checkbox
