class Tomato:
    states = {0: 'зелёный', 1: "жёлтый", 3: "красный"}

    def __init__(self, index):
        self.index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1
        print(f'Tomato {self.index} is {Tomato.states[self._state]}')

    def is_ripe(self):
        if self._state == 3:
            print("Помидор полностью созрел")
        else:
            print("Помидор ещё не созрел")

class TomatoBush:
    def __init__(self, kolvo):
        self.tomatoes = [Tomato(index) for index in range(0, kolvo)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()
        print("Садовник вырывает сорняки...\n"
              "Cадовник поливает помидоы...\n")

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран")
        else:
            print("К сожалению необходимо ещё подожать. Помидры ещё не созрели")
    @staticmethod
    def knowledge_base():
        print("Уход за томатами в теплице заключается в поддержании оптимального режима температуры и влажности,\n"
              "регулярных поливах теплой водой и формировании кустов. При нашествии вредителей или появлении болезней,\n"
              "проводят профилактические мероприятия и принимают меры по борьбе.\n"
              "Тепличные помидоры лучше всего растут при температуре воздух днем от +20°C до +25°C, ночью — +16-18°C.\n"
              "Оптимальная температура почвы в теплице от +17°C до +22°C. Относительная влажность воздуха в пределах 70%,\n "
              "а влажность почвы — 60-70%. Повышение влажности воздуха, вкупе с низкой температурой в теплице,\n"
              "грозит томатам заболеванием серой гнилью, бурой пятнистостью и фитофторозом. Гниль не дремлет.\n"
              "Помидоры страдают от гнили, если не проветривать теплицу. \n"
              "Томаты любят свежий воздух, поэтому теплицу, где растут помидоры надо регулярно проветривать, особенно во время массового цветения.\n"
              "Проветривание предупреждает гниль и улучшает оплодотворение цветков.\n"
              "После каждого полива, после просыхания почвы, землю рыхлят, устраняя почвенную корку.\n"
              "Рыхление замедляет испарение влаги из почвы и обеспечивает активное поступление воздуха к корням, лучший газообмен.")


if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(3)
    gardener = Gardener('Григорий', great_tomato_bush)
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()