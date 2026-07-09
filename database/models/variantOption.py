from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database.connection import Base


class VariantOption(Base):
    __tablename__ = "variant_options"

    id: Mapped[int] = mapped_column(primary_key=True)

    variant_id: Mapped[int] = mapped_column(
        ForeignKey("variants.id"),
    )

    option_type_id: Mapped[int] = mapped_column(
        ForeignKey("option_types.id"),
    )

    value: Mapped[str | None]

    variant = relationship(
        "Variant",
        back_populates="options",
    )

    option_type = relationship(
        "OptionType",
        back_populates="variant_options",
    )