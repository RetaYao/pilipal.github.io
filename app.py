from flask import Flask,json,send_file,request
from flask import Response  
app = Flask(__name__)  
  
@app.route('/api', methods=['GET'])  
def api():  
    response = {  
        "status": 200,  
        "responseType": 0,  
        "code": "000000",  
        "list": [  
            {  
                "title": "男士运动连帽开衫",  
                "tag": "X1",  
                "label": "¥298",  
                "anchor": "",  
                "thumbnail": "https://img.sobot.com/console/3041/kb/image/a877cc75f87a42df8c3de709f9e17b1b.jpeg",  
                "summary": "已发货",  
                "orderId": "1",  
                "paramsList": [  
                    {"key": "orderId", "value": "1"},  
                    {  
                        "key": "paramsList",  
                        "value": [  
                            {"key": "orderId", "value": "1"},  
                            {  
                                "key": "paramsList",  
                                "value": "[object Object]"  
                            }  
                        ]  
                    }  
                ]  
            },  
            {  
                "title": "牛仔纺英伦经典衬衫",  
                "tag": "X2",  
                "label": "¥198",  
                "anchor": "",  
                "thumbnail": "https://img.sobot.com/console/3041/kb/image/01dfebbb0c5d414aa3522a02ca1cd82e.jpeg",  
                "summary": "未发货",  
                "orderId": "2"  
            }  
        ]  
    }  
    json_response = json.dumps(response)  
    return Response(json_response, mimetype='application/json')

if __name__ == "__main__":  
    app.run(host='0.0.0.0',port=5002)