from sqlalchemy import func, select
from sqlalchemy.orm import Session

from database.models.product import Product
from database.models.productImage import ProductImage
from database.models.variants import Variant


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_catalog_products(self):
        statement = (
            select(
                Product.id,
                Product.name,
                func.min(Variant.price).label("price_from"),
                ProductImage.path,
            )
            .join(
                Variant,
                Variant.product_id == Product.id,
            )
            .join(
                ProductImage,
                (ProductImage.product_id == Product.id)
                & (ProductImage.sort_order == 1),
                isouter=True,
            )
            .where(Product.active.is_(True))
            .group_by(
                Product.id,
                Product.name,
                ProductImage.path,
            )
            .order_by(Product.name)
        )

        return self.db.execute(statement).all()