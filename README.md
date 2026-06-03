# StartupScope AI

A Streamlit-based application that analyzes startup ideas like an experienced VC investor would, providing detailed feedback on viability, risks, and recommendations.

## Features

- **Startup Scorecard**: Rates ideas on novelty, market potential, competition risk, monetization potential, and technical difficulty (1-10 scale)
- **Investor Perspective**: Summarizes what venture capitalists would like and worry about
- **Risk Analysis**: Identifies the top 3 risks for the startup idea
- **MVP Recommendations**: Suggests what the Minimum Viable Product should include
- **Competitive Landscape**: Identifies similar existing startups in the market
- **Final Verdict**: Provides a GO/PIVOT/SKIP recommendation

## Tech Stack

- **Frontend**: Streamlit
- **LLM Integration**: LangChain with OpenAI (GPT-5.1)
- **Language**: Python 3.12+

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Running the Application

Start the Streamlit app:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## Usage

1. Enter your startup idea in the text area
2. Specify your target customers
3. Select the revenue model (Subscription, Marketplace, Ads, SaaS, Freemium, or Other)
4. Click "Analyze Startup" to get the AI-powered analysis

## Project Structure

- `app.py` - Streamlit frontend application
- `chains.py` - LangChain integration and startup analysis chain
- `prompts.py` - AI prompt template for startup analysis
- `main.py` - Entry point (simple demo)
- `requirements.txt` - Python dependencies
- `pyproject.toml` - Project metadata

## Requirements

- OpenAI API key with access to GPT-5.1
- Python 3.12 or higher
- See `requirements.txt` for full list of dependencies

## License

This project is part of the HuggingFace startup scope initiative.
