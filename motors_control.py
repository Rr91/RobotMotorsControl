
class Robot:
    
    def __init__(self, name):
    	self.name = name
    	
    def move_front(self):
    	print(f'я {self.name} двигаюсь вперед')
    	
    def move_back(self):
    	print(f'я {self.name} двигаюсь назад')
    
    def turn_left(self):
        print(f'я {self.name} повернул налево')
    
    def turn_right(self):
        print(f'я {self.name} повернул направо')

rob1 = Robot('Вася')
rob1.move_front()
rob1.turn_left()
rob1.move_back()

    	
