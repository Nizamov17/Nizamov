from datetime import datetime
class Clock:
    @staticmethod
    def say_time():
        print(f"Сейчас {datetime.now().time()}")

Clock.say_time()
