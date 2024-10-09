SELECT 
    user_id,
    username,
    hours,
    products,
    page_order,
    date,
    text
FROM {{ ref('steam_new') }}
