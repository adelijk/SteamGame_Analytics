WITH fct_cte AS (
    SELECT 
        {{ dbt_utils.generate_surrogate_key(['g.id', 'n.user_id']) }} as fct_id,
        g.id as game_id,
        n.user_id
    FROM
        {{ ref('steam_games') }} g
    INNER JOIN 
        {{ ref('steam_new') }} n 
    ON 
        g.id = n.product_id
)

SELECT 
    f.fct_id,
    f.game_id,
    f.user_id
FROM 
    fct_cte f
INNER JOIN 
    {{ ref('dim_games') }} g 
ON 
    g.game_id = f.game_id
INNER JOIN 
    {{ ref('dim_user') }} u 
ON 
    u.user_id = f.user_id
