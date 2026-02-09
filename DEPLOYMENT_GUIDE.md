# Deployment Guide

## Quick Start - Local Development

The application is currently running at:
- **Local URL**: http://127.0.0.1:5000
- **Network URL**: http://192.168.0.100:5000

### Running Locally

```bash
# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows

# Run the application
python app.py

# Visit http://localhost:5000 in your browser
```

## Production Deployment Options

### Option 1: Heroku Deployment

1. **Install Heroku CLI**
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku
   
   # Or download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku App**
   ```bash
   heroku create your-portfolio-name
   ```

4. **Deploy**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push heroku main
   ```

5. **Open Your App**
   ```bash
   heroku open
   ```

### Option 2: DigitalOcean App Platform

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin your-github-repo-url
   git push -u origin main
   ```

2. **Deploy on DigitalOcean**
   - Go to https://cloud.digitalocean.com/apps
   - Click "Create App"
   - Connect your GitHub repository
   - Select the repository and branch
   - DigitalOcean will auto-detect Flask
   - Click "Next" and then "Create Resources"

### Option 3: AWS Elastic Beanstalk

1. **Install EB CLI**
   ```bash
   pip install awsebcli
   ```

2. **Initialize EB**
   ```bash
   eb init -p python-3.12 portfolio-app
   ```

3. **Create Environment and Deploy**
   ```bash
   eb create portfolio-env
   eb open
   ```

### Option 4: Google Cloud Run

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.12-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   COPY . .
   CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
   ```

2. **Deploy to Cloud Run**
   ```bash
   gcloud run deploy portfolio --source . --platform managed --region us-central1 --allow-unauthenticated
   ```

### Option 5: Traditional VPS (Ubuntu)

1. **SSH into your server**
   ```bash
   ssh user@your-server-ip
   ```

2. **Install dependencies**
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv nginx
   ```

3. **Clone and setup**
   ```bash
   git clone your-repo-url portfolio
   cd portfolio
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Create systemd service**
   ```bash
   sudo nano /etc/systemd/system/portfolio.service
   ```
   
   Add:
   ```ini
   [Unit]
   Description=Portfolio Flask App
   After=network.target

   [Service]
   User=your-username
   WorkingDirectory=/home/your-username/portfolio
   Environment="PATH=/home/your-username/portfolio/venv/bin"
   ExecStart=/home/your-username/portfolio/venv/bin/gunicorn -w 4 -b 127.0.0.1:5000 app:app

   [Install]
   WantedBy=multi-user.target
   ```

5. **Configure Nginx**
   ```bash
   sudo nano /etc/nginx/sites-available/portfolio
   ```
   
   Add:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://127.0.0.1:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }

       location /static {
           alias /home/your-username/portfolio/static;
       }
   }
   ```

6. **Enable and start**
   ```bash
   sudo ln -s /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled
   sudo systemctl start portfolio
   sudo systemctl enable portfolio
   sudo systemctl restart nginx
   ```

## Environment Variables

Create a `.env` file (copy from `.env.example`):

```bash
cp .env.example .env
```

Edit `.env` and set:
```
SECRET_KEY=your-random-secret-key-here
FLASK_ENV=production
```

Generate a secret key:
```python
python -c "import secrets; print(secrets.token_hex(32))"
```

## SSL/HTTPS Setup

### Using Let's Encrypt (Free)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

## Performance Optimization

### 1. Enable Gzip Compression (Nginx)
```nginx
gzip on;
gzip_types text/css application/javascript application/json;
```

### 2. Cache Static Files (Nginx)
```nginx
location /static {
    alias /path/to/portfolio/static;
    expires 30d;
    add_header Cache-Control "public, immutable";
}
```

### 3. Use CDN for Bootstrap and Font Awesome
Already configured in the template!

## Monitoring

### Application Logs

**Heroku:**
```bash
heroku logs --tail
```

**VPS:**
```bash
sudo journalctl -u portfolio -f
```

### Performance Monitoring

Consider adding:
- **Sentry** for error tracking
- **Google Analytics** for visitor tracking
- **New Relic** for performance monitoring

## Backup Strategy

1. **Database** (if added later): Regular automated backups
2. **Code**: Keep in Git repository
3. **Environment variables**: Document securely

## Security Checklist

- [x] SECRET_KEY set to random value
- [x] Debug mode disabled in production
- [x] HTTPS enabled
- [ ] Security headers configured
- [ ] Rate limiting implemented (if needed)
- [ ] Regular dependency updates

## Troubleshooting

### Issue: Application won't start
**Solution**: Check logs for errors, verify all dependencies installed

### Issue: Static files not loading
**Solution**: Check static file paths, ensure proper permissions

### Issue: 502 Bad Gateway
**Solution**: Ensure gunicorn is running, check firewall settings

## Scaling

### Horizontal Scaling
- Use load balancer (Nginx, HAProxy)
- Deploy multiple instances
- Use managed platforms (Heroku, AWS)

### Vertical Scaling
- Increase worker processes in gunicorn
- Upgrade server resources

## Cost Estimates

- **Heroku**: Free tier available, $7/month for hobby
- **DigitalOcean**: $5/month for basic droplet
- **AWS**: Variable, ~$10-20/month for small app
- **Google Cloud**: Free tier available, then pay-as-you-go

## Next Steps

1. ✅ Test locally (currently running!)
2. Choose deployment platform
3. Set up domain name (optional)
4. Configure SSL certificate
5. Set up monitoring
6. Create backup strategy

## Support

For issues or questions:
- Check Flask documentation: https://flask.palletsprojects.com/
- Review deployment platform docs
- Contact: psspavan96@gmail.com

---

**Current Status**: Application is running locally and ready for deployment! 🚀