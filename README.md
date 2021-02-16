# Cooks-playground-api

## CICD
### Github actions


## Test

## DB Tables
### Ingredents
> * id
> * image_urls
> * name_kr
> * desc_kr
> * name_en
> * desc_en
> * product_urls = {coupang: "coupang_url", naver: "url_naver"}

### Articles
> * id
> * title_kr
> * title_en
> * desc_kr
> * desc_en
> * cooking_time
> * user_id
> * comment_id
> * created_at
> * updated_at

### Comments
> * id
> * text
> * user_id
> * created_at
> * updated_at
> * 

### User
> * uid
> * user_name
> * password
> * profile_text
> * profile_image_url
> * created_at

### Logs
> * id
> * resource
> * resource_number
> * log_datetime
> 
