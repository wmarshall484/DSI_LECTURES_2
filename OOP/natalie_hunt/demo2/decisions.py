
# Note: Proper enums were added to python 3.4. We'll just
# use module-level variables instead of a proper enum.
EMPTY = 0
RECYCLE = 1
COMPOST = 2
LANDFILL = 3


class DecisionModule(object):
    '''
    This class makes decisions about where trash belongs.
    Currently, it makes every decision based on just one
    image of the trash. Future versions might use several
    images per decision.
    '''

    def __init__(self):
        '''
        Load the internal model and prepare for making
        decisions.
        '''
        pass  # TODO

    def process(self, frame):
        '''
        Use the internal model to process this frame and
        make a decision about which category it belongs to.
        Return the decision that is made for this object.
        '''
        pass # TODO
