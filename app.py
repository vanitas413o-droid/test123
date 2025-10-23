from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 模擬的部落格文章資料（可以當成記憶體內的資料庫）
posts = [
    {
        'id': 1,
        'title': '第一篇文章',
        'author': '小明',
        'content': '這是第一篇部落格文章的內容。'
    },
    {
        'id': 2,
        'title': '第二篇文章',
        'author': '小美',
        'content': '這是第二篇文章的內容，歡迎閱讀！'
    }
]

# 首頁，顯示所有文章列表
@app.route('/')
def index():
    return render_template('index.html', posts=posts)

# 顯示單篇文章
@app.route('/post/<int:post_id>')
def show_post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        return "文章未找到", 404
    return render_template('post.html', post=post)

# 新增文章的表單 + POST 方法處理
@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        new_id = len(posts) + 1
        posts.append({
            'id': new_id,
            'title': title,
            'author': author,
            'content': content
        })
        return redirect(url_for('index'))
    return '''
        <h1>新增文章</h1>
        <form method="post">
            標題: <input type="text" name="title"><br>
            作者: <input type="text" name="author"><br>
            內容:<br>
            <textarea name="content" rows="5" cols="40"></textarea><br>
            <input type="submit" value="送出">
        </form>
        <a href="/">回首頁</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)
