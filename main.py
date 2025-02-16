from fastapi import FastAPI

from app.api.routes import users, auth
from app.database import reset_database, Base, engine

# Ensure database is reset before FastAPI starts (Comment out if you don't want to reset the database)
reset_database()

# Recreate tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Define JWT Security for Swagger UI
security_scheme = {
    "BearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
    }
}

# Override OpenAPI to include JWT security
_openapi_schema = None


# Since I'm dealing with the router, I need to manually force the Authorize Setup
def custom_openapi():
    global _openapi_schema
    if _openapi_schema is None:
        openapi_schema = app.openapi()
        openapi_schema["components"] = {
            "securitySchemes": {
                "BearerAuth": security_scheme["BearerAuth"]
            }
        }

        # Apply security globally
        for path in openapi_schema["paths"].values():
            for method in path.values():
                method["security"] = [{"BearerAuth": []}]

        _openapi_schema = openapi_schema  # Cache OpenAPI schema

    return _openapi_schema


# Register routes using Facade, each endpoint is prefixed with /api
# and wee need to add each of the routes to the app using app.include_router()
app.include_router(users.router, prefix="/api", tags=["Users"])
app.include_router(auth.router, prefix="/api", tags=["Authorization"])


# Root Endpoint (for demo purposes)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Bill MAP API"}
