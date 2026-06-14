from sqlalchemy.orm import Session

from models.inventory import Inventory


class InventoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def GetByVariantId(self, variant_id: int) -> Inventory | None:
        return self.db.query(Inventory).filter(
            Inventory.VariantId == variant_id
        ).first()

    def Create(self, variant_id: int) -> Inventory:
        inventory = Inventory(
            VariantId=variant_id,
            StockAvailable=0,
            StockReserved=0
        )

        self.db.add(inventory)
        self.db.flush()

        return inventory

    def IncreaseStock(self, variant_id: int, quantity: int) -> Inventory:
        inventory = self.GetByVariantId(variant_id)

        if not inventory:
            inventory = self.Create(variant_id)

        inventory.StockAvailable += quantity
        self.db.flush()

        return inventory

    def DecreaseStock(self, variant_id: int, quantity: int) -> Inventory:
        inventory = self.GetByVariantId(variant_id)

        if not inventory:
            raise ValueError("Inventory not found")

        inventory.StockAvailable -= quantity
        self.db.flush()

        return inventory

    def ReserveStock(self, variant_id: int, quantity: int) -> Inventory:
        inventory = self.GetByVariantId(variant_id)

        if not inventory:
            raise ValueError("Inventory not found")

        inventory.StockAvailable -= quantity
        inventory.StockReserved += quantity

        self.db.flush()

        return inventory

    def ReleaseStock(self, variant_id: int, quantity: int) -> Inventory:
        inventory = self.GetByVariantId(variant_id)

        if not inventory:
            raise ValueError("Inventory not found")

        inventory.StockReserved -= quantity
        inventory.StockAvailable += quantity

        self.db.flush()

        return inventory

    def CommitReservedStock(self, variant_id: int, quantity: int) -> Inventory:
        inventory = self.GetByVariantId(variant_id)

        if not inventory:
            raise ValueError("Inventory not found")

        inventory.StockReserved -= quantity
        self.db.flush()

        return inventory