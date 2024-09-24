- [1. Overview of MongoDB](#1-overview-of-mongodb)
  - [1.1. What is MongoDB?](#11-what-is-mongodb)
- [1.2. Architecture of Document in MongoDB](#12-architecture-of-document-in-mongodb)
  - [1.3. Features](#13-features)
  - [1.4. Summary](#14-summary)
- [2. Benefit of MongoDB](#2-benefit-of-mongodb)
- [3. MongoDB Use Cases](#3-mongodb-use-cases)
- [4. Hands-on: Getting Started with MongoDB](#4-hands-on-getting-started-with-mongodb)
- [4. CRUD Operations](#4-crud-operations)
  - [4.1. Connect to MongoDB](#41-connect-to-mongodb)
  - [4.2. CRUD Operations](#42-crud-operations)
    - [4.2.1. CREATE](#421-create)
    - [4.2.2. READ](#422-read)
    - [4.2.3. UPDATE](#423-update)
    - [4.2.4. DELETE](#424-delete)
  - [4.3. Hands-on](#43-hands-on)
- [5. Indexes](#5-indexes)
  - [5.1. Why we need Indexes?](#51-why-we-need-indexes)
  - [5.2. Indexes in MongoDb](#52-indexes-in-mongodb)
  - [5.3. Compound Index](#53-compound-index)
  - [5.4. How MongoDB store indexes?](#54-how-mongodb-store-indexes)
  - [5.5. Hands-on lab](#55-hands-on-lab)
- [6. Aggregation Framework](#6-aggregation-framework)
  - [6.1. What is Aggregation Framework?](#61-what-is-aggregation-framework)
  - [6.2. Stages in Aggregation Framework](#62-stages-in-aggregation-framework)
  - [6.3. Other common stages in Aggregation Pipeline](#63-other-common-stages-in-aggregation-pipeline)
  - [6.4. When we use Aggregation Framework?](#64-when-we-use-aggregation-framework)
  - [6.5. Summary](#65-summary)
  - [6.6. Hands-on Lab](#66-hands-on-lab)
- [7. Replication and Sharding in MongoDB](#7-replication-and-sharding-in-mongodb)
  - [7.1. What is Replication?](#71-what-is-replication)
  - [7.2. Benefit of Replication](#72-benefit-of-replication)
  - [7.3. Relication Process in MongoDB](#73-relication-process-in-mongodb)
  - [7.4. What is Sharding?](#74-what-is-sharding)
  - [7.5. How Replication and Sharding work?](#75-how-replication-and-sharding-work)
  - [7.6. Summary](#76-summary)
- [8. Access MongoDB with Python](#8-access-mongodb-with-python)


# 1. Overview of MongoDB

## 1.1. What is MongoDB?

MongoDB là một cơ sở dữ liệu `document` và thuộc loại `NoSQL`. Thay vì lưu trữ dữ liệu trong các bảng theo hàng và cột như các cơ sở dữ liệu SQL, mỗi bản ghi trong MongoDB là một document, và dữ liệu được lưu trữ theo cách `phi quan hệ`.

**Document trong MongoDB**

Document trong MongoDB là các mảng kết hợp (associative arrays), giống như các đối tượng `JSON` hoặc `Python dictionary`.

- Ví dụ: Một document đại diện cho sinh viên có thể bao gồm thông tin như `họ tên`, `địa chỉ email`, và `ID sinh viên`. Các trường (fields) này có thể có dạng:

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "johndoe@example.com",
  "student_id": 12345
}
```

MongoDB cho phép nhóm các document cùng loại vào một `collection`. Ví dụ, tất cả các bản ghi sinh viên trong hệ thống quản lý trường học có thể được lưu trữ trong `student collection`, và tất cả các bản ghi nhân viên có thể được lưu trong `employee collection`.

- Ví dụ thực tế: Trong hệ thống quản lý trường học, ta có một `CampusManagementDB` chứa tất cả các loại dữ liệu như sinh viên, giáo viên, nhân viên, mỗi loại dữ liệu sẽ được lưu trữ trong một collection riêng biệt. Ví dụ, `collection` students sẽ chứa toàn bộ thông tin về sinh viên.

# 1.2. Architecture of Document in MongoDB

**Các trường dữ liệu và loại dữ liệu trong MongoDB**

Trong một document MongoDB, các trường như `first_name`, `last_name`, `email`, và `student_id` là các `fields` hoặc thuộc tính, với mỗi trường có giá trị tương ứng. Một điểm cần lưu ý là mỗi tên trường phải là `duy nhất` trong một document.

MongoDB hỗ trợ rất nhiều loại dữ liệu khác nhau, giúp chúng ta dễ dàng lưu trữ thông tin với định dạng chính xác.

```json
{
  "name": "John",
  "dateOfBirth": ISODate("2000-01-01T14:45:00.000Z"),
  "studentId": 20217484,
  "enrolled": true,
  "balance": 20.01,
  "address": {
    "city": "Stonefield",
    "country": "UK"
  },
  "interests": [
    "football",
    "skiing",
    "travelling"
  ]
}
```

- Ví dụ:
    - `Ngày tháng` có thể được lưu dưới dạng `ISODate` hoặc ngày kiểu Unix (Unix-style epoch dates), điều này giúp bạn dễ dàng truy vấn dữ liệu. Ví dụ: “Hãy lấy tất cả các sinh viên sinh từ ngày 15/01 đến 15/02”.
    - `Số liệu` có thể được lưu dưới dạng số nguyên (whole numbers) hoặc số thập phân (decimals).

MongoDB còn cho phép bạn lưu trữ subdocuments để nhóm các thông tin phụ cùng nhau.

- Ví dụ: Một document sinh viên không chỉ chứa thông tin cá nhân của sinh viên mà còn có thể chứa một subdocument về địa chỉ của sinh viên:

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "address": {
    "street": "123 Main St",
    "city": "New York",
    "zip_code": "10001"
  }
}
```

MongoDB cũng hỗ trợ lưu trữ danh sách các giá trị, và danh sách này không chỉ bao gồm văn bản mà còn có thể chứa nhiều loại dữ liệu khác nhau. (Ví dụ như key "interests" ở ví dụ trên)

## 1.3. Features

**a. Sự linh hoạt của MongoDB**

Khi làm việc với MongoDB, bạn có thể `tập trung vào dữ liệu` mà bạn đang viết và cách bạn sẽ đọc nó, thay vì lo lắng về việc tạo bảng hay cấu trúc trước như trong các cơ sở dữ liệu quan hệ.

- Ví dụ: Trong cơ sở dữ liệu SQL, trước khi lưu trữ thêm một trường dữ liệu mới, bạn cần phải thay đổi cấu trúc bảng bằng cách thêm cột. Trong MongoDB, bạn có thể thêm trường mới vào document mà không cần thay đổi cấu trúc của các document khác. Điều này tạo ra sự linh hoạt tuyệt vời khi yêu cầu thay đổi nhanh chóng.

MongoDB còn cho phép bạn tích hợp cả `dữ liệu có cấu trúc` và `dữ liệu không có cấu trúc`. Điều này có nghĩa là bạn có thể dễ dàng thêm dữ liệu mới mà không phải thay đổi toàn bộ cơ sở dữ liệu của mình.

**b. Tính khả dụng cao và khả năng mở rộng của MongoDB** 

MongoDB cung cấp tính `khả dụng cao` bằng cách lưu trữ `nhiều bản sao` của dữ liệu. Điều này đảm bảo rằng nếu một bản sao bị hỏng, các bản sao khác vẫn có thể tiếp tục phục vụ yêu cầu truy cập.

- Ví dụ: Trong một hệ thống quản lý trường học với nhiều người dùng, tính khả dụng của dữ liệu rất quan trọng để đảm bảo hệ thống hoạt động liên tục ngay cả khi một máy chủ bị sự cố.

MongoDB cũng hỗ trợ khả năng mở rộng linh hoạt, cho phép bạn `mở rộng theo chiều dọc` (vertical scaling) bằng cách sử dụng phần cứng mạnh hơn, hoặc `mở rộng theo chiều ngang` (horizontal scaling) bằng cách phân vùng dữ liệu.

- Ví dụ thực tế: Khi hệ thống quản lý trường học mở rộng sang các khu vực khác, như Mỹ, nơi sử dụng `zip code` thay vì `postcode`, MongoDB vẫn có thể dễ dàng mở rộng và điều chỉnh để lưu trữ thông tin phù hợp với từng quốc gia.

**c. Triển khai MongoDB trên các nền tảng khác nhau**

MongoDB có thể được triển khai theo nhiều cách khác nhau, từ việc tự quản lý trên hệ thống tại chỗ, đến các dịch vụ `đám mây` như `MongoDB Atlas` trên AWS, Azure, hoặc Google Cloud. Điều này mang đến sự linh hoạt và dễ dàng khi cần mở rộng hệ thống.

- Ví dụ: Một doanh nghiệp có thể lựa chọn triển khai MongoDB trên `IBM Cloud Databases` cho MongoDB để tận dụng sức mạnh của đám mây trong việc mở rộng và quản lý dữ liệu mà không cần phải lo lắng về hạ tầng phần cứng.

## 1.4. Summary

- MongoDB là một cơ sở dữ liệu document và NoSQL.
- MongoDB hỗ trợ nhiều loại dữ liệu khác nhau, giúp lưu trữ thông tin theo đúng định dạng.
- Các document trong MongoDB cung cấp một cách lưu trữ dữ liệu linh hoạt, với khả năng lưu trữ cả dữ liệu có cấu trúc và không có cấu trúc.
- MongoDB giúp quản lý dữ liệu dễ dàng theo cách bạn đọc và ghi, không yêu cầu phải thiết kế trước một schema cố định.
- Với khả năng khả dụng cao và mở rộng, MongoDB là một giải pháp lý tưởng cho các hệ thống yêu cầu dữ liệu lớn và mở rộng nhanh chóng.

MongoDB có thể được sử dụng cho nhiều mục đích khác nhau nhờ tính linh hoạt trong việc lưu trữ dữ liệu, từ các ứng dụng nhỏ đến những hệ thống lớn với yêu cầu về tính sẵn sàng và khả năng mở rộng.

# 2. Benefit of MongoDB

1. **Tính linh hoạt của schema**

Lợi ích đầu tiên của MongoDB là tính linh hoạt của `schema`. Hãy so sánh hai địa chỉ dưới đây:

- Địa chỉ ở Vương quốc Anh không có zip code nhưng có postcode.
- Địa chỉ ở Mỹ không có postcode nhưng có zip code.

![Lược đồ linh hoạt](flex_schema.png)

Trong hệ thống cơ sở dữ liệu quan hệ (relational database), nơi mà mỗi tên trường (field name) phải xuất hiện trong mỗi hàng, điều này có thể gây khó khăn. Bạn sẽ phải thêm các trường không có giá trị hoặc tạo ra quá nhiều trường để phục vụ cho từng trường hợp riêng biệt.

Tuy nhiên, trong MongoDB, việc lưu trữ thông tin theo định dạng linh hoạt này không phải là vấn đề vì MongoDB cho phép sử dụng `schema động`. Điều này đồng nghĩa với việc bạn có thể lưu trữ các loại dữ liệu `không có cấu trúc` một cách dễ dàng.

- Ví dụ: Bạn có thể kết hợp dữ liệu từ các nguồn khác nhau, với cấu trúc không đồng nhất, để lưu trữ hoặc phân tích mà không phải thay đổi cấu trúc tổng thể của cơ sở dữ liệu.

2. **Cách tiếp cận code-first**

Lợi ích thứ hai là MongoDB sử dụng cách tiếp cận `code-first`. Trong cơ sở dữ liệu quan hệ, bạn phải xây dựng `thiết kế bảng` (table design) trước, sau đó mới có thể làm việc với dữ liệu. Điều này thường làm tăng thêm độ phức tạp cho việc bắt đầu.

Ngược lại, MongoDB làm việc với `document`, nghĩa là bạn có thể truy cập và làm việc với dữ liệu mà không cần phải thông qua các định nghĩa bảng phức tạp.

![codefirst](codefirst.png)

- Ví dụ: Khi bạn kết nối với cơ sở dữ liệu MongoDB, bạn có thể bắt đầu viết dữ liệu ngay lập tức mà không cần tạo cấu trúc bảng phức tạp như trong SQL.

Điều này loại bỏ nhu cầu sử dụng bất kỳ framework của bên thứ ba nào để thực hiện các thao tác đọc và ghi, giúp giảm bớt các bước trung gian khi triển khai.

3. **Schema phát triển theo thời gian**

Một lợi ích quan trọng khác là khả năng schema phát triển trong MongoDB.

- Ví dụ thực tế: Giả sử bạn đang vận hành một công ty chuyển phát (courier company) và cần lưu trữ địa chỉ giao hàng. Với những thay đổi lớn trong quy trình giao hàng, chẳng hạn như các biện pháp giao hàng không tiếp xúc trong năm 2020, bạn cần cập nhật schema để lưu trữ thông tin mới về giao hàng an toàn mà không gây gián đoạn lớn đến hệ thống. Trong MongoDB, điều này được thực hiện một cách dễ dàng. Bạn chỉ cần thêm trường thông tin mới vào document mà không cần phải sửa đổi các bảng hoặc cấu trúc dữ liệu đã có.

![schema_develop](schema_develop.png)

4. **Lưu trữ dữ liệu không cấu trúc**

- Ví dụ: Hãy tưởng tượng bạn xây dựng một ứng dụng tổng hợp dữ liệu chứng khoán (stock market aggregator), lấy dữ liệu từ nhiều nguồn khác nhau. Mỗi nguồn có thể cung cấp dữ liệu với các hình dạng khác nhau, tức là về cơ bản, đây là dữ liệu không có cấu trúc. MongoDB, với tính linh hoạt trong việc lưu trữ, cho phép bạn lưu tất cả dữ liệu này trong một collection duy nhất mà không gặp phải các hạn chế của cơ sở dữ liệu quan hệ.
![store_unstructed_data](store_unstructed_data.png)

1. **Khả năng truy vấn và phân tích dữ liệu**

MongoDB hỗ trợ một ngôn ngữ truy vấn riêng gọi là `Mongo Query Language (MQL)`. MQL có một số lượng lớn các `toán tử (operators)` giúp bạn tạo các truy vấn phức tạp để tìm kiếm dữ liệu.

- Ví dụ: Nếu bạn muốn nhóm kết quả của tất cả sinh viên theo năm học và tìm những sinh viên có điểm cao nhất trong từng kỳ học, bạn có thể sử dụng các toán tử trong MQL hoặc các `aggregation pipelines` để thực hiện điều này.

MongoDB cung cấp các công cụ mạnh mẽ như aggregation pipelines giúp bạn thực hiện phân tích dữ liệu phức tạp ngay trên server, mà không cần phải chuyển dữ liệu ra ngoài để phân tích.

6. **Tính khả dụng cao (High Availability)**

Một lợi ích quan trọng cuối cùng là khả năng `khả dụng cao` (high availability) của MongoDB. MongoDB có sẵn tính năng này nhờ `sự dư thừa dữ liệu` (redundancy).

- Ví dụ thực tế: Trong một hệ thống MongoDB thông thường, sẽ có ít nhất ba nút (nodes) trong một `replica set`. Trong đó, một nút là `primary member` (thành viên chính), và các nút còn lại là `secondary members` (thành viên phụ). MongoDB thực hiện `replication` (sao lưu dữ liệu) để giữ bản sao của dữ liệu trên các nút khác nhau trong cụm (cluster).

Nếu một nút gặp sự cố, các nút khác sẽ tiếp quản mà không gây gián đoạn dịch vụ. Điều này cũng rất hữu ích trong quá trình `bảo trì hệ thống`, khi bạn cần thực hiện cập nhật phần mềm, hệ điều hành, hay các bản vá bảo mật mà không làm ngừng hoạt động của hệ thống.

7. **Summary**

Trong bài giảng này, bạn đã học về các lợi ích chính của MongoDB, bao gồm:

- **Tính linh hoạt của schema**: Bạn có thể thay đổi schema bất cứ lúc nào mà không cần thông qua các câu lệnh định nghĩa dữ liệu phức tạp.
- **Cách tiếp cận code-first**: Bạn có thể làm việc với dữ liệu ngay lập tức mà không cần thiết kế bảng trước.
- **Schema phát triển**: Bạn có thể dễ dàng thêm các trường mới mà không phải sửa đổi cấu trúc dữ liệu cũ.
- **Truy vấn và phân tích dữ liệu**: MongoDB cung cấp công cụ mạnh mẽ cho phép bạn thực hiện các truy vấn và phân tích phức tạp ngay trong cơ sở dữ liệu.
- **Khả năng cao về tính sẵn sàng**: MongoDB hỗ trợ khả năng dư thừa và sao lưu, đảm bảo hệ thống luôn sẵn sàng và không bị gián đoạn ngay cả khi xảy ra sự cố hoặc bảo trì.

MongoDB là một công cụ mạnh mẽ và linh hoạt, giúp đáp ứng tốt các nhu cầu dữ liệu phức tạp và thay đổi nhanh chóng trong các ứng dụng hiện đại.

# 3. MongoDB Use Cases

1. **Many Sources - One View (Nhiều Nguồn - Một Tầm Nhìn)**

MongoDB cho phép bạn tập hợp dữ liệu từ nhiều nguồn khác nhau, thay vì để từng phần dữ liệu sống độc lập trong các hệ thống riêng biệt (silos). Điều này có nghĩa là bạn có thể thu thập các loại dữ liệu có định dạng và hình dạng khác nhau, và lưu trữ chúng trong MongoDB để có một cái nhìn tổng thể, nhờ vào schema linh hoạt mà MongoDB hỗ trợ.

- Ví dụ thực tế: Bạn có một hệ thống quản lý khách hàng (CRM) với dữ liệu từ nhiều nguồn khác nhau như website, email, và các ứng dụng di động. Mỗi nguồn có thể có dữ liệu khác nhau về khách hàng. MongoDB cho phép bạn tổng hợp tất cả thông tin này lại trong một collection duy nhất, giúp bạn có một cái nhìn toàn diện về khách hàng mà không cần phải làm việc với các bảng phức tạp như trong cơ sở dữ liệu quan hệ.

2. **Internet of Things (IoT)**

MongoDB có thể được sử dụng với các thiết bị IoT (Internet of Things). Hiện nay, có hàng tỷ thiết bị IoT trên toàn cầu, từ những thành phần nhỏ trong xe tự hành (autonomous car) cho đến bóng đèn được kết nối Internet. Những thiết bị này tạo ra khối lượng dữ liệu khổng lồ.

- Ví dụ: Một trạm thời tiết gửi thông tin nhiệt độ và tốc độ gió mỗi phút. Nhờ khả năng mở rộng (scalability), MongoDB có thể dễ dàng lưu trữ toàn bộ dữ liệu này ở phạm vi toàn cầu. Sau khi dữ liệu được lưu trữ trong MongoDB, nhờ khả năng truy vấn mạnh mẽ, bạn có thể thực hiện các phân tích phức tạp và ra quyết định dựa trên dữ liệu từ các thiết bị IoT.

3. **E-commerce (Thương mại điện tử)**

MongoDB rất phù hợp với các giải pháp thương mại điện tử. Các sản phẩm được bán trên các trang web thương mại điện tử có các thuộc tính khác nhau.

- Ví dụ: Một chiếc điện thoại có các thuộc tính như dung lượng bộ nhớ, mạng và màu sắc. Trong khi đó, một cuốn sách lại có các thuộc tính như nhà xuất bản, tác giả và số trang. Các sản phẩm cũng có những thuộc tính như đánh giá cao nhất, giá bán, hàng tồn kho và các thông tin khác.

Với sự hỗ trợ của `documents`, `sub-documents`, và `list properties` trong MongoDB, bạn có thể lưu trữ tất cả các thông tin này cùng nhau, tối ưu hóa cho việc truy xuất dữ liệu. Điều này làm cho MongoDB trở thành lựa chọn hoàn hảo cho các trường hợp sử dụng yêu cầu schema động.

4. **Phân tích thời gian thực (Real-time Analytics)**

Hầu hết các tổ chức đều muốn đưa ra các quyết định tốt hơn dựa trên dữ liệu của họ. Việc phân tích dữ liệu lịch sử là dễ dàng, nhưng rất ít tổ chức có thể phản ứng với những thay đổi đang diễn ra từng phút. Phần lớn điều này là do các quá trình Extract, Transform, and Load (ETL) phức tạp.

- Ví dụ thực tế: Với MongoDB, bạn có thể thực hiện hầu hết các phân tích ngay tại nơi lưu trữ dữ liệu mà không cần phải chuyển dữ liệu ra ngoài. Dữ liệu có thể là bán cấu trúc hoặc hoàn toàn không có cấu trúc. Điều này cho phép bạn thực hiện phân tích thời gian thực một cách nhanh chóng và hiệu quả, giúp tổ chức phản ứng kịp thời với những thay đổi.

5. **Gaming (Trò chơi)**

MongoDB cũng đóng vai trò quan trọng trong thế giới gaming. Ngày càng nhiều trò chơi đa người chơi (multiplayer) được chơi trên toàn cầu, và việc truy cập dữ liệu trở nên rất quan trọng.

- Ví dụ: Trong các trò chơi multiplayer, việc xử lý dữ liệu từ hàng triệu người chơi đồng thời đòi hỏi một hệ thống cơ sở dữ liệu có khả năng mở rộng tốt. MongoDB cung cấp tính năng sharding (chia mảnh), giúp dễ dàng mở rộng và hỗ trợ người dùng trên toàn thế giới. Với schema linh hoạt, MongoDB cũng dễ dàng hỗ trợ những nhu cầu dữ liệu luôn thay đổi của trò chơi, như việc cập nhật bản đồ, nhân vật, hoặc các yếu tố trong trò chơi.

6. **Finance (Tài chính)**

MongoDB cũng có nhiều ứng dụng trong ngành tài chính. Ngày nay, chúng ta muốn các giao dịch ngân hàng diễn ra nhanh chóng và mong đợi ngành tài chính giữ an toàn thông tin của chúng ta.

- Ví dụ: Với MongoDB, bạn có thể thực hiện hàng ngàn thao tác trên cơ sở dữ liệu mỗi giây. Tất cả thông tin đều được mã hóa trong quá trình truyền tải và khi được lưu trữ trên đĩa. Ngoài ra, MongoDB còn cho phép mã hóa từng trường dữ liệu riêng lẻ, đảm bảo an toàn cho các thông tin nhạy cảm, giúp ngăn ngừa sự cố về dữ liệu.

Trong ngành tài chính, yêu cầu về tính khả dụng và độ tin cậy rất cao. Các hệ thống tài chính cần phải hoạt động liên tục, không có thời gian chết. MongoDB hỗ trợ yêu cầu này, khiến nó trở thành sự lựa chọn tuyệt vời cho các ngân hàng, công ty giao dịch và các tổ chức tài chính nói chung.

7. **Summary**

- **Many Sources - One View**: Giúp bạn tổng hợp dữ liệu từ nhiều nguồn khác nhau để có cái nhìn tổng thể.
- **IoT**: Lưu trữ và phân tích dữ liệu khổng lồ từ các thiết bị IoT trên toàn cầu.
- **E-commerce**: Quản lý và tối ưu hóa việc truy xuất dữ liệu sản phẩm với cấu trúc schema động.
- **Phân tích thời gian thực**: Phân tích dữ liệu ngay tại nơi lưu trữ, cho phép phản ứng nhanh với những thay đổi.
- **Gaming**: Hỗ trợ các trò chơi đa người chơi với khả năng mở rộng và quản lý dữ liệu linh hoạt.
- **Tài chính**: Thực hiện hàng ngàn giao dịch mỗi giây, đảm bảo an toàn thông tin và đáp ứng yêu cầu về tính khả dụng liên tục.

MongoDB cung cấp khả năng mở rộng tuyệt vời và cho phép phân tích dữ liệu thời gian thực, giúp bạn đáp ứng nhu cầu của các ứng dụng phức tạp trong nhiều ngành công nghiệp khác nhau.

# 4. Hands-on: Getting Started with MongoDB

[Cài đặt Mongodb Ubuntu](https://nxcuong.ued.vn/vi/news/databses/huong-dan-cai-dat-mongodb-tren-ubuntu-22-04-voi-7-buoc-157.html)

[Lab instruction](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAxNTFFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvTW9uZ29EQi9MYWIlMjAtJTIwTW9uZ29EQiUyMEdldHRpbmclMjBTdGFydGVkLm1kIiwidG9vbF90eXBlIjoidGhlaWFkb2NrZXIiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTcyNTI3MTgxNX0.NIyCPFUmOS4OXVJRby_RwAEy7Psq_0BMKTOIp9DSJgE)

Đăng nhập vào MongoDB: 

```bash
mongosh -u AdminCherry -p --authenticationDatabase admin
```


# 4. CRUD Operations

Mongo shell là một công cụ dòng lệnh do MongoDB cung cấp, cho phép bạn tương tác với cơ sở dữ liệu của mình. Nó là một giao diện tương tác sử dụng JavaScript và bạn có thể dùng nó để thực hiện các thao tác dữ liệu cũng như quản lý cơ sở dữ liệu.

## 4.1. Connect to MongoDB

Đầu tiên, để kết nối với một cụm (cluster) MongoDB, bạn cần cung cấp connection string (chuỗi kết nối). Sau khi kết nối thành công, bạn có thể xem danh sách các cơ sở dữ liệu bằng cách sử dụng lệnh `show dbs`.

- Ví dụ: Bạn đã kết nối với một instance MongoDB. Để bắt đầu làm việc với cơ sở dữ liệu quản lý khuôn viên (campus management database), bạn sẽ sử dụng lệnh `use campus_management`. Sau đó, bạn có thể sử dụng lệnh `show collections` để xem các collections có sẵn. Trong ví dụ này, hai collections là staff và students.

## 4.2. CRUD Operations

CRUD là viết tắt của Create (Tạo), Read (Đọc), Update (Cập nhật), và Delete (Xóa). Đây là các thao tác cơ bản trong việc quản lý dữ liệu trên MongoDB.

### 4.2.1. CREATE

**Create Operation (Tạo dữ liệu)**

Để tạo một document mới trong MongoDB, bạn sẽ sử dụng lệnh `insertOne`. Cú pháp là `DB.collection.insertOne(document)`, trong đó DB là tên cơ sở dữ liệu, `collection` là tên của collection, và `document` là tài liệu mà bạn muốn chèn.

- Ví dụ: Bạn muốn thêm một sinh viên mới vào collection students. Bạn có thể sử dụng lệnh:

```javascript
db.students.insertOne({ name: "John Doe", email: "john@example.com" })
```

Kết quả sẽ trả về `insertedId`, cho biết tài liệu đã được chèn thành công. Trường `_id` là một trường bắt buộc trong mỗi tài liệu MongoDB và nếu bạn không cung cấp, Mongo shell sẽ tự động tạo một `ObjectId`.

**Create nhiều documents**

Mongo shell cũng hỗ trợ chèn nhiều documents cùng lúc bằng cách sử dụng lệnh `insertMany`.

- Ví dụ: Bạn muốn chèn danh sách sinh viên mới:

```javascript
let students_list = [
    { name: "Alice Smith", email: "alice@example.com" },
    { name: "Bob Johnson", email: "bob@example.com" }
]
db.students.insertMany(students_list)
```

### 4.2.2. READ

**Bạn có thể đọc dữ liệu từ MongoDB bằng cách sử dụng lệnh `find` và `findOne`.**

**Read đơn giản**

- Ví dụ: Bạn muốn tìm sinh viên đầu tiên trong collection students mà không cần điều kiện lọc:

```javascript
db.students.findOne()
```

**Read có điều kiện**

Bạn có thể sử dụng bộ lọc để tìm tài liệu dựa trên các tiêu chí cụ thể.

- Ví dụ: Bạn muốn tìm sinh viên có địa chỉ email cụ thể:

```javascript
db.students.findOne({ email: "john@example.com" })
```

**Read nhiều tài liệu**

Nếu bạn muốn tìm tất cả các sinh viên có họ là "Doe", bạn có thể sử dụng lệnh `find`.

```javascript
db.students.find({ last_name: "Doe" })
```

**Đếm số tài liệu**

Bạn cũng có thể sử dụng lệnh `count` để đếm số lượng tài liệu phù hợp với tiêu chí lọc.

- Ví dụ: Đếm số lượng sinh viên có họ là "Doe":

```javascript
db.students.count({ last_name: "Doe" })
```

### 4.2.3. UPDATE

MongoDB cho phép bạn cập nhật dữ liệu theo hai cách: `thay thế toàn bộ tài liệu` hoặc `cập nhật một phần của tài liệu`.

**Thay thế toàn bộ tài liệu**

Khi bạn muốn thay thế toàn bộ nội dung của một tài liệu, bạn sử dụng lệnh `replaceOne`.

- Ví dụ: Bạn tìm một sinh viên có họ "Doe" và thay thế toàn bộ thông tin với bản ghi mới:

```javascript
db.students.replaceOne({ last_name: "Doe" }, { name: "Jane Doe", email: "jane@campus.edu", online: true })
```

**Cập nhật một phần tài liệu**

Nếu bạn chỉ muốn cập nhật một phần tài liệu, bạn sử dụng lệnh `updateOne` với cú pháp `$set`.

- Ví dụ: Bạn muốn cập nhật trạng thái online của sinh viên:

```javascript
db.students.updateOne({ last_name: "Doe" }, { $set: { online: true } })
```

**Cập nhật nhiều tài liệu**

Khi cần cập nhật nhiều tài liệu cùng một lúc, bạn sử dụng lệnh `updateMany`.

- Ví dụ: Cập nhật tất cả sinh viên sang trạng thái học online do lệnh giãn cách xã hội:

```javascript
db.students.updateMany({}, { $set: { online: true } })
```

### 4.2.4. DELETE

MongoDB cho phép bạn xóa tài liệu với các lệnh `deleteOne` và `deleteMany`.

**Xóa một tài liệu**

- Ví dụ: Bạn muốn xóa sinh viên có email là "john@example.com":

```javascript
db.students.deleteOne({ email: "john@example.com" })
```

**Xóa nhiều tài liệu**

- Ví dụ: Xóa tất cả sinh viên có họ "Doe":

```javascript
db.students.deleteMany({ last_name: "Doe" })
```

## 4.3. Hands-on

[Lab Instruction](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAxNTFFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvTW9uZ29EQi9MYWIlMjAtJTIwTW9uZ29EQiUyMENSVUQubWQiLCJ0b29sX3R5cGUiOiJ0aGVpYWRvY2tlciIsImFkbWluIjpmYWxzZSwiaWF0IjoxNzI1Mjc0NDQ5fQ.Rp9N_8kqqqbyj7b5uc7lqOUAupV0UC9dPUvF-eNlGNM)

# 5. Indexes

## 5.1. Why we need Indexes?

Indexes giúp ta tìm kiếm dữ liệu một cách nhanh chóng mà không cần phải duyệt qua toàn bộ cơ sở dữ liệu. Để hiểu rõ hơn, hãy tưởng tượng bạn đang ở thư viện Anh Quốc (British Library) với 25 triệu quyển sách. Bạn muốn tìm quyển "Designing Data-Intensive Applications" của Martin Kleppmann.

- Nếu không có indexes, bạn phải tìm kiếm quyển sách này trong tất cả các kệ sách, một việc rất tốn thời gian.
- Nhưng với indexes, bạn có thể dễ dàng vào đúng khu vực về máy tính, rồi đến ngăn sách về cơ sở dữ liệu, và cuối cùng tìm trên kệ "M" để tìm sách của Martin Kleppmann.

Indexes tương tự như những công cụ giúp chúng ta tìm kiếm thông tin hàng ngày, như:

- Danh bạ điện thoại (trước đây): Tên của mọi người được sắp xếp theo họ và tên. Nếu muốn tìm ai đó tên John Doe, bạn chỉ cần tra mục "D" rồi tiếp tục tìm "John".
- Từ điển: Các từ được sắp xếp theo thứ tự chữ cái.
- Mục lục ở cuối sách: Cho phép bạn nhanh chóng tìm nội dung cần thiết trong sách.

## 5.2. Indexes in MongoDb

Trong các hệ thống cơ sở dữ liệu, indexes nên được tạo cho những truy vấn phổ biến nhất để tối ưu hiệu suất. Chúng ta sẽ tìm hiểu ví dụ từ cơ sở dữ liệu quản lý khuôn viên (C`ampus Management Database`).

**Ví dụ về Index**

Giả sử chúng ta có collection về đăng ký khóa học (`course enrollment collection`) và thường xuyên tìm kiếm các sinh viên theo `courseId` (mã khóa học). Thay vì quét toàn bộ collection, chúng ta có thể tạo một chỉ mục (index) trên trường `courseId` để tối ưu hóa quá trình tìm kiếm.

- Tạo chỉ mục: Chúng ta có thể tạo chỉ mục theo thứ tự tăng dần như sau:
  ```javascript
  db.course_enrollment.createIndex({ courseId: 1 })
  ```

  - Ý nghĩa: courseId : 1 có nghĩa là chúng ta lưu chỉ mục theo thứ tự tăng dần.

Chỉ mục này sẽ giúp ta tìm các tài liệu có `courseId` cụ thể nhanh hơn mà không phải duyệt toàn bộ collection. Tuy nhiên, nếu ta muốn sắp xếp các sinh viên theo `studentId` (mã sinh viên) trong quá trình tìm kiếm, MongoDB sẽ phải thực hiện sắp xếp trong bộ nhớ (in-memory sort), điều này sẽ không hiệu quả.

## 5.3. Compound Index

Trong trường hợp này, chúng ta có thể sử dụng `compound index` - tức là chỉ mục trên nhiều hơn một trường.

- Ví dụ: Để tìm các sinh viên có `courseId` là `1547` và đồng thời sắp xếp họ theo `studentId` theo thứ tự tăng dần, chúng ta có thể tạo compound index như sau:
  ```javascript
   db.course_enrollment.createIndex({ courseId: 1, studentId: 1 })
  ```
  - Ý nghĩa: Khi MongoDB tạo chỉ mục, các tài liệu sẽ được sắp xếp trước theo courseId, sau đó, với những tài liệu có cùng courseId, chúng sẽ được sắp xếp tiếp theo theo studentId.

  - Lợi ích: Điều này giúp cho quá trình tìm kiếm và sắp xếp các tài liệu trở nên hiệu quả hơn vì các tài liệu đã được tổ chức sẵn trong chỉ mục.

## 5.4. How MongoDB store indexes?

Indexes trong MongoDB là các `cấu trúc dữ liệu đặc biệt`, chúng lưu trữ các trường mà bạn chỉ mục và vị trí của tài liệu đó trên đĩa.

- MongoDB lưu trữ các chỉ mục theo cấu trúc `cây cân bằng` (balanced tree). Điều này giúp quá trình tìm kiếm tài liệu trở nên hiệu quả hơn, dù đó là tìm kiếm theo điều kiện bằng (`equality search`) hay theo khoảng (`range search`).

- Ví dụ minh họa về cấu trúc cây: Trong ví dụ với courseId, mỗi nút trên cây đại diện cho một courseId, và dưới mỗi nút đó, các sinh viên được sắp xếp theo thứ tự tăng dần của studentId.

## 5.5. Hands-on lab

[Lab Instruction](https://cf-courses-data.static.labs.skills.network/IBM-DB0151EN-SkillsNetwork/labs/MongoDB/Lab%20-%20MongoDB%20Indexing.md.html)

# 6. Aggregation Framework

## 6.1. What is Aggregation Framework?

`Aggregation Framework`, hay còn được gọi là `Aggregation Pipeline`, là một chuỗi các phép toán bạn áp dụng lên dữ liệu để đạt được kết quả mong muốn. Đây là cách mà MongoDB cho phép bạn thực hiện các phân tích dữ liệu phức tạp dựa trên một loạt các giai đoạn, mỗi giai đoạn sẽ xử lý dữ liệu theo một cách nhất định.

**Ví dụ minh họa**

Giả sử bạn muốn hiểu rõ về sự tiến bộ của sinh viên thông qua việc `tính điểm trung bình của sinh viên` trong năm 2020, được sắp xếp theo `courseId` (mã khóa học). Để có được thông tin này, bạn sẽ cần thực hiện các bước sau:

1. Lọc các tài liệu thuộc năm 2020.
2. Nhóm các tài liệu này theo courseId.
3. Tính điểm trung bình cho mỗi nhóm.

Để minh họa rõ hơn, hãy xem xét một tập dữ liệu về `courseResults` (kết quả khóa học) với các trường `courseId`, `năm học` và `điểm số`.

## 6.2. Stages in Aggregation Framework

`Aggregation Framework` bao gồm nhiều giai đoạn (stages), mỗi giai đoạn thực hiện một thao tác cụ thể trên dữ liệu. Các giai đoạn thường gặp bao gồm:

- **$match**: Dùng để lọc các tài liệu dựa trên một tiêu chí nhất định.
- **$group**: Nhóm các tài liệu lại với nhau dựa trên một group key (khóa nhóm).
- **$project**: Chọn lọc các trường cần hiển thị trong kết quả cuối cùng.
- **$sort**: Sắp xếp dữ liệu theo thứ tự nhất định.
- **$count**: Đếm số lượng tài liệu trong một giai đoạn.
- **$merge**: Lưu kết quả vào một collection khác.

**Ví dụ cụ thể**

Giả sử bạn có tập dữ liệu như sau:

```json
[
    { "courseId": 1, "year": 2020, "score": 85 },
    { "courseId": 1, "year": 2020, "score": 90 },
    { "courseId": 2, "year": 2020, "score": 78 },
    { "courseId": 2, "year": 2020, "score": 82 }
]
```

- **Bước 1: $match**
  - Dùng $match để lọc các tài liệu có năm học 2020:
    ```javascript
    db.courseResults.aggregate([
      { $match: { year: 2020 } }
    ])
    ```
    Kết quả sẽ chỉ bao gồm các tài liệu thuộc năm 2020.
- **Bước 2: $group**
  - Sử dụng $group để nhóm các tài liệu theo courseId và tính điểm trung bình cho mỗi khóa học:
    ```javascript
    db.courseResults.aggregate([
      { $match: { year: 2020 } },
      { $group: { _id: "$courseId", averageScore: { $avg: "$score" } } }
    ])
    ```
    Trong kết quả, mỗi tài liệu sẽ chứa một courseId và điểm trung bình cho khóa học đó. Chẳng hạn, bạn sẽ nhận được:
    ```json
    [
        { "_id": 1, "averageScore": 87.5 },
        { "_id": 2, "averageScore": 80 }
    ]
    ```

## 6.3. Other common stages in Aggregation Pipeline

**$project**

- $project dùng để tái cấu trúc tài liệu bằng cách chọn những trường cần hiển thị hoặc loại bỏ những trường không cần thiết. Ví dụ, chỉ muốn hiển thị firstName và lastName của sinh viên:
  ```javascript
  db.students.aggregate([
    { $project: { firstName: 1, lastName: 1 } }
  ])
  ```

**$sort**

- $sort dùng để sắp xếp tài liệu theo thứ tự tăng dần hoặc giảm dần dựa trên một trường nào đó. Ví dụ, sắp xếp sinh viên theo lastName theo thứ tự giảm dần:
  ```javascript
  db.students.aggregate([
    { $sort: { lastName: -1 } }
  ])
  ```

**$count**

- $count dùng để đếm số lượng tài liệu trong giai đoạn đó và trả về tổng số sinh viên:
  ```javascript
  db.students.aggregate([
    { $count: "totalStudents" }
  ])
  ```

  Kết quả sẽ là:
  ```json

  { "totalStudents": 3 }
  ```

**$merge**

- $merge dùng để lưu kết quả của quá trình tổng hợp vào một collection mới. Ví dụ, bạn muốn lưu kết quả trung bình điểm của sinh viên vào một collection mới tên là `averageScores`:

  ```javascript
  db.courseResults.aggregate([
    { $match: { year: 2020 } },
    { $group: { _id: "$courseId", averageScore: { $avg: "$score" } } },
    { $merge: "averageScores" }
  ])
  ```
  Kết quả sẽ không được hiển thị trực tiếp, nhưng MongoDB sẽ lưu trữ các tài liệu này trong collection `averageScores`.

## 6.4. When we use Aggregation Framework?

`Aggregation Framework` là công cụ rất mạnh mẽ cho việc phân tích dữ liệu phức tạp trong MongoDB. Các trường hợp sử dụng phổ biến bao gồm:

- Theo dõi tiến trình học tập: Bạn có thể sử dụng aggregation để tính toán điểm trung bình của sinh viên theo từng khóa học và năm học.
- Ứng dụng thương mại điện tử: Tính toán doanh thu trung bình của sản phẩm theo từng quốc gia.
- Tính toán tổng hợp: Aggregation cho phép bạn thực hiện các phép tính từ đơn giản đến phức tạp, nhóm dữ liệu thành các nhóm có ý nghĩa để cung cấp những thông tin giá trị.

## 6.5. Summary

- Aggregation Framework là một chuỗi các phép toán được áp dụng lên dữ liệu để đạt được kết quả phân tích mong muốn.
- Bạn có thể xây dựng quy trình tổng hợp dữ liệu bằng cách sử dụng các giai đoạn như $match, $group, $project, $sort, và $merge.
- Aggregation Framework hữu ích trong các nhiệm vụ phân tích và báo cáo, giúp thực hiện những phép toán phức tạp trên dữ liệu lớn mà vẫn đảm bảo hiệu quả.

## 6.6. Hands-on Lab

[Lab Instruction](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAxNTFFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvTW9uZ29EQi9MYWIlMjAtJTIwTW9uZ29EQiUyMEFnZ3JlZ2F0aW9uLm1kIiwidG9vbF90eXBlIjoidGhlaWFkb2NrZXIiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTcyNDI1OTgyM30.LrQ0xcd-TCrhRm2vz4NsYZ7qSrE941RtUzm35sqA32A)

# 7. Replication and Sharding in MongoDB

## 7.1. What is Replication?

`Replication` (nhân bản) là việc tạo ra nhiều bản sao của dữ liệu trong một hệ thống cơ sở dữ liệu. Một Replica Set trong MongoDB bao gồm ít nhất ba `node` chứa dữ liệu giống nhau. Điều này có nghĩa là tất cả các `node` trong `Replica Set` đều có cùng một dữ liệu.

**Cách hoạt động của Replication**

Dữ liệu được ghi vào `primary node` (nút chính), sau đó nó sẽ được sao chép sang các `secondary node` (nút phụ). Quá trình này tạo ra `redundancy` (sự dư thừa), nghĩa là nếu một phần cứng gặp sự cố, bạn vẫn có nhiều bản sao của dữ liệu để duy trì tính khả dụng cao cho cơ sở dữ liệu của bạn.

Ví dụ: Hãy tưởng tượng bạn có một cơ sở dữ liệu chứa thông tin sinh viên. Cơ sở dữ liệu này được triển khai trên ba node trong một Replica Set:

- **Primary Node**: Nút này chịu trách nhiệm nhận và xử lý các yêu cầu ghi (insert, update, delete) từ ứng dụng.
- **Secondary Node 1 và Secondary Node 2**: Hai nút này chỉ nhận các bản sao của dữ liệu từ Primary Node.

Nếu Primary Node gặp sự cố, một trong các Secondary Node sẽ được bầu chọn làm Primary Node mới để tiếp tục nhận các yêu cầu ghi.

## 7.2. Benefit of Replication

- **Tăng cường tính khả dụng**: Replication giúp đảm bảo cơ sở dữ liệu vẫn hoạt động ngay cả khi một hoặc nhiều node gặp sự cố.
- **Redundancy (dư thừa)**: Có nhiều bản sao của dữ liệu giúp ngăn ngừa mất dữ liệu trong trường hợp phần cứng gặp vấn đề.
- **Bảo trì dễ dàng**: Có thể thực hiện bảo trì hoặc cập nhật phần mềm một cách tuần tự trên từng node mà không làm gián đoạn dịch vụ.

**Hiểu lầm phổ biến về Replication**

Nhiều người nghĩ rằng replication có thể cứu bạn khỏi các thảm họa như xóa nhầm cơ sở dữ liệu. Tuy nhiên, nếu bạn xóa dữ liệu trên `Primary Node`, thao tác đó sẽ được sao chép sang các `Secondary Node`. Do đó, replication không phải là giải pháp bảo vệ khỏi các lỗi do con người gây ra. Đối với những trường hợp này, bạn cần sử dụng `backups` (sao lưu) và quy trình `phục hồi`.

## 7.3. Relication Process in MongoDB

Khi ứng dụng ghi thay đổi vào `Primary Node`, nó sẽ ghi lại các thay đổi này vào `Oplog` (Operations Log) của nó, bao gồm cả dấu thời gian (timestamp). Các `Secondary Node` sẽ theo dõi `Oplog` của `Primary Node` để sao chép và áp dụng các thay đổi đó vào bản sao của mình.

**Ví dụ minh họa**

Giả sử bạn có một cơ sở dữ liệu chứa thông tin sinh viên với ba bản ghi sinh viên:

```json
[
    { "studentId": 1, "name": "John Doe" },
    { "studentId": 2, "name": "Jane Smith" },
    { "studentId": 3, "name": "Alice Johnson" }
]
```

Bạn thực hiện lệnh sau để xóa tất cả sinh viên:

```javascript
db.students.deleteMany({})
```

Trong `Oplog`, lệnh này sẽ được ghi lại như một thao tác duy nhất. Sau đó, các `Secondary Node` sẽ sao chép thao tác này và xóa các bản ghi tương ứng từ cơ sở dữ liệu của chúng.

## 7.4. What is Sharding?

Khi dữ liệu của bạn ngày càng lớn và phần cứng hiện tại không còn đủ khả năng lưu trữ hay xử lý, bạn có thể mở rộng hệ thống theo chiều ngang bằng cách sử dụng Sharding. Sharding là việc phân tán các bộ sưu tập dữ liệu lớn thành nhiều phân mảnh nhỏ hơn và lưu trữ chúng trên nhiều node khác nhau.

**Lợi ích của Sharding**

- **Tăng khả năng lưu trữ**: Bạn có thể lưu trữ nhiều dữ liệu hơn mà không bị giới hạn bởi dung lượng của một node duy nhất.
- **Tăng hiệu suất**: Phân chia dữ liệu giúp tăng tốc độ đọc và ghi bằng cách phân tán tải công việc cho nhiều node.
- **Phân vùng địa lý**: Bạn có thể phân vùng dữ liệu theo khu vực. Ví dụ, dữ liệu của khách hàng Mỹ sẽ được lưu trữ trên các shard ở Mỹ, trong khi dữ liệu của khách hàng châu Âu sẽ được lưu trên các shard ở châu Âu.

**Ví dụ về Sharding**

Giả sử bạn có một ứng dụng thương mại điện tử với dữ liệu khách hàng toàn cầu. Bạn có thể phân chia dữ liệu theo khu vực địa lý:

- **Shard 1:** Lưu trữ dữ liệu khách hàng ở Mỹ.
- **Shard 2:** Lưu trữ dữ liệu khách hàng ở châu Âu.
- **Shard 3:** Lưu trữ dữ liệu khách hàng ở châu Á.

Điều này giúp cải thiện hiệu suất truy vấn và cung cấp trải nghiệm người dùng tốt hơn.

## 7.5. How Replication and Sharding work?

- **Replication**: Chỉ có Primary Node mới có thể nhận các yêu cầu ghi (insert, update, delete) từ ứng dụng. Khi Primary Node không khả dụng, một Secondary Node sẽ được chọn làm Primary Node mới thông qua quá trình bầu chọn (election).
- **Sharding**: Dữ liệu được phân mảnh thành các shard nhỏ hơn, mỗi shard có thể là một Replica Set riêng biệt. Khi bạn gửi một truy vấn, MongoDB sẽ xác định shard nào chứa dữ liệu liên quan và chỉ gửi truy vấn đến shard đó, giúp tăng tốc độ truy vấn.

**Quá trình bầu chọn trong Replication**

Quá trình bầu chọn trong MongoDB đảm bảo rằng chỉ có một node trở thành `Primary Node`, giúp tránh hiện tượng "split-brain" (trạng thái mà có nhiều `Primary Node` tồn tại cùng lúc). Các thành viên trong Replica Set sẽ bầu chọn node có dữ liệu cập nhật nhất và độ trễ sao chép tối thiểu để trở thành `Primary Node`.

## 7.6. Summary

- Replication giúp tạo ra nhiều bản sao của dữ liệu, đảm bảo tính khả dụng và dư thừa, nhưng không thể ngăn chặn các thảm họa như xóa nhầm dữ liệu.
- Sharding giúp mở rộng cơ sở dữ liệu theo chiều ngang, cho phép lưu trữ nhiều dữ liệu hơn và cải thiện hiệu suất đọc/ghi.
- Replication và Sharding có thể được sử dụng cùng nhau để xây dựng các hệ thống cơ sở dữ liệu lớn, phức tạp và có khả năng mở rộng cao.

Replication và Sharding là hai công cụ quan trọng trong MongoDB, giúp bạn xây dựng các hệ thống cơ sở dữ liệu mạnh mẽ và linh hoạt, phục vụ tốt cho các ứng dụng từ nhỏ đến lớn.

# 8. Access MongoDB with Python

[Tutorial Script](access_mongodb_tutorial.py)

[Hans-on Lab Instruction](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAxNTFFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvTW9uZ29EQi9MYWIlMjAtJTIwQWNjZXNzaW5nJTIwTW9uZ29EQiUyMHVzaW5nJTIwUHl0aG9uLm1kIiwidG9vbF90eXBlIjoidGhlaWFkb2NrZXIiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTcyNDI1OTgwOX0.RVsEeRawOv6oZkFJqkTLFQDe4aTWEGyUrcRO2h629lA)

