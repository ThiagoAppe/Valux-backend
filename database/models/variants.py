from datetime import datetime
from decimal import Decimal

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.connection import Base


class Variant(Base):
    __tablename__ = "variants"

    Id: Mapped[int] = mapped_column(primary_key=True)

    ProductId: Mapped[int | None] = mapped_column(
        ForeignKey("products.id"),
    )

    Sku: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
    )

    Name: Mapped[str | None] = mapped_column(
        String,
    )

    Price: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
    )

    Active: Mapped[bool | None] = mapped_column(
        Boolean,
    )

    CreatedAt: Mapped[datetime | None] = mapped_column(
        DateTime,
    )

    from sqlalchemy.orm import relationship

    Product = relationship(
        "Product",
        back_populates="Variants",
    )

    Options = relationship(
        "VariantOption",
        back_populates="Variant",
    )

    CartItems = relationship(
        "CartItem",
        back_populates="Variant",
    )

    OrderItems = relationship(
        "OrderItem",
        back_populates="Variant",
    )

    Inventory = relationship(
        "Inventory", 
        back_populates="Variant",
        uselist=False
    )
    
    InventoryMovements = relationship(
        "InventoryMovement",
        back_populates="Variant"
    )