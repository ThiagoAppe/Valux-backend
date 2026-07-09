from decimal import Decimal

from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database.connection import Base


class Shipment(Base):
    __tablename__ = "shipments"

    id: Mapped[int] = mapped_column(primary_key=True)

    orderid: Mapped[int | None] = mapped_column(
        ForeignKey("orders.id"),
    )

    cost: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
    )

    status: Mapped[str | None] = mapped_column(String)

    shipping_street: Mapped[str | None] = mapped_column(String)

    shipping_city: Mapped[str | None] = mapped_column(String)

    shipping_province: Mapped[str | None] = mapped_column(String)

    shipping_postal_code: Mapped[str | None] = mapped_column(String)

    order = relationship(
        "Order",
        back_populates="shipments",
    )