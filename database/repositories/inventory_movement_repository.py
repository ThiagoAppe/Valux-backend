from sqlalchemy.orm import Session

from models.inventory_movements import InventoryMovement


class InventoryMovementRepository:
    def __init__(self, db: Session):
        self.db = db

    def CreateMovement(
        self,
        variant_id: int,
        movement_type: str,
        quantity: int,
        reference_type: str | None = None,
        reference_id: int | None = None
    ) -> InventoryMovement:

        movement = InventoryMovement(
            Variantid=variant_id,
            Type=movement_type,
            Quantity=quantity,
            reference_type=reference_type,
            Referenceid=reference_id
        )

        self.db.add(movement)
        self.db.flush()

        return movement

    def GetByVariantid(self, variant_id: int) -> list[InventoryMovement]:
        return self.db.query(InventoryMovement).filter(
            InventoryMovement.Variantid == variant_id
        ).all()

    def GetByReference(self, reference_type: str, reference_id: int):
        return self.db.query(InventoryMovement).filter(
            InventoryMovement.reference_type == reference_type,
            InventoryMovement.Referenceid == reference_id
        ).all()