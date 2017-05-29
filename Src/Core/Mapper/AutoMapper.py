from Src.Core.Mapper.TypeToInfo import TypeToInfo


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

        if not from_type.__name__ in self.__mappings:
            return

        type_to_info = TypeToInfo(class_type=to_type.__name__)

        from_class_name = from_type.__name__

        if self.__mappings[from_class_name]:
            self.__mappings[from_class_name] = [type_to_info]
        elif not any(self.__get_type_to(from_type. to_type)):
            self.__mappings[from_class_name].append(type_to_info)
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
        if not from_obj.__name__ in self.__mappings:
            raise Exception('There is not mapping related to class {0}'.format(from_obj.__name__))

        type_to_info = self.__get_type_to(from_obj, to_type)

        if type_to_info:
            raise Exception('There is not mapping related to classes {0} and {1}'.format(from_obj.__name__,
                                                                                         to_type.__name__))

        to_obj = to_type()

        if ignore_case:
            from_obj_dict = dict([(k.upper(), v) for k,v in from_obj.__dict__.items()])
        else:
            from_obj_dict = dict([(k, v) for k, v in from_obj.__dict__.items()]

        for prop in type_to_info.properties:
            to_obj[prop] = from_obj[prop.upper() if ignore_case else prop]

        return to_obj

    def __get_type_to(self, from_type, to_type):
        to_type_name = to_type.__name__
        type_to_info = [t for t in self.__mappings[from_type.__name__] if t.class_type.__name__ == to_type_name]
        return type_to_info[0] if type_to_info else None





