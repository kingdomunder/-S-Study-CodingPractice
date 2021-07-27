# 생활코딩 

모델링 : 이상을 현실에 적용하기 


1. 모델이란?
   - 목적을 가지고 진짜를 모방한 것?
   - 좋은 모델 : 목적에 부합하는 모방 
   - 목적 : 표에 정보를 담는 것? -> 굉장히 어려운 작업


2. 전체 흐름
   - 업무파악 -> 개념적 데이터 모델링 -> 논리적 -> 물리적
   - 개념적 모델링이 중요
   - 논리적 모델링 -> 다소 기계적인 작업일 수 있다 


3. ERD - 개체-관계형 데이터베이스(Entity-Relationship)
   - Entity    -> Table
   - Atrribute -> Column
   - Relation  -> PK(Primary Key),FK(Foreign?)
   - Tuple     -> Row


4. 원인과 결과
   - 기획자와 개발자
   - User Interface와 Database
   - 먼저 할 일 : Entity 찾아내기 - 저자/글/댓글 의 쓰기 화면에 잘 나타난다 
  
   - drawio 툴 -> 다이어그램 관계도 작성 등에 사용 (스키마?)


5. 식별자(Identifier)
   
   - primary key : user_id -> 행을 식별할 수 있는 유일무이한 키 
   - alternate key : email, national_id (secondary, 성능향상을 위해 추가 가능)
   - candidate key : 위의 3개 포함 

   - composed key (중복키) : 키 하나만으로 데이터를 식별하기 어려울 때 -> 키 두개 이상을 사용?

   - 식별자인 primary key 에는 밑줄을 그어준다 -> 스키마에서? 

   - Foreign key(외래키) : 다른 테이블에서 가져온 키? 


6. Cardinality 와 Optionality

   - Cardinality
     - 사전적 의미는 '기수', '대응 수', '관계 수'
     - 테이블의 두 데이터 간에 [일 대 일] / [일 대 다] 의 관계 가능
     - [일 대 다] ex)글쓴이 한 명은 여러 댓글을 달 수 있지만, 댓글은 하나의 글쓴이만 가진다 
     - [다 대 다] ex)글쓴이 한 명은 여러 글을 쓸 수 있고, 글은 여러 저자가 존재할 수 있다 

   - Optionality 
     - 다이어그램에서 O로 표현 (Option?)
     - ex) 글쓴이는 댓글을 작성하지 않을 수 있지만, 각 댓글은 반드시 저자가 있다 
     - 저자 : Mandatory(1) -> 다이어그램 |로 표기
     - 댓글 : Optional (N) -> 다이어그램 O로 표기


7. erd.yah.ac(주소) -> Entity relational diagram Helper (by 생활코딩)


8. Mapping Rule 
   - ER Master (ermaster.sourceforge.net) : 오픈소스 tool -> 종이나 엑셀에서 그려봐도 무방하다
   - 컬럼의 domain 설정 -> 해당 컬럼의 데이터타입이나 길이 등에 범위(제한)을 설정 


9. Relationshop 설정 - PK, FK 
   - Cardinality -> 일대일, 일대다, 다대다 

     - 일 대 일(1 대 1)
       - 누가 primary key를 가질 것인가? : 의존관계 따져보기 
         -> 부모(저자)-자식(휴면저자) 테이블 -> 휴면저자에 Foreign key 할당 
       - 저자는 휴면저자 데이터가 없어도 되지만, 휴면저자는 저자 데이터가 필요하다 (계정이 있어야 휴면이 진행) -> Optional과 유사? 
       - Optional과의 차이 생각해보기 : 휴면됐다는 
      
     - 일 대 다(1 대 N)
       - 한 쪽이 Optional : 비교적 간단하다 
       - topic(1,|)과 comment(N,Optional) 

     - __다 대 다(N 대 N)__
       - 관계 파악 및 설정이 어렵다 
       - 저자와 글 : 한 명의 저자가 여러 글 작성가능 , 하나의 글이 여러 저자를 가질 수 있음 


10. Mapping Table
    - author - topic -> 다 대 다 관계 -> Mapping Table 생성
    - author ---- [write] ---- topic
    - write 테이블에는 author와 topic의 id 컬럼들을 각각 가져와서 foreign key로 할당 
    - [write - topic] 은 [1,N 대 1] 의 관계


11. Normaliztion(정규화)
    - raw 데이터를 정제?
    - UNF , 1NF . 2NF ... EKNF, BCNF, ETNF ... 6NF
    - 1NF = First Normal Form - 첫 번째 정규화 
    - 3NF까지를 주로 사용한다 
    - http://bit.ly/2wV2SFj - 예시 구글시트 (by 생활코딩)
  

12. First Normal Form(1NF)  
    - Atomic columns : 컬럼은 원자적이어야 한다 -> 자세해야한다? 
    - tag 컬럼에 rdb, free [두 개의 데이터] 존재 -> atomic 하지 않다
      - select * from topic where tag = 'free'
      - select * from topic order by tag
      - join하기도 불가능하거나 어렵다

    - tag컬럼의 데이터 2개를 어떻게 나누어 표현할 것인가? - 다른 컬럼(topic)데이터 중복표시 등의 문제
        => tag table 생성하여 컬럼 분리  
        => mapping table 생성 : topic_tag_relation


13. Second Normal Form(2NF)
    - No partial dependencies(부분 종속성 제거) -> 중복 key 제거 ? 
        => 중복되는 key(컬럼)들을 중복되지 않는 key들과 분리 
        => 중복되지 않는 key들은 따로 table 생성 


14. Third Normal Form(3NF)
    - No transitive dependencies(이행적 종속성 제거)
    - transitive의 의미? : 타동사, 다른 대상에게 이행시키다
    - primary key에 직접 종속되지 않고, primary key에 종속되는 alternate key에 종속되는 중복되는 데이터? 
        => 2NF와 유사한 방법으로 중복 key들을 분리하여 table 생성 


15. 물리적 데이터 모델링 
    - 이상적인 모델링은 제품에 맞게 현실적 구현 
    - 성능 향상이 중요한 단계
      - find slow query : 병목으로 느려지는 쿼리 찾기 -> 제품마다 다를 수 있다 - 검색해보기 
      - index : 읽기 성능향상 , 쓰기 성능하락 
      - application : cache -> 입력에 따른 실행결과를 저장해두고 같은 입력이 들어오면 불러온다 
      - denormalize : 양날의 검 -> 최후의 수단


16. Denomrmalization 
    - 표의 구조를 바꾼다 
    - 쓰기의 편리함을 위해 읽기의 성능을 희생 
  
    1. 테이블의 역정규화
       -  컬럼을 기준으로 테이블 분리 -> 하나의 표 안에서 컬럼 바꾸기
       -  행을 기준으로 테이블 분리 -> 하나의 표를 여러개의 표로 쪼개기
    2. 관계의 역정규화
       -  테이블과 테이블 사이의 관계성을 조작하여 지름길을 만듦


17. 역정규화의 사례
    - join 줄이기 -> 컬럼 합치기 
   
    - group by 출력을 단순화 :
      -  group by 결과값 중 필요하지 않은 컬럼이 많을 때, 기준되는 key(중복되는 primary key)를 count하여 다른 테이블로 가져와 개수만 보여줄 수도 있음 
   
    - 테이블을 분리 :
      - 컬럼을 기준으로 
        - 사용빈도가 높고, 데이터량이 많은 컬럼들을 분리하여 서로 다른 컴퓨터에 각각 저장하는 방법 : 
           -  성능 향상  => Sharding - 최후의 수단 
      - 행을 기준으로 
        - 관리가 어려움 
        - primary key가 중복되고 다른 컬럼 데이터가 매우 많을 경우에, 해당 key를 기준으로 여러 테이블을 생성 
        - 오류의 가능성이 많고, 정교한 테크닉 필요

    - 관계의 역정규화
      - 지름길 만들기 
      - 3번의 join을 2번의 join으로 
      - 일 대 다 관계의 테이블에서, 일의 역할을 하는 key를 가져와 컬럼으로 추가(key값이 단순하고 중복이 많을 경우)
      - join 줄이기 방법의 하나? 