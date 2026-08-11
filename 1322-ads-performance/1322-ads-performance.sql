# Write your MySQL query statement below
SELECT
    ad_id,
    ROUND(
        IF(
            SUM(action='Clicked') + SUM(action='Viewed') = 0,
            0,
            SUM(action='Clicked') * 100 /
            (
                SUM(action='Clicked')
                +
                SUM(action='Viewed')
            )
        ),
        2
    ) AS ctr
FROM Ads
GROUP BY ad_id
ORDER BY ctr DESC, ad_id;