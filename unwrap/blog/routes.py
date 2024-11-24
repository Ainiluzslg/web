from flask import render_template, request, redirect, url_for, flash
from unwrap import db
from . import blog_bp

# 模拟数据库表结构
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

# 博客首页
@blog_bp.route('/')
def blog_home():
    posts = BlogPost.query.all()
    return render_template('blog_home.html', posts=posts)

# 添加博客文章
@blog_bp.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = BlogPost(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        flash('Post added successfully!', 'success')
        return redirect(url_for('blog.blog_home'))
    return render_template('add_post.html')
