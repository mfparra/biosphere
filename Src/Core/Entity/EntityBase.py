from abc import ABCMeta

from Src.Core.Converters.DictConverter import DictConvert
from Src.Core.Validation.EntityValidation import EntityValidation


class EntityBase(EntityValidation, DictConvert, metaclass = ABCMeta):
    pass