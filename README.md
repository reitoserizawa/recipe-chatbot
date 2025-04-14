<h1>Recipe Chatbot</h1>
<h2>Description</h2>
<p>An AI-integrated recipe chatbot applicattion utilizing 3rd API "Edamam API" for recipes</p>

![Screenshot 2025-04-13 at 11 05 51 PM](https://github.com/user-attachments/assets/4f5e5487-816b-43b2-b983-63e3503dac4e)

<h2>Demo</h2>

https://youtu.be/KfTZ1YASxcs

https://github.com/user-attachments/assets/841108a3-fd7d-4194-b821-cebe19c6dcdf



<h2>Features</h2>
<ul>
  <li>Utilized ChatGPT and Langchain</li>
  <li>Implemented with serverside rendering</li>
  <li>Connected to "Edamam API" to show the recipe data</li>
</ul>

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
