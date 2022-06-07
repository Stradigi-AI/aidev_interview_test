curl -X POST "http://localhost:5000/model1/train" \
       -H "accept: application/json" -H "Content-Type: application/json" \
       -d '{
            "features": [
                "V1", "V4", "V6", "V22"
            ]
        }'