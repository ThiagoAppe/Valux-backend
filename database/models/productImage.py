from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.connection import Base

from sqlalchemy.orm import relationship


class ProductImage(Base):
    __tablename__ = "product_images"

    Id: Mapped[int] = mapped_column(primary_key=True)

    ProductId: Mapped[int | None] = mapped_column(
        ForeignKey("products.id"),
    )

    Url: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    SortOrder: Mapped[int | None] = mapped_column()

    Product = relationship(
        "Product",
        back_populates="Images",
    )