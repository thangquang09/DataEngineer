# Advanced SQL

- [Advanced SQL](#advanced-sql)
  - [1. Procedure](#1-procedure)
    - [1.1 Ví dụ](#11-ví-dụ)
  - [2. Transaction](#2-transaction)
    - [2.1. ACID Transaction](#21-acid-transaction)
    - [2.2. ACID Commands](#22-acid-commands)
    - [2.3. ACID Commands Call](#23-acid-commands-call)
  - [3. Cheat Sheet](#3-cheat-sheet)


## 1. Procedure

Là một tập hợp các lệnh SQL được lưu trữ và được thực thi trên database. Thay vì gửi nhiều lệnh SQL từ client server đến database, có thể gói gọn nó bởi procedure trên server và gửi đúng 1 lệnh SQL.

Có thể viết các procedure lưu trữ sẵn bằng nhiều ngôn ngữ khác nhau. Ví dụ
- Với db2 trên cloud và db2, có thể viết bằng SQL, PL, PL/SQL, Java, C và các ngôn ngữ khác.
- Có thể chấp nhận thông tin dưới dạng tham số, thực hiện thao tác create, read, update, delete và trả về kết quả trên client server.

Các lợi ích:
- Giảm tải trọng băng thông vì chỉ cần 1 call.
- Cải thiện hiệu suất vì quá trình xử lý xảy ra trên server nơi dữ liệu được lưu trữ với chỉ là 1 kết quả cuối cùng được chuyển lại cho khách hàng.
- Tái sử dụng Code.
- Tăng tính bảo mật, vì không cần cung cấp thông tin như tên bảng, tên cột, ... cho khách hàng tự truy vấn.
- Nhưng hãy nhớ rằng SQL không phải là một ngôn ngữ lập trình, nên không thể viết tất cả các logic trong procedure.

### 1.1 Ví dụ

```SQL
DELIMITER $$
CREATE PROCEDURE UPDATE_SAL (IN empNum CHAR(6), IN rating SMALLINT)
BEGIN
    UPDATE employees SET salary = salary * 1.10 WHERE emp_id = empNum AND rating = 1;
    UPDATE employees SET salary = salary * 1.05 WHERE emp_id = empNum AND raing <> 1;
END
$$
DELIMITER;
```

Cuối cùng có thể gọi procedure từ ứng dụng bên ngoài, từ các câu lệnh SQL

```SQL
CALL UPDATE_SAL('E1001', 1)
```

## 2. Transaction

Một transaction là một đơn vị công việc không thể bị chia cắt. Nó có thể bao gồm nhiều câu lệnh SQL nhưng tất cả đều được coi là *thành công*, hoặc là các lệnh SQL phải hoàn thành hoàn toàn, mới sẵn sàng cho câu lệnh tiếp theo hoặc là không có lệnh nào được hoàn thành.

Ví dụ:

![Transaction example](transaction_exp.png)

Nếu **Rose** mua một đôi giày **Boots** trong ShoeShop thì quá trình diễn ra như sau: 

```SQL
% stage 1:
UPDATE BankAccounts
SET Balance = Balance - 200
WHERE AccountName = 'Rose'

% stage 2:
UPDATE BankAccounts
SET Balance = Balance + 200
WHERE AccountName = 'ShoeShop'

% stage 3:
UPDATE ShoeShop
SET Stock = Stock - 1
WHERE Product = 'Boots'
```

Nếu có bất kỳ lệnh update nào lỗi, thì toàn bộ quá trình sẽ không được xảy ra và vẫn giữ nguyên ban đầu.

### 2.1. ACID Transaction

Các giao dịch ở ví dụ trên là ACID transactions, ACID viết tắt của 
- Atomic: nghĩa là tất cả các quá trình phải được xảy ra thành công hoặc không có bất kỳ quá trình nào xảy ra.
- Consitent: Dữ liệu phải nhất quán trước khi và sau khi transaction xảy ra.
- Isolated: Không có quá trình nào được thay đổi dữ liệu trong khi transaction đang chạy.
- Durable: Nhưng thay đổi được thực hiện bởi transaction phải bền bĩ.

### 2.2. ACID Commands

```SQL
BEGIN
    % stage 1:
    UPDATE BankAccounts
    SET Balance = Balance - 200
    WHERE AccountName = 'Rose'

    % stage 2:
    UPDATE BankAccounts
    SET Balance = Balance + 200
    WHERE AccountName = 'ShoeShop'

    % stage 3:
    UPDATE ShoeShop
    SET Stock = Stock - 1
    WHERE Product = 'Boots'
COMMIT % hoặc ROLLBACK
```

### 2.3. ACID Commands Call

```C
void main() {
    EXEC SQL UPDATE BankAccounts
    SET Balance = Balance - 200
    WHERE AccountName = 'Rose';

    EXEC SQL UPDATE BankAccounts
    SET Balance = Balance + 200
    WHERE AccountName = 'ShoeShop';

    EXEC SQL UPDATE ShoeShop
    SET Stock = Stock - 1
    WHERE Product = 'Boots';

    FINISHED:
    EXEC SQL COMMIT WORK;
    return;

    SQLERR:
        EXEC SQL WHENEVER SQLERROR CONTINUE;
        EXEC SQL ROLLBACK WORK;
        return;
}
```

```SQL
DELIMITER //

CREATE PROCEDURE TRANSACTION_ROSE()
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    START TRANSACTION;
    UPDATE BankAccounts
    SET Balance = Balance-200
    WHERE AccountName = 'Rose';

    UPDATE BankAccounts
    SET Balance = Balance+200
    WHERE AccountName = 'Shoe Shop';

    UPDATE ShoeShop
    SET Stock = Stock-1
    WHERE Product = 'Boots';

    UPDATE BankAccounts
    SET Balance = Balance-300
    WHERE AccountName = 'Rose';

    COMMIT;
END //

DELIMITER ;

```

Gọi

```SQL
CALL TRANSACTION_ROSE;

SELECT * FROM BankAccounts;

SELECT * FROM ShoeShop;
```

## 3. Cheat Sheet

[Views, Procedure, Transaction Cheat Sheet](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTURldmVsb3BlclNraWxsc05ldHdvcmstREIwMjAxRU4tU2tpbGxzTmV0d29yay9sYWJzL0NoZWF0U2hlZXQvU1FMLUNoZWF0LVNoZWV0LUZvci1WaWV3cy1TdG9yZWQtUHJvY2VkdXJlcy1UcmFuc2FjdGlvbnMtYW5kLUpPSU5fU3RhdGVtZW50cy5tZCIsInRvb2xfdHlwZSI6Imluc3RydWN0aW9uYWwtbGFiIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE3MjEzODc2Njl9.rHdSEQmz1NzE1ubOWJkNPTSFGRi6OOgjs3KgIsDJG-M)

[Join Stament Cheat Sheet](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTURldmVsb3BlclNraWxsc05ldHdvcmstREIwMjAxRU4tU2tpbGxzTmV0d29yay9sYWJzL0NoZWF0U2hlZXQvU1FMLUNoZWF0LVNoZWV0LUpPSU5fU3RhdGVtZW50cy5tZCIsInRvb2xfdHlwZSI6Imluc3RydWN0aW9uYWwtbGFiIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE3MjEzODc5MTl9.9kxcoHoMxRAHqiB4dOu0rJ6Q-N9buAHO2PX7VeAn6QI)

