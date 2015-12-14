import sys
from types import ModuleType as __ModuleType__



class __SelfWrapper__(__ModuleType__):
    def __init__(self, module, args={}):
        for attr in ["__builtins__", "__doc__", "__name__", "__package__"]:
            setattr(self, attr, getattr(module, attr, None))

        from django.conf import settings
        keys = dir(settings)
        for key in keys:
            if key.startswith("_"):
                continue
            val = getattr(settings, key)
            setattr(self, key, val)


self = sys.modules[__name__]
sys.modules[__name__] = __SelfWrapper__(self)