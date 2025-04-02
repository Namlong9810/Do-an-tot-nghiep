drop table transaction
-- xử lý với bảng dataset transaction
create table transaction(
	TransactionID varchar(10),
	WalletID varchar(10),
	UserID varchar(10),
	Amount Decimal,
	TransactionDate Timestamp,
	TransactionType transactionType,
	IP_address varchar(15),
	Frequency int,
	TransactionDuration float,
	PreviousTransactionDate Timestamp,
	Balance decimal,
	IsFraud int
)

create type transactionType as enum('credit', 'debit');

Copy transaction(TransactionID, WalletID, UserID, Amount, TransactionDate, TransactionType, IP_address, 
Frequency, TransactionDuration, PreviousTransactionDate, Balance, IsFraud)
From 'D:\java-mini-project\fraud_dataset.csv'
Delimiter ','
CSV HEADER;

select * from transaction 

select *
from transaction
where WalletID = 'W10'
order by UserID asc, IsFraud desc; 

select count (*) as total_data
from transaction
where isfraud = 0;
83698

Select WalletID,
		IsFraud,
		Count(Distinct UserID) as user_count,
		String_agg(distinct UserID, ',') as user_list
From transaction
Group by WalletId, IsFraud
having count(distinct UserID) > 1
Order By WalletID asc, isfraud desc;

--  tìm các giải địa chỉ private
select * from transaction
where IP_Address like'192%'

select * from transaction
where IP_Address 