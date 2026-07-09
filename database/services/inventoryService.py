from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy import select

from models.inventory import Inventory
from models.inventory_movements import InventoryMovement


class InventoryService:
    def __init__(self, db: Session):
        self.db = db

    def _GetInventoryLocked(self, variant_id: int) -> Inventory:
        stmt = (
            select(Inventory)
            .where(Inventory.Variantid == variant_id)
            .with_for_update()
        )

        inventory = self.db.execute(stmt).scalar_one_or_none()

        if not inventory:
            inventory = Inventory(
                Variantid=variant_id,
                stock_available=0,
                stock_reserved=0
            )
            self.db.add(inventory)
            self.db.flush()

        return inventory

    def ReserveStock(
        self,
        variant_id: int,
        quantity: int,
        reference_type: Optional[str] = None,
        reference_id: Optional[int] = None
    ):
        inventory = self._GetInventoryLocked(variant_id)

        if inventory.stock_available < quantity:
            raise ValueError("Insufficient stock")

        inventory.stock_available -= quantity
        inventory.stock_reserved += quantity

        self.db.add(
            InventoryMovement(
                Variantid=variant_id,
                Type="reserve",
                Quantity=quantity,
                reference_type=reference_type,
                Referenceid=reference_id
            )
        )

        self.db.flush()

        return inventory

    def ReleaseStock(
        self,
        variant_id: int,
        quantity: int,
        reference_type: Optional[str] = None,
        reference_id: Optional[int] = None
    ):
        inventory = self._GetInventoryLocked(variant_id)

        inventory.stock_reserved -= quantity
        inventory.stock_available += quantity

        self.db.add(
            InventoryMovement(
                Variantid=variant_id,
                Type="release",
                Quantity=quantity,
                reference_type=reference_type,
                Referenceid=reference_id
            )
        )

        self.db.flush()

        return inventory

    def CommitStock(
        self,
        variant_id: int,
        quantity: int,
        reference_type: Optional[str] = None,
        reference_id: Optional[int] = None
    ):
        inventory = self._GetInventoryLocked(variant_id)

        if inventory.stock_reserved < quantity:
            raise ValueError("Invalid reserved stock")

        inventory.stock_reserved -= quantity

        self.db.add(
            InventoryMovement(
                Variantid=variant_id,
                Type="out",
                Quantity=quantity,
                reference_type=reference_type,
                Referenceid=reference_id
            )
        )

        self.db.flush()

        return inventory

    def AddStock(
        self,
        variant_id: int,
        quantity: int,
        reference_type: Optional[str] = None,
        reference_id: Optional[int] = None
    ):
        inventory = self._GetInventoryLocked(variant_id)

        inventory.stock_available += quantity

        self.db.add(
            InventoryMovement(
                Variantid=variant_id,
                Type="in",
                Quantity=quantity,
                reference_type=reference_type,
                Referenceid=reference_id
            )
        )

        self.db.flush()

        return inventory