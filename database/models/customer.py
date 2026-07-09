from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database.connection import Base


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
    )

    first_name: Mapped[str | None] = mapped_column(
        String,
    )

    last_name: Mapped[str | None] = mapped_column(
        String,
    )

    phone: Mapped[str | None] = mapped_column(
        String,
    )

    created_at: Mapped[datetime | None] = mapped_column(
        DateTime,
    )

    user = relationship(
        "User",
        back_populates="customer",
    )

    addresses = relationship(
        "Address",
        back_populates="customer",
    )

    carts = relationship(
        "Cart",
        back_populates="customer",
    )

    orders = relationship(
        "Order",
        back_populates="customer",
    )