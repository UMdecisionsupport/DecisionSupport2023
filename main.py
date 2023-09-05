import uvicorn
from fastapi import FastAPI
from starlette.exceptions import HTTPException
from starlette.responses import RedirectResponse

app = FastAPI()

learningobj_mapping = {
    # "281": "DecisionAgents",
    "282": "Logic",
    "283": "Probability",
    "284": "GraphicalModels",
    "285": "DecisionTheory",
    "286": "GameTheory",
    "289": "HMMs",
    "290": "MDPs",
    "287": "RL"
}


rating_mapping = {
    1: "Beginner.md",
    2: "Medium.md",
    3: "Advanced.md",
}


# https://EURE.URL.DE/getrecommendation?crsid=12345&learningobj=54321&rating=2
@app.get("/getrecommendation")
async def get_recommendation(crsid: str, learningobj: str, rating: int):

    # Exception Handling
    if not rating or rating not in rating_mapping:
        raise HTTPException(status_code=400, detail="Invalid rating or missing")
    
    if not learningobj or learningobj not in learningobj_mapping:
        raise HTTPException(status_code=400, detail="Invalid learning objective or missing")

    if not crsid or crsid != "12345":
        raise HTTPException(status_code=400, detail="Invalid crsid or missing")

    # Redirect to the correct page
    base_url = "https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main"
    url = f"{base_url}/{learningobj_mapping[learningobj]}/{rating_mapping[rating]}"

    return RedirectResponse(url=url)

if __name__ == "__main__":
    # change to 0.0.0.0 to make available outside localhost
    uvicorn.run(app, host="0.0.0.0", port=8000)