from sqlalchemy import Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from database.connection import Base


class Inventory(Base):
    __tablename__ = "inventory"

    variantid: Mapped[int] = mapped_column(
        ForeignKey("variants.id"),
        primary_key=True
    )

    stock_available: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    stock_reserved: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    variant = relationship("Variant", back_populates="inventory")