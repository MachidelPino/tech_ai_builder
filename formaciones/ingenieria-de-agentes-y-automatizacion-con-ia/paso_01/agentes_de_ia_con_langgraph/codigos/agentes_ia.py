# %pip install -U langchain
# %pip install -U langgraph
# %pip install -U google-generativeai
# %pip install -U langchain-google-genai
# %pip install -U langchain-community
# %pip install arxiv

"Esta es una copia del codigo trabajado en Google Colab"

import os
import google.generativeai as genai
from google.colab import userdata

api_key = userdata.get("GEMINI_API_KEY")
os.environ["GOOGLE_API_KEY"] = api_key
genai.configure(api_key=api_key)

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_core.prompts import PromptTemplate

modelo_de_prompt = PromptTemplate(
    template="Explica de manera clara y actualizada cuáles son los impactos de la inteligencia artificial en el área de {tema}.",
    input_variables=["tema"],
)

from langchain_core.output_parsers import StrOutputParser

cadena = modelo_de_prompt | llm | StrOutputParser()

respuesta = cadena.invoke({"tema": "educación"})

print(respuesta)

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
import os

os.environ["TAVILY_API_KEY"] = userdata.get("tavily")

@tool
def busca_web(query: str) -> list:
  """Realiza una búsqueda en la web sobre un tema específico"""

  tavily_search = TavilySearchResults(
      max_results=2,
      search_depth="advanced",
      max_tokens=1000
  )
  resultado_busca = tavily_search.invoke(query)
  return resultado_busca

busca_web.invoke("impacto de la inteligencia artificial en la educación")

tools = [busca_web]

llm_con_herramienta = llm.bind(tools=tools)

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

modelo_de_prompt = PromptTemplate(
    template="Usando solo las tools disponibles, dime cuáles son los impactos de la inteligencia artificial en el área de {tema}.",
    input_variables=["tema"],
)

cadena = modelo_de_prompt | llm_con_herramienta | StrOutputParser()

respuesta =  cadena.invoke({"tema": "educación"})

respuesta

prompt = "Usando solo las tools disponibles, dime cuáles son los impactos de la inteligencia artificial en el área de {tema}."

respuesta = llm_con_herramienta.invoke(prompt)

print(respuesta)

from langgraph.prebuilt import create_react_agent

system_prompt = """
Actúa como un asistente útil y especializado en investigación.
Utiliza las herramientas proporcionadas para responder a las preguntas del usuario.

Herramientas disponibles:
- busca_web: realiza búsquedas en la web y devuelve enlaces y resúmenes.

Siempre que el usuario pregunte sobre un tema específico:
1. Usa la herramienta busca_web.
2. Analiza los resultados.
3. Devuelve una respuesta clara.
4. Incluye los enlaces de las fuentes utilizadas.
"""

agente_web = create_react_agent(
    model=llm,
    tools=tools,
    prompt=system_prompt
)

resultado = agente_web.invoke({
    "messages": [
        ("user", "Cuáles son los impactos de la inteligencia artificial en la educación?")
    ]
})

resultado

resultado["messages"][-1]

from langchain_community.tools.arxiv.tool import ArxivQueryRun

tool_cientifica = ArxivQueryRun()

system_prompt2 = """
Actúa como un asistente útil.
Usa las herramientas proporcionadas para responder a las preguntas del usuario.

- tool_cientifica: Retorna resultados de una búsqueda en arXiv.

Cuando el usuario pregunte sobre un tema específico, usa tool_cientifica y devuelve los títulos de los artículos.
"""

agente_cientifico = create_react_agent(
    model=llm,
    tools=[tool_cientifica],
    prompt=system_prompt2
)

resultado = agente_cientifico.invoke({
    "messages": [
        ("user", "AI impact in education")
    ]
})

resultado

from typing import TypedDict

class AgentState(TypedDict):
    user_query: str
    web_answer: str
    scientific_answer: str
    final_answer: str

def funcion_agente_web(state: AgentState) -> dict:
    """
    Función que ejecuta un agente al estilo ReAct que realiza una búsqueda en la web
    sobre un término específico.
    """

    system_prompt = """
    Actúa como un asistente útil.
    Usa las herramientas proporcionadas para responder a las preguntas del usuario.

    - busca_web: Retorna resultados de búsqueda web.

    Cuando el usuario pregunte sobre un tema específico, usa busca_web y devuelve enlaces en la respuesta.
    """

    agente_web = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt
    )

    resultado = agente_web.invoke({
        "messages": [("user", state["user_query"])]
    })

    respuesta_final = resultado["messages"][-1].content
    return {"web_answer": respuesta_final}

def funcion_agente_cientifico(state: AgentState) -> dict:
    """
    Función que ejecuta un agente al estilo ReAct que realiza una búsqueda en arXiv
    sobre un término específico.
    """

    system_prompt = """
    Actúa como un asistente útil.
    Usa las herramientas proporcionadas para responder a las preguntas del usuario.

    - tool_cientifica: Retorna resultados de una búsqueda en arXiv.

    Cuando el usuario pregunte sobre un tema específico, usa tool_cientifica y devuelve los títulos de los artículos.
    """

    agente_cientifico = create_react_agent(
        model=llm,
        tools=[tool_cientifica],
        prompt=system_prompt
    )

    resultado = agente_cientifico.invoke({
        "messages": [("user", state["user_query"])]
    })

    respuesta_final = resultado["messages"][-1].content
    return {"scientific_answer": respuesta_final}

from langgraph.graph import START, StateGraph, END

workflow = StateGraph(AgentState)

workflow.add_node("agente_web", funcion_agente_web)
workflow.add_edge(START, "agente_web")
workflow.add_edge("agente_web", END)

app = workflow.compile()

from IPython.display import Image, display

Image(app.get_graph().draw_mermaid_png())

resultado = app.invoke({"user_query": "Cuál es el impacto de la IA en la medicina"})

print(resultado["web_answer"])

def supervisor_node(state: AgentState) -> dict:
  """
  Combina los resultados de los agentes web y cientificos y formatea la respuesta final.

  Args:
    state (AgentState): El estado actual del agente, que contiene web_answer y scientific_answer.
  Returns:
    dict: Un diccionario que contiene la respuesta final combinada y formateada.
  """

  web_results = state.get("web_answer", "No se realizó búsqueda web.")
  scientific_results = state.get("scientific_answer", "No se realizó búsqueda científica.")

  final_answer = '## Resultados combinados de búsqueda\n\n'
  final_answer += '### Resultados desde la Web\n\n' + web_results + '\n\n'
  final_answer += '### Artículos científicos (arXiv)\n\n' + scientific_results

  return {"final_answer": final_answer}

workflow = StateGraph(AgentState)

workflow.add_node("web_search", funcion_agente_web)
workflow.add_node("scientific_search", funcion_agente_cientifico)
workflow.add_node("supervisor", supervisor_node)

workflow.add_edge(START, "web_search")
workflow.add_edge("web_search", "scientific_search")
workflow.add_edge("scientific_search", "supervisor")
workflow.add_edge("supervisor", END)

app = workflow.compile()

Image(app.get_graph().draw_mermaid_png())

resultado = app.invoke({"user_query": "Cuál el impacto de la IA en la medicina?"})
print(resultado["final_answer"])

def router_agent(state: AgentState) -> dict:

  router_prompt = """
  Eres un agente ruteador. Tu tarea es decidir cuál agente es más apropiado
  para responder la pregunta del usuario.

  Pregunta del usuario: {user_query}

  Puedes elegir entre las siguientes opciones:
  - web_search: Usa esta opción si la pregunta requiere una búsqueda general en internet.
  - scientific_search: Usa esta opción si la pregunta requiere artículos científicos.

  Responde ÚNICAMENTE con el nombre de la opción (web_search o scientific_search).
  """

  router_agent_instance = create_react_agent(
      model=llm,
      tools=[],
      prompt=router_prompt
  )

  response = router_agent_instance.invoke({
      "messages": [("user", state["user_query"])]
  })

  decision = response["messages"][-1].content.strip().lower()

  if decision == "web_search":
      return {"router_decision": "web_search"}
  elif decision == "scientific_search":
      return {"router_decision": "scientific_search"}

  # Por defecto, usamos web_search
  return {"router_decision": "web_search"}

workflow = StateGraph(AgentState)

workflow.add_node("router", router_agent)
workflow.add_node("web_search", funcion_agente_web)
workflow.add_node("scientific_search", funcion_agente_cientifico)
workflow.add_node("supervisor", supervisor_node)

workflow.add_edge(START, "router")
workflow.add_conditional_edges(
    "router",
    lambda state: state["router_decision"],
    {
        "web_search": "web_search",
        "scientific_search": "scientific_search",
    }
)
workflow.add_edge("web_search", "supervisor")
workflow.add_edge("scientific_search", "supervisor")
workflow.add_edge("supervisor", END)

app = workflow.compile()

Image(app.get_graph().draw_mermaid_png())

resultado = app.invoke({
    "user_query": "Cuál es el impacto de la IA en la Educación? Usa solo fuentes web"
})
print(resultado["final_answer"])

resultado = app.invoke({
    "user_query": "Cuál es el impacto de la IA en la educación? Usa solo fuentes cientificas"
})

print(resultado["final_answer"])

import gradio as gr

def run_graph(user_query):
  """Ejecuta el LangGraph con la pregunta del usuario y devulve la respuesta final."""

  result = app.invoke({"user_query": user_query})
  return result["final_answer"]

iface = gr.Interface(
    fn=run_graph,
    inputs=gr.Textbox(label="Escribe tu pregunta:"),
    outputs=gr.Markdown(label="Respuesta final"),
    title="Agente de Búsqueda Inteligente",
    description="Haz una pregunta y obtén una respuesta usando fuentes web o científicas."
)

iface.launch()