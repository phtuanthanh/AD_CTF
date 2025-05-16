import sys
import os

# Thêm đường dẫn /etc vào PYTHONPATH nếu chưa có
sys.path.insert(0, '/etc')

# Thiết lập biến môi trường cho Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.prod_settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

