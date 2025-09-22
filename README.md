# FX Converter

## Author

**Name:** Parisasadat Kalaki  
**Student ID:** 25969686

---

## Description

This project is a **Foreign Exchange (FX) Converter** web application built with **Streamlit**.  
It allows users to:

- Convert an amount between two currencies using the latest exchange rate.
- Retrieve historical exchange rates for a specific date.
- Display the inverse conversion rate.
- Visualize the trend of exchange rates over the last 3 years in a line chart.

### Challenges faced

- Understanding how to interact with the [Frankfurter API](https://www.frankfurter.app/) and handle JSON responses.
- Managing Streamlit’s UI flow with multiple forms and buttons without causing syntax or logic errors.
- Handling cases where data may be missing (e.g., weekends or API downtime).

### Future improvements

- Add support for comparing multiple currencies at once.
- Allow users to download rate history as CSV/Excel.
- Add caching to reduce API calls and improve performance.
- Enhance UI with custom styling and interactivity.

---

## How to Setup

1. **Clone the repository**

```bash
   git clone streamlit-fx-converter
   cd dsp_at2_25969686
```

2. Create and activate a virtual environment

```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Python: 3.12.4
5. Packages:
   streamlit>=1.49.1
   pandas>=1.5.0
   requests>=2.28.0

## How to Run the Program

open the terminal in the project directory and

```bash
    streamlit run app.py
```

1. Select the source and target currencies.

2. Enter the amount you want to convert.

3. Click Get Latest Rate to view the current conversion rate, converted amount, inverse rate, and a 3-year trend chart.

4. Select a date and click Conversion Rate to view the historical rate and equivalent converted amount.

## Project Structure

```bash
project-folder/
│
├── app.py # Main Streamlit app
├── frankfurter.py # Module for handling Frankfurter API calls
├── currency.py # Utility functions (rounding, formatting, etc.)
├── api.py # Helper function for making API requests
├── requirements.txt # Project dependencies
└── README.md # Documentation (this file)
```
