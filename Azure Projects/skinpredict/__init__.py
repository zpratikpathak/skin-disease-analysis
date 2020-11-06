
import azure.functions as func
import requests
import json


def main(req: func.HttpRequest) -> func.HttpResponse:

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        #url=name
        #https://i.imgur.com/cYzaOkV.jpg
        
        url="https://centralindia.api.cognitive.microsoft.com/customvision/v3.0/Prediction/82462bcc-5616-4f82-98ea-8d4fda55a9e6/classify/iterations/Iteration1/url"
        headers={'content-type':'application/json','Prediction-Key':'24ab65398bb943768ed6aea74b9a073e'}
        body={"Url": name}
        r =requests.post(url,json=body,headers=headers)

        response=r.json()

        SkinOutput=[]
        result=[]

        for prediction in response["predictions"]:
            if prediction["probability"]>0.60:
                #result=prediction["tagName"]+":"+str(prediction["probability"]*100)+"<br>"
                result=prediction["tagName"]+":"+ str(prediction["probability"]*100)+"<br>"
                SkinOutput.append(result)

        ans=" ".join(SkinOutput)

        if len(ans)>2:
            return func.HttpResponse(ans)
        else:
            return func.HttpResponse("You Don't have any Skin Disease")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a URL in the query string or in the request body for Orediction result.",
             status_code=200
        )
