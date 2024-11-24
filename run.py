from unwrap import app
from unwrap.user.routes import user_bp
from unwrap.admin.routes import admin_bp
from unwrap.blog import blog_bp

# 注册蓝图
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(blog_bp, url_prefix='/blog')  # 注册博客蓝图

print(app.url_map)  # 确保注册完成后打印

from unwrap import db

# 创建所有表
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
