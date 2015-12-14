#import os
import sys
from types import ModuleType as __ModuleType__



class __SelfWrapper__(__ModuleType__):
    def __init__(self, module, args={}):
        # this is super ugly to have to copy attributes like this,
        # but it seems to be the only way to make reload() behave
        # nicely.  if i make these attributes dynamic lookups in
        # __getattr__, reload sometimes chokes in weird ways...
        for attr in ["__builtins__", "__doc__", "__name__", "__package__"]:
            setattr(self, attr, getattr(module, attr, None))


        from django.conf import settings
        keys = dir(settings)
        for key in keys:
            if key.startswith("_"):
                continue
            val = getattr(settings, key)
            print "%s = %s" % (key, val)
            setattr(self, key, val)

        # python 3.2 (2.7 and 3.3 work fine) breaks on osx (not ubuntu)
        # if we set this to None.  and 3.3 needs a value for __path__
        # self.__path__ = []
        # self.__module__ = module

        #self.__env = Environment(globals(), baked_args)

    # def __setattr__(self, name, value):
    #     raise Exception("You cannot assign a value from here!")

    # def __getattr__(self, name):
    #     from django.conf import settings
    #     try:
    #         return getattr(settings, name)
    #     except Exception, ex:
    #         print "ERROR: %s" % ex.message

    # # accept special keywords argument to define defaults for all operations
    # # that will be processed with given by return SelfWrapper
    # def __call__(self, **kwargs):
    #     return SelfWrapper(self.__module__, kwargs)


self = sys.modules[__name__]
sys.modules[__name__] = __SelfWrapper__(self)