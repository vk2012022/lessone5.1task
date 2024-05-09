#Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты:
#описание задачи, срок выполнения и статус (выполнено/не выполнено).
#Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.
class Task:
    def __init__(self):
        self.tasks = []  # Уникальный список задач для каждого экземпляра

    def add_task(self, description, due_date, completed=False):
        self.tasks.append({'description': description, 'due_date': due_date, 'completed': completed})

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['completed'] = True
                #print(f"Задача '{description}' помечена как завершенная.")
                return f"Задача '{description}' помечена как завершенная."
        #print(f"Задача '{description}' не найдена.")
        return f"Задача '{description}' не найдена."


    # вариант 1
    def list_current_tasks(self):
        if not self.tasks:
            return "Нет текущих задач."

        current_tasks = ""
        for task in self.tasks:
            if not task['completed']:
                if current_tasks:  # Если строка уже содержит задачи, добавляем перенос строки перед добавлением следующей задачи
                    current_tasks += "\n"
                current_tasks += f"{task['description']} ({task['due_date']}) - {'Завершена' if task['completed'] else 'Не завершена'}"
        return current_tasks
    # вариант 2
    # def list_current_tasks(self):
    #    current_tasks = [f"{task['description']} ({task['due_date']}) - {'Завершена' if task['completed'] else 'Не завершена'}"
    #                     for task in self.tasks if not task['completed']]
    #    return "\n".join(current_tasks) if current_tasks else "Нет текущих задач."

    def list_completed_tasks(self):
        current_tasks = [f"{task['description']} ({task['due_date']}) - {'Завершена' if task['completed'] else 'Не завершена'}"
                         for task in self.tasks if task['completed']]
        return "\n".join(current_tasks) if current_tasks else "Нет завершенных задач."

# Пример использования:
task_manager1 = Task()
task_manager2 = Task()

task_manager1.add_task("ЗАДАЧА1.1", "2024-05-10")
task_manager1.add_task("ЗАДАЧА1.2", "2024-05-07")
task_manager1.add_task("ЗАДАЧА1.3", "2024-05-05")
task_manager1.add_task("ЗАДАЧА1.4", "2024-05-01")

task_manager2.add_task("ЗАДАЧА2.1", "2024-06-01")
task_manager2.add_task("ЗАДАЧА2.2", "2024-06-03")

print("Текущие задачи для manager 1:")
print(task_manager1.list_current_tasks())
print(task_manager1.mark_task_completed("ЗАДАЧА1.1"))
print("Текущие задачи для manager 1:")
print(task_manager1.list_current_tasks())
print(task_manager1.mark_task_completed("ЗАДАЧА1.2"))
print("Текущие задачи для manager 1:")
print(task_manager1.list_current_tasks())
print("Завершенные задачи для manager 1:")
print(task_manager1.list_completed_tasks())

print("Текущие задачи для manager 2:")
print(task_manager2.list_current_tasks())
print("Завершенные задачи для manager 2:")
print(task_manager2.list_completed_tasks())
print(task_manager1.mark_task_completed("ЗАДАЧА1.5"))
