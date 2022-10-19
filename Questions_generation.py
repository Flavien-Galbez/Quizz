

class Question :

    type_question_posibility={"number","unique_choice","multiple_choice","free_answers"}

    def __init__(self,question_type,title,solution,answers=None,id=-1,range=None,point=1):
        self.id=id #id de la question
        self.question_type=question_type #type de la question
        self.title=title#intitulé de la question
        if isinstance(answers,list) :
            self.range=len(answers) #en cas de choix, le nombre de solution
        else :
            self.range=range #en cas de number, l'interval de nombre
        self.answers=answers #listes des reponses possible (non utilise pour free_answers et number)
        self.solution=solution #bonne(s) reponse(s)
        self.point=point #bareme de la question

    def verif_error(self):
        match self.question_type :
            case "number" :
                if not isinstance(self.solution,int):
                    raise Exception("Le type de la question est nombre mais la reponse n'est pas un nombre")
                if not isinstance(self.range,list) :
                    raise Exception("La plage de nombre n'est pas valide")
                else :
                    if len(self.range)!=2 or not isinstance(self.range[0],int) or not isinstance(self.range[1],int):
                        raise Exception("La plage de nombre n'est pas valide")
                    else :
                        if self.range[0]>self.range[1] or self.solution<self.range[0] or self.solution>self.range[1] :
                            raise Exception("La solution n'est pas comprise dans la plage")
                    return True
            case "unique_choice" :
                if not isinstance(self.answers,list):
                    raise Exception("Le type de la question est choix unique mais la reponse n'est pas adaptee")
                if not isinstance(self.solution,list):
                    raise Exception("Le type de la question est choix unique mais la reponse n'est pas adaptee")
                else :
                    if len(self.solution)!=1 :
                        raise Exception("La solution n'est pas unique")
                    else :
                        if self.solution[0] not in self.answers :
                            raise Exception("La solution n'est pas dans les reponses")    
                if not isinstance(self.range,int) and self.range!=len(self.answers):
                    raise Exception("La plage de nombre n'est pas valide")
                return True
            case "multiple_choice" :
                if not isinstance(self.answers,list):
                    raise Exception("Le type de la question est choix multiple mais la reponse n'est pas adaptee")
                if not isinstance(self.solution,list):
                    raise Exception("Le type de la question est choix multiple mais la reponse n'est pas adaptee")
                else :
                    if len(self.solution)!=self.range :
                        raise Exception("Le nombre de solution attendu ne correspond pas")
                    else :
                        for s in self.solution : 
                            if s not in self.answers : 
                                raise Exception("La solution n'est pas dans les reponses")
                if not isinstance(self.range,int) and self.range!=len(self.answers):
                    raise Exception("La plage de nombre n'est pas valide")
                return True
            case "free_answers" :
                if not isinstance(self.solution,list):
                    raise Exception("Le type de la question est reponse libre mais la reponse n'est pas adaptee")
                return True
            case _ :
                raise Exception ("Type de question inconnu")
    
    def score(self,user_answers):
        match self.question_type :
            case "number":
                if self.solution == user_answers :
                    return (1 * self.score)
                else :
                    return 0
            case "unique_choice" :
                if self.solution[0]==user_answers[0]:
                    return (1 * self.score)
                else :
                    return 0
            case "multiple_choice" :
                temp_score = 0
                for a in user_answers:
                    if a in self.solution:
                        temp_score+=1
                return((temp_score/len(self.solution))*self.score)
            case "free_answers" :
                if user_answers in self.solution :
                    return (1 * self.score)
                else :
                    return 0
            case _ :
                raise Exception ("Type de question inconnu")