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
  - [2.8. NoSQL Database Types and Use Cases](#28-nosql-database-types-and-use-cases)
    - [2.8.1. Document store databases](#281-document-store-databases)
    - [2.8.2. Key-value stores](#282-key-value-stores)
    - [2.8.3. Column-family stores](#283-column-family-stores)
    - [2.8.4. Graph Databases](#284-graph-databases)
    - [2.8.5. Wide-column stores](#285-wide-column-stores)
    - [2.8.6. Expanded use case example: Using MongoDB for a content management system (CMS)](#286-expanded-use-case-example-using-mongodb-for-a-content-management-system-cms)
  - [2.9. Key-Value NoSQL Databases](#29-key-value-nosql-databases)
    - [2.9.1. Architecture](#291-architecture)
    - [2.9.2. Practical Use Cases](#292-practical-use-cases)
    - [2.9.3. When we should not use Key-Value Databases?](#293-when-we-should-not-use-key-value-databases)
    - [2.9.4. Vendor](#294-vendor)
    - [2.9.5. Summary](#295-summary)
  - [2.10. Document-Based NoSQL Databases](#210-document-based-nosql-databases)
    - [2.10.1. Architecture](#2101-architecture)
    - [2.10.2. Practical Use Cases](#2102-practical-use-cases)
    - [2.10.3. When we should not use Document-Based NoSQL Databases?](#2103-when-we-should-not-use-document-based-nosql-databases)
    - [2.10.4. Vendor](#2104-vendor)
    - [2.10.5. Bonus: What is Map Reduce?](#2105-bonus-what-is-map-reduce)
      - [2.10.5.1. Architect](#21051-architect)
      - [2.10.5.2. Operation](#21052-operation)
      - [2.10.5.3. Example](#21053-example)
      - [2.10.5.4. Application](#21054-application)
      - [2.10.5.5. Advantages and Disadvantages](#21055-advantages-and-disadvantages)
  - [2.11. Column-Based NoSQL Databases](#211-column-based-nosql-databases)
    - [2.11.1. Architecture](#2111-architecture)
    - [2.11.2. Benefit](#2112-benefit)
    - [2.11.3. Practical Use Cases](#2113-practical-use-cases)
    - [2.11.4. Limitations](#2114-limitations)
    - [2.11.5. Application in Data Warehouse](#2115-application-in-data-warehouse)
    - [2.11.6. Vendor](#2116-vendor)
  - [2.12. Graph NoSQL Databases](#212-graph-nosql-databases)
    - [2.12.1. Architecture](#2121-architecture)
    - [2.12.2. Use Cases](#2122-use-cases)
    - [2.12.3. Unsuitable Cases](#2123-unsuitable-cases)
    - [2.12.4. Vendor](#2124-vendor)
- [3. Read more](#3-read-more)
- [4. Working with Distributed Data](#4-working-with-distributed-data)
  - [4.1. What is ACID and BASE?](#41-what-is-acid-and-base)
  - [4.2. Comparision](#42-comparision)
  - [4.3. Use Cases](#43-use-cases)
  - [4.4. Summary](#44-summary)
- [5. Distributed Databases](#5-distributed-databases)
  - [5.1. What is Distributed Database?](#51-what-is-distributed-database)
  - [5.2. Benefit](#52-benefit)
  - [5.3. Challenges](#53-challenges)
  - [5.4. Summary](#54-summary)
- [6. CAP Theorem](#6-cap-theorem)
  - [6.1. History of CAP Theorem](#61-history-of-cap-theorem)
  - [6.2. What is CAP Theorem?](#62-what-is-cap-theorem)
  - [6.3. Meaning of properties in CAP Theorem](#63-meaning-of-properties-in-cap-theorem)
  - [6.3. The Importance of Partition Tolerance](#63-the-importance-of-partition-tolerance)
  - [6.4. Classification of NoSQL systems according to the CAP Theorem](#64-classification-of-nosql-systems-according-to-the-cap-theorem)
  - [6.5. Summary](#65-summary)
- [7. Challenges in Migrating from RDBMS to NoSQL Databases](#7-challenges-in-migrating-from-rdbms-to-nosql-databases)
  - [7.1. Common Misunderstanding: Is NoSQL a Replacement for RDBMS?](#71-common-misunderstanding-is-nosql-a-replacement-for-rdbms)
  - [7.2. When to choose RDBMS and when to choose NoSQL?](#72-when-to-choose-rdbms-and-when-to-choose-nosql)
  - [7.3. Combines both RDBMS and NoSQL](#73-combines-both-rdbms-and-nosql)
  - [7.4. Design differences between RDBMS and NoSQL](#74-design-differences-between-rdbms-and-nosql)
  - [7.5. Considerable Problems](#75-considerable-problems)
  - [7.6. Summary](#76-summary)
- [8. Data Model Example in Relational vs Document](#8-data-model-example-in-relational-vs-document)
  - [8.1. Introduction](#81-introduction)
    - [8.1.1. Using a relational database for a library books catalog](#811-using-a-relational-database-for-a-library-books-catalog)
  - [8.1.2. Using a cocument database for a library books catalog](#812-using-a-cocument-database-for-a-library-books-catalog)
  - [8.2. Complexities of querying data](#82-complexities-of-querying-data)
    - [8.2.1. Querying book data using a relational database](#821-querying-book-data-using-a-relational-database)
    - [8.2.2. Querying book data using a NoSQL document database](#822-querying-book-data-using-a-nosql-document-database)
    - [8.2.3 Important! What about data duplication?](#823-important-what-about-data-duplication)
  - [8.3. Schema Evolution Considerations](#83-schema-evolution-considerations)


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

## 2.8. NoSQL Database Types and Use Cases

### 2.8.1. Document store databases

Document-store databases, còn được gọi là `document-orented databases`, lưu trữ dữ liệu ở định dạng tài liệu, `thường là JSON hoặc BSON (JSON nhị phân)` trong đó mỗi tài liệu chứa các cặp khóa-giá trị hoặc cặp khóa-tài liệu. Các cơ sở dữ liệu này `không có lược đồ`, cho phép linh hoạt trong cấu trúc dữ liệu trong bộ sưu tập.

**CÁC ĐẶC TRƯNG**

- Cung cấp tính linh hoạt của lược đồ: Tài liệu trong các bộ sưu tập có thể có các cấu trúc khác nhau, cho phép dễ dàng cập nhật và điều chỉnh các yêu cầu dữ liệu ngày càng phát triển.
- Thực hiện các hoạt động tạo, đọc, cập nhật và xóa (CRUD) hiệu quả: rất phù hợp cho các ứng dụng đọc và ghi chuyên sâu nhờ khả năng truy xuất toàn bộ tài liệu.
- Cung cấp khả năng mở rộng: khả năng mở rộng theo chiều ngang bằng cách phân chia dữ liệu trên các cụm.

**TRƯỜNG HỢP SỬ DỤNG**

- Hệ thống quản lý nội dung (CMS): Nền tảng CMS như WordPress sử dụng cơ sở dữ liệu lưu trữ tài liệu để lưu trữ nhanh và truy cập vào các loại nội dung như bài viết, hình ảnh và dữ liệu người dùng. (MongoDB)
- Thương mại điện tử: Nền tảng thương mại điện tử cần quản lý hiệu quả danh mục sản phẩm với các thuộc tính và thứ bậc đa dạng, phù hợp với tính chất năng động của danh sách sản phẩm thương mại điện tử. (Couchbase hoặc Amazon DocumentDB, sử dụng khả năng tương thích MongoDB)

**CÁC NHÀ CUNG CẤP ĐƯỢC ĐỀ CẬP THƯỜNG XUYÊN**

- MongoDB
- Couchbase
- Amazon DocumentDB

### 2.8.2. Key-value stores

Key-value stores là CSDL NoSQL đơn giản nhất, lưu trữ dữ liệu dưới dạng tập hợp khóa-giá trị, trong đó khóa là duy nhất và trỏ trực tiếp đến giá trị liên quan của nó.

**CÁC ĐẶC TRƯNG**

- Mang lại hiệu suất cao: hiệu quả cho các thao tác đọc và ghi, được tối ưu hóa để truy xuất nhanh chóng dựa trên các keys.
- Cung cấp khả năng mở rộng: dễ dàng mở rộng do cấu trúc đơn giản và khả năng phân phối dữ liệu trên các nút (nodes)
- Sử dụng bộ nhớ đệm để truy cập nhanh
- Cung cấp chức năng quản lý phiên
- Làm việc với hệ thống phân tán

**TRƯỜNG HỢP SỬ DỤNG**

- Nâng cao hiệu suất web bằng cách lưu vào bộ nhớ đệm dữ liệu được truy cập thường xuyên (Sử dụng Redis hoặc Memcached)
- E-commerce platforms, software applications, including gaming: Amazon DynamoDB provides a highly scalable key-value store, facilitating distributed systems' seamless operation by handling high traffic and scaling dynamically.

**CÁC NHÀ CUNG CẤP ĐƯỢC ĐỀ CẬP THƯỜNG XUYÊN**

- Redis
- Memcached
- Amazon DynamoDB

### 2.8.3. Column-family stores

Column-family stores NoSQL Databases, còn được gọi là CSDL cột, sắp xếp dữ liệu theo cột thay vì hàng. Các cơ sở dữ liệu này lưu trữ các cột dữ liệu cùng nhau, giúp chúng xử lý các tập dữ liệu lớn bằng lược đồ động một cách hiệu quả.

**CÁC ĐẶC TRƯNG**

- Sử dụng lưu trữ theo hướng cột: Dữ liệu được nhóm theo cột thay vì hàng, cho phép truy xuất hiệu quả các cột cụ thể.
- Cung cấp khả năng mở rộng: Kiến trúc phân tán mang lại tính sẵn sàng và khả năng mở rộng cao.

**TRƯỜNG HỢP SỬ DỤNG**

- Các ứng dụng IoT quản lý lượng lớn dữ liệu cảm biến một cách hiệu quả nhờ khả năng xử lý dữ liệu được đánh dấu thời gian trên quy mô lớn, được gọi là phân tích dữ liệu chuỗi thời gian. (Apache Cassandra)
- Các ứng dụng lưu trữ và phân tích sở thích và hành vi của người dùng thường mang lại khả năng cá nhân hóa. (HBase, một phần của hệ sinh thái Hadoop)
- Phân tích dữ liệu quy mô lớn.

**CÁC NHÀ CUNG CẤP ĐƯỢC ĐỀ CẬP THƯỜNG XUYÊN**

- Apache Cassandra
- Hbase

### 2.8.4. Graph Databases

Cơ sở dữ liệu Graph NoSQL được thiết kế để quản lý dữ liệu có tính liên kết cao, thể hiện các mối quan hệ với tư cách là công dân hạng nhất cùng với các nút và thuộc tính.

**CÁC ĐẶC TRƯNG**

- Phân tích dữ liệu bằng mô hình dữ liệu biểu đồ: các mối quan hệ cũng quan trọng như chính dữ liệu, cho phép truyền tải và truy vấn hiệu quả các mối quan hệ phức tạp.
- Hiệu suất nhanh cho truy vấn mối quan hệ: được tối ưu hóa cho các truy vấn liên quan đến mối quan hệ, khiến chúng trở nên lý tưởng cho mạng xã hội, hệ thống đề xuất và phân tích mạng.

**TRƯỜNG HỢP SỬ DỤNG**

- Mạng xã hội yêu cầu quản lý dữ liệu hiệu quả về mối quan hệ giữa người dùng, bài đăng, nhận xét và lượt thích. (Neo4j)
- Hệ thống đề xuất: Các tổ chức cần một cấu trúc cơ sở dữ liệu có thể tạo ra các công cụ đề xuất phức tạp, phân tích các mối quan hệ phức tạp giữa người dùng, sản phẩm và hành vi để đưa ra các đề xuất chính xác. (Amazon Neptune)

**CÁC NHÀ CUNG CẤP ĐƯỢC ĐỀ CẬP THƯỜNG XUYÊN**
- Neo4j
- Amazon Neptune
- ArangoDB Memcached

### 2.8.5. Wide-column stores

Wide-column store NoSQL databases sắp xếp dữ liệu theo bảng, hàng và cột, `giống như cơ sở dữ liệu quan hệ` nhưng có `lược đồ linh hoạt`.

**CÁC ĐẶC TRƯNG**

- Sử dụng lưu trữ theo cột: Dữ liệu được lưu trữ trong các cột, cho phép truy xuất hiệu quả các cột cụ thể thay vì toàn bộ hàng.
- Cung cấp khả năng mở rộng theo chiều ngang và khả năng chịu lỗi.

**TRƯỜNG HỢP SỬ DỤNG**

- Phân tích dữ liệu lớn: Xử lý hiệu quả việc xử lý dữ liệu quy mô lớn để phân tích dữ liệu lớn theo thời gian thực. (Apache HBase được sử dụng cùng với Hadoop)
- Quản lý nội dung doanh nghiệp: Cơ sở dữ liệu của các tổ chức lớn cần quản lý lượng lớn dữ liệu có cấu trúc như hồ sơ nhân viên hoặc hàng tồn kho đến hạn. (Cassandra)

**CÁC NHÀ CUNG CẤP ĐƯỢC ĐỀ CẬP THƯỜNG XUYÊN**
- Apache HBase
- Apache Cassandra

### 2.8.6. Expanded use case example: Using MongoDB for a content management system (CMS)

Hệ thống quản lý nội dung (CMS) thu thập, quản lý, quản lý và làm phong phú nội dung doanh nghiệp một cách thông minh, bao gồm các trang HTML, hình ảnh, bài viết, v.v. Hệ thống quản lý nội dung giúp các công ty triển khai nội dung của họ một cách hiệu quả và an toàn trên mọi đám mây và trong mọi ứng dụng.

Quản lý nội dung tốt có nghĩa là các thành viên trong nhóm có thể nhanh chóng thêm, cập nhật và xóa nội dung khỏi cơ sở dữ liệu cũng như các trang liên quan có nội dung đó. Các ví dụ bao gồm đưa ra tin nóng, cập nhật tin tức hiện tại, bao gồm dự báo thời tiết, quảng cáo nội dung, cập nhật chính sách tuyển sinh đại học, ra mắt các dịch vụ mới của thành phố, v.v.

Ví dụ: sử dụng MongoDB làm cơ sở dữ liệu phụ trợ cho hệ thống quản lý nội dung (CMS) là một lựa chọn thiết thực khi bạn cần quản lý và phục vụ nhiều loại nội dung khác nhau, đặc biệt là trong các tình huống mà bạn mong đợi các thay đổi lược đồ thường xuyên hoặc yêu cầu mở rộng quy mô.

Tiếp theo, hãy xem một số khía cạnh của việc quản lý nội dung bằng hệ thống quản lý nội dung, cụ thể là sử dụng MongoDB.

**Cấu trúc nội dung sử dụng MongoDB**

Trong MongoDB, bạn thể hiện nội dung dưới dạng tài liệu. Mỗi tài liệu tương ứng với một phần nội dung, chẳng hạn như bài viết, hình ảnh, video hoặc trang. Bạn có thể sử dụng các tài liệu phụ trong tài liệu để sắp xếp cấu trúc và phân cấp nội dung.

**Ví dụ về cấu trúc: Lưu trữ một bài viết blog**

Khi lưu trữ một bài đăng trên blog, bạn sẽ lưu trữ các thuộc tính cốt lõi như tiêu đề, nội dung, được tạo tại và URL hình ảnh. Sau đó, bằng cách sử dụng trường mảng, bạn có thể lưu trữ các thẻ. Các nhận xét về bài đăng đó được lưu trữ dưới dạng một mảng các đối tượng.

```python
// Collection: posts
{
"\_id":1,
"title":"Sample Blog Post",
"content":"This is the content of the blog post...",
"author":{
"name":"John Doe",
"email":"john@example.com",
"bio":"A passionate blogger.",
"created\_at":"2023-09-20T00:00:00Z"
},
"created\_at":"2023-09-20T08:00:00Z",
"tags":["mongodb","blogging","example"],
"comments":[
{
"text":"Great post!",
"author":"Emily Johnson",
"created\_at":"2023-09-20T10:00:00Z"
},
{
"text":"Thanks for sharing!",
"author":"James Martin",
"created\_at":"2023-09-20T11:00:00Z"
}
]
}
```

**META DATA AND INDEXING USING MongoDB**

Bạn có thể sử dụng khả năng lập chỉ mục của MongoDB để tối ưu hóa việc truy xuất nội dung. Bạn có thể tạo chỉ mục trên các trường thường được sử dụng để lọc hoặc tìm kiếm, chẳng hạn như từ khóa, ngày xuất bản hoặc loại nội dung hoặc sử dụng hỗ trợ chỉ mục văn bản của MongoDB cho truy vấn tìm kiếm văn bản trên các trường chứa nội dung chuỗi. Chỉ mục văn bản cải thiện hiệu suất khi tìm kiếm các từ hoặc cụm từ cụ thể trong nội dung chuỗi.

Ví dụ: bạn muốn cung cấp khả năng tìm kiếm trên nội dung blog của mình. Đầu tiên bạn sẽ tạo một chỉ mục văn bản:

```
db.articles.createIndex({subject: "text"})
```

Và sau đó bạn có thể cung cấp một truy vấn như:

```
db.posts.find({$text: {$search: "digital life"}})
```

nơi MongoDB sẽ tìm kiếm các phiên bản gốc của những từ này: `digital` hoặc `life`.

**MỞ RỘNG QUY MÔ CMS BẰNG MongoDB**

Khi CMS của bạn phát triển, MongoDB có thể giúp bạn mở rộng quy mô. Bạn có thể sử dụng phân đoạn để chia tỷ lệ theo chiều ngang hoặc sử dụng phân đoạn theo vùng để phân phối toàn cầu.

**Sử dụng sharding để chia tỷ lệ theo chiều ngang (tăng dung lượng)**

Hãy xem xét một công ty hiện có `100 triệu khách hàng`. Công ty này dự kiến ​​sẽ `mở rộng cơ sở khách hàng của mình lên 200 triệu khách hàng`. Số lượng khách hàng tăng lên đồng nghĩa với việc công ty sẽ `cần tăng gấp đôi phần cứng lưu trữ dữ liệu CNTT`. Công ty `có thể mở rộng quy mô theo chiều dọc`, điều này có thể khiến `chi phí tăng lên theo cấp số nhân vì chi phí phần cứng không tỷ lệ tuyến tính với hiệu suất`. Sơ đồ sau đây cho thấy công ty có thể mở rộng quy mô theo chiều ngang và sử dụng sharding để quản lý cơ sở dữ liệu.

![diagrame show horizontal scale](horizontal_scale.png)

Tuy nhiên, việc sử dụng sharding để mở rộng quy mô theo chiều ngang mang lại cho công ty thông lượng gấp đôi với chi phí gấp đôi.

## 2.9. Key-Value NoSQL Databases

### 2.9.1. Architecture

Trong cơ sở dữ liệu dạng Key-Value, tất cả dữ liệu được lưu trữ dưới dạng cặp khóa (key) và giá trị (value) tương ứng. Về mặt kiến trúc, đây là loại cơ sở dữ liệu đơn giản nhất trong các hệ thống NoSQL.

- Dữ liệu được lưu trữ dưới dạng bảng băm (hash map). Điều này giúp cho các thao tác cơ bản như tạo, đọc, cập nhật, và xóa (CRUD) trở nên cực kỳ nhanh chóng.
- Khả năng phân mảnh (sharding) dữ liệu cũng rất dễ thực hiện trong cơ sở dữ liệu Key-Value. Mỗi phần dữ liệu sẽ chứa một dải khóa và các giá trị tương ứng, từ đó giúp cơ sở dữ liệu mở rộng theo chiều ngang tốt hơn.

Tuy nhiên, một điểm hạn chế của loại cơ sở dữ liệu này là nó không phù hợp cho các truy vấn phức tạp liên quan đến nhiều mối quan hệ giữa các phần dữ liệu. Hệ thống Key-Value thường chỉ hỗ trợ các thao tác atomic trên các thao tác với một khóa duy nhất.

### 2.9.2. Practical Use Cases

Key-Value databases thường được sử dụng khi cần:

- Hiệu suất cao cho các thao tác CRUD cơ bản.
- Dữ liệu không có mối liên hệ phức tạp giữa các phần tử.

Ví dụ thực tiễn:

- Lưu trữ thông tin phiên làm việc của người dùng cho ứng dụng web. Mỗi phiên làm việc sẽ có một khóa duy nhất và tất cả dữ liệu của phiên làm việc đó sẽ được lưu trữ trong giá trị blob. Vì chúng ta không cần phải truy vấn dựa trên thông tin bên trong blob, mà chỉ cần dựa vào khóa, Key-Value database là một lựa chọn phù hợp.

- Lưu trữ hồ sơ người dùng và tùy chỉnh trong ứng dụng. Mỗi người dùng sẽ có một khóa duy nhất đại diện cho hồ sơ của họ, còn tất cả các dữ liệu liên quan sẽ được lưu trong giá trị blob.

- Lưu trữ dữ liệu giỏ hàng cho các cửa hàng trực tuyến. Mỗi giỏ hàng sẽ có một khóa duy nhất, và tất cả các sản phẩm trong giỏ hàng sẽ được lưu trữ trong blob. Với các tác vụ cơ bản như thêm, xóa sản phẩm, Key-Value database có thể đáp ứng tốt.

### 2.9.3. When we should not use Key-Value Databases?

Dù Key-Value databases có nhiều ưu điểm, nhưng cũng có những trường hợp mà loại cơ sở dữ liệu này không phù hợp:

- D**ữ liệu có nhiều mối quan hệ phức tạp**: Ví dụ, trong các mạng xã hội hoặc các hệ thống đề xuất, dữ liệu có nhiều mối quan hệ nhiều-nhiều. Trong những trường hợp này, cơ sở dữ liệu Key-Value sẽ gặp khó khăn và không đảm bảo hiệu suất tốt.

- **Giao dịch phức tạp và yêu cầu tính toàn vẹn cao**: Nếu ứng dụng yêu cầu thực hiện giao dịch đa thao tác với nhiều khóa khác nhau và cần đảm bảo tính toàn vẹn và đồng bộ (theo mô hình ACID - atomicity, consistency, isolation, durability), Key-Value databases sẽ không phải là lựa chọn tốt.

- **Nhu cầu truy vấn dựa trên giá trị thay vì khóa**: Nếu bạn cần phải truy vấn dựa trên thông tin bên trong giá trị blob thay vì khóa, hãy cân nhắc sử dụng các cơ sở dữ liệu dạng tài liệu (Document databases) để có nhiều tính linh hoạt hơn.

### 2.9.4. Vendor

Một số ví dụ về cơ sở dữ liệu NoSQL dạng Key-Value phổ biến hiện nay bao gồm:

- **Amazon DynamoDB**: Hỗ trợ khả năng mở rộng tự động và hiệu suất cao cho các ứng dụng web quy mô lớn.
- **Oracle NoSQL Database**: Giải pháp từ Oracle cho các ứng dụng yêu cầu khả năng lưu trữ đơn giản và hiệu suất cao.
- **Redis**: Là hệ thống Key-Value với khả năng truy xuất dữ liệu cực nhanh, thường được dùng làm bộ nhớ đệm (cache).
- **MemcacheDB**: Cơ sở dữ liệu Key-Value dành cho các ứng dụng yêu cầu truy vấn nhanh và đơn giản.
- **Project Voldemort**: Được phát triển bởi LinkedIn, nó giúp xử lý các tác vụ lưu trữ và truy vấn đơn giản.

### 2.9.5. Summary

Tổng kết lại, ta có

- Bốn loại chính của cơ sở dữ liệu NoSQL: Key-Value, Document, Column, và Graph.
- Key-Value databases là loại cơ sở dữ liệu đơn giản nhất về mặt kiến trúc, sử dụng cặp khóa-giá trị để lưu trữ dữ liệu và được biểu diễn dưới dạng bảng băm.
- Các trường hợp sử dụng phổ biến của Key-Value databases bao gồm lưu trữ thông tin phiên làm việc, hồ sơ người dùng, và giỏ hàng cho các cửa hàng trực tuyến.
- Tuy nhiên, Key-Value databases không phù hợp cho các hệ thống yêu cầu truy vấn phức tạp, nhiều mối quan hệ dữ liệu, hoặc yêu cầu giao dịch đa thao tác với tính toàn vẹn cao.

Key-Value databases là một lựa chọn tuyệt vời cho các ứng dụng cần xử lý dữ liệu nhanh và đơn giản, nhưng nếu hệ thống của bạn yêu cầu các tính năng phức tạp hơn, bạn có thể cân nhắc sử dụng các loại NoSQL khác như Document hoặc Graph databases.

## 2.10. Document-Based NoSQL Databases

### 2.10.1. Architecture

Cơ sở dữ liệu document là sự mở rộng của mô hình `Key-Value` nhưng cung cấp nhiều tính năng hơn bằng cách cho phép dữ liệu có thể được truy vấn và hiển thị chi tiết hơn. Thay vì giá trị chỉ đơn thuần là một blob (như trong mô hình Key-Value), trong mô hình này, giá trị sẽ được lưu trữ dưới dạng `document` – thông thường là các tệp `JSON` hoặc `XML`.

Một điểm đặc biệt của cơ sở dữ liệu dạng document là chúng có `schema linh hoạt`. Điều này có nghĩa là mỗi document có thể chứa thông tin hoàn toàn khác nhau và không cần phải có cùng cấu trúc dữ liệu. Đây là một lợi thế lớn khi bạn muốn lưu trữ dữ liệu không đồng nhất, vì bạn không bị ràng buộc vào các bảng cố định như trong cơ sở dữ liệu quan hệ.

Cơ sở dữ liệu document cũng cung cấp khả năng `truy vấn` và `lập chỉ mục` trên nội dung của document, giúp bạn thực hiện các thao tác tìm kiếm từ khóa hoặc các truy vấn phức tạp. Ngoài ra, chúng hỗ trợ các phép tìm kiếm theo phạm vi hoặc các truy vấn phân tích dựa trên các mô hình như `MapReduce`.

Hơn nữa, tương tự như các cơ sở dữ liệu NoSQL khác, cơ sở dữ liệu document có `khả năng phân tán ngang (horizontal scalability)`, tức là chúng có thể được mở rộng bằng cách phân chia dữ liệu giữa nhiều node khác nhau, và thường việc phân chia này được thực hiện dựa trên một khóa duy nhất của document.

### 2.10.2. Practical Use Cases

- **Logging sự kiện (Event Logging)**: Một trường hợp sử dụng điển hình của cơ sở dữ liệu document là ghi nhận sự kiện trong các ứng dụng hoặc quy trình. Mỗi sự kiện sẽ được lưu trữ dưới dạng một document, chứa tất cả các thông tin liên quan như thời gian sự kiện xảy ra, nội dung sự kiện, và các thông số khác. Điều này rất hữu ích cho việc theo dõi hành vi của hệ thống hoặc các ứng dụng lớn.
- **Blog trực tuyến**: Ví dụ thứ hai là trong các hệ thống blog trực tuyến. Mỗi bài viết của người dùng sẽ được lưu dưới dạng một document. Document này có thể chứa các thông tin như tên người viết, nội dung bài viết, và thời gian đăng bài. Ngoài ra, mỗi bình luận, lượt thích (like) hay hành động trên bài viết cũng sẽ được lưu trữ dưới dạng các document riêng biệt. Với cấu trúc linh hoạt, cơ sở dữ liệu document rất phù hợp để quản lý dữ liệu dạng phi cấu trúc như nội dung blog.
- **Ứng dụng web và di động**: Cơ sở dữ liệu document cũng được sử dụng rộng rãi trong các ứng dụng web và di động hiện đại. Với tính linh hoạt trong việc lưu trữ dữ liệu phi cấu trúc, cùng khả năng tương tác tốt với các API RESTful, loại cơ sở dữ liệu này hỗ trợ rất tốt cho việc lưu trữ và quản lý dữ liệu hoạt động của ứng dụng. Ví dụ, dữ liệu người dùng, dữ liệu sản phẩm, hoặc thông tin giao dịch có thể được lưu trữ dưới dạng các document.

### 2.10.3. When we should not use Document-Based NoSQL Databases?

Mặc dù cơ sở dữ liệu document có rất nhiều ưu điểm, nhưng chúng không phải lúc nào cũng là lựa chọn tốt nhất. Có một số trường hợp mà bạn nên cân nhắc sử dụng cơ sở dữ liệu quan hệ (RDBMS) thay vì NoSQL dạng document:
- **Giao dịch ACID (Atomicity, Consistency, Isolation, Durability)**: Nếu ứng dụng của bạn yêu cầu tính `toàn vẹn giao dịch cao` (ACID), đặc biệt là với các giao dịch đòi hỏi thao tác trên nhiều document cùng một lúc, cơ sở dữ liệu document có thể không phù hợp. Loại cơ sở dữ liệu này chỉ đảm bảo tính atomic cho các thao tác trên từng document riêng lẻ, vì vậy nếu bạn cần thực hiện các giao dịch phức tạp, cơ sở dữ liệu quan hệ sẽ là lựa chọn tốt hơn.
- **Mô hình dữ liệu dạng bảng (Normalized Data)**: Nếu dữ liệu của bạn tự nhiên phù hợp với mô hình dữ liệu đã chuẩn hóa (normalized) hoặc dạng bảng, việc ép buộc dữ liệu vào một thiết kế dạng document có thể không hiệu quả. Trong trường hợp này, sử dụng cơ sở dữ liệu quan hệ sẽ mang lại hiệu quả cao hơn trong việc lưu trữ và quản lý dữ liệu.

### 2.10.4. Vendor

Hiện nay, cơ sở dữ liệu document là một trong những loại cơ sở dữ liệu NoSQL được sử dụng rộng rãi nhất. Một số hệ thống NoSQL dạng document phổ biến bao gồm:

- IBM Cloudant
- MongoDB
- Apache CouchDB
- Terrastore
- OrientDB
- Couchbase
- RavenDB

### 2.10.5. Bonus: What is Map Reduce?

#### 2.10.5.1. Architect

Mô hình MapReduce có hai bước chính:

- Map: Trong giai đoạn này, dữ liệu đầu vào được chia thành nhiều phần nhỏ (các mảng dữ liệu nhỏ hơn) và được xử lý song song. Mỗi phần dữ liệu sẽ được ánh xạ (map) thành một cặp key-value. Từ đây, các giá trị sẽ được nhóm lại theo khóa (key).

- Reduce: Giai đoạn này tập trung vào việc tổng hợp (reduce) các kết quả được sinh ra từ giai đoạn Map. Các cặp key-value giống nhau sẽ được gom lại và xử lý để trả về kết quả cuối cùng.

#### 2.10.5.2. Operation

MapReduce hoạt động dựa trên một mô hình phân tán dữ liệu. Dữ liệu đầu vào (có thể là tệp lớn, như tệp log hoặc cơ sở dữ liệu phân tán) sẽ được chia nhỏ thành các phần (splits) và phân phối cho các node khác nhau trong hệ thống để xử lý. Sau đó:

- Trong giai đoạn Map, mỗi node xử lý từng phần dữ liệu và biến đổi nó thành cặp key-value.
- Sau đó, tất cả các kết quả sẽ được thu thập và chuyển qua giai đoạn Reduce. Trong giai đoạn này, các giá trị có cùng khóa sẽ được nhóm lại và xử lý để tạo ra kết quả cuối cùng.

#### 2.10.5.3. Example

Giả sử bạn có một tập dữ liệu lớn chứa danh sách từ ngữ trong một loạt các văn bản, và bạn muốn đếm số lần mỗi từ xuất hiện. Quá trình thực hiện bằng MapReduce sẽ như sau:

- **Giai đoạn Map:**
  - Đọc từng dòng văn bản và tách ra thành các từ.
  - Gán mỗi từ với giá trị "1" (cặp key-value: từ - số lần xuất hiện).
  - Ví dụ: từ "apple" sẽ trở thành cặp ("apple", 1).

- **Giai đoạn Shuffle:** Gom nhóm các từ giống nhau lại với nhau (tức là gom các key giống nhau).

- **Giai đoạn Reduce:**
  - Tổng hợp tất cả các cặp có cùng khóa lại để tính tổng số lần từ đó xuất hiện.
  - Ví dụ: với từ "apple", nếu nó xuất hiện trong các bản ghi khác nhau, bạn sẽ cộng tất cả các giá trị "1" để tìm ra tổng số lần từ "apple" xuất hiện.

Kết quả cuối cùng sẽ là một danh sách các từ và số lần chúng xuất hiện trong tập dữ liệu lớn.

#### 2.10.5.4. Application

MapReduce thường được sử dụng trong các hệ thống dữ liệu lớn, ví dụ như:

- **Phân tích log**: Để xử lý và phân tích khối lượng lớn dữ liệu log của các máy chủ.
- **Tìm kiếm web**: Các công cụ tìm kiếm như Google sử dụng MapReduce để lập chỉ mục các trang web trên quy mô lớn.
- **Phân tích dữ liệu lớn**: Trong các hệ thống như Hadoop, MapReduce được sử dụng để thực hiện các phân tích dữ liệu lớn, giúp xử lý các tập dữ liệu lớn một cách nhanh chóng và hiệu quả.

#### 2.10.5.5. Advantages and Disadvantages

- Ưu điểm:
  - Phân tán: MapReduce có thể xử lý khối lượng lớn dữ liệu trên nhiều máy tính song song, giúp tăng hiệu suất và giảm thời gian xử lý.
  - Chịu lỗi: Hệ thống phân tán có khả năng khôi phục dữ liệu nếu một node gặp sự cố.
  - Dễ mở rộng: Có thể mở rộng quy mô xử lý bằng cách thêm nhiều node vào hệ thống.

- Nhược điểm:
  - Độ trễ: Do các thao tác chia nhỏ và tổng hợp dữ liệu, mô hình MapReduce có thể gặp vấn đề về độ trễ nếu dữ liệu quá lớn hoặc không được tổ chức tốt.
  - Hạn chế trong truy vấn phức tạp: Các truy vấn phức tạp có thể khó triển khai hơn so với các hệ thống cơ sở dữ liệu truyền thống.

## 2.11. Column-Based NoSQL Databases

### 2.11.1. Architecture

- **Dữ liệu được lưu trữ theo cột**: Cơ sở dữ liệu dạng cột lưu trữ dữ liệu dựa trên các cột và nhóm các cột, thay vì lưu trữ theo hàng như các cơ sở dữ liệu truyền thống.
- **Families cột**: Dữ liệu trong cơ sở dữ liệu này được tổ chức thành families cột, mỗi family chứa nhiều hàng, và mỗi hàng có một key hoặc định danh riêng. Các cột trong một family có thể được chia sẻ giữa các hàng hoặc không cần phải giống nhau.

Ví dụ:

Hãy tưởng tượng một cơ sở dữ liệu chứa thông tin khách hàng với các family cột như sau:

- Family "Thông tin cá nhân": Gồm các cột như tên, tuổi, địa chỉ.
- Family "Thông tin tài chính": Gồm các cột như số tài khoản ngân hàng, số dư.

Mỗi hàng đại diện cho một khách hàng, và không phải khách hàng nào cũng có đủ thông tin trong tất cả các cột.

### 2.11.2. Benefit

- **Xử lý dữ liệu thưa thớt hiệu quả**: Cơ sở dữ liệu dạng cột đặc biệt hiệu quả khi xử lý lượng dữ liệu lớn nhưng thưa thớt, nơi nhiều cột không có dữ liệu cho tất cả các hàng.
- **Nén và tiết kiệm không gian lưu trữ**: Do dữ liệu được lưu trữ theo cột, việc nén dữ liệu trở nên dễ dàng hơn, tiết kiệm không gian lưu trữ.
- **Khả năng mở rộng ngang**: Cũng giống như các cơ sở dữ liệu NoSQL khác, cơ sở dữ liệu dạng cột có thể được triển khai trên các cụm máy chủ, giúp tăng khả năng mở rộng khi cần thiết.

### 2.11.3. Practical Use Cases

- Ghi nhật ký sự kiện (event logging): Mỗi ứng dụng có thể ghi nhật ký vào một tập hợp các cột riêng, giúp truy xuất dữ liệu dễ dàng theo thời gian và loại ứng dụng.

  - Ví dụ: Một công ty có thể ghi lại nhật ký hoạt động của một ứng dụng với các cột ghi lại loại sự kiện, thời gian xảy ra sự kiện và chi tiết về sự kiện đó.

- Bộ đếm (counters): Một số cơ sở dữ liệu dạng cột như Cassandra có các loại cột đặc biệt cho phép đếm hoặc tăng giảm giá trị dễ dàng. Điều này rất hữu ích cho các ứng dụng cần theo dõi số lượng sự kiện.

  - Ví dụ: Một ứng dụng cần đếm số lần một sản phẩm được xem trên trang web. Bộ đếm có thể tự động tăng mỗi khi sản phẩm đó được xem.

- Thời gian sống (TTL - Time-to-Live): Các cột có thể có tham số thời gian sống, làm cho chúng hữu ích trong việc lưu trữ dữ liệu có hạn sử dụng, chẳng hạn như thời gian dùng thử hoặc thời gian hiển thị quảng cáo.

### 2.11.4. Limitations

- Không hỗ trợ giao dịch ACID: Các giao dịch chỉ mang tính nguyên tử (atomic) ở cấp độ hàng, vì vậy nếu yêu cầu mức độ nhất quán cao và giao dịch liên quan đến nhiều hàng, bạn nên xem xét sử dụng cơ sở dữ liệu quan hệ.

- Thay đổi thiết kế tốn kém: Khi mẫu truy vấn thay đổi trong quá trình phát triển, việc thay đổi thiết kế của cơ sở dữ liệu dạng cột có thể mất nhiều thời gian và chi phí.

### 2.11.5. Application in Data Warehouse

Cơ sở dữ liệu dạng hàng (row-oriented) trong kho dữ liệu lưu trữ dữ liệu của một bản ghi liên tục trong một khối, trong khi cơ sở dữ liệu dạng cột lưu trữ dữ liệu của một bản ghi liên tục theo cột. Điều này giúp tăng tốc truy vấn dữ liệu và cải thiện khả năng báo cáo và trí tuệ doanh nghiệp.

Ví dụ:

Một công ty thương mại điện tử cần truy vấn tổng số tiền của tất cả các đơn hàng cho sản phẩm có mã P101. Với cơ sở dữ liệu dạng cột, chỉ cần đọc dữ liệu từ các cột mã sản phẩm và tổng giá trị, mà không cần đọc toàn bộ bản ghi, giúp tăng tốc quá trình truy vấn.

### 2.11.6. Vendor

Một số cơ sở dữ liệu dạng cột nổi tiếng bao gồm:

- Cassandra
- HBase
- Hypertable
- Accumulo

## 2.12. Graph NoSQL Databases

Cơ sở dữ liệu đồ thị là một dạng biến thể của NoSQL, và có cách thức tổ chức dữ liệu rất khác so với các loại cơ sở dữ liệu NoSQL khác mà chúng ta đã học trước đó, như Key-Value, Document, và Column-based.

### 2.12.1. Architecture

- **Nút (Nodes)**: Đây là các `thực thể` lưu trữ thông tin. Mỗi nút có thể đại diện cho các đối tượng trong thực tế như người dùng, sản phẩm, địa điểm, hoặc bất kỳ đối tượng nào khác mà bạn cần lưu trữ.

- **Cạnh (Edges)**: Các cạnh đại diện cho `mối quan hệ` giữa các nút. Các cạnh này không chỉ nối các nút lại với nhau mà còn chứa thông tin bổ sung về mối quan hệ giữa chúng, như loại quan hệ (bạn bè, đồng nghiệp, kết nối gia đình,...).

Điểm mạnh của cơ sở dữ liệu đồ thị là khả năng `duyệt qua các mối quan hệ` một cách nhanh chóng và hiệu quả. Điều này khác biệt so với các loại cơ sở dữ liệu NoSQL khác, bởi chúng không được tối ưu hóa để xử lý các mối quan hệ phức tạp.

**TÍNH CHẤT ACID VÀ KHẢ NĂNG MỞ RỘNG**

Một trong những khác biệt lớn giữa cơ sở dữ liệu đồ thị và các loại NoSQL khác là chúng tuân thủ `ACID transactions`, điều này đảm bảo tính nhất quán và an toàn cho dữ liệu khi có các giao dịch xảy ra. Tuy nhiên, `nhược điểm lớn` của cơ sở dữ liệu đồ thị là `khả năng mở rộng theo chiều ngang`(horizontal scalability) `không tốt`.

- Sharding (phân mảnh dữ liệu) trong cơ sở dữ liệu đồ thị rất phức tạp và có thể gây giảm hiệu suất, bởi các nút và mối quan hệ của chúng thường phải được lưu trên cùng một máy chủ để đảm bảo tốc độ duyệt quan hệ nhanh.

### 2.12.2. Use Cases

Cơ sở dữ liệu đồ thị phát huy tác dụng tối đa trong những hệ thống mà `dữ liệu có mối liên hệ chặt chẽ` và cần `mô hình hóa các mối quan hệ` phức tạp.

**a. Mạng xã hội (Social Networking Sites)**

  Một ví dụ điển hình là các trang mạng xã hội như `Facebook` hoặc `LinkedIn`. Trong hệ thống này, cơ sở dữ liệu đồ thị giúp lưu trữ thông tin về người dùng (nút) và các mối quan hệ giữa họ (cạnh). Ví dụ, mỗi người dùng là một nút, và mối quan hệ bạn bè là các cạnh nối giữa các nút.

  Các thuật toán gợi ý bạn bè, tìm kiếm bạn chung (friends of friends) đều cần dựa trên việc duyệt các mối quan hệ, điều mà cơ sở dữ liệu đồ thị thực hiện rất nhanh chóng.

**b. Ứng dụng định tuyến, bản đồ (Routing and Spatial Applications)**

  Cơ sở dữ liệu đồ thị cũng được ứng dụng trong các hệ thống như `Google Maps`, nơi mỗi vị trí có thể là một nút và các con đường là cạnh nối giữa các vị trí đó. Điều này giúp dễ dàng `tìm kiếm đường ngắn nhất` giữa hai điểm hoặc tìm các địa điểm gần đó.

**c. Công cụ gợi ý (Recommendation Engines)**

  Các công cụ gợi ý sản phẩm như trên `Amazon` hay `Netflix` sử dụng cơ sở dữ liệu đồ thị để dựa vào các mối quan hệ giữa các sản phẩm và hành vi người dùng. Ví dụ: nếu một khách hàng mua sản phẩm A, hệ thống sẽ gợi ý sản phẩm B dựa trên mối liên hệ giữa các sản phẩm mà những khách hàng khác đã mua trước đó.4

### 2.12.3. Unsuitable Cases

Mặc dù rất mạnh mẽ trong việc xử lý các mối quan hệ phức tạp, nhưng cơ sở dữ liệu đồ thị có một số hạn chế khiến nó không phù hợp trong một số tình huống.

**a. Khả năng mở rộng (Scalability)**

  Nếu hệ thống của bạn cần mở rộng theo chiều ngang để xử lý khối lượng dữ liệu lớn, cơ sở dữ liệu đồ thị sẽ không phải là lựa chọn tối ưu. Việc sharding dữ liệu trong đồ thị rất phức tạp, và nếu các nút và mối quan hệ bị phân tán trên nhiều máy chủ, hiệu suất sẽ bị giảm đáng kể.

**b. Cập nhật hàng loạt (Batch Updates)**

  Việc cập nhật hàng loạt hoặc cập nhật một nhóm các nút trong đồ thị có thể rất khó khăn và phức tạp. Nếu ứng dụng của bạn thường xuyên yêu cầu cập nhật một phần lớn của cơ sở dữ liệu, các loại NoSQL khác như Key-Value hoặc Column-based sẽ phù hợp hơn.

### 2.12.4. Vendor

Dưới đây là một số hệ thống cơ sở dữ liệu đồ thị phổ biến hiện nay:

- **Neo4j**: Một trong những hệ quản trị cơ sở dữ liệu đồ thị nổi tiếng nhất và được sử dụng rộng rãi.
- **OrientDB**: Một hệ cơ sở dữ liệu NoSQL hỗ trợ cả mô hình đồ thị và các mô hình NoSQL khác.
- **ArangoDB**: Hỗ trợ nhiều mô hình dữ liệu, bao gồm đồ thị.
- **Amazon Neptune**: Cơ sở dữ liệu đồ thị do Amazon Web Services cung cấp.
- **JanusGraph**: Một cơ sở dữ liệu đồ thị mã nguồn mở sử dụng để lưu trữ dữ liệu đồ thị với khả năng tích hợp tốt vào các hệ thống phân tán.

# 3. Read more

[NoSQL Database Deployment](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTVNraWxsc05ldHdvcmstQ1MwMTAxRU4tQ291cnNlcmEvbGFicy9EYXRhYmFzZV9EZXBsb3ltZW50X09wdGlvbnMubWQiLCJ0b29sX3R5cGUiOiJpbnN0cnVjdGlvbmFsLWxhYiIsImFkbWluIjpmYWxzZSwiaWF0IjoxNzExNDI0ODMzfQ.Ynng4BKl_2vPOGiCsQmisjupCX2YY-xxB7FKddKE1v4)

[Glossary: Basics of NoSQL](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTVNraWxsc05ldHdvcmstQ1MwMTAxRU4tQ291cnNlcmEvbGFicy9HbG9zc2FyeV8tX0Jhc2ljc19vZl9Ob1NRTC5tZCIsInRvb2xfdHlwZSI6Imluc3RydWN0aW9uYWwtbGFiIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE3MTE0MjQ4Mzh9.k7wLxhGW_lYuMXTA5DuhkQ2MVcW4DKr1vHWINcNIZAg)

# 4. Working with Distributed Data

## 4.1. What is ACID and BASE?

Một trong những sự khác biệt lớn nhất giữa hệ quản trị cơ sở dữ liệu quan hệ (RDBMS) và NoSQL là mô hình tính nhất quán dữ liệu mà chúng sử dụng.

- ACID là mô hình tính nhất quán được sử dụng phổ biến trong cơ sở dữ liệu quan hệ.
- BASE là mô hình thường được sử dụng trong các hệ thống NoSQL.

**ACID - Atomicity, Consistency, Isolation, Durability**

![ACID](acid.png)

Mô hình ACID bao gồm bốn nguyên tắc chính:

1. **Atomicity (Tính nguyên tử)**: Tất cả các thao tác trong một giao dịch hoặc thành công hoàn toàn, hoặc sẽ bị hoàn tác nếu có lỗi. Điều này đảm bảo không có sự thất thoát dữ liệu trung gian.
  - Ví dụ: Trong giao dịch chuyển tiền ngân hàng, nếu tiền đã bị trừ từ tài khoản A nhưng chưa được cộng vào tài khoản B do lỗi, toàn bộ giao dịch sẽ bị hoàn tác để giữ nguyên trạng thái ban đầu.

2. **Consistency (Tính nhất quán)**: Sau khi giao dịch hoàn tất, dữ liệu trong hệ thống luôn duy trì tính toàn vẹn và tuân theo các ràng buộc đã được thiết lập trước đó.
  - Ví dụ: Khi thực hiện giao dịch mua bán, dù có xảy ra lỗi nào trong quá trình, dữ liệu về số lượng hàng tồn kho luôn phải tuân thủ ràng buộc: số hàng không bao giờ được âm.

3. **Isolation (Tính độc lập)**: Các giao dịch đang thực hiện không được làm ảnh hưởng đến nhau. Điều này giúp ngăn chặn việc một giao dịch can thiệp vào quá trình của giao dịch khác.

4. **Durability (Tính bền vững)**: Dữ liệu liên quan đến các giao dịch đã hoàn thành sẽ tồn tại vĩnh viễn, ngay cả khi hệ thống gặp sự cố về mạng hoặc nguồn điện.

**BASE - Basically Available, Soft State, Eventually Consistent**

![BASE](base.png)

Mô hình BASE là lựa chọn thay thế cho ACID trong các hệ thống NoSQL, nhằm phục vụ các hệ thống yêu cầu khả năng mở rộng cao và luôn sẵn sàng (high availability).

1. **Basically Available (Cơ bản khả dụng)**: Dữ liệu luôn khả dụng bằng cách phân tán và sao chép nó trên nhiều máy chủ. Thay vì đảm bảo tính nhất quán ngay lập tức, mô hình BASE ưu tiên tính sẵn sàng của dữ liệu.

2. **Soft State (Trạng thái không cứng nhắc)**: Do không tuân thủ tính nhất quán tức thời, dữ liệu trong mô hình BASE có thể thay đổi theo thời gian. Các bản sao của cùng một dữ liệu không nhất thiết phải luôn đồng nhất tại mọi thời điểm.

3. **Eventually Consistent (Cuối cùng sẽ nhất quán)**: Dữ liệu sẽ cuối cùng trở nên nhất quán sau một khoảng thời gian nhất định, nhưng trong quá trình này, người dùng có thể đọc phải dữ liệu không chính xác tạm thời.

## 4.2. Comparision

**a. ACID:**

  - Ưu điểm:
      - Tính nhất quán cao, đảm bảo dữ liệu luôn chính xác.
      - Phù hợp với các giao dịch tài chính hoặc các hệ thống yêu cầu sự an toàn dữ liệu tuyệt đối.
  - Nhược điểm:
      - Không linh hoạt khi hệ thống cần mở rộng. Đối với các hệ thống lớn, việc duy trì tính nhất quán trên nhiều máy chủ có thể làm giảm hiệu suất.
      - Không đảm bảo tính khả dụng cao khi hệ thống gặp sự cố.

**b. BASE:**

  - Ưu điểm:
      - Tính khả dụng cao, phục vụ tốt các hệ thống yêu cầu mở rộng và truy cập từ nhiều nơi trên thế giới.
      - Dữ liệu có thể được phân tán và sao chép trên nhiều máy chủ, giúp hệ thống có khả năng chịu lỗi cao.

  - Nhược điểm:
      - Không đảm bảo tính nhất quán tức thời, dẫn đến khả năng đọc dữ liệu lỗi tạm thời.
      - Không phù hợp với các hệ thống yêu cầu dữ liệu chính xác tuyệt đối ngay lập tức, như ngân hàng hoặc quản lý tài chính.

## 4.3. Use Cases

**a. ACID trong hệ thống tài chính**

Một ví dụ điển hình về việc sử dụng mô hình ACID là các tổ chức tài chính. Với các giao dịch chuyển tiền, hệ thống không thể cho phép dữ liệu sai lệch, dù là trong chốc lát. Một giao dịch không hoàn tất (ví dụ, tiền đã bị trừ từ tài khoản này nhưng chưa cộng vào tài khoản kia) sẽ dẫn đến các hậu quả nghiêm trọng.

- Ví dụ thực tế: Khi chuyển khoản trong ngân hàng, ACID đảm bảo rằng hoặc cả hai tài khoản đều được cập nhật đúng số dư, hoặc không có gì thay đổi nếu gặp sự cố.

![money transfers](money_transfers.png)

**b. BASE trong hệ thống dịch vụ trực tuyến**

Các hệ thống dịch vụ trực tuyến như Netflix, Spotify, hay Uber thường sử dụng mô hình BASE. Những hệ thống này cần khả dụng 24/7 và phải phục vụ hàng triệu người dùng trên toàn cầu. Tính nhất quán ngay lập tức không phải là ưu tiên hàng đầu, mà thay vào đó là việc đảm bảo hệ thống không bị gián đoạn.

- Ví dụ thực tế: Khi sử dụng Netflix, có thể trong một khoảng thời gian ngắn, danh sách các bộ phim yêu thích của bạn chưa được cập nhật chính xác ngay sau khi bạn thêm một bộ phim mới. Tuy nhiên, hệ thống sẽ cuối cùng đồng bộ và hiển thị dữ liệu đúng sau một thời gian ngắn.

![Worldwide online services](ww_online_services.png)

## 4.4. Summary

- ACID:
    - Atomicity, Consistency, Isolation, Durability.
    - Phù hợp với các hệ thống đòi hỏi tính nhất quán và độ an toàn cao.
    - Thường được sử dụng trong các ứng dụng tài chính và giao dịch.

- BASE:
    - Basically Available, Soft State, Eventually Consistent.
    - Được sử dụng cho các hệ thống yêu cầu tính khả dụng cao và khả năng mở rộng lớn.
    - Phù hợp với các dịch vụ trực tuyến quy mô toàn cầu như Netflix, Spotify, và Uber.

Mỗi mô hình đều có ưu điểm và nhược điểm riêng, và việc lựa chọn giữa chúng phụ thuộc vào yêu cầu cụ thể của ứng dụng và hệ thống bạn đang phát triển.

# 5. Distributed Databases

## 5.1. What is Distributed Database?

Cơ sở dữ liệu phân tán là tập hợp các cơ sở dữ liệu được kết nối với nhau và phân tán trên nhiều địa điểm khác nhau. Các cơ sở dữ liệu này giao tiếp thông qua một `mạng máy tính`. Điều đặc biệt của cơ sở dữ liệu phân tán là dữ liệu được phân phối vật lý bằng cách `phân mảnh` và `sao chép` trên các vị trí dữ liệu khác nhau, giúp mở rộng quy mô hệ thống và tăng cường tính sẵn sàng.

**a. Phân mảnh dữ liệu (Fragmentation/Partitioning/Sharding)**

Để lưu trữ một lượng dữ liệu lớn trên nhiều máy chủ trong một hệ thống phân tán, chúng ta cần phải chia nhỏ dữ liệu thành các phần nhỏ hơn. Quá trình này được gọi là phân mảnh dữ liệu. Một số hệ thống cơ sở dữ liệu NoSQL còn gọi quá trình này là `partitioning` hoặc `sharding`.

![Fragmentation](fracmentation.png)

Ví dụ, khi bạn có một tập dữ liệu lớn như thông tin giao dịch bán hàng, bạn có thể phân chia dữ liệu dựa trên key. Có hai cách phổ biến để phân chia dữ liệu:

![Fragmentation example](fracmentation_example.png)

  - **Phân nhóm theo thứ tự từ khóa (lexical grouping)**: Ví dụ, các khóa bắt đầu bằng chữ cái từ A đến C sẽ được lưu trữ trên một máy chủ cụ thể.
  - **Phân nhóm theo giá trị khóa**: Ví dụ, tất cả các giao dịch từ một cửa hàng có mã cửa hàng giống nhau sẽ được lưu trữ trên một máy chủ. Điều này giúp tối ưu hóa các truy vấn như: "Lấy tất cả giao dịch từ cửa hàng A" mà không cần truy xuất dữ liệu từ nhiều máy chủ.

**b. Sao chép dữ liệu (Replication)**

Sau khi dữ liệu được phân mảnh và phân phối, để đảm bảo tính an toàn, chúng ta cần sao chép dữ liệu. Sao chép đảm bảo rằng mọi phân mảnh của dữ liệu đều được lưu trữ dư thừa ở hai hoặc nhiều địa điểm. Điều này giúp tránh mất dữ liệu nếu một nút (node) trong hệ thống bị lỗi.

- Ví dụ: Nếu một phần dữ liệu của bạn nằm trên máy chủ A, hệ thống sẽ sao chép nó lên máy chủ B. Nếu máy chủ A bị lỗi, bạn vẫn có thể truy xuất dữ liệu từ máy chủ B.

**Nhược điểm của sao chép dữ liệu**: Việc duy trì tính nhất quán giữa các bản sao dữ liệu là một thách thức lớn. Khi một bản sao dữ liệu thay đổi, tất cả các bản sao khác cần được cập nhật theo. Nếu không, hệ thống sẽ gặp tình trạng `không nhất quán`.

## 5.2. Benefit

![distributed_db_benefit](distributed_db_benefit.png)

Cơ sở dữ liệu phân tán mang lại nhiều lợi ích quan trọng cho các hệ thống hiện đại, bao gồm:

**a. Tính khả dụng và độ tin cậy cao**

Vì dữ liệu được sao chép trên nhiều máy chủ, hệ thống có khả năng chịu lỗi tốt. Nếu một máy chủ gặp sự cố, bạn vẫn có thể truy xuất dữ liệu từ các máy chủ khác.

- Ví dụ: Các dịch vụ như `Google Drive` hay `Dropbox` đảm bảo rằng dữ liệu của bạn vẫn an toàn và khả dụng ngay cả khi một máy chủ của họ gặp sự cố.

**b. Hiệu suất cao**

Cơ sở dữ liệu phân tán giúp cải thiện hiệu suất khi xử lý khối lượng dữ liệu lớn. Các truy vấn có thể được xử lý nhanh hơn nhờ việc phân chia dữ liệu và tải công việc lên nhiều máy chủ.

- Ví dụ: Hãy tưởng tượng bạn có một ứng dụng bán hàng toàn cầu, nơi hàng triệu giao dịch được thực hiện mỗi giây. Hệ thống phân tán sẽ giúp xử lý các truy vấn này nhanh chóng bằng cách phân chia và phân phối công việc cho nhiều máy chủ khác nhau.

**c. Khả năng mở rộng**

Khi nhu cầu xử lý dữ liệu tăng cao, bạn có thể dễ dàng mở rộng hệ thống bằng cách thêm máy chủ mới vào cụm máy chủ (cluster). Điều này rất hữu ích cho các ứng dụng phát triển nhanh chóng như `Facebook`, nơi lượng người dùng và dữ liệu tăng trưởng nhanh chóng.

## 5.3. Challenges

Mặc dù cơ sở dữ liệu phân tán mang lại nhiều lợi ích, chúng cũng đi kèm với một số thách thức:

**a. Kiểm soát đồng thời (Concurrency Control)**

Vì dữ liệu được sao chép tại nhiều địa điểm khác nhau, việc cập nhật, xóa, hay sửa đổi dữ liệu có thể dẫn đến các vấn đề đồng bộ hóa. Hệ thống cần một cơ chế để đảm bảo rằng các thay đổi trên một bản sao sẽ được áp dụng trên tất cả các bản sao khác.

- Ví dụ: Khi bạn thực hiện một giao dịch mua bán trên một ứng dụng, hệ thống cần đảm bảo rằng mọi bản sao của dữ liệu liên quan đến giao dịch này đều được cập nhật chính xác trên tất cả các máy chủ.

Để giải quyết vấn đề này, một số hệ thống chỉ cho phép các thao tác trên một phân mảnh dữ liệu diễn ra trên một máy chủ duy nhất, sau đó mới đồng bộ hóa các bản sao khác. Các hệ thống khác cho phép ghi dữ liệu trên tất cả các máy chủ và đọc từ một số máy chủ đủ để đảm bảo tính nhất quán.

**b. Không hỗ trợ giao dịch hoàn chỉnh**

Do các vấn đề về kiểm soát đồng thời và tính nhất quán, các hệ thống cơ sở dữ liệu phân tán thường không hỗ trợ đầy đủ các giao dịch kiểu ACID (atomic, consistent, isolated, durable) mà chỉ cung cấp một phiên bản giới hạn.

**c. Tính nhất quán cuối cùng (Eventual Consistency)**

Các hệ thống cơ sở dữ liệu phân tán thường tuân theo mô hình BASE. Điều này có nghĩa là hệ thống `luôn sẵn sàng` nhưng dữ liệu có thể `không nhất quán ngay lập tức`. Tuy nhiên, qua thời gian, hệ thống sẽ đạt được `tính nhất quán cuối cùng`.

- Ví dụ: Nếu bạn thêm một tệp vào tài khoản Google Drive của mình từ điện thoại, có thể mất vài giây trước khi bạn thấy tệp đó xuất hiện trên máy tính của mình, nhưng cuối cùng nó sẽ xuất hiện.

## 5.4. Summary

- `Cơ sở dữ liệu phân tán` giúp phân phối và sao chép dữ liệu trên nhiều máy chủ, đảm bảo tính sẵn sàng và độ tin cậy cao.
- `Phân mảnh dữ liệu` chia nhỏ dữ liệu để lưu trữ trên nhiều máy chủ, giúp cải thiện hiệu suất truy vấn.
- `Sao chép dữ liệu` đảm bảo an toàn và khả dụng khi một máy chủ gặp sự cố.
- Tuy nhiên, hệ thống phân tán cũng gặp các thách thức về `kiểm soát đồng thời` và `tính nhất quán`. Chúng tuân theo mô hình BASE, trong đó tính nhất quán chỉ đạt được sau một khoảng thời gian.

Cơ sở dữ liệu phân tán là giải pháp lý tưởng cho các dịch vụ yêu cầu mở rộng toàn cầu và tính sẵn sàng cao, như Google, Facebook, hay Amazon, nhưng cũng cần cẩn thận khi thiết kế để giải quyết các thách thức về tính nhất quán và đồng bộ dữ liệu.

# 6. CAP Theorem

## 6.1. History of CAP Theorem

Vào đầu những năm 2000, kiến trúc `Hadoop` dành cho dữ liệu lớn ra đời, đánh dấu một bước đột phá quan trọng trong việc lưu trữ và xử lý khối lượng dữ liệu khổng lồ. Lúc bấy giờ, nhiều dịch vụ bắt đầu yêu cầu các cơ sở dữ liệu cũng phải được phân tán. Các doanh nghiệp không chỉ muốn dịch vụ của họ luôn `khả dụng` trên toàn cầu mà còn yêu cầu hệ thống luôn `hoạt động liên tục`.

Tuy nhiên, các cơ sở dữ liệu quan hệ truyền thống gặp khó khăn khi đối mặt với yêu cầu về tính `sẵn sàng` trong một hệ thống phân tán. Điều này đã được chứng minh qua `Định lý CAP`, còn được gọi là `Định lý Brewer,` lần đầu tiên được giới thiệu bởi Giáo sư Eric A. Brewer trong một bài giảng về tính toán phân tán vào năm 2000. Sau đó, định lý này được các giáo sư của MIT, Seth Gilbert và Nancy Lynch, xem xét và hoàn thiện.

## 6.2. What is CAP Theorem?

Định lý CAP nêu rõ rằng trong một hệ thống phân tán, có ba đặc tính cần thiết để thiết kế và triển khai thành công các ứng dụng, bao gồm:

- C: Tính nhất quán (Consistency)
- A: Tính sẵn sàng (Availability)
- P: Khả năng chịu lỗi phân vùng (Partition Tolerance)

Tuy nhiên, một hệ thống phân tán chỉ có thể đảm bảo `2 trong 3 đặc tính` này. Điều này có nghĩa là `không có hệ thống phân tán nào` có thể đạt được `cả 3` đặc tính đồng thời.

## 6.3. Meaning of properties in CAP Theorem

**a. Tính nhất quán (Consistency)**

Tính nhất quán trong hệ thống phân tán đề cập đến việc tất cả các nút trong hệ thống có thể truy xuất cùng một dữ liệu tại mọi thời điểm. Nói cách khác, nếu bạn cập nhật một giá trị tại một nút, tất cả các nút khác phải nhìn thấy giá trị đó ngay lập tức.

- Ví dụ: Trong một hệ thống ngân hàng, nếu bạn thực hiện chuyển tiền từ tài khoản của mình, mọi bản sao của dữ liệu tài khoản đó trên tất cả các máy chủ phải được cập nhật ngay lập tức để tránh tình trạng sai lệch thông tin.

**b. Tính sẵn sàng (Availability)**

Tính sẵn sàng đảm bảo rằng mọi yêu cầu gửi đến hệ thống đều nhận được phản hồi, bất kể thành công hay thất bại. Điều này có nghĩa là hệ thống luôn phải sẵn sàng phục vụ yêu cầu của người dùng, ngay cả khi có sự cố xảy ra.

- Ví dụ: Một ứng dụng mạng xã hội như Facebook luôn cần đảm bảo rằng khi bạn đăng tải một trạng thái, hệ thống sẽ phản hồi rằng thao tác của bạn đã được ghi nhận.

**c. Khả năng chịu lỗi phân vùng (Partition Tolerance)**

Khả năng chịu lỗi phân vùng đề cập đến việc hệ thống vẫn tiếp tục hoạt động bình thường ngay cả khi có sự cố về kết nối hoặc mất dữ liệu giữa các nút trong hệ thống. Điều này đặc biệt quan trọng trong hệ thống phân tán, nơi các kết nối giữa các nút có thể bị gián đoạn tạm thời.

- Ví dụ: Trong một hệ thống với 8 nút (node), nếu mạng bị phân vùng và kết nối giữa các nút bị mất, thay vì toàn bộ hệ thống bị sập, các cụm nhỏ hơn vẫn có thể tiếp tục hoạt động và dữ liệu sẽ được đồng bộ khi kết nối được khôi phục.

## 6.3. The Importance of Partition Tolerance

Trong các hệ thống phân tán, việc `phân vùng` (partition) là không thể tránh khỏi. Khi một phân vùng xảy ra, hệ thống phải có khả năng duy trì hoạt động mà không bị gián đoạn. Đây là lý do tại sao khả năng chịu lỗi phân vùng trở thành một tính năng `bắt buộc` của các hệ thống phân tán hiện đại, đặc biệt là trong các cơ sở dữ liệu NoSQL.

**Ví dụ về phân vùng:**

Giả sử bạn có một hệ thống với 8 nút phân tán trên toàn cầu. Khi có sự cố về kết nối, hệ thống có thể tạm thời phân chia thành hai cụm 4 nút. Khi kết nối được khôi phục, tính nhất quán giữa các nút sẽ được đảm bảo bằng cách đồng bộ hóa dữ liệu.

## 6.4. Classification of NoSQL systems according to the CAP Theorem

Dựa trên Định lý CAP, ta có thể phân loại các hệ thống cơ sở dữ liệu NoSQL thành hai nhóm chính:

- **CP (Consistent and Partition Tolerant)**: Hệ thống ưu tiên tính nhất quán và khả năng chịu lỗi phân vùng. Tuy nhiên, điều này có thể làm giảm tính sẵn sàng.
  - Ví dụ: MongoDB là một ví dụ điển hình. MongoDB ưu tiên tính nhất quán, đảm bảo rằng dữ liệu luôn đồng bộ giữa các nút, ngay cả khi điều này khiến một số yêu cầu tạm thời không thể đáp ứng được.
- **AP (Available and Partition Tolerant)**: Hệ thống ưu tiên tính sẵn sàng và khả năng chịu lỗi phân vùng, nhưng có thể chấp nhận sự không nhất quán tạm thời của dữ liệu.
  - Ví dụ: Apache Cassandra chọn ưu tiên tính sẵn sàng. Cassandra đảm bảo rằng ngay cả khi có sự cố phân vùng, hệ thống vẫn có thể xử lý và phản hồi yêu cầu của người dùng.

Điều này `không có nghĩa là MongoDB không thể có tính sẵn sàng` hoặc `Cassandra không thể nhất quán`. Cả hai hệ thống đều `có thể điều chỉnh để đạt được đặc tính còn lại`, nhưng chúng ưu tiên một trong hai yếu tố (nhất quán hoặc sẵn sàng) làm trọng tâm.

## 6.5. Summary

- `Định lý CAP` cho biết rằng trong một hệ thống phân tán, bạn chỉ có thể chọn 2 trong 3 đặc tính: `tính nhất quán`, `tính sẵn sàng`, và `khả năng chịu lỗi phân vùng`.
- `Khả năng chịu lỗi phân vùng` là một yếu tố bắt buộc trong các hệ thống phân tán như NoSQL, nơi phân vùng là điều không thể tránh khỏi.
- Các hệ thống NoSQL thường phải lựa chọn giữa `tính nhất quán` và `tính sẵn sàng`, tùy thuộc vào nhu cầu của hệ thống và ưu tiên thiết kế.

Các hệ thống hiện đại như MongoDB và Apache Cassandra là những ví dụ tiêu biểu cho việc áp dụng Định lý CAP vào thực tế. MongoDB chọn ưu tiên tính nhất quán, trong khi Cassandra ưu tiên tính sẵn sàng, tùy thuộc vào từng trường hợp sử dụng và yêu cầu của người dùng.

# 7. Challenges in Migrating from RDBMS to NoSQL Databases

## 7.1. Common Misunderstanding: Is NoSQL a Replacement for RDBMS?

Một số người nghĩ rằng NoSQL là sự thay thế cho RDBMS hoặc rằng ta phải lựa chọn giữa hai hệ thống này. Tuy nhiên, thực tế là `RDBMS và NoSQL không cạnh tranh trực tiếp với nhau`, vì chúng phục vụ cho những yêu cầu và trường hợp sử dụng khác nhau. Điều quan trọng là bạn cần xem xét đặc điểm của hệ thống mà bạn đang xây dựng để quyết định việc sử dụng RDBMS hay NoSQL.

- Ví dụ: Một hệ thống bán lẻ lớn có thể cần tính nhất quán và giao dịch phức tạp để xử lý các đơn đặt hàng, nhưng cũng cần một hệ thống NoSQL để xử lý khối lượng lớn dữ liệu không có cấu trúc như phản hồi khách hàng hoặc phân tích dữ liệu người dùng.

## 7.2. When to choose RDBMS and when to choose NoSQL?

**a. RDBMS:**

- Nếu bạn cần đảm bảo tính nhất quán cao cho dữ liệu của mình.
- Khi dữ liệu của bạn có cấu trúc rõ ràng.
- Nếu bạn cần thực hiện giao dịch nhiều tài liệu hoặc các phép JOIN phức tạp giữa các bảng.

Trong những trường hợp này, cơ sở dữ liệu quan hệ sẽ là lựa chọn phù hợp hơn.

- Ví dụ: Trong một hệ thống ngân hàng, các giao dịch tài chính cần sự chính xác tuyệt đối và có thể yêu cầu nhiều bảng dữ liệu liên kết với nhau để xác nhận số dư tài khoản, lịch sử giao dịch,...

**b. NoSQL:**

- Khi bạn có khối lượng lớn dữ liệu cần hệ thống hiệu năng cao.
- Nếu dữ liệu của bạn không có cấu trúc và có thể hưởng lợi từ một lược đồ linh hoạt.
- Khi hệ thống của bạn cần phải khả dụng cao và có thể mở rộng nhanh chóng.

Trong những trường hợp này, NoSQL sẽ mang lại nhiều lợi thế hơn.

- Ví dụ: Một hệ thống mạng xã hội lớn như Facebook phải xử lý lượng dữ liệu không có cấu trúc từ người dùng (bài đăng, bình luận, hình ảnh), do đó cần sử dụng NoSQL để tăng khả năng mở rộng và đáp ứng nhanh.

## 7.3. Combines both RDBMS and NoSQL

Có những trường hợp mà cả `RDBMS và NoSQL` đều cần thiết. Nếu hệ thống của bạn cần xử lý một khối lượng dữ liệu lớn, yêu cầu tính `hiệu năng và mở rộng nhanh`, nhưng đồng thời cũng cần hỗ trợ `giao dịch` và các phép `JOIN` phức tạp, thì giải pháp kết hợp có thể là lựa chọn tốt nhất.

- Ví dụ: Một công ty thương mại điện tử có thể sử dụng RDBMS cho việc quản lý đơn hàng, nhưng sử dụng NoSQL để xử lý phân tích hành vi người dùng, vì cần sự linh hoạt trong việc lưu trữ dữ liệu không cấu trúc và khả năng mở rộng.

## 7.4. Design differences between RDBMS and NoSQL

**a. Dữ liệu được điều khiển bởi truy vấn trong NoSQL**

Trong RDBMS, quá trình thiết kế bắt đầu từ dữ liệu: ta xác định các thực thể và mối quan hệ của chúng. Nhưng trong NoSQL, quá trình thiết kế không dựa trên cấu trúc dữ liệu mà dựa vào truy vấn của ứng dụng.

- Ví dụ: Trong NoSQL, bạn không cần lo lắng về việc làm thế nào để lưu trữ dữ liệu thành các hàng và bảng, mà thay vào đó bạn phải cân nhắc về cách ứng dụng của bạn sẽ truy cập dữ liệu như thế nào, từ đó tối ưu hóa cấu trúc lưu trữ.

**b. Dữ liệu được chuẩn hóa trong RDBMS, nhưng phi chuẩn hóa trong NoSQL**

Trong RDBMS, dữ liệu được chuẩn hóa nhằm giảm thiểu sự trùng lặp và đảm bảo tính toàn vẹn. Ngược lại, trong NoSQL, dữ liệu thường phi chuẩn hóa, nghĩa là có thể lưu trữ các bản sao của dữ liệu trong nhiều nơi khác nhau chỉ để tối ưu hóa việc truy vấn.

- Ví dụ: Trong NoSQL, bạn có thể lưu trữ thông tin về cùng một khách hàng trong nhiều bảng khác nhau để tránh phải thực hiện JOIN phức tạp khi truy vấn.

## 7.5. Considerable Problems

**a. Tính nhất quán và khả dụng trong hệ thống phân tán**

Khi bạn di chuyển từ RDBMS sang NoSQL, bạn cần phải hiểu rằng `nhiều dịch vụ ngày nay đánh giá cao tính khả dụng hơn tính nhất quán`, đặc biệt khi nói đến hệ thống phân tán. Định lý CAP đã chỉ ra rằng trong một hệ thống phân tán, không thể đảm bảo cả tính nhất quán và tính khả dụng cùng lúc.

- Ví dụ: Các dịch vụ trực tuyến hiện đại như Amazon hoặc Netflix thường ưu tiên tính khả dụng để đảm bảo người dùng không gặp phải tình trạng hệ thống bị sập, ngay cả khi phải đánh đổi một chút về tính nhất quán của dữ liệu trong thời gian ngắn.

**b. Những hạn chế của NoSQL**

NoSQL không được thiết kế để hỗ trợ `giao dịch`, `JOIN`, hoặc xử lý dữ liệu phức tạp ngoại trừ trong một số trường hợp hạn chế. Khi di chuyển từ RDBMS sang NoSQL, bạn cần phải xem xét điều này, vì nó có thể ảnh hưởng đến khả năng triển khai của bạn nếu bạn phụ thuộc nhiều vào những tính năng này.

- Ví dụ: Nếu hệ thống của bạn cần thực hiện các giao dịch tài chính hoặc các phép toán phức tạp, việc chỉ sử dụng NoSQL có thể không phải là giải pháp tốt.

## 7.6. Summary

- NoSQL ``không phải là sự thay thế hoàn toàn` cho RDBMS. Hai hệ thống này phục vụ các `trường hợp sử dụng khác nhau`.
- Bạn có thể sử dụng `cả RDBMS và NoSQL` trong một hệ thống để đáp ứng các yêu cầu khác nhau.
- Việc di chuyển từ RDBMS sang NoSQL có thể xuất phát từ nhu cầu về `hiệu năng`, `khả năng mở rộng`, hoặc `lược đồ linh hoạt`.
- `NoSQL` yêu cầu bạn phải `thay đổi cách suy nghĩ` từ một mô hình dữ liệu dựa trên quan hệ sang một mô hình dựa trên `truy vấn` và tương tác với dữ liệu.
- Khi sử dụng NoSQL, bạn phải chấp nhận rằng hệ thống của bạn có thể `không hỗ trợ giao dịch` hoặc phép `JOIN` phức tạp.

NoSQL và RDBMS đều có vị trí của mình trong kiến trúc hệ thống hiện đại. Điều quan trọng là phải hiểu được đặc điểm và yêu cầu của hệ thống của bạn để chọn lựa giải pháp phù hợp nhất.

# 8. Data Model Example in Relational vs Document

## 8.1. Introduction

Đầu tiên, so sánh tổ chức thông tin trong cơ sở dữ liệu quan hệ với cơ sở dữ liệu tài liệu NoSQL.

Cơ sở dữ liệu quan hệ tổ chức dữ liệu thành các bảng với các lược đồ và mối quan hệ được xác định trước giữa các bảng. Trong mô hình quan hệ, bạn tránh sao chép bất kỳ dữ liệu nào để dữ liệu được lưu trữ một lần và cập nhật ở một vị trí. Bất cứ nơi nào và bất cứ khi nào cần dữ liệu, dữ liệu sẽ được tham chiếu. Đó là khía cạnh quan hệ của dữ liệu.

Mặt khác, một thiết kế dựa trên tài liệu xuất sắc bắt đầu bằng việc sử dụng dữ liệu đó.

Hãy sử dụng ví dụ về sách thư viện và tổ chức dữ liệu.

**LÀM VIỆC VỚI MỘT THƯ VIỆN**

Danh mục sách của thư viện lưu trữ thông tin về sách và tác giả của chúng.

### 8.1.1. Using a relational database for a library books catalog

Nếu bạn làm việc với dữ liệu sách thư viện bằng cơ sở dữ liệu quan hệ, bạn sẽ tạo các bảng Sách, Tác giả, Thể loại và BookGenres:

**Books**

| BookID | Title                 | AuthorID | ISBN            | Published Year |
|--------|-----------------------|----------|-----------------|----------------|
| 1      | The Great Gatsby       | 1        | 978-0743273565  | 1925           |
| 2      | To Kill a Mockingbird  | 2        | 978-0061120084  | 1960           |
| 3      | 1984                   | 3        | 978-0451524935  | 1949           |
| 4      | Pride and Prejudice    | 4        | 978-0141439518  | 1813           |
| 5      | The Hobbit             | 5        | 978-0618260300  | 1937           |

**Authors**

| AuthorID | Name                 |
|----------|----------------------|
| 1        | F. Scott Fitzgerald   |
| 2        | Harper Lee            |
| 3        | George Orwell         |
| 4        | Jane Austen           |
| 5        | J.R.R. Tolkien        |

**Genres**

| GenreID | Genre Name |
|---------|------------|
| 1       | Fiction    |
| 2       | Classic    |
| 3       | Dystopian  |
| 4       | Romance    |
| 5       | Fantasy    |

**BookGenres**

| BookID | GenreID |
|--------|---------|
| 1      | 1       |
| 1      | 2       |
| 2      | 1       |
| 3      | 1       |
| 3      | 3       |
| 4      | 1       |
| 4      | 4       |
| 5      | 1       |
| 5      | 5       |

## 8.1.2. Using a cocument database for a library books catalog

Ngược lại, cơ sở dữ liệu tài liệu được đơn giản hóa và hiển thị dưới dạng một tài liệu duy nhất với tất cả thông tin cần thiết.

```json
{
  “_id”: 1,
  ”title”: “The Great Gatsby”,
  ”author”: “F. Scott Fitzgerald”,
  ”isbn”: “978-0743273565”,
  ”published_year”: 1925,
  ”genres”: [“Fiction”, “Classic”]
  }
```

Tiếp theo, so sánh mức độ phức tạp của việc truy vấn dữ liệu trong cơ sở dữ liệu quan hệ và tài liệu.

## 8.2. Complexities of querying data

Hãy xem xét mức độ phức tạp của việc truy vấn cùng một dữ liệu sách bằng cơ sở dữ liệu quan hệ so với cơ sở dữ liệu NoSQL.

### 8.2.1. Querying book data using a relational database

Bây giờ, hãy truy vấn dữ liệu. Bạn sẽ cần tất cả các chi tiết cuốn sách cùng một lúc. Bạn sẽ cấu trúc truy vấn SQL của mình bằng cách thực hiện JOIN giữa các bảng đó. Đây là ví dụ về truy vấn SQL của bạn:

```SQL
SELECT
  Books.Title AS BookTitle,
  Authors.AuthorName AS Author,
  GROUP_CONCAT(Genres.GenreName) AS GenresFROMBooks
JOIN
  Authors ON Books.AuthorID = Authors.AuthorID
JOIN
  BookGenres ON Books.BookID = BookGenres.BookID
JOIN 
  Genres ON BookGenres.GenreID = Genres.GenreID
GROUP BY
  Books.Title, Authors.AuthorName;
```

Số lượng JOIN, việc sử dụng hàm GROUP_CONCAT và hàm GROUP BY khiến truy vấn này trở nên phức tạp.

- Lệnh SELECT lấy tên sách, tên tác giả và danh sách thể loại được ghép nối cho mỗi cuốn sách.
- Lệnh JOIN nối bảng Books với bảng Authors trên trường AuthorID để lấy tên tác giả.
- Lệnh JOIN nối bảng Books với bảng BookGenres trên trường BookID để liên kết sách với thể loại.
- Lệnh JOIN nối bảng BookGenres với bảng Genres trên trường GenreID để lấy tên thể loại.
- Truy vấn sử dụng hàm GROUP_CONCAT (chức năng chính xác có thể khác nhau tùy thuộc vào hệ thống cơ sở dữ liệu SQL của bạn; GROUP_CONCAT được sử dụng trong MySQL và STRING_AGG trong PostgreSQL) để ghép nhiều tên thể loại thành một chuỗi duy nhất.
- Truy vấn sử dụng GROUP BY để hiển thị kết quả theo tên sách và tên tác giả.

Đây là một ví dụ đầu ra:

| BookTitle                | Author                | Genres                  |
|--------------------------|-----------------------|-------------------------|
| 1984                     | George Orwell         | Fiction, Dystopian      |
| Pride and Prejudice      | Jane Austen           | Fiction, Romance        |
| The Great Gatsby         | F. Scott Fitzgerald    | Fiction, Classic        |
| The Hobbit               | J.R.R. Tolkien        | Fiction, Fantasy        |
| To Kill a Mockingbird    | Harper Lee            | Fiction                 |

### 8.2.2. Querying book data using a NoSQL document database

Bạn đã biết đầu ra mình cần và đầu ra đó là tiêu chí hàng đầu trong cơ sở dữ liệu tài liệu. Hãy nhớ rằng tài liệu sách của bạn trông như thế này:

```json
{
  “_id”: 1,
  ”title”: “The Great Gatsby”,
  ”author”: “F. Scott Fitzgerald”,
  ”isbn”: “978-0743273565”,
  ”published_year”: 1925,
  ”genres”: [“Fiction”, “Classic”]
  }
```

Ví dụ: khi tạo truy vấn cơ sở dữ liệu tài liệu, sử dụng MongoDB, bạn chỉ định dấu ngoặc trống làm đối số đầu tiên biểu thị bạn muốn xem tất cả tài liệu. Đối số thứ hai, được gọi là phép chiếu, cho phép bạn chọn trường nào sẽ hiển thị thông tin khách hàng. Không phải lúc nào bạn cũng cần hiển thị tất cả các trường. Và bạn sẽ nhận thấy sự đơn giản của truy vấn này vì nó không cần bất kỳ sự kết hợp nào với các bộ sưu tập khác.

Đây là truy vấn của bạn:

```noSQL
Db.books.find({}, { title:1, author: 1, genres: 1 })
```

Dữ liệu bạn cần để thực hiện yêu cầu đã có sẵn trong tài liệu và không yêu cầu bất kỳ sự kết hợp nào với các bộ sưu tập khác.

### 8.2.3 Important! What about data duplication?

Sao chép dữ liệu là một thực tế phổ biến và được gọi là "không chuẩn hóa". Sao chép dữ liệu có thể cải thiện hiệu suất đọc bằng cách tránh các phép nối và truy vấn phức tạp. Tuy nhiên, bạn sẽ phải đối mặt với những thách thức về tính nhất quán của dữ liệu và yêu cầu lưu trữ ngày càng tăng.
Ví dụ: hãy tưởng tượng rằng tác giả, J.R.R. Tolkien, muốn được biết đến với tên đầy đủ của mình, John Ronald Reuel Tolkien, và bạn cần thực hiện thay đổi này trong cơ sở dữ liệu quan hệ và cơ sở dữ liệu tài liệu. Bạn sẽ triển khai thay đổi này như thế nào trong hai loại cơ sở dữ liệu khác nhau này?

| Relational database                | Document database                |
|--------------------------|-----------------------|
| Yêu cầu này chỉ yêu cầu một thay đổi trong bảng Tác giả trong cơ sở dữ liệu quan hệ.                     | Vì tác giả đã viết 12 cuốn sách trong cơ sở dữ liệu tài liệu nên bạn phải cập nhật thông tin này trong 12 tài liệu, đây là một cái giá nhỏ phải trả vì đây là một sự kiện hiếm gặp.         |

Tiếp theo, hãy khám phá những cân nhắc liên quan đến việc phát triển một lược đồ.

## 8.3. Schema Evolution Considerations

Việc thay đổi lược đồ trong cơ sở dữ liệu có thể cần thiết để đáp ứng các yêu cầu ứng dụng đang phát triển. Tuy nhiên, có sự khác biệt đáng kể về cách cơ sở dữ liệu tài liệu và quan hệ cho phép thay đổi lược đồ.

Trong cơ sở dữ liệu quan hệ, việc thay đổi lược đồ thường liên quan đến việc sửa đổi các bảng hiện có, thêm bảng mới hoặc thay đổi mối quan hệ giữa các bảng. Đây là một ví dụ:

```SQL
ALTER TABLE table_nameADD column_name data_type;
```

Sau khi thực hiện thay đổi lược đồ, bạn có thể cần phải di chuyển dữ liệu hiện có để khớp với lược đồ mới, điều này có thể liên quan đến các tập lệnh di chuyển và chuyển đổi dữ liệu.

Trong cơ sở dữ liệu tài liệu như MongoDB, lược đồ thường linh hoạt hơn và bạn thường có thể thêm hoặc xóa các trường khỏi tài liệu (tài liệu riêng lẻ, vì thường không có lược đồ được thực thi trên toàn bộ sưu tập) mà không cần cấu trúc được xác định trước. Đây là một ví dụ:

```noSQL
Db.books.update ({ _id: 1 },{$set: {Newfield: “Some value”}});
```

