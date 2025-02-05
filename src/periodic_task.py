from task import Task

class PeriodicTask(Task):
    def __init__(self, name, description, start_date, end_date, status='Ожидает старта', created_at=None, run_time=0, frequency="Ежедневная"):
        super().__init__(name, description, status, created_at, run_time)
        self.start_date = start_date
        self.end_date = end_date
        self.frequency = frequency

    def __add__(self, other):
        if type(other) is PeriodicTask:
            return self.run_time + other.run_time
        raise TypeError


if __name__ == "__main__":
    periodic_task = PeriodicTask("Купить огурцы", "Купить огурцы для салата", "01.04.2024", "01.01.2024", run_time=60)
    print(periodic_task.name)
    print(periodic_task.description)
    print(periodic_task.status)
    print(periodic_task.created_at)

    print(periodic_task.start_date)
    print(periodic_task.end_date)
    print(periodic_task.frequency)

    task = Task("Купить огурцы", "Купить огурцы для салата", run_time=60)
    periodic_task2 = PeriodicTask("Купить огурцы", "Купить огурцы для салата", "01.04.2024", "01.01.2024", run_time=60)

    periodic_task + periodic_task2