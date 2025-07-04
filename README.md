# Credit Risk Analysis Dashboard

## Overview
This project is a comprehensive **Credit Risk Analysis Dashboard** built with Python and Streamlit. It provides interactive visualizations and AI-powered insights for analyzing German credit risk data, helping financial institutions make informed lending decisions.

<p align="center">
  <img src="https://primary-production-2548.up.railway.app/wp-content/uploads/2025/07/Untitled-Project-2-1.gif" alt="Credit Risk Analysis Dashboard" />
</p>


## Features

### 🎯 Core Functionality
- **Interactive Dashboard**: Real-time data filtering and visualization
- **AI-Powered Analysis**: OpenAI GPT-3.5-turbo integration for dynamic insights
- **Professional UI**: Dark theme with rounded corners and responsive design
- **8 Chart Types**: Age distribution, loan purposes, credit amounts, housing analysis, and more
- **Real-time Filtering**: Sidebar controls for loan purpose, housing type, age range, and credit amount

### 📊 Analytics Included
1. **Age Distribution by Gender** - Stacked bar chart
2. **Loan Purpose Distribution** - Interactive pie chart
3. **Credit Amount Distribution** - Histogram analysis
4. **Housing Type by Job Category** - Comparative bar chart
5. **Credit Amount by Housing Type** - Box plot analysis
6. **Duration vs Credit Amount** - Scatter plot with purpose coding
7. **Savings vs Checking Accounts** - Account relationship analysis
8. **Credit Risk Distribution** - Risk assessment visualization

### 🤖 AI Integration
- **Live Analysis**: Real-time insights using OpenAI GPT-3.5-turbo
- **Dynamic Updates**: Analysis refreshes based on filtered data
- **Professional Reports**: Structured business insights and recommendations

## Technical Stack

### Backend
- **Python 3.11+**
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **Plotly** - Interactive visualizations
- **OpenAI API** - AI-powered analysis

### Frontend
- **Dark Theme** - Professional black and off-white design
- **Responsive Layout** - Mobile-friendly interface
- **Interactive Controls** - Real-time filtering and updates

### Deployment
- **Docker** - Containerized deployment
- **Docker Compose** - Easy orchestration
- **Multi-platform** - Runs on any Docker-supported system

## Dataset
- **German Credit Data** - 1000 credit applications
- **10 Features** - Age, gender, job, housing, purpose, duration, amount, accounts
- **Preprocessing** - Automated handling of missing values and categorization

## Installation & Usage

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run streamlit_dashboard.py --server.port 8501
```

### Docker Deployment
```bash
# Build and run with Docker
docker build -t credit-risk-dashboard .
docker run -p 8501:8501 credit-risk-dashboard

# Or use Docker Compose
docker-compose up -d
```

### Access
- **Local**: http://localhost:8501
- **Features**: Interactive filtering, AI analysis, professional reporting

## Project Structure
```
Credit Risk Prediction/
├── streamlit_dashboard.py      # Main Streamlit application
├── german_credit_data.csv      # Dataset
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── docker-compose.yml          # Docker Compose setup
└── README.md                   # This file
```

## Key Files
- `streamlit_dashboard.py` - Main application with 8 interactive charts
- `german_credit_data.csv` - German credit risk dataset (1000 records)
- `requirements.txt` - Python dependencies (Streamlit, Plotly, OpenAI, etc.)
- `Dockerfile` - Container configuration for deployment
- `docker-compose.yml` - Easy deployment orchestration

## Configuration

### OpenAI API Key
The dashboard uses OpenAI GPT-3.5-turbo for AI analysis. The API key is configured in the code:
```python
os.environ['OPENAI_API_KEY'] = 'your-api-key-here'
```

### Styling
- **Dark Theme**: Professional black (#1a1a1a) and off-white (#f5f5f5) color scheme
- **Rounded Corners**: 15px border radius for modern appearance
- **Interactive Elements**: Red-coral accent color (#ff6b6b) for controls

## Business Value
- **Risk Assessment** - Identify high-risk loan applications
- **Portfolio Analysis** - Understand customer demographics
- **Decision Support** - Data-driven lending recommendations
- **Trend Analysis** - Market insights and patterns
- **Automated Reporting** - AI-generated business insights

## Screenshots
The dashboard features:
- Interactive sidebar with filters
- Real-time metrics display
- 8 professional chart visualizations
- AI-powered analysis section
- Responsive design for all devices

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test the dashboard
5. Submit a pull request

## License
This project is for educational and demonstration purposes.

---

**Built with ❤️ using Streamlit, Plotly, and OpenAI**

*Transform raw credit data into actionable business intelligence*
