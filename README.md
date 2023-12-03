# Comparative-Opinion-Summarization-Data-Genarator

## Usage:

**1. Collecting reviews:**
  * Go to data_collector.py
  * customize get_hotels_city & add_details functions based on the structure of the website you're collecting data from. I implemented these functions based on Eghatam24.com
  * note: I collect extra hotel information, such as addresses, average scores, stars, etc. You only need the name of the hotel and its corresponding reviews.

**2. Preparing GPT client:**
  * Go to Main.ipynb
  * You need an openai API key to build your GPT client
  * build your client

**3. Generating Results:**
  * Go to Main.ipynb
  * Specify Hotel_A & Hotel_A
  * Build the final prompt based on their reviews
  * Give the final prompt to the gpt client and get the result
  * Note_1: You could customize the initial_prompt
  * Note_2: You should customize generate_prompt() in gpt_functions.py based on the structure of reviews.

Contact me for any possible issues.
