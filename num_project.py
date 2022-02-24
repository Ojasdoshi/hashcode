
class Contributor:
    def __init__(self,name,no_of_skill):
        self.name = name
        self.no_of_skill = no_of_skill

        self.skills = dict()

    def add_skills(self,skill,level):
        self.skills[skill] = int(level)
        
    def has_skill(self, skill, level):
        if skill in self.skills:
            if self.skills[skill] >= level:
                return True
        return False
    

class Project:

    def __init__(self,project_name,required_days,score,best_before,roles):
        self.project_name = project_name
        self.required_days =required_days
        self.score= score
        self.best_before = best_before
        self.roles = roles
        self.active_contributors = list()
        self.require_skills = dict()

    def add_required_skills(self,skill,level):
        self.require_skills[skill]  = int(level)

    def add_contributor(self, contributor):
         self.active_contributors.append(contributor)
            
    def post_realease(self):
        for contributor in self.active_contributors:
            for skill in self.require_skills: 
                if contributor.has_skill(skill,self.require_skills[skill]):
                    self.roles[contributor] = skill
                    break
            return skill
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
                skills = contributor.skills.keys()
                for skill_key in skills:
                    if skill_key in required_skills and project.require_skills[skill_key] >= contributor.skills[skill_key]:
                        assign_project_roles[project.project_name].append(contributor.name)
        assigned_projects = len(assign_project_roles)


        print(f'{assigned_projects}')

        for project_name, roles_assign in assign_project_roles.items():
            print(f'{project_name}')
            print(' '.join(roles_assign))

def execution(projects, contributors):
    days = 0
    available_projects = sorted(projects, key=lambda prj:prj.score, reverse=True)
    projects_completed = False
    prj_execution = list()
    ans = list()
    while not projects_completed:
        released_prj, released_contri = project_release(prj_execution,days)
        contributors.extend(released_contri)
        ans.extend(released_prj)
        for prj in available_projects:
            prj_contri = list()
            for skill, level in prj.require_skills.items():
                for contributor in contributors:
                    if contributor.has_skill(skill, level) :
                        prj.add_contributor(contributor)
                        break
                prj_contri.append(contributor)
                        
                        
        days = days + 1
        
def project_release(prj_execution,current_day ):
    '''
    '''
    released_contri = list()
    released_proj = list()
    for prj, start_day in prj_execution:
        if (current_day - start_day) > prj.required_days:
            released_contri.extend(prj.active_contributors)
            released_proj.append(prj)
    
    return released_proj, released_contri
            
    

main()
