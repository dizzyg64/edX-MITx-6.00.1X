# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 20:16:41 2016

@author: RichardG
"""

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return 'It is obvious that ' + self.say(stuff)



#Problem 6-1
'''
e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')

>>> e.say('the sky is blue')
eric says: the sky is blue

>>> le.say('the sky is blue')
eric says: the sky is blue

>>> le.lecture('the sky is blue')
I believe that eric says: the sky is blue

>>> pe.say('the sky is blue')
eric says: I believe that eric says: the sky is blue

>>> pe.lecture('the sky is blue')
I believe that eric says: the sky is blue

>>> ae.say('the sky is blue')
eric says: It is obvious that eric says: the sky is blue

>>> ae.lecture('the sky is blue')
It is obvious that eric says: the sky is blue

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: '+'It is obvious that ' + Person.say(self,stuff)
    def lecture(self,stuff):
        return 'It is obvious that ' + Person.say(self,stuff)
'''
#Problem 6-2
'''
>>> ae.say('the sky is blue')
eric says: It is obvious that I believe that eric says: the sky is blue

>>> ae.lecture('the sky is blue')
It is obvious that I believe that eric says: the sky is blue

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: '+'It is obvious that ' + Lecturer.lecture(self,stuff)
    def lecture(self,stuff):
        return 'It is obvious that ' + Lecturer.lecture(self,stuff)
'''

#Problem 6-3
'''
>>> pe.say('the sky is blue')
Prof. eric says: I believe that eric says: the sky is blue 

>>> ae.say('the sky is blue')
Prof. eric says: It is obvious that I believe that eric says: the sky is blue

class Professor(Lecturer):
    def say(self, stuff):
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)
'''