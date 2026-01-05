from enum import Enum

class SQLDialect(str, Enum):
    postgresql = "postgresql"
    mysql = "mysql"
    sqlite = "sqlite"
    mssql = "mssql"
