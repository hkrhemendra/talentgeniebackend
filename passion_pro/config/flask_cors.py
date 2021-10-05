from flask_cors import CORS

cors = CORS(resources={
    r"/api/*": {
        "origins": "*",
        "methods": ["GET", "HEAD", "POST", "OPTIONS", "PUT", "PATCH", "DELETE"],
        "allow_headers": "*"  
    }
})



#  ["Authorization", "Content-Type"]