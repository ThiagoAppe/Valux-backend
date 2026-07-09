from sqlalchemy.orm import Session

from database.models.user import User


class UserRepository:
    def __init__(self, Db: Session):
        self.Db = Db

    def GetByid(self, Userid: int) -> User | None:
        return self.Db.get(User, Userid)

    def GetByEmail(self, Email: str) -> User | None:
        return (
            self.Db.query(User)
            .filter(User.Email == Email)
            .first()
        )

    def Create(
        self,
        Email: str,
        FullName: str,
    ) -> User:
        UserEntity = User(
            Email=Email,
            FullName=FullName,
        )

        self.Db.add(UserEntity)
        self.Db.commit()
        self.Db.refresh(UserEntity)

        return UserEntity