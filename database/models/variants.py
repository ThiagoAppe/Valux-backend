from datetime import datetime
from decimal import Decimal

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database.connection import Base


class Variant(Base):
    __tablename__ = "variants"

    id: Mapped[int] = mapped_column(primary_key=True)

    product_id: Mapped[int | None] = mapped_column(
        ForeignKey("products.id"),
    )

    sku: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
    )

    name: Mapped[str | None] = mapped_column(
        String,
    )

    price: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
    )

    active: Mapped[bool | None] = mapped_column(
        Boolean,
    )

    created_at: Mapped[datetime | None] = mapped_column(
        DateTime,
    )

    product = relationship(
        "Product",
        back_populates="variants",
    )

    options = relationship(
        "VariantOption",
        back_populates="variant",
    )

    cart_items = relationship(
        "CartItem",
        back_populates="variant",
    )

    order_items = relationship(
        "OrderItem",
        back_populates="variant",
    )

    inventory = relationship(
        "Inventory",
        back_populates="variant",
        uselist=False,
    )

    inventory_movements = relationship(
        "InventoryMovement",
        back_populates="variant",
    )