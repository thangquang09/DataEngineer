- [1. Overview of NoSQL](#1-overview-of-nosql)
  - [1.1. What is NoSQL?](#11-what-is-nosql)
  - [1.2. Benefit of NoSQL](#12-benefit-of-nosql)
  - [1.3. History of NoSQL](#13-history-of-nosql)
  - [1.4. Why we use NoSQL?](#14-why-we-use-nosql)
  - [1.5. Summary](#15-summary)
- [2. Characteristics of NoSQL Databases](#2-characteristics-of-nosql-databases)
  - [2.1. What is NoSQL?](#21-what-is-nosql)
  - [2.2. Types of NoSQL Databases](#22-types-of-nosql-databases)
  - [2.3. Common Points](#23-common-points)
  - [2.4. Distributed and scalable (Phân tán và mở rộng)](#24-distributed-and-scalable-phân-tán-và-mở-rộng)
  - [2.5. Flexibility in Data Modeling](#25-flexibility-in-data-modeling)
  - [2.6. Benefit of Using NoSQL Databases](#26-benefit-of-using-nosql-databases)
  - [2.7. Summary](#27-summary)


# 1. Overview of NoSQL

## 1.1. What is NoSQL?

Tên gọi "NoSQL" xuất hiện lần đầu tiên trong một sự kiện thảo luận về các cơ sở dữ liệu phân tán mã nguồn mở mới và đã được chấp nhận rộng rãi kể từ đó. Ngược lại với cách hiểu thông thường, `NoSQL không có nghĩa là "No SQL" (không có SQL) mà là "Not Only SQL" (không chỉ là SQL)`. Điều này có nghĩa rằng NoSQL là một tập hợp các cơ sở dữ liệu có nhiều kiểu khác nhau nhưng đều `không tuân theo mô hình quan hệ truyền thống`. Chúng không phải là các hệ quản trị cơ sở dữ liệu quan hệ (RDBMS) thông thường, vốn lưu trữ dữ liệu theo các hàng và cột cố định. Do đó, một tên gọi khác có thể phù hợp hơn là "Non-relational" (phi quan hệ).

## 1.2. Benefit of NoSQL

NoSQL cung cấp các cách mới để lưu trữ và truy vấn dữ liệu, đặc biệt phù hợp với các ứng dụng hiện đại có nhu cầu thay đổi liên tục. Điểm quan trọng nhất là cơ sở dữ liệu NoSQL `không yêu cầu các lược đồ cố định`, phù hợp cho các trường hợp sử dụng cần phát triển và mở rộng. Ngoài ra, các cơ sở dữ liệu NoSQL còn có `khả năng phân tán ngang (horizontal scaling)`, cho phép tăng cường khả năng lưu trữ và xử lý dữ liệu khi nhu cầu tăng lên. Chúng cũng là các hệ thống phân tán tự nhiên, cung cấp tính chịu lỗi và khả dụng cao.

**KHẢ NĂNG PHÂN TÁN NGANG LÀ GÌ?**

Khả năng phân tán ngang (horizontal scalability) là khả năng `mở rộng hệ thống bằng cách thêm nhiều máy chủ` (hoặc nút) mới vào hệ thống `thay vì nâng cấp sức mạnh của một máy chủ duy nhất`. Trong hệ thống có khả năng phân tán ngang, dữ liệu và tải công việc được chia đều và phân phối qua nhiều máy chủ, giúp tăng khả năng xử lý mà không cần phụ thuộc vào phần cứng mạnh mẽ hơn của một máy chủ duy nhất.

Ví dụ để hiểu rõ hơn:

- **Mở rộng dọc (vertical scalability)**: Khi một cơ sở dữ liệu chỉ chạy trên một máy chủ duy nhất, để tăng hiệu suất, ta có thể phải nâng cấp phần cứng của máy chủ đó (tăng thêm RAM, CPU mạnh hơn, ổ cứng lớn hơn). Đây là mở rộng theo chiều dọc. Tuy nhiên, cách này có giới hạn vì phần cứng chỉ có thể được nâng cấp đến một mức độ nhất định.

- **Mở rộng ngang (horizontal scalability)**: Đối với các hệ thống NoSQL, thay vì nâng cấp một máy chủ duy nhất, chúng ta có thể thêm nhiều máy chủ mới và chia dữ liệu hoặc các yêu cầu truy vấn đến các máy chủ này. Khi lượng dữ liệu tăng lên hoặc số người dùng truy cập tăng, ta chỉ cần thêm nhiều máy chủ vào hệ thống, và dữ liệu được phân phối đồng đều giữa các máy chủ.

Ví dụ: Trong một ứng dụng thương mại điện tử, khi số lượng người dùng và các đơn đặt hàng tăng lên, cơ sở dữ liệu NoSQL có thể mở rộng dễ dàng bằng cách thêm nhiều máy chủ mà không cần phải thay đổi cấu trúc dữ liệu.

## 1.3. History of NoSQL

Lịch sử NoSQL có thể được chia thành hai giai đoạn chính:

- 1970-2000: Trong giai đoạn này, thị trường cơ sở dữ liệu bị thống trị bởi các cơ sở dữ liệu quan hệ như Oracle, IBM DB2, Microsoft SQL Server và MySQL. Các cơ sở dữ liệu phi quan hệ như IBM's IMS (sử dụng cho các sứ mệnh không gian Apollo) là ngoại lệ.
- Từ cuối những năm 1990: Với sự bùng nổ của các ứng dụng Internet trong thời kỳ "dot-com boom", các ứng dụng cần phục vụ hàng triệu người dùng công khai thay vì chỉ hàng nghìn nhân viên nội bộ. Điều này đặt ra nhu cầu mới về khả năng mở rộng và hiệu suất, thúc đẩy sự ra đời của các công nghệ cơ sở dữ liệu mới. Một số công ty lớn như Google, Amazon và IBM đã phát triển các công nghệ như MapReduce và Dynamo để xử lý khối lượng dữ liệu lớn trên các hệ thống phân tán. Nhiều cơ sở dữ liệu NoSQL đã ra đời từ các cộng đồng mã nguồn mở vào cuối những năm 2000, bao gồm Cassandra, MongoDB, CouchDB, HBase, Redis, và Neo4j.

![History of NoSQL](history_nosql.png)

## 1.4. Why we use NoSQL?

Có bốn lý do chính để sử dụng NoSQL trong các ứng dụng hiện đại:

- **Mô hình dữ liệu linh hoạt**: NoSQL hỗ trợ dữ liệu không có cấu trúc hoặc bán cấu trúc, dễ dàng hơn trong việc lưu trữ dữ liệu thay đổi thường xuyên.

- **Khả năng mở rộng theo chiều ngang**: NoSQL có khả năng tự động mở rộng mà không cần tái cấu trúc dữ liệu, giúp các ứng dụng xử lý nhiều dữ liệu và lưu lượng truy cập hơn.

- **Phù hợp với các ứng dụng hiện đại**: Các nhà phát triển có thể làm việc hiệu quả hơn với các cấu trúc dữ liệu phù hợp với nhu cầu đọc và ghi của ứng dụng.

- **Khả dụng cao và chịu lỗi**: NoSQL hoạt động trong môi trường phân tán, cung cấp tính khả dụng cao và khả năng chịu lỗi mà không cần phụ thuộc vào một máy chủ duy nhất.

Ví dụ: Một nền tảng mạng xã hội như Facebook có thể sử dụng NoSQL để lưu trữ hồ sơ người dùng trong cơ sở dữ liệu tài liệu (document database), lưu trữ thông tin bài đăng và hoạt động trong cơ sở dữ liệu cột (column database), và sử dụng cơ sở dữ liệu key-value để quản lý phiên đăng nhập của người dùng nhằm tăng tốc độ truy cập.

## 1.5. Summary

- NoSQL không có nghĩa là "Không SQL" mà là "Not Only SQL," ám chỉ các cơ sở dữ liệu phi quan hệ.
- Các cơ sở dữ liệu NoSQL xuất hiện như một phản ứng với nhu cầu ngày càng cao của các ứng dụng Internet lớn.
- Mặc dù các cơ sở dữ liệu NoSQL có sự khác biệt về cách triển khai, chúng đều có chung các tính năng như khả năng mở rộng ngang, tính chịu lỗi và khả dụng cao.
- NoSQL cung cấp các khả năng mạnh mẽ để xử lý dữ liệu không có cấu trúc và bán cấu trúc, phù hợp cho các ứng dụng hiện đại yêu cầu mở rộng linh hoạt.

# 2. Characteristics of NoSQL Databases

## 2.1. What is NoSQL?

Như đã thảo luận ở bài trước, một đặc điểm quan trọng nhất của NoSQL là chúng `không tuân theo kiến trúc quan hệ (non-relational)`. Nhưng các loại NoSQL nào hiện có và chúng có đặc điểm chung gì?

## 2.2. Types of NoSQL Databases

Theo sự đồng thuận chung, cơ sở dữ liệu NoSQL có thể được chia thành bốn loại chính:

- **Key-Value Stores (lưu trữ khóa-giá trị)**: Lưu trữ dữ liệu dưới dạng các cặp khóa và giá trị. Ví dụ như Redis, nơi các khóa có thể được sử dụng để truy cập nhanh dữ liệu.
- **Document Databases (cơ sở dữ liệu tài liệu)**: Lưu trữ dữ liệu dưới dạng tài liệu, thường ở định dạng JSON hoặc BSON. MongoDB là một ví dụ tiêu biểu.
- **Column-based Databases (cơ sở dữ liệu dạng cột)**: Lưu trữ dữ liệu thành các cột, giúp tối ưu hóa truy vấn dữ liệu lớn theo từng thuộc tính cụ thể. Apache Cassandra là một ví dụ nổi bật.
- **Graph Databases (cơ sở dữ liệu đồ thị)**: Quản lý dữ liệu dựa trên các quan hệ và kết nối giữa các nút dữ liệu. Neo4j là ví dụ điển hình cho cơ sở dữ liệu loại này.

Tuy có sự phân loại rõ ràng, nhưng đôi khi cũng có sự chồng chéo giữa các loại cơ sở dữ liệu NoSQL, dẫn đến việc khó xác định rõ ràng loại nào thuộc về loại nào.

## 2.3. Common Points

Một trong những điểm chung là **nguồn gốc mã nguồn mở**. Phần lớn các cơ sở dữ liệu NoSQL đều xuất phát từ cộng đồng mã nguồn mở, điều này đã thúc đẩy sự phát triển của chúng. Nhiều công ty đã thương mại hóa các sản phẩm mã nguồn mở và cung cấp dịch vụ hỗ trợ. Ví dụ:

- IBM Cloudant cho CouchDB,
- Datastax cho Apache Cassandra,
- MongoDB cũng có phiên bản mã nguồn mở của riêng mình.

## 2.4. Distributed and scalable (Phân tán và mở rộng)

Một đặc điểm quan trọng khác của NoSQL là chúng thường được xây dựng để có thể `phân tán ngang (horizontal scalability)`, nghĩa là có thể dễ dàng mở rộng bằng cách thêm nhiều máy chủ. Để làm được điều này, NoSQL thường `sử dụng khóa duy nhất toàn cục` để giúp quá trình phân mảnh dữ liệu (sharding) trở nên dễ dàng hơn.

## 2.5. Flexibility in Data Modeling

NoSQL đặc biệt phù hợp với những ứng dụng cần `mô hình dữ liệu linh hoạt`. `Thay vì bị ràng buộc` bởi các `lược đồ cố định` (fixed schemas) như trong cơ sở dữ liệu quan hệ (RDBMS), `NoSQL cho phép` sử dụng `lược đồ linh hoạt`, cho phép `dễ dàng thêm mới các tính năng` mà `không làm gián đoạn hệ thống`.

Ví dụ, với MongoDB, bạn có thể thêm các trường dữ liệu mới vào tài liệu mà không cần phải định nghĩa trước cấu trúc bảng, điều này giúp việc phát triển ứng dụng trở nên nhanh chóng hơn.

## 2.6. Benefit of Using NoSQL Databases

Vậy tại sao lại sử dụng cơ sở dữ liệu NoSQL? NoSQL đang ngày càng phổ biến vì những lý do sau:

- **Khả năng mở rộng**: NoSQL hỗ trợ mở rộng ngang (horizontal scalability) dễ dàng, giúp hệ thống đáp ứng được nhu cầu của các ứng dụng quy mô lớn, phân phối dữ liệu qua nhiều máy chủ, trung tâm dữ liệu.

- **Hiệu suất cao**: Với khả năng phân tán dữ liệu và sử dụng tài nguyên của nhiều máy chủ, NoSQL đảm bảo thời gian phản hồi nhanh ngay cả khi dữ liệu lớn và tải truy cập cao.

- **Khả năng chịu lỗi và tính khả dụng cao**: Các cơ sở dữ liệu NoSQL thường chạy trên cụm máy chủ với nhiều bản sao dữ liệu, điều này giúp hệ thống vẫn hoạt động bình thường ngay cả khi một máy chủ bị hỏng.

- **Tiết kiệm chi phí**: Nhờ sử dụng kiến trúc đám mây và hệ thống phân tán, NoSQL giúp tiết kiệm đáng kể chi phí so với các hệ thống cơ sở dữ liệu truyền thống chạy trên phần cứng đắt tiền.

- **Lược đồ linh hoạt**: Đối với các nhà phát triển, khả năng sử dụng lược đồ linh hoạt giúp xây dựng và triển khai tính năng mới mà không phải lo lắng về khóa cơ sở dữ liệu hay downtime.

- **Cấu trúc dữ liệu đa dạng**: NoSQL cung cấp nhiều cấu trúc dữ liệu khác nhau tùy theo nhu cầu, như:
    - Key-value stores cho việc tìm kiếm nhanh.
    - Document stores để lưu trữ dữ liệu phi chuẩn hóa.
    - Graph databases cho các mối quan hệ phức tạp.

Ví dụ: Một công ty truyền thông xã hội như Facebook có thể sử dụng:

- Cơ sở dữ liệu tài liệu (Document database) để lưu trữ thông tin hồ sơ người dùng,
- Cơ sở dữ liệu dạng cột (Column database) để quản lý các hoạt động của người dùng,
- Key-value store để quản lý các phiên truy cập của người dùng, tăng tốc độ truy xuất dữ liệu.

## 2.7. Summary

- NoSQL là cơ sở dữ liệu phi quan hệ với 4 loại chính: Key-Value, Document, Column-based, và Graph.
- NoSQL có nguồn gốc từ cộng đồng mã nguồn mở và có khả năng mở rộng linh hoạt, chịu lỗi tốt.
- Lợi ích chính của NoSQL bao gồm mở rộng ngang, hiệu suất cao, chi phí thấp, lược đồ linh hoạt, và cấu trúc dữ liệu đa dạng.

NoSQL đã mang đến những giải pháp hiệu quả cho những thách thức về hiệu suất, tính sẵn sàng và chi phí mà các hệ thống truyền thống không thể đáp ứng tốt. Tuy nhiên, vẫn có những trường hợp mà cơ sở dữ liệu quan hệ (RDBMS) có thể là lựa chọn tốt hơn, tùy thuộc vào yêu cầu cụ thể của hệ thống.