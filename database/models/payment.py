from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.connection import Base


class Payment(Base):
    __tablename__ = "payments"

    Id: Mapped[int] = mapped_column(primary_key=True)

    OrderId: Mapped[int | None] = mapped_column(
        ForeignKey("orders.id"),
    )

    Method: Mapped[str | None] = mapped_column(String)

    Status: Mapped[str | None] = mapped_column(String)

    TransactionId: Mapped[str | None] = mapped_column(
        String,
        unique=True,
    )

    Amount: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
    )

    CreatedAt: Mapped[datetime | None] = mapped_column(
        DateTime,
    )

    from sqlalchemy.orm import relationship

    Order = relationship(
        "Order",
        back_populates="Payments",
    )