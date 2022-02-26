###########################################
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
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name

class Project:

    def __init__(self,project_name,required_days,score,best_before,roles):
        self.project_name = project_name
        self.required_days = int(required_days)
        self.score= score
        self.best_before = best_before
        self.roles = roles
        self.active_contributors = dict()
        self.require_skills = dict()

    def add_required_skills(self,skill,level):
        self.require_skills[skill]  = int(level)

    def add_contributor(self, contributor, skill):
        self.active_contributors[skill] = contributor

    def is_proj_spec_satisfied(self, list_contributors):
        if len(list_contributors) == len(self.require_skills.keys()):
            for contributor, skill in list_contributors:
                self.add_contributor(contributor, skill)
        return len(list_contributors) == len(self.require_skills.keys())
            
    def post_realease(self):
        for skill,contributor in self.active_contributors.items():
            contri_skill_level = contributor.skills[skill]
            if self.require_skills[skill] == contri_skill_level:
                contri_skill_level = contri_skill_level + 1
                contributor.skills[skill] = contri_skill_level

            

        
    def __repr__(self):
        return self.project_name

def parse_inp():
    with open('input_data/b_better_start_small.in.txt') as f:
        contrib, no_of_projects = f.readline().split(' ')
        contibutors = list()
        
        for i in range(int(contrib)):
            name,no_of_skill = f.readline().split(' ')
            contrib_inst = Contributor(name,no_of_skill)
            for j in range(int(no_of_skill)):
                skill,level = f.readline().split(' ')
                contrib_inst.add_skills(skill,level)
            contibutors.append(contrib_inst)
        
        projects = list()
        for i in range(int(no_of_projects)):
            project_name,required_days,score,best_before,roles = f.readline().split(' ')
            project = Project(project_name,required_days,score,best_before,roles)
            for j in range(int(roles)):
                skill,level = f.readline().split()
                project.add_required_skills(skill,level)
            projects.append(project)
    
    return projects, contibutors

def project_completed(prj_execution, current_day):
    released_contri = list()
    released_proj = list()
    for prj, start_day in prj_execution:
        if (current_day - start_day) > prj.required_days:
            released_contri.extend([v for k, v in prj.active_contributors.items()])
            released_proj.append((prj, start_day))
            # released_proj.remove(prj)

    return released_proj, released_contri

def execution(projects, contributors):
    days = 0
    available_projects = sorted(projects, key=lambda prj:prj.score, reverse=True)
    total_proj = len(projects)
    projects_completed = False
    prj_execution = list()
    ans = list()
    while (not projects_completed) and (days < 50):
        released_prj, released_contri = project_completed(prj_execution,days)
        contributors.extend(released_contri)
        for prj, start_day in released_prj:
            prj.post_realease()
            prj_execution.remove((prj, start_day))
            ans.append(prj)
        for prj in available_projects:
            prj_contri = list()
            for skill, level in prj.require_skills.items():
                for contributor in contributors:
                    if contributor.has_skill(skill, level) :
                        # prj.add_contributor(contributor)
                        prj_contri.append((contributor, skill))
                        break

            if prj.is_proj_spec_satisfied(prj_contri):
                   prj_execution.append((prj, days))
                   available_projects.remove(prj)
                   for con, skill in prj_contri:
                       contributors.remove(con)
                    

        projects_completed = (total_proj == len(ans))
        days = days + 1

    return ans

def main():
    projects, contibutors = parse_inp()
    ans = execution(projects, contibutors)
    print(len(ans))
    for project in ans:
        print(f'{project.project_name}')
        contri = [value.name for k, value in project.active_contributors.items()]
        print(' '.join(contri))

if __name__ == "__main__":
    main()

        