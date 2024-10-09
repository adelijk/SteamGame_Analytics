SELECT 
    game_id,
    publisher,
    genres,
    game_name,
    developer,
    date,
    price,
    specs,
    early_access,
    sentiment,
    metascore
FROM
    {{ ref('steam_games') }}
WHERE 
    metascore IS NOT NULL
    AND publisher IS NOT NULL