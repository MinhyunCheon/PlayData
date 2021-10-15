# hello-git



# 로컬 README.md 업로드 실습
### 강의자료와 다르게 기존 git을 clone하여 시작
![image](https://user-images.githubusercontent.com/90489192/137481575-39cf7951-9b60-49c4-bf30-66b01bf94340.png)   
### clone한 PlayData 폴더로 이동해 status, diff 명령어 확인
![image](https://user-images.githubusercontent.com/90489192/137481663-59c9a989-0252-4eea-944e-bd88ed6e74e1.png)   
### log 명령어 확인
![image](https://user-images.githubusercontent.com/90489192/137481740-e538b797-2eaa-4193-ba3f-3cf3147ce876.png)   
### PlayData 하위에 위치한 Git 폴더로 이동해 README.md 생성 후 add
![image](https://user-images.githubusercontent.com/90489192/137481777-b80643ea-0a63-44a8-91c5-fb0742129cdd.png)   
### 위 warning 메세지에 대해 검색한 결과 유닉스 줄바꿈(LF, Line Feed)과 윈도우 줄바꿈(CRLF, Carriage Return Line Feed) 문자열 차이로 인해 줄바꿈 문자 변환 시 오류가 발생할 수 있어 경고 발생, 이를 해결하기 위해 core.autocrlf를 true로 설정
![image](https://user-images.githubusercontent.com/90489192/137481804-712ae05a-0591-452c-8497-ad0d9d9a09e9.png)   
### README.md를 add한 뒤 status 확인
![image](https://user-images.githubusercontent.com/90489192/137481820-36d85666-2a7d-4662-96b1-ecc11c410ffc.png)   
### commit
![image](https://user-images.githubusercontent.com/90489192/137481841-81602e46-e1bb-4131-a9b7-66a82c3ce811.png)   
### 캡쳐는 하지 않았지만, Git 폴더에서 remote 명령어를 실행했을 때, 아무 내용이 출력되지 않아 상위 PlayData로 이동해 확인 후 push 수행
![image](https://user-images.githubusercontent.com/90489192/137481864-d6a1eca4-acbf-4291-9252-578fff5ad897.png)   
### push 권한을 확인하기 위해 출력된 connect창
![image](https://user-images.githubusercontent.com/90489192/137481883-a8f1ecc5-6e46-4105-a933-917388537154.png)   
### connect창과 동시에 git bash에 출력된 메세지
![image](https://user-images.githubusercontent.com/90489192/137481907-24736a99-fd94-40a6-8749-b1e624921095.png)   
### browser를 통해 인증 완료
![image](https://user-images.githubusercontent.com/90489192/137481928-3695d538-53a1-4b22-8bc8-83c28a06857f.png)   
### 원격 저장소에 commit한 내용이 반영되지 않아 add부터 다시 수행, 이 과정에서 commit을 누락하여 같은 증상을 계속 겪음
![image](https://user-images.githubusercontent.com/90489192/137482125-d7fc42d2-2696-4b36-8e45-415844c0e247.png)   
### git push -u 명령어도 입력해봤지만, commit을 하지 않은 상태이기 때문에 변화 없음
![image](https://user-images.githubusercontent.com/90489192/137482160-11748482-9d38-4ff3-81f8-2fdb3ff0b9de.png)   
### 문제를 찾기 위해 restore --staged 명령으로 staged 상태인 Git/README.md 파일을 untracked로 변경
![image](https://user-images.githubusercontent.com/90489192/137482183-02310c0f-1a8c-4acb-a0ec-44aed7368228.png)   
### 위와 동일하게 문제를 찾기 위해 fetch 밑 reset 수행
![image](https://user-images.githubusercontent.com/90489192/137482202-20c1686b-7716-421c-b37b-283fd053d33c.png)   
### restore
![image](https://user-images.githubusercontent.com/90489192/137482211-fca0cda1-c281-4b82-bfff-bb97cadc7f46.png)   
### 최종 commit 후 원격 브랜치에 README.md 업로드
![image](https://user-images.githubusercontent.com/90489192/137482241-eb917d2f-4368-4d54-bbf4-73e72beeccfc.png)   
### # 아마 처음 Git 폴더에서 commit 후 바로 push를 했어야 원활히 동작했을 것으로 판단
### # 각 명령어에 대한 이해도가 부족한 상태에서 벌어진 해프닝으로 9시 ~ 14시까지 결과물에 비해 상당히 긴 시간이 소요됐지만, 덕분에 restore와 reset에 관련된 내용, 업로드가 되지 않는 여러 상황 등을 검색을 통해 숙지했기에 좋은 경험이었다고 생각한다.
