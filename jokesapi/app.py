from fastapi import FastAPI, HTTPException
import requests
from sqlalchemy.orm import Session
from models import Joke, Base
from database import SessionLocal, engine

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# External API URL
JOKE_API_URL = "https://v2.jokeapi.dev/joke/Any"

@app.get("/fetch-jokes/")
def fetch_and_store_jokes():
    session = SessionLocal()
    total_jokes_to_fetch = 100
    max_jokes_per_request = 10
    jokes_fetched = 0
    jokes_to_store = []

    try:
        while jokes_fetched < total_jokes_to_fetch:
            # Calculate how many jokes to request (max 10 per API call)
            jokes_remaining = total_jokes_to_fetch - jokes_fetched
            jokes_to_request = min(jokes_remaining, max_jokes_per_request)

            # Make the API call to fetch jokes
            response = requests.get(JOKE_API_URL, params={"amount": jokes_to_request})
            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail="Failed to fetch jokes from external API")
            
            jokes_data = response.json()

            # Process the jokes and add to the list
            for joke in jokes_data.get('jokes', []):
                if joke["type"] == "single":
                    joke_record = Joke(
                        category=joke["category"],
                        type=joke["type"],
                        joke=joke["joke"],
                        flags_nsfw=joke["flags"]["nsfw"],
                        flags_political=joke["flags"]["political"],
                        flags_sexist=joke["flags"]["sexist"],
                        safe=joke["safe"],
                        lang=joke["lang"]
                    )
                else:
                    joke_record = Joke(
                        category=joke["category"],
                        type=joke["type"],
                        setup=joke["setup"],
                        delivery=joke["delivery"],
                        flags_nsfw=joke["flags"]["nsfw"],
                        flags_political=joke["flags"]["political"],
                        flags_sexist=joke["flags"]["sexist"],
                        safe=joke["safe"],
                        lang=joke["lang"]
                    )
                
                jokes_to_store.append(joke_record)

            # Increment the jokes fetched count
            jokes_fetched += jokes_to_request

        # Store all jokes in the database
        session.bulk_save_objects(jokes_to_store)
        session.commit()
        
        return {"message": f"{jokes_fetched} jokes fetched and stored successfully!"}
    
    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while storing jokes")
    
    finally:
        session.close()
