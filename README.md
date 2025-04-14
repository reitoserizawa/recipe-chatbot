<h1>Recipe Chatbot</h1>
<h2>Description</h2>
<p>An AI-integrated recipe chatbot applicattion utilizing 3rd API "Edamam API" for recipes</p>

![Screenshot 2025-04-13 at 11 05 51 PM](https://github.com/user-attachments/assets/4f5e5487-816b-43b2-b983-63e3503dac4e)

<h2>Live</h2>
<p>https://recipe-chatbot-434r.onrender.com/</p>

<h2>Demo</h2>

https://youtu.be/KfTZ1YASxcs

https://github.com/user-attachments/assets/841108a3-fd7d-4194-b821-cebe19c6dcdf

<h2>Features</h2>
<ul>
  <li>Utilized ChatGPT and Langchain</li>
  <li>Implemented with serverside rendering</li>
  <li>Connected to "Edamam API" to show the recipe data</li>
</ul>

<h2>Challenges</h2>
<ul>
  <li>Connecting to the 3rd party API with LLM => utilized LangChain</li>
  <li>Formatting the responses to render from the server side => added a method to structure it</li>
  <li>Adding additional features, such as adding similar recipes, utilizing the vector databases like PineCone</li>
</ul>


<h2>System Architecture Diagram</h2>

![Screenshot 2025-04-13 at 11 48 57 PM](https://github.com/user-attachments/assets/142c3b42-a383-45c0-bb83-f8bb2ca50bc4)


<h2>3rd party API</h2>
<ul>
  <li>Edamam API: https://www.edamam.com/</li>
</ul>

<h2>Tech Stacks</h2>
<ul>
  <li>Python</li>
  <li>Flask</li>
  <li>OpenAI</li>
  <li>LangChain</li>
  <li>Tailwind CSS</li>
</ul>

<h2>Set-up</h2>
<p>Create .env file with the below variables (subscriptions for Edamam API's Recipe Search API and Open AI required)</p>

```
OPENAI_API_KEY

EDAMAM_APP_ID
EDAMAM_APP_KEY
EDAMAM_URL
```


<h2>Instllation</h2>


```
pip install -r requirements.txt
flask --app app run --debug
```
