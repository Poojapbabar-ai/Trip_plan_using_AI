from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from agents.agentic_workflow import GraphBuilder
# from logger.logging import logger
import requests
import os
app = FastAPI()


class QueryRequest(BaseModel):
    question: str


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
        messages = {"messages": [query.question]}
        output = react_app.invoke(messages)


        if isinstance(output, dict) and "messages" in output:
            final_output = next(
                (
                    message.content
                    for message in reversed(output["messages"])
                    if getattr(message, "content", None)
                    and not getattr(message, "tool_calls", None)
                ),
                "No answer was returned by the travel agent.",
            )
        else:
            final_output = str(output)

        return {"answer":final_output}
    except Exception as e:
        return JSONResponse(status_code = 500,content = {"error":str(e)})

        
