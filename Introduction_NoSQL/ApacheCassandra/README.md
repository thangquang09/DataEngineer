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

