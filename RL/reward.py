import Levenshtein

def reward_func(text_answer: str, text_recog: str) -> float:
    answer = text_answer.lower()
    recog = text_recog.lower()
    
    dist = Levenshtein.distance(answer, recog)
    max_len = max(len(answer), len(recog))

    similarity = 1 - (dist / max_len)
    reward = 1 - similarity

    return reward