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


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True)

    orderid: Mapped[int | None] = mapped_column(
        ForeignKey("orders.id"),
    )

    method: Mapped[str | None] = mapped_column(String)

    status: Mapped[str | None] = mapped_column(String)

    transactionid: Mapped[str | None] = mapped_column(
        String,
        unique=True,
    )

    amount: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
    )

    created_at: Mapped[datetime | None] = mapped_column(
        DateTime,
    )

    order = relationship(
        "Order",
        back_populates="payments",
    )