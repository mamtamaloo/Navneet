from src.core.config import settings

workers = settings.workers
worker_class = "uvicorn.workers.UvicornWorker"
bind = "0.0.0.0:9001"
