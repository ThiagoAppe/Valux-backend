from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from database.connection import Base


class CartItem(Base):
    __tablename__ = "cart_items"

    Id: Mapped[int] = mapped_column(primary_key=True)

    CartId: Mapped[int | None] = mapped_column(
        ForeignKey("carts.id"),
    )

    VariantId: Mapped[int | None] = mapped_column(
        ForeignKey("variants.id"),
    )

    Quantity: Mapped[int | None] = mapped_column()

    Cart = relationship(
        "Cart",
        back_populates="Items",
    )

    Variant = relationship(
        "Variant",
        back_populates="CartItems",
    )