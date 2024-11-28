# First_Twitter_Bot-2022-

## Twitter Bot: A Simple Python Automation Tool

This project contains Python scripts for interacting with the Twitter API using the `Tweepy` library. The scripts showcase basic functionalities like fetching tweets from your timeline and connecting to the Twitter API for creating or managing a Twitter bot.

Features:
1. **Fetch Tweets**:
   - Retrieve tweets from your home timeline and save them in a structured CSV format for analysis (`twitter_pi.py`).
2. **Twitter Bot Setup**:
   - Demonstrates the process of authenticating with the Twitter API and verifying credentials (`MonPremierBotTwitter.py`).
3. **Data Storage**:
   - Tweets fetched from the API are organized and saved into a CSV file for further use.


Files Included:
- `twitter_pi.py`:
   - Fetches tweets from the home timeline using Tweepy.
   - Saves tweet data (time, username, tweet text) into a CSV file for analysis.
- `MonPremierBotTwitter.py`:
   - A simple example of authenticating with the Twitter API and verifying credentials.
- `config.ini`:
   - Stores sensitive API keys and tokens securely.

How to Use:
1. Set Up Your Twitter Developer Account:
   - Register for a developer account on [Twitter Developer Portal](https://developer.twitter.com/).
   - Create an app to get your API key, secret, access token, and secret token.

2. Configure `config.ini`:
   - Add your API keys and tokens in the `config.ini` file:
     ```
     [twitter]
     api_key = YOUR_API_KEY
     api_key_secret = YOUR_API_SECRET_KEY
     access_token = YOUR_ACCESS_TOKEN
     access_token_secret = YOUR_ACCESS_SECRET_TOKEN
     ```

3. Install Dependencies**:
   - Install required Python packages:
     ```
     pip install tweepy pandas
     ```

4. Run the Scripts:
   - Execute `twitter_pi.py` to fetch tweets from your timeline and save them to `tweets.csv`.
   - Use `MonPremierBotTwitter.py` to test authentication and explore further bot functionalities.


Security Note:
- Ensure you keep your `config.ini` file secure and never expose your API keys or access tokens in public repositories.
