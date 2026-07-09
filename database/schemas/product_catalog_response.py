from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ProductCatalogResponse(BaseModel):
    id: int
    name: str
    price_from: Decimal
    image_url: str | None = None

    model_config = ConfigDict(
        from_attributes=True
    )