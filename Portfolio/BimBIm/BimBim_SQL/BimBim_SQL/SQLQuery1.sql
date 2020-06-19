create table BimBim_Dataset (
	collectType varchar(100),
	shopName varchar(100),
	locations varchar(100),
	amountOfOrder int,
	nameInOrder varchar(100),
	shipperName varchar(100),
	shopTotal int,
	statusType varchar(100),
	timeCollect datetime,
	paymentType varchar(100)
)

go

insert into BimBim_Dataset (collectType,shopName,locations,amountOfOrder,shipperName,shopTotal,statusType,timeCollect)
values (