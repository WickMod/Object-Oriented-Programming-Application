from VideoSharing_DTO.User import User
from VideoSharing_Repo.UserRepository import UserRepository

class UserService:

    user_repo: UserRepository

    def __init__(self) -> None:
        self.user_repo = UserRepository()

    def get_user(self,username: str) -> User:
        return self.user_repo.get_user(username)

    def user_exists(self, user: User) -> bool:
        usr = self.get_user(user.UserName)
        if usr is None:
            return False
        return True

    def register(self, user: User) -> bool:
        if self.user_exists(user):
            return False
        return self.user_repo.add_user(user)