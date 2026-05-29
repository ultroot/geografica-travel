from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn
import random
import urllib.parse

app = FastAPI(title="Geographica Travel Pricing Engine", version="1.3")

@app.get("/")
def read_root():
    return {"status": "Active", "message": "Geographica Travel API is running"}

# 1. MakeMyTrip Mock
@app.get("/api/mock/makemytrip/flights")
def get_makemytrip_flights(origin: str = "HYD", destination: str = "DXB"):
    price = random.randint(15000, 25000)
    return {
        "provider": "MakeMyTrip",
        "route": f"{origin}-{destination}",
        "price_inr": price,
        "flight_number": f"MMT-{random.randint(100, 999)}"
    }

# 2. Akbar Travels Mock
@app.get("/api/mock/akbartravels/flights")
def get_akbar_flights(origin: str = "HYD", destination: str = "DXB"):
    price = random.randint(14500, 26000)
    return {
        "provider": "Akbar Travels",
        "route": f"{origin}-{destination}",
        "price_inr": price,
        "flight_number": f"AKB-{random.randint(100, 999)}"
    }

# 3. The Aggregator Engine
@app.get("/api/search/cheapest")
def get_cheapest_flight(origin: str = "HYD", destination: str = "DXB"):
    mmt_flight = get_makemytrip_flights(origin, destination)
    akbar_flight = get_akbar_flights(origin, destination)

    if mmt_flight["price_inr"] <= akbar_flight["price_inr"]:
        cheapest = mmt_flight
    else:
        cheapest = akbar_flight

    return {
        "recommended_flight": cheapest,
        "all_results": [mmt_flight, akbar_flight]
    }

# 4. NEW: The WhatsApp Redirect Gateway
@app.get("/api/book/whatsapp")
def book_via_whatsapp(flight_number: str, price: int):
    # WhatsApp requires the country code (91) but NO '+' symbol.
    client_phone_number = "916302383231" 
    
    # 1. Draft the message
    raw_message = f"Hello Geographica! I would like to book flight {flight_number} for the guaranteed price of {price} INR."
    
    # 2. Convert spaces and characters into a URL-safe format
    encoded_message = urllib.parse.quote(raw_message)
    
    # 3. Construct the official WhatsApp API link using the variable
    whatsapp_url = f"https://wa.me/{client_phone_number}?text={encoded_message}"
    
    # 4. Force the user's browser to immediately go to that link
    return RedirectResponse(url=whatsapp_url)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)