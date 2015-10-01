from progress.bar import Bar
from progress.helpers import SHOW_CURSOR


class ProgressBarMixin(object):

    def __init__(self,*args,**kwargs):
        self._name = kwargs.get('name','Loading')
        self._max = kwargs.get('max',100)

    def _create_bar(self):
        return Bar(self._name,max=self._max)

    def update_bar(self):
        self._bar.next()

    def finish_bar(self):
        self._bar = None
        print(SHOW_CURSOR)
        print("")

    def initialize_bar(self,*args,**kwargs):
        self._name = kwargs.get('name',self._name)
        self._max = kwargs.get('max',self._max)
        self._bar = self._create_bar()