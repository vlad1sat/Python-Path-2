class MyStack:

    def __init__(self, *args):
        self.__stack = list(args)

    def push(self, element):
        self.__stack.append(element)

    def pop_stack(self):
        if len(self.__stack) == 0:
            return None
        return self.__stack.pop()

    def clean(self):
        self.__stack = list()

    @property
    def show(self):
        return self.__stack


class TaskManager:

    def __init__(self):
        self.__task_stack = MyStack()

    def new_task(self, name_task: str, priority: int):
        for index, object_stack in enumerate(self.__task_stack.show):
            if object_stack[0] == priority:
                self.__task_stack.show[index][1].append(name_task)
                self.__stack_priority()
                return
        self.__task_stack.push([priority, [name_task]])
        self.__stack_priority()

    def __stack_priority(self):
        self.__task_stack.show.sort(key=lambda x: x[0])

    def __str__(self):
        result = ''
        for object_stack in self.__task_stack.show:
            tasks = None
            for task in object_stack[1]:
                if tasks is None:
                    tasks = ''. join([': ', task])
                    continue
                tasks = '; '.join([tasks, task])
            result = ''.join([result, str(object_stack[0]), tasks, '\n'])
        return result


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
