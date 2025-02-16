from datetime import datetime

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declared_attr


class BaseEntity:
    """
    This class is a base class for all models in the application.
    It provides the following columns:
    - id: primary key
    - created_at: creation date
    - updated_at: last update date
    - deletion_date: deletion date (null means not deleted)
    """

    @declared_attr
    def id(self):
        return Column(Integer, primary_key=True, autoincrement=True, index=True)

    @declared_attr
    def created_at(self):
        return Column(DateTime, default=datetime.utcnow, nullable=False)

    @declared_attr
    def updated_at(self):
        return Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    @declared_attr
    def deletion_date(self):
        return Column(DateTime, nullable=True)  # Null means not deleted
