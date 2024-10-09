SELECT 
    id as game_id,
    publisher,
    genres.list as genres,
    app_name AS game_name,
    SAFE.PARSE_DATE('%Y-%m-%d', release_date) AS date,
    CAST(price AS INTEGER) AS price,
    specs,
    early_access,
    sentiment,
    metascore 
FROM 
    {{ source('steam_data' , 'steam_games')}} 
