from sqlalchemy import Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from database.connection import Base


class Inventory(Base):
    __tablename__ = "inventory"

    VariantId: Mapped[int] = mapped_column(
        ForeignKey("variants.id"),
        primary_key=True
    )

    StockAvailable: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    StockReserved: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    UpdatedAt: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    Variant = relationship("Variant", back_populates="Inventory")