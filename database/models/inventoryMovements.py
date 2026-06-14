from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from database.connection import Base


class InventoryMovement(Base):
    __tablename__ = "inventory_movements"

    Id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    VariantId: Mapped[int] = mapped_column(
        ForeignKey("variants.id"),
        nullable=False,
        index=True
    )

    Type: Mapped[str] = mapped_column(String(50), nullable=False)

    Quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    ReferenceType: Mapped[str] = mapped_column(String(50), nullable=True)

    ReferenceId: Mapped[int] = mapped_column(Integer, nullable=True)

    CreatedAt: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    Variant = relationship("Variant", back_populates="InventoryMovements")