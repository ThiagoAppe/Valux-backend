from fastapi import APIRouter, Depends

from database.dependencies import GetProductService
from database.services.product_service import ProductService


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/catalog")
def get_catalog(
    product_service: ProductService = Depends(GetProductService)
):
    return product_service.get_catalog_products()