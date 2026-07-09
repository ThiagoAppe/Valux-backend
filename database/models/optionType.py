from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database.connection import Base


class OptionType(Base):
    __tablename__ = "option_types"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    code: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
    )

    sort_order: Mapped[int | None] = mapped_column()

    variant_options = relationship(
        "VariantOption",
        back_populates="option_type",
    )