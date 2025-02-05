from task import Task
from user import User

class TaskIterator:
    def __init__(self, user_obj):
        self.user = user_obj
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.user.task_in_list):
            task = self.user.task_in_list[self.index]
            self.index += 1
            return task
        else:
            raise StopIteration


if __name__ == "__main__":
    task1 = Task("Купить огурцы", "Купить огурцы для салата")
    task2 = Task("Купить помидоры", "Купить помидоры для салата")
    task3 = Task("Купить лук", "Купить лук для салата")
    task4 = Task("Купить перец", "Купить перец для салата")

    user = User('User', 'user@mail.ru', 'User', 'Userov', [task1, task2, task3, task4])

    iterator = TaskIterator(user)
    
    for task in iterator:
        print(task)
    print()
    for task in iterator:
        print(task)