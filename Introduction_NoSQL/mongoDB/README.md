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

