from fastapi import FastAPI
import uvicorn
import random

# Initialize the FastAPI application
app = FastAPI(title="Geographica Travel Pricing Engine", version="1.1")

@app.get("/")
def read_root():
    return {"status": "Active", "message": "Geographica Travel API is running"}

# Mock API: MakeMyTrip B2B Endpoint
@app.get("/api/mock/makemytrip/flights")
def get_makemytrip_flights(origin: str = "HYD", destination: str = "DXB"):
    # Simulating a live API response with randomized prices
    price = random.randint(15000, 25000)
    return {
        "provider": "MakeMyTrip",
        "route": f"{origin}-{destination}",
        "price_inr": price,
        "flight_number": f"MMT-{random.randint(100, 999)}"
    }

# Mock API: Akbar Travels B2B Endpoint
@app.get("/api/mock/akbartravels/flights")
def get_akbar_flights(origin: str = "HYD", destination: str = "DXB"):
    price = random.randint(14500, 26000)
    return {
        "provider": "Akbar Travels",
        "route": f"{origin}-{destination}",
        "price_inr": price,
        "flight_number": f"AKB-{random.randint(100, 999)}"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)