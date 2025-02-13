#class User:

	#def __init__(self, name):
		#print("я создался")
		#print("меня зовут ", name) #добавили запрос

#user1 = User("Alex")
#user2 = User("Mark")
#user3 = User("Marta")



#class User:
#	age = 0

	#def __init__(self, name):
#		print("я создался")
#		self.username = name

#	def sayName(self):
#		print("меня зовут ", self.username)

#	def sayAge(self):
#		print(self.age)

#	def setAge(self, newAge):
#		self.age = newAge

#alex = User("Alex")
#mark = User("Mark")
#marta = User("Marta")

#alex.sayName()
#alex.sayAge() #в скрипте уже был запрос на выведение возраста
#alex.setAge(33) #создали запрос на изменение возраста
#alex.sayAge() #создали запрос на проверку изменения возраста

from user3 import User
from card3 import Card

alex = User("Alex")

alex.sayName()
alex.setAge(33)
alex.sayAge()

card = Card("1234 5678 8765 4321", "03/28", "Alex F")
alex.addCard(card)
alex.getCard().pay(1000) #пользователь оплачивает карточкой из своего класса