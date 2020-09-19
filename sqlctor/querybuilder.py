from abc import ABC, abstractmethod


class QueryBuilder(ABC):
    @abstractmethod
    def __str__(self):
        yield None


class SelectQueryBuilder(object):
    pass


class InsertQueryBuilder(object):
    pass


class UpdateQueryBuilder(object):
    pass


class DeleteQueryBuilder(object):
    pass