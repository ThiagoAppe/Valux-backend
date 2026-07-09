from config.settings import settings

from database.repositories.product_repository import ProductRepository
from database.schemas.product_catalog_response import ProductCatalogResponse


class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def get_catalog_products(self) -> list[ProductCatalogResponse]:
        rows = self.repository.get_catalog_products()

        return [
            ProductCatalogResponse(
                id=row.id,
                name=row.name,
                price_from=row.price_from,
                image_url=(
                    settings.build_media_url(row.path)
                    if row.path
                    else None
                ),
            )
            for row in rows
        ]