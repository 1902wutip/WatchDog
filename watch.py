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
