##Lee Kamar
##01/5/2020
##Use statistics modules to calculate mean,median,mode of different persons and their respective ages
import statistics


class Person:
    "initializes class of persons with name and age"
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def get_age(self):
        "gets age"
        return self.__age


def basic_stats(people):
    "calculates mean,median and mode of ages"
    ages=[]
    for person in people:
        ages.append(person.get_age())

        meanz= statistics.mean(ages)                                #mean using stat module
        medianz= statistics.median(ages)                            #median using stat module
        modez= statistics.mode(ages)                                #mode using stat module
    return(meanz,medianz,modez)




