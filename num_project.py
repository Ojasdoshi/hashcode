
class Contributor:
    def __init__(self,name,no_of_skill):
        self.name = name
        self.no_of_skill = no_of_skill

        self.Skill = dict()

    def add_skills(self,skill,level):
        self.Skill[skill] = level

class Project:

    def __init__(self,project_name,required_days,score,best_before,roles):
        self.project_name = project_name
        self.required_days =required_days
        self.score= score
        self.best_before = best_before
        self.roles = roles

        self.require_skills = dict()

    def add_required_skills(self,skill,level):
        self.require_skills[skill]  = level

def main():

    with open('input_data/a_an_example.in.txt') as f:
        contrib, no_of_projects = f.readline().split(' ')
        contibutors = list()
        
        for i in range(int(contrib)):
            name,no_of_skill = f.readline().split(' ')
            contrib_cls = Contributor(name,no_of_skill)
            for j in range(int(no_of_skill)):
                skill,level = f.readline().split(' ')
                contrib_cls.add_skills(skill,level)
            contibutors.append(contrib_cls)
        
        projects = list()
        for i in range(int(no_of_projects)):
            project_name,required_days,score,best_before,roles = f.readline().split(' ')
            project = Project(project_name,required_days,score,best_before,roles)
            for j in range(int(roles)):
                skill,level = f.readline().split()
                project.add_required_skills(skill,level)
            projects.append(project)
        
        assign_project_roles = dict()
        for project in projects:
            required_skills  = project.require_skills.keys()
            assign_project_roles[project.project_name] = list()
            for contributor in contibutors:
                skills = contributor.Skill.keys()
                print(required_skills)
                print(skills)
                if skills in required_skills:
                    assign_project_roles[project.project_name].append(contributor.name)
        assigned_projects = len(assign_project_roles)
        print(f'{assigned_projects}')

        for project_name, roles_assign in assign_project_roles.items():
            print(f'{project_name}')
            print('\n'.join(roles_assign))

main()