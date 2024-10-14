# Many-to-Many relationships 04 🚀

> ### N:M or M:N
> - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
> - 양쪽 모두에서 N:1 관계를 가짐

> #### 의사 - 환자 간 모델 관계 설정
> ![img.png](images/img.png)
> ![img_1.png](images/img_1.png)
> ![img_2.png](images/img_2.png)
> ![img_3.png](images/img_3.png)
> ![img_4.png](images/img_4.png)
> ![img_5.png](images/img_5.png)
> ![img_6.png](images/img_6.png)
> ![img_7.png](images/img_7.png)
> ![img_8.png](images/img_8.png)
> ![img_9.png](images/img_9.png)
> #### Django에서는 'ManyToManyField'로 중개모델을 자동으로 생성

> ### ManyToManyField()
> ![img_10.png](images/img_10.png)
> ![img_11.png](images/img_11.png)
> ![img_12.png](images/img_12.png)
> ![img_13.png](images/img_13.png)
> ![img_14.png](images/img_14.png)
> ![img_15.png](images/img_15.png)
> ![img_16.png](images/img_16.png)
> #### 만약 예약 정보에 병의 증상, 예약일 등 추가 정보가 포함되어야 한다면?

> ### 'through' argument
> - 중개 테이블에 '추가 데이터'를 사용해 M:N 관계를 형성하려는 경우에 사용
> ![img_17.png](images/img_17.png)
> ![img_18.png](images/img_18.png)
> ![img_19.png](images/img_19.png)
> ![img_20.png](images/img_20.png)
> ![img_21.png](images/img_21.png)
> ![img_22.png](images/img_22.png)

> ### M:N 관계 주요 사항
> ![img_23.png](images/img_23.png)

> ### ManyToManyField(to, **options)
> ![img_24.png](images/img_24.png)
> ![img_25.png](images/img_25.png)
> ![img_26.png](images/img_26.png)
> ![img_27.png](images/img_27.png)
> ![img_28.png](images/img_28.png)
> ![img_29.png](images/img_29.png)
> ![img_30.png](images/img_30.png)

> ### 좋아요 기능 구현
> ![img_31.png](images/img_31.png)
> ![img_32.png](images/img_32.png)
> ![img_33.png](images/img_33.png)
> ![img_34.png](images/img_34.png)
> ![img_35.png](images/img_35.png)
> ![img_36.png](images/img_36.png)
> ![img_37.png](images/img_37.png)