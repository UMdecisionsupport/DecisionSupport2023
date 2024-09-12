import uvicorn, datetime
import fastapi
from starlette.exceptions import HTTPException
from starlette.responses import RedirectResponse
from pathlib import Path

app = fastapi.FastAPI()

learningobj_mapping = {
    # "281": "DecisionAgents",
    "374": "Logic",
    "375": "Probability",
    "376": "GraphicalModels",
    "377": "DecisionTheory",
    "378": "GameTheory",
    "379": "HMMs",
    "380": "MDPs",
    "381": "RL"
}


rating_mapping = {
    1: "Beginner.md",
    2: "Medium.md",
    3: "Advanced.md",
}

#@app.get("/get_exercise")
#async def get_recommendation(crsid: str, learningobj: str, page: str, perceived_difficulty: str, user: str):
# i.e. localhost:8000/get_exercise?crsid=1405209&learningobj=282&page=2&perceived_difficulty=2&user=1
#    return fastapi.responses.FileResponse(path/"index.html")


@app.get("/getrecommendation")
async def get_recommendation(crsid: str, learningobj: str, rating: int):
# i.e. localhost:8000/getrecommendation?crsid=1405209&learningobj=282&rating=2
    # Exception Handling
    if not rating or rating not in rating_mapping:
        raise HTTPException(status_code=400, detail="Invalid rating or missing")
    
    if not learningobj or learningobj not in learningobj_mapping:
        raise HTTPException(status_code=400, detail="Invalid learning objective or missing")

    if not crsid or crsid != "1405209":
        raise HTTPException(status_code=400, detail="Invalid crsid or missing")

    # log the request with timestamp to a file
    with open("reccomendation_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} {crsid} {learningobj} {rating}\n")

    # Redirect to the correct page
    base_url = "https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main"
    url = f"{base_url}/{learningobj_mapping[learningobj]}/{rating_mapping[rating]}"

    return RedirectResponse(url=url)

if __name__ == "__main__":
    # change to 0.0.0.0 to make available outside localhost
    # change to localhost to run locally
    path = Path(__file__).parent
    uvicorn.run(app, host="localhost", port=8000)
