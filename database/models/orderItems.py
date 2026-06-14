from decimal import Decimal

from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.connection import Base


class OrderItem(Base):
    __tablename__ = "order_items"

    Id: Mapped[int] = mapped_column(primary_key=True)

    OrderId: Mapped[int | None] = mapped_column(
        ForeignKey("orders.id"),
    )

    VariantId: Mapped[int | None] = mapped_column(
        ForeignKey("variants.id"),
    )

    Quantity: Mapped[int | None] = mapped_column()

    UnitPrice: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
    )

    ProductName: Mapped[str | None] = mapped_column(String)

    VariantName: Mapped[str | None] = mapped_column(String)

    Sku: Mapped[str | None] = mapped_column(String)

    OptionsSnapshot: Mapped[str | None] = mapped_column(Text)

    from sqlalchemy.orm import relationship

    Order = relationship(
        "Order",
        back_populates="Items",
    )

    Variant = relationship(
        "Variant",
        back_populates="OrderItems",
    )