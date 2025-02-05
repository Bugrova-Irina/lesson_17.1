from task import Task
from exceptions import ZeroRunTimeTask


class User:
    username: str
    email: str
    first_name: str
    last_name: str
    task_list: list
    users_count = 0
    all_tasks_count = 0

    def __init__(self, username, email, first_name, last_name, task_list=None):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.__task_list = task_list if task_list else []
        User.users_count += 1
        User.all_tasks_count += len(task_list) if task_list else 0

    def __str__(self):
        return f'{self.last_name} {self.first_name}, Email: {self.email}, Всего задач в списке: {len(self.__task_list)}'


    @property
    def task_list(self):
        task_str = ""
        for task in self.__task_list:
            task_str += f"{str(task)}\n"
        return task_str

    @task_list.setter
    def task_list(self, task: Task):
        if isinstance(task, Task):
        # if type(task).__name__ == "Task": # проверяем, принадлежит ли задача классу Task
            try:
                if task.run_time == 0:
                    raise ZeroRunTimeTask("Нельзя задать задачу с нулевым временем выполнения")
            except ZeroRunTimeTask as e:
                print(str(e))
            else:
                self.__task_list.append(task)
                User.all_tasks_count += 1
                print("Задача добавлена успешно")
            finally:
                print("Обработка добавления задачи завершена")
        else:
            raise TypeError

    @property
    def task_in_list(self):
        return self.__task_list

    def middle_task_run_time(self):
        try:
            return sum([task.run_time for task in self.__task_list]) / len(self.__task_list)
        except ZeroDivisionError:
            return 0


if __name__ == "__main__":
    task1 = Task("Купить огурцы", "Купить огурцы для салата", run_time=20)
    task2 = Task("Купить помидоры", "Купить помидоры для салата", run_time=20)
    task3 = Task("Купить лук", "Купить лук для салата", run_time=20)
    task4 = Task("Купить перец", "Купить перец для салата", run_time=20)

    user = User('User', 'user@mail.ru', 'User', 'Userov', [task1, task2, task3, task4])
    print(user.username)
    print(user.email)
    print(user.first_name)
    print(user.last_name)
    print(user.task_list)

    print(user.users_count)
    print(user.all_tasks_count)

    # task5 = Task("Купить огурцы", "Купить огурцы для салата")
    # user.task_list = task5

    print(user.task_list)
    print(user.all_tasks_count)

    print(user)

    print(user.middle_task_run_time())

    user1 = User('User', 'user@mail.ru', 'User', 'Userov', [])

    print(user1.middle_task_run_time())

    task5 = Task("Купить огурцы", "Купить огурцы для салата", run_time=60)
    user.task_list = task5
