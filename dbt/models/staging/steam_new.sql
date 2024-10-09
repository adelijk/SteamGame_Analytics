SELECT 
    username,
    CAST(hours as integer) as hours,
    products,
    product_id,
    page_order,
    cast(date as date),
    text,
    user_id
FROM {{ source('steam_data' , 'steam_new') }} sn
