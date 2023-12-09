SELECT
    c.login AS courier_login,
    COUNT(*) AS orders_in_delivery
FROM
    "Couriers" AS c
    INNER JOIN "Orders" AS o ON c.id = o."courierId"
WHERE
    o."inDelivery" = TRUE
GROUP BY
    c.login;