import os

class Config:
    # مفتاح الجلسة – غيّره لأي نص قوي وطويل
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-this-to-a-long-random-key")

    # قاعدة البيانات
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "exam.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # بيانات الأدمن يمكن لاحقاً نقلها للـ env في الاستضافة
    ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL", "feras_sst@outlook.com")
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "Fe@0771978Ras")