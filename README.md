# Comparative Opinion Summarization Data Generator

## Introduction

This repository provides a tool for generating comparative summaries of hotel reviews using GPT-based models. The tool allows users to collect hotel reviews from various websites, prepare data, and generate comparison summaries between two hotels. It is designed to streamline the process of review collection, data preparation, and summary generation, leveraging the power of GPT to create insightful comparisons based on user reviews.

## Usage

### 1. Collecting Reviews
* Navigate to `data_collector.py`.
* Customize the `get_hotels_city` and `add_details` functions according to the structure of the website you're collecting data from. The current implementation is tailored for Eghatam24.com.
* **Note:** This script also collects extra information about hotels (e.g., addresses, average scores, stars, etc.), but the primary data needed are the hotel names and their respective reviews.

### 2. Preparing GPT Client
* Open `Main.ipynb`.
* You will need an OpenAI API key to create your GPT client.
* Build and configure your client in this notebook.

### 3. Generating Results
* In `Main.ipynb`, specify `Hotel_A` and `Hotel_B`.
* Construct the final prompt using the collected reviews for these two hotels.
* Pass the final prompt to the GPT client to generate the comparison result.
  * **Note 1:** You can customize the `initial_prompt` as per your requirement.
  * **Note 2:** Modify the `generate_prompt()` function in `gpt_functions.py` to fit the structure of your reviews.

---

Feel free to reach out for any issues or questions!

--- 
