from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.connection import Base

from sqlalchemy.orm import relationship


class ProductImage(Base):
    __tablename__ = "product_images"

    id: Mapped[int] = mapped_column(primary_key=True)

    product_id: Mapped[int | None] = mapped_column(
        ForeignKey("products.id"),
    )

    path: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    sort_order: Mapped[int | None] = mapped_column()

    product = relationship(
        "Product",
        back_populates="images",
    )