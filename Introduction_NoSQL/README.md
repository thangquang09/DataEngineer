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

