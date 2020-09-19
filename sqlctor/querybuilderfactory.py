from optypes import OpTypes
from querybuilder import SelectQueryBuilder, InsertQueryBuilder, UpdateQueryBuilder, DeleteQueryBuilder


class SqlQueryBuilderFactory(object):

    @staticmethod
    def get_query_builder(operation: OpTypes):
        '''
        Returns an instance of a QueryBuilder object
        based on the operation type @param OpType
        '''

        if operation is OpTypes.SELECT:
            return SelectQueryBuilder()
        if operation is OpTypes.INSERT:
            return InsertQueryBuilder()
        if operation is OpTypes.UPDATE:
            return UpdateQueryBuilder()
        if operation is OpTypes.DELETE:
            return DeleteQueryBuilder()
    