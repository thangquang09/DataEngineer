- [Module 1](#module-1)
  - [1. Database Life Cycle Management](#1-database-life-cycle-management)
    - [1.1 Thiết kế phân tích yêu cầu](#11-thiết-kế-phân-tích-yêu-cầu)
    - [1.2 Thiết kế và lập kế hoạch triển khai cơ sở dữ liệu](#12-thiết-kế-và-lập-kế-hoạch-triển-khai-cơ-sở-dữ-liệu)
    - [1.3 Xây dựng thực tế](#13-xây-dựng-thực-tế)
    - [1.4 Giám sát thực tế và duy trì hoạt động thường ngày](#14-giám-sát-thực-tế-và-duy-trì-hoạt-động-thường-ngày)
  - [2. Database Object](#2-database-object)
    - [2.1 Instance](#21-instance)
    - [2.2 Schema](#22-schema)
    - [2.3 Database Object](#23-database-object)
  - [3. System Objects and Database Configuration](#3-system-objects-and-database-configuration)
    - [3.1 System Objects](#31-system-objects)
      - [3.1.1 Db2 system objects](#311-db2-system-objects)
      - [3.1.2 MySQL system objects](#312-mysql-system-objects)
      - [3.1.3 PostgreSQL system objects](#313-postgresql-system-objects)
    - [3.2 Database Configuration](#32-database-configuration)
    - [3.3 Example RDBMS configurations](#33-example-rdbms-configurations)
    - [3.4 How to configure databases](#34-how-to-configure-databases)
  - [4. Database Storage](#4-database-storage)
    - [4.1 Plan database storage](#41-plan-database-storage)
    - [4.2 Tablespaces and Containers](#42-tablespaces-and-containers)
    - [4.3 Tablespace benefits](#43-tablespace-benefits)
    - [4.4 Storage Group](#44-storage-group)
    - [4.5 Data partitions](#45-data-partitions)
    - [4.6. Commands for working with Storage Engines](#46-commands-for-working-with-storage-engines)
    - [4.7. Postgre CLI](#47-postgre-cli)
- [Module 2](#module-2)
  - [5. Backup and Restore](#5-backup-and-restore)
    - [5.1. Physical vs logical backups](#51-physical-vs-logical-backups)
      - [5.1.1. Logical backup](#511-logical-backup)
      - [5.1.2. Physical backup](#512-physical-backup)
    - [5.2. Những gì có thể backup](#52-những-gì-có-thể-backup)
    - [5.3. Key considerations](#53-key-considerations)
    - [5.4. Backup options](#54-backup-options)
    - [5.5. Types of backup](#55-types-of-backup)
      - [5.5.1. Full backup](#551-full-backup)
      - [5.5.2. Point-in-time backup](#552-point-in-time-backup)
      - [5.5.3. Differential backup](#553-differential-backup)
      - [5.5.4. Incremental backup](#554-incremental-backup)
    - [5.6. Backup Policies](#56-backup-policies)
      - [5.6.1. Hot Backup](#561-hot-backup)
      - [5.6.2. Cold backup](#562-cold-backup)
      - [5.6.3. Hot and Cold](#563-hot-and-cold)
    - [5.7 Using Database transaction logs for recovery](#57-using-database-transaction-logs-for-recovery)
      - [5.7.1. Khái niệm và ví dụ](#571-khái-niệm-và-ví-dụ)
      - [5.7.2. Storing transaction log files](#572-storing-transaction-log-files)
      - [5.7.3. Accessing transaction log files](#573-accessing-transaction-log-files)
      - [5.7.3. Lab with PostreSQL](#573-lab-with-postresql)
      - [5.7.3. Lab with MySQL](#573-lab-with-mysql)
      - [5.7.4. Perform Point-in-Time Backup and Restore](#574-perform-point-in-time-backup-and-restore)
      - [5.7.5. Performing MySQL Physical Backup and Restoration](#575-performing-mysql-physical-backup-and-restoration)
- [Module 3](#module-3)
  - [6. Monitoring and Optimization](#6-monitoring-and-optimization)
    - [6.1. Database monitoring](#61-database-monitoring)
    - [6.2. Database monitoring tasks](#62-database-monitoring-tasks)
    - [6.3. Reactive monitoring](#63-reactive-monitoring)
    - [6.4. Proactive Monitoring](#64-proactive-monitoring)
    - [6.5. Establish a performance baseline](#65-establish-a-performance-baseline)
    - [6.6. Baseline data (các thứ có thể ảnh hưởng đến hiệu suất)](#66-baseline-data-các-thứ-có-thể-ảnh-hưởng-đến-hiệu-suất)
    - [6.7. Database monitoring options](#67-database-monitoring-options)
  - [7. Monitoring usage and performance](#7-monitoring-usage-and-performance)
    - [7.1. Levels of monitoring](#71-levels-of-monitoring)
      - [7.1.1. Infrastructure level](#711-infrastructure-level)
      - [7.1.2. Instance (RDBMS) level](#712-instance-rdbms-level)
      - [7.1.3. Query level](#713-query-level)
      - [7.1.4. User level](#714-user-level)
    - [7.2. Typical Metrics](#72-typical-metrics)
    - [7.3. Others metrics](#73-others-metrics)
    - [7.4. Tool for view listed metrics](#74-tool-for-view-listed-metrics)
    - [7.5. Optimizing Database](#75-optimizing-database)
      - [7.5.1. MySQL](#751-mysql)
      - [7.5.2. PostgreSQL](#752-postgresql)
    - [7.6. Using Indexes](#76-using-indexes)
      - [7.6.1. Tại Sao Cần Sử Dụng Chỉ Mục?](#761-tại-sao-cần-sử-dụng-chỉ-mục)
      - [7.6.2. Các Loại Chỉ Mục](#762-các-loại-chỉ-mục)
      - [7.6.3. Cách Tạo và Quản Lý Chỉ Mục](#763-cách-tạo-và-quản-lý-chỉ-mục)
      - [7.6.4. Các cân nhắc khi sử dụng indexes](#764-các-cân-nhắc-khi-sử-dụng-indexes)
      - [7.6.5. Tùy chọn tối ưu indexes](#765-tùy-chọn-tối-ưu-indexes)
- [Module 4](#module-4)
  - [8. Troubleshooting and Automation](#8-troubleshooting-and-automation)
    - [8.1. Trouble shooting common issues](#81-trouble-shooting-common-issues)
    - [8.2. Tool for issue supporting](#82-tool-for-issue-supporting)
    - [8.3. Practical examples](#83-practical-examples)
    - [8.4. Using status variable, error codes, and documentations](#84-using-status-variable-error-codes-and-documentations)
    - [8.5. Giải mã lỗi và sử dụng tài liệu](#85-giải-mã-lỗi-và-sử-dụng-tài-liệu)
    - [8.6. Using logs for troubleshooting](#86-using-logs-for-troubleshooting)
    - [8.7 Configuring and accessing logs](#87-configuring-and-accessing-logs)
    - [8.8. Automating Database tasks](#88-automating-database-tasks)
      - [8.8.1 Automating database](#881-automating-database)
      - [8.8.2. Benefit of automation](#882-benefit-of-automation)
      - [8.8.3. Benefit of scripting automation](#883-benefit-of-scripting-automation)
      - [8.8.4. Tools and methods of automation](#884-tools-and-methods-of-automation)
    - [8.9. Automating Reports and Alerts](#89-automating-reports-and-alerts)
      - [8.9.1. Difference of Reports, Nofitications and Alerts](#891-difference-of-reports-nofitications-and-alerts)
      - [8.9.2. Benefit](#892-benefit)
      - [8.9.3. Automation](#893-automation)
      - [8.10. Hands-on](#810-hands-on)

# Module 1

## 1. Database Life Cycle Management

Vòng đời cơ sở dữ liệu được chia ra làm 4 giai đoạn. 

**Thiết kế phân tích yêu cầu $\to$ Thiết kế và lập kế hoạch triển khai cơ sở dữ liệu $\to$ Xây dựng thực sự $\to$ Giám sát thực tế và duy trì hoạt động thường ngày.**

### 1.1 Thiết kế phân tích yêu cầu

Trong giai đoạn **Thiết kế phân tích yêu cầu**, cần làm việc với các kỹ sư dữ liệu để hiểu mục đích và phạm vi của cơ sở dữ liệu. Cần bàn luận với các người liên quan: *người sử dụng*, *nhà sản xuất dữ liệu*, *phát triển mẫu về cách người dùng sử dụng dữ liệu* dưới dạng báo cáo hoặc dashboards. 

Một số nhiệm vụ có thể làm là: *phân tích nhu cầu về cơ sở dữ liệu, làm rõ mục tiêu mà cơ sở dữ liệu đáp ứng và xác định người dùng của cơ sở dữ liệu*

### 1.2 Thiết kế và lập kế hoạch triển khai cơ sở dữ liệu

Cần lên kế hoạch thiết kế cơ sở dữ liệu, có hai thao tác chính: `Database Modelling`, `Capacity Planning`. 

- Database Modelling: Sử dụng cơ sở nào, làm việc với table ra sao, cách người dùng truy cập được vào csdl.
- Capacity Planning: Xác định tài nguyên máy chủ thích hợp như không gian lưu trữ, sức mạnh của máy chủ. 

Ví dụ: Các DBA có thể chọn lưu trữ thường xuyên dữ liệu đã sử dụng trên mảng đĩa tốc độ cao hoặc chỉ lưu trữ các index riêng biệt từ data để hiệu suất tốt hơn.

### 1.3 Xây dựng thực tế

Trong giai đoạn này, DBA triển khai cơ sở dữ liệu một cách cẩn thận theo kế hoạch. Tạo ra csdl như database, instances, tables, indexes. Sau đó thực hiện cấu hình bảo mật cơ sở dữ liệu, cấp quyền truy cập cho cơ sở dữ liệu: users, groups, roles để csdl chỉ được truy cập bởi những người dùng cụ thể. 

Tự động lặp lại các thao tác *sao lưu, khôi phục và triển khai* để nâng cao hiệu quả.

Làm cho csdl có thể nhập dữ liệu từ csdl khác, xuất dữ liệu dựa trên truy vấn từ một nguồn khác, hoặc di chuyển dự án từ môi trường này đến môi trường khác ví dụ như: *chuyển một dự án từ môi trường Application Development lên môi trường Product*.

### 1.4 Giám sát thực tế và duy trì hoạt động thường ngày

Giám sát hệ thống trong thời gian truy vấn dài và giúp *end-users* tối ưu hóa chúng để chạy nhanh hơn và không tốn quá nhiều tài nguyên hệ thống.

Xem báo cáo.

Giữ cho csdl hoạt động tốt nhất, áp dụng các nâng cấp và bảo mật, ngày càng nâng cấp csdl.

Tự động hóa việc triển khai và công việc thường ngày như là: *sao lưu bất cứ khi nào có thể* để giữ quy trình hoạt động hiệu quả.

Trong mọi csdl, vấn đề vận hành đôi khi phát sinh, cần khắc phục vấn đề khi cần thiết. 

Giữ bảo mật và an toàn cho dữ liệu, thường xuyên thực hiện kiểm tra và đảm bảo người dùng chỉ có thể nhìn thấy những gì được nhìn thấy.


## 2. Database Object

Hệ quản trị cơ sở dữ liệu RDMS chứa nhiều đối tượng mà kỹ sư dữ liệu và DBA phải tổ chức. Lưu trữ tables, contraints, indexes, và các database objects trong cấu trúc phân cấp cho phép các DBA quản lý bảo mật, bảo trì, và khả năng tiếp cận. 

Ví dụ một hệ thống phân cấp. Hầu hết các RDBMS đều bắt đầu với một **instance**, một cách để tổ chức database và mọi thứ mà nó chứa. Nhiều RDBMS cho phép nhiều cơ sở dữ liệu trong một **instance** duy nhất. Nói chung chắc chắn tìm thấy một lược đồ (**schema**) ở mức độ nào đó trong hệ thống phân cấp. Lược đồ thể hiện cách đặt tên các đối tượng trong csdl và ngăn chặn sự *tham chiếu mơ hồ*, trong schema lại có tables, constraints, indexes.

### 2.1 Instance

Một **instance** là ranh giới logic cho cơ sở dữ liệu hoặc tập hợp cơ sở dữ liệu mà bạn tổ chức database object và thiết lập các thông số cấu hình.

Mọi csdl trong một instance đều được chỉ định duy nhất một cái tên, có bộ danh mục hệ thống riêng các bảng (cái mà theo dõi các đối tượng bên trong csdl) và có file cấu hình riêng. Có thể tạo nhiều hơn instance trên cùng một máy chủ vật lý cung cấp 1 cơ sở dữ liệu duy nhất.

Database objects trong một instance được tách biệt hoàn toàn khỏi instance khác. Ví dụ một instance cho Dev và một instance cho Production, với mỗi instance thì quyền hạn sẽ khác nhau.

![Ví dụ instance](instance_exp.png)

Không phải tất cả các RDBMS đều sử dụng khái niệm **instance**, thay vào đó thường xuyên quản lý thông tin cấu hình csdl trong một csdl đặc biệt. 

Trong RDBMS trên nền tảng CLOUD, thuật ngữ **instance** có nghĩa là một bản sao đang chạy cụ thể của một dịch vụ.

### 2.2 Schema

Lược đồ là database object đặc biệt cung cấp cách để nhóm các database object khác một cách logic. Chứa các tables, contraints, indexes và các object khác. Khi tạo một database object có thể gán nó vào schema.

Trong hầu hết RDBMS, lược đồ mặc định là *lược đồ người dùng*, cho người dùng hiện tại đăng nhập. Nhiều RDBMS sử dụng một `lược đồ chuyên dụng (system schema)` để lưu trữ thông tin cấu hình và siêu dữ liệu về một csdl cụ thể. Ví dụ, các bảng trong system schema có thể lưu trữ danh sách người dùng cơ sở dữ liệu và quyền truy cập của họ, thông tin về các chỉ mục trên bảng, chi tiết của bất kỳ phân vùng csdl nào tồn tại và kiểu dữ liệu do người dùng xác định.

### 2.3 Database Object

Là tất cả các mục tồn tại trong csdl. Quá trình thiết kế csdl bao gồm việc xác định các đối tượng cơ sở dữ liệu và mối quan hệ của chúng với nhau.

Có thể tạo và quản lý với tools, scripting và APIs. Nếu dùng SQL để tạo hoặc quản lý db object, thì sử dụng `Data Definition Language` statement (DDL) như CREATE, ALTER. 

Hầu hết các RDBMS, có thể tạo các db object như: *tables, constraints, indexes, keys, views, aliases, events, triggers, logfile*.

- Indexes là tập hợp các con trỏ được sử dụng để cải thiện hiệu suất và đảm bảo tính duy nhất của dữ liệu.
- Keys, khóa xác định duy nhất 1 hàng của 1 table, cho phép xác định quan hệ giữa các bảng.
- Views, Cung cấp một cách khác biểu diễn dữ liệu trong một hoặc nhiều bảng. Một view không có phải là bảng thực tế và yêu cầu không có nơi lưu trữ vĩnh viễn.
- Aliases, bí danh là một tên thay thế cho object như table, kiểu đặt tên cho dễ gọi hơn, ngắn hơn.
- Events, là thao tác dữ liệu `Data Manipulation Language` hay DDL trên một db object mà có thể khởi tạo Trigger.
- Trigger, Là một tập hợp các hành động như INSERT, UPDATE, DELETE trên bảng cụ thể.
- Log file, lưu trữ thông tin về các transaction trong csdl.

## 3. System Objects and Database Configuration

### 3.1 System Objects

RDBMs lưu trữ thông tin về cơ sở dữ liệu của họ, được gọi là **metadata** (siêu dữ liệu), trong một database cụ thể, lược đồ hoặc catalog. Họ lưu trữ các loại thông tin cụ thể về csdl chẳng hạn như tên cơ sở dữ liệu, tables, datatype của column, quyền truy cập được gọi là siêu dữ liệu. Các thuật ngữ khác được dùng cho kho thông tin này là **data dictionary** và **system catalog**. 

RDBMs kiểm soát và cập nhật system object nhưng bạn vẫn có thể truy vấn các metadata tables để khám phá thông tin về các đối tượng trong database. 

#### 3.1.1 Db2 system objects

Db2 sử dụng `catalog` và `directory`. 

- Catalog bao gồm các bảng dữ liệu về mọi thứ được xác định cho hệ thống db2. Khi người dùng CREATE, ALTER, DROP bất kỳ đối tượng nào, Db2 inserts, updates, deletes các hàng của catalog mà mô tả đối tượng đó và nó liên quan đến các đối tượng khác như thế nào.
- Directory chứa Db2 internal control data được Db2 sử dụng trong quá trình hoạt động bình thường của nó. Trong số những thứ khác, Directory chứa database descriptors, access path cho các ứng dụng và thông tin trạng thái tiện ích và khôi phục.

![DB2 system objects](db2_system_objects.png)

#### 3.1.2 MySQL system objects

MySQL sử dụng system schema để lưu trữ cơ sở dữ liệu metadata. Ví dụ mỗi instance MySQL mới có 4 system databases: `information_schema`, `mysql`, `performance_schema`, `sys`. Mỗi một system database đó chứa một số table READ-ONLY.

#### 3.1.3 PostgreSQL system objects

PostgreSQL sử dụng system catalog cái mà là lược đồ với các bảng và views chứa metadata về tất cả các đối tượng khác bên trong database, và hơn thế nữa với nó, bạn có thể khám phá khi nào các hoạt động khác nhau xảy ra, cách tables hay indexes được truy cập và liệu csdl hệ thống có đang đọc thông tin từ bộ nhớ hay cần đọc data từ đĩa cứng. 

### 3.2 Database Configuration

Trong bất kỳ quá trình cài đặt cơ sở dữ liệu nào, bạn cung cấp các tham số như vị trí thư mục dữ liệu, port number mà dịch vụ lắng nghe để kết nối, bộ nhớ, và nhiều hơn nữa. 

Bạn có thể sử dụng tùy chọn mặc định hoặc cung cấp giá trị tùy chỉnh để phù hợp với môi trường. Quá trình cài đặt cơ sở dữ liệu sẽ lưu thông tin này thành một tập tin, được gọi là configuration file (.conf, .cfg) hay initialization file (.ini).

Csdl sử dụng thông tin trong file đó để thiết lập các thông số khi nó khởi động. Các RDBMs khác nhau sử dụng file, vị trí, cài đặt khác nhau. Tuy nhiên đều có chung mục đích là phục vụ cung cấp thông tin cấu hình ban đầu cho csdl khi nó khởi động và vận hành.

Configuration file có thể bao gồm:
-  Location của data files và log files.
-  Port server listen cho các yêu cầu
-  Memury Allocation
-  Connection Timeout
-  Maximum packet size
-  

### 3.3 Example RDBMS configurations

- Db2 sử dụng file `SQLDBCONF`
- MySQL sử dụng `my.ini` hoặc `my.cnf` (tệp ini trên windows và conf trên linux)
- PostgreSQL sử dụng `Postgresql.conf`

### 3.4 How to configure databases

Khi muốn chỉnh sửa file cấu hình, nếu đang sử dụng RDBMS on-premises, hãy
- Dừng database service
- Chỉnh sửa configuration file
- Khởi động lại database service

Nếu sử dụng RDBMS trên CLOUD thì 
- Chọn tùy chọn cấu hình khi tạo cơ sở dữ liệu
- Chỉnh sửa

Lợi thế của Cloud-based RDBMs là có thể mở rộng nhiều tùy chọn cấu hình như kích thước lưu trữ, sức mạnh tính toán thông qua giao diện đồ họa khi dịch vụ đang chạy mà không cần tắt. `Chỉ cần chỉnh tùy chọn không cần chỉnh CONFIGURATION FILE`.

## 4. Database Storage

### 4.1 Plan database storage

Cần chịu trách nhiệm đảm bảo csdl đủ dung lượng lưu trữ, cần xác định dung lượng cần thiết cho csdl và kế hoạch tăng trưởng. Trong csdl đám mây, việc mở rộng bộ nhớ của csdl thông qua giao diện đồ họa hoặc API, cũng chính là một trong những lợi ích của csdl đám mây. 

Trong csdl tự quản lý, có thể thiết lập kế hoạch không gian lưu trữ để cải thiện hiệu suất lưu trữ tài nguyên trên các đĩa khác nhau. RDBMs tách biệt lưu trữ vật lý của các tập tin csdl trên disk từ thiết kế logic của csdl, cho phép linh hoạt hơn trong việc quản lý các tập tin dữ liệu. Bạn có thể quản lý dữ liệu thông qua đối tượng Logic mà không cần quan tâm đến bản chất của bộ nhớ vật lý.

Ví dụ: Bạn có thể tạo một command để backup csdl mà không cần chỉ định tất các đĩa vật lý mà chứa csdl đó.

### 4.2 Tablespaces and Containers

`Tablespaces` là các cấu trúc mà chứa database object như tables, indexes, large objects, và long data. Các DBA sử dụng không gian bảng để tổ chức một cách hợp lý database object dựa trên nơi mà dữ liệu của họ được lưu trữ. `Tablespaces` xác định một ánh xạ logic giữa database object và `database containers`.

Một `database container` có thể là một tập tin dữ liệu, thư mục hay một thiết bị thô. 

Tablespaces có thể chứa (contain) một hoặc nhiều database object. Ví dụ:

![Ví dụ tablespace](tablespace_exp.png)

DBAs cấu hình một hoặc nhiều *vùng lưu trữ* (`database containers`) để lưu trữ từng tablespace. 

### 4.3 Tablespace benefits

Bằng cách sử dụng sự kết hợp của các tablespaces và containers, bạn có thể giữ csdl logic tách biệt khỏi lưu trữ vật lý và quản lý bố cục đĩa của csdl và object của nó. Điều này mang lại một số lợi ích:
- **Performance**: sử dụng tablespace để tối ưu hóa hiệu năng, ví dụ đặt nơi sử dụng nhiều index (truy cập nhiều) trên SSD, và lưu trữ các bảng chứa dữ liệu hiếm khi được truy cập trên ổ cứng rẻ tiền hơn nhưng chậm hơn.
- **Recoverability**: giúp backup và restore tiện lợi hơn, sử dụng một lệnh duy nhất, có thể sao lưu hoặc khôi phục tất cả database objects mà không cần lo lắng về việc cái storage nào mà mỗi object hay tablespace đang được lưu trữ trong đó.
- **Storage management**: RDBMs tạo và mở rộng tệp dữ liệu hay containers dựa trên nhu cầu. Khi cần thiết, có thể mở rộng một cách thủ công bằng cách thêm đường dẫn storage khác hay container vào tablespace.

### 4.4 Storage Group

Một số RDMBs cung cấp Storage Group, một storage group là một nhóm các đường dẫn lưu trữ hoặc containers dựa trên hiệu suất đặc trưng tương tự nhau. Điều này cho phép thực hiện Multi-Temperature Data Management dễ dàng hơn. Trong bối cảnh này, Temperature đề cập đến việc truy cập dữ liệu thường xuyên. 

- **Hot-data**: Dữ liệu được truy cập rất thường xuyên.
- **Warm-data**: Dữ liệu được truy cập tần suất bình thường.
- **Cold-data**: Dữ liệu rất ít khi được truy cập đến.

Từ đó có thể sử dụng storage group để sắp xếp dữ liệu nhằm tối ưu hiệu năng, và giảm chi phí thông qua việc để Cold-data vào đĩa rẻ và chậm hơn.

### 4.5 Data partitions

Csdl quan hệ được phân vùng là một csdl quan hệ có dữ liệu được quản lý trên nhiều phân vùng csdl. Bạn có thể phân vùng các bảng cần chứa số lượng rất lớn dữ liệu thành nhiều phân vùng hợp lý, với mỗi phân vùng chứa một tập con của dữ liệu tổng thể.

Phân vùng csdl được sử dụng trong các tính huống liên quan đến khối lượng dữ liệu rất lớn như data warehousing, data analysis cho doanh nghiệp thông minh. 

[Storage Engine in MySQL](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAyMzFFTi1Ta2lsbHNOZXR3b3JrL1JlYWRpbmdzL0RFOS4yMDAyODJfTXlTUUxfU3RvcmFnZV9FbmdpbmVzLm1kIiwidG9vbF90eXBlIjoiaW5zdHJ1Y3Rpb25hbC1sYWIiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTcxMTQyNTQxNX0.k5fD-0usPNAg_oHh-5heIrqGdMyr6poALY55EniHZMs)

Tóm tắt:

| Engine    | Description                                                                                             |
|-----------|---------------------------------------------------------------------------------------------------------|
| InnoDB    | Là engine lưu trữ mặc định cho MySQL 5.5 trở lên. Phù hợp với hầu hết các kịch bản lưu trữ dữ liệu. Cung cấp các bảng tuân thủ ACID và các ràng buộc toàn vẹn khóa ngoại (FOREIGN KEY). Hỗ trợ khả năng commit, rollback và phục hồi sau sự cố để bảo vệ dữ liệu. Hỗ trợ khóa cấp độ hàng (row-level locking). Lưu trữ dữ liệu trong các chỉ mục cụm (clustered indexes), giảm thiểu I/O cho các truy vấn dựa trên khóa chính (primary keys). |
| MyISAM    | Quản lý các bảng không transaction (non-transactional). Cung cấp tốc độ lưu trữ và truy xuất cao. Hỗ trợ tìm kiếm toàn văn bản (full-text searching). |
| MEMORY    | Cung cấp các bảng trong bộ nhớ, trước đây gọi là HEAP. Lưu trữ tất cả dữ liệu trong RAM để truy cập nhanh hơn so với lưu trữ dữ liệu trên đĩa. Hữu ích cho việc tra cứu nhanh các dữ liệu tham chiếu và dữ liệu giống nhau. |
| MERGE     | Xem các nhóm bảng MyISAM tương tự như một bảng duy nhất. Xử lý các bảng không transaction. |
| EXAMPLE   | Cho phép các nhà phát triển thực hành tạo một engine lưu trữ mới. Cho phép các nhà phát triển tạo bảng. Không lưu trữ hoặc lấy dữ liệu. |
| ARCHIVE   | Lưu trữ một lượng lớn dữ liệu. Không hỗ trợ các chỉ mục. |
| CSV       | Lưu trữ dữ liệu theo định dạng Comma Separated Value trong một tệp văn bản. |
| BLACKHOLE | Chấp nhận dữ liệu để lưu trữ nhưng luôn trả về kết quả rỗng. |
| FEDERATED | Lưu trữ dữ liệu trong một cơ sở dữ liệu từ xa. |


### 4.6. Commands for working with Storage Engines

**SHOW ENGINES**

```shell
mysql> SHOW ENGINES;
```

**CREATE TABLE WITH SPECIFIC ENGINE**

```SQL
CREATE TABLE Products (i INT) ENGINE = INNODB;
```

```SQL
CREATE TABLE Product_Codes (i INT) ENGINE = CSV;
```

```SQL
CREATE TABLE History (i INT) ENGINE = MEMORY;
```

Nếu không nêu ENGINE cụ thể thì mặc định sẽ là **InnoDB**

**SET**

Ta có thể chỉ ra ENGINE mặc định bằng cách sau:

```SQL
SET defaut_storage_engine=<engine_name>
```

**ALTER**

Có thể thay đổi ENGINE

```SQL
ALTER TABLE Products ENGINE = <engine_name>;
```

Note: **InnoDB** phù hợp với hầu hết các nhu cầu lưu trữ dữ liệu.

### 4.7. Postgre CLI

**CONFIGURATION**

Dùng `\i <file_name>` để chạy file SQL. và `\dt` để xem các database nào có trong postgreSQL.

PostgreSQL có configuration file là `postgresql.conf`.

Khi điều chỉnh các thay đổi về cấu hình trong postgresql thì nó sẽ tự tạo một file tên là `postgresql.auto.conf` để khi khởi động lại sever thì nó sẽ tự động đọc file này và thay đổi cấu hình.

Có thể sử dụng 

```SQL
ALTER SYSTEM SET <system_parameter> = <value>;
```

hoặc chỉnh sửa trực tiếp trong file `postgresql.conf`.

**CONNECTION**

Sử dụng lệnh `\connect <db_name>` để kết nối tới database mong muốn.

# Module 2

## 5. Backup and Restore

Thường quá trình backup và restore sẽ được diễn ra khi cần chuyển tất cả dữ liệu từ csdl này sang csdl khác. Điều này nhằm tạo điều kiện thuận lợi cho việc thay đổi RDBMs để chia sẽ dữ liệu hoặc tải dữ liệu từ một doanh nghiệp đối tác, hoặc để tạo bản sao của dữ liệu cho việc sử dụng ở một vị trí khác hay một hệ thống khác. Ví dụ như: **development** hay **test**.

### 5.1. Physical vs logical backups

#### 5.1.1. Logical backup

- Là một bản lưu trữ DDL và DML commands như lệnh tạo bảng, và insert để tạo lại các đối tượng và dữ liệu trong csdl. Vậy có thể sử dụng file này để tạo lại csdl trên cùng một hệ thống hoặc hệ thống khác.
- Có thể lấy lại được không gian lưu trữ bị lãng phí từ csdl gốc vì quá trình khôi phục tạo ra một phiên bản clean của tables. Tạo logical backup có thể `mất nhiều thời gian dành cho csdl lớn` và có thể `ảnh hưởng đến hiệu suất của các truy vấn mà đang chạy`.
- Cho phép `sao lưu chi tiết` (granular). Ví dụ: có thể sao lưu một bảng hay một csdl đơn lẻ, tuy nhiên không thể sử dụng nó để sao lưu `configuration file` và `log file`.
- Thường dùng `import, export, dump, load utilities` để thực hiện logical backup.

#### 5.1.2. Physical backup

- Là bản sao của file vật lý, `bao gồm cả log file và configuration file`.
- Thường nhỏ hơn và nhanh hơn logical backup, hữu ích cho csdl lớn hoặc quan trọng đòi hỏi thời gian recovery nhanh. Nó tương tự như sao lưu bất kỳ loại file nào trên hệ thống của bạn.
- Tuy nhiên, không dễ dàng khôi phục các bảng hoặc database object riêng lẻ nếu file chứa nhiều hơn một đối tượng.
- `Chỉ có thể backup và recovery cho RDBMS tương tự`.

### 5.2. Những gì có thể backup

Toàn bộ database, nội dung của schema, một hay nhiều tables từ database, một tập hợp con của dữ liệu từ một hoặc nhiều bảng của database, hay một tập hợp các đối tượng khác trong database.

### 5.3. Key considerations

Khi sử dụng sao lưu và khôi phục cần nhớ kiểm tra xem backup file của bạn hay các files có hợp lệ hay không để có thể restore thành công.

Chắc chắn rằng đảm bảo an toàn cho quá trình chuyển đổi và vị trí của file backup.

### 5.4. Backup options

Khi thực hiện sao lưu, một số RDBMS hỗ trợ các tùy chọn bổ sung mà có thể sử dụng là:

- Compression: giảm size cho việc lưu trữ và vận chuyển đi, nhưng làm tăng thời gian backup và restore.
- Encryption: Mã hóa bản sao lưu, giảm nguy cơ bất kỳ dữ liệu nào xâm phạm, nhưng vẫn làm tăng thời gian backup và restore.

### 5.5. Types of backup

Thường dùng:
- Full backup
- Point-in-time backup
- Differential backup
- Incremental backup

#### 5.5.1. Full backup

Sao lưu toàn bộ dữ liệu, tất cả các object database. Việc thực hiện full backup giúp đơn giản hóa quá trình khôi phục vì bạn chỉ cần xác định vị trí của bản backup và khôi phục nó. Tuy nhiên kích thước csdl tăng thì bản full backup cũng tăng làm tăng thời gian, băng thông và dung lượng tăng.

Nếu quyết định giữ lại cả những bản sao trước đó của backup để đảm bảo an toàn thì nó sẽ tốn rất nhiều dung lượng. Tuy nhiên nếu chỉ giữ lại đúng 1 file backup thì phải chấp nhận rủi ro rằng nó sẽ biến mất (bằng cách nào đó).

#### 5.5.2. Point-in-time backup

Khi khôi phục csdl từ full backup thì trong thời gian khôi phục đó, có thể đã có rất nhiều transaction xảy ra, nên lý tưởng nhất là các transaction đó cũng nên được khôi phục luôn.

Một cách giải quyết vấn đề này là kích hoạt tính năng ghi nhật ký (logging) của mỗi transaction đã xảy ra trên csdl và sau đó sử dụng thông tin trong file log để khôi phục các transaction. Quá trình áp dụng lại các transaction sau khi restoring dữ liệu được gọi là recovery, cho phép khôi phục dữ liệu về trạng khái tại một điểm cụ thể.

#### 5.5.3. Differential backup

Bởi vì fullbackup tốn rất nhiều tg, băng thông, và dung lượng nên một cách thay thế là sử dụng chúng kết hợp với differential backup.

Một bản differential backup bao gồm các bản sao của bất kỳ dữ liệu nào đã thay đổi kể từ lần full backup gần nhất đã được sao lưu. Điều này làm bản differential backup nhỏ hơn rất nhiều so với một full backup, giảm tốn băng thông, thời gian, dung lượng cần thiết cho sao lưu trong khi vẫn cho phép chúng ta khôi phục bình thường. 

Ví dụ: Có thể thực hiện full backup mỗi tuần vào ngày chủ nhật sau đó chạy differential backup mỗi ngày trong tuần, mỗi bản differential backup chứa những sự thay đổi kể từ lần fullbackup gần nhất, vậy nếu cần khôi phục dữ liệu vào ngày thứ 3 thì chỉ cần chạy khôi phục từ file full backup ngày chủ nhật và file differential backup thứ 3, không cần phải chạy differential backup thứ 2 vì mọi sự thay đổi của file đó cũng có trong thứ 3.

#### 5.5.4. Incremental backup

Tương tự như differential backup, nhưng chúng chỉ chứa những dữ liệu mà đã thay đổi từ bất kỳ lần sao lưu cuối cùng nào (bất kỳ loại backup nào). 

Ví dụ: Mỗi tuần chạy full backup vào chủ nhật, và mỗi ngày chạy incremental backup, thì mỗi file incremental backup chỉ chứa các thay đổi full backup đã chạy vào chủ nhật. Nên nếu muốn khôi phục dữ liệu vào ngày thứ 3 thì mình cần khôi phục file full backup, sau đó incremental thứ 2, cuối cùng là incremental thứ 3.

### 5.6. Backup Policies

#### 5.6.1. Hot Backup

Được thực hiện khi dữ liệu được trong trạng thái được sử dụng. Ưu điểm: Không ảnh hưởng đến tính khả dụng và người dùng có thể tiếp tục các hoạt động của họ trong quá trình sao lưu. Tuy nhiên có thể dẫn đến hiệu suất xuống cấp cho người dùng trong khi quá trình sao lưu đang được thực hiện và có thể ảnh hưởng đến tính vẹn toàn của dữ liệu.

Cách thay thế cho hot backup là stop csdl trong khi quá trình sao lưu đang chạy, nó được gọi là Cold backup

#### 5.6.2. Cold backup

Loại bỏ rủi ro về tính vẹn toàn dữ liệu liên quan đến hot backup, nhưng nó có tác động lớn hơn vào tính khả dụng của người dùng, và sẽ không sử dụng được trong môi trường 24/7. 

#### 5.6.3. Hot and Cold

Các bản hot backup thường được lưu trữ trên một máy chủ có sẵn và thường được cập nhật từ production database. Điều này cho phép chúng được đưa lên online nếu production server bị lỗi, để đảm bảo trải nghiệm người dùng.

Các bản cold backup thường được lưu trữ vào ổ đĩa cứng hoặc trên server mà đã được shutdown trong hoạt động sao lưu. Điều này mang lại sự an toàn dữ liệu cao hơn, nhưng không có nghĩa là quá trình phục hồi sẽ lâu hơn so với hot backup.

### 5.7 Using Database transaction logs for recovery

#### 5.7.1. Khái niệm và ví dụ

Chứa thay đổi của transaction và chỉnh sửa database, thông tin được lưu trữ trong log có thể được dùng cho quá trình phục hồi khi dữ liệu vô tính bị xóa hay lỗi gì đó, cũng có thể đóng vai trò là một backup file tại một thời điểm cụ thể.

![Transaction log example](transaction_log_exp.png)

Ví dụ trên:
- T1: thực hiện sao lưu toàn bộ csdl, trong thời gian T1 đến T2 đã có xảy ra transaction và được lưu vào logs.
- T2: máy chủ bị sự cố
- T3: khôi phục từ T1
- T4: áp dụng transaction lúc giữa T1 và T2

Ví dụ trên được gọi là `roll forward recovery`.

#### 5.7.2. Storing transaction log files

- Db2: sqlogdir
- PostgreSQL: pg_xlog, các transaction được lưu trong write-ahead log (WAL).

Một phương pháp hay được đề xuất trong thực tiễn là: ít nhất là cho production database, đặt transaction log files trên các ổ đĩa lưu trữ riêng biệt từ các database object như tablespaces.

Nó không chỉ giúp về hiệu suất, mà còn để csdl không ghi xung đột, với tăng hiệu quả khôi phục vì lỡ crash máy hay bay server thì vẫn còn file log giữ được.

#### 5.7.3. Accessing transaction log files

Logging thường mặc định không được bật, nhưng vẫn có thể tùy chỉnh cài đặt bình thường. Thường các log file sẽ được mã hóa nhị phân.

- Mysql: `SHOW BINARY LOG;` $\to$ `mysqlbinlog -v DB_Bin_Logs.000001`
- Db2: `db2fmtlog S0000002.LOG -replayonlywindow`


#### 5.7.3. Lab with PostreSQL

Dataset: `wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/example-guided-project/flights_RUSSIA_small.sql`

Load data với `\i flights_RUSSIA_small.sql`

Làm việc với table `aircrafts_data`, giả sử cần thêm vào máy bay **Airbus A380** với range 15,700 km và code là 380.

```SQL
INSERT INTO aircrafts_data(aircraft_code, model, range) VALUES (380, '{"en": "Airbus A380-800"}', 15700);
```

Bắt đầu thực hiện backup với pgAdmin

Bấm `\q` để thoát ra khỏi postreSQL

Đơn giản chỉ cần vào GUI và tạo file backup

[Hướng dẫn](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAyMzFFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvUG9zdGdyZVNRTC9MYWIlMjAtJTIwQmFja3VwJTIwYW5kJTIwUmVzdG9yZSUyMHVzaW5nJTIwUG9zdGdyZVNRTC9CYWNrdXBfUmVzdG9yZV9wb3N0Z3JlU1FMLm1kIiwidG9vbF90eXBlIjoidGhlaWFkb2NrZXIiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTcyMTM3ODA5NX0.e0MC8fTNTfgIg_nrPjwMbZjirvv7POlUKSizKqL_-wA)

#### 5.7.3. Lab with MySQL

[Hướng dẫn](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAyMzFFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvTXlTUUwvTGFiJTIwLSUyMEJhY2t1cCUyMGFuZCUyMFJlc3RvcmUlMjB1c2luZyUyME15U1FML2luc3RydWN0aW9uYWwtbGFicy5tZCIsInRvb2xfdHlwZSI6InRoZWlhZG9ja2VyIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE3MjEzNzgzNzZ9.bxYDzDDAZplZHwAW9ltdTL2f1qou2KDgVzA_whYqiQ4)

#### 5.7.4. Perform Point-in-Time Backup and Restore

[Hướng dẫn](https://www.coursera.org/learn/relational-database-administration/ungradedWidget/LgMns/reading-perform-point-in-time-backup-and-restore)

#### 5.7.5. Performing MySQL Physical Backup and Restoration

[Hướng dẫn](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL2cxWWZYQmdJQlNFbUd6ZS03OWNCOUEvUGh5c2ljYWwtQmFja3Vwcy12MS5tZCIsInRvb2xfdHlwZSI6Imluc3RydWN0aW9uYWwtbGFiIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE3MTQ3MTE0NjZ9.6jPFjGfFc3kNTZGvsR9-Joz1w0ZQgnmF759sQxMb60s)

# Module 3

## 6. Monitoring and Optimization

### 6.1. Database monitoring

Một trong những điều quan trọng nhất là điều chỉnh hiệu suất của hệ thống (performance tuning) và một phần nữa chính là database monitoring (giám sát csdl)

Thuật ngữ database monitoring đề cập đến việc kiểm tra các task khác nhau liên quan đến việc kiểm tra về tình trạng hoạt động hàng ngày của csdl. Là một phần thiết yếu để duy trì hiệu suất của csdl. Khi thực hiện giám sát cơ sở dữ liệu thường xuyên sẽ giúp xác định các vấn đề một cách kịp thời, để có thể duy trì hiệu năng và khả năng truy cập csdl. 

Nếu không thực hiện database monitoring, những sự cố nghiệm trọng trong csdl có thể không bị phát hiện kịp thời. Hầu hết các RDBMS đều cung cấp chức năng database monitoring cho phép quan sát trạng thái hiện tại của dữ liệu và để theo dõi hiệu suất mọi lúc.

### 6.2. Database monitoring tasks

- Dự báo trước yêu cầu về phần cứng, ví dụ như không gian lưu trữ cần thiết dựa trên csdl.
- Phân tích hiệu suất của từng application hay những câu truy vấn csdl.
- Theo dỏi việc sử dụng của indexes và tables.
- Xác định nguyên nhân gốc rễ của bất kỳ sự suy thoái hiệu suất hệ thống nào.
- Tối ưu hóa (optimizing) các thành phần của csdl để cung cấp hiệu suất tốt nhất có thể.
- Đánh giá các tác động đến từ các sự tối ưu hóa trên.

### 6.3. Reactive monitoring

Reactive monitoring được thực hiện sau khi sự cố xảy ra, khi bạn đối mặt với vấn đề đó. Có thể là bằng cách sửa chữa configuration setting hay thêm nhiều tài nguyên hơn.

Các tình huống phố biến nhất khi reactive monitoring xảy ra là khi sự bảo mật của csdl bị xâm phạm, hay hiệu suất csdl đạt mức cực thấp hoặc một số loại sự cố csdl xảy ra mà ảnh hưởng nghiêm trọng đến doanh nghiệp của mình.

### 6.4. Proactive Monitoring

Ngược lại hoàn toàn với reactive monitoring, proactive monitoring tìm cách ngăn chặn một cơn hỏa hoạn ngay từ lúc nó còn là một đám cháy nhỏ. Điều này đạt được bằng cách quan sát cụ thể số liệu từ csdl sau đó gửi cảnh báo cho các bộ phận đảm nhiệm nếu các giá trị trong các số liệu đó bắt đầu trở nên bất thường.

Thường sử dụng tự động các quy trình để thực hiện các tasks như thường xuyên xác minh rằng hệ thống csdl có đang trực tuyến và truy cập được, xác minh nhưng thay đổi cấu hình không ảnh hưởng xấu đến hiệu suất của hệ thống, và csdl đang vận hành và hoạt động ở mức độ chấp nhận được.

Cách monitoring này phổ biến hơn và được tin dùng hơn.

### 6.5. Establish a performance baseline

Để xác định xem liệu csdl của mình đang hoạt động ở mức tối ưu nhất hay không thì trước tiên cần thiết lập một baseline cho hiệu suất csdl hệ thống. Để đạt được điều này cần ghi lại số liệu **key performance** đều đặn trong một khoảng thời gian nhất định. Khi đã thiết lập được một **db system performance baseline**, sau đó có thể so sánh những số liệu thống kê này với hiệu suất của csdl tại bất kỳ thời điểm nào.

Nếu sự so sánh trên chỉ ra được rằng hiệu suất hiện tại đang thực sự trên hoặc thực sự dưới đường baseline, thì đó có thể là những mục tiêu tiềm năng cho sự phân tích và điều tra. Sau khi phân tích xong, có thể xác định rằng một số thành phần csdl cần cấu hình lại hoặc tối ưu hóa.

Ngay cả khi hệ thống đã hoạt động ổn định thì vẫn có thể sử dụng performance baseline để xác định **operational norms**:
- Giờ hoạt động cao điểm và thấp điểm của quá trình vận hành
- Thời gian phản hồi của các truy vấn đang chạy và các lệnh xử lý hàng loạt.
- Thời gian cần thực hiện để sao lưu và khôi phục dữ liệu.

### 6.6. Baseline data (các thứ có thể ảnh hưởng đến hiệu suất)

- Tài nguyên phần cứng
- Kiến trúc mạng
- Hệ điều hành
- Database applications
- Client applications

### 6.7. Database monitoring options

Có hai cách để giám sát hoạt động csdl: 
- Point-in-time (manual): Xem thông tin hiển thị trạng thái các thành phần csdl trong real time bằng cách sử dụng table function, sử dụng table function nó lightweight, high-speed monitoring infrastructure.
- Historical (automated): Thiết lập một lịch trình một cách cụ thể, ghi lại thông tin của hoạt động csdl khi một sự kiện gì đó xảy ra, ví dụ như hiệu năng đạt đến ngưỡng nào đó thì tự động ghi lại thông tin csdl, ...

## 7. Monitoring usage and performance

Cần sử dụng các công cụ phù hợp để giám sát csdl và hiệu suất của nó một cách hiệu quả, nhưng bất kể sử dụng công cụ giám sát nào thì thông tin liên quan được thu thập thông qua các chỉ số hiệu suất chính (key performance indicators - KPIs), thường được gọi là **metrics** (chỉ số). Hiệu suất cơ sở dữ liệu được đo lường bằng cách sử dụng các chỉ số hiệu suất cơ sở dữ liệu chính này, giúp tối ưu hóa csdl để đạt được hiệu suất tốt nhất. 

Ngoài việc giám sát vì lí do **hiệu suất**, việc giám sát thường xuyên cũng hữu ích cho các mục đích **vận hành**, **khả dụng** và **bảo mật**. Mục tiêu cuối cùng của giám sát là xác định và ngăn chặn các vấn đề gây ảnh hưởng xấu đến hiệu suất cơ sở dữ liệu. Tuy nhiên, một số vấn đề có thể do phần cứng, phần mềm, kết nối mạng, các truy vấn mà bạn thực thi, hoặc một số yếu tố khác gây ra. Do đó, để giám sát việc sử dụng và hiệu suất của cơ sở dữ liệu một cách hiệu quả và thành công, bạn cần giám sát ở một số cấp độ riêng biệt trong môi trường cơ sở dữ liệu của mình.

### 7.1. Levels of monitoring

Có bốn cấp độ giám sát: Cấp độ hạ tầng, cấp độ nền tảng (hoặc cấp độ instance), cấp độ truy vấn và cấp độ người dùng (hoặc cấp độ phiên).

#### 7.1.1. Infrastructure level

Đây là cấp độ đầu tiên. Điều quan trọng là tất cả các thành phần hạ tầng cơ sở như hệ điều hành, máy chủ, phần cứng lưu trữ và các thành phần mạng phải hoạt động hiệu quả để hỗ trợ nền tảng cơ sở dữ liệu và các truy vấn.

#### 7.1.2. Instance (RDBMS) level

 Cho dù bạn đang xử lý các hệ thống cơ sở dữ liệu quan hệ như Db2, PostgreSQL, MySQL hay bất kỳ loại hệ thống cơ sở dữ liệu quan hệ nào khác, hoặc nếu bạn đang quản lý sự kết hợp của nhiều loại cơ sở dữ liệu, mỗi nền tảng đều cần được xem xét về hiệu suất. Giám sát cơ sở dữ liệu ở cấp độ nền tảng là điều cần thiết vì nó cung cấp cái nhìn toàn diện về tất cả các yếu tố cần thiết để duy trì hiệu suất cơ sở dữ liệu ổn định.

 #### 7.1.3. Query level

 Thông thường, các ứng dụng của doanh nghiệp sẽ liên tục chạy các truy vấn đối với các instance cơ sở dữ liệu của bạn và sau đó định dạng và trả về kết quả liên quan của các truy vấn đó cho người dùng của bạn. Phần lớn các nút thắt cổ chai xảy ra ở cấp độ này chủ yếu là do các câu lệnh truy vấn không hiệu quả, có thể gây ra độ trễ, xử lý lỗi không tốt và làm giảm thông lượng và độ đồng thời của truy vấn.

 #### 7.1.4. User level

 Cấp độ này thường có thể gây hiểu lầm nhất trong tất cả các cấp độ giám sát. Bởi vì nếu người dùng của bạn đang phàn nàn về một vấn đề nào đó không hoạt động, thì bạn có thể thu thập thêm thông tin về vấn đề họ gặp phải, điều tra và hy vọng sửa chữa nó.

 Nhưng điều gì sẽ xảy ra nếu người dùng của bạn hiện không phàn nàn về bất cứ điều gì? Bạn có thể cho rằng mọi thứ đang hoạt động tốt và thư giãn không? Thật không may là không. Chỉ vì không có vấn đề xảy ra ngay bây giờ, không có nghĩa là sẽ không có vấn đề trong tương lai gần. 
 
 **Giám sát thành công thực sự có nghĩa là bạn phải liên tục giám sát việc sử dụng, hiệu suất và hành vi của hệ thống cơ sở dữ liệu một cách chủ động và liên tục**. "Nirvana" của giám sát cơ sở dữ liệu đạt được khi bạn chủ động xác định các vấn đề trước khi người dùng của bạn nhận thức được chúng.

 ### 7.2. Typical Metrics

 Một số chỉ số chính để giám sát việc sử dụng và hiệu suất của cơ sở dữ liệu bao gồm:

 - **Thông lượng cơ sở dữ liệu (Database throughput)**: Đây là một trong những chỉ số quan trọng nhất về hiệu suất cơ sở dữ liệu. Nó chỉ ra khối lượng công việc tổng thể mà cơ sở dữ liệu của bạn đang xử lý và thường được đo bằng số lượng truy vấn được thực thi mỗi giây.
 - **Sử dụng tài nguyên cơ sở dữ liệu (Database resource usage)**: Giám sát việc sử dụng tài nguyên cơ sở dữ liệu bằng cách đo lường CPU, bộ nhớ, không gian log và dung lượng lưu trữ. Chỉ số này thể hiện việc sử dụng tài nguyên cơ sở dữ liệu thông qua hai khía cạnh: số trung bình/tối đa/mới nhất và dữ liệu theo chuỗi thời gian.
 - **Khả dụng cơ sở dữ liệu (Database availability)**: Cho biết cơ sở dữ liệu có hoạt động hay không, tức là có khả dụng hay không.
 - **Khả năng phản hồi cơ sở dữ liệu (Database responsiveness)**: Cho biết hệ thống phản hồi tốt như thế nào đối với các yêu cầu từ bên ngoài. Đây là một trong những chỉ số hiệu suất cơ sở dữ liệu phổ biến và cung cấp thông tin cho các DBA về thời gian phản hồi trung bình cho mỗi truy vấn.
 - **Cạnh tranh cơ sở dữ liệu (Database contention)**: Đo lường việc chờ đợi khóa và các kết nối đồng thời vào cơ sở dữ liệu để xác định có sự cạnh tranh giữa các kết nối hay không. Điều này xảy ra khi nhiều quy trình cùng cạnh tranh để truy cập vào cùng một tài nguyên cơ sở dữ liệu.
 - **Đơn vị công việc (Units of work)**: Theo dõi các giao dịch đang tiêu tốn nhiều tài nguyên nhất trên máy chủ cơ sở dữ liệu.

### 7.3. Others metrics

- **Kết nối (Connections)**: Hiển thị thông tin về các kết nối mạng đến hệ thống quản lý cơ sở dữ liệu và có thể chỉ ra máy chủ có nguy cơ gặp lỗi do các truy vấn dài hoặc quá nhiều kết nối mở.
- **Truy vấn thường xuyên nhất (Most frequent queries)**: Theo dõi các truy vấn thường xuyên nhất và thời gian xử lý trung bình để các DBA tối ưu hóa.
- **Đối tượng bị khóa (Locked objects)**: Cung cấp thông tin chi tiết về các quy trình bị khóa và quy trình đã chặn chúng.
- **Thủ tục lưu trữ (Stored procedures)**: Hiển thị số liệu tổng hợp cho các thủ tục và hàm biên dịch đã được kích hoạt kể từ khi cơ sở dữ liệu được kích hoạt.
- **Bộ đệm (Buffer pools)**: Theo dõi việc sử dụng bộ đệm và không gian bảng (table space), cải thiện hiệu suất cơ sở dữ liệu bằng cách lưu trữ dữ liệu trong bộ nhớ đệm.

### 7.4. Tool for view listed metrics

Để xem các chỉ số này, bạn sẽ sử dụng các công cụ khác nhau tùy thuộc vào cơ sở dữ liệu của mình. Ví dụ:

- Trong `Db2`, bạn có thể sử dụng `Db2 Data Management Console, workload manager, và snapshot monitors.`
- Trong `PostgreSQL`, bạn có thể sử dụng bảng điều khiển `pgAdmin`.
- Trong `MySQL`, bạn có thể sử dụng `Performance Dashboard, Performance Reports, và Query Statistics từ MySQL Workbench, và MySQL Query Profiler` để xác định các truy vấn chạy chậm.

Ngoài ra, còn có các công cụ từ bên thứ ba để giám sát truy vấn, tối ưu hóa hiệu suất và tăng tốc cơ sở dữ liệu, ví dụ:

- **pganalyze**: Dành cho PostgreSQL, cung cấp thông tin chi tiết tự động về các kế hoạch truy vấn, phân tích cơ sở dữ liệu và giám sát hiệu suất.
- **PRTG Network Monitor**: Giám sát truy vấn cho PostgreSQL, MySQL, SQL Server hoặc Oracle.
- **SolarWinds**: Cung cấp giải pháp giám sát hiệu suất cơ sở dữ liệu qua đăng ký.
- **Foglight** của Quest: Giám sát toàn bộ môi trường cơ sở dữ liệu của bạn trong một giao diện duy nhất.
- **Datadog**: Là một nền tảng SaaS (Software as a Service) bao gồm nhiều công cụ giám sát hệ thống và có hơn 450 tích hợp sẵn.

### 7.5. Optimizing Database

Tối ưu hóa cơ sở dữ liệu là một phần thiết yếu trong việc duy trì hiệu suất ổn định của hệ thống. Khi cơ sở dữ liệu phát triển về dung lượng và mức độ phức tạp của các tác vụ vận hành, việc lưu trữ dữ liệu có thể bị phân mảnh, các bảng bị bỏ trống một phần, hoặc hiệu suất tổng thể bị suy giảm. Điều này dẫn đến tốc độ phản hồi chậm và ảnh hưởng đến trải nghiệm của người dùng. Việc tối ưu hóa cơ sở dữ liệu giúp giải quyết những vấn đề này, bằng cách xác định các điểm tắc nghẽn, tinh chỉnh các truy vấn và cải thiện đáng kể thời gian phản hồi.

#### 7.5.1. MySQL

Trong MySQL, cơ sở dữ liệu có thể bị phân mảnh do các hoạt động thêm, cập nhật và xóa. Điều này dẫn đến việc lãng phí không gian lưu trữ và làm giảm hiệu suất truy cập dữ liệu. Để khắc phục tình trạng này, lệnh `OPTIMIZE TABLE` được sử dụng để sắp xếp lại cấu trúc lưu trữ vật lý của bảng và các chỉ mục liên quan. Lệnh này giúp giảm không gian lưu trữ bị lãng phí và cải thiện hiệu quả nhập/xuất dữ liệu. Khi sử dụng lệnh này, bạn cần có quyền SELECT và INSERT đối với bảng mà bạn muốn tối ưu hóa.

Ngoài ra, bạn có thể sử dụng các công cụ đồ họa như phpMyAdmin để tối ưu hóa bảng một cách dễ dàng hơn. Nếu bạn muốn sử dụng công cụ đồ họa như phpMyAdmin để tối ưu hóa, bạn chỉ cần chọn bảng trong giao diện và nhấn vào tùy chọn "Optimize Table".

Ví dụ:

```SQL
OPTIMIZE TABLE employees;
```

Hay có thể optimize nhiều tables cùng lúc:

```SQL
OPTIMIZE TABLE employees, departments, salaries;
```

#### 7.5.2. PostgreSQL

Trong PostgreSQL, lệnh `VACUUM` được sử dụng để thực hiện thu hồi không gian bị lãng phí từ các bản ghi đã bị xóa hoặc không còn sử dụng. Những bản ghi này không được loại bỏ vật lý khỏi bảng sau khi bị xóa hoặc thay thế, dẫn đến mất mát không gian lưu trữ. Những bản ghi này không được loại bỏ vật lý khỏi bảng sau khi bị xóa hoặc thay thế, dẫn đến mất mát không gian lưu trữ. VACUUM giúp giải phóng không gian và cải thiện hiệu suất hệ thống. PostgreSQL cũng có tính năng autovacuum tự động thực hiện quá trình bảo trì này nếu được kích hoạt.

Ví dụ:

**VỀ VACUUM**

Nếu chỉ thực hiện lệnh VACUUM thì sẽ thu hồi không gian trống cho tất cả các bảng trong cơ sở dữ liệu, nhưng sẽ không khóa bảng.

```SQL
VACUUM;
```
Thu hồi không gian cho một bảng cụ thể bằng cách chỉ định tên bảng.

```SQL
VACUUM employees;
```

Lệnh `VACUUM FULL` sẽ tạo ra một bản sao của bảng, sau đó sắp xếp lại toàn bộ dữ liệu mà không còn chứa không gian trống nào. Tuy nhiên, lệnh này yêu cầu khóa toàn bộ bảng trong quá trình thực hiện và mất nhiều thời gian hơn

```SQL
VACUUM FULL employees;
```

**VỀ autovacuum**

Tính năng `autovacuum` tự động chạy trong PostgreSQL và giúp tự động hóa quy trình `VACUUM` mà không cần DBA phải thực hiện thủ công. Mặc định, tính năng này đã được bật và sẽ tự chạy khi bảng đạt đến một số lượng bản ghi chết nhất định.

Cấu hình của `autovacuum` có thể được điều chỉnh trong file cấu hình PostgreSQL (postgresql.conf). Ví dụ, bạn có thể điều chỉnh khoảng thời gian giữa các lần chạy autovacuum như sau (trong file config):

```conf
autovacuum_naptime = 1min
```

Xem trạng thái **autovacuum**: 

```SQL
SELECT relname, last_autovacuum, n_dead_tup, n_live_tup 
FROM pg_stat_all_tables 
WHERE schemaname = 'public';
```

Lệnh trên sẽ trả về thông tin về thời điểm chạy autovacuum gần nhất và số lượng bản ghi chết (n_dead_tup) và bản ghi sống (n_live_tup) trong mỗi bảng.

**VỀ REINDEX**

Ngoài ra, PostgreSQL cung cấp lệnh REINDEX để xây dựng lại các chỉ mục bị lỗi hoặc bị phình to do chứa nhiều trang trống. Quá trình này tương tự như việc xóa và tái tạo lại chỉ mục nhưng có ưu điểm về cách xử lý khóa đọc và ghi, giúp tối ưu hóa cơ sở dữ liệu mà không làm gián đoạn nhiều.

Bạn có thể xây dựng lại một chỉ mục cụ thể trên bảng. Giả sử bạn có một chỉ mục tên là emp_idx trên bảng employees, bạn có thể sử dụng lệnh sau để xây dựng lại chỉ mục đó:

```SQL
REINDEX INDEX emp_idx;
```

Để xây dựng lại tất cả các chỉ mục trên bảng employees, bạn có thể sử dụng lệnh sau:

```SQL
REINDEX TABLE employees;
```

Nếu bạn muốn xây dựng lại tất cả các chỉ mục trên toàn bộ cơ sở dữ liệu, bạn có thể chạy lệnh:

```SQL
REINDEX DATABASE mydatabase;
```

Nếu bạn muốn chỉ định một schema cụ thể, ví dụ như schema public, bạn có thể sử dụng lệnh sau:

```SQL
REINDEX SCHEMA public;
```

**Khi nào cần sử dụng REINDEX?**

- Khi chỉ mục bị hỏng do lỗi phần cứng hoặc phần mềm.
- Khi chỉ mục trở nên phân mảnh và chiếm quá nhiều không gian.
- Sau một thời gian dài mà cơ sở dữ liệu có nhiều cập nhật, xóa bỏ khiến chỉ mục kém hiệu quả.
- 
**Lưu ý khi sử dụng REINDEX:**
- Trong quá trình `REINDEX`, các chỉ mục sẽ tạm thời không có sẵn để sử dụng, vì vậy các truy vấn cần sử dụng chỉ mục đó có thể bị ảnh hưởng về hiệu suất.
- Lệnh `REINDEX` sẽ khóa bảng hoặc chỉ mục mà nó đang xử lý, do đó cần lên kế hoạch để tránh gián đoạn hệ thống nếu cơ sở dữ liệu đang chạy với khối lượng công việc lớn.

### 7.6. Using Indexes

#### 7.6.1. Tại Sao Cần Sử Dụng Chỉ Mục?

Chỉ mục trong cơ sở dữ liệu giống như chỉ mục trong sách. Nó giúp tìm kiếm dữ liệu nhanh hơn mà không cần quét toàn bộ cơ sở dữ liệu. Chỉ mục là một bản sao có thứ tự của các cột dữ liệu trong bảng, giúp tăng tốc độ truy vấn bằng cách tạo các liên kết tới các hàng gốc trong bảng.

#### 7.6.2. Các Loại Chỉ Mục

- `Chỉ Mục Chính (Primary Key Index)`: Là loại chỉ mục đặc biệt, luôn là duy nhất và không thể có giá trị null. Nó sắp xếp dữ liệu trong bảng theo thứ tự của chỉ mục. Mỗi bảng chỉ có thể có một chỉ mục chính.
- `Chỉ Mục Phụ (Secondary Index)`: Có thể có nhiều chỉ mục phụ trên một bảng, không nhất thiết phải là duy nhất và có thể bao gồm một hoặc nhiều cột. Các chỉ mục phụ giúp cải thiện hiệu suất tìm kiếm cho các truy vấn không phải là chỉ mục chính.
#### 7.6.3. Cách Tạo và Quản Lý Chỉ Mục

**TẠO CHỈ MỤC INDEXES**

Ví dụ 1: Tạo chỉ mục duy nhất trên cột projname của bảng project:

```SQL
CREATE UNIQUE INDEX unique_nam ON project (projname);
```

Điều này đảm bảo không có hai hàng trong bảng `project` có cùng giá trị `projname`.

Ví dụ 2: Tạo chỉ mục không duy nhất trên các cột workdept và job của bảng employee:

```SQL
CREATE INDEX job_by_dpt ON employee (workdept, job);
```

Chỉ mục này giúp tăng tốc độ truy vấn cho các điều kiện lọc theo workdept và job.

**XÓA CHỈ MỤC INDEXES**

Để xóa một chỉ mục, sử dụng lệnh DROP INDEX. Ví dụ:

```SQL
DROP INDEX job_by_dpt;
```

#### 7.6.4. Các cân nhắc khi sử dụng indexes

- **Hiểu Cách Sử Dụng Cơ Sở Dữ Liệu**: Có cần xử lý giao dịch trực tuyến nặng hay chỉ lưu trữ và truy xuất dữ liệu lớn?

Ví dụ: Giả sử bạn có một cơ sở dữ liệu cho một hệ thống quản lý bán hàng. Nếu hệ thống chủ yếu được sử dụng cho giao dịch trực tuyến (OLTP) với nhiều thao tác chèn, cập nhật và xóa dữ liệu, bạn nên tối ưu hóa chỉ mục để phục vụ cho việc tìm kiếm và sắp xếp các bản ghi giao dịch nhanh chóng.

Chỉ mục phù hợp: Chỉ mục trên cột transaction_date trong bảng sales_transactions giúp nhanh chóng tìm các giao dịch theo ngày.

```SQL
CREATE INDEX idx_transaction_date ON sales_transactions (transaction_date);
```

- **Tìm Hiểu Các Truy Vấn Thường Xuyên**: Các truy vấn thường xuyên tham gia vào nhiều bảng hay lọc qua các cột cụ thể sẽ giúp bạn chọn loại chỉ mục phù hợp.

Ví dụ: Trong một ứng dụng báo cáo, bạn thường xuyên thực hiện truy vấn để tìm tất cả các đơn hàng theo trạng thái và ngày đặt hàng.

Chỉ mục phù hợp: Chỉ mục kết hợp trên các cột order_status và order_date trong bảng orders có thể cải thiện hiệu suất cho các truy vấn này.

```SQL
CREATE INDEX idx_order_status_date ON orders (order_status, order_date);
```

- **Tính Chất Các Cột**: Loại dữ liệu trong các cột, giá trị có duy nhất không, đều là yếu tố quan trọng khi chọn loại chỉ mục.

Ví dụ: Bạn có một bảng users với cột email và age. Cột email là duy nhất cho mỗi người dùng, trong khi cột age có thể chứa nhiều giá trị giống nhau.

Chỉ mục phù hợp: Tạo chỉ mục duy nhất trên cột email vì mỗi giá trị phải là duy nhất và tạo chỉ mục không duy nhất trên cột age để cải thiện truy vấn theo độ tuổi.

```SQL
-- Chỉ mục duy nhất cho cột email
CREATE UNIQUE INDEX idx_unique_email ON users (email);

-- Chỉ mục không duy nhất cho cột age
CREATE INDEX idx_age ON users (age);
```

#### 7.6.5. Tùy chọn tối ưu indexes

- **Chỉ Mục Clustered vs Non-Clustered**: Chỉ mục clustered sắp xếp dữ liệu trong bảng theo thứ tự của chỉ mục, trong khi chỉ mục non-clustered giữ bản sao của dữ liệu và các liên kết đến các hàng gốc.

**CLUSTERED**

Ví dụ: Khi tạo chỉ mục, bạn có thể sử dụng các tùy chọn tối ưu hóa để cải thiện hiệu suất, chẳng hạn như chỉ mục FULLTEXT cho các tìm kiếm văn bản hoặc PARTITIONED cho các bảng phân vùng lớn.

Chỉ mục `FULLTEXT`:
Được sử dụng cho tìm kiếm văn bản toàn văn trong cột văn bản lớn.

```SQL
CREATE FULLTEXT INDEX idx_fulltext_description ON products (description);
```

Chỉ mục `PARTITIONED`:
Phân vùng chỉ mục trên các phần dữ liệu khác nhau để cải thiện hiệu suất truy vấn.

```SQL
CREATE INDEX idx_partitioned_order_date ON orders (order_date)
PARTITION BY RANGE (order_date);
```

Chỉ mục phân vùng giúp tăng hiệu suất truy vấn bằng cách chia nhỏ dữ liệu thành các phần dễ quản lý hơn. Ví dụ, nếu bạn có một bảng orders rất lớn với dữ liệu từ nhiều năm, việc phân vùng dữ liệu theo cột order_date sẽ cho phép hệ thống cơ sở dữ liệu tìm kiếm nhanh hơn trong các phân vùng nhỏ hơn thay vì quét toàn bộ bảng.

Phân vùng theo `RANGE` giúp quản lý dữ liệu theo các khoảng thời gian, chẳng hạn như hàng tháng hoặc hàng năm, tùy thuộc vào cách phân vùng được cấu hình cụ thể.

**NON-CLUSTERED**

Ví dụ: Chỉ mục non-clustered tạo một bản sao của dữ liệu với các liên kết đến các hàng gốc. Một bảng có thể có nhiều chỉ mục non-clustered.

```SQL
CREATE NONCLUSTERED INDEX idx_nonclustered_customer_name ON customers (customer_name);
```

Chỉ mục không phân nhóm giúp tăng hiệu suất truy vấn bằng cách tạo ra một cấu trúc dữ liệu tách biệt để tìm kiếm các giá trị trong cột customer_name. Khi thực hiện các truy vấn tìm kiếm hoặc lọc dựa trên cột customer_name, cơ sở dữ liệu có thể sử dụng chỉ mục này để nhanh chóng tìm ra các hàng phù hợp, thay vì quét toàn bộ bảng.

Trong một chỉ mục không phân nhóm, chỉ mục chứa các giá trị của cột chỉ mục và các liên kết đến các hàng gốc trong bảng. Điều này cho phép chỉ mục tìm kiếm nhanh mà không làm thay đổi thứ tự của dữ liệu trong bảng

- **Tùy Chọn Indexing**: Sử dụng các tùy chọn như ONLINE khi tạo chỉ mục trên bảng lớn, để cho phép hoạt động đồng thời trong khi chỉ mục được xây dựng.

Ví dụ: Khi tạo chỉ mục trên bảng lớn, bạn có thể sử dụng tùy chọn ONLINE để cho phép các hoạt động khác trên bảng tiếp tục trong khi chỉ mục được xây dựng, giúp giảm thiểu gián đoạn.

```SQL
CREATE INDEX idx_online_product_name ON products (product_name) ONLINE;
```

Trong ví dụ này, tùy chọn `ONLINE` giúp xây dựng chỉ mục `idx_online_product_name` mà không làm gián đoạn các hoạt động đọc/ghi trên bảng `products`.

- **Vị Trí Lưu Trữ Chỉ Mục**: Đặt chỉ mục trên nhóm lưu trữ khác với bảng chính có thể cải thiện hiệu suất bằng cách giảm độ trễ đọc/ghi đĩa.

Ví dụ: Đặt chỉ mục trên nhóm lưu trữ khác với bảng chính có thể cải thiện hiệu suất đọc/ghi đĩa.

```SQL
CREATE INDEX idx_storage_location ON orders (order_date)
STORAGE GROUP = index_storage_group;
```

Trong ví dụ trên, chỉ mục `idx_storage_location` được lưu trữ trên nhóm lưu trữ `index_storage_group` khác với nhóm lưu trữ chính của bảng `orders`, giúp giảm độ trễ khi thực hiện các thao tác đọc/ghi.

# Module 4

## 8. Troubleshooting and Automation

### 8.1. Trouble shooting common issues

Các vấn đề thường gặp là:

- **Hiệu Suất Kém**: Truy vấn chạy chậm hoặc ứng dụng gặp sự cố khi kết nối với cơ sở dữ liệu. Ví dụ, việc đọc và ghi dữ liệu từ đĩa chậm có thể do phần cứng không đủ mạnh hoặc do thiết kế truy vấn chưa tối ưu.
- **Cấu Hình Sai**: Máy chủ hoặc cơ sở dữ liệu được cấu hình sai có thể dẫn đến hiệu suất thấp, lỗi hoặc thậm chí làm hỏng cơ sở dữ liệu. Ví dụ, nếu giới hạn số kết nối quá thấp, cơ sở dữ liệu sẽ không thể đáp ứng được nhiều người dùng cùng lúc.
- **Kết Nối Kém**: Sự cố về mạng hoặc cấu hình sai về thông tin kết nối có thể gây ra các lỗi khi người dùng hoặc ứng dụng cố gắng truy cập cơ sở dữ liệu.

Cách giải quyết các vấn đề phổ biến:

- **Hiệu Suất Chậm**: Các nguyên nhân có thể bao gồm phần cứng không đủ, cấu hình không hợp lý, hoặc các truy vấn được viết không hiệu quả. Các giải pháp bao gồm việc nâng cấp phần cứng (RAM, CPU, đĩa cứng), điều chỉnh cấu hình cơ sở dữ liệu (bộ nhớ đệm, chỉ mục), và tối ưu hóa các truy vấn.
- **Cấu Hình Sai**: Để giải quyết cấu hình sai, cần kiểm tra các thiết lập cơ bản như số lượng kết nối được phép, bộ nhớ đệm, chỉ mục, và xem xét tăng cường các thông số này để cải thiện hiệu suất.
- **Kết Nối Kém**: Các bước khắc phục bao gồm kiểm tra tính khả dụng của máy chủ cơ sở dữ liệu, xác minh rằng máy chủ và phiên bản cơ sở dữ liệu đang chạy chính xác, và kiểm tra thông tin đăng nhập và cấu hình trên client (tên người dùng, mật khẩu, địa chỉ IP).

### 8.2. Tool for issue supporting

- **Giám Sát Hiệu Suất**: Sử dụng công cụ giám sát như bảng điều khiển (dashboard) để theo dõi hiệu suất cơ sở dữ liệu theo thời gian thực, phát hiện các vấn đề tiềm ẩn và có biện pháp khắc phục kịp thời.
- **Nhật Ký Cơ Sở Dữ Liệu và Máy Chủ**: Các nhật ký ghi lại các lỗi, sự cố, và thời gian xảy ra lỗi, giúp xác định nguyên nhân gốc rễ của vấn đề và giúp bạn đưa ra giải pháp chính xác.

### 8.3. Practical examples

- **Hiệu Suất Kém**: Một ứng dụng thương mại điện tử gặp sự cố khi quá nhiều người dùng truy cập cùng một lúc, dẫn đến thời gian phản hồi truy vấn chậm. Giải pháp có thể là nâng cấp CPU và RAM của máy chủ cơ sở dữ liệu và tối ưu hóa các truy vấn truy xuất dữ liệu.
- **Cấu Hình Sai**: Một bảng không có đủ chỉ mục dẫn đến việc truy vấn tìm kiếm mất nhiều thời gian. Giải pháp là tạo các chỉ mục phù hợp trên các cột được truy vấn thường xuyên.
- **Kết Nối Kém**: Một người dùng không thể kết nối với cơ sở dữ liệu do địa chỉ IP của máy chủ bị cấu hình sai. Sau khi cập nhật lại địa chỉ IP chính xác, người dùng có thể kết nối bình thường.

### 8.4. Using status variable, error codes, and documentations

**Kiểm Tra Trạng Thái Máy Chủ**

Truy vấn trạng thái cơ sở dữ liệu: Bạn có thể sử dụng các lệnh dòng lệnh hoặc giao diện đồ họa để kiểm tra tình trạng sức khỏe và hoạt động của cơ sở dữ liệu. Ví dụ:

- **MySQL**: Sử dụng lệnh `SHOW STATUS` hoặc `SERVICE MYSQL STATUS`.
- **Db2**: Dùng lệnh `db2pd`.
- **PostgreSQL**: Dùng lệnh `PG_ISREADY` để kiểm tra trạng thái kết nối.

**Biến Trạng Thái**

Các cơ sở dữ liệu sử dụng nhiều biến trạng thái để cung cấp thông tin về hoạt động. Biến trạng thái có thể là `GLOBAL` (toàn cục) hoặc `SESSION` (phiên hiện tại).

Ví dụ: `Aborted_connects` là biến toàn cục, trong khi `Bytes_received` là biến phiên.

MySQL:

```SQL
SHOW GLOBAL STATUS;
```

Lệnh này sẽ trả về tất cả các biến trạng thái toàn cục của máy chủ MySQL.

```SQL
SHOW SESSION STATUS;
```

Lệnh này sẽ trả về tất cả các biến trạng thái phiên của kết nối hiện tại.

```SQL
SHOW STATUS LIKE 'Connections%';
```

Lệnh này sẽ chỉ hiển thị các biến trạng thái mà tên của chúng bắt đầu bằng "Connections".

PostgreSQL:

```SQL
SELECT * FROM pg_stat_activity;
```

Lệnh này sẽ trả về thông tin về tất cả các kết nối hiện tại đến cơ sở dữ liệu.

```SQL
SELECT * FROM pg_settings;
```

Lệnh này sẽ cung cấp thông tin về các cấu hình hiện tại của cơ sở dữ liệu.

```sh
pg_isready
```

Lệnh này được sử dụng từ dòng lệnh để kiểm tra trạng thái kết nối của PostgreSQL.


### 8.5. Giải mã lỗi và sử dụng tài liệu

**Nhật Ký (Logs)**: Nhật ký hệ điều hành và nhật ký cơ sở dữ liệu giúp xác định thời điểm và vị trí lỗi xảy ra. Một số loại nhật ký phổ biến là:

- Error Log: Tạo ra mỗi khi SQL Server khởi động.
- Event Log: Ghi lại các sự kiện và lỗi.
- Default Trace Log: Theo dõi các thay đổi cấu hình cơ sở dữ liệu.

**Mã Lỗi**: Thông báo lỗi thường chứa mã ID, tên quy trình gây ra lỗi, trạng thái cơ sở dữ liệu tại thời điểm lỗi, và mức độ nghiêm trọng của vấn đề.

**Tài Liệu Hướng Dẫn**: Sau khi thu thập thông tin về lỗi, bước tiếp theo là tra cứu mã lỗi trên các trang web tài liệu chính thức. Một số nguồn tài liệu phổ biến bao gồm:

- Db2: ibm.com/docs/db2
- PostgreSQL: postgresql.org/docs
- Microsoft SQL: docs.microsoft.com/sql
- MySQL: dev.mysql.com/doc/

### 8.6. Using logs for troubleshooting

Mục đích của Dianostic Logs

Diagnostic logs, hay còn gọi là logs khắc phục sự cố, là các bản ghi theo dõi hoạt động của hệ thống hoặc ứng dụng, chứa thông tin về các sự kiện, lỗi, và tình trạng hệ thống. Chúng cung cấp thông tin quan trọng để xác định nguyên nhân và khắc phục sự cố khi xảy ra vấn đề.

**CÁC LOẠI DIAGNOSTIC LOGS**

1. Logs của Máy Chủ (Server Logs):
- **Db2 Diagnostic Log (db2diag.log)**: Ghi lại thông tin về hoạt động của máy chủ Db2, lỗi, và sự kiện.
- **PostgreSQL Logs**: Ghi lại các sự kiện như khởi động, tắt máy, lỗi, và vấn đề kết nối.
2. Logs của Ứng Dụng và Cơ Sở Dữ Liệu:
- **MySQL General Query Log**: Ghi lại tất cả các kết nối và truy vấn từ khách hàng.
- **MySQL Slow Query Log**: Ghi lại các truy vấn mất nhiều thời gian để thực thi.
- **MySQL Error Log**: Ghi lại các thông báo lỗi và cảnh báo từ MySQL server.
3. Logs của Hệ Điều Hành và Phần Cứng:
- **Windows Event Log**: Ghi lại các sự kiện hệ thống, bao gồm lỗi và cảnh báo.
- **Syslog trên Linux/Unix**: Ghi lại các sự kiện và lỗi từ hệ thống.

**THÔNG TIN TRONG DIAGNOSTIC LOGS**

- **Loại và Mức Độ Vấn Đề**: Ví dụ: sự kiện, thông tin, cảnh báo, lỗi.
- **Mã lỗi và Thông báo**: Chi tiết về lỗi xảy ra.
- **Vị trí, URL hoặc Subsystem**: Nơi xảy ra lỗi.
- **Thời gian (Timestamp)**: Thời điểm lỗi hoặc sự kiện xảy ra.
- **IP và User Agent**: Thông tin về người dùng hoặc hệ thống gây ra lỗi.
- **Thông tin Bổ Sung**: Có thể bao gồm thông tin chi tiết hơn tùy vào sự kiện hoặc lỗi.

**VÍ DỤ**

1. **Db2 Diagnostic Log: Một mục trong `db2diag.log` có thể chứa thông tin như:**

```vbnet
2024-08-17-12:34:56.789123+00 I1234560A1234 LEVEL: Event
PID: 1234 TID: 5678 PROC: db2start.exe
INSTANCE: db2inst1 NODE: 000
FUNCTION: DB2 UDB, SQLEventMonitor, sqleInitEventMonitor, probe:999
MESSAGE: Initialization of the DB2 Event Monitor completed successfully.
```

Trong log này:

- Timestamp: 2024-08-17-12:34:56.789123+00 - Thời điểm khi sự kiện hoặc lỗi xảy ra. Đây là thông tin quan trọng để xác định khi vấn đề xảy ra.
- Level: Event - Loại thông báo. Trong trường hợp này là sự kiện, cho biết một sự kiện bình thường đã xảy ra, không phải lỗi.
- PID: 1234 - Process ID, số nhận diện của tiến trình đang chạy. Thông tin này giúp xác định tiến trình cụ thể liên quan đến log.
- TID: 5678 - Thread ID, số nhận diện của luồng xử lý. Giúp phân biệt các luồng trong tiến trình.
- PROC: db2start.exe - Tên tiến trình hoặc ứng dụng đang chạy. Trong ví dụ này, đó là tiến trình khởi động Db2.
- INSTANCE: db2inst1 - Tên instance của Db2. Cho biết instance nào đang xử lý yêu cầu này.
- NODE: 000 - ID của node trong môi trường phân tán. Trong trường hợp đơn giản, giá trị này có thể là 000.
- FUNCTION: DB2 UDB, SQLEventMonitor, sqleInitEventMonitor, probe:999 - Chức năng và thông tin chi tiết về hoạt động. Cung cấp ngữ cảnh về loại sự kiện và phần mềm liên quan.
- MESSAGE: Initialization of the DB2 Event Monitor completed successfully. - Thông báo chi tiết về sự kiện hoặc lỗi. Trong trường hợp này, thông báo cho biết rằng việc khởi tạo Event Monitor đã hoàn tất thành công.

2. **PostgreSQL Logs: Một mục trong log có thể chứa thông tin như:**

```yaml
2024-08-17 12:34:56 UTC [12345] LOG:  connection received: host=127.0.0.1 port=5432
2024-08-17 12:34:56 UTC [12345] ERROR:  missing semicolon after SQL statement
```

Trong đó:

- Timestamp: 2024-08-17 12:34:56 UTC - Thời điểm ghi nhận sự kiện trong log.
- PID: [12345] - Process ID của tiến trình PostgreSQL đang xử lý sự kiện.
- LOG/ERROR: LOG và ERROR - Loại thông báo. LOG cho biết một sự kiện thông thường, còn ERROR báo lỗi.
- Message:
  - connection received: host=127.0.0.1 port=5432 - Thông báo cho biết có một kết nối đến cơ sở dữ liệu từ địa chỉ IP 127.0.0.1 qua cổng 5432.
  - missing semicolon after SQL statement - Thông báo lỗi cho biết cú pháp SQL không hợp lệ do thiếu dấu chấm phẩy sau câu lệnh SQL.

3. **MySQL Error Log: Một mục trong log có thể chứa thông tin như:**

```bash
2024-08-17T12:34:56.789123Z 12345 [ERROR] /usr/sbin/mysqld: Table 'mydb.mytable' doesn't exist
```

Trong đó:

- Timestamp: 2024-08-17T12:34:56.789123Z - Thời gian ghi nhận lỗi, định dạng là UTC.
- PID: 12345 - Process ID của tiến trình MySQL đang xử lý lỗi.
- Log Level: [ERROR] - Loại thông báo, cho biết đây là lỗi nghiêm trọng.
- Message: /usr/sbin/mysqld: Table 'mydb.mytable' doesn't exist - Thông báo lỗi chi tiết. Trong trường hợp này, lỗi cho biết bảng mytable trong cơ sở dữ liệu mydb không tồn tại.

### 8.7 Configuring and accessing logs

- **Db2**: Có thể cấu hình vị trí và mức độ chi tiết của logs thông qua các tham số cấu hình.
- **PostgreSQL**: Sử dụng `postgresql.conf` để cấu hình `log_destination`, `log_directory`, và `log_filename`.
- **MySQL**: Sử dụng tham số cấu hình `log_error` để chỉ định tên file log lỗi.

### 8.8. Automating Database tasks

#### 8.8.1 Automating database

Tự động hóa cơ sở dữ liệu sử dụng các quy trình không cần giám sát và các quy trình tự cập nhật để thực hiện các nhiệm vụ quản trị cơ sở dữ liệu. Điều này giúp giảm lỗi triển khai, cải thiện độ tin cậy và tốc độ khi thực hiện thay đổi. Một số nhiệm vụ tự động hóa thường gặp bao gồm:

- **Kiểm tra sức khỏe cơ sở dữ liệu**: Kiểm tra tình trạng và hiệu quả của hệ thống cơ sở dữ liệu.
- **Dọn dẹp log file cảnh báo**: Xóa các log file chứa thông báo và lỗi.
- **Dọn dẹp file trace**: Xóa các file backup chứa ảnh chụp quá trình thực thi và các module đã tải.
- **Thống kê từ điển dữ liệu**: Thu thập thông tin về các yếu tố dữ liệu đang được sử dụng trong cơ sở dữ liệu.

#### 8.8.2. Benefit of automation

- **Tăng năng suất**: Giảm thiểu công việc lặp đi lặp lại cho nhân viên.
- **Cải thiện chất lượng**: Giảm khả năng lỗi và cải thiện sự đồng nhất của quy trình.
- **Tăng tính nhất quán**: Đảm bảo rằng các quy trình và kết quả đều ổn định và đồng nhất.
- **Giải phóng nguồn lực**: Cho phép nhân viên tập trung vào các nhiệm vụ quan trọng hơn.

#### 8.8.3. Benefit of scripting automation

- **Dễ dàng triển khai và bảo trì**: Các script có thể được viết để thực hiện các công việc thường xuyên mà không cần phát triển và duy trì script tùy chỉnh mỗi lần.
- **Quản lý phiên bản**: Các script có thể được quản lý bằng hệ thống quản lý phiên bản để theo dõi và lưu trữ lịch sử thay đổi.
- **Tự động hóa các nhiệm vụ**: Các nhiệm vụ như sao lưu, xóa log, và phục hồi cơ sở dữ liệu có thể được tự động hóa bằng các script.

#### 8.8.4. Tools and methods of automation

- **Công cụ tích hợp sẵn**: Nhiều cơ sở dữ liệu cung cấp công cụ tự động hóa tích hợp sẵn.
- **Tạo Script**: Các DBA có thể viết script bằng các ngôn ngữ lập trình như Python, shell script, hoặc các ngôn ngữ khác để tự động hóa các nhiệm vụ quản trị cơ sở dữ liệu.
- **Lịch Trình Tự Động**: Sử dụng công cụ lập lịch như cron jobs để thực hiện các nhiệm vụ tự động tại thời gian cụ thể.

Lợi ích:

- Giảm chi phí và tăng tốc độ kiểm thử: Kiểm thử tự động nhanh hơn và rẻ hơn so với kiểm thử thủ công.
- Tăng độ sâu và phạm vi kiểm thử: Kiểm thử tự động có thể bao quát nhiều khía cạnh hơn và giúp cải thiện chất lượng và bảo mật của hệ thống cơ sở dữ liệu.
- Kiểm tra tính toàn vẹn và nhất quán dữ liệu: Đảm bảo rằng các giá trị và thông tin trong cơ sở dữ liệu là hợp lệ và nhất quán.

### 8.9. Automating Reports and Alerts

#### 8.9.1. Difference of Reports, Nofitications and Alerts

**Báo Cáo**: Cung cấp cái nhìn tổng quan về sức khỏe cơ sở dữ liệu theo định kỳ. Ví dụ: số lượng người dùng kết nối thành công hoặc thất bại, dung lượng sử dụng và tỷ lệ tăng trưởng, số lượng truy vấn thực hiện. Báo cáo có thể được cấu hình để chạy hàng ngày, hàng tuần hoặc hàng tháng, tùy thuộc vào nhu cầu.

**Thông Báo**: Được sử dụng khi có sự kiện cần theo dõi nhưng không yêu cầu sự chú ý ngay lập tức. Ví dụ: thông báo khi người dùng cố gắng đăng nhập không thành công. Thông báo có thể được gửi qua SMS, email hoặc qua bảng điều khiển.

**Cảnh Báo**: Thông báo về các vấn đề cần sự chú ý khẩn cấp. Ví dụ: dung lượng đĩa thấp nghiêm trọng, lỗi trong log file, hoặc các tác vụ đã lên lịch không hoàn thành. Cảnh báo thường có các ngưỡng cảnh báo và ngưỡng quan trọng để phản ánh mức độ nghiêm trọng của sự kiện.

#### 8.9.2. Benefit

**Báo Cáo**: Giúp theo dõi và dự đoán các vấn đề tiềm ẩn trước khi chúng trở nên nghiêm trọng. Cung cấp thông tin để cải thiện hiệu suất và kế hoạch dự phòng.

**Thông Báo**: Cung cấp thông tin về các sự kiện có thể trở thành vấn đề lớn nếu không được giải quyết. Giúp DBAs theo dõi và phân tích các sự kiện để phát hiện các hành vi đáng ngờ hoặc sự cố tiềm ẩn.

**Cảnh Báo**: Cung cấp thông tin ngay lập tức về các vấn đề nghiêm trọng, giúp DBAs có thể phản ứng nhanh chóng để giải quyết các vấn đề quan trọng và tránh các sự cố nghiêm trọng.

#### 8.9.3. Automation

**Báo Cáo Tự Động**: Hầu hết các RDBMS cung cấp giao diện đồ họa để cấu hình nội dung và tần suất báo cáo. Bạn có thể tạo và cấu hình báo cáo tùy chỉnh hoặc sử dụng báo cáo mẫu có sẵn.

**Thông Báo và Cảnh Báo Tự Động**: Có thể cấu hình thông qua giao diện đồ họa, công cụ dòng lệnh, hoặc script. Các RDBMS thường cho phép thiết lập ngưỡng cảnh báo và thông báo để phù hợp với nhu cầu cụ thể của môi trường.

**Ngưỡng Cảnh Báo**: Thiết lập ngưỡng cảnh báo khi đạt 85% và cảnh báo quan trọng khi đạt 95%. Bạn có thể điều chỉnh các giá trị này phù hợp với môi trường của mình.

**Cấu Hình Hợp Lý**: Đánh giá và cấu hình các thông báo và cảnh báo để không bị quá tải và có thể phản ứng hiệu quả. Chỉ định những cảnh báo quan trọng và phù hợp với yêu cầu của hệ thống.

#### 8.10. Hands-on

[Instruction](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAyMzFFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvTXlTUUwvTGFiJTIwLSUyMEF1dG9tYXRlJTIwQmFja3VwJTIwaW4lMjBNeVNRTC9BdXRvbWF0aW5nU1FMVGFza3MubWQiLCJ0b29sX3R5cGUiOiJ0aGVpYWRvY2tlciIsImFkbWluIjpmYWxzZSwiaWF0IjoxNzIxMzc4NDM2fQ.WqzZNcHpssAlYj375SXU4mGurNWIbL4NSFAwt9En9qs)

