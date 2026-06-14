from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.connection import Base


class Customer(Base):
    __tablename__ = "customers"

    Id: Mapped[int] = mapped_column(primary_key=True)

    UserId: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
    )

    FirstName: Mapped[str | None] = mapped_column(
        String,
    )

    LastName: Mapped[str | None] = mapped_column(
        String,
    )

    Phone: Mapped[str | None] = mapped_column(
        String,
    )

    CreatedAt: Mapped[datetime | None] = mapped_column(
        DateTime,
    )

    from sqlalchemy.orm import relationship

    User = relationship(
        "User",
    )

    Addresses = relationship(
        "Address",
        back_populates="Customer",
    )

    Carts = relationship(
        "Cart",
        back_populates="Customer",
    )

    Orders = relationship(
        "Order",
        back_populates="Customer",
    )