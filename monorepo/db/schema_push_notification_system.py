from enum import Enum
from typing import Any, Optional
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum, 
    Integer,
    JSON,
    String,
    Text,
)
from sqlalchemy.dialects import mssql, postgresql, sqlite, mysql
from sqlalchemy.engine.interfaces import Dialect

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.schema import CreateTable
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.schema import ForeignKey
from sqlalchemy.schema import MetaData
from sqlalchemy.schema import UniqueConstraint
from monorepo.common.env_manager import get_env_variable
from monorepo.common.logger import get_logger


log = get_logger(__file__, "INFO")
metadata_obj = MetaData(schema="push_notification_system")


class Base(DeclarativeBase):
    metadata = metadata_obj

    def get_dict_repr(self):
        for key in self.__table__.columns.keys():
            value = self.__getattribute__(key)
            yield key, value

    def __repr__(self) -> str:
        fields = ", ".join(["{0}={1}".format(key, value) for key, value in self.get_dict_repr()])
        return "{0} {1}".format(self.__class__.__name__, fields)


class PushNotificationTypes(Enum):
    MOBILE = 'mobile'
    SMS = 'sms'
    EMAIL = 'email'


class TblUsers(Base):
    __tablename__ = 'tbl_users'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment='Primary Key'
    )
    email: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment='User Email'
    )
    country_code: Mapped[int] = mapped_column(
        nullable=False,
        comment='Country Code'
    )
    phone_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        comment='Phone Number'
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        comment='Date created'
    )

    __table_args__ = (
        UniqueConstraint('email'),
    )


class TblDevices(Base):
    __tablename__ = 'tbl_devices'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment='Primary Key'
    )
    device_token: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment='User Email'
    )
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('tbl_users.id', ondelete='CASCADE'),
        nullable=False,
        comment='Foreing key User Id',
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        comment='Date created'
    )
    last_logged_in_at: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        comment='Date created'
    )

    __table_args__ = (
        UniqueConstraint('device_token'),
    )

