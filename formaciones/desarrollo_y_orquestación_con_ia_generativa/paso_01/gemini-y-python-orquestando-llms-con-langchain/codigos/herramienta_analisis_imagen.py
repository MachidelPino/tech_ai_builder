from langchain_google_genai import ChatGoogleGenerativeAI
from my_models import GEMINI_FLASH
from my_keys import GEMINI_API_KEY, COHERE_API_KEY
from my_helper import encode_image
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from detalles_imagen import DetallesImagen
from langchain.tools import BaseTool
from sqlalchemy import false
import ast

class HerramientaAnalisisImagen(BaseTool):
    name: str = "HerramientaAnalisisImagen"
    description: str =  """
                        Utiliza esta herramienta siempre que te sea solicitado realizar un análisis de imagen.
                        # ENTRADAS REQUERIDAS
                        ---
                        - 'nombre_imagen' (str) : Nombre de la imagen a ser analizada con extensión JPG.
                        Ejemplo: test.jpg o test.jpeg
                        """
    return_direct: bool = False

    def _run(self, action):
        action = ast.literal_eval(action)
        camino_imagen = action.get("nombre_imagen", "")

        llmG = ChatGoogleGenerativeAI(
            api_key=GEMINI_API_KEY, # type: ignore
            model=GEMINI_FLASH
            )
        
        imagen = encode_image(f"datos/{camino_imagen}")

        pregunta = "Describe la imagen: "

        template_analisis = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
                    Asume que eres analista de imagenes. Tu principal tarea consiste en: analizar una imagen
                    para extraer las informaciones mas relevantes de manera objetiva.

                    # FORMATO DE SALIDA
                    Descripcion de la imagen: Tu descripcion de la imagen aqui.
                    Etiquetas: Una lista con 3 palabras clave separadas con comas.
                    """
                ),
                (
                    "user",
                    [
                        {
                            "type":"text",
                            "text":pregunta
                        },
                        {
                            "type":"image_url",
                            "image_url":"data:image/jpeg;base64,{imagen_informada}"
                        }
                    ]
                )
            ]
        )

        cadena_analisis = template_analisis | llmG | StrOutputParser()

        parser_json = JsonOutputParser(
            pydantic_object=DetallesImagen
        )

        template_respuesta = PromptTemplate(
            template=   """
                Genera un resumen, utilizando un lenguaje claro y objetivo, enfocado en el publico colombiano.
                La idea es que la comunicacion del resultado sea lo mas sencilla posible, priorizando los registros
                para consultas posteriores.

                #RESULTADO DE LA IMAGEN
                {respuesta_analisis_imagen}
                
                #FORMATO DE SALIDA
                {formato_salida}
                """,
                input_variables={"respuesta_analisis_imagen"}, # type: ignore
                partial_variables={"formato_salida":parser_json.get_format_instructions()}
        )

        cadena_resumen = template_respuesta | llmG | parser_json

        cadena_compuesta = (cadena_analisis | cadena_resumen) # type: ignore

        respuesta = cadena_compuesta.invoke({"imagen_informada":imagen})
        
        return respuesta