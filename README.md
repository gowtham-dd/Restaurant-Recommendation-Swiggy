
# 🍽️ Restaurant Recommendation System

A smart, fast, and user-friendly Streamlit app that recommends restaurants based on city, cuisine, rating, and cost preferences. Built using machine learning and real restaurant data.

## 🔍 Features
- **📍 City-based filtering** (e.g., New York, Bangalore, London)
- **🍕 Cuisine selection** (Italian, Indian, Chinese, etc.)
- **⭐ Rating filter** (1-5 stars)
- **💰 Budget slider** 
- **🚀 Fast recommendations** using Cosine Similarity
- **📱 Mobile-friendly** Streamlit interface

## ⚙️ Tech Stack
| Component          | Technology       |
|--------------------|------------------|
| Frontend           | Streamlit        |
| Backend            | Python           |
| Data Processing    | Pandas, NumPy    |
| Machine Learning   | Scikit-learn     |
| Deployment         | Streamlit Cloud  |

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation
```bash
# Clone repository
git clone https://github.com/gowtham-dd/Restaurant-Recommendation-Swiggy.git
cd restaurant-recommender

# Install dependencies
pip install -r requirements.txt
```

### Run Locally
```bash
streamlit run app.py
```

## 🧠 How It Works
1. **Data Processing**:
   - OneHotEncoding for categorical features (city, cuisine)
   - StandardScaler for numerical features (rating, cost)

2. **Recommendation Engine**:
   ```python
   # Cosine Similarity Calculation
   similarities = cosine_similarity(user_profile, restaurant_features)
   top_matches = argsort(similarities)[-5:]
   ```

## 📁 Project Structure
```
restaurant-recommender/
├── app.py                # Streamlit application
├── recommender.py        # Core recommendation logic
├── data_processing.py    # Cleaning and encoding
├── requirements.txt      # Dependencies
└── assets/               # Images/sample data
```

## 📊 Sample Data Format
| name       | city     | cuisine   | rating | cost | link          |
|------------|----------|-----------|--------|------|---------------|
| Cafe Paris | New York | French    | 4.5    | 50   | swiggy.com/123|

## 🤝 Contributing
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

