from VideoSharing_DTO.School import School
from VideoSharing_DTO.User import User
from VideoSharing_Repo.UserSchoolMappingRepository import USMRepository

class SchoolService:

    school_repo: SchoolRepository

    def __init__(self) -> None:
        self.USM_repo = USMRepository()
    
    def get_schools_from_user(self, user: User) -> list:
        #returns a list of DTOs
        return self.USM_repo.get_schools_from_user(user)

    def get_users_from_school(self, school: School) -> list:
        #returns a list of DTOs
        return self.USM_repo.get_users_from_school(school)


    def pair_exists(self, school: School) -> bool:
        school = self.school_repo.get_school(school)
        if school is None:
            return False
        return True
    
    def register_pair(self, school: School) -> bool:
        if self.school_exists(school):
            return False
        return self.school_repo.add_school(school)
