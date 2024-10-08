create table articles (
    id INTEGER primary key autoincrement,
    content text not null,
    title varchar(100) not null,
    created_at date not null
);

-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');


-- 1. Insert data into table
insert into articles (title, content, created_at) values ('제목 1', '내용 1', date());


-- 2. Update data in table
update articles
set title = '제목 수정'
where id = 1;

-- 3. Delete data from table
-- 표현식 : 평가를 통해 하나의 값을 반환하는 식.
delete from articles
where id in (
    select id
    from articles
    order by created_at
    limit 2
    );