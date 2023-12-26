from faker import Faker
import mysql.connector

fake = Faker()

# MySQL 연결 설정
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="happy99",  # 본인의 MySQL 비밀번호로 변경
    database="inha_db"
)

cursor = connection.cursor()

# INSERT 쿼리 생성 및 실행
for _ in range(100000):  # 10만개의 데이터를 생성
    sid = fake.random_int(min=100000, max=999999)  # 예시로 6자리 랜덤 숫자 생성
    sname = fake.name()
    semail = fake.email()
    sphonenumber = fake.phone_number()
    Major = fake.random_element(elements=("Computer Science", "Mathematics", "Physics", "Biology", "Chemistry"))
    class_id = fake.random_int(min=20231, max=20235)  # 예시로 20231부터 20235 중 랜덤 숫자 생성

    insert_query = f"""
        INSERT INTO student (sid, sname, semail, sphonenumber, Major, class_id)
        VALUES ({sid}, '{sname}', '{semail}', '{sphonenumber}', '{Major}', {class_id});
    """

    cursor.execute(insert_query)

# 변경 사항 저장
connection.commit()

# 연결 종료
cursor.close()
connection.close()
