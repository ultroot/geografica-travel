from fastapi import FastAPI
import uvicorn

# Initialize the FastAPI application
app = FastAPI(title="Geographica Travel Pricing Engine", version="1.0")

# Define the root endpoint
@app.get("/")
def read_root():
    return {"status": "Active", "message": "Geographica Travel API is running"}

# Run the server on port 8000, accessible from any IP address
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)