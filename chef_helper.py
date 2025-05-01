from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents.agent_types import AgentType
from langchain.agents import initialize_agent, load_tools
from secret_key import GEMINI_API_KEY, SERPAPI_API_KEY
import os

# Set up environment variables for API keys
os.environ['GEMINI_API_KEY'] = GEMINI_API_KEY
os.environ['SERPAPI_API_KEY'] = SERPAPI_API_KEY

llm = ChatGoogleGenerativeAI(temperature=0.5, model="gemini-1.5-pro", api_key=os.environ["GEMINI_API_KEY"])

def generate_dish_ingredients_list(cuisine, dish_name):
    prompt = PromptTemplate(
        input_variables=["dish_name", "cuisine"],
        template="""I want to make {dish_name} from {cuisine} cuisine. Suggest the ingredients as a comma-separated string (only ingredient names, no quantities)."""
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(dish_name=dish_name, cuisine=cuisine)
    return [item.strip() for item in response.split(",")]

def generate_recipe_info_and_other_details(recipe_name, selected_items, location):
    # Step-by-step recipe
    procedure_prompt = PromptTemplate(
        input_variables=["recipe_name"],
        template="""Give me the step-by-step recipe for {recipe_name}. Include ingredients with quantities, cooking time, and instructions."""
    )
    recipe_chain = LLMChain(llm=llm, prompt=procedure_prompt)
    recipe_details = recipe_chain.run(recipe_name=recipe_name)

    # Shopping assistance
    tools = load_tools(["wikipedia", "llm-math", "serpapi"], llm=llm)

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False
    )

    query = f"""Find 3 grocery stores near {location} that sell {", ".join(selected_items)}. 
    For each shop, include only: Shop name, Distance in km, Rating out of 5 stars, and Estimated Price for these items. in a table format."""
    
    shop_details = agent.run(query)
  

    return recipe_details, shop_details
