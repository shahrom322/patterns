from src.strategy.duck import MallardDuck, RedHeadDuck, RubberDuck
from src.strategy.fly import FlyRocketPowered
from src.strategy.quack import MuteQuack


def start_stategy():
    ducks_types = (
        MallardDuck, RedHeadDuck, RubberDuck
    )
    for duck_type in ducks_types:
        duck = duck_type()
        duck.display()
        duck.perform_fly()
        duck.perform_quack()

        # Меняем поведение утки
        duck.fly_behavior = FlyRocketPowered()
        duck.quack_behavior = MuteQuack()
        duck.perform_fly()
        duck.perform_quack()

        print('-' * 20)


if __name__ == "__main__":
    start_stategy()
