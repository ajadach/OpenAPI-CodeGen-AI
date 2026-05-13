*** Settings ***
Library    PetStore2Client
Library    PetStore2Client.Pet


*** Test Cases ***
TEST
    ${pet}=    Evaluate    {"id": 123, "name": "doggie", "photoUrls": [], "status": "available"}
    PetStore2Client.Pet.Post Add Pet    ${pet}
