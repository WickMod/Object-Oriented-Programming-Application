from VideoSharing_DTO.School import School
from VideoSharing_Repo.SchoolRepository import SchoolRepository

class SchoolService:

    school_repo: SchoolRepository

    def __init__(self) -> None:
        self.school_repo = SchoolRepository()
    
    def get_school(self, school: School):
        existing_school = self.school_repo.get_school(school)
        return existing_school

    def school_exists(self, school: School) -> bool:
        school = self.school_repo.get_school(school)
        if school is None:
            return False
        return True
    
    def register_school(self, school: School) -> bool:
        # TODO:: Add user that created school to school when school is successfully created.
        # To comply with Single Responsibility Principle this should be called in app.py
        if self.school_exists(school):
            return False
        return self.school_repo.add_school(school)
