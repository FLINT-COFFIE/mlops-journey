# Write your solution here:
class Task:
    id = 1
    def __init__(self, description: str, programmer: str, hours : int):
        self.description = description
        self.programmer = programmer
        self.workload = hours
        self.id = Task.id
        Task.id += 1
        self.finished = False
        
    def mark_finished(self):
        self.finished = True
        
    def is_finished(self):
        return self.finished
    
    def __str__(self):
        state = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {state}"
    
class OrderBook:
    def __init__(self):
        self.orders = []
        
    def add_order(self, description: str, programmer: str, workload : int):
        task = Task(description, programmer, workload)
        self.orders.append(task)
        
    def all_orders(self):
        return self.orders
    
    def programmers(self):
        return list(set([task.programmer for task in self.orders]))
        
    def mark_finished(self, id: int):
        for task in self.orders:
            if task.id == id:
                task.mark_finished()
                return
        raise ValueError
    
    def finished_orders(self):
        return [task for task in self.orders if task.is_finished()]
        
    def unfinished_orders(self):
        return [task for task in self.orders if not task.is_finished()]
                
    def status_of_programmer(self, programmer: str):
        all_tasks = [task for task in self.orders if task.programmer == programmer]
        
        if len(all_tasks) == 0:
            raise ValueError
            
        finished_tasks = [task for task in all_tasks if task.is_finished()]
        unfinished_tasks = [task for task in all_tasks if not task.is_finished()]
        
        finished_hours = sum([task.workload for task in finished_tasks])
        unfinished_hours = sum([task.workload for task in unfinished_tasks])
        
        return (len(finished_tasks), len(unfinished_tasks), finished_hours, unfinished_hours)