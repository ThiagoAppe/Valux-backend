from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from database.connection import Base


class InventoryMovement(Base):
    __tablename__ = "inventory_movements"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    variantid: Mapped[int] = mapped_column(
        ForeignKey("variants.id"),
        nullable=False,
        index=True
    )

    type: Mapped[str] = mapped_column(String(50), nullable=False)

    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    reference_type: Mapped[str] = mapped_column(String(50), nullable=True)

    referenceid: Mapped[int] = mapped_column(Integer, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    variant = relationship("Variant", back_populates="inventory_movements")