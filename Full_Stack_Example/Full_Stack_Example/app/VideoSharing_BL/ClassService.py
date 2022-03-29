from VideoSharing_Repo.ClassRepository import ClassRepository
from VideoSharing_DTO.Class import Class
from VideoSharing_DTO.School import School
from VideoSharing_Repo.ClassRepository import ClassRepository
from VideoSharing_BL.SchoolService import SchoolService

#class variables are named _class by necessity of syntax

#To do
#->add a way to add the class and school id
#->link to create class from the school page instead of the top bar
#->improve classname.html to not be so shitty

class ClassService:

    school_svc: SchoolService
    class_repo: ClassRepository

    def __init__(self) -> None:
        self.class_repo = ClassRepository()
        self.school_svc = SchoolService()

    def register_class(self, _class: Class) -> bool:
        if self.class_exists(_class):
            return False
        return self.class_repo.add_class(_class)

    def class_exists(self, _class: Class) -> bool:
        _class = self.class_repo.get_class(_class)
        if _class is None:
            return False
        return True
        
    def get_class(self, _class: Class) -> Class:
        #honestly idk what this does it looks like it just takes a class and returns it,
        #but schoolservice.py had one so I made it
        existing_class = self.class_repo.get_class(_class)
        return existing_class

    def get_school_from_class_id(self, class_id: int) -> School:
        #stub function 
        # not sure why the squiggle 
        return self.school_svc.get_school_from_id(class_id)

    def search_for_classes(self, search_term:str) -> list:
        return self.class_repo.find_classes(search_term)