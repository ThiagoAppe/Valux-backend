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
            .where(Inventory.VariantId == variant_id)
            .with_for_update()
        )

        inventory = self.db.execute(stmt).scalar_one_or_none()

        if not inventory:
            inventory = Inventory(
                VariantId=variant_id,
                StockAvailable=0,
                StockReserved=0
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

        if inventory.StockAvailable < quantity:
            raise ValueError("Insufficient stock")

        inventory.StockAvailable -= quantity
        inventory.StockReserved += quantity

        self.db.add(
            InventoryMovement(
                VariantId=variant_id,
                Type="reserve",
                Quantity=quantity,
                ReferenceType=reference_type,
                ReferenceId=reference_id
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

        inventory.StockReserved -= quantity
        inventory.StockAvailable += quantity

        self.db.add(
            InventoryMovement(
                VariantId=variant_id,
                Type="release",
                Quantity=quantity,
                ReferenceType=reference_type,
                ReferenceId=reference_id
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

        if inventory.StockReserved < quantity:
            raise ValueError("Invalid reserved stock")

        inventory.StockReserved -= quantity

        self.db.add(
            InventoryMovement(
                VariantId=variant_id,
                Type="out",
                Quantity=quantity,
                ReferenceType=reference_type,
                ReferenceId=reference_id
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

        inventory.StockAvailable += quantity

        self.db.add(
            InventoryMovement(
                VariantId=variant_id,
                Type="in",
                Quantity=quantity,
                ReferenceType=reference_type,
                ReferenceId=reference_id
            )
        )

        self.db.flush()

        return inventory