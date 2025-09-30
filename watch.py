print("fix(web): custom-tool output_schema.properties missing type (#25731)")
print("Co-authored-by: joeyczheng <joeyczheng@tencent.com>")
print({
    "name": "XSS Test #1: HTML实体编码绕过",
    "commit_data": {
        "repository": "testorg/testrepo", 
        "branch": "main",
        "sha": "abc123def456xss1",
        # 使用 HTML 实体编码 &lt; 代替 < 来绕过 <script 检测
        "message": "fix: update user profile &lt;script&gt;alert('XSS')&lt;/script&gt; validation",
        "author": "security_tester",
        "author_email": "test@example.com",
        "date": "2024-01-15T10:30:00Z",
        "url": "https://github.com/testorg/testrepo/commit/abc123def456xss1"
    }
})
print({
    "name": "XSS Test #2: SVG向量绕过",
    "commit_data": {
        "repository": "testorg/testrepo",
        "branch": "main", 
        "sha": "def789ghi012xss2",
        # 使用 SVG 标签而非 script 标签，当前检测未覆盖此向量
        "message": "feat: add profile avatar <svg onLoad=alert('XSS_SVG')> display feature",
        "author": "security_tester",
        "author_email": "test@example.com", 
        "date": "2024-01-15T10:31:00Z",
        "url": "https://github.com/testorg/testrepo/commit/def789ghi012xss2"
    }
})
print({
    "name": "XSS Test #3: XSS注入绕过",
    "commit_data": {
        "repository": "testorg/testrepo",
        "branch": "main", 
        "sha": "def789ghi012xss2",
        # 使用 SVG 标签而非 script 标签，当前检测未覆盖此向量
        "message": "my <section><h2><div>new <a href='https://github.com'>branch</a></div></h2></section>",
        "author": "security_tester",
        "author_email": "test@example.com", 
        "date": "2024-01-15T10:31:00Z",
        "url": "https://github.com/testorg/testrepo/commit/def789ghi012xss2"
    }
})
print({
    "name": "SQL Injection Test #1: UNION-based注入",
    "commit_data": {
        "repository": "testorg/testrepo",
        "branch": "main",
        "sha": "ghi345jkl678sql1", 
        # 使用经典的UNION SELECT注入，当前检测未覆盖UNION关键字
        "message": "fix: update query ' UNION SELECT password FROM users WHERE id=1#",
        "author": "security_tester",
        "author_email": "test@example.com",
        "date": "2024-01-15T10:32:00Z",
        "url": "https://github.com/testorg/testrepo/commit/ghi345jkl678sql1"
    }
})
print({
    "name": "SQL Injection Test #2: 时间盲注绕过",
    "commit_data": {
        "repository": "testorg/testrepo",
        "branch": "main",
        "sha": "jkl789mno012sql2",
        # 使用单引号和睡眠函数进行时间盲注测试，绕过当前检测模式
        "message": "perf: optimize database query'; WAITFOR DELAY '00:00:05'#",
        "author": "security_tester",
        "author_email": "test@example.com",
        "date": "2024-01-15T10:33:00Z", 
        "url": "https://github.com/testorg/testrepo/commit/jkl789mno012sql2"
    }
})
print({
    "name": "SQL Injection Test #3: 注释绕过",
    "commit_data": {
        "repository": "testorg/testrepo",
        "branch": "main",
        "sha": "jkl789mno012sql2",
        # 使用单引号和睡眠函数进行时间盲注测试，绕过当前检测模式
        "message": "perf: optimize database --query'; WAITFOR DELAY '00:00:05'#",
        "author": "security_tester",
        "author_email": "test@example.com",
        "date": "2024-01-15T10:33:00Z", 
        "url": "https://github.com/testorg/testrepo/commit/jkl789mno012sql2"
    }
})
