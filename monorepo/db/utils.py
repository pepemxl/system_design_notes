from sqlalchemy.dialects import mssql, postgresql, sqlite, mysql
from sqlalchemy.engine.interfaces import Dialect
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.schema import CreateTable
from monorepo.db.schema_push_notification_system import TblUsers


def get_ddl_for_table(tbl_obj: DeclarativeBase, dialect:Dialect) -> str:
    if dialect is None:
        return CreateTable(tbl_obj.__table__).compile(bind=None)
    else:
        return CreateTable(tbl_obj.__table__).compile(dialect=dialect)


def get_mysql_ddl_for_table(tbl_obj: DeclarativeBase):
    return get_ddl_for_table(tbl_obj, dialect=mssql.dialect())


def get_postgresql_ddl_for_table(tbl_obj: DeclarativeBase):
    return get_ddl_for_table(tbl_obj, dialect=postgresql.dialect())


def get_sqlite_ddl_for_table(tbl_obj: DeclarativeBase):
    return get_ddl_for_table(tbl_obj, dialect=sqlite.dialect())


def get_mysql_ddl_for_table(tbl_obj: DeclarativeBase):
    return get_ddl_for_table(tbl_obj, dialect=mysql.dialect())


def print_schema_definition(metadata_obj):
    for table in metadata_obj.tables.values():
        print("| Column | Type | Comment |")
        print("| --- | --- | --- |")
        for col in table.c:
            comment = col.comment if col.comment is not None else ""
            print("|{0}|{1}|{2}|".format(col.name, col.type, comment))
        print("")



if __name__ == '__main__':
    print(TblUsers())
    print(TblUsers().metadata.schema)
    # print_schema_definition(TblUsers().metadata)
    # ddl_tbl = get_mysql_ddl_for_table(TblUsers())
    # print(ddl_tbl)
