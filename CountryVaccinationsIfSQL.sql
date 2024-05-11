UPDATE VaccinationData AS vd
SET vd.daily_vaccinations = (
    SELECT MEDIAN(daily_vaccinations)
    FROM VaccinationData
    WHERE country = vd.country
    AND daily_vaccinations IS NOT NULL
)
WHERE vd.daily_vaccinations IS NULL;

UPDATE VaccinationData
SET daily_vaccinations = 0
WHERE daily_vaccinations IS NULL;
