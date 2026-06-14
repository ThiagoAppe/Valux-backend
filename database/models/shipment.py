from decimal import Decimal

from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.connection import Base


class Shipment(Base):
    __tablename__ = "shipments"

    Id: Mapped[int] = mapped_column(primary_key=True)

    OrderId: Mapped[int | None] = mapped_column(
        ForeignKey("orders.id"),
    )

    Cost: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
    )

    Status: Mapped[str | None] = mapped_column(String)

    ShippingStreet: Mapped[str | None] = mapped_column(String)

    ShippingCity: Mapped[str | None] = mapped_column(String)

    ShippingProvince: Mapped[str | None] = mapped_column(String)

    ShippingPostalCode: Mapped[str | None] = mapped_column(String)

    from sqlalchemy.orm import relationship

    Order = relationship(
        "Order",
        back_populates="Shipments",
    )