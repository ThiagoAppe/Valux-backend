from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.connection import Base


class Order(Base):
    __tablename__ = "orders"

    Id: Mapped[int] = mapped_column(primary_key=True)

    CustomerId: Mapped[int | None] = mapped_column(
        ForeignKey("customers.id"),
    )

    Status: Mapped[str | None] = mapped_column(String)

    TotalAmount: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
    )

    CreatedAt: Mapped[datetime | None] = mapped_column(
        DateTime,
    )

    from sqlalchemy.orm import relationship

    Customer = relationship(
        "Customer",
        back_populates="Orders",
    )

    Items = relationship(
        "OrderItem",
        back_populates="Order",
    )

    Payments = relationship(
        "Payment",
        back_populates="Order",
    )

    Shipments = relationship(
        "Shipment",
        back_populates="Order",
    )