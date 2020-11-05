import azure.functions as func
import requests


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

        token ='1256249898:AAHLGGnPqJNdRddD-78giZJ1OS_Oh3AcYAY'
        url = f'https://api.telegram.org/bot{token}/getUpdates'

        url = f'https://api.telegram.org/bot{token}/sendMessage'
        data = {'chat_id':949196621, 'text':name}
        requests.post(url, data).json()

        return func.HttpResponse(f"Function Runned Successfully")

    else:
        return func.HttpResponse(
             "Please pass a value on the query string or in the request body",
             status_code=400
        )
