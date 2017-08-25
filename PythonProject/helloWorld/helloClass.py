#! /usr/bin/python
#Filename: helloClass.py

class Person:
    population = []


    def __init__(self, name):
        """

        Initialize a person
        :param name: name of the person
        """

        self.name = name
        self.population.append(self)
        print  ' A new Person object is initialized with name \'' , self.name, '\''

    def SayHello(self):
        print "hello, I am ", self.name, ", how are you?"

    def __del__(self):
        """
        Delete a Person object
        :return:
        """
        print '%s says Bye.' %self.name
        # self.population.remove(self)
        if  len(self.population) == 0:
            print "I am the last one."
        else:
            print "After deleting ", self.name , ", there are ", len(self.population)-1, " person(s) left."

    def howMany(self):
        print "There are %d person(s) in total. "  %len(self.population)

p = Person("Bob")
p.SayHello()
p.howMany()

print len(p.population)

q = Person('Jack')
q.SayHello()
q.howMany()

print len(q.population)

p.SayHello()
p.howMany()

print p.population == q.population



