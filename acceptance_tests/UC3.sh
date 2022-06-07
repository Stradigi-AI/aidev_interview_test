curl -X POST "http://localhost:5000/model2/train"
curl -X POST "http://localhost:5000/model2/predict" \
       -H "accept: application/json" -H "Content-Type: application/json" \
       -d '{
            "data": [
                {
                    "V1": 46,
                    "V2": "Female",
                    "V3": 1.4,
                    "V4": 0.4,
                    "V5": 298,
                    "V6": 509,
                    "V7": 623,
                    "V8": 3.6,
                    "V9": 1,
                    "V10": 0.3
                },
                {
                    "V1": 39,
                    "V2": "Male",
                    "V3": 1.6,
                    "V4": 0.8,
                    "V5": 230,
                    "V6": 88,
                    "V7": 74,
                    "V8": 8,
                    "V9": 4,
                    "V10": 1,
                    "V55": 99
                }
            ]
        }'