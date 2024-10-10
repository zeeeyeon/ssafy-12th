-- Table 구조 확인
PRAGMA table_info('examples');
-- PRAGMA 방식
-- sqlite에서 테이블의 구성 정보를 확인하기 위한 용도

-- 1. Create a table
CREATE TABLE examples (
    ExamId Integer primary key autoincrement ,
    LastName varchar(50) not null ,
    FirstName varchar(50) not null
);

-- 2. Modifying table fields

-- 2.1 ADD COLUMN

ALTER TABLE examples
ADD Country varchar(100) not null default 'default value';


alter table examples
add age INTEGER not null default 0;

alter table examples
add address varchar(100) not null default 'default value';

-- sqlite는 단일 문을 사용하여 한번에 여러 열을 추가하는 것을 지원하지 않음

-- 2.2 RENAME COLUMN

alter table examples
rename column address to PostCode;


-- 2.3 RENAME TO
alter table examples
rename to new_examples;


-- 3. Delete a table
drop table new_examples;

-- sqlite는 컬럼 수정 불가
-- 대신 테이블의 이름을 바꾸고, 새 테이블을 만들고 데이터를 새 테이블에 복사하는 방식을 사용
