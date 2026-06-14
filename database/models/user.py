from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.connection import Base


class User(Base):
    __tablename__ = "users"

    Id: Mapped[int] = mapped_column(primary_key=True)

    Email: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
    )

    PasswordHash: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    Role: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    CreatedAt: Mapped[datetime | None] = mapped_column(
        DateTime,
    )

    from sqlalchemy.orm import relationship

    Customer = relationship(
        "Customer",
        uselist=False,
    )