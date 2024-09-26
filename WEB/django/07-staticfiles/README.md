# Static Files 💻

> ### Static Files, 정적 파일
> ![img.png](img.png)
> ![img_1.png](img_1.png)
> - 서버 측에서 변경되지 않고 고정적으로 제공되는 파일 (이미지, JS, CSS file 등)

>> - static file 기본 경로 : app/static
>> ![img_2.png](img_2.png)
>> ![img_3.png](img_3.png)
>> ![img_4.png](img_4.png)
>> - static_url : 기본 경로 및 추가 경로에 위치한 정적 파일을 참조하기 위한 URL(실제 경로가 아니며, URL로만 존재)
>> ![img_5.png](img_5.png)
>> - static files 추가 경로 : STATICFILES_DIRS에 문자열 값으로 추가 경로 설정
>> - STATICFILES_DIRS : 정적 파일의 기본 경로 외에 추가적인 경로 목록을 정의하는 리스트
>> ![img_6.png](img_6.png)
>> ![img_7.png](img_7.png)
>> ![img_8.png](img_8.png)
>> ![img_9.png](img_9.png)

>> - 정적 파일을 제공하려면 요청에 응답하기 위한 URL이 필요

> #### Media Files
> - 사용자가 웹에서 업로드하는 정적 파일(user-uploaded)
>> - ImageField() : 이미지 업로드에 사용하는 모델 필드, 이미지 객체가 직접 DB에 저장되는 것이 아닌 '이미지 파일 경로' 문자열이 저장됨.
>> ![img_10.png](img_10.png)
>> ![img_11.png](img_11.png)
>> ![img_12.png](img_12.png)
>> ![img_13.png](img_13.png)

> #### 이미지 업로드
> ![img_14.png](img_14.png)
> ![img_15.png](img_15.png)
> ![img_16.png](img_16.png)
> ![img_17.png](img_17.png)
> ![img_18.png](img_18.png)
> ![img_19.png](img_19.png)


> #### 업로드 이미지 제공하기
> ![img_20.png](img_20.png)
> ![img_21.png](img_21.png)
> ![img_22.png](img_22.png)

> #### 업로드 이미지 수정
> ![img_25.png](img_25.png)
> ![img_26.png](img_26.png)

> #### 미디어 파일 추가 경로
> ![img_23.png](img_23.png)
> - 'upload_to' argument : ImageField()의 upload_to 속성을 사용해 다양한 추가 경로 설정
> ![img_24.png](img_24.png)
> - request.FILES가 두번째 위치 인자인 이유 : ModelForm의 상위 클래스 BaseModelForm의 생성자 함수 키워드 인자
