from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database.connection import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)

    customerid: Mapped[int | None] = mapped_column(
        ForeignKey("customers.id"),
    )

    status: Mapped[str | None] = mapped_column(String)

    total_amount: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
    )

    created_at: Mapped[datetime | None] = mapped_column(
        DateTime,
    )

    customer = relationship(
        "Customer",
        back_populates="orders",
    )

    items = relationship(
        "OrderItem",
        back_populates="order",
    )

    payments = relationship(
        "Payment",
        back_populates="order",
    )

    shipments = relationship(
        "Shipment",
        back_populates="order",
    )