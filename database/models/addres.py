from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from database.connection import Base


class Address(Base):
    __tablename__ = "addresses"

    Id: Mapped[int] = mapped_column(primary_key=True)

    CustomerId: Mapped[int | None] = mapped_column(
        ForeignKey("customers.id"),
    )

    Street: Mapped[str | None] = mapped_column(String)

    City: Mapped[str | None] = mapped_column(String)

    Province: Mapped[str | None] = mapped_column(String)

    PostalCode: Mapped[str | None] = mapped_column(String)

    Country: Mapped[str | None] = mapped_column(String)

    IsDefault: Mapped[bool | None] = mapped_column(Boolean)

    Customer = relationship(
        "Customer",
        back_populates="Addresses",
    )