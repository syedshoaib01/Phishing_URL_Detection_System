# 🛡️ Phishing URL Detection System

A machine learning-powered web application and browser extension that detects phishing URLs in real time.

---

## 🔍 What it does

You give it a URL — it tells you if it's **Safe** or **Phishing**.

The system extracts 9 structural features directly from the URL string (no website visits required) and passes them to a trained Random Forest model that returns a verdict with a confidence score.

---

## 🏗️ Project Structure
Phishing_Detector/
│
├── detector/
│   ├── analyzer.py       # Feature extractor (YOU wrote this)
│   ├── views.py          # Django API + home view
│   ├── urls.py           # URL routing
│   └── templates/
│       └── detector/
│           └── index.html
│
├── phishing_dectector/
│   ├── settings.py
│   └── urls.py
│
├── train.py              # Model trainer (YOU wrote this)
├── model.pkl             # Saved trained model
├── dataset_phishing.csv  # Kaggle dataset
└── manage.py

---

## ⚙️ How it works

1. `analyzer.py` converts any URL into 9 numerical features:
   - URL length
   - Has HTTPS?
   - Has `@` symbol?
   - Number of dots
   - Number of hyphens
   - Number of slashes
   - Is IP address?
   - Suspicious keywords (`login`, `verify`, `bank`, etc.)
   - Is known safe domain?

2. A **Random Forest Classifier** (100 trees) trained on 11,430 labeled URLs from Kaggle predicts: **phishing or legitimate**

3. Django serves the model as a REST API at `/api/detect/`

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Dataset | Web Page Phishing Detection Dataset (Kaggle) |
| Total URLs | 11,430 (balanced 50/50) |
| Algorithm | Random Forest (100 estimators) |
| Train/Test Split | 80% / 20% |
| Accuracy | **75.07%** |

> The model uses only URL-string features (no network calls), making it fast and privacy-preserving. The accuracy tradeoff vs. network-based systems is intentional.

---

## 🚀 How to run
```bash
# 1. Clone the repo
git clone https://github.com/syedshoaib01/Phishing_Detector.git
cd Phishing_Detector

# 2. Activate virtual environment
.\env_1\Scripts\activate

# 3. Install dependencies
pip install django scikit-learn pandas

# 4. Train the model (only needed once)
python train.py

# 5. Run the server
python manage.py runserver
```

Then open **http://127.0.0.1:8000/** in your browser.

---

## 🔌 API Usage

**Endpoint:** `POST /api/detect/`

**Request:**
```json
{
  "url": "http://paypal-secure-login-verify.com/account"
}
```

**Response:**
```json
{
  "url": "http://paypal-secure-login-verify.com/account",
  "is_phishing": true,
  "confidence": 87.5,
  "verdict": "Phishing Detected"
}
```

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **ML:** scikit-learn (Random Forest), pandas
- **Frontend:** HTML, JavaScript (Fetch API)
- **IDE:** Google Antigravity
- **Dataset:** Kaggle — Web Page Phishing Detection Dataset

---

## 👥 Team

**NullPointers** — Shadan College of Engineering & Technology

| Name | Roll Number |
|------|-------------|
| Syed Shoaib Ali | 24081A05B8 |
| Mohd Khaja Moinuddin Siddiqui | 24081A0574 |

---

## 📄 License

This project is for academic purposes only.
