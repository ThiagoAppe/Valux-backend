from decimal import Decimal

from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database.connection import Base


class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True)

    orderid: Mapped[int | None] = mapped_column(
        ForeignKey("orders.id"),
    )

    variantid: Mapped[int | None] = mapped_column(
        ForeignKey("variants.id"),
    )

    quantity: Mapped[int | None] = mapped_column()

    unit_price: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
    )

    product_name: Mapped[str | None] = mapped_column(String)

    variant_name: Mapped[str | None] = mapped_column(String)

    sku: Mapped[str | None] = mapped_column(String)

    options_snapshot: Mapped[str | None] = mapped_column(Text)

    order = relationship(
        "Order",
        back_populates="items",
    )

    variant = relationship(
        "Variant",
        back_populates="order_items",
    )