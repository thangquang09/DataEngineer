- [1. Data Warehouses](#1-data-warehouses)
  - [1.1. What is Data Warehouses](#11-what-is-data-warehouses)
  - [1.2. History and Development of Data Warehouse](#12-history-and-development-of-data-warehouse)
  - [1.3. Data Warehouses Use Cases](#13-data-warehouses-use-cases)
  - [1.4. Benefit of Using Data Warehouses](#14-benefit-of-using-data-warehouses)
  - [1.5. Population Data Warehouse Systems](#15-population-data-warehouse-systems)
    - [1.5.1. Data Warehouse Application](#151-data-warehouse-application)
    - [1.5.2. Data Warehouse Cloud](#152-data-warehouse-cloud)
    - [1.5.3. Data Warehouse supports both of Cloud and On-premesis](#153-data-warehouse-supports-both-of-cloud-and-on-premesis)
    - [1.5.4. Example](#154-example)
  - [1.6. Selecting Data Warehouse Systems](#16-selecting-data-warehouse-systems)
    - [1.6.1. Tính năng và khả năng của hệ thống Data Warehouse](#161-tính-năng-và-khả-năng-của-hệ-thống-data-warehouse)
    - [1.6.2. Khả năng triển khai và quản lý](#162-khả-năng-triển-khai-và-quản-lý)
    - [1.6.3. Độ dễ sử dụng và kỹ năng cần thiết](#163-độ-dễ-sử-dụng-và-kỹ-năng-cần-thiết)
    - [1.6.4. Chất lượng hỗ trợ](#164-chất-lượng-hỗ-trợ)
    - [1.6.5. Chi phí tổng thể (TCO - Total Cost of Ownership)](#165-chi-phí-tổng-thể-tco---total-cost-of-ownership)
    - [1.6.6. Example](#166-example)
- [2. Data Marts](#2-data-marts)
  - [2.1. What is Data Marts?](#21-what-is-data-marts)
  - [2.2. Purpose of Data Marts](#22-purpose-of-data-marts)
  - [2.3. Data Mart Category](#23-data-mart-category)
  - [2.4. Data Pipeline for Data Marts](#24-data-pipeline-for-data-marts)
- [3. IBM Db2 Data Warehouse](#3-ibm-db2-data-warehouse)
  - [3.1. What is IBM Data Warehouse?](#31-what-is-ibm-data-warehouse)
  - [3.2. Features](#32-features)


# 1. Data Warehouses

## 1.1. What is Data Warehouses

Kho dữ liệu là một hệ thống tập hợp dữ liệu từ một hoặc nhiều nguồn vào một kho dữ liệu trung tâm, đồng nhất để hỗ trợ các yêu cầu phân tích dữ liệu khác nhau. Hãy cùng tìm hiểu sâu hơn về phân tích kho dữ liệu.

Hệ thống kho dữ liệu hỗ trợ khai thác dữ liệu, bao gồm ứng dụng trí tuệ nhân tạo (AI) và học máy (machine learning). Quá trình chuyển đổi dữ liệu trong quá trình ETL (Extract, Transform, Load) giúp tăng tốc độ báo cáo phía trước, cung cấp thông tin quan trọng nhanh chóng. Kho dữ liệu cho phép xử lý phân tích trực tuyến (OLAP), cung cấp phân tích dữ liệu đa chiều, linh hoạt và nhanh chóng cho các ứng dụng hỗ trợ quyết định và thông tin kinh doanh.

## 1.2. History and Development of Data Warehouse

Truyền thống, các kho dữ liệu được lưu trữ tại chỗ trong các trung tâm dữ liệu doanh nghiệp, ban đầu trên các máy chính và sau đó trên các hệ thống Unix, Windows và Linux. Các thiết bị kho dữ liệu xuất hiện với sự gia tăng khối lượng dữ liệu lớn vào những năm 2000. Những thiết bị này bao gồm một gói phần cứng chuyên biệt và phần mềm kho dữ liệu được tối ưu hóa, giúp giảm chi phí quản lý kho dữ liệu quy mô lớn.

Trong thập kỷ qua, với lượng dữ liệu khổng lồ được tạo ra và lưu trữ trên đám mây, các Kho Dữ Liệu Đám Mây (Cloud Data Warehouses - CDWs) đã trở nên phổ biến, nơi các tổ chức không mua phần cứng hoặc cài đặt phần mềm kho dữ liệu. Thay vào đó, các tổ chức truy cập kho dữ liệu như một dịch vụ có thể mở rộng, trả tiền theo mức sử dụng.

## 1.3. Data Warehouses Use Cases

**Thương Mại và E-commerce:** Các tổ chức thương mại và e-commerce sử dụng kho dữ liệu để phân tích và báo cáo hiệu suất bán hàng. Các tổ chức này cũng áp dụng mua sắm hỗ trợ bằng học máy, cung cấp cho người tiêu dùng các gợi ý phù hợp để thúc đẩy doanh số bán hàng thêm.

**Y Tế:** Bằng cách áp dụng trí tuệ nhân tạo vào dữ liệu bệnh nhân, các nhà cung cấp dịch vụ chăm sóc sức khỏe có thể truy cập các thông tin mới nhất và sử dụng thông tin đó để chẩn đoán và điều trị bệnh nhân với độ chính xác cao hơn.

**Giao Thông Vận Tải:** Các khả năng BI cho phép các nhà cung cấp giao thông vận tải tối ưu hóa lộ trình, thời gian di chuyển, nhu cầu thiết bị và yêu cầu nhân lực.

**Ngân Hàng và Fintech:** Các tổ chức fintech, bao gồm ngân hàng, áp dụng phân tích dữ liệu để đánh giá rủi ro, phát hiện gian lận và bán chéo dịch vụ.

**Mạng Xã Hội:** Các tổ chức mạng xã hội cần khả năng phân tích có thể đo lường nhanh chóng cảm xúc của khách hàng đang thay đổi và dự đoán doanh số sản phẩm.

**Chính Phủ:** Chính phủ áp dụng trí tuệ kinh doanh để phân tích và đánh giá các chương trình tập trung vào công dân và hỗ trợ các quyết định thay đổi chính sách.

## 1.4. Benefit of Using Data Warehouses

Kho dữ liệu cho phép các tổ chức tập trung dữ liệu từ các nguồn dữ liệu khác nhau, chẳng hạn như hệ thống giao dịch, cơ sở dữ liệu hoạt động và các tệp dữ liệu. Tích hợp dữ liệu, loại bỏ dữ liệu sai, loại bỏ trùng lặp và chuẩn hóa dữ liệu tạo ra một nguồn dữ liệu duy nhất, làm tăng chất lượng dữ liệu để phân tích. Một nguồn dữ liệu duy nhất cho phép người dùng tận dụng toàn bộ dữ liệu của công ty và truy cập dữ liệu đó hiệu quả hơn.

Ngoài ra, việc tách biệt các hoạt động cơ sở dữ liệu khỏi phân tích dữ liệu thường cải thiện hiệu suất truy cập dữ liệu, dẫn đến thông tin kinh doanh nhanh hơn. Các chức năng BI quy mô lớn như khai thác dữ liệu, trí tuệ nhân tạo và công cụ học máy hỗ trợ quyết định thông minh hơn bởi các chuyên gia dữ liệu và lãnh đạo doanh nghiệp. Những khả năng này xây dựng dựa trên nhau để cung cấp cho các tổ chức cơ hội và phương tiện để đạt được lợi thế cạnh tranh.

## 1.5. Population Data Warehouse Systems

Hầu hết các hệ thống Data Warehouse hiện nay được hỗ trợ thông qua ba nền tảng chính:

- **Thiết bị (appliance)**: Bao gồm phần cứng và phần mềm đã được tích hợp sẵn, cung cấp hiệu suất cao và giảm chi phí bảo trì.
- **Cloud**: Các nhà cung cấp chỉ hỗ trợ triển khai trên nền tảng đám mây, mang lại lợi ích về khả năng mở rộng và tính kinh tế dựa trên mô hình "pay-per-use" (trả theo nhu cầu).
- **On-premises**: Một số hệ thống Data Warehouse vẫn có thể được cài đặt tại môi trường nội bộ của tổ chức, nhưng hiện nay đa số nhà cung cấp cũng cung cấp cả giải pháp triển khai trên đám mây.

### 1.5.1. Data Warehouse Application

**Oracle Exadata**: Đây là hệ thống Data Warehouse được triển khai dưới dạng cài đặt nội bộ hoặc thông qua Oracle Public Cloud. Nó hỗ trợ nhiều loại tải công việc, bao gồm OLTP (xử lý giao dịch trực tuyến), phân tích dữ liệu, và phân tích dữ liệu trong bộ nhớ.

**IBM Netezza**: Có thể được triển khai trên IBM Cloud, Amazon Web Services, Microsoft Azure, hoặc các đám mây riêng tư. Netezza được biết đến với khả năng hỗ trợ khoa học dữ liệu và máy học.

### 1.5.2. Data Warehouse Cloud

- Amazon Redshift: Sử dụng phần cứng và phần mềm đặc thù của AWS để cung cấp tốc độ nén dữ liệu nhanh chóng, mã hóa, và tối ưu hóa thuật toán đồ thị. Nó tự động sắp xếp và lưu trữ dữ liệu theo cách tối ưu.

- Snowflake: Cung cấp giải pháp phân tích đa đám mây, tuân thủ các quy định bảo mật như GDPR và CCPA. Snowflake nổi bật với khả năng mã hóa liên tục cả khi dữ liệu đang di chuyển và khi lưu trữ.

- Google BigQuery: Được mô tả là giải pháp Data Warehouse "linh hoạt, đa đám mây", BigQuery cung cấp tốc độ truy vấn nhanh dưới một giây và khả năng phân tích thời gian thực với lượng dữ liệu khổng lồ (petabyte).

### 1.5.3. Data Warehouse supports both of Cloud and On-premesis

**Microsoft Azure Synapse Analytics**: Cung cấp quá trình ETL/ELT trực quan không cần mã với hơn 95 đầu nối gốc, hỗ trợ các trường hợp sử dụng cả Data Lake và Data Warehouse. Azure Synapse cũng hỗ trợ nhiều ngôn ngữ lập trình như T-SQL, Python, Scala, Spark SQL, và .NET.

**Teradata Vantage**: Kết hợp các công nghệ mã nguồn mở và thương mại để mang lại khả năng phân tích doanh nghiệp, hỗ trợ nhiều loại dữ liệu và nguồn dữ liệu mới. Teradata cung cấp các dịch vụ vận hành toàn diện như theo dõi, tối ưu hóa hiệu suất và quản lý bảo mật.

**IBM Db2 Warehouse**: Được biết đến với khả năng mở rộng, xử lý song song mạnh mẽ và tốc độ nhanh (petaflop), cũng như tính năng bảo mật và khả năng hoạt động ổn định với 99.99% thời gian hoạt động.

### 1.5.4. Example

**Ví dụ 1**: Amazon Redshift và Snowflake trong E-commerce Một doanh nghiệp thương mại điện tử lớn như Amazon có thể sử dụng Amazon Redshift để phân tích hành vi mua sắm của khách hàng từ hàng triệu giao dịch mỗi ngày. Đồng thời, Snowflake giúp các doanh nghiệp khác như Shopify thực hiện các phân tích đa đám mây, bảo mật dữ liệu khách hàng, và tuân thủ các quy định quốc tế.

**Ví dụ 2**: Google BigQuery trong phân tích thời gian thực Google BigQuery có thể giúp một công ty quảng cáo phân tích dữ liệu từ các chiến dịch quảng cáo hàng ngày. Với khả năng phân tích hàng petabyte dữ liệu chỉ trong vài giây, doanh nghiệp có thể điều chỉnh chiến dịch quảng cáo của mình theo thời gian thực để đạt hiệu quả tốt hơn.

## 1.6. Selecting Data Warehouse Systems

Khi lựa chọn hệ thống Data Warehouse, doanh nghiệp cần cân nhắc các tiêu chí chính sau đây:

- **Tính năng và khả năng**: Các tính năng liên quan đến vị trí, kiến trúc, khả năng mở rộng, loại dữ liệu hỗ trợ và khả năng phân tích dữ liệu.
- **Khả năng tương thích và triển khai**: Liệu hệ thống có hỗ trợ các quy trình quản lý, di chuyển, và chuyển đổi dữ liệu một cách dễ dàng hay không.
- **Độ dễ sử dụng và yêu cầu kỹ năng**: Nhân viên của tổ chức có đủ kỹ năng để triển khai và vận hành hệ thống không?
- **Chất lượng hỗ trợ**: Hỗ trợ từ nhà cung cấp có đủ đáp ứng yêu cầu về bảo mật, hiệu suất, và các kênh hỗ trợ không?
- **Chi phí tổng thể**: Bao gồm các chi phí hạ tầng, giấy phép phần mềm, di chuyển dữ liệu, quản lý và duy trì hệ thống.

### 1.6.1. Tính năng và khả năng của hệ thống Data Warehouse

**Vị trí**: Hệ thống có thể tồn tại dưới dạng on-premises, thiết bị chuyên dụng (appliance), hoặc trên một hay nhiều đám mây. Việc chọn vị trí phụ thuộc vào yêu cầu về bảo mật dữ liệu và tính riêng tư, ví dụ như tuân thủ CCPA hoặc GDPR.

**Kiến trúc và cấu trúc**: Doanh nghiệp cần xác định liệu họ sẵn sàng gắn kết với kiến trúc của một nhà cung cấp cụ thể hay không, hoặc liệu họ cần hệ thống đa đám mây. Khả năng mở rộng và hỗ trợ nhiều loại dữ liệu như dữ liệu bán cấu trúc và không cấu trúc cũng rất quan trọng.

**Khả năng hỗ trợ Big Data**: Hệ thống cần hỗ trợ cả dữ liệu theo lô (batch) và dữ liệu trực tuyến (streaming) nếu doanh nghiệp làm việc với dữ liệu lớn.

### 1.6.2. Khả năng triển khai và quản lý

**Quản trị dữ liệu**: Khả năng thực hiện quản trị dữ liệu hiệu quả là điều cần thiết. Hệ thống cũng cần có khả năng tối ưu hóa và điều chỉnh lại hiệu suất khi nhu cầu thay đổi.

**Quản lý người dùng**: Với xu hướng áp dụng chính sách "zero-trust", các tổ chức cần triển khai chương trình quản lý và xác thực người dùng để bảo vệ dữ liệu khỏi các rủi ro bảo mật.

### 1.6.3. Độ dễ sử dụng và kỹ năng cần thiết

**Kỹ năng nhân sự**: Doanh nghiệp cần đánh giá xem nhân viên của họ có đủ kỹ năng để triển khai và vận hành hệ thống mới không. Nếu không, liệu họ có thể nhanh chóng học hỏi các kỹ năng cần thiết hay không.

**Đối tác triển khai**: Đối tác triển khai có kinh nghiệm sẽ giúp đảm bảo quá trình tích hợp diễn ra thuận lợi, đặc biệt đối với các hệ thống lớn và phức tạp.

### 1.6.4. Chất lượng hỗ trợ

**Hỗ trợ từ nhà cung cấp**: Việc lựa chọn một nhà cung cấp duy nhất có thể giảm bớt thời gian và chi phí, vì họ có trách nhiệm toàn bộ với hệ thống. Tổ chức cần kiểm tra kỹ các điều khoản về dịch vụ, bao gồm thời gian hoạt động, bảo mật, và khả năng mở rộng.

**Kênh hỗ trợ**: Các kênh hỗ trợ phổ biến bao gồm điện thoại, email, chat, và tin nhắn. Ngoài ra, hệ thống có cung cấp các giải pháp tự phục vụ và cộng đồng người dùng phong phú hay không cũng là một yếu tố quan trọng.

### 1.6.5. Chi phí tổng thể (TCO - Total Cost of Ownership)

**Chi phí hạ tầng**: Bao gồm chi phí tính toán và lưu trữ, bất kể hệ thống được triển khai on-premises hay trên đám mây.

**Giấy phép phần mềm và chi phí sử dụng**: Đối với các giải pháp đám mây, chi phí có thể bao gồm đăng ký hoặc sử dụng dựa trên tài nguyên.

**Chi phí di chuyển dữ liệu**: Việc di chuyển dữ liệu vào hệ thống Data Warehouse mới có thể đòi hỏi chi phí cho việc tích hợp, cắt giảm dữ liệu thừa và quản lý dữ liệu.

**Chi phí quản trị**: Bao gồm chi phí nhân lực để quản lý và đào tạo nhân viên về hệ thống mới.

**Chi phí hỗ trợ và bảo trì**: Các khoản chi phí định kỳ để duy trì dịch vụ và hỗ trợ từ nhà cung cấp.

### 1.6.6. Example

**Ví dụ 1**: Chọn Data Warehouse dựa trên yêu cầu bảo mật Một tổ chức tài chính lớn có yêu cầu nghiêm ngặt về bảo mật và tuân thủ quy định. Do đó, họ quyết định triển khai hệ thống Data Warehouse on-premises để kiểm soát hoàn toàn dữ liệu và đáp ứng các quy định quốc gia về bảo mật như GDPR.

**Ví dụ 2**: Hệ thống Data Warehouse trên đám mây cho công ty khởi nghiệp Ngược lại, một công ty khởi nghiệp công nghệ với nguồn tài chính hạn chế có thể chọn giải pháp Data Warehouse đám mây như Amazon Redshift để tận dụng khả năng mở rộng linh hoạt và chỉ phải trả cho những tài nguyên họ sử dụng.

# 2. Data Marts

## 2.1. What is Data Marts?

Data mart là một `phần biệt lập của enterprise data warehouse (EDW)`, được thiết kế để `phục vụ một chức năng`, `mục đích cụ thể `hoặc một `nhóm người dùng trong doanh nghiệp`. Ví dụ, phòng kinh doanh và tài chính của công ty có thể có các data marts riêng để thu thập dữ liệu cần thiết cho các báo cáo doanh thu hàng quý. Tương tự, bộ phận marketing có thể sử dụng data marts để phân tích hành vi khách hàng, trong khi các bộ phận như vận chuyển, sản xuất hoặc bảo hành có thể có data marts riêng của họ.

**Ví dụ**: Một công ty sản xuất có thể có một data mart dành riêng cho phòng tài chính, nơi lưu trữ dữ liệu về chi phí, lợi nhuận và doanh thu. Data mart này giúp bộ phận tài chính có thể truy xuất nhanh chóng và dễ dàng các báo cáo liên quan đến tình hình kinh doanh của công ty mà không cần truy cập vào kho dữ liệu tổng thể lớn hơn.

## 2.2. Purpose of Data Marts

Mục đích chính của data marts là cung cấp dữ liệu tập trung và hỗ trợ đưa ra các quyết định chiến thuật. Data marts thường chỉ tập trung vào các dữ liệu liên quan nhất, giúp người dùng tiết kiệm thời gian tìm kiếm trong kho dữ liệu rộng lớn.

`Cấu trúc của data mart` thường là một `cơ sở dữ liệu quan hệ với sơ đồ dạng sao` (star schema) hoặc `bông tuyết` (snowflake schema). Trong đó:

- Bảng thực tế (fact table) lưu trữ các chỉ số kinh doanh quan trọng.
- Bảng chiều (dimension table) cung cấp ngữ cảnh cho các chỉ số đó, ví dụ như thời gian, khu vực địa lý, hoặc sản phẩm.

## 2.3. Data Mart Category

Có ba loại data mart chính, dựa trên mối quan hệ của chúng với data warehouse:

- **Data Mart Phụ thuộc (Dependent Data Mart)**: Lấy dữ liệu từ kho dữ liệu doanh nghiệp (EDW). Loại này thừa hưởng các quy tắc bảo mật và tính năng đã được thiết lập sẵn từ EDW.

- **Data Mart Độc lập (Independent Data Mart)**: Không phụ thuộc vào EDW mà trực tiếp lấy dữ liệu từ các hệ thống vận hành nội bộ hoặc từ các nguồn bên ngoài. Các data marts này cần pipeline ETL riêng để xử lý, chuyển đổi và tích hợp dữ liệu.

- **Data Mart Lai (Hybrid Data Mart)**: Kết hợp giữa data warehouse và các nguồn dữ liệu khác (nội bộ hoặc bên ngoài).

## 2.4. Data Pipeline for Data Marts

Để `tải dữ liệu vào một data mart`, các doanh nghiệp sử dụng quy trình `ETL (Extract, Transform, Load)`:

- Extract: Trích xuất dữ liệu từ các nguồn khác nhau.
- Transform: Chuyển đổi và làm sạch dữ liệu, loại bỏ thông tin không chính xác hoặc không phù hợp.
- Load: Tải dữ liệu đã làm sạch vào data mart để phục vụ các truy vấn phân tích.

**Ví dụ thực tế**: Một công ty bán lẻ có thể sử dụng ETL pipeline để trích xuất dữ liệu bán hàng từ các cửa hàng, làm sạch và tổ chức lại dữ liệu, sau đó tải dữ liệu vào data mart để phòng kinh doanh có thể phân tích xu hướng doanh số.

# 3. IBM Db2 Data Warehouse

## 3.1. What is IBM Data Warehouse?

**IBM Db2 Warehouse** là một giải pháp kho dữ liệu hoàn chỉnh, cung cấp mức độ kiểm soát cao đối với dữ liệu và ứng dụng của bạn. Nó hỗ trợ `triển khai dễ dàng trong môi trường container hóa như Docker` và cực kỳ linh hoạt cho các môi trường quản lý bởi khách hàng `(on-premises), đám mây (cloud), và môi trường lai (hybrid)`.

Db2 Warehouse sử dụng công nghệ `Massively Parallel Processing (MPP)` giúp tự động mở rộng quy mô và hỗ trợ các triển khai container. Điều này giúp các hệ thống có khả năng xử lý khối lượng lớn truy vấn phức tạp một cách nhanh chóng và hiệu quả.

Một điểm nổi bật của Db2 Warehouse là `tích hợp sẵn các thuật toán máy học` và khả năng phân tích nghiệp vụ trong cơ sở dữ liệu để tối ưu tốc độ.

## 3.2. Features

**Tự động tạo lược đồ dữ liệu**: Db2 Warehouse có khả năng tự động tạo lược đồ dữ liệu và chuyển đổi dữ liệu không có cấu trúc thành dạng có cấu trúc để dễ dàng phân tích.

**Tăng tốc truy vấn bằng BLU Acceleration**: Sử dụng các phương pháp tối ưu như xử lý SQL theo cột trong bộ nhớ (in-memory columnar processing) và data-skipping (bỏ qua dữ liệu không cần thiết), Db2 Warehouse đẩy nhanh quá trình truy vấn dữ liệu.

**Dashboard theo dõi hiệu suất**: Cung cấp các widget giám sát hiệu suất hệ thống, bao gồm các cảnh báo về phần cứng, phần mềm và lưu trữ. Người dùng có thể xem chi tiết về thời gian thực hiện truy vấn SQL, trạng thái chờ khóa, và nhiều thông tin khác liên quan đến sự kiện cảnh báo cơ sở dữ liệu.

