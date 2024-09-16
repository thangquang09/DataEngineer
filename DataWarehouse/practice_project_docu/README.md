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