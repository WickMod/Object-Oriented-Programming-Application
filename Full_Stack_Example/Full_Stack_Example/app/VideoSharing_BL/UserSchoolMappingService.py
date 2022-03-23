from VideoSharing_DTO.School import School
from VideoSharing_Repo.SchoolRepository import SchoolRepository
from VideoSharing_DTO.User import User
from VideoSharing_Repo.UserSchoolMappingRepository import USMRepository

class USMService:

    school_repo = SchoolRepository()

    def __init__(self) -> None:
        self.USM_repo = USMRepository()
    
    def get_schools_from_user(self, user: User) -> list:
        #returns a list of DTOs
        return self.USM_repo.get_schools_from_user(user)

    def get_users_from_school(self, school: School) -> list:
        #returns a list of DTOs
        return self.USM_repo.get_users_from_school(school)


    def pair_exists(self, school_id: int, user_id: int) -> bool:
        pair = self.USM_repo.get_pair(school_id, user_id)
        if pair is None:
            return False
        return True
    
    def register_pair(self, school_id: int, user_id: int) -> bool:
        if self.pair_exists(school_id, user_id):
            return False
        return self.USM_repo.add_pair(school_id, user_id)
