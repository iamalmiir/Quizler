from src.classes.Quiz import QuizGame


class App(QuizGame):
    def __init__(self) -> None:
        super().__init__()

    def start(self) -> None:
        self.start_quiz()
