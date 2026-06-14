from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.connection import Base


class Category(Base):
    __tablename__ = "categories"

    Id: Mapped[int] = mapped_column(primary_key=True)

    Name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    Slug: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
    )

    ParentId: Mapped[int | None] = mapped_column(
        ForeignKey("categories.id"),
        nullable=True,
    )

    from sqlalchemy.orm import relationship

    Variants = relationship(
        "Variant",
        back_populates="Product",
    )

    Images = relationship(
        "ProductImage",
        back_populates="Product",
    )

    Categories = relationship(
        "ProductCategory",
        back_populates="Product",
    )