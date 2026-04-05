import re
import urllib.parse

SUSPICIOUS_WORDS = [
    'login', 'verify', 'secure', 'account', 'update',
    'bank', 'confirm', 'password', 'credit', 'signin'
]

SAFE_DOMAINS = [
    'google.com', 'youtube.com', 'facebook.com',
    'microsoft.com', 'apple.com', 'github.com'
]

def extract_features(url):
    features = {}

    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc  # e.g. "paypal-secure.com"
    path = parsed.path      # e.g. "/login/verify"
    
    features['url_length'] = len(url)
    features['has_https'] = 1 if parsed.scheme == 'https' else 0
    features['has_at_symbol'] = 1 if '@' in url else 0
    features['num_dots'] = url.count('.')
    features['num_hyphens'] = url.count('-')
    features['num_slashes'] = url.count('/')
    features['has_ip'] = 1 if re.match(r'\d+\.\d+\.\d+\.\d+', domain) else 0
    features['suspicious_words'] = sum(1 for w in SUSPICIOUS_WORDS if w in url.lower())
    features['is_safe_domain'] = 1 if any(s in domain for s in SAFE_DOMAINS) else 0

    return features