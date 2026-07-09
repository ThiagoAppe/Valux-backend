from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database.connection import Base


class ProductCategory(Base):
    __tablename__ = "product_categories"

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
        primary_key=True,
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        primary_key=True,
    )

    product = relationship(
        "Product",
        back_populates="categories",
    )

    category = relationship(
        "Category",
        back_populates="products",
    )