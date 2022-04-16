from VideoSharing_DTO.Class import Class
from VideoSharing_Repo.ClassRepository import ClassRepository
from VideoSharing_DTO.User import User
from VideoSharing_Repo.UserClassMappingRepository import UCMRepository

class UCMService:

    class_repo = ClassRepository()

    def __init__(self) -> None:
        self.UCM_repo = UCMRepository()
    
    def get_classes_from_user(self, user_id: int) -> list:
        #returns a list of DTOs
        return self.UCM_repo.get_classes_from_user(user_id)

    def get_users_from_class(self, _class: Class) -> list:
        #returns a list of DTOs
        return self.UCM_repo.get_users_from_class(_class)


    def pair_exists(self, class_id: int, user_id: int) -> bool:
        pair = self.UCM_repo.get_pair(class_id, user_id)
        if pair is None:
            return False
        return True
    
    def register_pair(self, class_id: int, user_id: int) -> bool:
        if self.pair_exists(class_id, user_id):
            return False
        return self.UCM_repo.add_pair(class_id, user_id)
