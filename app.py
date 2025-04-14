from flask import Flask, request, jsonify, render_template
import requests
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
import os

EDAMAM_APP_ID = os.getenv("EDAMAM_APP_ID")
EDAMAM_APP_KEY = os.getenv("EDAMAM_APP_KEY")
EDAMAM_URL = "https://api.edamam.com/api/recipes/v2"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# recipe search
def search_recipes(query):
    params = {
        "type": "public",
        "q": query,
        "app_id": EDAMAM_APP_ID,
        "app_key": EDAMAM_APP_KEY,
    }
    response = requests.get(EDAMAM_URL, params=params)
    data = response.json()
    
    if "hits" not in data:
        return "No recipes found."

    results = []
    for hit in data["hits"]:
        recipe = hit["recipe"]
        results.append({
            "label": recipe["label"],
            "url": recipe["url"],
            "ingredients": recipe["ingredientLines"]
        })
    return results

def edamam_tool_func(query):
    results = search_recipes(query)
    if isinstance(results, str):
        return results
    
    html = "<div><strong>Here are some recipes I found:</strong><ul>"
    for r in results:
        html += f"""
            <li>
                <strong>{r['label']}</strong><br />
                <a href="{r['url']}" target="_blank">View Recipe</a><br />
                <em>Ingredients:</em>
                <ul>
                    {''.join(f"<li>{ingredient}</li>" for ingredient in r['ingredients'])}
                </ul>
            </li>
        """
    html += "</ul></div>"

    return html

edamam_tool = Tool(
    name="RecipeSearch",
    func=edamam_tool_func,
    return_direct = True,
    description="Recipe search tool",
)

llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)
agent = initialize_agent(
    tools=[edamam_tool],
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("query", "")
    
    if not user_input:
        return jsonify({"error": "Query required."}), 400
    try:
        print("User Input:", user_input)
        response = agent.run(user_input)
        print("Agent Response:", response)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
