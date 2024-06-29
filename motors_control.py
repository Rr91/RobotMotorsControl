
class Robot:
    
    def __init__(self, name):
    	self.name = name
    	
    def move_front(self):
    	print(f'я {self.name} двигаюсь вперед')
    	
    def move_back(self):
    	print(f'я {self.name} двигаюсь назад')

rob1 = Robot('Вася')
rob1.move_front()
rob1.move_back()

    	
