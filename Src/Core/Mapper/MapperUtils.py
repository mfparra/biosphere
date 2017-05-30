class MapperUtils(object):
    """"""
    @staticmethod
    def get_properties_from_class(class_type):
        """
        
        :param class_type: 
        :return: 
        """
        if not class_type:
            raise ValueError('The class_type is required.')

        return [p for p in dir(class_type) if isinstance(getattr(class_type, p), property)]