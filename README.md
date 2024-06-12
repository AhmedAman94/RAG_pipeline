# Retrieval Augmented Generation Pipeline Built on LangChain Framework

In this repository is a chatbot built on the open-source LangChain framework and served on both Streamlit web apps as well as an API. The models include open-source models such as Llama 3 and OpenAI's GPT-3.5 Turbo. A core component of the application is its RAG pipeline which will take files (both locally stored and from the web) and store the information in a vector store to provide more context to the model.

Below is a diagram that explains the RAG process succinctly.
[![rag explain](https://github.com/AhmedAman94/RAG_pipeline/blob/main/miscellaneous/rag_explanation.png)](#rag)

## Demo
This app, hosted via Uvicorn using the LangChain/LangServe framework, showcases the RAG pipeline using GPT-4 turbo as the LLM of choice and a dense congressional hearing as the context. The LangChain framework allows for a generic, model-agnostic framework to be utilized. This allows us to scale and add more models, features, or swap models with ease.

In the example below, the app is being called via Uvicorn and Streamlit in the command line.

[![command](https://github.com/AhmedAman94/RAG_pipeline/blob/main/miscellaneous/command.png)](#cmd)
![ui](https://github.com/AhmedAman94/RAG_pipeline/blob/main/miscellaneous/ui.png)

In the example below, the app is being interacted with by giving it queries about the document.

![answer1](https://github.com/AhmedAman94/RAG_pipeline/blob/main/miscellaneous/answer1.png)
![answer2](https://github.com/AhmedAman94/RAG_pipeline/blob/main/miscellaneous/answer2.png)

## 🚀 About Me
I leverage AI and cloud technologies to design and build scalable business and consumer-facing products and services. I work with cross-functional teams to deliver end-to-end model development and deployment, using production-grade programming and best practices.

I am deeply passionate about applying data science to solve real-world problems and create value for customers and stakeholders. I am always eager to learn new skills and technologies, and to collaborate with diverse and talented professionals. I am looking for opportunities to further grow and challenge myself as an Applied Scientist and AI Engineer.

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/AhmedAman94)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mahmedaman/)
