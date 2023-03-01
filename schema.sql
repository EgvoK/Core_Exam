drop table if exists categories;
drop table if exists expenditures;

create table categories(
    id integer primary key autoincrement,
    category_name text not null
);

create table expenditures(
    id integer primary key autoincrement,
    expenditure_name text not null,
    expenditure_date text not null,
    amount integer not null,
    category_id integer not null,
    foreign key (category_id) references categories(id)
);