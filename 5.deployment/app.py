from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Load the DictVectorizer and Logistic Regression model
with open("dv.bin", "rb") as f_in:
    dv = pickle.load(f_in)

with open("model1.bin", "rb") as f_in:
    model = pickle.load(f_in)


# Define a Pydantic model for the input data
class ClientData(BaseModel):
    job: str
    duration: int
    poutcome: str


# Initialize the FastAPI app
app = FastAPI()


# Define the prediction endpoint
@app.post("/predict")
def predict(client: ClientData):
    client_dict = client.dict()
    X = dv.transform([client_dict])
    y_pred = model.predict_proba(X)[0, 1]
    return {"subscription_probability": y_pred}


# Homepage route
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Predict Churn API!"}
