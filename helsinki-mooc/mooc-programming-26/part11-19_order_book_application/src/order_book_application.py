# Write your solution here
# If you use the classes made in the previous exercise, copy them here
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



def main():
    orders = OrderBook()

    print("commands:")
    print("0 exit")
    print("1 add order")
    print("2 list finished tasks")
    print("3 list unfinished tasks")
    print("4 mark task as finished")
    print("5 programmers")
    print("6 status of programmer")
    
    while True:  
        print()      
        command = input("command: ")
        
        #exit
        if command == "0":
            break
        
        try:       
            if command == "1":
                description = input("description: ")
                prog_and_work = input("programmer and workload estimate: ") 
                parts = prog_and_work.split()
                
                if len(parts) != 2:
                    raise ValueError
                
                programmer = parts[0]
                workload = int(parts[1])
                
                orders.add_order(description, programmer, workload)
                print("added!")
                
            elif command == "2":
                finished = orders.finished_orders()
                if not finished:
                    print("no finished tasks")
                else:
                    for task in finished:
                        print(task)
            
            elif command == "3":
                unfinished = orders.unfinished_orders()
                if not unfinished:
                    print("no unfinished tasks")
                else:
                    for task in unfinished:
                        print(task)
                
            elif command == "4":
                id = input("id: ")
                orders.mark_finished(int(id))
                print("marked as finished")
                
            elif command == "5":
                for programmer in orders.programmers():
                    print(programmer)
                
            elif command == "6":
                programmer = input("programmer: ")
                summary = orders.status_of_programmer(programmer)
                print(f"tasks: finished {summary[0]} not finished {summary[1]}, hours: done {summary[2]} scheduled {summary[3]}")
            
            else:
                print("erroneous input")
        except:
            print("erroneous input")


main()