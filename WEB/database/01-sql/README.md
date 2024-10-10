# SQL 🚀

> ### Database
> - 관게형 데이터베이스 : 테이블, 행, 열의 정보를 구조화하는 방식, 서로 관련된 데이터 포인터를 저장하고 이에 대한 엑세스를 제공
> ![img.png](image/img.png)
>> 예시
>> - 고객 데이터 간 비교를 위해서는 어떤 값을 활용해야 할까? 
>> - 기본 키(데이터에 고유한 식별 값을 부여), 외래 키(주문 정보에 고객의 고유한 식별 값을 저장하기)
>> ![img_1.png](image/img_1.png)
>> ![img_2.png](image/img_2.png)
>> ![img_3.png](image/img_3.png)
>> ![img_4.png](image/img_4.png)

> #### Keyword
> 1. Table(Relation) : 데이터를 기록하는 곳
> ![img_5.png](image/img_5.png)
> 2. Field(Column, Attribute) : 고유의 타입이 지정됨
> ![img_6.png](image/img_6.png)
> 3. Record(Row, Tuple) : 구체적인 데이터 값이 저장됨
> ![img_7.png](image/img_7.png)
> 4. Database(Schema) : 테이블의 집합
> ![img_8.png](image/img_8.png)
> 5. Primary Key(PK) : 각 레코드의 고유한 값, 레코드의 식별자로 활용
> ![img_9.png](image/img_9.png)
> 6. Foreign Key(FK) : 각 레코드에서 서로 다른 테이블 간의 관계를 만드는 데 사용
> ![img_10.png](image/img_10.png)


> ### DBMS (Database Managements System)
> - 데이터베이스를 관리하는 소프트웨어 프로그램
> - 데이터 저장 및 관리를 용이하게 하는 시스템
> - 데이터베이스와 사용자 간의 인터페이스 역할
> - 사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구 등을 할 수 있도록 도움
> - ex) SQLite, MySQL, PostgreSQL, Oracle Database

> ### 정리
> - Table은 데이터가 기록되는 곳
> - Table에는 행에서 고유하게 식별 가능한 기본 키라는 속성이 존재, 외래 키를 사용하여 각 행에서 서로 다은 테이블 간의 관계를 만들 수 있음
> - 데이터는 기본 키 또는 외래 키를 통해 결합(join) 될 수 있는 여러 테이블에 걸쳐 구조화 됨

> ### SQL(Structure Query Language)
> ![img_11.png](image/img_11.png)
> ![img_12.png](image/img_12.png)
> - 데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어

> #### SQL Statements 예시
> ![img_13.png](image/img_13.png)
> - 이 Statement는 SELECT, FROM 2개의 keyword 로 구성 됨
>> - DDL : 데이터 정의
>> - DQL : 데이터 검색
>> - DML : 데이터 조작
>> - DCL : 데이터 제어
>> ![img_14.png](image/img_14.png)

> ### DQL(Data Query Language) - 데이터 검색 : select
> ![img_15.png](image/img_15.png)
> - select 키워드 이후 데이터를 선택하려는 필드를 하나 이상 지정
> - from 키워드 이후 데이터를 선택하려는 테이블의 이름을 지정

