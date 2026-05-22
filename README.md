# lk_religion

Analyses of Sri Lanka's religious demographics, comparing the **2012 Census** and **2024 Census**.

Each analysis now lives in its own folder under [`analyses/`](analyses/), together with its own README, workflow script, and related data files. The sections below are copied from those child READMEs.

- [`analyses/a0-national-population-by-religion/`](analyses/a0-national-population-by-religion/)
- [`analyses/a1-religion-by-country-key-trends/`](analyses/a1-religion-by-country-key-trends/)
- [`analyses/a2-religion-by-province-key-trends/`](analyses/a2-religion-by-province-key-trends/)
- [`analyses/a3-religion-by-district-key-trends/`](analyses/a3-religion-by-district-key-trends/)
- [`analyses/a4-religion-by-dsd-key-trends/`](analyses/a4-religion-by-dsd-key-trends/)

---

## A0. National Population by Religion

![A0 representative chart](analyses/a0-national-population-by-religion/chart.png)

### Commentary

- Sri Lanka's total population grew from **20,357,776** (2012) to **21,781,800** (2024), an increase of **+1,424,024** at an annual rate of **+0.57%**.
- **Buddhism** remains the dominant religion, accounting for **69.8%** of the population in 2024, growing at **+0.53%** per year.
- **Islam** has the fastest growth rate among major religions at **+1.45%** per year, reaching a share of **10.7%** in 2024.
- **Roman Catholic** and **Other Christian** communities show slight declines over the period.

---

## A1. Religion by Country: Key Trends

![A1 Country change maps](analyses/a1-religion-by-country-key-trends/chart.png)

Country labels show the **country name** and **change in share of population (pp)**. Countries are shaded by **change in share of population (pp)** from **blue (decline)** to **red (growth)**.

### Buddhist

*No countries exceed the **1.0pp** share-change threshold.*

### Hindu

*No countries exceed the **1.0pp** share-change threshold.*

### Islam


***Sri Lanka** gained the most share at **+1.1pp**.*

### Roman Catholic

*No countries exceed the **1.0pp** share-change threshold.*

### Other Christian

*No countries exceed the **1.0pp** share-change threshold.*

### Other

*No countries exceed the **1.0pp** share-change threshold.*

---

## A2. Religion by Province: Key Trends

![A2 Province change maps](analyses/a2-religion-by-province-key-trends/chart.png)

Province labels show the **province name** and **change in share of population (pp)**. Provinces are shaded by **change in share of population (pp)** from **blue (decline)** to **red (growth)**.

### Buddhist


***Eastern** saw the steepest share decline at **-1.1pp**.*

### Hindu


***Northern** saw the steepest share decline at **-2.3pp**.*

### Islam


***Eastern** gained the most share at **+2.7pp**. **North Western** had the smallest share gain at **+1.1pp**.*

### Roman Catholic


***North Western** saw the steepest share decline at **-1.1pp**.*

### Other Christian

*No provinces exceed the **1.0pp** share-change threshold.*

### Other

*No provinces exceed the **1.0pp** share-change threshold.*

---

## A3. Religion by District: Key Trends

![A3 District change maps](analyses/a3-religion-by-district-key-trends/chart.png)

District labels show the **district name** and **change in share of population (pp)**. Districts are shaded by **change in share of population (pp)** from **blue (decline)** to **red (growth)**.

### Buddhist


***Trincomalee** saw the steepest share decline at **-2.0pp**. **Ampara** had the largest absolute increase (**+24,749**).*

### Hindu


***Mannar** saw the steepest share decline at **-2.9pp**. **Batticaloa** had the largest absolute increase (**+35,954**).*

### Islam


***Mannar** gained the most share at **+10.8pp**. **Kegalle** had the smallest share gain at **+1.1pp**. **Ampara** had the largest absolute increase (**+57,909**).*

### Roman Catholic


***Mullaitivu** gained the most share at **+1.6pp**. **Mannar** saw the steepest share decline at **-6.0pp**. **Mannar** had the largest absolute increase (**+5,298**).*

### Other Christian


***Mullaitivu** gained the most share at **+1.2pp**.*

### Other

*No districts exceed the **1.0pp** share-change threshold.*

---

## A4. Religion by DSD: Key Trends

![A4 DSD change maps](analyses/a4-religion-by-dsd-key-trends/chart.png)

DSDs are shaded by **change in share of population (pp)** from **blue (decline)** to **red (growth)**. DSD labels are omitted due to map density.

*New, removed, and altered DSDs are excluded to avoid boundary-change artifacts.*

### Buddhist


***Vavuniya North** gained the most share at **+3.4pp**. **Dehiwala** saw the steepest share decline at **-7.9pp**. **Kaduwela** had the largest absolute increase (**+28,609**).*

### Hindu


***Wattala** gained the most share at **+3.9pp**. **Puthukkudiyiruppu** saw the steepest share decline at **-6.2pp**. **Puthukkudiyiruppu** had the largest absolute increase (**+10,864**).*

### Islam


***Musali** gained the most share at **+15.1pp**. **Rambewa** saw the steepest share decline at **-2.3pp**. **Kolonnawa** had the largest absolute increase (**+22,911**).*

### Roman Catholic


***Delft** gained the most share at **+6.6pp**. **Musali** saw the steepest share decline at **-11.8pp**. **Katana** had the largest absolute increase (**+6,528**).*

### Other Christian


***Koralai Pattu South** gained the most share at **+2.3pp**. **Dehiwala** saw the steepest share decline at **-1.4pp**. **Puthukkudiyiruppu** had the largest absolute increase (**+1,291**).*

### Other


***Kalpitiya** saw the steepest share decline at **-1.2pp**.*

---

*Data from the 2012 and 2024 Sri Lanka Census, accessed via [lanka_data](https://pypi.org/project/lanka-data/). Raw data and derived tables live in the corresponding directories under [`analyses/`](analyses/).*
