from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from database.connection import Base


class CartItem(Base):
    __tablename__ = "cart_items"

    id: Mapped[int] = mapped_column(primary_key=True)

    cartid: Mapped[int | None] = mapped_column(
        ForeignKey("carts.id"),
    )

    variantid: Mapped[int | None] = mapped_column(
        ForeignKey("variants.id"),
    )

    quantity: Mapped[int | None] = mapped_column()

    cart = relationship(
        "Cart",
        back_populates="items",
    )

    variant = relationship(
        "Variant",
        back_populates="cart_items",
    )