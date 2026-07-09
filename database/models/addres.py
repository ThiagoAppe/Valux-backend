from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from database.connection import Base


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True)

    customerid: Mapped[int | None] = mapped_column(
        ForeignKey("customers.id"),
    )

    street: Mapped[str | None] = mapped_column(String)

    city: Mapped[str | None] = mapped_column(String)

    province: Mapped[str | None] = mapped_column(String)

    postal_code: Mapped[str | None] = mapped_column(String)

    country: Mapped[str | None] = mapped_column(String)

    is_default: Mapped[bool | None] = mapped_column(Boolean)

    customer = relationship(
        "Customer",
        back_populates="addresses",
    )