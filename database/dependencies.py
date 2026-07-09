from fastapi import Depends
from sqlalchemy.orm import Session

from database.connection import GetDb
from database.repositories.product_repository import ProductRepository
from database.services.product_service import ProductService


def GetProductService(
    db: Session = Depends(GetDb)
) -> ProductService:
    repository = ProductRepository(db)

    return ProductService(repository)