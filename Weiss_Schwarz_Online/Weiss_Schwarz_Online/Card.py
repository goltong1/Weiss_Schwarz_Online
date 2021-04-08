class Card(object):
    def __init__(self,name,type,level,cost,color,trigger):
        self._name=name
        self._type=type
        self._cost=cost
        self._color=color
        self._trigger=trigger
        self._level=level
        

class Character(Card):
    def __init__(self,name,type,level,cost,color,trigger,power,soul,tab):
        self._power=power
        self._soul=soul
        self._tab=tab
        super().__init__(name,type,level,cost,color,trigger)

class Event(Card):
    def __init__(self,name,type,level,cost,color,trigger):
        super().__init__(name,type,level,cost,color,trigger)

class Climax(Card):
    def __init__(self,name,type,level,cost,color,trigger):
        super().__init__(name,type,level,cost,color,trigger)

