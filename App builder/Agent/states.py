#imported field for structure of plan
from pydantic  import BaseModel, Field

class File(BaseModel):
    path:str = Field(description="Path to the file to be created or modified")
    purpose:str = Field(description="Purpose of the file , e.g. 'main application logic', 'data processing module',etc.")

#schema for defining the plan
class Plan(BaseModel):
    name: str = Field(description="Name of the App to be Built")
    description: str = Field(description="An online description of the app to be built, e.g. 'A web application for managing persononal finances'")
    techstack: str = Field(description="Techstack version of the app to be built e.g. 'python', 'Javascript' , 'react', 'flask' , etc")
    features: list[str] = Field(description= "A list of features that the app should have,e.g. 'User Authentication','Datavisualization',etc.")
   #file here is another class above which tells the purpose of the files created
    files:list[File] = Field(description= "A list of files to be created , each with a 'path' and 'purpose'")
