from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.connection import Base


class OptionType(Base):
    __tablename__ = "option_types"

    Id: Mapped[int] = mapped_column(primary_key=True)

    Name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    Code: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
    )

    SortOrder: Mapped[int | None] = mapped_column()