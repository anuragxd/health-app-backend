from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)

def generate_diet_plan(data):

    prompt = f"""
    You are a certified nutritionist.

    Create a daily meal plan.

    User information:

    Goal: {data['goal']}
    Current Weight: {data['current_weight']}
    Target Weight: {data['target_weight']}
    Daily Calorie Target: {data['daily_calorie_target']}
    Average Steps: {data['steps_avg']}

    Provide:

    Breakfast
    Lunch
    Dinner
    Snacks

    Keep calories close to target.
    """

    response = llm.invoke(prompt)

    return response.content