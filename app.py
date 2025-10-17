from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>GitHub DevOps Demo</title>
            <style>
                body { 
                    font-family: Arial, sans-serif; 
                    text-align: center; 
                    padding: 50px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                }
                h1 { font-size: 3em; }
                .container { 
                    background: rgba(255,255,255,0.1); 
                    padding: 30px; 
                    border-radius: 10px; 
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>GitHub DevOps 실습</h1>
                <p>Flask 애플리케이션이 성공적으로 배포되었습니다!</p>
                <p>Version: 1.0</p>
                <p>Source: GitHub</p>
            </div>
        </body>
    </html>
    '''

@app.route('/health')
def health():
    return {'status': 'healthy', 'version': '1.0'}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)
```

**Commit changes** 클릭

---

### 3-2. requirements.txt 생성

**"Add file"** → **"Create new file"**

**File name:** `requirements.txt`
```
Flask==2.3.0
gunicorn==21.2.0
