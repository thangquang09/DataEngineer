- [1. Tổng quan về Apache Cassandra](#1-tổng-quan-về-apache-cassandra)
  - [1.1. Apache Cassandra là gì?](#11-apache-cassandra-là-gì)
  - [1.2. Cassandra và MongoDB: So sánh và khác biệt](#12-cassandra-và-mongodb-so-sánh-và-khác-biệt)
  - [1.3. Kiến trúc của Cassandra](#13-kiến-trúc-của-cassandra)
  - [1.4. Khả năng mở rộng và độ sẵn sàng của Cassandra](#14-khả-năng-mở-rộng-và-độ-sẵn-sàng-của-cassandra)
  - [1.5. Cassandra và các tính năng bị thiếu so với cơ sở dữ liệu quan hệ](#15-cassandra-và-các-tính-năng-bị-thiếu-so-với-cơ-sở-dữ-liệu-quan-hệ)
  - [1.6. Các kịch bản sử dụng tốt nhất cho Apache Cassandra](#16-các-kịch-bản-sử-dụng-tốt-nhất-cho-apache-cassandra)
  - [1.7. Trường hợp sử dụng Time Series](#17-trường-hợp-sử-dụng-time-series)
  - [1.8. Architecture of ApacheCassandra](#18-architecture-of-apachecassandra)
- [2. Các tính năng chính của Apache Cassandra](#2-các-tính-năng-chính-của-apache-cassandra)
  - [2.1. Kiến trúc phân tán và phi tập trung của Apache Cassandra](#21-kiến-trúc-phân-tán-và-phi-tập-trung-của-apache-cassandra)
  - [2.2. Sao chép (Replication), Khả năng mở rộng (Scalability) và tính khả dựng (Availability)](#22-sao-chép-replication-khả-năng-mở-rộng-scalability-và-tính-khả-dựng-availability)
  - [2.3. Hiệu suất ghi dữ liệu cao và Ngôn ngữ CQL](#23-hiệu-suất-ghi-dữ-liệu-cao-và-ngôn-ngữ-cql)
- [3. Mô Hình Dữ Liệu Apache Cassandra](#3-mô-hình-dữ-liệu-apache-cassandra)
  - [3.1. Giới thiệu về Mô Hình Dữ Liệu Cassandra](#31-giới-thiệu-về-mô-hình-dữ-liệu-cassandra)
  - [3.2. Keyspace và Bảng trong Cassandra](#32-keyspace-và-bảng-trong-cassandra)
  - [3.3. Khóa chính trong Cassandra](#33-khóa-chính-trong-cassandra)
  - [3.4. Phân vùng và Tính Địa Phương của Dữ Liệu](#34-phân-vùng-và-tính-địa-phương-của-dữ-liệu)
  - [3.5. Bảng tĩnh và bảng động trong Cassandra](#35-bảng-tĩnh-và-bảng-động-trong-cassandra)
  - [3.6. Clustering Key trong Cassandra](#36-clustering-key-trong-cassandra)
  - [3.7. Bảng động (Dynamic Table)](#37-bảng-động-dynamic-table)
  - [3.8. Mô hình hóa dữ liệu trong Cassandra](#38-mô-hình-hóa-dữ-liệu-trong-cassandra)
- [4. Giới Thiệu về Cassandra Query Language (CQL) Shell](#4-giới-thiệu-về-cassandra-query-language-cql-shell)
  - [4.1. Cassandra Query Language (CQL) là gì?](#41-cassandra-query-language-cql-là-gì)
  - [4.2. Các tùy chọn để chạy các truy vấn CQL](#42-các-tùy-chọn-để-chạy-các-truy-vấn-cql)
  - [4.3. Các lệnh đặc biệt trong CQL Shell](#43-các-lệnh-đặc-biệt-trong-cql-shell)
  - [4.4. Chi tiết về các lệnh CONSISTENCY và COPY](#44-chi-tiết-về-các-lệnh-consistency-và-copy)
- [5. Hands-on Lab: Using the CQL Shell (cqlsh)](#5-hands-on-lab-using-the-cql-shell-cqlsh)
- [6. Ngôn ngữ truy vấn Cassandra (CQL) - Các kiểu dữ liệu](#6-ngôn-ngữ-truy-vấn-cassandra-cql---các-kiểu-dữ-liệu)
  - [6.1. Kiểu dữ liệu tích hợp sẵn](#61-kiểu-dữ-liệu-tích-hợp-sẵn)
  - [6.2. Kiểu dữ liệu tập hợp](#62-kiểu-dữ-liệu-tập-hợp)
  - [6.3. Kiểu dữ liệu do người dùng tự định nghĩa](#63-kiểu-dữ-liệu-do-người-dùng-tự-định-nghĩa)
  - [6.4. Kết luận](#64-kết-luận)
- [7. Các thao tác với Keyspace trong Apache Cassandra](#7-các-thao-tác-với-keyspace-trong-apache-cassandra)
- [7.1. Các khái niệm chính](#71-các-khái-niệm-chính)
  - [7.2. Tạo Keyspace và các yếu tố cần xem xét](#72-tạo-keyspace-và-các-yếu-tố-cần-xem-xét)
  - [7.3. Replication Factor và Replication Strategy](#73-replication-factor-và-replication-strategy)
  - [7.4. Sao lưu dữ liệu trong môi trường đa trung tâm dữ liệu](#74-sao-lưu-dữ-liệu-trong-môi-trường-đa-trung-tâm-dữ-liệu)
  - [7.5. Chỉnh sửa và xóa Keyspace](#75-chỉnh-sửa-và-xóa-keyspace)
  - [7.6. Kết luận](#76-kết-luận)
- [8. Các thao tác với bảng trong Apache Cassandra](#8-các-thao-tác-với-bảng-trong-apache-cassandra)
  - [8.1. Giới thiệu về bảng](#81-giới-thiệu-về-bảng)
  - [8.2. Cú pháp tạo bảng](#82-cú-pháp-tạo-bảng)
  - [8.3. Tạo bảng tĩnh và động](#83-tạo-bảng-tĩnh-và-động)
  - [8.4. Các thuộc tính nâng cao của bảng](#84-các-thuộc-tính-nâng-cao-của-bảng)
  - [8.5. Ghi dữ liệu và quá trình lưu trữ](#85-ghi-dữ-liệu-và-quá-trình-lưu-trữ)
  - [8.6. Chỉnh sửa và xóa bảng](#86-chỉnh-sửa-và-xóa-bảng)
  - [8.7. Kết luận](#87-kết-luận)
  - [8.8. Hands-on Lab](#88-hands-on-lab)
- [9. CRUD Operations trong Apache Cassandra (Phần 1: INSERT và UPDATE)](#9-crud-operations-trong-apache-cassandra-phần-1-insert-và-update)
  - [9.1 Quá trình ghi (Write) trong Cassandra](#91-quá-trình-ghi-write-trong-cassandra)
  - [9.2 Lệnh INSERT trong Cassandra](#92-lệnh-insert-trong-cassandra)
  - [9.3 Lệnh UPDATE trong Cassandra](#93-lệnh-update-trong-cassandra)
  - [9.4. Lightweight Transactions (Giao dịch nhẹ)](#94-lightweight-transactions-giao-dịch-nhẹ)
  - [9.5. Kết luận](#95-kết-luận)
- [10. CRUD trong Apache Cassandra – Phần 2: Đọc và Xóa dữ liệu](#10-crud-trong-apache-cassandra--phần-2-đọc-và-xóa-dữ-liệu)
  - [10.1. Câu lệnh SELECT trong Cassandra](#101-câu-lệnh-select-trong-cassandra)
  - [10.2. Xóa dữ liệu trong Cassandra](#102-xóa-dữ-liệu-trong-cassandra)
  - [10.3. Kết luận](#103-kết-luận)
- [11. Hands-on lab](#11-hands-on-lab)


# 1. Tổng quan về Apache Cassandra

## 1.1. Apache Cassandra là gì?

Apache Cassandra là một cơ sở dữ liệu NoSQL mã nguồn mở, phân tán và phi tập trung. Nó nổi bật với khả năng mở rộng đàn hồi, luôn sẵn sàng (highly available), chịu lỗi (fault-tolerant), và có tính nhất quán có thể điều chỉnh (tunable consistency). Thiết kế phân phối của Cassandra dựa trên mô hình Dynamo của Amazon và mô hình dữ liệu của Bigtable từ Google. Nó được tạo ra tại Facebook và hiện đang được sử dụng bởi nhiều trang web lớn như Netflix, Spotify, và Uber.

Ví dụ thực tế: Netflix sử dụng Cassandra để quản lý lượng truy cập khổng lồ từ người dùng trên toàn cầu. Mỗi lần một người dùng đăng nhập hoặc truy cập phim, dữ liệu về người dùng và hành động của họ được ghi lại và xử lý ngay lập tức.

## 1.2. Cassandra và MongoDB: So sánh và khác biệt

Cassandra và MongoDB đều là cơ sở dữ liệu NoSQL, nhưng mỗi loại lại phục vụ cho những trường hợp sử dụng khác nhau. MongoDB chủ yếu được thiết kế cho các tác vụ liên quan đến việc tìm kiếm dữ liệu (search), trong đó dữ liệu có thể được biểu diễn dưới dạng các tài liệu (document). Điều này làm cho MongoDB phù hợp với các trường hợp đọc dữ liệu với tính nhất quán cao.

**Sự khác biệt chính:**

- **MongoDB**: Tập trung vào các trường hợp sử dụng đọc dữ liệu, đòi hỏi tính nhất quán cao.
- **Cassandra**: Tập trung vào các trường hợp yêu cầu ghi dữ liệu nhanh, sẵn sàng cao và phân phối địa lý.

- Ví dụ: Một cửa hàng trực tuyến cần ghi lại nhanh các giao dịch hoặc thông tin truy cập người dùng với tốc độ cao. Cassandra sẽ phù hợp hơn trong trường hợp này, trong khi MongoDB sẽ phù hợp hơn khi bạn cần truy vấn phức tạp và nhất quán dữ liệu.

## 1.3. Kiến trúc của Cassandra

Cassandra có kiến trúc ngang hàng (peer-to-peer) đơn giản, khác với kiến trúc chính-phụ (primary-secondary) của MongoDB. Điều này làm cho Cassandra dễ dàng cài đặt và mở rộng theo chiều ngang (scale out) mà không cần dừng hệ thống hay cấu hình lại.

**Tính năng nổi bật:**

- **Phi tập trung (Decentralized)**: Không có nút trung tâm, mỗi nút đều bình đẳng.
- **Khả năng chịu lỗi (Fault-tolerant)**: Hệ thống vẫn hoạt động khi một vài nút bị lỗi.
- **Hiệu suất ghi cao (High write throughput)**: Cassandra rất mạnh ở khả năng ghi nhanh.
- **Tính mở rộng dễ dàng (Scalable)**: Cassandra có thể mở rộng tuyến tính mà không cần cấu hình lại.

**Ví dụ thực tế**: Spotify sử dụng Cassandra để quản lý các phiên truy cập từ người dùng toàn cầu. Nhờ khả năng phân phối và mở rộng dễ dàng, Spotify có thể đảm bảo dịch vụ của mình luôn sẵn sàng và phản hồi nhanh dù số lượng người dùng rất lớn.

## 1.4. Khả năng mở rộng và độ sẵn sàng của Cassandra

Cassandra hỗ trợ triển khai trên nhiều trung tâm dữ liệu, điều này rất quan trọng với các dịch vụ cần truy cập từ khắp nơi trên thế giới. Nó cũng có khả năng mở rộng nhanh chóng mà không cần khởi động lại dịch vụ, làm cho Cassandra rất hữu ích khi ứng dụng cần xử lý lưu lượng truy cập lớn và thay đổi nhanh.

**Ví dụ**: Uber sử dụng Cassandra để lưu trữ và xử lý thông tin từ hàng triệu chuyến đi mỗi ngày trên toàn cầu. Nhờ Cassandra, Uber có thể mở rộng dịch vụ của mình mà không lo lắng về giới hạn hiệu suất hay tính sẵn sàng.

## 1.5. Cassandra và các tính năng bị thiếu so với cơ sở dữ liệu quan hệ

Mặc dù Cassandra là một cơ sở dữ liệu mạnh mẽ, nhưng nó không thể thay thế hoàn toàn cơ sở dữ liệu quan hệ. Cassandra không hỗ trợ một số tính năng cơ bản của cơ sở dữ liệu quan hệ, như:

- **Joins**: Không hỗ trợ các truy vấn nối (joins) giữa các bảng.
- **Hỗ trợ tổng hợp hạn chế**: Khả năng thực hiện các phép tính tổng hợp như tính trung bình hoặc tổng số là hạn chế.
- **Hỗ trợ giao dịch hạn chế**: Giao dịch không phải là tính năng mạnh mẽ của Cassandra.

Ví dụ: Nếu bạn đang phát triển một hệ thống ngân hàng cần kiểm tra số dư tài khoản với nhiều yêu cầu giao dịch phức tạp, Cassandra có thể không phải là lựa chọn tốt nhất. Trong trường hợp này, bạn nên xem xét sử dụng các cơ sở dữ liệu quan hệ như PostgreSQL hoặc MySQL.

## 1.6. Các kịch bản sử dụng tốt nhất cho Apache Cassandra

Cassandra đặc biệt phù hợp với các ứng dụng có số lượng ghi lớn hơn số lượng đọc. Dưới đây là một số kịch bản mà Cassandra phát huy tốt nhất:

- **Ghi dữ liệu nhanh và không cần chỉnh sửa nhiều**: Khi dữ liệu đến theo kiểu thêm (append-only) và không cần cập nhật hay xóa nhiều. Ví dụ: Ghi lại toàn bộ các lượt nhấp chuột trên một trang web.
- **Truy cập dữ liệu qua khóa chính**: Khi dữ liệu được truy cập thông qua khóa chính (partition key).
- **Không yêu cầu các phép nối (joins)** hoặc tổng hợp phức tạp.

**Ví dụ thực tế:**

- **Ứng dụng phân tích dữ liệu thời gian thực**: Lưu trữ và phân tích các giao dịch trong thời gian thực cho các trang web thương mại điện tử.
- **Ứng dụng quản lý hồ sơ người dùng**: Quản lý thông tin hồ sơ người dùng cho các dịch vụ như cá nhân hóa trải nghiệm hoặc xác thực người dùng.

## 1.7. Trường hợp sử dụng Time Series

Cassandra rất hiệu quả trong việc xử lý dữ liệu dạng chuỗi thời gian (time series), nơi dữ liệu được ghi lại theo thứ tự thời gian. Một ví dụ phổ biến là các cảm biến thu thập dữ liệu về điều kiện thời tiết.

**Ví dụ**: Giả sử bạn có một hệ thống cảm biến đo nhiệt độ môi trường ở nhiều vị trí khác nhau. Dữ liệu này có thể được ghi lại liên tục và truy vấn theo khoảng thời gian nhất định để phân tích xu hướng biến đổi.

## 1.8. Architecture of ApacheCassandra

[Reading](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTVNraWxsc05ldHdvcmstQ1MwMTAxRU4tQ291cnNlcmEvbGFicy9yZWFkaW5nL0FyY2hpdGVjdHVyZV9vZl9DYXNzYW5kcmEubWQiLCJ0b29sX3R5cGUiOiJpbnN0cnVjdGlvbmFsLWxhYiIsImFkbWluIjpmYWxzZSwiaWF0IjoxNzExNDI0ODY0fQ.7ps3uuvqJC53T1bQpF6JA20hBRtkqcLRGVuxiCvfr-E)

# 2. Các tính năng chính của Apache Cassandra

## 2.1. Kiến trúc phân tán và phi tập trung của Apache Cassandra

![architecture](cassandra_architecture.png)

Apache Cassandra nổi bật với tính chất phân tán (distributed) và phi tập trung (decentralized). Đa số các cơ sở dữ liệu NoSQL đều hỗ trợ tính phân tán, nhưng Cassandra đặc biệt hơn nhờ khả năng phi tập trung.

- **Phân tán**: Cassandra cho phép các cụm (cluster) chạy trên nhiều máy khác nhau, nhưng từ góc nhìn của người dùng hoặc ứng dụng, hệ thống vẫn hiển thị như một khối thống nhất. Các máy chủ Cassandra sẽ xử lý và định tuyến yêu cầu của người dùng một cách tối ưu thông qua thông tin cung cấp từ máy khách Cassandra.

    - Ví dụ: Trong một dịch vụ video trực tuyến như Netflix, dữ liệu người dùng như lịch sử xem phim sẽ được phân tán trên nhiều máy chủ, nhưng người dùng vẫn có thể truy cập và nhận thông tin một cách liền mạch.

- **Phi tập trung**: Không có máy chủ "chính" hay "phụ" (primary-secondary) như ở nhiều hệ thống khác, mà tất cả các nút (node) trong Cassandra đều giống nhau và giao tiếp theo mô hình ngang hàng (peer-to-peer) thông qua giao thức gossip.

    - Ví dụ: Khi một nút trong hệ thống gặp sự cố, Cassandra vẫn đảm bảo rằng dữ liệu có thể truy cập được từ các nút khác mà không cần chuyển đổi vai trò của bất kỳ nút nào.
  
## 2.2. Sao chép (Replication), Khả năng mở rộng (Scalability) và tính khả dựng (Availability)

1. **Sao chép dữ liệu (Replication) trong Cassandra**

    Khi dữ liệu đã được phân phối trong cụm, Cassandra tiến hành sao chép dữ liệu. Số lượng bản sao được xác định bởi `replication factor` (hệ số sao chép). Các bản sao được phân phối theo chiều kim đồng hồ trong cụm, và Cassandra cũng quan tâm đến việc đặt các nút trên các rack và trung tâm dữ liệu khác nhau để tăng khả năng chịu lỗi.

    **Ví dụ**: Nếu có một hệ số sao chép là 3, Cassandra sẽ lưu trữ cùng một dữ liệu trên ba nút khác nhau, giúp tăng cường khả năng phục hồi khi một nút gặp lỗi.

---
2. **Khả năng mở rộng và tính khả dụng (Scalability & Availability)**

    **Khả năng mở rộng**: Cassandra có khả năng mở rộng rất linh hoạt. Khi cần thêm hiệu suất, bạn chỉ cần thêm nút vào cụm, và cụm sẽ tự động phân phối lại dữ liệu mà không cần phải khởi động lại hệ thống hay cấu hình lại.

    - Ví dụ: Nếu bạn có một hệ thống thương mại điện tử như Amazon, khi số lượng người mua hàng tăng mạnh trong dịp giảm giá, bạn có thể dễ dàng thêm máy chủ để xử lý lưu lượng truy cập cao hơn.

    **Khả dụng và nhất quán**: Theo định lý CAP, một hệ thống phân tán không thể vừa đảm bảo tính nhất quán (consistency) vừa đảm bảo tính khả dụng (availability) cùng lúc. Cassandra ưu tiên khả dụng hơn nhất quán, nghĩa là ngay cả khi một phần của cụm gặp lỗi, hệ thống vẫn có thể trả về dữ liệu từ các nút khác, mặc dù dữ liệu có thể không hoàn toàn chính xác ngay lập tức (tính nhất quán cuối cùng - eventual consistency).

    - Ví dụ: Trong hệ thống ngân hàng, nếu bạn cần cập nhật số dư tài khoản ngay lập tức và chính xác tuyệt đối, Cassandra có thể không phải lựa chọn tốt nhất. Tuy nhiên, nếu bạn chỉ cần ghi nhanh dữ liệu giao dịch mà không cần kiểm tra tức thì số dư, Cassandra có thể đảm bảo yêu cầu này.

## 2.3. Hiệu suất ghi dữ liệu cao và Ngôn ngữ CQL

1. **Hiệu suất ghi dữ liệu cao (High Write Throughput)**

    Một trong những ưu điểm nổi bật của Cassandra là khả năng ghi dữ liệu nhanh chóng, không cần đọc trước khi ghi. Khi dữ liệu được ghi vào Cassandra, chúng được ghi trực tiếp vào bộ nhớ và sau đó được đẩy xuống ổ đĩa theo thứ tự. Các bản ghi dữ liệu được lưu theo cách tuần tự để tối ưu hóa việc ghi, và dữ liệu sẽ được hợp nhất lại sau thông qua quá trình compaction.

    **Ví dụ**: Trong một trang web thương mại điện tử, việc lưu trữ các nhấp chuột của người dùng có thể tạo ra một lượng dữ liệu khổng lồ, và Cassandra có thể xử lý điều này mà không bị chậm trễ.

---
2. **Ngôn ngữ CQL (Cassandra Query Language)**

    CQL là ngôn ngữ truy vấn dữ liệu trong Cassandra, có cú pháp tương tự như SQL nhưng chỉ dừng lại ở mức cú pháp. Các thao tác như tạo bảng (create table), chèn dữ liệu (insert), cập nhật (update), và xóa dữ liệu (delete) đều có thể thực hiện thông qua CQL.

    Tuy nhiên, dù cú pháp CQL giống SQL, cách mà Cassandra xử lý các thao tác đọc và ghi dữ liệu khác hoàn toàn với cơ sở dữ liệu quan hệ (RDBMS).

    Ví dụ: Nếu bạn đã quen với việc sử dụng SQL để quản lý dữ liệu trong MySQL, bạn sẽ dễ dàng chuyển sang CQL để làm việc với Cassandra, nhưng bạn cần lưu ý rằng cách dữ liệu được phân phối và xử lý trong Cassandra sẽ khác biệt.

# 3. Mô Hình Dữ Liệu Apache Cassandra

## 3.1. Giới thiệu về Mô Hình Dữ Liệu Cassandra

Apache Cassandra là một hệ thống cơ sở dữ liệu NoSQL phân tán và phi tập trung, được thiết kế để quản lý một lượng lớn dữ liệu trên nhiều máy chủ (cluster). Mô hình dữ liệu của Cassandra tập trung vào việc tối ưu hóa hiệu suất truy vấn thông qua việc sử dụng **keyspace**, **bảng**, **khóa chính (primary key)**, và các **khóa phân vùng (partition key)**.

Ví dụ tạo một bảng trong Cassandra (bắt buộc phải chỉ định khóa)

```SQL
CREATE TABLE intro_cassandra.groups(
    groupid int,
    group_name text STATIC,
    username text,
    age int,
    PRIMARY KEY ((groupid), username));
```

## 3.2. Keyspace và Bảng trong Cassandra

**Keyspace** là đơn vị logic chứa nhiều bảng trong Cassandra, tương tự như một cơ sở dữ liệu trong hệ quản trị cơ sở dữ liệu quan hệ (RDBMS). Mỗi keyspace định nghĩa một số tùy chọn nhất định, nổi bật nhất là **chiến lược sao lưu** (replication strategy) cho dữ liệu trong các bảng.

**Ví dụ thực tế**: Nếu bạn có một ứng dụng quản lý người dùng, bạn có thể tạo một keyspace cho ứng dụng đó để chứa các bảng lưu thông tin người dùng, thông tin nhóm, và các bảng khác liên quan đến ứng dụng.

Các bảng trong Cassandra là các thực thể logic chứa dữ liệu, tương tự như bảng trong cơ sở dữ liệu quan hệ. Mỗi bảng được cấu trúc bằng cách xác định:

- Các cột (columns) để lưu trữ dữ liệu.
- **Khóa chính (primary key)**, bao gồm **khóa phân vùng** và **khóa sắp xếp (clustering key)**.

Bạn có thể tạo, xóa, hoặc thay đổi cấu trúc bảng mà không ảnh hưởng đến các hoạt động đang chạy trên dữ liệu.

## 3.3. Khóa chính trong Cassandra

Trong Cassandra, **khóa chính (primary key)** có hai vai trò chính:

- **Tối ưu hóa hiệu suất truy vấn**: Dữ liệu trong Cassandra được lưu trữ và truy xuất dựa trên cách truy vấn được thiết kế, do đó việc lựa chọn khóa chính phù hợp sẽ giúp tăng tốc độ truy vấn.
- **Đảm bảo tính duy nhất của dữ liệu**: Khóa chính giúp đảm bảo rằng mỗi dòng dữ liệu trong bảng là duy nhất.

Thành phần của Khóa Chính:

- **Khóa phân vùng (partition key)**: Đây là thành phần bắt buộc, xác định cách dữ liệu được phân bố trong các node của cluster. Mỗi khóa phân vùng sẽ được băm (hash) để xác định node nào trong cluster sẽ lưu trữ dữ liệu.
- **Khóa sắp xếp (clustering key)**: Là thành phần tùy chọn, giúp sắp xếp dữ liệu trong cùng một phân vùng theo một thứ tự nhất định.

Ví dụ: Giả sử bạn có bảng lưu thông tin nhóm với các cột `groupid`, `group_name`, và thông tin thành viên như `username` và `age`. Trong đó, khóa chính gồm:

- **Khóa phân vùng**: `groupid` - để xác định nhóm.
- **Khóa sắp xếp**: `username` - để sắp xếp các thành viên trong cùng nhóm.

Như vậy, mỗi phân vùng sẽ chứa dữ liệu của một nhóm, và các thành viên trong nhóm sẽ được sắp xếp dựa trên `username`.

## 3.4. Phân vùng và Tính Địa Phương của Dữ Liệu

Dữ liệu trong Cassandra được nhóm theo **khóa phân vùng** thành các phân vùng, và các phân vùng này được phân bố đều trên các node trong cluster. Quá trình phân bổ dựa trên một hàm băm được áp dụng lên khóa phân vùng.

Điều này giúp Cassandra có thể định vị dữ liệu nhanh chóng và giảm thiểu số lượng node cần được truy cập để trả lời các truy vấn. Trong trường hợp có nhiều node (hàng trăm hoặc hàng ngàn node), việc giới hạn số lượng node cần thiết để xử lý truy vấn là yếu tố quan trọng giúp cải thiện hiệu suất.

Ví dụ: Nếu bạn muốn truy vấn thông tin tất cả người dùng trong nhóm có `groupid = 12`, hệ thống chỉ cần truy cập vào một node chứa dữ liệu của nhóm đó để trả về kết quả, thay vì phải truy vấn toàn bộ cluster.

## 3.5. Bảng tĩnh và bảng động trong Cassandra

Cassandra hỗ trợ hai loại bảng chính:

- **Bảng tĩnh (static tables)**: Là các bảng có khóa chính **chỉ bao gồm khóa phân vùng mà không có khóa sắp xếp**. Mỗi phân vùng trong bảng tĩnh chỉ chứa một bản ghi (entry).
    - **Ví dụ**: Bảng lưu thông tin người dùng có khóa chính là `username`. Mỗi phân vùng sẽ chỉ chứa thông tin của một người dùng duy nhất.

![Bảng tĩnh](static_table.png)

- **Bảng động (dynamic tables)**: Là các bảng có khóa chính **bao gồm cả khóa phân vùng và khóa sắp xếp**. Điều này cho phép mỗi phân vùng chứa nhiều bản ghi khác nhau, được sắp xếp theo khóa sắp xếp.
    - **Ví dụ**: Bảng lưu thông tin thành viên của nhóm có khóa phân vùng là groupid và khóa sắp xếp là username. Mỗi nhóm có thể chứa nhiều thành viên, và các thành viên sẽ được sắp xếp theo tên trong cùng một nhóm.
  

## 3.6. Clustering Key trong Cassandra

Clustering key là thành phần thứ hai của khóa chính (primary key) và có vai trò quan trọng trong việc sắp xếp dữ liệu bên trong phân vùng (partition).

**Vai trò của Clustering Key:**

- **Sắp xếp dữ liệu**: Clustering key xác định cách sắp xếp dữ liệu trong một phân vùng. Dữ liệu có thể được sắp xếp theo thứ tự tăng dần hoặc giảm dần.
- **Tối ưu hóa truy vấn**: Clustering key giúp cải thiện hiệu suất đọc bằng cách giảm số lượng dữ liệu cần đọc trong một phân vùng.

**Ví dụ**: Giả sử chúng ta có bảng chứa thông tin các nhóm với `groupid` là khóa phân vùng, và `username` là clustering key. Dữ liệu bên trong mỗi phân vùng (tức mỗi nhóm) sẽ được sắp xếp theo thứ tự tăng dần của `username`. Khi truy vấn thông tin người dùng trong một nhóm, kết quả sẽ được trả về theo thứ tự sắp xếp đã định trước, giúp tăng hiệu suất truy vấn.

---
**Clustering Key và Hiệu suất truy vấn**

Giả sử bạn muốn truy vấn tất cả người dùng trong nhóm có `groupid = 12` và có `age = 32`. Để tối ưu hóa truy vấn này, bạn có thể thiết kế bảng với:

- **Khóa phân vùng**: `groupid`.
- **Clustering key**: `age` và `username`.

Dữ liệu trong mỗi phân vùng sẽ được sắp xếp trước tiên theo `age` và sau đó là `username`. Điều này giúp hệ thống chỉ cần tìm kiếm trong một lượng dữ liệu nhỏ, thay vì phải duyệt qua toàn bộ phân vùng. Kết quả là, Cassandra có thể trả về dữ liệu một cách nhanh chóng mà không cần phải đọc toàn bộ phân vùng, đặc biệt là trong các phân vùng lớn chứa hàng trăm megabyte dữ liệu.

**Ví dụ thực tế:**

Trong một hệ thống quản lý thành viên câu lạc bộ, nếu bạn cần truy vấn tất cả thành viên của nhóm có cùng độ tuổi, clustering key được sắp xếp theo `age` sẽ giúp bạn trả về kết quả nhanh hơn. Hệ thống chỉ cần đọc dữ liệu từ một phần nhỏ trong phân vùng, thay vì đọc tất cả thông tin của nhóm đó.

![example_clustering_key](example_clustering_key.png)

## 3.7. Bảng động (Dynamic Table)

**Bảng động** là các bảng mà dữ liệu bên trong phân vùng sẽ phát triển linh hoạt theo số lượng các bản ghi nhờ sự hiện diện của **clustering key** trong **khóa chính**. Điều này khác với **bảng tĩnh**, nơi mỗi phân vùng chỉ có một bản ghi.

- **Trong bảng động**, các phân vùng có thể chứa nhiều bản ghi, và các bản ghi này được sắp xếp theo thứ tự dựa trên clustering key.
- **Khi chèn dữ liệu mới**, dữ liệu sẽ được chèn vào vị trí thích hợp trong phân vùng, tăng kích thước phân vùng lên.

**Ví dụ thực tế:**

Giả sử bạn có bảng chứa thông tin nhóm với `groupid` là khóa phân vùng và `username` là clustering key. Khi bạn thêm một thành viên mới vào nhóm, dữ liệu sẽ được tự động chèn vào phân vùng tương ứng với `groupid`, và được sắp xếp theo `username`. Điều này giúp hệ thống dễ dàng quản lý và mở rộng dữ liệu khi nhóm có thêm thành viên mới.

## 3.8. Mô hình hóa dữ liệu trong Cassandra

Việc xây dựng mô hình dữ liệu trong Cassandra không chỉ dừng lại ở việc định nghĩa khóa chính, mà còn phụ thuộc vào các quy tắc quan trọng để tối ưu hóa hiệu suất truy vấn.

**Hướng dẫn cơ bản để xây dựng khóa chính:**

1. **Chọn khóa phân vùng hợp lý:**

   - Khóa phân vùng nên giúp phân bổ dữ liệu đều trên toàn bộ cluster.
   - Ví dụ, `groupid` có thể là một khóa phân vùng tốt nếu có nhiều nhóm với số lượng thành viên tương đối giống nhau.

2. **Tối ưu hóa để trả lời truy vấn với ít phân vùng nhất có thể:**

    Khi thiết kế khóa chính, bạn nên đảm bảo rằng hệ thống chỉ cần truy xuất dữ liệu từ một phân vùng để trả lời truy vấn. Điều này giúp giảm thời gian truy vấn và tránh tình trạng timeout.

3. **Sắp xếp dữ liệu theo clustering key để tối ưu hóa truy vấn:**

   - Việc chọn clustering key không chỉ để đảm bảo tính duy nhất của dữ liệu mà còn giúp sắp xếp và tối ưu hóa hiệu suất truy vấn.
   - Ví dụ: Nếu bạn cần truy vấn theo độ tuổi và tên người dùng, hãy chọn `age` và `username` làm **clustering key** để dữ liệu được sắp xếp theo thứ tự tăng dần hoặc giảm dần, tùy vào yêu cầu truy vấn.

**Ví dụ thực tế:**

Trong một hệ thống quản lý nhóm, bạn có thể thiết kế khóa chính với:

  - **Partition key**: `groupid` - để nhóm các thành viên theo nhóm.
  - **Clustering key**: `age`, `username` - để sắp xếp thành viên theo tuổi và tên trong mỗi nhóm.

Cấu trúc này giúp truy vấn thông tin thành viên trong nhóm theo độ tuổi nhanh chóng và chính xác, đồng thời giảm thiểu số lượng dữ liệu cần đọc từ mỗi phân vùng.

# 4. Giới Thiệu về Cassandra Query Language (CQL) Shell

## 4.1. Cassandra Query Language (CQL) là gì?

Cassandra Query Language (CQL) là ngôn ngữ chính để giao tiếp với các cụm Apache Cassandra. CQL có cú pháp đơn giản và trực quan, giống với SQL, cho phép bạn thực hiện các thao tác như tạo keyspace, tạo bảng, chèn dữ liệu, cập nhật, xóa và thực hiện các truy vấn SELECT.

Điểm tương đồng và khác biệt với SQL:

- **Tương đồng**: Cú pháp CQL giống SQL, giúp các nhà phát triển quen thuộc với SQL dễ dàng bắt đầu với CQL.
- **Khác biệt**: CQL không hỗ trợ các câu lệnh JOIN. Thay vào đó, bạn cần lưu trữ dữ liệu đã được kết hợp sẵn. Ngoài ra, các thao tác như INSERT, UPDATE và DELETE được thực hiện trực tiếp trong bộ nhớ mà không cần đọc trước để xác định dữ liệu.

Một số lệnh CQL cơ bản:

```SQL
CREATE KEYSPACE intro_cassandra WITH ...
CREATE TABLE test (...) ...
INSERT INTO test () VALUES (...) ...
SELECT * FROM test WHERE ...
UPDATE test SET age = 25 WHERE userid=30 ...
DELETE FROM test WHERE userid=30 ...
DROP TABLE test;
TRUNCATE TABLE test;
```

Ví dụ thực tế: Giả sử bạn có một bảng users trong Cassandra. Bạn có thể sử dụng CQL để tạo bảng, chèn dữ liệu và thực hiện các truy vấn như sau:

```SQL
-- Tạo bảng users
CREATE TABLE users (
    userid UUID PRIMARY KEY,
    name TEXT,
    email TEXT
);

-- Chèn dữ liệu vào bảng users
INSERT INTO users (userid, name, email) VALUES (uuid(), 'John Doe', 'john.doe@example.com');

-- Truy vấn dữ liệu
SELECT * FROM users WHERE userid = <some-uuid>;
```

## 4.2. Các tùy chọn để chạy các truy vấn CQL

Bạn có thể chạy các truy vấn CQL theo hai cách chính:

- **Chạy chương trình bằng cách sử dụng các driver client Cassandra**: Có nhiều lựa chọn bao gồm Java, Python, Scala, v.v. Driver mặc định thường là Datastax Java Driver.
- **Sử dụng CQL Shell client (cqlsh)**: Đây là một shell dòng lệnh dựa trên Python được cung cấp cùng với gói Cassandra, cho phép bạn giao tiếp trực tiếp với cụm Cassandra.

**Ví dụ thực tế**: Nếu bạn đang viết một ứng dụng Python và muốn tương tác với Cassandra, bạn có thể sử dụng thư viện `cassandra-driver` của DataStax:

```python
from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
session = cluster.connect('keyspace_name')

# Thực hiện truy vấn
rows = session.execute("SELECT * FROM users")
for row in rows:
    print(row.name, row.email)
```

---
**CQL SHELL (cqlsh)**

CQL Shell (cqlsh) là một shell dòng lệnh cho phép bạn chạy các truy vấn CQL trực tiếp trên cụm Cassandra. Nó cung cấp một giao diện tương tác để quản lý cơ sở dữ liệu, thực hiện các thao tác CRUD và quản lý keyspace cũng như bảng.

**Ví dụ thực tế**: Để mở CQL Shell, bạn chỉ cần chạy lệnh `cqlsh` trong terminal:

```bash
cqlsh [options][host[port]]
```

Trong đó Options:

- **--help**: Hiển thị trợ giúp về các tùy chọn lệnh của CQL Shell.
- **--version**: Kiểm tra phiên bản của CQL Shell đang sử dụng.
- **-u -user**: Để xác thực khi kết nối vào Cassandra.
- **-p -password**: Để xác thực khi kết nối vào Cassandra.
- **-k -keyspace**: Chỉ định keyspace để xác thực.
- **-f -file**: Cho phép thực hiện các lệnh từ một file cụ thể.
- **--request-timeout**: Đặt thời gian chờ cho các truy vấn; mặc định là 10 giây.

Sau khi kết nối thành công, bạn có thể bắt đầu thực hiện các truy vấn CQL như tạo bảng, chèn dữ liệu và truy vấn dữ liệu.

Ví dụ:
```bash
cqlsh -u AdminCherry -p 090924 -k campus_management
```

## 4.3. Các lệnh đặc biệt trong CQL Shell

CQL Shell cung cấp một số lệnh đặc biệt giúp bạn quản lý và tương tác với Cassandra hiệu quả hơn:

  - **CAPTURE**: Ghi lại kết quả của một lệnh và thêm vào một file.

    ```sql
    CAPTURE SELECT * FROM users TO 'output.csv';
    ```

- **CONSISTENCY**: Hiển thị mức độ nhất quán hiện tại và thiết lập mức độ mới.

    ```sql
    CONSISTENCY QUORUM;
    ```
- **COPY**: Sao chép dữ liệu vào và ra khỏi Cassandra.

    - **COPY TO**: Xuất dữ liệu từ bảng ra file CSV.

        ```sql
        COPY users TO 'users.csv' WITH HEADER = TRUE;
        ```

  - **COPY FROM**: Nhập dữ liệu từ file CSV vào bảng.

    ```sql
    COPY users FROM 'users.csv' WITH HEADER = TRUE;
    ```
- **DESCRIBE**: Mô tả cụm Cassandra và các đối tượng của nó.

    ```sql
    DESCRIBE KEYSPACE campus_management;
    ```

- **EXIT**: Kết thúc phiên làm việc trong CQL Shell.

    ```sql
    EXIT;
    ```
- **PAGING**: Bật hoặc tắt phân trang kết quả truy vấn.

    ```sql
    PAGING OFF;
    ```
- **TRACING**: Bật hoặc tắt theo dõi các yêu cầu.

    ```sql
    TRACING ON;
    ```
    
**Ví dụ thực tế**: 

- Để xuất dữ liệu từ bảng `users` vào file CSV:

    ```sql
    COPY users TO 'users.csv' WITH HEADER = TRUE;
    ```

- Để nhập dữ liệu từ file CSV vào bảng users:

    ```sql
    COPY users FROM 'users.csv' WITH HEADER = TRUE;
    ```

## 4.4. Chi tiết về các lệnh CONSISTENCY và COPY

**CONSISTENCY Command**

Cassandra hỗ trợ **tunable consistency**, tức là bạn có thể điều chỉnh mức độ nhất quán của dữ liệu tại cấp độ thao tác. Mức độ nhất quán xác định số lượng node (trong tổng số bản sao) cần phản hồi yêu cầu (ghi hoặc đọc) để thao tác được coi là thành công.

**Các tùy chọn consistency:**

- **ONE**: Chỉ cần một node trả lời.
- **TWO**, THREE: Cần hai hoặc ba node trả lời.
- **QUORUM**: Phần lớn node trong bản sao (ví dụ: 3 trong 5).
- **ALL**: Tất cả node trong bản sao phải trả lời.
- **LOCAL_QUORUM**: Phần lớn node trong trung tâm dữ liệu địa phương.

Ví dụ thực tế: Giả sử bạn có một cụm Cassandra gồm 8 node, phân phối trong hai trung tâm dữ liệu:

- **DC1**: replication factor 2
- **DC2**: replication factor 3

Tổng số bản sao là 5. Nếu bạn đặt `CONSISTENCY QUORUM` cho một thao tác ghi, ít nhất 3 node (từ cả hai trung tâm dữ liệu) phải trả lời để thao tác được coi là thành công.

```sql
CONSISTENCY QUORUM;
INSERT INTO users (userid, name, email) VALUES (uuid(), 'Alice', 'alice@example.com');
```

**COPY Command**

Lệnh COPY trong CQL Shell cho phép bạn nhập và xuất dữ liệu từ Cassandra một cách nhanh chóng bằng cách sử dụng file CSV.

- COPY TO: Xuất dữ liệu từ bảng vào file CSV.

    ```sql
    COPY users TO 'users_export.csv' WITH HEADER = TRUE;
    ```

- COPY FROM: Nhập dữ liệu từ file CSV vào bảng.

    ```sql
    COPY users FROM 'users_import.csv' WITH HEADER = TRUE;
    ```

**Lưu ý**: Mặc dù lệnh `COPY` tiện lợi cho việc thử nghiệm với dữ liệu nhỏ hoặc đã được định dạng sẵn, đối với các thao tác sao chép dữ liệu lớn, bạn nên sử dụng các phương pháp sao chép đặc biệt khác của Cassandra để đảm bảo hiệu suất và tính toàn vẹn của dữ liệu.

**Ví dụ thực tế**: Giả sử bạn muốn xuất toàn bộ dữ liệu từ bảng `users` vào file `users.csv` để phân tích sau này:

```sql
COPY users TO 'users.csv' WITH HEADER = TRUE;
```

Sau đó, bạn có thể chỉnh sửa file `users.csv` và nhập lại dữ liệu đã chỉnh sửa vào Cassandra:

```sql
COPY users FROM 'users.csv' WITH HEADER = TRUE;
```

**Lưu ý cuối cùng**: Khi sử dụng CQL và CQL Shell, hãy luôn bắt đầu từ việc xác định các truy vấn bạn cần trả lời, sau đó thiết kế khóa chính và mô hình dữ liệu dựa trên các truy vấn đó để tối ưu hóa hiệu suất và đảm bảo tính nhất quán của dữ liệu.

# 5. Hands-on Lab: Using the CQL Shell (cqlsh)

[Install Apache Cassandra](https://ultahost.com/knowledge-base/install-cassandra-ubuntu/)

[Lab Instruction](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAxNTFFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvQ2Fzc2FuZHJhL0xhYiUyMC0lMjBVc2luZyUyMHRoZSUyMENRTCUyMFNoZWxsLm1kIiwidG9vbF90eXBlIjoidGhlaWFkb2NrZXIiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTcyNDI1OTczM30.pxRev5SrqlOkblXireacLlxrFVR8bH8UyyMf2qfFJg4)

[Glossary: Cassandra Basic](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAxNTFFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvQ2Fzc2FuZHJhL0xhYiUyMC0lMjBVc2luZyUyMHRoZSUyMENRTCUyMFNoZWxsLm1kIiwidG9vbF90eXBlIjoidGhlaWFkb2NrZXIiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTcyNDI1OTczM30.pxRev5SrqlOkblXireacLlxrFVR8bH8UyyMf2qfFJg4)

# 6. Ngôn ngữ truy vấn Cassandra (CQL) - Các kiểu dữ liệu

Khi làm việc với cơ sở dữ liệu **NoSQL Cassandra**, ngôn ngữ truy vấn Cassandra (Cassandra Query Language - CQL) là công cụ quan trọng để tương tác với các cụm Cassandra. Một trong những yếu tố chính trong CQL là các kiểu dữ liệu, giúp chúng ta quản lý và lưu trữ dữ liệu theo cách có cấu trúc.

Hôm nay, chúng ta sẽ tìm hiểu các kiểu dữ liệu trong CQL bao gồm:

- Kiểu dữ liệu tích hợp sẵn (Built-in data types),
- Kiểu dữ liệu tập hợp (Collection data types),
- Kiểu dữ liệu do người dùng định nghĩa (User-defined data types - UDTs).

## 6.1. Kiểu dữ liệu tích hợp sẵn

Các kiểu dữ liệu tích hợp sẵn là các kiểu dữ liệu đã được định nghĩa sẵn trong Cassandra. Những kiểu này bao gồm:

- **Ascii**: Chuỗi ký tự ASCII.
- **Boolean**: Biến Boolean với giá trị true/false.
- **Decimal, Double, Float**: Các kiểu dữ liệu số, sử dụng cho các phép toán số học.
- **Int và Bigint**: Kiểu số nguyên, trong đó bigint là số nguyên 64-bit có khả năng lưu trữ dải số lớn hơn int.
- **Text và Varchar**: Chuỗi ký tự UTF8.

Ngoài ra, Cassandra còn hỗ trợ kiểu dữ liệu **Blob (Binary Large Object)**, cho phép lưu trữ các đối tượng nhị phân lớn như hình ảnh, âm thanh. Lưu ý rằng kích thước của một blob không nên vượt quá 1 MB để tránh gây quá tải cho hệ thống.

**Ví dụ thực tế:**

Giả sử bạn cần lưu trữ thông tin một tập tin hình ảnh của người dùng, bạn có thể sử dụng kiểu dữ liệu blob. Tuy nhiên, nếu kích thước tập tin vượt quá giới hạn 1MB, bạn cần chia nhỏ dữ liệu hoặc tìm một cách lưu trữ khác, như sử dụng hệ thống lưu trữ tệp ngoài.

## 6.2. Kiểu dữ liệu tập hợp

Các kiểu dữ liệu tập hợp trong Cassandra giúp bạn lưu trữ nhiều giá trị trong một cột duy nhất. Điều này đặc biệt hữu ích khi bạn cần quản lý các quan hệ 1-nhiều mà không sử dụng JOIN. Các kiểu dữ liệu tập hợp bao gồm:

- **List**: Danh sách các phần tử, trong đó thứ tự phần tử được duy trì. Ví dụ, khi lưu trữ các công việc mà người dùng đã từng làm, bạn có thể dùng list để lưu chúng theo thứ tự thời gian.
- **Map**: Cặp giá trị khóa và giá trị, ví dụ như lưu trữ thông tin lịch sử nhập dữ liệu theo ngày.
- **Set**: Tập hợp các phần tử không trùng lặp và được sắp xếp theo thứ tự. Bạn có thể sử dụng set để lưu trữ các địa chỉ email của người dùng mà không cho phép trùng lặp.

**Ví dụ thực tế:**

Giả sử bạn đang xây dựng một hệ thống quản lý công việc và muốn lưu lại danh sách các công việc mà người dùng đã từng đảm nhiệm. Bạn có thể sử dụng list để lưu trữ các công việc này theo thứ tự thời gian, đảm bảo mỗi lần thêm một công việc mới, hệ thống sẽ giữ nguyên thứ tự đã lưu.

```sql
ALTER TABLE users ADD jobs list<text>;
UPDATE users SET jobs = jobs + ['Giáo viên'] WHERE user_id = 123;
```

## 6.3. Kiểu dữ liệu do người dùng tự định nghĩa

Kiểu dữ liệu do người dùng định nghĩa (UDT) cho phép bạn tạo ra những cấu trúc dữ liệu phức tạp hơn, tương tự như việc lưu trữ một quan hệ 1-một. Ví dụ, bạn có thể lưu trữ một địa chỉ bao gồm số nhà, tên đường, thành phố, v.v. trong một cột duy nhất thay vì phải tạo nhiều cột riêng biệt.

Sau khi tạo kiểu dữ liệu UDT, bạn có thể sử dụng nó để khai báo các cột trong bảng. Điều này giúp đơn giản hóa cấu trúc dữ liệu và tăng hiệu quả quản lý.

**Ví dụ thực tế:**

Giả sử bạn muốn lưu trữ thông tin địa chỉ của người dùng bao gồm các thành phần như số nhà, tên đường và thành phố. Bạn có thể tạo một UDT như sau:

```sql
CREATE TYPE address (
  street text,
  city text,
  zipcode int
);
```

Sau đó, bạn có thể thêm UDT này vào bảng users để lưu trữ địa chỉ:

```sql
ALTER TABLE users ADD address frozen<address>;
```

## 6.4. Kết luận

Cassandra hỗ trợ nhiều kiểu dữ liệu khác nhau để phục vụ nhiều nhu cầu lưu trữ khác nhau. Trong đó, **kiểu dữ liệu tích hợp sẵn** là những kiểu cơ bản và dễ hiểu, **kiểu dữ liệu tập hợp** giúp giải quyết các quan hệ 1-nhiều mà không cần `JOIN`, và **UDT** giúp mô hình hóa các quan hệ 1-một với tính linh hoạt cao. Nắm vững các kiểu dữ liệu này sẽ giúp bạn thiết kế cơ sở dữ liệu Cassandra một cách hiệu quả và tối ưu cho các ứng dụng thực tế.

# 7. Các thao tác với Keyspace trong Apache Cassandra

Keyspace là một khái niệm cốt lõi trong cơ sở dữ liệu phân tán Apache Cassandra. Nó tương tự như một "schema" trong các hệ quản trị cơ sở dữ liệu quan hệ (RDBMS). Trước khi tạo bảng, bạn phải định nghĩa Keyspace, vì Cassandra không cung cấp một Keyspace mặc định. Keyspace là nơi chứa các bảng và quyết định cách dữ liệu được phân phối và sao lưu trong cụm Cassandra.

Sau bài giảng này, bạn sẽ hiểu rõ vai trò của Keyspace, cách tạo, chỉnh sửa và xóa Keyspace trong Cassandra, cũng như các khái niệm về replication factor (hệ số sao lưu) và replication strategy (chiến lược sao lưu).

# 7.1. Các khái niệm chính

- **Keyspace**: Chứa nhiều bảng (tables), và mỗi bảng chỉ thuộc về một keyspace duy nhất.
- **Replication**: Được xác định tại mức keyspace, giúp đảm bảo dữ liệu được sao lưu trên nhiều node (nút) khác nhau để tăng tính an toàn và sẵn sàng của hệ thống.
- **Replication Factor**: Xác định số lượng bản sao dữ liệu được đặt trên các node khác nhau.
- **Replication Strategy**: Xác định các node nào trong cụm sẽ chứa các bản sao của dữ liệu.

## 7.2. Tạo Keyspace và các yếu tố cần xem xét

Khi tạo một Keyspace mới, bạn cần chỉ định hai yếu tố chính:

- **Class**: Chỉ định chiến lược sao lưu (replication strategy).
- **Replication Factor**: Xác định số lượng bản sao tại mỗi trung tâm dữ liệu.

Ví dụ:

Chúng ta tạo một Keyspace với tên **intro_cassandra**, với hệ số sao lưu là 5, trong đó 3 bản sao được đặt tại **datacenter1** và 2 bản sao tại **datacenter2**.

```sql
CREATE KEYSPACE intro_cassandra
WITH replication = {
  'class': 'NetworkTopologyStrategy',
  'datacenter1': 3,
  'datacenter2': 2
};
```

Sau khi tạo Keyspace, bạn có thể dùng lệnh `DESCRIBE KEYSPACES` hoặc `DESCRIBE intro_cassandra` để kiểm tra Keyspace đã tạo.

## 7.3. Replication Factor và Replication Strategy

- **Replication Factor** xác định số lượng bản sao của dữ liệu sẽ được lưu trên các node khác nhau trong cụm.
- **Replication Strategy** chỉ định node nào trong cụm sẽ chứa các bản sao đó.

**Hai điều cần lưu ý:**

- Tất cả các bản sao đều quan trọng như nhau trong Cassandra. Không có bản sao chính hay bản sao phụ.
- Replication Factor không nên vượt quá số lượng node trong cụm Cassandra.

**Ví dụ với một cụm Cassandra 4 node:**

Giả sử cụm có 4 node trong datacenter1 với hệ số sao lưu là 3. Khi dữ liệu ban đầu được phân bổ cho node 1, Cassandra sẽ sao chép dữ liệu lên node 3 và node 4 (do node 2 và node 1 cùng rack, Cassandra sẽ ưu tiên đặt bản sao lên các rack khác nhau).

## 7.4. Sao lưu dữ liệu trong môi trường đa trung tâm dữ liệu

Khi triển khai Cassandra trong môi trường nhiều trung tâm dữ liệu (multidatacenter), bạn có thể chỉ định hệ số sao lưu cho từng trung tâm dữ liệu.
Ví dụ với 2 trung tâm dữ liệu:

Cụm Cassandra có hai trung tâm dữ liệu, và chúng ta muốn có hệ số sao lưu là 5, trong đó 3 bản sao tại datacenter1 và 2 bản sao tại datacenter2.

```sql
CREATE KEYSPACE intro_cassandra
WITH replication = {
  'class': 'NetworkTopologyStrategy',
  'datacenter1': 3,
  'datacenter2': 2
};
```

Dữ liệu sẽ được sao chép qua các node khác nhau trong hai trung tâm dữ liệu này dựa trên chiến lược sao lưu và vị trí của các rack.

## 7.5. Chỉnh sửa và xóa Keyspace

- **ALTER KEYSPACE**: Lệnh này cho phép thay đổi các thuộc tính của Keyspace, chẳng hạn như tăng hệ số sao lưu.

    Ví dụ, tăng hệ số sao lưu của **datacenter2** từ 2 lên 3:

    ```sql
    ALTER KEYSPACE intro_cassandra
    WITH replication = {
    'class': 'NetworkTopologyStrategy',
    'datacenter1': 3,
    'datacenter2': 3
    };
    ```

- **DROP KEYSPACE**: Lệnh này dùng để xóa Keyspace, bao gồm cả các bảng và dữ liệu chứa trong nó.

    ```sql
    DROP KEYSPACE intro_cassandra;
    ```

Cassandra sẽ tự động tạo snapshot trước khi xóa Keyspace để có thể khôi phục dữ liệu nếu cần.

## 7.6. Kết luận

Trong Cassandra, Keyspace là nền tảng cho việc quản lý dữ liệu. Việc tạo, chỉnh sửa và xóa Keyspace đòi hỏi sự hiểu biết về các yếu tố như hệ số sao lưu và chiến lược sao lưu. Với chiến lược đúng, bạn có thể đảm bảo dữ liệu được sao lưu hiệu quả, giảm thiểu rủi ro mất mát dữ liệu, và tăng tính khả dụng của hệ thống.

- **Replication Factor** xác định số lượng bản sao dữ liệu trên các node khác nhau.
- **Replication Strategy** xác định node nào sẽ chứa các bản sao.
- Các thao tác cơ bản với Keyspace bao gồm: `CREATE KEYSPACE`, `ALTER KEYSPACE`, và `DROP KEYSPACE`.

**Ví dụ thực tế**: Giả sử bạn đang xây dựng một hệ thống thương mại điện tử phân tán với khách hàng đến từ nhiều khu vực khác nhau. Bạn có thể tạo Keyspace để lưu trữ dữ liệu về giao dịch, với việc sao lưu dữ liệu trên nhiều trung tâm dữ liệu để đảm bảo độ sẵn sàng cao. Mỗi khi có sự cố xảy ra với một trung tâm dữ liệu, hệ thống vẫn có thể phục hồi từ bản sao ở các trung tâm khác.

# 8. Các thao tác với bảng trong Apache Cassandra

## 8.1. Giới thiệu về bảng

Trong Apache Cassandra, dữ liệu được tổ chức và lưu trữ dưới dạng bảng. Bảng không chỉ lưu dữ liệu mà còn định nghĩa cấu trúc lưu trữ của dữ liệu trên cấp độ cụm (cluster) và node. Trước khi khai báo bảng, bạn phải tạo **keyspace**, vì bảng sẽ luôn được tạo trong một keyspace đã tồn tại.

**Ví dụ thực tế:**

Giả sử bạn đang xây dựng một hệ thống quản lý người dùng với hàng triệu bản ghi. Bạn sẽ cần một keyspace chứa bảng thông tin người dùng, nơi bảng này định nghĩa cấu trúc dữ liệu của từng người dùng và cách dữ liệu sẽ được phân phối và lưu trữ qua các node trong hệ thống Cassandra.

## 8.2. Cú pháp tạo bảng

Cassandra sử dụng cú pháp CREATE TABLE để tạo bảng với cú pháp tổng quát như sau:

```sql
CREATE TABLE [IF NOT EXISTS] keyspace_name.table_name (
    column1 datatype,
    column2 datatype,
    ...
    PRIMARY KEY (column1)
);

    IF NOT EXISTS: Tùy chọn này ngăn việc tạo bảng mới nếu bảng đã tồn tại, tránh việc hiển thị lỗi khi bảng đã được tạo trước đó.
    PRIMARY KEY: Xác định khóa chính của bảng.
```

Ví dụ:

```sql
CREATE TABLE IF NOT EXISTS user_data (
    username TEXT PRIMARY KEY,
    email TEXT,
    age INT
);
```

Trong ví dụ trên, bảng `user_data` chứa các thông tin về người dùng, với username là khóa chính.

## 8.3. Tạo bảng tĩnh và động

- **Bảng tĩnh**: Khóa chính chỉ chứa một khóa phân vùng (partition key).
- **Bảng động**: Khóa chính bao gồm cả khóa phân vùng và khóa sắp xếp (clustering key).

Ví dụ về bảng tĩnh:

```sql
CREATE TABLE user_profile (
    username TEXT PRIMARY KEY,
    name TEXT,
    age INT
);
```

Ví dụ về bảng động:

```sql
CREATE TABLE group_members (
    groupid UUID,
    username TEXT STATIC,
    PRIMARY KEY (groupid, username)
);
```

Ở đây, bảng `group_members` có khóa chính bao gồm `groupid` làm khóa phân vùng và `username` làm khóa sắp xếp.

## 8.4. Các thuộc tính nâng cao của bảng

![describe_table](describe_table.png)

Một số thuộc tính và tùy chọn quan trọng của bảng trong Cassandra bao gồm:

- Clustering Order: Mặc định, dữ liệu trong partition được sắp xếp theo khóa sắp xếp (clustering key) theo thứ tự tăng dần.

    Ví dụ:

    ```sql
    CREATE TABLE group_members (
        groupid UUID,
        username TEXT,
        PRIMARY KEY (groupid, username)
    ) WITH CLUSTERING ORDER BY (username DESC);
    ```

- Time-To-Live (TTL): Cho phép đặt thời gian tồn tại cho dữ liệu. Sau khi hết thời gian này, dữ liệu sẽ bị xóa tự động.

    Ví dụ:

    ```sql
    INSERT INTO user_data (username, email, age) VALUES ('user1', 'user1@example.com', 25) USING TTL 300;
    ```

    Dữ liệu này sẽ bị xóa sau 300 giây (5 phút).

## 8.5. Ghi dữ liệu và quá trình lưu trữ

Dữ liệu ghi vào bảng được lưu trên đĩa trong ba trường hợp:

- Khi memtable đầy,
- Khi commit log đầy,
- Hoặc theo khoảng thời gian nhất định (được cấu hình riêng cho mỗi bảng).

Mặc định, Cassandra không kích hoạt việc lưu dữ liệu theo khoảng thời gian.

## 8.6. Chỉnh sửa và xóa bảng

- **ALTER TABLE**: Dùng để thêm hoặc xóa cột, đổi tên cột, hoặc thay đổi các thuộc tính của bảng.

    Ví dụ:

    ```sql
    ALTER TABLE user_data ADD phone_number TEXT;
    ```
    **Lưu ý rằng các thay đổi này chỉ áp dụng cho các cột thông thường, không áp dụng cho cột khóa chính. Nếu muốn thay đổi khóa chính, bạn cần tạo bảng mới và nhập lại dữ liệu.**

- **TRUNCATE**: Xóa tất cả dữ liệu trong bảng nhưng không xóa định nghĩa bảng.

- **DROP**: Xóa toàn bộ bảng cùng với dữ liệu và định nghĩa.

Trước khi xóa hoặc truncate bảng, Cassandra tự động chụp lại ảnh (snapshot) của dữ liệu để làm bản sao lưu, giúp khôi phục dữ liệu khi cần.

## 8.7. Kết luận

- Bảng trong Cassandra chứa dữ liệu và có thể bao gồm các cột tĩnh hoặc động.
- Khóa chính (PRIMARY KEY) quyết định cách dữ liệu được phân phối và lưu trữ trên các node.
- Bạn có thể thêm TTL để tự động xóa dữ liệu sau một khoảng thời gian xác định.
- Các thao tác chỉnh sửa bảng như thêm, xóa cột chỉ áp dụng với cột thường, không thể thay đổi khóa chính.

## 8.8. Hands-on Lab

[Keyspace Operations](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAxNTFFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvQ2Fzc2FuZHJhL0xhYiUyMC0lMjBLZXlzcGFjZV9PcGVyYXRpb25zLm1kIiwidG9vbF90eXBlIjoidGhlaWFkb2NrZXIiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTcyNDI1OTc1Nn0.xRbO06VRQWxvWvQ_afsB-EkMQUrmuhTxMDu1SsWKTVk)

[Cassandra Table Operations](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAxNTFFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvQ2Fzc2FuZHJhL0xhYiUyMC0lMjBUYWJsZV9PcGVyYXRpb25zLm1kIiwidG9vbF90eXBlIjoidGhlaWFkb2NrZXIiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTcyNDI1OTc0MX0.E_jSYrr0dH6UcA0nr_MPGrq7kaUrHuQIPYs9-IYudtM)

# 9. CRUD Operations trong Apache Cassandra (Phần 1: INSERT và UPDATE)

## 9.1 Quá trình ghi (Write) trong Cassandra

**a. Ghi dữ liệu tại cấp cụm (Cluster Level)**

![write_operation_node_level](write_operation_cluster_level.png)

**Trong Cassandra, khi một thao tác ghi diễn ra:**

Node nhận yêu cầu ghi sẽ đóng vai trò coordinator (điều phối viên), chịu trách nhiệm hoàn tất thao tác và trả kết quả về cho người dùng.
Dữ liệu sẽ được ghi vào tất cả các node chứa bản sao (replicas) của phân vùng, nhưng để thành công, Cassandra cần nhận được xác nhận từ một số lượng node tối thiểu dựa trên yếu tố consistency (độ nhất quán).

**Ví dụ:**

Keyspace có **Replication Factor = 3** và thao tác ghi có **Consistency = 2**.
Nếu phân vùng dữ liệu nằm trên các node 1, 2, và 3, và yêu cầu ghi đến node 4, thì node 4 sẽ gửi dữ liệu đến node 1, 2, và 3. Nếu node 2 không khả dụng, chỉ cần node 1 và 3 gửi xác nhận để đảm bảo đủ mức Consistency.

**b. Ghi dữ liệu tại cấp node (Node Level)**

![write_operation_cluster_level](write_operation_node_level.png)

- **Không cần đọc trước khi ghi**: Cassandra không cần kiểm tra dữ liệu hiện có trước khi thực hiện ghi, điều này giúp tối ưu hóa tốc độ.
- **Dữ liệu ghi vào bộ nhớ (Memtable)** và sau đó được ghi vào ổ đĩa dưới dạng các file SSTables. Khi bộ nhớ đầy, dữ liệu sẽ được chuyển từ bộ nhớ ra đĩa.
- **Mỗi thao tác ghi được gắn một timestamp**, giúp hệ thống quyết định dữ liệu mới nhất.


## 9.2 Lệnh INSERT trong Cassandra

**a. Quy tắc chung cho lệnh INSERT**

- Lệnh INSERT yêu cầu chỉ định khóa chính (primary key) đầy đủ. Điều này có nghĩa là mỗi lần ghi là cho từng bản ghi một.
- Do Cassandra không đọc dữ liệu trước khi ghi, nên thao tác INSERT có thể hoạt động như UPSERT (cập nhật nếu bản ghi đã tồn tại).
- Lệnh INSERT yêu cầu cung cấp giá trị cho các cột trong primary key, nhưng các cột khác không bắt buộc phải có dữ liệu.
- Có thể sử dụng Time-To-Live (TTL) cho dữ liệu, giúp xóa dữ liệu sau một khoảng thời gian định trước.

**b. Ví dụ:**

- Thêm hai người dùng vào nhóm làm bánh (group 12): Các cột bắt buộc như `username`, `groupid` phải được cung cấp.
- Thêm người dùng với TTL: Ví dụ, thêm một người dùng vào nhóm 25 với TTL 10 giây, sau 10 giây dữ liệu này sẽ không còn khả dụng để truy vấn.

## 9.3 Lệnh UPDATE trong Cassandra

**a. Quy tắc cho lệnh UPDATE**

Lệnh `UPDATE` có thể sử dụng để cập nhật dữ liệu, chẳng hạn như cập nhật tuổi người dùng trong nhóm.
Static column có thể được cập nhật mà không cần chỉ định khóa chính đầy đủ, chỉ cần chỉ định khóa phân vùng (partition key).

**b. Ví dụ:**

- Cập nhật tên nhóm 45: Bạn có thể cập nhật tên nhóm chỉ với **khóa phân vùng.**
- Cập nhật tuổi người dùng trong nhóm 12: Khi chạy `SELECT`, bạn sẽ thấy dữ liệu đã được cập nhật.

## 9.4. Lightweight Transactions (Giao dịch nhẹ)

**a. Chức năng của Lightweight Transactions**

- **Lightweight Transactions (LWT)** cho phép Cassandra thực hiện kiểm tra trước khi ghi. Điều này giúp ngăn chặn việc ghi đè dữ liệu không mong muốn.
- Sử dụng cú pháp `IF` để kiểm tra trước khi ghi.

**b. Ví dụ:**

- Chỉ cập nhật tuổi người dùng nếu dữ liệu đã tồn tại và tuổi hiện tại thỏa mãn điều kiện cụ thể.
- `INSERT IF NOT EXISTS`: Chỉ thêm dữ liệu nếu bản ghi chưa tồn tại.

**c. Nhược điểm của Lightweight Transactions:**

Giao dịch nhẹ chậm hơn khoảng 4 lần so với thao tác ghi thông thường, vì vậy chỉ nên sử dụng khi thật sự cần thiết.

## 9.5. Kết luận

- `INSERT` và `UPDATE` trong Cassandra có thể hoạt động tương tự nhau vì Cassandra không đọc dữ liệu trước khi ghi.
- **Lightweight Transactions** cung cấp cơ chế kiểm tra trước khi ghi, nhưng gây ảnh hưởng lớn đến hiệu suất.
- Khi ghi dữ liệu, Cassandra gửi dữ liệu đến tất cả các bản sao trong cụm, và chỉ yêu cầu xác nhận từ một số node tối thiểu dựa trên consistency level.

**Ví dụ thực tế:**

Trong một hệ thống thương mại điện tử, bạn có thể sử dụng Cassandra để quản lý thông tin người dùng. Lệnh INSERT sẽ tạo tài khoản người dùng mới, trong khi UPDATE sẽ được dùng để cập nhật thông tin tài khoản như địa chỉ giao hàng hoặc thông tin thanh toán. Lightweight Transactions có thể được dùng để đảm bảo không có tài khoản trùng lặp khi thêm người dùng mới.

# 10. CRUD trong Apache Cassandra – Phần 2: Đọc và Xóa dữ liệu

Khi bạn thực hiện một thao tác đọc trong Cassandra, nút nhận yêu cầu đọc sẽ trở thành coordinator (nút điều phối), có trách nhiệm thực hiện và hoàn thành thao tác đọc. Ví dụ, nếu thao tác đọc được gửi đến node 4, thì node này sẽ đóng vai trò là coordinator của thao tác đó.

Coordinator sẽ chỉ gửi yêu cầu đến số lượng node bằng với consistency level (mức độ nhất quán) đã được cấu hình. Ví dụ: nếu mức độ nhất quán là 2, thì chỉ có 2 trong số 3 node lưu trữ bản sao của dữ liệu được liên hệ để trả về kết quả. Khi các node phản hồi, coordinator sẽ xử lý và đồng bộ hóa dữ liệu dựa trên timestamps (dấu thời gian) để quyết định dữ liệu mới nhất, sau đó trả về kết quả cho người dùng.

## 10.1. Câu lệnh SELECT trong Cassandra

Để đọc dữ liệu trong Cassandra, chúng ta sử dụng câu lệnh `SELECT`. Dưới đây là một số quy tắc cần ghi nhớ khi sử dụng `SELECT` để đảm bảo hiệu suất tốt nhất:

- **Bắt đầu bằng khóa phân vùng (partition key)**: Mỗi truy vấn đọc phải bắt đầu bằng khóa phân vùng để giới hạn phạm vi dữ liệu cần đọc, điều này giúp chỉ các bản sao tương ứng với phân vùng đó được truy vấn.

- **Theo thứ tự các trường của khóa chính**: Đảm bảo rằng bạn tuân theo thứ tự của các trường khóa chính để có hiệu suất tối ưu. Ví dụ:
    - Nếu khóa chính gồm một khóa phân vùng và hai khóa phân cụm (clustering key), truy vấn theo thứ tự này sẽ có hiệu suất tốt hơn.

Một số thao tác được cho là **OK**:

- Lọc dựa trên giá trị khóa phân vùng.
- Lọc kết hợp khóa phân vùng và khóa phân cụm thứ nhất, thứ hai, v.v.

Các thao tác **không được khuyến nghị**:

- Không lọc tất cả dữ liệu: Việc truy vấn toàn bộ dữ liệu trong bảng (SELECT *) có thể dẫn đến việc gửi yêu cầu đến tất cả các node trong cluster, gây ảnh hưởng xấu đến hiệu suất.
- Không lọc theo cột thường (regular column): Nếu bạn cố gắng lọc theo một cột thường (không phải là một phần của khóa chính), Cassandra sẽ trả về lỗi.

![OK_and_not_OK](OK_and_not_OK.png)

![secondary_index](secondary_index.png)

**Ví dụ thực tế:**

Giả sử bạn có một bảng lưu trữ thông tin nhóm với khóa chính gồm `group ID` và `username`. Khi bạn thực hiện truy vấn dựa trên `group ID` hoặc kết hợp với `username`, kết quả sẽ trả về nhanh chóng và chính xác.

Ngược lại, nếu bạn cố gắng lọc theo cột `age` (một cột thường), hệ thống sẽ trả về lỗi. Để giải quyết điều này, bạn có thể tạo chỉ mục (index) trên cột `age`. Tuy nhiên, hiệu suất tốt nhất vẫn đạt được khi bạn kết hợp khóa phân vùng `group ID` trong truy vấn cùng với cột `age`.

## 10.2. Xóa dữ liệu trong Cassandra

Trong Cassandra, bạn có thể xóa dữ liệu theo nhiều cách khác nhau:

- **Xóa theo khóa chính** : Bạn có thể xóa một bản ghi cụ thể dựa trên khóa chính đầy đủ (full primary key).
- **Xóa một cell**: Bạn cũng có thể xóa một cell cụ thể trong một bản ghi, ví dụ, xóa cột `age` của một người dùng.

Ngoài ra, bạn có thể xóa dữ liệu ở mức độ lớn hơn:

- **Xóa theo phạm vi (range)**: Ví dụ, nếu bảng của bạn chứa dữ liệu từ các cảm biến (sensor ID) và dữ liệu được phân cụm theo thời gian, bạn có thể xóa tất cả các bản ghi từ 1:00 PM đến 3:00 PM cho một cảm biến cụ thể.
- **Xóa một phân vùng (partition)**: Điều này xóa toàn bộ dữ liệu thuộc về một khóa phân vùng nhất định.

**Cảnh báo khi xóa dữ liệu**

Việc xóa dữ liệu trong Cassandra không đơn giản như trong cơ sở dữ liệu quan hệ. Cassandra sử dụng tombstone để ghi nhận rằng dữ liệu đã bị xóa. Tuy nhiên, dữ liệu thực tế vẫn tồn tại trên ổ đĩa trong một khoảng thời gian cấu hình được gọi là gc_grace_seconds (thời gian mặc định là 10 ngày). Trong khoảng thời gian này, hệ thống vẫn có thể đồng bộ hóa và đảm bảo rằng dữ liệu đã xóa được cập nhật đúng trên tất cả các node.

**Tombstone là gì?**

- Tombstone là một giá trị đặc biệt được ghi vào hệ thống để đánh dấu rằng một bản ghi đã bị xóa. Dữ liệu được ghi với dấu thời gian của thao tác xóa (T1). Khi một yêu cầu đọc đến, Cassandra sẽ so sánh các dấu thời gian của dữ liệu từ các node khác nhau để quyết định dữ liệu nào mới nhất. Nếu một node chưa nhận được thao tác xóa và trả về dữ liệu cũ với dấu thời gian T0, coordinator sẽ chọn dữ liệu với dấu thời gian mới nhất (T1) và quyết định rằng bản ghi đã bị xóa.

## 10.3. Kết luận

- Đọc trong Cassandra chỉ liên quan đến số lượng node theo mức độ nhất quán đã được cấu hình.
- Xóa dữ liệu cần thận trọng, vì có thể ảnh hưởng đến hiệu suất hệ thống, đặc biệt trong môi trường phân tán.
- Tombstones giúp ghi nhận các thao tác xóa, nhưng chúng cần thời gian để được loại bỏ khỏi hệ thống, gây ra nguy cơ ảnh hưởng đến hiệu suất nếu sử dụng quá nhiều.

**Ví dụ thực tế:** Giả sử bạn có một ứng dụng theo dõi cảm biến và cần xóa dữ liệu từ một cảm biến giữa 1:00 PM và 3:00 PM. Bạn có thể thực hiện điều này bằng cách sử dụng câu lệnh xóa phạm vi dựa trên thời gian và khóa phân vùng. Tuy nhiên, hãy cân nhắc tần suất xóa dữ liệu và cấu hình hệ thống để tránh tích lũy quá nhiều tombstone, dẫn đến tình trạng quá tải.

# 11. Hands-on lab

[Lab Instruction](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAxNTFFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvQ2Fzc2FuZHJhL0xhYiUyMC0lMjBDUlVEX09wZXJhdGlvbnMubWQiLCJ0b29sX3R5cGUiOiJ0aGVpYWRvY2tlciIsImFkbWluIjpmYWxzZSwiaWF0IjoxNzI0MjU5NzQ3fQ.h7hLanOaYH7rAkXNbjJS-pJWto7Cb3WpKpWCpDCzz9s)
