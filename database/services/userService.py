from database.repositories.userRepository import UserRepository


class UserService:
    def __init__(
        self,
        UserRepositoryInstance: UserRepository,
    ):
        self.UserRepository = UserRepositoryInstance

    def GetUser(self, Userid: int):
        return self.UserRepository.GetByid(Userid)