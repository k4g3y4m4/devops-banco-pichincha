# devops-banco-pichincha


Banco Pichincha - DevOps Technical assessment 

EndPoint URL
http://3.21.167.85:5000/

First generate token in: http://3.21.167.85:5000/get_token

Token
2f5ae96c-b558-4c7b-a590-a501ae1c3f6c
The APIKey must be included in HTTP Headers
In our side, we will use this command to test your endPoint
curl -X POST \
-H "X-Parse-REST-API-Key: 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c" \
-H "X-JWT-KWY: ${JWT}" \
-H "Content-Type: application/json" \
-d '{ “message” : “This is a test”, “to”: “Juan Perez”, “from”: “Rita Asturia”, “timeToLifeSec” : 45 }' \
http://3.21.167.85:5000/DevOps
