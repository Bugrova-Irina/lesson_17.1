from pyexpat.errors import messages

from src.task import Task
from src.periodic_task import PeriodicTask
from src.dedline_task import DeadlineTask


def test_print_mixin(capsys):
    Task("Купить огурцы", "Купить огурцы для салата", created_at="20.04.2024")
    message = capsys.readouterr()
    assert message.out.strip() == "Task(Купить огурцы, Купить огурцы для салата, Ожидает старта, 20.04.2024)"

    PeriodicTask("Купить огурцы", "Купить огурцы для салата", "01.04.2024", "01.01.2024", created_at="20.04.2024", run_time=60)
    message = capsys.readouterr()
    assert message.out.strip() == "PeriodicTask(Купить огурцы, Купить огурцы для салата, Ожидает старта, 20.04.2024)"

    DeadlineTask("Купить перец", "Купить перец для салата", "20.04.2024", created_at="20.04.2024", run_time=60)
    message = capsys.readouterr()
    assert message.out.strip() == "DeadlineTask(Купить перец, Купить перец для салата, Ожидает старта, 20.04.2024)"
