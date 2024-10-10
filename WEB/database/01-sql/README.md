# SQL 🚀

> ### Database
> - 관게형 데이터베이스 : 테이블, 행, 열의 정보를 구조화하는 방식, 서로 관련된 데이터 포인터를 저장하고 이에 대한 엑세스를 제공
> ![img.png](image01/img.png)
>> 예시
>> - 고객 데이터 간 비교를 위해서는 어떤 값을 활용해야 할까? 
>> - 기본 키(데이터에 고유한 식별 값을 부여), 외래 키(주문 정보에 고객의 고유한 식별 값을 저장하기)
>> ![img_1.png](image01/img_1.png)
>> ![img_2.png](image01/img_2.png)
>> ![img_3.png](image01/img_3.png)
>> ![img_4.png](image01/img_4.png)

> #### Keyword
> 1. Table(Relation) : 데이터를 기록하는 곳
> ![img_5.png](image01/img_5.png)
> 2. Field(Column, Attribute) : 고유의 타입이 지정됨
> ![img_6.png](image01/img_6.png)
> 3. Record(Row, Tuple) : 구체적인 데이터 값이 저장됨
> ![img_7.png](image01/img_7.png)
> 4. Database(Schema) : 테이블의 집합
> ![img_8.png](image01/img_8.png)
> 5. Primary Key(PK) : 각 레코드의 고유한 값, 레코드의 식별자로 활용
> ![img_9.png](image01/img_9.png)
> 6. Foreign Key(FK) : 각 레코드에서 서로 다른 테이블 간의 관계를 만드는 데 사용
> ![img_10.png](image01/img_10.png)


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
> ![img_11.png](image01/img_11.png)
> ![img_12.png](image01/img_12.png)
> - 데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어

> #### SQL Statements 예시
> ![img_13.png](image01/img_13.png)
> - 이 Statement는 SELECT, FROM 2개의 keyword 로 구성 됨
>> - DDL : 데이터 정의
>> - DQL : 데이터 검색
>> - DML : 데이터 조작
>> - DCL : 데이터 제어
>> ![img_14.png](image01/img_14.png)

> ### DQL(Data Query Language)
> #### 01. Querying data
> - ***select***
>> ![img_15.png](image01/img_15.png)
>> - select 키워드 이후 데이터를 선택하려는 필드를 하나 이상 지정
>> - from 키워드 이후 데이터를 선택하려는 테이블의 이름을 지정

> #### 02. Sorting data
> - ***order by***
>> ![img.png](image02/img.png)
>> - from clause 뒤에 위치
>> - 하나 이상의 컬럼을 기준으로 결과를 오름차순(ASC, default), 내림차순(DESC) 정렬
>> ![img_1.png](image02/img_1.png)
>> - 1. 테이블에서(from) 
>> - 2. 조회하여 (select)
>> - 3. 정렬 (order by)

> #### 03. Filtering data
>> ![img_2.png](image02/img_2.png)

> - ***distinct*** : 조회 결과에서 중복된 레코드를 제거
>> ![img_3.png](image02/img_3.png)
>> - select 키워드 바로 뒤에 작성
>> - select distinct 키워드 다음에 고유한 값을 선택하려는 하나 이상의 필드를 지정
> - ***where*** : 조회 시 특정 검색 조건을 지정
>> ![img_4.png](image02/img_4.png)
>> - from clause 뒤에 위치
>> - search_condition은 비교연산자 및 논리연산자(and, or, not 등)를 사용하는 구문이 사용됨
> - ***Comparison Operators***
>   - 비교 연산자 [=, >=, <= , != , IS, LIKE, IN, BETWEEN...AND]
> - ***Logical Operators***
>   - 논리 연산자 [AND(&&), OR(||), NOT(!)]
> - ***In Operator***
>   - 값이 특정 목록 안에 있는지 확인
> - ***LIKE Operator***
>   - 값이 특정 패턴에 일치하는지 확인
>   - % : 0개 이상의 문자열과 일치 하는지 확인
>   - _ : 단일 문자와 일치하는지 확인

> - ***LIMIT clause***
> ![img_7.png](image02/img_7.png)
> ![img_8.png](image02/img_8.png)
> - 하나 또는 두 개의 인자를 사용(0 또는 양의 정수), row_count는 조회하는 최대 레코드 수를 지정

> #### 04. Grouping data
> - 레코드를 그룹화하여 요약본 생성('집계 합수'와 함께 사용)
> - Aggregation Functions
>   - 값에 대한 계산을 수행하고 단일한 값을 반환하는 함수 
>   - SUM, AVG, MAX, MIN, COUNT
> ![img_9.png](image02/img_9.png)
> - FROM 및 WHERE 절 뒤에 배치
> - GROUP BY 절 뒤에 그룹화 할 필드 목록을 작성
> ![img_10.png](image02/img_10.png)
> ![img_11.png](image02/img_11.png)

> ![img_12.png](image02/img_12.png)



> ### DDL(Data Definition Language)

> #### 01. Create
> ![img_13.png](image02/img_13.png)
> ![img_14.png](image02/img_14.png)
> ![img_15.png](image02/img_15.png)
> ![img_16.png](image02/img_16.png)
> - Constraints : 테이블 필드에 적용되는 규칙 또는 제한 사항 (데이터의 무결성을 유지하고 데이터베이스의 일관성을 보장)
> ![img_17.png](image02/img_17.png)
> - autoincrement
> ![img_18.png](image02/img_18.png)

> #### 02. Alter
> ![img_19.png](image02/img_19.png)
> - column 추가
> ![img_20.png](image02/img_20.png)
> ![img_21.png](image02/img_21.png)
> ![img_22.png](image02/img_22.png)
> ![img_23.png](image02/img_23.png)
> - column 이름 변경 (rename column)
> ![img_24.png](image02/img_24.png)
> ![img_25.png](image02/img_25.png)
> ![img_26.png](image02/img_26.png)
> - column 삭제
> ![img_27.png](image02/img_27.png)
> ![img_28.png](image02/img_28.png)
> - table 이름 변경 (rename to table)
> ![img_30.png](image02/img_30.png)
> ![img_29.png](image02/img_29.png)

> #### 03. Drop
> ![img_31.png](image02/img_31.png)


> ### DML(Data Manuplation Language)

> #### 01. Insert
> ![img_32.png](image02/img_32.png)
> ![img_33.png](image02/img_33.png)
> ![img_34.png](image02/img_34.png)
> ![img_35.png](image02/img_35.png)

> #### 02 Update
> ![img_36.png](image02/img_36.png)
> ![img_37.png](image02/img_37.png)
> ![img_38.png](image02/img_38.png)

> #### 03. Delete
> ![img_39.png](image02/img_39.png)
> ![img_40.png](image02/img_40.png)
> ![img_41.png](image02/img_41.png)

> ### Multi table queries
> ***join***
> ![img_42.png](image02/img_42.png)
> ![img_43.png](image02/img_43.png)
> ![img_44.png](image02/img_44.png)
> ![img_45.png](image02/img_45.png)
> ![img_46.png](image02/img_46.png)
> ![img_47.png](image02/img_47.png)
> ![img_48.png](image02/img_48.png)
> ![img_49.png](image02/img_49.png)
> ![img_50.png](image02/img_50.png)
> ![img_51.png](image02/img_51.png)
> ![img_52.png](image02/img_52.png)
> ![img_53.png](image02/img_53.png)
> ![img_54.png](image02/img_54.png)