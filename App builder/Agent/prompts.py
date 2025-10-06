def planner_prompt(user_prompt: str)-> str:
    PLANNER_PROMPT = f"""
            You are the PLANNER agent. Convert the user prompt into a COMPLETE Engineering project plan
            
            User request:{user_prompt}
       """
    return PLANNER_PROMPT