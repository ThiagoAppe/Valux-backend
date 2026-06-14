from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from database.connection import Base


class Cart(Base):
    __tablename__ = "carts"

    Id: Mapped[int] = mapped_column(primary_key=True)

    CustomerId: Mapped[int | None] = mapped_column(
        ForeignKey("customers.id"),
    )

    CreatedAt: Mapped[datetime | None] = mapped_column(
        DateTime,
    )

    Status: Mapped[str | None] = mapped_column(String)

    Customer = relationship(
        "Customer",
        back_populates="Carts",
    )

    Items = relationship(
        "CartItem",
        back_populates="Cart",
    )