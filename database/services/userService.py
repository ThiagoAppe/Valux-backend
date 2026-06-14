from database.repositories.userRepository import UserRepository


class UserService:
    def __init__(
        self,
        UserRepositoryInstance: UserRepository,
    ):
        self.UserRepository = UserRepositoryInstance

    def GetUser(self, UserId: int):
        return self.UserRepository.GetById(UserId)