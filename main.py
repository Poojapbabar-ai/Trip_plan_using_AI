from fastapi import FastAPI
from pydantic import BaseModel
from agents.agentic_workflow import GraphBuilder
from logger.logging import logger
import os

app = FastAPI()


class QueryRequest(BaseException):
    query : str


@app.post("/query")
async def query_travel_agent(query:QueryRequest):
    #------------- Graph Builder ------------
    try:
        print(query)
        graph = GraphBuilder(model_provider  = "groq")
        react_app = graph()


        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png","wb") as f:
            f.write(png_graph)
        print(f"Graph Saved as 'my_graph.png in{os.getcwd()}")

        #Assuming request is a pydantic object like {'question':'your text'}
        messages = {"messages":[query.question]}
        output = react_app.invoke(messages)


        if isinstance(output,dict) and "message" in output:
            final_output = output["message"][-1].content #Last Api response
        else:
            final_output = str(output)

        return {"answer":final_output}
    except Exception as e:
        return JSONResponse(status_code = 500,content = {"error":str(e)})

        
