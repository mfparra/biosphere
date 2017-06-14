from typing import Dict

from Src.Core.Mapper.MapperUtils import MapperUtils
from Src.Core.Mapper.ToTypeInfo import ToTypeInfo


class AutoMapper(object):
    """
    
    """
    def __init__(self):
        self.__mappings = {}

    def create_map(self, from_type, to_type, mapping:Dict=None):
        """
        
        :param type_from: 
        :param type_to: 
        :param mapping: 
        :return: 
        """
        if not from_type:
            raise ValueError('The from_type parameter is required.')

        if not to_type:
            raise ValueError('The to_type parameter is required.')

        no_properties = False

        if isinstance(from_type, str):
            from_class_name = from_type
            no_properties = True
        else:
            from_class_name = from_type.__name__

        to_type_info = ToTypeInfo(class_type=to_type, mapping=mapping, no_properties=no_properties)

        if not from_class_name in self.__mappings:
            self.__mappings[from_class_name] = [to_type_info]
            return

        if not any(self.__get_type_to(from_type, to_type.__name__)):
            self.__mappings[from_class_name].append(to_type_info)
        else:
            raise Exception('There is already mapping create for the classes {0} and {1}'.format(from_class_name,
                                                                                                 to_type.__name__))

    def map(self, from_obj, to_type, ignore_case:bool=True, from_obj_class_name:str=''):
        """
        
        :param from_obj: 
        :param to_type: 
        :param ignore_case: 
        :return: 
        """
        if not from_obj:
            raise ValueError('The from_obj parameter is required.')

        if not to_type:
            raise ValueError('The to_type parameter is required.')

        from_obj_name =  from_obj_class_name if from_obj_class_name else from_obj.__class__.__name__

        if not from_obj_name in self.__mappings:
            raise Exception('There is not mapping related to class {0}'.format(from_obj_name))

        to_obj = to_type()
        to_type_name = to_obj.__class__.__name__
        to_type_info = self.__get_type_to(from_obj_name, to_type_name)

        if not to_type_info:
            raise Exception('There is not mapping related to classes {0} and {1}'.format(from_obj_name,
                                                                                         to_type_name))


        if not from_obj_class_name:
            from_obj_dict = dict(map(lambda prop: (prop.lower() if ignore_case else prop,
                                                   getattr(from_obj, prop)),
                                     MapperUtils.get_properties_from_class(type(from_obj))))

            to_properties = map(lambda prop: prop.lower() if ignore_case else prop,
                                MapperUtils.get_properties_from_class(to_type))

            for prop in filter(lambda prop: prop in from_obj_dict, to_properties):
                setattr(to_obj, prop, from_obj_dict[prop])

        if not to_type_info.mapping:
            return to_obj

        for to_prop, map_func in [(prop, map_func) for prop, map_func in to_type_info.mapping.items() if map_func]:
            setattr(to_obj, to_prop, map_func(from_obj))

        return to_obj

    def __get_type_to(self, from_obj_name, to_type_name):
        to_type_info = list(filter(lambda t: t.class_type.__name__ == to_type_name, self.__mappings[from_obj_name]))
        return to_type_info[0] if any(to_type_info) else None





