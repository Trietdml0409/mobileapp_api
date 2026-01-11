#An Enum class is a special type in programming (especially in Java) used to define a fixed set of named constants. 
# It improves readability, type safety, and maintainability by replacing arbitrary values (like integers or strings) with meaningful names.
from enum import Enum
from fastapi import FastAPI


#An attribute of many model
#Particular attribute passed into the pathway
class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"



app = FastAPI()



#Path way to model /models/{models_name}
@app.get("/models/{models_name}")
#Declare a path parameter
#The path parameter are predefined
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet: #Comparing
        return {"model_name":model_name,"message":"Deep Learning FTW!"}
    if model_name.value == "lenet": #Get the actual value
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}

#Path parameters containing paths
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}