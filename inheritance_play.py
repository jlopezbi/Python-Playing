# Inheritance model with hooks
class Plant(object):

    def __init__(self,**kwargs):
        self.food = kwargs.get('food','sunlight')
        self.post_initialize(kwargs)

    def post_initialize(self,kwargs):
        pass

    def local_explain(self):
        pass

    def explain(self):
        print "I eat {}.".format(self.food),
        self.local_explain()

class Tree(Plant):

    def post_initialize(self,kwargs):
        self.branching_levels = kwargs['branching_levels']

    def local_explain(self):
        print  "I have {} branching_levels".format(self.branching_levels)

class Fern(Plant):

    def post_initialize(self,kwargs):
        self.frond_number = kwargs['frond_number']

    def local_explain(self):
        print "I have {} fronds".format(self.frond_number)

