
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
