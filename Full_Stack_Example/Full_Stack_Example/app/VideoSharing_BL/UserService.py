from datetime import datetime
from VideoSharing_DTO.User import User
from VideoSharing_Repo.UserRepository import UserRepository
from sqlite3 import Timestamp

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
    
    def check_username_password_match(self, uname: str, pword: str) -> bool:
        cur_user = self.get_user(uname)
        #if not self.user_exists(cur_user):
        if cur_user is None:
            # The user does not exists and needs to register
            return False
        #if cur_user.Pwd == pword and cur_user.UserName == uname:
        if cur_user.UserName == uname and cur_user.Pwd == pword:
            # the entered info matches a stored pair
            return True
        else:
            # the entreed info does not match a stored pair
            return False

    def update_last_login(self, username: str)-> bool:
        new_time:Timestamp = datetime.now()
        cur_user = self.get_user(username)
        if cur_user is None:
            return False # This shouldn't ever happen, but just in case

        cur_user.LastLogin = new_time
        self.user_repo.update_login_time(cur_user)
        return True
        #get user and update time with Timestamp