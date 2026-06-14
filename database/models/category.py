from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.connection import Base


class User(Base):
    __tablename__ = "users"

    Id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    Email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False,
    )

    PasswordHash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    Role: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    CreatedAt: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
    )

    from sqlalchemy.orm import relationship

    Children = relationship(
        "Category",
        back_populates="Parent",
    )

    Parent = relationship(
        "Category",
        remote_side=[Id],
        back_populates="Children",
    )