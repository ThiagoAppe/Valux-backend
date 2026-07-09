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

    id: Mapped[int] = mapped_column(primary_key=True)

    customerid: Mapped[int | None] = mapped_column(
        ForeignKey("customers.id"),
    )

    created_at: Mapped[datetime | None] = mapped_column(
        DateTime,
    )

    status: Mapped[str | None] = mapped_column(String)

    customer = relationship(
        "Customer",
        back_populates="carts",
    )

    items = relationship(
        "CartItem",
        back_populates="cart",
    )