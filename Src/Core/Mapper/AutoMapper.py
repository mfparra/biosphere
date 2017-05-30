from Src.Core.Mapper.MapperUtils import MapperUtils
from Src.Core.Mapper.ToTypeInfo import ToTypeInfo


class AutoMapper(object):
    """
    
    """
    def __init__(self):
        self.__mappings = {}

    def create_map(self, from_type, to_type, mapping=None):
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

        from_class_name = from_type.__name__
        to_type_info = ToTypeInfo(class_type=to_type)

        if not from_class_name in self.__mappings:
            self.__mappings[from_class_name] = [to_type_info]
            return

        if not any(self.__get_type_to(from_type. to_type)):
            self.__mappings[from_class_name].append(to_type_info)
        else:
            raise Exception('There is already mapping create for the classes {0} and {1}'.format(from_class_name,
                                                                                                 to_type.__name__))

    def map(self, from_obj, to_type, ignore_case=True):
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

        from_obj_name = from_obj.__class__.__name__

        if not from_obj_name in self.__mappings:
            raise Exception('There is not mapping related to class {0}'.format(from_obj_name))

        to_type_name = to_type.__class__.__name__
        to_type_info = self.__get_type_to(from_obj_name, to_type_name)

        if to_type_info:
            raise Exception('There is not mapping related to classes {0} and {1}'.format(from_obj_name,
                                                                                         to_type_name))

        to_obj = to_type()

        if ignore_case:
            from_obj_dict = dict([(p.lower(), getattr(from_obj, p)) for p in MapperUtils.get_properties_from_class(type(from_obj))])
        else:
            from_obj_dict = dict([(p, getattr(from_obj, p)) for p in  MapperUtils.get_properties_from_class(type(from_obj))])

        for prop in MapperUtils.get_properties_from_class(to_type):
            setattr(to_obj, prop, from_obj_dict[prop.lower() if ignore_case else prop])

        return to_obj

    def __get_type_to(self, from_obj_name, to_type_name):
        to_type_info = [t for t in self.__mappings[from_obj_name] if t.class_type.__name__ == to_type_name]
        return to_type_info[0] if to_type_info else None





