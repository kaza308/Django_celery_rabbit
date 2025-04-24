# Django_celery_rabbit
this project show the demo of Django use celery and rabbit.

本地需先部署rabbitmq，本仓库中使用的是
rabbitmq: stable 4.1.0
接着启动rabbitmq服务，不同操作系统启动命令可自行搜索

进入ceproject目录下: cd ceproject ，执行：
pip install -r requirements.txt

安装完成后执行：
celery -A ceproject worker -l INFO

开启另一个terminal，进入当前项目manage.py目录下，继续执行：
python manage.py runserver 127.0.0.1:8000

