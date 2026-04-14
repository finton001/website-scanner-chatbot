# Website Scanner Chatbot

A chatbot-based website security scanner that checks for missing security headers and provides educational information on web vulnerabilities.

## Features

- Scan websites for missing security headers (HSTS, CSP, X-Frame-Options, etc.)
- Interactive chatbot interface with AI-like responses
- Educational information about web security concepts
- REST API with rate limiting and API key authentication
- Real-time backend status indicator

## Setup

### Prerequisites
- Python 3.8+
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/finton001/website-scanner-chatbot.git
   cd website-scanner-chatbot
   ```

2. Install backend dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```

3. Set environment variable for API key:
   ```bash
   export API_KEY=your-secret-api-key-here
   ```

4. Run the backend server:
   ```bash
   python backend/app.py
   ```

5. Open the frontend:
   - Open `frontend/index.html` in your web browser
   - The app will connect to the backend running on `http://localhost:5000`

## Usage

- Type messages in the chat interface to scan websites or ask security questions
- Use commands like "scan example.com" to check security headers
- Ask about XSS, SQL injection, HTTPS, etc. for explanations

## API Documentation

### Health Check
```
GET /health
```
Returns: `{"status": "ok"}`

### Scan Security Headers
```
POST /scan
Headers: X-API-Key: your-api-key
Body: {"target": "example.com"}
```
Returns scan results with missing and present headers.

## Security Features

- Rate limiting: 10 requests per minute per IP
- API key authentication required for scanning
- SSL certificate validation disabled for scanning (use with caution)

## License

MIT License - see LICENSE file for details