-- 공통
SELECT * FROM articles;
SELECT * FROM users;
DROP TABLE articles;
DROP TABLE users;
PRAGMA table_info('articles');


-- 실습용 데이터
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL
);

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  content VARCHAR(100) NOT NULL,
  userId INTEGER NOT NULL,
  FOREIGN KEY (userId) 
    REFERENCES users(id)
);

INSERT INTO 
  users (name)
VALUES 
  ('하석주'),
  ('송윤미'),
  ('유하선');

INSERT INTO
  articles (title, content, userId)
VALUES 
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);

-- INNER JOIN
SELECT *
FROM articles
inner join users
on articles.userId = users.id
where users.id = 1;

-- LEFT JOIN(from절이 왼쪽 테이블), 게시글은 전부 다 불러옴 join 한 테이블은 null값으로 채워버림
SELECT *
FROM users
left join articles
on articles.userId = users.id
where articles.id is null;

-- RIGHT JOIN()
SELECT *
FROM articles
inner join users
on articles.userId = users.id
where users.id = 1;