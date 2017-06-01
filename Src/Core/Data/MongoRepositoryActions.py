from typing import List, Dict

from Src.BioDataManagement.DataAccess.Mappers.Mapper import Mapper
from Src.Core.Filter.FilterEntityListBase import FilterEntityListBase


class MongoRepositoryActions:
    """description of class"""

    def __init__(self, collection):
        """
        
        :param collection: 
        """
        if collection:
            raise ValueError('The collection is required.')

        self.__collection = collection

    def add_many(self, dtos:List, entity_class):
        entities = [self.__map_dto_to_entity(dto, entity_class) for dto in dtos]
        self.__collection.insert_many(entities, many=True)

    def get_many(self, query, filter_entity: FilterEntityListBase, entity_class,
                  dto_class=None, include_or_exclude_fields: Dict[str, int] = None) -> FilterEntityListBase:
        """
        
        :param query: 
        :param filter_entity:        
        :param entity_class: 
        :param dto_class: 
        :param include_or_exclude_fields: 
        :return: 
        """
        cursor = None

        if filter.is_paged:
            start_row = filter.page_size * filter.current_page

            result_count = self.__collection.find(query).count() if not include_or_exclude_fields \
                else self.__collection.find(query, include_or_exclude_fields).count()

            result_list = list(self.__collection.find(query, skip=start_row, limit=filter.page_size)) \
                if not include_or_exclude_fields \
                else list(self.__collection.find(query, include_or_exclude_fields, skip=start_row, limit=filter.page_size))

            div_result = divmod(result_count, filter.page_size)
            filter.page_count = div_result[0]

            if div_result[1] > 0:
                filter.page_count += 1
        else:
            filter.page_count = 1
            result_list = list(self.__collection.find(query)) \
                if not include_or_exclude_fields \
                else list(self.__collection.find(query, include_or_exclude_fields))

        filter.current_page += 1

        if not result_list:
            filter.result_list = []
        elif dto_class:
            filter.result_list = [Mapper.get_instance().map(entity_class(**e), dto_class) for e in result_list]
        else:
            filter.result_list = result_list

        return filter

    def __map_dto_to_entity(self, dto, entity_class):
        entity = Mapper.get_instance().map(dto, entity_class)
        entity.validate()
        return entity.as_dict()
