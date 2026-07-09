from sqlalchemy.orm import Session

from models.inventory import Inventory


class InventoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def GetByVariantid(self, variant_id: int) -> Inventory | None:
        return self.db.query(Inventory).filter(
            Inventory.Variantid == variant_id
        ).first()

    def Create(self, variant_id: int) -> Inventory:
        inventory = Inventory(
            Variantid=variant_id,
            stock_available=0,
            stock_reserved=0
        )

        self.db.add(inventory)
        self.db.flush()

        return inventory

    def IncreaseStock(self, variant_id: int, quantity: int) -> Inventory:
        inventory = self.GetByVariantid(variant_id)

        if not inventory:
            inventory = self.Create(variant_id)

        inventory.stock_available += quantity
        self.db.flush()

        return inventory

    def DecreaseStock(self, variant_id: int, quantity: int) -> Inventory:
        inventory = self.GetByVariantid(variant_id)

        if not inventory:
            raise ValueError("Inventory not found")

        inventory.stock_available -= quantity
        self.db.flush()

        return inventory

    def ReserveStock(self, variant_id: int, quantity: int) -> Inventory:
        inventory = self.GetByVariantid(variant_id)

        if not inventory:
            raise ValueError("Inventory not found")

        inventory.stock_available -= quantity
        inventory.stock_reserved += quantity

        self.db.flush()

        return inventory

    def ReleaseStock(self, variant_id: int, quantity: int) -> Inventory:
        inventory = self.GetByVariantid(variant_id)

        if not inventory:
            raise ValueError("Inventory not found")

        inventory.stock_reserved -= quantity
        inventory.stock_available += quantity

        self.db.flush()

        return inventory

    def CommitReservedStock(self, variant_id: int, quantity: int) -> Inventory:
        inventory = self.GetByVariantid(variant_id)

        if not inventory:
            raise ValueError("Inventory not found")

        inventory.stock_reserved -= quantity
        self.db.flush()

        return inventory