insert into foi_user(username) values ('Bob') on conflict do nothing;
insert into foi_user(username) values ('Alice') on conflict do nothing;

