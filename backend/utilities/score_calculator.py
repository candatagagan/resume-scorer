

class Score_Calculator:

    def __init__(self):
        pass

    def jd_wise_score(self, result):
        jd_dict = {}
        for key, value in result.items():
            if len(value) > 0:
                score = sum(value.values()) / len(value)
                jd_dict[key] = score
        return jd_dict


    def overall_score(self, results_experience, results_skills):
        result = {**results_experience, **results_skills}
        score = sum(result.values()) / len(result.values())
        return score
        
