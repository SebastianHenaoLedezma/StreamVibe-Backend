from collections.abc import Iterable

from rest_framework.serializers import ModelSerializer


class ParentModelSerializer(ModelSerializer):

    def __init__(self, *args, **kwargs):

        if len(args) > 0:
            objs = args[0]
            objs = self.__class__._process_data(objs, **kwargs)
            super().__init__(objs)
        else:
            super().__init__(**kwargs)

    @staticmethod
    def process_data(obj, **kwargs):
        return obj

    @classmethod
    def _process_data(cls, objs, **kwargs):

        if objs is None:
            return None

        if isinstance(objs, cls.Meta.model):
            return cls.process_data(objs, **kwargs)
        elif isinstance(objs, Iterable):
            return [cls.process_data(obj, **kwargs) for obj in objs]
        else:
            raise NotImplementedError(f'Object should be of class Iterable or {cls.Meta.model}, but found {type(objs)}')
