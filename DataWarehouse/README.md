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
  - [3.3. Application of IBM Db2 Warehouse](#33-application-of-ibm-db2-warehouse)
  - [3.4. Support Tool and Library](#34-support-tool-and-library)
- [4. Data Lake](#4-data-lake)
  - [4.1. What is Data Lake?](#41-what-is-data-lake)
  - [4.2. Benefit ot Data Lake](#42-benefit-ot-data-lake)
  - [4.3. Data Lake Application](#43-data-lake-application)
  - [4.4. Difference of Data Lake and Data Warehouse](#44-difference-of-data-lake-and-data-warehouse)
- [5. Data Lake Explained](#5-data-lake-explained)
  - [5.1. Scenerio](#51-scenerio)
  - [5.2. Related with Data](#52-related-with-data)
  - [5.3. What is Data Lake?](#53-what-is-data-lake)
  - [5.4. What is Data Warehouse?](#54-what-is-data-warehouse)
  - [5.5. Challenge of Data Lake and Data Warehouse](#55-challenge-of-data-lake-and-data-warehouse)
  - [5.6. Data LakeHouse](#56-data-lakehouse)
- [6. Data Warehouse Architecture](#6-data-warehouse-architecture)
  - [6.1. Layers of Data Warehouse Architecture](#61-layers-of-data-warehouse-architecture)
  - [6.2. Security in Data Warehouse](#62-security-in-data-warehouse)
  - [6.3. Reference Architecture of IBM](#63-reference-architecture-of-ibm)
  - [6.4. Support Application from IBM](#64-support-application-from-ibm)
- [7. Cubes, Rollups, and Materialzed Views and Tables](#7-cubes-rollups-and-materialzed-views-and-tables)
  - [7.1. What is Data Cube?](#71-what-is-data-cube)
  - [7.2. Data Cube Operation](#72-data-cube-operation)
    - [7.2.1. Slicing](#721-slicing)
    - [7.2.2. Dicing](#722-dicing)
    - [7.2.3. Drilling Up or Down](#723-drilling-up-or-down)
    - [7.2.4. Pivoting](#724-pivoting)
    - [7.2.5. Rolling Up](#725-rolling-up)
  - [7.3. Materialized Views](#73-materialized-views)
    - [7.3.1. Creation Materialized View](#731-creation-materialized-view)
- [8. Grouping Sets in SQL](#8-grouping-sets-in-sql)
  - [8.1. SQL GROUP BY CLAUSE](#81-sql-group-by-clause)
  - [8.2. Examples](#82-examples)
    - [8.2.1. Example 1](#821-example-1)
    - [8.2.2. Example 2](#822-example-2)
- [9. Facts and Dimensional Modeling](#9-facts-and-dimensional-modeling)
  - [9.1. Facts](#91-facts)
  - [9.2. Fact Table](#92-fact-table)
  - [9.3. Dimensions](#93-dimensions)
  - [9.4. Dimension Table](#94-dimension-table)
  - [9.5 Example of Data Modeling](#95-example-of-data-modeling)
  - [9.6. Summary](#96-summary)
  - [9.7 Hands-on Lab](#97-hands-on-lab)
    - [9.7.1. Exercise 1: Study the schema of the given csv file](#971-exercise-1-study-the-schema-of-the-given-csv-file)
    - [9.7.2. Exercise 2: Design the fact tables](#972-exercise-2-design-the-fact-tables)
    - [9.7.3. Exercise 3: Design the dimension tables](#973-exercise-3-design-the-dimension-tables)
    - [9.7.4. Exercise 4: Create a star schema using the fact and dimension tables](#974-exercise-4-create-a-star-schema-using-the-fact-and-dimension-tables)
    - [9.7.5. Exercise 5: Create the schema on the data warehouse](#975-exercise-5-create-the-schema-on-the-data-warehouse)
    - [9.7.6. Practice Exercises](#976-practice-exercises)
- [10. Data Modeling with Star and Snowflake Schemas](#10-data-modeling-with-star-and-snowflake-schemas)
  - [10.1. What is Star Schema](#101-what-is-star-schema)
  - [10.2. What is Snowflake Schema?](#102-what-is-snowflake-schema)
  - [10.3. Design a Star Schema](#103-design-a-star-schema)
  - [10.4. Expand from Star Schema to Snowflake Schema](#104-expand-from-star-schema-to-snowflake-schema)
  - [10.5. Summary](#105-summary)
- [11. Data Warehousing with Star and Snowflake schemas](#11-data-warehousing-with-star-and-snowflake-schemas)
  - [11.1. Why do we use these schemas, and how do they differ?](#111-why-do-we-use-these-schemas-and-how-do-they-differ)
  - [11.2. Normalization reduces redundancy](#112-normalization-reduces-redundancy)
  - [11.3. Normalization reduces data size](#113-normalization-reduces-data-size)
  - [11.4. Comparing benefits: snowflake vs. star data warehouses](#114-comparing-benefits-snowflake-vs-star-data-warehouses)
  - [11.5. Practical differences](#115-practical-differences)
  - [11.6. Too much of a good thing?](#116-too-much-of-a-good-thing)
- [12. Staging Areas for Data Warehouses](#12-staging-areas-for-data-warehouses)
  - [12.1. What is Staging Areas in Data Warehouse?](#121-what-is-staging-areas-in-data-warehouse)
  - [12.2. Data Warehouse Architecture with Staging Area](#122-data-warehouse-architecture-with-staging-area)
  - [12.3. Main functions of Staging Area](#123-main-functions-of-staging-area)
  - [12.4. Benefit of Staging Area](#124-benefit-of-staging-area)
  - [12.5. Summary](#125-summary)
  - [12.6. Hands-on Lab: Setting up a staging area](#126-hands-on-lab-setting-up-a-staging-area)
- [13. Verify Data Quality](#13-verify-data-quality)
  - [13.1. What is Data Quality Verification?](#131-what-is-data-quality-verification)
  - [13.2. Why we need to verify data quality?](#132-why-we-need-to-verify-data-quality)
  - [13.3. Error Data Processing](#133-error-data-processing)
  - [13.4. Tools](#134-tools)
  - [13.5. Summary](#135-summary)
  - [13.6. Hands-on Lab: Verifying Data Quality for a Data Warehouse](#136-hands-on-lab-verifying-data-quality-for-a-data-warehouse)
- [14. Populating a Data Warehouse](#14-populating-a-data-warehouse)
  - [14.1. Loading Frequency](#141-loading-frequency)
  - [14.2. Incremental Load and Change Detection](#142-incremental-load-and-change-detection)
  - [14.3. Data Warehouse Periodic Maintenance](#143-data-warehouse-periodic-maintenance)
  - [14.4. Example Populating Data](#144-example-populating-data)
  - [14.5. Summary](#145-summary)
  - [14.6. Hands-on](#146-hands-on)
- [15. Querying the Data](#15-querying-the-data)
  - [15.1. Scenario](#151-scenario)
  - [15.2. ShinyAutoSales - ERD](#152-shinyautosales---erd)
  - [15.3. View the tables](#153-view-the-tables)
  - [15.4. Denormalized View](#154-denormalized-view)
  - [15.5. Applying CUBE and ROLLUP to the materialized view](#155-applying-cube-and-rollup-to-the-materialized-view)
  - [15.6. Hands-on](#156-hands-on)
- [16. Practice Project](#16-practice-project)
  - [16.1. Scenario](#161-scenario)
  - [16.2. Instruction](#162-instruction)
  - [16.3. Go to project](#163-go-to-project)


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

## 3.3. Application of IBM Db2 Warehouse

Db2 Warehouse rất phù hợp với các trường hợp sau:

- **Tính linh hoạt và khả năng mở rộng**: Phù hợp với các hệ thống cần tính mở rộng cao.
- **Triển khai trên đám mây, tại chỗ (on-premises), hoặc hybrid**: Hỗ trợ đa dạng các môi trường triển khai.
- **Tích hợp các nguồn dữ liệu rời rạc**: Hợp nhất và tích hợp các nguồn dữ liệu khác nhau.
- **Phát triển nhanh các sản phẩm phân tích theo dòng nghiệp vụ**: Tạo các data marts một cách nhanh chóng.
- **Quản lý dữ liệu nhạy cảm hoặc có tính pháp lý**: Hỗ trợ lưu trữ và quản lý dữ liệu quan trọng, nhạy cảm.
- **Lưu trữ dữ liệu có cấu trúc lâu năm**: Phù hợp cho các dữ liệu SQL cũ, không thường xuyên sử dụng.

## 3.4. Support Tool and Library

Db2 Warehouse tích hợp với nhiều ngôn ngữ và công cụ phổ biến như:

- `JDBC, Node.JS, Spring, Python, R, Go, Spark, và Microsoft Visual Studio.`
- `Apache Spark`: Hỗ trợ phân vùng và triển khai trên nhiều máy chủ để mở rộng phân tích dữ liệu.

**Ví dụ thực tế**: Bạn có thể triển khai các job Apache Spark qua các stored procedures để chạy trên Db2 Warehouse, giúp mở rộng khả năng phân tích.

    R Studio: Hỗ trợ phân tích, xử lý, mô hình hóa và trực quan hóa dữ liệu với Db2 Warehouse. Ví dụ, bạn có thể tạo một Docker image chứa RStudio cùng các gói và driver cần thiết để kết nối với Db2 Warehouse. Thậm chí, bạn có thể phát triển ứng dụng chạy mã R tích hợp với Db2 thông qua REST API.


Db2 Warehouse cũng cung cấp nhiều driver mã nguồn mở phổ biến trên GitHub, như thư viện `python-ibmdb`, cho phép kết nối Python với IBM Db2.

# 4. Data Lake

## 4.1. What is Data Lake?

Data Lake là một kho lưu trữ dữ liệu có khả năng lưu trữ một lượng lớn dữ liệu thuộc nhiều loại khác nhau như:

- Dữ liệu có cấu trúc (structured data), ví dụ như các bảng dữ liệu từ cơ sở dữ liệu quan hệ.
- Dữ liệu bán cấu trúc (semi-structured data), chẳng hạn như các file JSON hoặc XML.
- Dữ liệu phi cấu trúc (unstructured data), bao gồm văn bản, email, hình ảnh và video.

Điểm quan trọng của Data Lake là `dữ liệu được lưu trữ trực tiếp từ nguồn gốc` mà `không cần phải qua quá trình xử lý hoặc định nghĩa trước` về cấu trúc hay lược đồ (schema).

**Ví dụ thực tế**: `Google Drive` hoặc `Amazon S3` có thể được xem như các dạng đơn giản của Data Lake, nơi bạn lưu trữ nhiều loại file khác nhau mà không cần phải sắp xếp hay phân loại chi tiết từ ban đầu.

![example data lake](image/example_datalake.png)

## 4.2. Benefit ot Data Lake

Data Lake mang lại nhiều lợi ích quan trọng, đặc biệt là đối với các tổ chức có `khối lượng dữ liệu lớn` và `đa dạng`:

- **Lưu trữ linh hoạt**: Data Lake có thể lưu trữ mọi loại dữ liệu, từ có cấu trúc, bán cấu trúc đến phi cấu trúc, mà không cần phải chuyển đổi hay định nghĩa trước.
- **Khả năng mở rộng**: Bạn có thể mở rộng dung lượng lưu trữ từ terabyte đến petabyte dữ liệu mà không gặp khó khăn trong việc quản lý cấu trúc dữ liệu.
- **Tiết kiệm thời gian**: Không cần phải tạo lược đồ hay chuyển đổi dữ liệu trước khi tải vào Data Lake, giúp tiết kiệm thời gian và công sức cho tổ chức.
- **Tái sử dụng linh hoạt**: Dữ liệu được lưu trữ ở dạng thô, nguyên bản, do đó có thể dễ dàng sử dụng lại cho các mục đích phân tích khác nhau trong tương lai, bao gồm cả phân tích máy học và phân tích nâng cao.

## 4.3. Data Lake Application

Một trong những ứng dụng chính của Data Lake là làm `kho lưu trữ dữ liệu trung gian trước khi tải dữ liệu vào Data Warehouse hoặc Data Mart`. Bạn có thể lấy dữ liệu từ nhiều nguồn khác nhau, lưu trữ trong Data Lake, và sau đó chuyển đổi dữ liệu theo nhu cầu phân tích cụ thể.

**Ví dụ thực tế:** Trong một tổ chức lớn như Amazon, nơi có rất nhiều loại dữ liệu đến từ nhiều hệ thống khác nhau (giao dịch, thông tin khách hàng, logs hệ thống), họ sẽ dùng Data Lake để lưu trữ tất cả dữ liệu này dưới dạng thô. Sau đó, tùy vào các mục đích phân tích, dữ liệu mới được chuyển đổi và tải vào Data Warehouse để tạo các báo cáo cụ thể.

## 4.4. Difference of Data Lake and Data Warehouse

Data Lake và Data Warehouse có các điểm khác biệt cơ bản về cách lưu trữ và sử dụng dữ liệu:

- **Dữ liệu trong Data Lake**: `Được lưu trữ dưới dạng thô, chưa qua xử lý`. Dữ liệu này có thể chưa tuân theo bất kỳ quy chuẩn hay cấu trúc nào và chưa được kiểm duyệt.

- **Dữ liệu trong Data Warehouse**: `Đã được xử lý, chuẩn hóa và tuân thủ các tiêu chuẩn dữ liệu trước khi lưu trữ`. Điều này giúp việc truy vấn và phân tích dễ dàng hơn nhưng lại cần nhiều công đoạn chuẩn bị.

- **Cấu trúc dữ liệu (Schema)**: `Trong Data Lake, bạn không cần định nghĩa cấu trúc dữ liệu trước khi tải dữ liệu vào`. Điều này tạo sự linh hoạt khi lưu trữ các loại dữ liệu khác nhau.
    - Ngược lại, `Data Warehouse yêu cầu phải có cấu trúc và lược đồ dữ liệu rõ ràng trước khi dữ liệu được tải vào`.

- **Chất lượng dữ liệu**: Dữ liệu trong Data Lake có thể chưa được kiểm duyệt hoặc không tuân thủ quy trình quản lý dữ liệu (Data Governance). Trong khi đó, dữ liệu trong Data Warehouse luôn được kiểm tra, tuân thủ các quy chuẩn và đảm bảo chất lượng.

- **Người dùng**:
    - `Data Lake thường được sử dụng bởi các nhà khoa học dữ liệu` (Data Scientists), `nhà phát triển dữ liệu` (Data Developers), và `kỹ sư máy học` (Machine Learning Engineers) do tính linh hoạt và khả năng lưu trữ dữ liệu chưa qua xử lý của nó.
    - `Data Warehouse chủ yếu được dùng bởi các nhà phân tích kinh doanh` (Business Analysts) và `nhà phân tích dữ liệu `(Data Analysts) vì nó cung cấp dữ liệu đã qua xử lý, dễ dàng hơn cho việc tạo các báo cáo và phân tích trực tiếp.

# 5. Data Lake Explained

## 5.1. Scenerio

Trong một nhà bếp thương mại, có rất `nhiều khâu để biến nguyên liệu thô thành món ăn hoàn chỉnh`. Chúng ta có nguyên liệu được vận chuyển từ các nhà cung cấp và giao đến kho bãi của nhà hàng. `Các nguyên liệu được sắp xếp và bảo quản theo từng loại như kho khô cho thực phẩm khô hoặc tủ lạnh/tủ đông cho rau tươi và thịt`. Quy trình này `phải được tiến hành nhanh chóng để tránh lãng phí` và `đảm bảo an toàn thực phẩm`. `Nếu không` thực hiện đúng, các đầu bếp sẽ `mất nhiều thời gian tìm kiếm nguyên liệu` hơn là nấu nướng.

## 5.2. Related with Data

Bạn có thể đang tự hỏi: Điều này liên quan gì đến dữ liệu? Thực ra, quy trình tương tự này cũng tồn tại trong kiến trúc dữ liệu của các tổ chức. Hãy tưởng tượng rằng thay vì nguyên liệu thực phẩm, bạn có đủ loại dữ liệu đến từ nhiều nguồn khác nhau: từ các dịch vụ đám mây, ứng dụng hoạt động, đến dữ liệu từ mạng xã hội. Chúng ta luôn có dữ liệu mới liên tục được đưa vào tổ chức giống như việc nhà hàng luôn nhận nguyên liệu từ các nhà cung cấp.

Cũng giống như nhà hàng cần kho bãi để chứa nguyên liệu, trong thế giới dữ liệu, chúng ta cần nơi để chứa những dữ liệu thô này. Đó là lý do mà Data Lake (Hồ dữ liệu) xuất hiện.

## 5.3. What is Data Lake?

`Data Lake là một kho lưu trữ cho phép chúng ta thu thập nhanh chóng và ít tốn chi phí cả dữ liệu thô`, có thể là dữ liệu có cấu trúc, dữ liệu phi cấu trúc, và thậm chí là dữ liệu bán cấu trúc.

Tuy nhiên, `cũng giống như nhà hàng không nấu ăn ngay tại bến tải hàng`, chúng ta `không phân tích dữ liệu thô ngay tại Data Lake`. Dữ liệu `cần được tổ chức và chuyển đổi từ trạng thái thô thành một thứ có thể sử dụng được`. Đó là lúc chúng ta cần đến Enterprise Data Warehouse (EDW).

## 5.4. What is Data Warehouse?

`Data Warehouse là nơi dữ liệu được tối ưu hóa và tổ chức để phục vụ cho các nhiệm vụ phân tích cụ thể`. Dữ liệu có thể được chuyển từ Data Lake hoặc trực tiếp từ các nguồn dữ liệu khác vào Data Warehouse, sau đó được sử dụng cho các tác vụ như Business Intelligence (BI), xây dựng báo cáo và dashboard.

Dữ liệu trong Data Warehouse được làm sạch, tổ chức và quản lý chặt chẽ. `Nó giống như các kho lạnh trong nhà bếp`, nơi nguyên liệu được bảo quản kỹ lưỡng để luôn sẵn sàng cho đầu bếp sử dụng một cách an toàn và hiệu quả.

## 5.5. Challenge of Data Lake and Data Warehouse

Mặc dù `Data Lakes` cho phép lưu trữ dữ liệu lớn với chi phí thấp, nhưng nó có thể `gặp khó khăn về quản lý chất lượng và quản trị dữ liệu`. Đôi khi, `Data Lakes có thể trở thành một "data swamp" (đầm lầy dữ liệu)` với `nhiều dữ liệu trùng lặp`, `thiếu chính xác` hoặc `không đầy đủ`. Điều này làm cho việc phân tích trở nên khó khăn và dữ liệu dễ mất giá trị, tương tự như nguyên liệu thô bị hỏng nếu không được sử dụng kịp thời trong nhà bếp.

Mặt khác, `Data Warehouse cung cấp hiệu năng truy vấn vượt trội`, nhưng đi kèm với `chi phí cao`. Nó giống như việc vận hành các tủ lạnh lớn tốn kém và không thể chứa tất cả mọi thứ. Ngoài ra, Data Warehouse cũng có hạn chế về việc hỗ trợ dữ liệu bán cấu trúc và phi cấu trúc, vốn là những loại dữ liệu đang gia tăng nhanh chóng.

Một `điểm yếu khác của Data Warehouse` là đôi khi nó `chậm trong việc xử lý dữ liệu mới nhất` do quá trình làm sạch và nạp dữ liệu.

## 5.6. Data LakeHouse

Để giải quyết các vấn đề của Data Lake và Data Warehouse, các nhà phát triển đã kết hợp những gì tốt nhất từ cả hai mô hình và tạo ra công nghệ mới mang tên Data Lakehouse.

Data Lakehouse cho phép chúng ta lưu trữ dữ liệu từ những nguồn mới phát sinh với chi phí thấp, đồng thời tích hợp các tính năng quản lý và quản trị dữ liệu giống như Data Warehouse để hỗ trợ cả Business Intelligence và Machine Learning một cách nhanh chóng và hiệu quả.

Có nhiều cách để bắt đầu sử dụng Data Lakehouse. Bạn có thể:

- Hiện đại hóa hệ thống Data Lake hiện tại.
- Bổ sung cho Data Warehouse để hỗ trợ các ứng dụng AI và Machine Learning.

# 6. Data Warehouse Architecture

Chi tiết kiến trúc của một data warehouse phụ thuộc vào mục đích sử dụng của nền tảng. Các yêu cầu có thể bao gồm:

- Tạo báo cáo và dashboard.
- Phân tích dữ liệu khám phá.
- Tự động hóa và ứng dụng machine learning.
- Phân tích tự phục vụ (self-serve analytics).

Chúng ta sẽ bắt đầu bằng việc tìm hiểu mô hình kiến trúc tổng quan của Enterprise Data Warehouse (EDW) – một nền tảng mà các công ty có thể điều chỉnh để phù hợp với nhu cầu phân tích của họ.

## 6.1. Layers of Data Warehouse Architecture

Trong kiến trúc này, chúng ta có các tầng hoặc thành phần chính, bao gồm:

- **Nguồn dữ liệu (Data Sources)**: Các nguồn dữ liệu có thể bao gồm tệp phẳng (flat files), cơ sở dữ liệu, và các hệ thống vận hành hiện có.

- **Tầng ETL (Extract, Transform, Load)**: Được sử dụng để trích xuất, chuyển đổi, và tải dữ liệu vào hệ thống.

- **Khu vực staging và sandbox (tùy chọn)**: Các khu vực này dùng để giữ dữ liệu và phát triển workflows trước khi dữ liệu được nạp vào kho.

- **Kho dữ liệu doanh nghiệp (Enterprise Data Warehouse Repository)**: Đây là nơi lưu trữ dữ liệu đã được tổ chức và tối ưu hóa.

- **Data Marts (tùy chọn)**: Được sử dụng khi có nhiều data marts, kiến trúc này thường được gọi là `mô hình "hub and spoke"`.

- **Tầng phân tích và công cụ BI (Analytics Layer & BI Tools)**: Đây là các công cụ phân tích và tình báo kinh doanh giúp tạo ra báo cáo, dashboard, và phân tích dữ liệu.

![example EDW architecture](image/example_EDW_architecture.png)

## 6.2. Security in Data Warehouse

Data Warehouse phải đảm bảo an ninh dữ liệu cho mọi quá trình, từ khi dữ liệu được đưa vào đến khi dữ liệu được sử dụng bởi các người dùng khác nhau trong mạng lưới. Điều quan trọng là tính tương tác giữa các thành phần của hệ thống phải được đảm bảo.

Các nhà cung cấp giải pháp Enterprise Data Warehouse thường tạo ra các `kiến trúc tham chiếu (reference architecture)` và triển khai các giải pháp theo mô hình tổng quát, đã được kiểm nghiệm để đảm bảo tính tương thích giữa các thành phần.

## 6.3. Reference Architecture of IBM

Tiếp theo, chúng ta sẽ tìm hiểu về kiến trúc tham chiếu cho data warehouse của IBM. Trong mô hình này, mỗi tầng kiến trúc sẽ đảm nhiệm một chức năng cụ thể:

- **Tầng thu thập dữ liệu (Data Acquisition Layer)**:
    Thành phần này chịu trách nhiệm thu thập dữ liệu thô từ các hệ thống nguồn như bộ phận nhân sự, tài chính, và thanh toán.

- **Tầng tích hợp dữ liệu (Data Integration Layer)**:
    Đây là khu vực staging, nơi diễn ra các quá trình trích xuất, chuyển đổi, và tải dữ liệu vào kho lưu trữ. Nó cũng chứa các công cụ quản trị và siêu dữ liệu trung tâm (central metadata).

- **Tầng lưu trữ dữ liệu (Data Repository Layer)**:
    Dữ liệu đã được tích hợp sẽ được lưu trữ tại đây, thường dưới dạng mô hình quan hệ (relational model).

- **Tầng phân tích (Analytics Layer)**:
    Dữ liệu tại tầng này thường được lưu trữ dưới dạng khối (cube) để dễ dàng cho việc phân tích.

- **Tầng trình bày (Presentation Layer)**:
    Các ứng dụng tại tầng này cung cấp khả năng truy cập dữ liệu cho các nhóm người dùng khác nhau như chuyên viên phân tích marketing, người dùng, và đại lý. Dữ liệu có thể được tiêu thụ thông qua web pages và cổng thông tin hoặc qua các dịch vụ web (web services).

![Example of IBM reference architecrture](image/example_ibmreference_architecture.png)

## 6.4. Support Application from IBM

Kiến trúc tham chiếu của IBM được hỗ trợ và mở rộng thông qua các sản phẩm thuộc bộ IBM InfoSphere:

- **IBM InfoSphere DataStage**:
    Nền tảng ETL linh hoạt và có thể mở rộng, hỗ trợ tích hợp dữ liệu theo thời gian thực, cả trong môi trường on-premises và cloud.

- **IBM InfoSphere MetaData Workbench**:
    Công cụ này cung cấp khả năng theo dõi dòng dữ liệu (data flow reporting) và phân tích tác động (impact analysis), giúp dễ dàng chia sẻ, tìm kiếm và truy xuất thông tin.

- **IBM InfoSphere QualityStage**:
    Công cụ này hỗ trợ cải thiện chất lượng dữ liệu và quản trị thông tin. Nó giúp làm sạch và quản lý các dữ liệu như khách hàng, nhà cung cấp, địa điểm, và sản phẩm.

- **IBM Db2 Warehouse**:
    Dòng sản phẩm quản lý dữ liệu hiệu suất cao, hỗ trợ cả dữ liệu có cấu trúc và phi cấu trúc, hoạt động trong cả môi trường on-premises và cloud.

- **IBM Cognos Analytics**:
    Nền tảng business intelligence nâng cao, cho phép tạo báo cáo, scoreboards, dashboards, và phân tích dữ liệu khám phá.

# 7. Cubes, Rollups, and Materialzed Views and Tables

Chúng ta sẽ bắt đầu bằng cách minh họa khái niệm về data cube thông qua ví dụ cụ thể, sau đó đi vào các thao tác trên cube, và cuối cùng, tìm hiểu về materialized views.

## 7.1. What is Data Cube?

Một data cube là `cấu trúc dữ liệu được hình thành từ các dimension` (chiều) trong star schema. Mỗi dimension đại diện cho một khía cạnh của dữ liệu, ví dụ như sản phẩm, vị trí địa lý, hoặc năm bán hàng. Các ô trong cube chứa giá trị của một fact quan trọng, ví dụ như doanh thu.

Hãy xem xét ví dụ về một hệ thống OLAP (Online Analytical Processing) cho dữ liệu bán hàng. Giả sử ta có ba chiều:

- **Product category**: Các loại sản phẩm như "Áo phông", "Áo khoác",...
- **State/Province**: Bang hoặc tỉnh nơi sản phẩm được bán.
- **Year**: Năm sản phẩm được bán.

Mỗi ô của cube có thể chứa một giá trị như 243 (nghìn đô la), tương ứng với doanh thu bán hàng của một loại sản phẩm tại một bang cụ thể trong một năm nhất định.

![Example Data Cube](image/example_datacube.png)

## 7.2. Data Cube Operation

### 7.2.1. Slicing 

Là quá trình chọn một thành phần duy nhất từ một dimension để thu hẹp cube. Ví dụ, bạn có thể chọn chỉ năm 2018 từ dimension Year, cho phép bạn phân tích tổng doanh thu của tất cả các bang và sản phẩm chỉ trong năm đó.

![Example Data Slicing](image/example_dataslicing.png)

### 7.2.2. Dicing

Tương tự như slicing, nhưng bạn chọn một tập hợp con của các giá trị từ một dimension. Ví dụ, chọn chỉ các sản phẩm "Áo phông", "Áo khoác", và "Giày", giúp bạn thu hẹp phạm vi phân tích xuống các sản phẩm cụ thể.

![Example Data Dicing](image/example_datadicing.png)

### 7.2.3. Drilling Up or Down

Trong một số dimension, có thể có các `hierarchies` (cấp bậc) mà bạn có thể drill down vào để xem chi tiết hơn. Ví dụ, khi bạn drill down vào category "Áo phông", có thể bạn sẽ thấy các nhóm sản phẩm con như "Áo phông cổ tròn", "Áo phông cổ tim". Ngược lại, drill up sẽ đưa bạn trở lại mức tổng quát hơn.

![Example Data Drilling Up or Down](image/example_datadrilling.png)

### 7.2.4. Pivoting

Là quá trình xoay data cube để thay đổi góc nhìn. Ví dụ, thay vì phân tích theo năm trước tiên, bạn có thể xoay cube để phân tích theo sản phẩm trước, sau đó là bang.

![Example Data Pivoting](image/example_datapivoting.png)

### 7.2.5. Rolling Up

Là quá trình tóm tắt dữ liệu dọc theo một dimension. Bạn có thể tính tổng, đếm, hoặc tính trung bình. Ví dụ, tính trung bình doanh thu bán áo phông ở các bang bằng cách tổng hợp doanh thu của từng bang rồi chia cho số bang.

![Example Rolling Up](image/example_rollingup.png)

## 7.3. Materialized Views

Materialized view là một bản sao tĩnh của kết quả truy vấn, thường được sử dụng để giảm tải hệ thống bằng cách lưu trữ các kết quả truy vấn phức tạp hoặc dữ liệu tổng hợp. `Các đặc điểm quan trọng của materialized view` là:

- **Local, read-only copy**: Bản sao tĩnh chỉ dùng để đọc.
- **Query caching**: Được dùng để lưu trữ kết quả của các truy vấn tốn kém như các phép nối hoặc phép tính tổng hợp.

Các materialized views có thể được cài đặt với các tùy chọn làm mới khác nhau:

- **Never refresh**: Chỉ tạo dữ liệu khi view được tạo.
- **Refresh on demand**: Làm mới thủ công sau khi có thay đổi dữ liệu.
- **Scheduled refresh**: Làm mới theo lịch định kỳ, chẳng hạn như sau mỗi lần tải dữ liệu hàng ngày.
- **Immediate refresh**: Tự động làm mới sau mỗi thay đổi dữ liệu.

### 7.3.1. Creation Materialized View

**ORACLE**

```SQL
CREATE MATERIALIZED VIEW <My_Mat_View>
REFRESH FAST START WITH SYSDATE NEXT DAY
AS SELECT * FROM <My_Table>;
```

**PostgreSQL**

```SQL
CREATE MATERIALIZED VIEW <My_Mat_View>
[ WITH (storage_parameter [=value] [, ...]) ]
[ TABLESPACE <table_space_name> ]
AS SELECT * FROM <Table_Name>;
```

Trong `[]` nghĩa là tùy chọn

Và trong PostgreSQL ta có thể làm mới thủ công materialized view bằng

```SQL
REFRESH MATERIALIZED VIEW <My_Mat_View>;
```

**Db2**

Trong Db2, materialied view được gọi là MQTs (Materialized Query Tables)

```SQL
CREATE TABLE Emp_MQT AS
(SELECT empno, empname, deptname
 FROM Employee, Department
 WHERE Employee.dept_id = Department.dept_id)
DATA INITIALLY DEFERRED REFRESH IMMEDIATE;
```

Câu lệnh trên tạo ra một bảng Emp_MQT dựa trên dữ liệu từ hai bảng Employee và Department.

# 8. Grouping Sets in SQL

Mệnh đề `GROUPING SETS` được sử dụng cùng với mệnh đề `GROUP BY` để cho phép bạn dễ dàng tóm tắt dữ liệu bằng cách tổng hợp sự kiện theo bao nhiêu chiều (cột) tùy thích.  

## 8.1. SQL GROUP BY CLAUSE

Hãy nhớ lại rằng mệnh đề SQL GROUP BY cho phép bạn tóm tắt một tập hợp như SUM hoặc AVG trên các thành viên hoặc nhóm riêng biệt của một biến hoặc thứ nguyên phân loại. 

Bạn có thể mở rộng chức năng của mệnh đề `GROUP BY` bằng cách sử dụng các mệnh đề SQL như `CUBE` và `ROLLUP` để chọn nhiều chiều và tạo các bản tóm tắt đa chiều. Hai mệnh đề này cũng tạo ra tổng cộng, giống như báo cáo bạn có thể thấy trong ứng dụng bảng tính hoặc biểu định kiểu kế toán. Giống như `CUBE` và `ROLLUP`, mệnh đề `GROUPING SETS` trong SQL cho phép bạn tổng hợp dữ liệu theo nhiều chiều nhưng không tạo ra tổng cuối. 

## 8.2. Examples

Hãy bắt đầu với một ví dụ về tổng hợp GROUP BY thông thường và sau đó so sánh kết quả với kết quả sử dụng mệnh đề `GROUPING SETS`. Chúng tôi sẽ sử dụng dữ liệu từ một công ty hư cấu có tên là Shiny Auto Sales. Lược đồ kho hàng của công ty được hiển thị trong sơ đồ mối quan hệ thực thể trong Hình dưới đây:

![Shiny Auto Sales Schema](image/shiny_auto_sales_schema.png)

Chúng tôi sẽ làm việc với một chế độ xem được cụ thể hóa một cách thuận tiện về một bảng dữ kiện hoàn toàn không chuẩn hóa từ lược đồ sao bán hàng, được gọi là `DNsale`, trông giống như sau: 

![SELECT * FROM DNsales](image/selectfull.png)

Bảng `DNsale` này được tạo bằng cách nối tất cả các bảng thứ nguyên với bảng thực tế trung tâm và chỉ chọn các cột được hiển thị. Mỗi bản ghi trong `DNsale` chứa thông tin chi tiết về một giao dịch bán hàng riêng lẻ. 

### 8.2.1. Example 1

Hãy xem xét mã SQL sau đây gọi GROUP BY trên thứ nguyên loại ô tô để tóm tắt tổng doanh số bán ô tô mới theo loại ô tô. 

```SQL
SELECT 
    autoclassname,
    SUM(amount)
FROM
    DNsales
WHERE
    isNew=True
GROUP BY
    autoclassname
```

Kết quả trông như thế này: 

![Result of Group by and sum query](image/select_group_by.png)

### 8.2.2. Example 2

Bây giờ, giả sử bạn muốn tạo một chế độ xem tương tự, nhưng bạn cũng muốn bao gồm tổng doanh số bán hàng của nhân viên bán hàng. Bạn có thể sử dụng mệnh đề `GROUPING SETS` để truy cập vào cả thứ nguyên lớp ô tô và nhân viên bán hàng trong cùng một truy vấn. Đây là mã SQL bạn có thể sử dụng để tóm tắt tổng doanh số bán ô tô mới, theo cả loại ô tô và theo nhân viên bán hàng, tất cả chỉ trong một biểu thức: 

```SQL
SELECT
    autoclassname,
    salespersonname,
    SUM(amount)
FROM
    DNsales
WHERE
    isNew=True
GROUP BY
GROUPING SETS(autoclassname, salespersonname)
```

Đây là kết quả truy vấn. Lưu ý rằng bốn hàng đầu tiên giống hệt với kết quả của Ví dụ 1, trong khi 5 hàng tiếp theo là kết quả bạn sẽ nhận được bằng cách thay thế tên nhân viên bán hàng cho tên tự động phân loại trong Ví dụ 1. 

![Result of Group by + grouping set query](image/select_group_by_grouping_sets.png)

Về cơ bản, việc áp dụng `GROUPING SETS` cho hai thứ nguyên, `salespersonname` và `autoclassname` sẽ mang lại cùng một kết quả mà bạn sẽ nhận được bằng cách thêm hai kết quả riêng lẻ của việc áp dụng `GROUP BY` cho từng thứ nguyên riêng biệt như trong Ví dụ 1. 

# 9. Facts and Dimensional Modeling

## 9.1. Facts

Trong kho dữ liệu, dữ liệu thường được phân thành hai loại chính: Facts và Dimensions.

`Facts` là các giá trị có thể đo lường được, ví dụ như nhiệt độ, số lượng bán hàng, hoặc lượng mưa tính bằng milimét. Những giá trị này thường là định lượng nhưng cũng có thể là định tính, ví dụ như điều kiện thời tiết ("có mây rải rác").

**Ví dụ:**

- Nhiệt độ: "24°C".
- Doanh thu bán hàng: "1000 đô la".
- Lượng mưa: "5 mm".

## 9.2. Fact Table

`Fact Table` (Bảng Fact) là bảng lưu trữ các facts của một quy trình kinh doanh và chứa các khóa ngoại để liên kết với các bảng dimension. Bảng fact thường bao gồm các số liệu có thể cộng dồn được, như số tiền bán hàng.

- Fact Table có thể chứa các facts chi tiết, như giao dịch bán hàng từng đơn lẻ, hoặc facts đã được tổng hợp, như tổng doanh thu hàng ngày hoặc hàng tuần.

Ví dụ:

- Bảng Fact cho bán hàng có thể bao gồm các trường như:
    - **Sale Date**: Ngày bán hàng.
    - **Sale Amount**: Số tiền bán hàng.
    - **Sale ID**: Khóa chính.

`Bảng Fact cũng có thể chứa các khóa ngoại để liên kết với các bảng dimension.`

## 9.3. Dimensions

Dimensions (Chiều) là `các thuộc tính phân loại các facts`. Chúng cung cấp ngữ cảnh cho các facts, làm cho các facts trở nên có ý nghĩa hơn.

- Dimensions có thể là các biến phân loại như tên người, sản phẩm, địa điểm, hoặc thời gian.

**Ví dụ:**

- Dimension Table cho sản phẩm có thể bao gồm các trường:
    - Product ID: Khóa chính.
    - Product Name: Tên sản phẩm.
    - Product Category: Danh mục sản phẩm.
  
## 9.4. Dimension Table

Dimension Table (Bảng Dimension) `lưu trữ các dimension của một fact và được liên kết với bảng fact qua khóa ngoại.`

Ví dụ về Dimension Tables:

- **Product Table**: Mô tả các sản phẩm, bao gồm thông tin như tên sản phẩm, loại sản phẩm, màu sắc, và kích thước.
- **Employee Table**: Mô tả các nhân viên, bao gồm tên, chức danh, và phòng ban.
- **Temporal Table**: Mô tả thời gian với độ phân giải chi tiết, như ngày, tháng, năm.
- **Geography Table**: Mô tả địa điểm như quốc gia, bang, thành phố, và mã bưu điện.

![Example Dimension Table](image/example_dimensiontable.png)

## 9.5 Example of Data Modeling

Để làm rõ mối quan hệ giữa bảng fact và các bảng dimension, hãy xem xét ví dụ sau:

**Bài toán: Bán hàng tại đại lý ô tô**

![Example Schema Relation of Fact table and Dimension table](image/example_relation_fact_dimension_table.png)

- Fact Table: Bảng lưu trữ thông tin về các giao dịch bán hàng.
    - Sale Date: Ngày bán hàng.
    - Sale Amount: Số tiền bán hàng.
    - Sale ID: Khóa chính.

- Dimension Tables:

    - Vehicle Table: Mô tả các xe bán, bao gồm:
        - Vehicle ID: Khóa chính.
        - Make: Hãng xe.
        - Model: Mẫu xe.

    - Salesperson Table: Mô tả các nhân viên bán hàng, bao gồm:
        - Salesperson ID: Khóa chính.
        - First Name: Tên.
        - Last Name: Họ.

- Mối liên kết: Bảng Fact liên kết với các bảng Dimension thông qua khóa ngoại:
    - Vehicle ID trong bảng Fact liên kết với Vehicle ID trong bảng Vehicle.
    - Salesperson ID trong bảng Fact liên kết với Salesperson ID trong bảng Salesperson.

## 9.6. Summary

- `Facts và Dimensions` là hai loại dữ liệu chính trong kho dữ liệu.
- `Facts` thường là các số liệu đo lường quy trình kinh doanh, như số tiền bán hàng.
- `Dimensions` phân loại và cung cấp ngữ cảnh cho các facts, ví dụ như người bán, ngày bán, và cửa hàng.
- `Fact Table` chứa các facts và khóa ngoại liên kết với các bảng dimension.
- `Dimension Table` lưu trữ các thuộc tính phân loại và giúp làm rõ các facts.

## 9.7 Hands-on Lab

Lab được thiết kế để hướng dẫn bạn trong quá trình thiết kế kho dữ liệu cho nhà cung cấp dịch vụ đám mây. Nó tập trung vào việc sử dụng dữ liệu thanh toán được cung cấp trong tệp CSV để tạo lược đồ sao, bao gồm cả việc thiết kế các `Fact Tables` và `Dimensions`. Lược đồ này sẽ hỗ trợ các truy vấn phức tạp liên quan đến thanh toán, chẳng hạn như thanh toán trung bình cho mỗi khách hàng, thanh toán theo quốc gia, ngành và danh mục cũng như xu hướng theo thời gian.

### 9.7.1. Exercise 1: Study the schema of the given csv file

Trong lab này, ta sẽ thiết kế data warehouse cho một nhà cung cấp dịch vụ đám mây

Nhà cung cấp dịch vụ đám mây đã cung cấp cho chúng tôi dữ liệu thanh toán của họ trong tệp csv `cloud-billing-dataset.csv`. Tệp này chứa dữ liệu thanh toán trong thập kỷ qua.

File csv có các cột sau:

| Field Name | Details |
| ------------ | --------- |
| customerid | Id của khách hàng |
| category | Hạng mục khách hàng. Ví dụ: Cá nhân hoặc Công ty |
| country | Quốc gia của khách hàng |
| industry | Khách hàng thuộc lĩnh vực/ngành nào. Ví dụ: Pháp lý, Kỹ thuật |
| month | Tháng thanh toán, được lưu trữ dưới dạng YYYY-MM. Ví dụ: 2009-01 là tháng 1 năm 2009 |
| billedamount | Số tiền được tính bởi các dịch vụ đám mây được cung cấp trong tháng đó bằng USD |

Chúng ta cần thiết kế một kho dữ liệu có thể hỗ trợ các truy vấn được liệt kê bên dưới:


- average billing per customer: hóa đơn trung bình cho mỗi khách hàng
- billing by country: thanh toán theo quốc gia
- top 10 customers: 10 khách hàng hàng đầu
- top 10 countries: 10 quốc gia hàng đầu
- billing by industry: thanh toán theo ngành
- billing by category: thanh toán theo danh mục
- billing by year: thanh toán theo năm
- billing by month: thanh toán theo tháng
- billing by quarter: thanh toán theo quý
- average billing per industry per month: thanh toán trung bình mỗi ngành mỗi tháng
- average billing per industry per quarter: thanh toán trung bình cho mỗi ngành mỗi quý
- average billing per country per quarter: thanh toán trung bình cho mỗi quốc gia mỗi quý
- average billing per country per industry per quarter: thanh toán trung bình cho mỗi quốc gia cho mỗi ngành mỗi quý

Dưới đây là năm hàng được chọn ngẫu nhiên từ tệp csv.

![The head of csv file](image/head_csv_file.png)

### 9.7.2. Exercise 2: Design the fact tables

Fact trong dữ liệu này là hóa đơn được tạo hàng tháng. Các trường `customerid` và `billedamount` là những trường quan trọng trong bảng dữ kiện.

Chúng tôi cũng cần một cách để xác định thông tin khách hàng bổ sung, ngoài thông tin id và ngày. Vì vậy, chúng ta cần các trường tham chiếu đến thông tin khách hàng và ngày tháng trong các bảng khác.

Bảng fact cuối cùng cho bill sẽ trông như thế này:

| Field Name | Details |
| ------------ | --------- |
|billid|Khóa chính - Mã định danh duy nhất cho mỗi hóa đơn|
|customerid|Khóa ngoại - Id của khách hàng|
|monthid|Khóa ngoại - Id của tháng. Chúng tôi có thể giải quyết thông tin tháng thanh toán bằng cách này|
|billedamount|Số tiền được tính bởi các dịch vụ đám mây được cung cấp trong tháng đó bằng USD|

### 9.7.3. Exercise 3: Design the dimension tables

Chúng ta có 2 dimensions cho fact (ở đây là bill hàng tháng)

1. Customer information
2. Date information

Chúng ta hãy sắp xếp tất cả các trường cung cấp thông tin về khách hàng vào một dimension table.

| Field Name | Details |
| ------------ | --------- |
|customerid|Khóa chính - Id của khách hàng|
|category|Hạng mục khách hàng. Ví dụ: Cá nhân hoặc Công ty|
|country|Quốc gia của khách hàng|
|industry|Khách hàng thuộc lĩnh vực/ngành nào. Ví dụ: Pháp lý, Kỹ thuật|

Hãy để chúng tôi sắp xếp hoặc lấy ra tất cả các trường cung cấp thông tin về ngày của hóa đơn.

| Field Name | Details |
| ------------ | --------- |
|monthid|Khóa chính - Id của tháng|
|year|Năm bắt nguồn từ trường tháng của dữ liệu gốc. Ví dụ: 2010|
|month|Số tháng được lấy từ trường tháng của dữ liệu gốc. Ví dụ: 1, 2, 3|
|monthname|Tên tháng được lấy từ trường tháng của dữ liệu gốc. Ví dụ: March|
|quarter|Số quý được lấy từ trường tháng của dữ liệu gốc. Ví dụ: 1, 2, 3, 4|
|quartername|Tên quý bắt nguồn từ trường tháng của dữ liệu gốc. Ví dụ: Q1, Q2, Q3, Q4|

### 9.7.4. Exercise 4: Create a star schema using the fact and dimension tables

Dựa vào 2 bài tập trước hiện tại chúng ta đã có 3 bảng, chúng ta có thể đặt tên như bảng bên dưới.

| Table Name | Type | Details |
| ------------ | --------- | --------- |
|FactBilling|Fact|Bảng này chứa số tiền thanh toán và khóa ngoại cho dữ liệu khách hàng và tháng|
|DimCustomer|Dimension|Bảng này chứa tất cả các thông tin liên quan đến khách hàng|
|DimMonth|Dimension|Bảng này chứa tất cả các thông tin liên quan đến tháng thanh toán|

Khi chúng ta sắp xếp các bảng trên theo kiểu Star Schema, chúng ta sẽ có được cấu trúc bảng trông giống như trong hình bên dưới.

![Star Schema Created by Fact Tables and Dimension Tables](image/star_schema.png)

### 9.7.5. Exercise 5: Create the schema on the data warehouse

[SQL Script Using PostgreSQL](image/star-schema.sql)

### 9.7.6. Practice Exercises

Trong bài tập thực hành này, bạn sẽ phân tích tệp csv bên dưới, chứa dữ liệu về doanh số bán hàng hàng ngày tại các cửa hàng khác nhau của một nhà bán lẻ thời trang quốc tế.

![Fashion retailer CSV](image/fashion_retailer_csv.png)

1. Thiết kế lược đồ cho dimension table DimStore.

| Field Name | Details |
| ------------ | --------- |
|storeid|Id của cửa hàng, khóa chính|
|country|Quốc gia của cửa hàng|
|city|Thành phố của cửa hàng|

2. Thiết kế lược đồ cho dimension table DimDate.

| Field Name | Details |
| ------------ | --------- |
|dateid|Id của ngày, khóa chính|
|dayofweek|Ngày trong tuần|
|day|Ngày của date|
|month|Tháng của date|
|year|Năm của date|
|weekdayname|Tên của ngày trong tuần|
|monthname|Tên của tháng|
|quater|Quý mà date nằm trong|
|quatername|Tên của quý mà date nằm trong|

3. Thiết kế lược đồ cho bảng FactSales.

| Field Name | Details |
| ------------ | --------- |
|saleid|Id của sale, khóa chính|
|storeid|Id của store, khóa ngoại liên kết với DimStore|
|dateid|Id của date, khóa ngoại liên kết với DimDate|
|totalsales|Tổng doanh thu|

# 10. Data Modeling with Star and Snowflake Schemas

## 10.1. What is Star Schema

`Star Schema` được xây dựng dựa trên cách các bảng dimension có thể được hình dung như các nhánh tỏa ra từ một bảng fact trung tâm, và liên kết qua các khóa ngoại. Điều này tạo ra một cấu trúc giống như một đồ thị, nơi các nút là các bảng fact và dimension, còn các cạnh là mối quan hệ giữa các bảng.

![Example Star Schema](image/example_star_schema.png)

`Star schemas thường được sử dụng trong các data marts`, một dạng nhỏ hơn và chuyên biệt của kho dữ liệu.

Ví dụ về Star Schema:

Trung tâm của schema là `Fact Table` cho các giao dịch bán hàng (sale transactions), chứa thông tin như:
 - Sale ID (khóa chính).
 - Sale Amount (số tiền bán hàng).
 - Quantity Sold (số lượng bán).
 - Discount (giảm giá nếu có).

Xung quanh `Fact Table` là các `Dimension Tables`, ví dụ như:

- Store Table lưu trữ tên và địa chỉ cửa hàng.
- Product Table lưu thông tin sản phẩm như tên, mã sản phẩm, và danh mục sản phẩm.
- Date Table lưu ngày tháng của giao dịch.

## 10.2. What is Snowflake Schema?

`Snowflake Schema` là một sự `tổng quát hóa của Star Schema` và có thể được coi là một star schema chuẩn hóa. Chuẩn hóa ở đây có nghĩa là tách các cấp bậc của bảng dimension thành các bảng con riêng biệt.

`Không nhất thiết phải chuẩn hóa hoàn toàn` để được coi là snowflake schema, chỉ cần ít nhất một bảng dimension có các cấp bậc tách ra thành các bảng riêng.

Ví dụ về Snowflake Schema:

- Từ `Star Schema` ở trên, bạn có thể chuẩn hóa Store Table bằng cách tách địa chỉ thành bảng City Table, bảng này chứa thông tin về thành phố mà cửa hàng đặt tại, sau đó thêm City ID vào Store Table để duy trì liên kết.

## 10.3. Design a Star Schema

Khi thiết kế star schema, bạn cần cân nhắc các nguyên tắc sau:

- **Chọn quy trình kinh doanh**: Đây là bước đầu tiên trong việc xác định điều bạn muốn mô hình hóa. Ví dụ, bạn có thể quan tâm đến các quy trình như bán hàng, sản xuất, hoặc chuỗi cung ứng.

- **Chọn mức độ chi tiết (Granularity)**: Mức độ chi tiết bạn muốn nắm bắt trong dữ liệu. Ví dụ, bạn có muốn thu thập dữ liệu ở mức tổng quan như doanh số bán hàng theo năm trong toàn bộ khu vực không, hay bạn muốn chi tiết hơn, như hiệu suất bán hàng hàng tháng theo từng nhân viên bán hàng?

- **Xác định các dimensions**: Bao gồm các thuộc tính như thời gian, tên người, địa điểm, và các yếu tố liên quan khác.

- **Xác định các facts**: Đây là các số liệu cần đo lường trong quy trình kinh doanh. Ví dụ, doanh số bán hàng, số lượng sản phẩm bán ra, hoặc thuế bán hàng.


**Ví dụ thực tiễn**: Giả sử bạn là kỹ sư dữ liệu và được giao nhiệm vụ thiết kế một mô hình dữ liệu cho hệ thống Point-of-Sale (POS) của một cửa hàng bán lẻ có tên là “A to Z Discount Warehouse.” Nhiệm vụ của bạn là thu thập dữ liệu về các giao dịch tại quầy thanh toán, nơi khách hàng thanh toán cho các mặt hàng đã mua.

![Example AZDiscoutWarehouse](image/example_azdiscount_warehouse.png)

- **Quy trình kinh doanh**: Mô hình hóa các giao dịch bán hàng tại điểm bán hàng.
- **Granularity**: Bạn muốn ghi nhận các thông tin chi tiết từng dòng sản phẩm trên hóa đơn của khách hàng.
- **Dimensions**: Ngày giờ mua hàng, tên sản phẩm, tên cửa hàng, và nhân viên thu ngân.
- **Facts**: Giá của mỗi mặt hàng, số lượng bán ra, thuế bán hàng, và giảm giá.

Từ đó, bạn có thể bắt đầu xây dựng Star Schema với `bảng fact trung tâm là POS Fact Table`, chứa các thông tin như:

- POS ID: Mã định danh duy nhất cho từng dòng sản phẩm.
- Amount: Số tiền của giao dịch.
- Quantity: Số lượng sản phẩm.
- Discount: Giảm giá.
- ...

Các bảng dimension sẽ được liên kết với bảng fact qua các khóa ngoại như:

- Store ID từ bảng Store Table.
- Product ID từ bảng Product Table.
- Date ID từ bảng Date Table.
- ...

![AZWarehouse Star Schema](image/azwarehouse_star_schema.png)

## 10.4. Expand from Star Schema to Snowflake Schema

Khi `cần chuẩn hóa`, bạn có thể `tách thêm các thông tin từ bảng dimension thành các bảng con`. Ví dụ, từ Store Table, bạn có thể tạo một bảng City Table để lưu thông tin về thành phố, sau đó liên kết thông qua khóa ngoại City ID. Bạn cũng có thể tách thông tin về State, Country, hoặc Sales Region từ Store Table.

Tiếp tục chuẩn hóa các dimensions khác, ví dụ:

- Tách thông tin Brand từ Product Table thành Brand Table.
- Tách thông tin Category của sản phẩm thành Product Category Table.
- Tách ngày giao dịch thành Day of Week, Month, Quarter, và Year từ Date Table.

![AZWarehouse SnowFlake Schema](image/azwarehouse_snowflake_schema.png)

`Quá trình này tạo ra nhiều cấp bậc phân nhánh`, `giống như hình dạng bông tuyết`, và vì vậy được gọi là `Snowflake Schema`.

## 10.5. Summary

- `Facts` và `Dimension Tables` `kết hợp với các khóa ngoại và khóa chính` để tạo thành các mô hình Star Schema và Snowflake Schema.
- Khi `thiết kế Star Schema`, bạn cần xác định `quy trình kinh doanh`, `mức độ chi tiết`, và `các facts` và `dimensions` liên quan.
- `Snowflake Schema là phiên bản chuẩn hóa của Star Schema`, trong đó việc chuẩn hóa giúp giảm dung lượng bộ nhớ bằng cách tách các bảng dimension thành các bảng con, tạo ra cấu trúc phân nhánh giống hình bông tuyết.

# 11. Data Warehousing with Star and Snowflake schemas

## 11.1. Why do we use these schemas, and how do they differ?

`Star Schemas được tối ưu hóa cho việc đọc` và được `sử dụng rộng rãi để thiết kế trung tâm dữ liệu`, trong khi `Snowflake Schemas được tối ưu hóa cho việc ghi` và được `sử dụng rộng rãi để lưu trữ dữ liệu giao dịch`. Star Schemas là trường hợp đặc biệt của Snowflake Schemas trong đó tất cả các kích thước phân cấp đã được chuẩn hóa hoặc làm phẳng.

|Atrribute|Star Schema|Snowflake Schema|
|---|---|---|
|Tốc độ đọc |Nhanh |Vừa phải |
|Tốc độ ghi |Vừa phải |Nhanh |
|Không gian lưu trữ |Trung bình đến cao |Thấp đến trung bình |
|Rủi ro toàn vẹn dữ liệu |Thấp đến trung bình  |Thấp  |
|Độ phức tạp của truy vấn  |Đơn giản đến vừa phải |Trung bình đến phức tạp |
|Độ phức tạp của lược đồ |Đơn giản đến vừa phải |Trung bình đến phức tạp |
|Phân cấp dimension|Các bảng đơn không chuẩn hóa |Chuẩn hóa trên nhiều bảng |
|Tham gia theo thứ bậc thứ nguyên |Một  |Một cho mỗi cấp độ  |
|Sử dụng lý tưởng với|Hệ thống OLAP (Xử lý phân tích trực tuyến), Data Marts |hệ thống OLTP (Xử lý giao dịch trực tiếp) |

## 11.2. Normalization reduces redundancy

Cả lược đồ ngôi sao và bông tuyết đều được hưởng lợi từ việc áp dụng chuẩn hóa. “Chuẩn hóa làm giảm sự dư thừa” là một thành ngữ chỉ ra lợi thế chính được cả hai lược đồ tận dụng.

Chuẩn hóa bảng có nghĩa là tạo cho mỗi thứ nguyên:

1. Khóa thay thế để thay thế khóa tự nhiên, nghĩa là các giá trị duy nhất của cột đã cho
2. Bảng tra cứu để lưu trữ các cặp khóa thay thế và khóa tự nhiên.

Mỗi giá trị của khóa thay thế được lặp lại chính xác nhiều lần trong bảng chuẩn hóa như khóa tự nhiên trước khi di chuyển khóa tự nhiên sang bảng tra cứu mới. Vì vậy, bạn đã không làm gì để giảm bớt sự dư thừa của bảng gốc.

Tuy nhiên, thứ nguyên thường chứa các nhóm mục xuất hiện thường xuyên, chẳng hạn như “tên thành phố” hoặc “danh mục sản phẩm”. Vì bạn chỉ cần một phiên bản từ mỗi nhóm để xây dựng bảng tra cứu nên bảng tra cứu của bạn sẽ có ít hàng hơn bảng dữ kiện. Nếu có các thứ nguyên con liên quan thì bảng tra cứu có thể vẫn còn một số dư thừa trong các cột thứ nguyên con. Nói cách khác, nếu bạn có thứ nguyên phân cấp, chẳng hạn như “Quốc gia”, “Tiểu bang” và “Thành phố”, bạn có thể lặp lại quy trình ở từng cấp độ để giảm bớt sự dư thừa.

Lưu ý rằng việc chuẩn hóa thêm các thứ nguyên phân cấp của bạn không ảnh hưởng đến kích thước hoặc nội dung của bảng dữ kiện - các mô hình dữ star và snowflake schema có chung các bảng dữ kiện giống hệt nhau.

## 11.3. Normalization reduces data size

Khi chuẩn hóa một bảng, bạn thường giảm kích thước dữ liệu của nó, vì trong quá trình này, bạn có thể thay thế các kiểu dữ liệu đắt tiền, chẳng hạn như chuỗi, bằng các kiểu số nguyên nhỏ hơn nhiều. Nhưng để bảo toàn nội dung thông tin, bạn cũng cần tạo bảng tra cứu mới chứa các đối tượng gốc.

Câu hỏi đặt ra là, bảng mới này có sử dụng ít dung lượng lưu trữ hơn mức tiết kiệm mà bạn vừa đạt được trong bảng chuẩn hóa không?

Đối với dữ liệu nhỏ, câu hỏi này có lẽ không đáng để quan tâm, nhưng đối với dữ liệu lớn, hay chỉ là dữ liệu đang phát triển nhanh chóng thì câu trả lời là có, đó là điều tất yếu. Thật vậy, fact tables của bạn sẽ phát triển nhanh hơn nhiều so với các dimension table, do đó việc chuẩn hóa fact tables của bạn, ít nhất là ở mức độ tối thiểu của star schema có thể được đảm bảo. Bây giờ câu hỏi là cái nào tốt hơn – star hay snowflake?

## 11.4. Comparing benefits: snowflake vs. star data warehouses

`Snowflake, được chuẩn hóa hoàn toàn`, mang lại `ít sự dư thừa nhất và dung lượng lưu trữ nhỏ nhất`. Nếu dữ liệu thay đổi, mức độ dư thừa tối thiểu này có nghĩa là `dữ liệu được phân loại cần phải được thay đổi ở ít vị trí hơn so với yêu cầu đối với lược đồ hình sao`. Nói cách khác, việc ghi nhanh hơn và các thay đổi dễ thực hiện hơn.

`Tuy nhiên`, do cần có `các phép nối bổ sung khi truy vấn dữ liệu nên thiết kế snowflake có thể có tác động bất lợi đến tốc độ đọc`. Bằng cách chuẩn hóa ngược về star schema, bạn có thể tăng hiệu quả truy vấn của mình.

Bạn cũng có thể `chọn con đường trung gian trong việc thiết kế kho dữ liệu của mình`. Bạn có thể chọn lược đồ được chuẩn hóa một phần. Bạn có thể `triển khai snowflake schema làm cơ sở và tạo các chế độ xem hoặc thậm chí các chế độ xem cụ thể hóa dữ liệu không chuẩn hóa`. Ví dụ: bạn có thể mô phỏng star schema trên snowflake schema. Với chi phí phức tạp hơn, bạn có thể chọn từ những gì tốt nhất của cả hai thế giới để tạo ra giải pháp tối ưu đáp ứng yêu cầu của bạn.

## 11.5. Practical differences

Hầu hết các truy vấn bạn áp dụng cho tập dữ liệu, bất kể lựa chọn lược đồ của bạn là gì, đều đi qua bảng dữ kiện. Fact Table của bạn đóng vai trò như một cổng thông tin tới các Dimension Tables của bạn.

`Sự khác biệt thực tế chính giữa star và snowflake schema` theo quan điểm của nhà phân tích `liên quan đến việc truy vấn dữ liệu`. Bạn `cần nhiều kết nối hơn cho snowflake schema để có quyền truy cập vào các cấp độ sâu hơn của thứ nguyên phân cấp`, điều này có thể làm `giảm hiệu suất truy vấn trên lược đồ hình sao`. Do đó, các nhà phân tích dữ liệu và nhà khoa học dữ liệu `có xu hướng thích lược đồ sao đơn giản hơn`.

`Snowflake schema` nhìn chung `phù hợp với việc thiết kế kho dữ liệu` và đặc biệt là `hệ thống xử lý giao dịch`, trong khi `star schema phù hợp hơn để phục vụ Data Marts` hoặc kho dữ liệu có mối quan hệ thứ nguyên thực tế đơn giản. Ví dụ: giả sử bạn có các bản ghi điểm bán hàng tích lũy trong Hệ thống xử lý giao dịch trực tuyến (OLTP) được sao chép dưới dạng quy trình ETL hàng ngày sang một hoặc nhiều hệ thống Xử lý phân tích trực tuyến (OLAP), nơi phân tích tiếp theo khối lượng lớn dữ liệu lịch sử. dữ liệu được thực hiện. Nguồn OLTP có thể sử dụng snowflake để tối ưu hóa hiệu suất cho các lần ghi thường xuyên, trong khi hệ thống OLAP sử dụng lược đồ hình sao để tối ưu hóa cho các lần đọc thường xuyên. Đường dẫn ETL di chuyển dữ liệu giữa các hệ thống bao gồm bước không chuẩn hóa giúp thu gọn từng hệ thống phân cấp của bảng thứ nguyên thành bảng thứ nguyên gốc thống nhất.

## 11.6. Too much of a good thing?

Luôn có sự cân bằng giữa lưu trữ và tính toán sẽ ảnh hưởng đến các lựa chọn thiết kế kho dữ liệu của bạn. Ví dụ: người dùng cuối hoặc ứng dụng của bạn có cần phải tính toán trước các thứ nguyên được lưu trữ như 'ngày trong tuần', 'tháng trong năm' hoặc 'quý' trong năm không? Các cột hoặc bảng hiếm khi được yêu cầu đang chiếm dung lượng đĩa có thể sử dụng được. Có thể tốt hơn là chỉ tính toán các kích thước như vậy trong câu lệnh SQL của bạn khi cần thiết. Ví dụ: với một star schema có dimension table ngày, bạn có thể áp dụng hàm 'MONTH' của SQL dưới dạng MONTH(dim_date.date_column) theo yêu cầu thay vì nối cột tháng được tính toán trước từ bảng MONTH trong lược đồ bông tuyết.

**SCENARIO**

Giả sử bạn được khách hàng giao một mẫu dữ liệu nhỏ từ một tập dữ liệu rất lớn dưới dạng bảng. Họ muốn bạn xem dữ liệu và xem xét các lược đồ tiềm năng cho kho dữ liệu dựa trên mẫu. Tạm thời tạm gác việc thu thập các yêu cầu cụ thể sang một bên, bạn bắt đầu bằng cách khám phá bảng và nhận thấy rằng có chính xác `hai loại cột trong tập dữ liệu - Facts và Dimensions`. `Không có khóa ngoại mặc dù có một chỉ mục`. Bạn coi bảng này như một tập `dữ liệu hoàn toàn không chuẩn hóa` hoặc được làm phẳng.
 
Bạn cũng nhận thấy rằng trong số các thứ nguyên có các cột có `loại dữ liệu tương đối đắt tiền về kích thước lưu trữ, chẳng hạn như chuỗi tên người và địa điểm.`

Ở giai đoạn này, bạn đã biết rằng bạn có thể áp dụng tốt star or snowflake schema cho tập dữ liệu, từ đó chuẩn hóa ở mức độ bạn muốn. Cho dù bạn chọn star hay snowflake, tổng kích thước dữ liệu của bảng dữ kiện trung tâm sẽ giảm đáng kể. Điều này là do `thay vì sử dụng các thứ nguyên trực tiếp trong bảng dữ kiện chính, bạn sử dụng các khóa thay thế`, thường là các số nguyên; và bạn di chuyển các thứ nguyên tự nhiên sang các bảng riêng của chúng hoặc hệ thống phân cấp của các bảng được tham chiếu bởi các khóa thay thế. Ngay cả số nguyên 32 bit cũng nhỏ so với chuỗi 10 ký tự (8 X 10 = 80 bit).
 
Bây giờ, vấn đề là thu thập các yêu cầu và tìm ra sơ đồ chuẩn hóa tối ưu nào đó cho lược đồ của bạn.

# 12. Staging Areas for Data Warehouses

## 12.1. What is Staging Areas in Data Warehouse?

Khu vực dự trữ là một kho lưu trữ trung gian được sử dụng cho quá trình ETL (Extract, Transform, Load - Trích xuất, Chuyển đổi, Tải dữ liệu). Nói một cách đơn giản, đây là cầu nối giữa các nguồn dữ liệu và hệ thống đích như kho dữ liệu (Data Warehouse), data mart hoặc các hệ thống lưu trữ dữ liệu khác.

Các khu vực này thường là tạm thời, tức là dữ liệu sẽ bị xóa sau khi quy trình ETL hoàn tất. Tuy nhiên, trong một số kiến trúc, dữ liệu có thể được giữ lại để phục vụ cho việc lưu trữ hoặc xử lý sự cố. Ngoài ra, khu vực dự trữ còn hữu ích cho việc giám sát và tối ưu hóa các quy trình ETL.

Ví dụ:

- Flat files (các tệp dạng phẳng) như tệp CSV được lưu trữ trong một thư mục và được quản lý bằng các công cụ như Bash hoặc Python.
- Bảng SQL trong các hệ thống quản lý cơ sở dữ liệu quan hệ như Db2.
- Một cơ sở dữ liệu riêng biệt trong nền tảng kho dữ liệu như Cognos Analytics.

## 12.2. Data Warehouse Architecture with Staging Area

Hãy tưởng tượng một doanh nghiệp muốn xây dựng một hệ thống phân tích trực tuyến (OLAP) cho Kế toán Chi phí. Dữ liệu cần thiết được quản lý trong các hệ thống xử lý giao dịch trực tuyến (OLTP) riêng biệt, chẳng hạn như từ bộ phận Nhân sự, bộ phận Bán hàng, và bộ phận Mua hàng.

Dữ liệu từ các hệ thống này sẽ được trích xuất vào các bảng dự trữ riêng biệt, được tạo trong Cơ sở dữ liệu Dự trữ. Sau đó, dữ liệu sẽ được chuyển đổi trong khu vực dự trữ bằng các truy vấn SQL để phù hợp với yêu cầu của hệ thống kế toán chi phí. Khi đã được chuyển đổi, dữ liệu sẽ được tích hợp (joined) thành một bảng duy nhất và sau đó tải vào hệ thống kế toán.

![DW with Staging Area](image/dw_staging_area.png)

## 12.3. Main functions of Staging Area

- **Tích hợp dữ liệu**: Khu vực dự trữ giúp hợp nhất dữ liệu từ nhiều hệ thống nguồn khác nhau.
- **Phát hiện thay đổi**: Có thể thiết lập để chỉ trích xuất các thay đổi mới hoặc dữ liệu đã thay đổi.
- **Lập lịch**: Các tác vụ trong quy trình ETL có thể được lập lịch để chạy theo thứ tự cụ thể hoặc song song.

Ngoài ra còn có:

- **Làm sạch và xác thực dữ liệu**: Ví dụ, xử lý các giá trị thiếu hoặc bản ghi trùng lặp.
- **Tổng hợp dữ liệu**: Dữ liệu bán hàng hàng ngày có thể được tổng hợp thành trung bình hàng tuần, hàng tháng, hoặc hàng năm trước khi tải vào hệ thống báo cáo.
- **Chuẩn hóa dữ liệu**: Đảm bảo tính nhất quán về kiểu dữ liệu hoặc mã danh mục như mã quốc gia và mã bang.

Ví dụ:

Giả sử bạn có dữ liệu về các giao dịch bán hàng từ nhiều cửa hàng khác nhau. Các cửa hàng này có thể có cách ghi nhận khác nhau về tên bang như "Mont," "MA," hoặc "Montana." Khu vực dự trữ sẽ đảm nhận việc chuẩn hóa tất cả các giá trị này về một định dạng chung.

## 12.4. Benefit of Staging Area

Khu vực dự trữ là một khu vực tách biệt, nơi dữ liệu từ hệ thống nguồn được trích xuất. Bước trích xuất này giúp tách biệt các quá trình như xác thực, làm sạch khỏi hệ thống nguồn, giảm thiểu rủi ro gây hỏng dữ liệu gốc. Nó cũng đơn giản hóa việc xây dựng và bảo trì quy trình ETL.

Nếu dữ liệu bị hỏng, bạn có thể dễ dàng khôi phục từ khu vực dự trữ mà không ảnh hưởng đến hệ thống nguồn.

## 12.5. Summary

- Khu vực dự trữ là cầu nối giữa các nguồn dữ liệu và hệ thống đích, giúp tích hợp các nguồn dữ liệu khác nhau trong kho dữ liệu.
- Khu vực dự trữ có thể được triển khai đơn giản dưới dạng các tệp phẳng hoặc bảng trong cơ sở dữ liệu.
- Việc sử dụng khu vực dự trữ giúp giảm thiểu rủi ro hỏng dữ liệu, đồng thời giúp tối ưu hóa quy trình ETL.

Thông qua ví dụ và các chức năng của khu vực dự trữ, chúng ta thấy rõ vai trò quan trọng của nó trong việc đảm bảo quá trình trích xuất, chuyển đổi, và tải dữ liệu diễn ra suôn sẻ và an toàn.

## 12.6. Hands-on Lab: Setting up a staging area

Mục đích của Lab là trang bị cho bạn những kỹ năng thực tế trong việc thiết lập và quản lý máy chủ chạy thử cho kho dữ liệu, đặc biệt là sử dụng PostgreSQL. Lab tập trung vào việc dạy cách thiết kế và triển khai lược đồ cơ sở dữ liệu, tải dữ liệu vào bảng và chạy các truy vấn mẫu để tương tác với dữ liệu. Điều này nhằm mục đích cung cấp cho bạn sự hiểu biết thực tế về những vấn đề phức tạp liên quan đến việc chuẩn bị và quản lý môi trường kho dữ liệu.

[Lab Instruction](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAyNjBFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvU2V0dGluZyUyMHVwJTIwYSUyMHN0YWdpbmclMjBhcmVhL1NldHRpbmclMjB1cCUyMGElMjBzdGFnaW5nJTIwYXJlYS5tZCIsInRvb2xfdHlwZSI6InRoZWlhZG9ja2VyIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE3MjUwMjE4MDB9.3WOPjR78QhS--cUWgfncSrOm52nwWvu4t01IbN3veJw)

# 13. Verify Data Quality

## 13.1. What is Data Quality Verification?

Xác minh chất lượng dữ liệu là quá trình kiểm tra dữ liệu của bạn dựa trên các tiêu chí sau:

- **Độ chính xác (Accuracy)**: Dữ liệu của bạn có chính xác không?
- **Tính đầy đủ (Completeness)**: Có dữ liệu bị thiếu không?
- **Tính nhất quán (Consistency)**: Các trường dữ liệu có được nhập liệu nhất quán không?
- **Tính kịp thời (Currency)**: Dữ liệu của bạn có cập nhật kịp thời không?

Xác minh chất lượng dữ liệu là quản lý chất lượng dữ liệu để nâng cao độ tin cậy của dữ liệu. Dữ liệu chất lượng cao giúp việc tích hợp dữ liệu phức tạp và các mối quan hệ liên quan thành công hơn. Điều này cung cấp cho bạn cái nhìn tổng thể về tổ chức, dữ liệu sẵn sàng cho các phân tích nâng cao, mô hình thống kê và học máy. Cuối cùng, bạn sẽ có nhiều sự tự tin hơn khi ra quyết định.

**Ví dụ:**

Nếu bạn có một tập dữ liệu khách hàng nhưng một số bản ghi thiếu địa chỉ email, thì điều này sẽ gây khó khăn cho việc gửi thông tin khuyến mãi hoặc khảo sát. Xác minh chất lượng dữ liệu giúp bạn phát hiện và khắc phục các lỗi thiếu sót này.

## 13.2. Why we need to verify data quality?

Trong khi điều hành doanh nghiệp, chất lượng dữ liệu thường không được quan tâm đúng mức. Theo báo cáo của Harvard Business Review, ước tính từ IBM năm 2016 cho thấy tổn thất do chất lượng dữ liệu kém ở Mỹ đã lên đến hơn 3 nghìn tỷ đô la mỗi năm. Các tổ chức phải đối mặt với nhiều vấn đề về chất lượng dữ liệu, bao gồm:

- **Độ chính xác**: Đảm bảo dữ liệu từ hệ thống nguồn và hệ thống đích là chính xác và đồng bộ.
    - **Vấn đề thường gặp**: Lỗi chính tả, giá trị vượt ngưỡng, giá trị ngoại lệ, hoặc các lỗi căn chỉnh dữ liệu, chẳng hạn như dấu phẩy không đúng vị trí trong tệp CSV.

- **Tính đầy đủ**: Dữ liệu có thể bị thiếu khi các trường bắt buộc không được điền hoặc hệ thống sử dụng các giá trị thay thế như “999” hoặc “-1” để chỉ ra thiếu sót.

- **Tính nhất quán**: Dữ liệu có được nhập đúng định dạng và quy chuẩn không? Ví dụ, nếu một hệ thống sử dụng định dạng ngày “năm-tháng-ngày” và một hệ thống khác sử dụng “tháng-ngày-năm,” dữ liệu sẽ không nhất quán.

- **Tính kịp thời**: Dữ liệu có được cập nhật mới nhất không? Ví dụ, thông tin địa chỉ khách hàng có thể bị lỗi thời, gây khó khăn trong việc liên lạc.

Ví dụ trực quan:

Trong một cơ sở dữ liệu khách hàng, một số khách hàng có tên là "Mr. John Doe," trong khi những người khác chỉ có "John Doe." Điều này có thể gây nhầm lẫn vì hệ thống sẽ xem hai bản ghi này là hai cá nhân khác nhau.

## 13.3. Error Data Processing

Việc xử lý và ngăn ngừa dữ liệu lỗi là một quy trình phức tạp và lặp đi lặp lại. Dưới đây là quy trình điển hình:

- **Thiết lập quy tắc để phát hiện dữ liệu lỗi.** Ví dụ, bạn có thể viết các truy vấn SQL để kiểm tra các giá trị thiếu hoặc giá trị vượt ngưỡng.

- **Cô lập dữ liệu lỗi sau khi phát hiện.** Ví dụ, bạn có thể lưu trữ dữ liệu lỗi trong một khu vực cách ly để không ảnh hưởng đến các quy trình khác.

- **Báo cáo dữ liệu lỗi và chia sẻ với chuyên gia** để phân tích nguyên nhân gốc rễ của vấn đề, từ đó điều chỉnh quy trình để ngăn ngừa lỗi xảy ra trong tương lai.

- **Tự động hóa quy trình**: Tạo các script để tự động kiểm tra và sửa lỗi dữ liệu trong các lần tải dữ liệu hàng đêm.

Ví dụ:

Một doanh nghiệp phát hiện ra rằng dữ liệu từ một số nguồn luôn gặp phải các vấn đề như thiếu dữ liệu, trùng lặp, và giá trị không hợp lệ. Họ viết các truy vấn SQL để kiểm tra và loại bỏ các bản ghi lỗi này. Sau đó, họ tạo một script tự động chạy các truy vấn đó vào ban đêm và báo cáo những vấn đề chưa được giải quyết.

## 13.4. Tools

Có nhiều công cụ hỗ trợ các tổ chức xác minh và quản lý chất lượng dữ liệu, chẳng hạn như:

- IBM InfoSphere Information Server for Data Quality
- Informatica Data Quality
- SAP Data Quality Management
- SAS Data Quality
- Talend Open Studio for Data Quality
- Microsoft Data Quality Services
- Oracle Enterprise Data Quality
- OpenRefine (một công cụ mã nguồn mở)

Ví dụ: IBM InfoSphere Information Server for Data Quality

Sản phẩm này giúp bạn liên tục giám sát chất lượng dữ liệu và duy trì dữ liệu luôn sạch. Nó cung cấp các công cụ để:

- Hiểu dữ liệu và các mối quan hệ của nó.
- Giám sát và phân tích chất lượng dữ liệu một cách liên tục.
- Làm sạch, chuẩn hóa và khớp dữ liệu.
- Bảo trì lịch sử dữ liệu, bao gồm nguồn gốc và những gì đã xảy ra với dữ liệu trong quá trình sử dụng.

## 13.5. Summary

- Xác minh chất lượng dữ liệu dựa trên các yếu tố: độ chính xác, tính đầy đủ, tính nhất quán, và tính kịp thời.
- Xác minh dữ liệu giúp quản lý chất lượng, tăng độ tin cậy và giá trị của dữ liệu.
- Xử lý dữ liệu lỗi là một quy trình phức tạp và lặp đi lặp lại, nhưng có thể tự động hóa để giảm thiểu công việc thủ công.
- Các công cụ như IBM InfoSphere Information Server for Data Quality giúp quản lý dữ liệu trong một môi trường thống nhất và toàn diện.

Việc duy trì chất lượng dữ liệu không chỉ giúp giảm thiểu rủi ro, mà còn nâng cao độ chính xác của các phân tích và quyết định kinh doanh trong doanh nghiệp.

## 13.6. Hands-on Lab: Verifying Data Quality for a Data Warehouse

[Lab Instruction](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAyNjBFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvVmVyaWZ5aW5nJTIwRGF0YSUyMFF1YWxpdHklMjBmb3IlMjBhJTIwRGF0YSUyMFdhcmVob3VzZS9WZXJpZnlpbmclMjBEYXRhJTIwUXVhbGl0eSUyMGZvciUyMGElMjBEYXRhJTIwV2FyZWhvdXNlLm1kIiwidG9vbF90eXBlIjoidGhlaWFkb2NrZXIiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTcyNjAzNzIwNn0.fDGoN3u4As3IzmuG2AfKHQVAix1QjCpOdl2oN4uOxxU)

# 14. Populating a Data Warehouse

## 14.1. Loading Frequency

Nhập dữ liệu vào Data Warehouse của doanh nghiệp là một quá trình liên tục bao gồm hai giai đoạn:

- **Tải ban đầu (Initial Load)**: Đây là bước đầu tiên khi bạn tải toàn bộ dữ liệu vào Data Warehouse.
- **Tải dữ liệu từng phần (Incremental Load)**: Đây là quá trình định kỳ, có thể là hàng ngày hoặc hàng tuần, để cập nhật những thay đổi mới trong dữ liệu.

**Một ví dụ thực tế**: bạn có thể tải các giao dịch bán hàng mới vào Data Warehouse vào mỗi cuối tuần, trong khi các danh sách thành phố hoặc cửa hàng (các bảng dimension) hiếm khi thay đổi và chỉ cần cập nhật định kỳ khi có sự thay đổi lớn.

1. Tải ban đầu và tải từng phần

- `Fact tables` là các bảng chứa các dữ liệu giao dịch, thường thay đổi liên tục và cần cập nhật thường xuyên.
- `Dimension tables` chứa các thông tin tĩnh hơn, như danh sách thành phố, loại sản phẩm, hoặc thông tin nhân viên, và thường không thay đổi nhiều.

Ví dụ: Bảng fact có thể chứa thông tin về các giao dịch bán hàng diễn ra hàng ngày, trong khi bảng dimension có thể chứa thông tin về các cửa hàng bán hàng, không cần cập nhật quá thường xuyên.

2. Công cụ hỗ trợ quá trình nhập liệu

Nhiều công cụ có sẵn để tự động hóa quá trình này, ví dụ:

- Db2 Load Utility có thể tải dữ liệu nhanh hơn so với việc chèn từng dòng.
- Công cụ `Apache Airflow` và `Apache Kafka` cũng được dùng để tự động hóa quá trình nhập dữ liệu trong các ETL pipelines.

Ngoài ra, bạn cũng có thể tự viết các script sử dụng các công cụ như Bash, Python, và SQL để xây dựng pipeline dữ liệu và sử dụng cron để định lịch.

3. Quá trình nhập dữ liệu ban đầu

Trước khi bắt đầu nhập dữ liệu, cần đảm bảo rằng:

- Schema đã được mô hình hóa.
- Dữ liệu đã được chuyển qua giai đoạn staging vào các bảng hoặc file.
- Có cơ chế để kiểm tra chất lượng dữ liệu.

Sau đó, quá trình nhập dữ liệu bắt đầu với:

- Khởi tạo Data Warehouse và tạo bảng theo schema đã thiết lập.
- Thiết lập mối quan hệ giữa các bảng fact và dimension.
- Tải dữ liệu đã làm sạch và chuẩn bị vào các bảng từ staging tables.

## 14.2. Incremental Load and Change Detection

Sau khi tải dữ liệu ban đầu, bước tiếp theo là thiết lập quá trình tải dữ liệu từng phần để cập nhật thường xuyên.

- **Tải dữ liệu từng phần (Incremental Load)**: Đây là việc chỉ cập nhật những bản ghi mới, thay đổi, hoặc đã bị xóa kể từ lần tải cuối cùng.
- **Phát hiện thay đổi (Change Detection)**: Cần phát hiện những thay đổi trong hệ thống nguồn, ví dụ, thông qua timestamps ghi lại thời gian tạo hoặc cập nhật dữ liệu.

Ví dụ: Nếu bạn có một bảng chứa thông tin địa chỉ khách hàng, mỗi khi một địa chỉ được thay đổi, bạn chỉ cần tải các thay đổi này thay vì tải lại toàn bộ bảng.

Một số hệ thống cung cấp cơ chế phát hiện thay đổi, nhưng trong trường hợp không có, bạn có thể sử dụng phương pháp so sánh đối chiếu toàn bộ dữ liệu, mặc dù phương pháp này chỉ phù hợp khi kích thước dữ liệu nguồn không quá lớn.

## 14.3. Data Warehouse Periodic Maintenance

Data Warehouse cần được bảo trì định kỳ, có thể là hàng tháng hoặc hàng năm, để lưu trữ dữ liệu cũ và ít được sử dụng.

- **Lưu trữ (Archive)**: Dữ liệu cũ có thể được chuyển sang các kho lưu trữ có tốc độ truy xuất chậm hơn nhưng ít tốn chi phí hơn.
- **Xóa dữ liệu cũ (Delete old data)**: Dữ liệu không còn hữu ích sẽ được loại bỏ khỏi hệ thống để tối ưu hiệu suất.

## 14.4. Example Populating Data

Hãy cùng xem một ví dụ thực tế về cách nhập dữ liệu thủ công vào Data Warehouse với sơ đồ sao (Star Schema) của một công ty bán ô tô giả định tên là Shiny Auto Sales.

Dữ liệu bán hàng có các cột sau:

- `“sales ID”` là mã hóa đơn bán hàng.
- `“emp no”` là mã số nhân viên.
- `“class ID”` là mã loại xe bán ra, ví dụ "small SUV".
- `“date”` là ngày giao dịch.
- `“amount”` là số tiền bán hàng (fact chính trong bảng fact).

![Example: autosale data](image/example_sales_data.png)

Trong ví dụ này, chúng ta sẽ sử dụng PSQL, giao diện dòng lệnh của PostgreSQL, để tạo và nhập liệu vào bảng DimSalesPerson (bảng dimension của nhân viên bán hàng).

**Tạo bảng Dimension**

Dùng lệnh CREATE TABLE để tạo bảng DimSalesPerson:

```SQL
CREATE TABLE sales.DimSalesPerson (
  SalesPersonID SERIAL primary key,
  SalesPersonAltID varchar(10) not null,
  SalesPersonName varchar(50)
)
```

Sau khi tạo bảng, ta sử dụng lệnh INSERT INTO để thêm dữ liệu vào bảng này, ví dụ:

```SQL
INSERT INTO sales.DimSalesPerson(SalesPersonAltID, SalesPersonName)
values
(617, 'Gocart Joe'),
(642, 'Jake Salesbouroughs'),
(680, 'Cadillac Jack'),
(707, 'Jane Honda'),
(720, 'Keyla Keycar'),
(607, 'William Jeepman'),
(609, 'Happy Dollarmaker'),
(711, 'Sally Caraway');
```

Dữ liệu cho các dimension khác cũng được nhập theo cách tương tự.

**Tạo bảng Fact**

Tiếp theo, ta tạo bảng fact cho giao dịch bán hàng với lệnh:

```SQL
CREATE TABLE sales.FactAutoSales(
  TransactionID bigserial primary key,
  SalesID int not null,
  SalesDateKey int,
  AutoClassID int not null,
  SalesPersonID int not null,
  Amount money
)
```

**Thiết lập mối quan hệ giữa các bảng**

Sau khi tạo bảng, ta cần thiết lập quan hệ giữa các bảng fact và dimension. Ví dụ, dùng lệnh ALTER TABLE và ADD CONSTRAINT để tạo khóa ngoại:

```SQL
ALTER TABLE sales.FactAutoSales
ADD CONSTRAINT
KV_AutoClassID FOREIGN KEY (AutoClassID)
REFERENCES
sales.DimAutoCategory(AutoClassID)
```

**Nhập dữ liệu vào bảng Fact**

Cuối cùng, ta dùng lệnh INSERT INTO để nhập dữ liệu vào bảng fact:

```SQL
INSERT INTO sales.FactAutoSales(
  SalesID,
  Amount,
  SalesPersonID,
  AutoClassID,
  SalesDateKey
)
values
(1629, 42000.00, 2, 1, 4),
(1630, 17680.00, 1, 2, 4),
(1631, 37100.00, 2, 2, 5);
```

## 14.5. Summary

- Quá trình nhập dữ liệu vào Data Warehouse bao gồm tải ban đầu và tải dữ liệu từng phần.
- Fact tables thường xuyên thay đổi, trong khi dimension tables khá tĩnh.
- Bạn có thể tự động hóa quá trình nhập dữ liệu và bảo trì định kỳ của Data Warehouse bằng các công cụ hoặc script.

## 14.6. Hands-on

[Lab Instruction](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAyNjBFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvQklXb3JrYXJvdW5kRmlsZXMvd2VlazIvUG9wdWxhdGluZ19kYXRhd2FyZWhvdXNlX3dpdGhfcG9zdGdyZXMubWQiLCJ0b29sX3R5cGUiOiJ0aGVpYW9wZW5zaGlmdCIsImFkbWluIjpmYWxzZSwiaWF0IjoxNzIyODYxNTUwfQ.aBsSwOkitqvgplLag0F7G6m53j0DklBu9EpwjxZWNVw)

**PRACTICE**

**Bài toán 1**: Sử dụng công cụ PostgreSQL tìm số hàng trong bảng FactBilling

```SQL
SELECT count(*) from public."FactBilling";
```

**Bài toán 2**: Sử dụng công cụ PostgreSQL, tạo một chế độ xem cụ thể hóa đơn giản có tên avg_customer_bill với các trường customerid và averagebillamount.

```SQL
CREATE MATERIALIZED VIEW avg_customer_bill (customerid, averagebillamount)
AS 
(SELECT customerid, avg(billamount) 
FROM public."FactBilling" 
GROUP BY customerid
);
```

**Bài toán 3**: Làm mới các khung nhìn Materialized mới được tạo

```SQL
REFRESH MATERIALIZED VIEW avg_customer_bill;
```

**Bài toán 4**: Sử dụng các chế độ xem Materialized mới được tạo để tìm những khách hàng có hóa đơn trung bình lớn hơn 11000.

```SQL
SELECT * 
FROM avg_customer_bill
WHERE averagebillamount > 11000;
```

# 15. Querying the Data

Nhắc lại về Materialized View: `Materialized view cho phép bạn tạo ra một bảng được lưu trữ mà bạn có thể làm mới theo lịch trình hoặc khi cần`. Khi một view phức tạp, thường xuyên được yêu cầu, hoặc chạy trên tập dữ liệu lớn, việc materialize view có thể giúp giảm tải cho cơ sở dữ liệu. Do `dữ liệu đã được tính trước`, việc `truy vấn materialized view thường nhanh hơn so với việc truy vấn các bảng cơ bản`.

Kết hợp các thao tác CUBE hoặc ROLLUP với materialized view có thể nâng cao hiệu suất, và bạn thậm chí có thể tạo materialized cho chính CUBE hoặc ROLLUP đó.

## 15.1. Scenario

Bạn có nhiệm vụ tạo một bảng tóm tắt trực tiếp để báo cáo doanh số bán hàng tháng 1 của các nhân viên bán hàng và các loại ô tô cho doanh nghiệp ShinyAutoSales.

Bắt đầu bằng cách tìm hiểu star schema trong kho dữ liệu của họ được gọi là `sasDW` dựa trên PostgreSQL. Sau đó khám phá các dữ liệu ShinyAutoSales có liên quan bằng cách truy vấn các bảng từ `sales` star schema trong sasWD.

Sau khi khám phá xong lược đồ, bạn quyết định tạo một Materialized View như một staging table. Việc tạo một chế độ xem dưới dạng staging table như vậy sẽ vẫn cung cấp được dữ liệu mình cần trong khi tối thiểu hóa tác động đến csdl. Có thể làm mới (refesh) view dần dần vào những giờ thấp điểm.

## 15.2. ShinyAutoSales - ERD

![ShinyAutoSales ERD](image/shinyautosales_erd.png)

Table màu đỏ chính là fact table.

## 15.3. View the tables

Giả sử rằng đã kết nối vào csdl mà công ty cung cấp và vào được kho dữ liệu sasWD, với giao diện PostgreSQL như sau:

![PostgresSQL interface](image/psql_interface.png)

Ta cùng xem qua Fact Table

![Fact Table](image/sales_fact_table.png)

Tiếp tục xem các Dimension Tables

![View Auto Category Table](image/view_auto_category.png)

![View Sales Person](image/view_sales_person.png)

![View Date](image/view_date.png)

## 15.4. Denormalized View

Ở giai đoạn này, sẽ thuận tiện hơn nếu có một bảng dữ liệu chứa các cột mà con người có thể dễ dàng hiểu được, thay vì chỉ là các khóa như fact table. Về cơ bản, chúng ta muốn tạo một bảng không chuẩn hóa bằng cách join các dimension tables lại.

![denormailized_view](image/denormalized_view.png)

Thay vì cứ select quài một câu lệnh, ta có thể tạo một bảng xem Materialized View với tên gọi là `DNsales` như sau:

![denormalized_view_materialized_view](image/denormalized_view_materialized_view.png)

Ta cùng xem trong `DNsales` này có gì:

![DNsales_view](image/DNsales_view.png)

## 15.5. Applying CUBE and ROLLUP to the materialized view

1. Ta có thể áp dụng CUBE cho `DNsales` như sau:

Ta chọn `autoclassname`, `salespersonname`, và tổng số tiền bán hàng với điều kiện hàng bán ra là `new` và cuối cùng gom nhóm theo `autoclassname` và `salespersonname` và đầu ra sẽ trông thế này:

![apply_cube_dnsales](image/apply_cube_dnsales.png)

Ở hàng đầu tiên, không có mục nào trong 2 cột `autoclassname` và `salespersonname`, điều này có nghĩa là đếm tất cả thể hiện tổng doanh thu cho các hàng "mới" được bán ra.

Và khối tiếp theo, khối mà có thông tin ở cả hai cột. Có thể đọc ví dụ như sau:

- Ở hàng `|Midsize SUV | Gocart Joe | 32,099,00|` có thể được đọc là tổng doanh thu bán xe Midsize SUV mới được bán bởi Gocart Joe là 32,099,00 USD.

Tương tự ở hai khối tiếp theo nơi mà một cột bị khuyết ở khối này thể hiện doanh thu của riêng cá thể đó.

2. Tương tự áp dụng ROLLUP vào `DNsales` giống hệt ở trên chỉ thay chữ CUBE thành ROLLUP:

![apply_rollup_dnsales](image/apply_rollup_dnsales.png)

Kết quả gần như tương tự chỉ thiếu đi 5 hàng mà chỉ có cột `salespersonname`. Vậy ta có thể thấy CUBE sẽ tạo ra tất cả các hoán vị mà có thể `GROUP BY`, còn ROLLUP chỉ tạo ra hoán vị duy nhất được xác định theo thứ tự được liệt kê trong lệnh gọi ROLLUP (ở đây là `autoclassname, salespersonname`) 

## 15.6. Hands-on

[Lab Instruction](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAyNjBFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvQklXb3JrYXJvdW5kRmlsZXMvd2VlazIvUXVlcnlpbmdfZHdfY3ViZXNfcm9sbHVwc19ncm91cGluZ3NldHNfTVFULm1kIiwidG9vbF90eXBlIjoidGhlaWFvcGVuc2hpZnQiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTcyMzgwNjU3OX0.EB_qnA2t3Jpug_HwJsbBz4uD-FXzit-K9K63yian4gg)

# 16. Practice Project

## 16.1. Scenario

Bạn là kỹ sư dữ liệu được một công ty bán lẻ điện tử tiêu dùng thuê. Công ty bán nhiều sản phẩm điện tử khác nhau thông qua các kênh trực tuyến và ngoại tuyến trên khắp các thành phố lớn ở Hoa Kỳ. Họ vận hành nhiều cửa hàng và nhà kho để quản lý hàng tồn kho và hoạt động bán hàng của mình. Công ty muốn tạo một kho dữ liệu để phân tích hiệu suất bán hàng và quản lý hàng tồn kho, đồng thời nhằm mục đích tạo các báo cáo, chẳng hạn như:

- Tổng doanh thu bán hàng mỗi năm tại mỗi thành phố
- Tổng doanh thu bán hàng mỗi tháng tại mỗi thành phố
- Tổng doanh thu bán hàng mỗi quý tại mỗi thành phố
- Tổng doanh thu bán hàng mỗi năm cho mỗi loại sản phẩm
- Tổng doanh thu bán hàng theo danh mục sản phẩm tại mỗi thành phố
- Tổng doanh thu bán hàng theo danh mục sản phẩm trên mỗi cửa hàng

## 16.2. Instruction

Trong project này các việc cần làm là:

- Task 1: Thiết kế Dimension Table DimDate
- Task 2: Thiết kế Dimension Table DimProduct
- Task 3: Thiết kế Dimension Table DimCustomerSegment
- Task 4: Thiết kế Fact Table FactSales
- Task 5: Tạo Dimension Table DimDate
- Task 6: Tạo Dimension Table DimProduct
- Task 7: Tạo Dimension Table DimCustomerSegment
- Task 8: Tạo Fact Table FactSales
- Task 9: Nạp dữ liệu vào DimDate
- Task 10: Nạp dữ liệu vào DimProduct
- Task 11: Nạp dữ liệu vào DimCustomerSegment
- Task 12: Nạp dữ liệu vào FactSales
- Task 13: Tạo truy vấn Grouping Sets
- Task 14: Tạo truy vấn Rollup
- Task 15: Tạo truy vấn Cube sử dụng các cột (year, city, productid, average sales revenue)
- Task 16: Tạo Materialized View tên `max_sales` sử dụng các cột (city, productid, product type, and max sales)

Điều kiện: Phải sử dụng CSDL PostgreSQL, thiết kế lược đồ hình sao

## 16.3. Go to project

**Original Table Data**

|Sales ID| 	Product Type| 	Price Per Unit| 	Quantity Sold| 	City 	Date|
|------|------|-----|-----|-----|
|001| 	Electronics| 	$299.99| 	30| 	New York| 	2024-04-01|
|002| 	Apparel| 	$49.99 	50| 	Los Angeles| 	2024-04-01|
|003| 	Furniture| 	$399.99| 	10| 	Chicago| 	2024-04-02|
|004| 	Electronics| 	$199.99| 	20| 	Houston| 	2024-04-02|
|005| 	Groceries| 	$2.99| 	100| 	Miami 	|2024-04-03|

Task 1: Thiết kế DimDate

|Column name| Description|
|---|---|
|dateID|Khóa chính|
|day|lấy ra ngày|
|month|lấy ra tháng|
|year|lấy ra năm|
|quarter| số quý (int range 1-4)|
|quarterName| tên quý varchar|
|weekday| ngày trong tuần (int range 1-8)|
|weekdayname| tên ngày trong tuần (varchar (mon, tue, ...))|

Task 2: Thiết kế DimProduct

|Column name|Description|
|---|---|
|productID|Khóa chính|
|productName|Tên của sản phẩm|

Task 3: Thiết kế DimCustomerSegment

|Column name|Description|
|---|---|
|segmentID|Khóa chính|
|segmentName|tên loại khách hàng|

Task 4: Thiết kế FactSales

|Column name|Description|
|---|---|
|salesID|Khóa chính|
|quantitySold|số lượng hàng bán ra|
|pricePerUnit|giá mỗi một mặt hàng|
|productID|khóa phụ nối với DimProduct|
|segmentID|khóa phụ nối với DimCustomerSegment|
|dateID|khóa phụ nối với DimDate|

Task 5: Tạo bảng DimDate

Đầu tiên tạo database trước

```SQL
create database my_electric_amount_project;
use my_electric_amount_project;
```

```SQL
create table DimDate (
  dateID int not null primary key,
  year int,
  month int,
  day int,
  quarter int,
  quaterName varchar(10),
  weekday int,
  nameweekday varchar(10)
);
```

Task 6: Tạo bảng DimProduct

```SQL
create table DimProduct (
  productID int not null primary key,
  productName varchar(50)
);
```

Task 7: Tạo bảng DimCustomerSegment

```SQl
create table DimCustomerSegment (
  segmentID int noll null primary key,
  segmentName varchar(255)
);
```

Task 8: Tạo FactSales

```SQL
create table FactSales (
  salesID int not null primary key,
  quantitySold int,
  pricePerUnit decimal(10, 2),
  productID int,
  segmentID int,
  dateID int,
  foreign key (productID) references DimProduct(productID),
  foreign key (segmentID) references DimCustomerSegment(segmentID),
  foreign key (dateID) references DimDate(dateId)
);
```

Task 9: Load Data to DimDate

[Data Link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/-omGFpVSWBIZKFSCxUkBwg/DimDate.csv)

Task 10: Load Data to DimProduct

[Data Link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/Y-76u4An3zb5R6HxxFPabA/DimProduct.csv)

Task 11: Load Data to DimCustomerSegment

[Data Link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/h_dnxb8yzQyVjeb8oYnm8A/DimCustomerSegment.csv)

Task 12: Load Data to FactSales

[Data Link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/a8kTjzvpdqzOp46ODatyAA/FactSales.csv)


Task 13: Tạo một truy vấn Grouping Sets

Tạo truy vấn nhóm nhóm bằng cách sử dụng các cột Productid, Producttype, Total Sales.

```SQL
SELECT
      p.Productid,
      p.Producttype,
      SUM(f.Price_PerUnit * f.QuantitySold) AS TotalSales
FROM
      FactSales f
INNER JOIN
      DimProduct p ON f.Productid = p.Productid
GROUP BY GROUPING SETS (
      (p.Productid, p.Producttype),
      p.Productid,
      p.Producttype,
      ()
)
ORDER BY
      p.Productid,
      p.Producttype;
```

Trong truy vấn này, chúng ta join FactSales "f" với DimProduct "d" dựa trên productid để tương quan mỗi lần bán hàng với loại sản phẩm.

Ta sử dụng GROUPING SETS để chỉ định cấp độ tổng hợp khác nhau:
- Theo cả Productid và Producttype
- Chỉ có Productid
- Chỉ có Producttype
- Và tổng `()`, không group gì cả do đó trả về tổng cho tất cả doanh số bán hàng.

Task 14: Tạo truy vấn Rollup

Tạo truy vấn tổng hợp bằng cách sử dụng các cột năm, thành phố, id sản phẩm và tổng doanh số. 

```SQL
SELECT
      d.Year,
      cs.City,
      p.Productid,
      SUM(f.Price_PerUnit * f.QuantitySold) As TotalSales
FROM
      FactSales f
INNER JOIN
      DimDate d ON f.Dateid = d.Dateid
INNER JOIN
      DimProduct p ON f.Productid = p.Productid
INNER JOIN
      DimCustomerSegment cs ON f.Segmentid = cs.Segmentid
GROUP BY ROLLUP (d.Year, cs.City, p.Productid)
ORDER BY
      d.Year DESC,
      cs.City,
      p.Productid;
```

Truy vấn này thực hiện những hoạt động sau:

Tính toán và join các bảng Dim lại với bảng Fact theo khóa ngoại. Nhóm các kết quả bằng hàm ROLLUP để tạo một nhóm nhóm bao gồm tất cả các kết hợp của năm, thành phố và id sản phẩm, cùng với các tổng phụ tương ứng và tổng cộng cho tất cả doanh số bán hàng.

Task 15: Tạo truy vấn CUBE bằng cách sử dụng các cột năm, thành phố, id sản phẩm và doanh số trung bình.

```SQL
SELECT
    d.Year,
    cs.City,
    p.Productid,
    AVG(f.Price_PerUnit * f.QuantitySold) AS AverageSales
FROM
    FactSales f
INNER JOIN
    DimDate d ON f.Dateid = d.Dateid
INNER JOIN
    DimProduct p ON f.Productid = p.Productid
INNER JOIN
    DimCustomerSegment cs ON f.Segmentid = cs.Segmentid
GROUP BY CUBE (d.Year, cs.City, p.Productid);
```

Mệnh đề CUBE được sử dụng trong GROUP BY để tạo tổng phụ cho tất cả các kết hợp năm, thành phố và mã sản phẩm ngoài tổng cộng của tất cả các nhóm.

Task 16: Tạo Materialized View tên `max_sales` bằng cách sử dụng các cột thành phố, id sản phẩm, loại sản phẩm và doanh số tối đa.

```SQL
    CREATE MATERIALIZED VIEW max_sales AS
    SELECT
        cs.City,
        p.Productid,
        p.Producttype,
        MAX(f.Price_PerUnit * f.QuantitySold) AS MaxSales
    FROM
        FactSales f
    JOIN
        DimProduct p ON f.Productid = p.Productid
    JOIN
        DimCustomerSegment cs ON f.Segmentid = cs.Segmentid
    GROUP BY
        cs.City,
        p.Productid,
        p.Producttype
    WITH DATA;
```

Câu lệnh này sẽ tạo chế độ xem cụ thể hóa và điền vào đó dữ liệu hiện tại từ các bảng đã nối. Mệnh đề `WITH DATA` yêu cầu PostgreSQL điền kết quả truy vấn vào khung nhìn ngay lập tức. Nếu bạn muốn tạo chế độ xem mà không điền dữ liệu vào đó, bạn sẽ sử dụng `WITH NO DATA`.

