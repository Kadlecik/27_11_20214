"""1.	Abstraktná trieda View:
	•	Obsahuje:
	•	Atribúty: name (názov), position (pozícia ako tuple).
	•	Abstraktnu metódu move(new_position: tuple), ktorá nastaví novú pozíciu.

2.	Rozhranie Zobrazitelny:
	•	Obsahuje:
	•	Abstraktnu metódu show(), ktorá vypíše informácie o komponente.

3.	Triedy Button a TextLabel:
	•	Obe triedy dedia od View a implementujú Zobrazitelny.
	•	Implementácia:
	•	Button má navyše atribút label (text na tlačidle),
	    a funkciu ktoru spusta pod volanim metody click. # BONUS
	•	TextLabel má navyše atribút text (zobrazovaný text).
	•	Metóda show() vypíše konkrétne informácie o tlačidle alebo textovom štítku."""

from abc import ABC, abstractmethod

# 1. Abstraktní třída view
class View(ABC):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    @abstractmethod
    def move(self, new_position):
        pass

# 2. Rozhraní
class Zobrazitelny(ABC):
    @abstractmethod
    def show(self):
        pass

# 3. Tridy Button a TextLabel
class Button(View, Zobrazitelny):
    def __init__(self, name, position, label):
        super().__init__(name, position)
        self.label = label

    def move(self, new_position):
        self.position = new_position

    def show(self):
        print(f"Button: {self.name}, Position: {self.position}, Label: {self.label}")

    def click(self):
        print(f"Button '{self.label}' clicked!")

class TextLabel(View, Zobrazitelny):
    def __init__(self, name, position, text):
        super().__init__(name, position)
        self.text = text

    def move(self, new_position):
        self.position = new_position

    def show(self):
        print(f"TextLabel: {self.name}, Position: {self.position}, Text: {self.text}")

# Příklad použití:
button = Button("SubmitButton", (10, 20), "Submit")
text_label = TextLabel("GreetingLabel", (5, 10), "Hello, World!")

button.show()
button.move((15, 25))
button.show()
button.click()

text_label.show()
text_label.move((10, 15))
text_label.show()